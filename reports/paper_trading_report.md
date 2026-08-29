# Paper trading automatico KuCoin

Generato: 2026-08-29T05:33:23+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-29T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-29T05:05:29+00:00 | 2026-08-29T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-29T04:45:00+00:00 | 2026-08-29T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-29T04:00:00+00:00 | 2026-08-29T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-29T00:00:00+00:00 | 2026-08-29T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Partial 1R V1 | DOGE | 60m | SHORT | -7,78 | 5,00 | 0,00 | OPENED | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | DOGE | 60m | SHORT | -7,78 | 5,00 | 0,00 | OPENED | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | PEPE | 60m | SHORT | -6,25 | 5,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 5,09 | 6,00 | 0,91 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -3,78 | 6,00 | 2,22 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,61 | 6,00 | 3,39 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 2,44 | 6,00 | 3,56 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -1,58 | 6,00 | 4,42 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,62 | 6,00 | 5,38 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -0,35 | 6,00 | 5,65 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,19 | 6,00 | 5,81 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| 1H Fast No Pepe V1 | TRUMP | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | TRUMP | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | TRUMP | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | TRUMP | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | TRUMP | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | TRUMP | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Mfe Lock V1 | TRUMP | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | TRUMP | 60m | LONG | 9,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Donchian 1H Gb20 120R V1 | TRUMP | 60m | LONG | 9,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.900,13 | -1,00% | €151,78 | €3.000,00 | 5,06% | 6 | 54 | 38,89% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 54 | 2432 | PRIME INDICAZIONI | 100 (mancano 46) |

- Trade del Principale 4H chiusi: **54**; win rate **38,89%**; profit factor **0,87**.
- Expectancy: **€-3,54** per trade; P&L netto: **€-191,01**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.900,13 | €704,83 | €2.114,50 | €197,39 | €92,25 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.310,16 | €1.330,78 | €3.992,35 | €226,21 | €24,01 |
| TEST | Benchmark Donchian breakout 1H | 5 | €11.206,61 | €2.794,96 | €5.589,91 | €223,74 | €18,88 |
| TEST | Scanner Top 5 Long 1H | 4 | €11.028,11 | €858,91 | €1.717,82 | €163,75 | €74,18 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.015,85 | €1.837,10 | €3.674,20 | €167,85 | €-41,76 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.942,77 | €2.729,15 | €5.458,31 | €218,47 | €18,44 |
| TEST | Main Side Regime Guard V1 | 6 | €10.921,58 | €609,79 | €1.829,37 | €163,42 | €72,90 |
| TEST | Combo Adaptive | 6 | €10.607,41 | €2.167,22 | €4.334,45 | €212,31 | €-4,15 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.528,26 | €1.900,98 | €5.702,93 | €211,08 | €-23,95 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.515,97 | €1.280,06 | €3.840,19 | €210,32 | €2,00 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.460,62 | €1.888,76 | €5.666,29 | €209,72 | €-23,80 |
| TEST | Ampia 4H | 8 | €10.401,14 | €1.071,19 | €2.142,37 | €207,40 | €121,72 |
| TEST | Combo Adaptive Long Only V1 | 4 | €10.401,12 | €2.025,96 | €4.051,91 | €155,53 | €-4,89 |
| TEST | Rapida 1H V2 | 3 | €10.396,81 | €1.793,88 | €5.381,63 | €155,57 | €40,53 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €10.326,59 | €1.067,00 | €2.133,99 | €155,00 | €-23,92 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.313,79 | €1.944,24 | €5.832,71 | €207,22 | €-19,62 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.308,62 | €801,82 | €1.603,64 | €152,69 | €69,35 |
| TEST | Sol Donchian 1H | 0 | €10.305,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.305,34 | €2.360,29 | €7.080,87 | €152,94 | €41,81 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 5 | €10.254,10 | €3.258,24 | €9.774,72 | €205,75 | €40,06 |
| TEST | 1H Fast Tp2 V1 | 5 | €10.243,76 | €1.416,74 | €4.250,21 | €155,10 | €-24,11 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.228,07 | €407,92 | €815,83 | €51,22 | €-14,64 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.222,14 | €1.774,14 | €3.548,28 | €152,62 | €69,45 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.216,16 | €1.773,10 | €3.546,20 | €152,53 | €69,41 |
| TEST | Combo Adaptive Partial 1R V1 | 6 | €10.212,76 | €2.001,23 | €4.002,45 | €154,39 | €135,74 |
| TEST | Scanner Top10 Long | 5 | €10.211,23 | €2.249,29 | €4.498,58 | €152,82 | €68,33 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.194,81 | €449,62 | €899,24 | €50,98 | €-1,07 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.177,93 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €10.173,13 | €2.385,80 | €7.157,41 | €152,16 | €30,63 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.140,30 | €281,35 | €844,05 | €101,29 | €31,48 |
| TEST | 1H Fast Nohigh Cap75 V1 | 6 | €10.139,89 | €1.168,35 | €3.505,05 | €199,19 | €23,59 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.092,76 | €439,17 | €878,34 | €50,55 | €-15,76 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 3 | €10.085,51 | €282,69 | €848,06 | €99,85 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.081,13 | €775,58 | €1.551,16 | €0,00 | €51,84 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.033,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €10.013,20 | €835,22 | €2.505,66 | €49,96 | €22,36 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.988,31 | €687,72 | €2.063,16 | €49,94 | €0,56 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.959,74 | €478,97 | €957,94 | €49,65 | €29,65 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.939,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €9.924,24 | €768,73 | €2.306,18 | €49,62 | €0,62 |
| TEST | Scanner Top15 Long | 6 | €9.919,55 | €1.651,53 | €3.303,06 | €194,30 | €67,26 |
| TEST | Scanner Top20 Long | 6 | €9.919,55 | €1.651,53 | €3.303,06 | €194,30 | €67,26 |
| TEST | Combo Scanner | 5 | €9.915,66 | €1.870,15 | €3.740,29 | €196,29 | €78,83 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 6 | €9.887,57 | €1.139,28 | €3.417,83 | €194,23 | €23,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.873,73 | €345,61 | €691,22 | €49,80 | €-22,91 |
| TEST | Eth Adaptive 1H | 0 | €9.873,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.852,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.839,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €9.814,68 | €825,99 | €2.477,98 | €145,33 | €0,00 |
| TEST | Forza relativa 1H V2 | 5 | €9.807,68 | €981,41 | €1.962,83 | €98,38 | €67,65 |
| TEST | Eth Ema 1H | 0 | €9.799,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.785,26 | €1.534,40 | €3.068,79 | €147,60 | €-22,70 |
| TEST | Btc Ema 1H | 1 | €9.777,64 | €1.131,88 | €3.395,64 | €48,90 | €0,24 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.767,92 | €1.964,50 | €5.893,51 | €195,57 | €-9,21 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.749,54 | €341,26 | €682,52 | €49,17 | €-22,62 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.727,35 | €1.858,38 | €5.575,13 | €195,00 | €2,62 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.720,03 | €1.225,31 | €3.675,94 | €145,47 | €65,01 |
| TEST | Eth Donchian 1H | 0 | €9.709,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.694,76 | €1.707,76 | €3.415,51 | €145,01 | €44,15 |
| TEST | Global Confluence puro 1H | 1 | €9.689,15 | €964,56 | €1.929,13 | €48,40 | €10,88 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.684,46 | €1.421,82 | €4.265,46 | €194,20 | €-23,81 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €9.663,83 | €751,67 | €1.503,34 | €143,14 | €65,01 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 3 | €9.551,46 | €509,71 | €1.019,41 | €95,23 | €5,59 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 1 | €9.550,02 | €134,26 | €402,77 | €48,33 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 3 | €9.541,30 | €509,16 | €1.018,33 | €95,13 | €5,58 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.524,02 | €731,29 | €1.462,57 | €143,29 | €-17,13 |
| TEST | Master Adaptive V1 | 3 | €9.504,39 | €507,20 | €1.014,39 | €94,76 | €5,56 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.486,47 | €1.458,09 | €2.916,19 | €143,36 | €103,08 |
| TEST | Bilanciata 1H V2 | 5 | €9.443,75 | €1.033,11 | €3.099,32 | €142,02 | €46,29 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.404,17 | €1.638,44 | €3.276,88 | €187,64 | €-19,51 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.392,35 | €1.164,15 | €2.328,31 | €187,85 | €105,94 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.378,99 | €500,46 | €1.000,91 | €93,50 | €5,49 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.368,98 | €898,20 | €1.796,40 | €141,49 | €47,19 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 1 | €9.337,15 | €130,02 | €390,07 | €46,81 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.302,52 | €714,28 | €1.428,56 | €139,95 | €-16,74 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 4 | €9.262,27 | €916,09 | €1.832,18 | €144,61 | €90,02 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.238,67 | €1.858,06 | €5.574,18 | €184,98 | €-8,71 |
| TEST | Combo Trend | 4 | €9.196,29 | €1.553,71 | €3.107,42 | €137,50 | €-39,67 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 2 | €9.196,10 | €332,47 | €664,95 | €48,68 | €-16,50 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €9.174,06 | €1.215,22 | €2.430,44 | €92,36 | €-21,47 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.104,24 | €1.386,17 | €2.772,34 | €137,72 | €-15,28 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 2 | €9.001,08 | €645,10 | €1.290,20 | €45,24 | €41,52 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 2 | €8.882,46 | €1.796,12 | €3.592,23 | €89,18 | €-34,15 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.804,89 | €821,85 | €1.643,69 | €131,68 | €43,39 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 2 | €8.725,94 | €1.155,86 | €2.311,72 | €87,85 | €-20,42 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.900,13 | €-191,01 | 54 | 54 | 38,89% | 0,87 | €-3,54 | 6,86% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.310,16 | €1.288,54 | 152 | 152 | 53,29% | 1,43 | €8,48 | 5,23% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.206,61 | €1.189,97 | 114 | 114 | 46,49% | 1,46 | €10,44 | 6,34% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.028,11 | €955,06 | 150 | 150 | 47,33% | 1,33 | €6,37 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.015,85 | €1.059,99 | 121 | 121 | 52,89% | 1,49 | €8,76 | 6,20% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.942,77 | €926,51 | 82 | 82 | 45,12% | 1,55 | €11,30 | 6,34% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.921,58 | €850,09 | 38 | 38 | 55,26% | 2,20 | €22,37 | 3,82% |
| TEST | Combo Adaptive | Combo Adaptive | €10.607,41 | €614,42 | 158 | 158 | 46,20% | 1,24 | €3,89 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.528,26 | €555,75 | 197 | 197 | 50,25% | 1,17 | €2,82 | 9,50% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.515,97 | €516,34 | 230 | 230 | 46,09% | 1,12 | €2,24 | 7,86% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.460,62 | €487,93 | 241 | 241 | 44,81% | 1,11 | €2,02 | 9,48% |
| TEST | Ampia 4H | Confluenza trend | €10.401,14 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.401,12 | €408,52 | 130 | 130 | 46,92% | 1,15 | €3,14 | 7,78% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.396,81 | €359,25 | 50 | 45 | 50,00% | 1,31 | €7,18 | 3,89% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.326,59 | €352,12 | 121 | 121 | 47,11% | 1,15 | €2,91 | 8,68% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.313,79 | €336,88 | 87 | 87 | 47,13% | 1,20 | €3,87 | 5,24% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.308,62 | €240,34 | 133 | 133 | 44,36% | 1,09 | €1,81 | 11,27% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.305,79 | €305,79 | 15 | 15 | 60,00% | 2,24 | €20,39 | 2,77% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.305,34 | €267,33 | 44 | 44 | 45,45% | 1,25 | €6,08 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.254,10 | €219,34 | 64 | 64 | 50,00% | 1,16 | €3,43 | 4,50% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.243,76 | €270,41 | 240 | 240 | 40,00% | 1,07 | €1,13 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.228,07 | €243,28 | 8 | 8 | 62,50% | 3,16 | €30,41 | 1,01% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.222,14 | €155,13 | 113 | 113 | 41,59% | 1,06 | €1,37 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.216,16 | €149,19 | 117 | 117 | 41,88% | 1,06 | €1,28 | 12,06% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.212,76 | €79,41 | 159 | 159 | 45,28% | 1,03 | €0,50 | 8,69% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.211,23 | €145,91 | 140 | 140 | 47,86% | 1,06 | €1,04 | 10,31% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.194,81 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Ema 1H | Trend following EMA | €10.177,93 | €177,93 | 17 | 17 | 47,06% | 1,41 | €10,47 | 3,33% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.173,13 | €146,34 | 39 | 39 | 43,59% | 1,14 | €3,75 | 3,63% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.140,30 | €109,39 | 14 | 14 | 35,71% | 1,28 | €7,81 | 2,61% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.139,89 | €118,31 | 159 | 159 | 40,88% | 1,04 | €0,74 | 7,10% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.092,76 | €109,13 | 9 | 9 | 44,44% | 1,51 | €12,13 | 2,27% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.085,51 | €86,12 | 169 | 169 | 43,20% | 1,02 | €0,51 | 10,60% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.081,13 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.033,18 | €33,18 | 18 | 18 | 44,44% | 1,07 | €1,84 | 4,59% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.013,20 | €-7,40 | 10 | 10 | 50,00% | 0,97 | €-0,74 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Doge Ema 1H | Trend following EMA | €9.988,31 | €-11,15 | 17 | 17 | 58,82% | 0,97 | €-0,66 | 2,77% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.959,74 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.939,72 | €-60,28 | 6 | 6 | 33,33% | 0,71 | €-10,05 | 1,83% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,24 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.919,55 | €-145,34 | 137 | 137 | 47,45% | 0,94 | €-1,06 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.919,55 | €-145,34 | 137 | 137 | 47,45% | 0,94 | €-1,06 | 10,31% |
| TEST | Combo Scanner | Combo Scanner | €9.915,66 | €-160,97 | 138 | 138 | 44,20% | 0,95 | €-1,17 | 11,38% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.887,57 | €-133,48 | 123 | 123 | 39,02% | 0,94 | €-1,09 | 7,10% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.873,73 | €-102,88 | 41 | 41 | 46,34% | 0,90 | €-2,51 | 4,21% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.873,49 | €-126,51 | 14 | 14 | 42,86% | 0,72 | €-9,04 | 3,14% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.852,58 | €-147,42 | 77 | 77 | 40,26% | 0,91 | €-1,91 | 4,16% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.839,28 | €-160,72 | 13 | 13 | 38,46% | 0,68 | €-12,36 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.814,68 | €-183,73 | 178 | 178 | 41,57% | 0,95 | €-1,03 | 12,52% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.807,68 | €-258,79 | 120 | 113 | 42,50% | 0,92 | €-2,16 | 10,88% |
| TEST | Eth Ema 1H | Trend following EMA | €9.799,26 | €-200,74 | 20 | 20 | 40,00% | 0,71 | €-10,04 | 4,80% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.785,26 | €-189,83 | 67 | 67 | 47,76% | 0,88 | €-2,83 | 5,38% |
| TEST | Btc Ema 1H | Trend following EMA | €9.777,64 | €-220,56 | 14 | 14 | 28,57% | 0,55 | €-15,75 | 2,39% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.767,92 | €-219,51 | 166 | 166 | 40,96% | 0,94 | €-1,32 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.749,54 | €-227,36 | 41 | 41 | 41,46% | 0,79 | €-5,55 | 5,41% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.727,35 | €-272,24 | 138 | 138 | 42,03% | 0,91 | €-1,97 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.720,03 | €-342,70 | 108 | 108 | 44,44% | 0,84 | €-3,17 | 9,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.709,98 | €-290,02 | 14 | 14 | 28,57% | 0,52 | €-20,72 | 3,74% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.694,76 | €-347,27 | 84 | 84 | 39,29% | 0,83 | €-4,13 | 8,88% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.689,15 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.684,46 | €-289,06 | 213 | 213 | 43,19% | 0,93 | €-1,36 | 9,00% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.663,83 | €-400,19 | 125 | 125 | 43,20% | 0,84 | €-3,20 | 12,28% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.551,46 | €-453,10 | 71 | 71 | 30,99% | 0,78 | €-6,38 | 8,39% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.550,02 | €-449,64 | 96 | 96 | 39,58% | 0,82 | €-4,68 | 6,64% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.541,30 | €-463,26 | 66 | 66 | 34,85% | 0,77 | €-7,02 | 7,98% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.524,02 | €-457,62 | 115 | 115 | 38,26% | 0,84 | €-3,98 | 7,34% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.504,39 | €-500,14 | 68 | 68 | 33,82% | 0,77 | €-7,36 | 7,80% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.486,47 | €-614,00 | 58 | 58 | 31,03% | 0,70 | €-10,59 | 8,18% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.443,75 | €-600,45 | 113 | 103 | 44,25% | 0,75 | €-5,31 | 9,47% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.404,17 | €-574,23 | 73 | 73 | 35,62% | 0,73 | €-7,87 | 7,96% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.392,35 | €-711,92 | 171 | 171 | 41,52% | 0,78 | €-4,16 | 15,45% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.378,99 | €-625,49 | 102 | 102 | 47,06% | 0,73 | €-6,13 | 9,02% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.368,98 | €-676,72 | 68 | 68 | 33,82% | 0,70 | €-9,95 | 7,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.337,15 | €-662,28 | 100 | 100 | 44,00% | 0,78 | €-6,62 | 8,22% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.302,52 | €-679,55 | 132 | 132 | 39,39% | 0,78 | €-5,15 | 8,78% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.262,27 | €-826,31 | 58 | 58 | 24,14% | 0,60 | €-14,25 | 11,41% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.238,67 | €-749,44 | 120 | 120 | 40,83% | 0,69 | €-6,25 | 8,85% |
| TEST | Combo Trend | Combo Trend | €9.196,29 | €-761,32 | 163 | 163 | 38,65% | 0,80 | €-4,67 | 10,85% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.196,10 | €-786,94 | 76 | 76 | 35,53% | 0,67 | €-10,35 | 10,52% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.174,06 | €-802,95 | 36 | 36 | 22,22% | 0,34 | €-22,30 | 9,80% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.104,24 | €-878,94 | 128 | 128 | 37,50% | 0,67 | €-6,87 | 12,31% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.001,08 | €-1.039,60 | 94 | 94 | 35,11% | 0,62 | €-11,06 | 10,76% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.882,46 | €-1.081,03 | 48 | 48 | 35,42% | 0,46 | €-22,52 | 13,01% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.804,89 | €-1.237,19 | 62 | 62 | 25,81% | 0,54 | €-19,95 | 12,92% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.725,94 | €-1.252,19 | 82 | 82 | 30,49% | 0,49 | €-15,27 | 14,79% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 3,02800 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €93,40 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,38615 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-1,31 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 796,70931 | 799,74000 | 737,00710 | 535,12309 | 916,11372 | €14,36 | €43,07 | €3,23 | €0,16 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | ENA | LONG | Confluenza trend | 60m | 3,0x | 0,16818 | 0,16261 | 0,15607 | 0,11296 | 0,19242 | €13,64 | €40,93 | €2,95 | €-1,36 |
| 1H Balanced Long No Rhv V1 | TRUMP | LONG | Confluenza trend | 60m | 3,0x | 2,76755 | 3,02800 | 2,85759 | 1,85887 | 3,14133 | €235,06 | €705,17 | €0,00 | €66,36 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19977 | €131,74 | €395,21 | €47,43 | €0,00 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16818 | 0,16261 | 0,15607 | 0,11296 | 0,19242 | €218,78 | €656,35 | €47,29 | €-21,75 |
| Bilanciata 1H V2 | TRUMP | LONG | Confluenza trend V2 | 60m | 3,0x | 2,76555 | 3,02800 | 2,86271 | 1,85753 | 3,12699 | €239,03 | €717,09 | €0,00 | €68,05 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,17 | €63,51 | €1,45 | €-0,01 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16848 | 0,16261 | 0,15591 | 0,11316 | 0,19363 | €219,57 | €658,70 | €49,15 | €-22,96 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08564 | 0,08516 | 0,08758 | 0,11376 | 0,08178 | €724,64 | €2.173,91 | €49,08 | €12,26 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20120 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €1,49 |
| 1H Fast Score 6 75 Range Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €694,04 | €2.082,12 | €50,73 | €22,21 |
| 1H Fast Score 6 75 Range Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08493 | 0,08516 | 0,08648 | 0,11282 | 0,08261 | €926,55 | €2.779,65 | €50,72 | €-7,43 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20120 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €15,84 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,02 | €417,05 | €50,05 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €757,52 | €2.272,57 | €55,37 | €24,25 |
| 1H Fast Score 6 75 Cost Aware V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08236 | €9,42 | €28,27 | €0,47 | €-0,23 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €132,75 | €398,25 | €47,79 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €692,07 | €2.076,20 | €50,59 | €22,15 |
| 1H Fast Nohigh Cap75 V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,74965 | 0,74150 | 0,74696 | 0,99579 | 0,72339 | €52,16 | €156,47 | €0,00 | €1,70 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08236 | €10,52 | €31,56 | €0,52 | €-0,26 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €145,28 | €435,84 | €52,30 | €0,00 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08518 | 0,08516 | 0,08679 | 0,11315 | 0,08278 | €29,81 | €89,44 | €1,68 | €0,02 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20120 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €1,97 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08166 | €974,16 | €2.922,49 | €48,45 | €-24,11 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20120 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €18,06 |
| Rapida 1H V2 | PEPE | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €708,48 | €2.125,44 | €51,79 | €22,68 |
| Rapida 1H V2 | TRUMP | LONG | Momentum / breakout V2 | 60m | 3,0x | 3,02861 | 3,02800 | 2,87244 | 2,03421 | 3,26285 | €336,08 | €1.008,25 | €51,99 | €-0,20 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,42 | €25,27 | €3,03 | €0,00 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08236 | €961,36 | €2.884,08 | €47,81 | €-23,80 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €9,29 | €27,86 | €3,34 | €0,00 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08518 | 0,08516 | 0,08679 | 0,11315 | 0,08278 | €865,27 | €2.595,82 | €48,87 | €0,70 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20120 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €1,92 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €135,44 | €406,31 | €48,76 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €134,26 | €402,77 | €48,33 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08236 | €961,72 | €2.885,16 | €47,83 | €-23,81 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,69 | €419,06 | €50,29 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,48 | €25,43 | €3,05 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08236 | €967,58 | €2.902,74 | €48,12 | €-23,95 |
| 1H Fast V3 No Esports Stress Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08518 | 0,08516 | 0,08679 | 0,11315 | 0,08278 | €904,62 | €2.713,85 | €51,10 | €0,73 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20120 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €17,81 |
| 1H Fast V3 No Esports Stress Guard V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €721,39 | €2.164,16 | €51,13 | €23,50 |
| 1H Fast V3 No Esports Stress Guard V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,38539 | 1,38615 | 1,41237 | 1,84026 | 1,34493 | €875,07 | €2.625,20 | €51,12 | €-1,43 |
| 1H Fast V3 No Esports Stress Guard V1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,73415 | 0,74150 | 0,75200 | 0,97520 | 0,70739 | €18,13 | €54,39 | €1,32 | €-0,54 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15804 | 0,15804 | 0,13908 | 0,10615 | 0,18649 | €130,02 | €390,07 | €46,81 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2439,54000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,15 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 82,01200 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,94 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 3,02800 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €116,28 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08516 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €4,30 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 103,96200 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €0,05 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | BTR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,15974 | 0,15974 | 0,14057 | 0,08067 | 0,20191 | €200,93 | €401,87 | €48,22 | €0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20120 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €0,28 |
| Forza relativa 1H V2 | TRUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 2,76755 | 3,02800 | 2,84628 | 1,39761 | 3,17870 | €357,94 | €715,88 | €0,00 | €67,37 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €803,68 | €1.607,36 | €55,95 | €17,15 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08518 | 0,08516 | 0,08747 | 0,12735 | 0,07945 | €1.039,92 | €2.079,84 | €55,94 | €0,56 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20120 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €1,17 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €784,76 | €1.569,52 | €54,63 | €16,75 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08518 | 0,08516 | 0,08747 | 0,12735 | 0,07945 | €1.015,44 | €2.030,87 | €54,63 | €0,55 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20120 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €1,14 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 799,74000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-0,35 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,08437 | 0,08516 | 0,08662 | 0,12614 | 0,07944 | €800,03 | €1.600,05 | €42,54 | €-14,92 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 3,02800 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €99,64 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €384,03 | €768,07 | €55,34 | €-25,45 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | BTR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €206,82 | €413,63 | €49,64 | €0,00 |
| Scanner Top10 Long | ENA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €20,79 | €41,59 | €3,00 | €-1,38 |
| Scanner Top10 Long | TRUMP | LONG | Scanner Top10 Long | 60m | 2,0x | 2,76755 | 3,02800 | 2,85759 | 1,39761 | 3,14133 | €370,38 | €740,77 | €0,00 | €69,71 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 3,02800 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €90,04 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | BTR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top15 Long | ENA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €343,65 | €687,31 | €49,52 | €-22,78 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 3,02800 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €90,04 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | BTR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top20 Long | ENA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €343,65 | €687,31 | €49,52 | €-22,78 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 3,02800 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €93,02 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €357,11 | €714,22 | €51,46 | €-23,67 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 3,02800 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €87,20 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €334,77 | €669,55 | €48,24 | €-22,19 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 3,02800 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €4,82 |
| Scanner Top5 Btc Guard V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €189,80 | €379,60 | €45,55 | €0,00 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €331,18 | €662,37 | €47,72 | €-21,95 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €308,12 | €616,23 | €44,40 | €-20,42 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €323,94 | €647,88 | €46,68 | €-21,47 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 3,02800 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €4,71 |
| Scanner Top5 Btc Guard Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €185,39 | €370,78 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €323,48 | €646,96 | €46,61 | €-21,44 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 3,02800 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €4,70 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €319,77 | €639,55 | €46,08 | €-21,19 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €313,96 | €627,93 | €45,24 | €-20,81 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,76755 | 3,02800 | 2,85759 | 1,39761 | 3,17870 | €331,14 | €662,27 | €0,00 | €62,32 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,82 | €421,64 | €50,60 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,20453 | €12,60 | €25,20 | €1,82 | €-0,84 |
| Scanner Top5 Btc Runner25 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,76755 | 3,02800 | 2,85759 | 1,39761 | 3,32821 | €373,21 | €746,42 | €0,00 | €70,24 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,94 | €421,89 | €50,63 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,20453 | €12,61 | €25,22 | €1,82 | €-0,84 |
| Scanner Top5 Btc Tp3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,76755 | 3,02800 | 2,85759 | 1,39761 | 3,32821 | €373,43 | €746,85 | €0,00 | €70,28 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08564 | 0,08516 | 0,08779 | 0,12804 | 0,08027 | €964,56 | €1.929,13 | €48,40 | €10,88 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 799,74000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-5,02 |
| Combo Trend | ENA | LONG | Combo Trend | 60m | 2,0x | 0,16848 | 0,16261 | 0,15452 | 0,08508 | 0,19921 | €272,14 | €544,28 | €45,12 | €-18,97 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08437 | 0,08516 | 0,08662 | 0,12614 | 0,07944 | €840,25 | €1.680,50 | €44,68 | €-15,67 |
| Combo Mean Reversion | PEPE | LONG | Combo Mean Reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €854,12 | €1.708,24 | €44,59 | €-18,90 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20120 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €-15,25 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 3,02800 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €89,25 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19484 | €343,11 | €686,22 | €49,44 | €-22,74 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,08564 | 0,08516 | 0,08758 | 0,12804 | 0,08139 | €1.093,09 | €2.186,18 | €49,36 | €12,33 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 3,02800 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €7,45 |
| Combo Adaptive | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €222,35 | €444,69 | €53,36 | €0,00 |
| Combo Adaptive | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €370,32 | €740,64 | €53,36 | €-24,55 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08564 | 0,08516 | 0,08758 | 0,12804 | 0,08178 | €1.147,68 | €2.295,36 | €51,83 | €12,94 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 3,02800 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €125,95 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €163,28 | €326,55 | €39,19 | €0,00 |
| Combo Adaptive Mfe Trail | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €324,72 | €649,45 | €46,79 | €-21,52 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €71,85 | €143,70 | €4,50 | €1,53 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08514 | 0,08516 | 0,08650 | 0,12729 | 0,08242 | €44,22 | €88,44 | €1,41 | €-0,02 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €336,30 | €672,60 | €48,46 | €-22,29 |
| Combo Adaptive Quality7 V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,76755 | 3,02800 | 2,86891 | 1,39761 | 3,14133 | €352,99 | €705,98 | €0,00 | €66,44 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €204,79 | €409,58 | €49,15 | €0,00 |
| Combo Adaptive Regime V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €342,54 | €685,09 | €49,36 | €-22,70 |
| Combo Adaptive Quality7 Regime V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €341,26 | €682,52 | €49,17 | €-22,62 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 3,02800 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €19,19 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €363,37 | €726,74 | €52,36 | €-24,08 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 3,02800 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €138,49 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €41,31 | €82,63 | €5,95 | €-2,74 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08514 | 0,08516 | 0,08650 | 0,12729 | 0,08242 | €39,06 | €78,12 | €1,25 | €-0,02 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €345,61 | €691,22 | €49,80 | €-22,91 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77644,36802 | 77638,90000 | 78762,44692 | 103137,60219 | 75408,21022 | €1.131,88 | €3.395,64 | €48,90 | €0,24 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 77638,90000 | 79375,01684 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €51,84 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 105,86117 | 103,96200 | 99,76922 | 53,45989 | 121,09104 | €439,17 | €878,34 | €50,55 | €-15,76 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 103,96200 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €-1,07 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 103,96200 | 112,84334 | 160,38740 | 97,27311 | €478,97 | €957,94 | €49,65 | €29,65 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,86117 | 103,96200 | 99,21540 | 53,45989 | 122,47558 | €407,92 | €815,83 | €51,22 | €-14,64 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08518 | 0,08516 | 0,08725 | 0,11315 | 0,08106 | €687,72 | €2.063,16 | €49,94 | €0,56 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,08518 | 0,08516 | 0,08702 | 0,11315 | 0,08152 | €768,73 | €2.306,18 | €49,62 | €0,62 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08441 | 0,08516 | 0,08272 | 0,05669 | 0,08693 | €835,22 | €2.505,66 | €49,96 | €22,36 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,23 | €382,45 | €45,89 | €0,00 |
| Master Adaptive V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16261 | 0,14798 | 0,08135 | 0,18729 | €293,22 | €586,43 | €47,70 | €5,56 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,14959 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16781 | 0,16261 | 0,15575 | 0,08475 | 0,19195 | €327,73 | €655,45 | €47,13 | €-20,32 |
| Master Adaptive No Alt V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,76555 | 3,02800 | 2,58484 | 1,39660 | 3,12699 | €355,70 | €711,41 | €46,49 | €67,51 |
| Master Adaptive Strict3 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €184,95 | €369,91 | €44,39 | €0,00 |
| Master Adaptive Strict3 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16818 | 0,16261 | 0,15607 | 0,08493 | 0,19242 | €302,60 | €605,21 | €43,60 | €-20,06 |
| Master Adaptive Strict3 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,76555 | 3,02800 | 2,58484 | 1,39660 | 3,12699 | €334,29 | €668,58 | €43,69 | €63,45 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16110 | 0,16110 | 0,14177 | 0,08136 | 0,19977 | €197,88 | €395,75 | €47,49 | €0,00 |
| Master Adaptive Expanded V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16791 | 0,16261 | 0,15510 | 0,08480 | 0,19353 | €308,85 | €617,69 | €47,12 | €-19,51 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €188,69 | €377,37 | €45,28 | €0,00 |
| Master Adaptive Gb20 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16261 | 0,14798 | 0,08135 | 0,18729 | €289,32 | €578,64 | €47,07 | €5,49 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 82,01200 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €35,55 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16261 | 0,15522 | 0,08370 | 0,19732 | €14,90 | €29,81 | €1,89 | €-0,56 |
| Master Adaptive Runner25 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15905 | 0,15905 | 0,13997 | 0,08032 | 0,21631 | €158,41 | €316,83 | €38,02 | €0,00 |
| Master Adaptive Runner25 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,76555 | 3,02800 | 2,58484 | 1,39660 | 3,30770 | €358,77 | €717,54 | €46,89 | €68,09 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €210,11 | €420,21 | €50,43 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16848 | 0,16261 | 0,15591 | 0,08508 | 0,19363 | €346,85 | €693,71 | €51,76 | €-24,18 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08564 | 0,08516 | 0,08758 | 0,12804 | 0,08178 | €23,51 | €47,02 | €1,06 | €0,27 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €192,17 | €384,35 | €46,12 | €0,00 |
| Master Adaptive Gb20 Be V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16261 | 0,14798 | 0,08135 | 0,18729 | €294,67 | €589,34 | €47,94 | €5,59 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,97 | €383,94 | €46,07 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16261 | 0,14798 | 0,08135 | 0,18729 | €294,36 | €588,71 | €47,89 | €5,58 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,20861 | €188,78 | €377,55 | €45,31 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16261 | 0,15126 | 0,08135 | 0,18729 | €63,69 | €127,37 | €7,77 | €1,21 |
| Master Adaptive Gb20 Loss Cap V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,76555 | 3,02800 | 2,63002 | 1,39660 | 3,12699 | €467,93 | €935,86 | €45,87 | €88,81 |
| 1H Fast V3 Nohigh Range Only V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08518 | 0,08516 | 0,08679 | 0,11315 | 0,08278 | €906,64 | €2.719,92 | €51,21 | €0,73 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20120 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €17,85 |
| 1H Fast V3 Nohigh Range Only V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €712,96 | €2.138,88 | €50,53 | €23,22 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08518 | 0,08516 | 0,08679 | 0,11315 | 0,08278 | €919,46 | €2.758,37 | €51,93 | €0,74 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20120 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €0,83 |
| 1H Fast V3 Nohigh Regime Guard V1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,73415 | 0,74150 | 0,75200 | 0,97520 | 0,70739 | €706,21 | €2.118,63 | €51,49 | €-21,20 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,38615 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-2,21 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2439,54000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,02 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16261 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €4,28 |
| Main Side Regime Guard V1 | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,61252 | 3,02800 | 2,67306 | 1,75474 | 3,23953 | €148,42 | €445,27 | €0,00 | €70,81 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16261 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €4,01 |
| Main Dynamic Asset Selector V1 | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,84257 | 3,02800 | 2,50146 | 1,90926 | 3,52478 | €140,37 | €421,12 | €50,53 | €27,47 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | LONG | Combo Trend | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €231,16 | €462,32 | €55,48 | €0,00 |
| Combo Trend Side Regime Guard V1 | ENA | LONG | Combo Trend | 60m | 2,0x | 0,16818 | 0,16261 | 0,15472 | 0,08493 | 0,19780 | €338,29 | €676,57 | €54,16 | €-22,42 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08437 | 0,08516 | 0,08662 | 0,12614 | 0,07944 | €1.036,98 | €2.073,96 | €55,14 | €-19,34 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €129,45 | €388,34 | €46,60 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €674,84 | €2.024,53 | €49,33 | €21,60 |
| 1H Fast Nohigh Cap75 Short Only V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,74965 | 0,74150 | 0,74696 | 0,99579 | 0,72339 | €50,86 | €152,57 | €0,00 | €1,66 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08446 | 0,08516 | 0,08586 | 0,11220 | 0,08236 | €10,26 | €30,78 | €0,51 | €-0,25 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16848 | 0,16261 | 0,15591 | 0,11316 | 0,19363 | €207,67 | €623,01 | €46,49 | €-21,72 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08564 | 0,08516 | 0,08758 | 0,11376 | 0,08178 | €685,37 | €2.056,12 | €46,42 | €11,59 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20120 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €1,41 |
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
| Master Adaptive V1 | TRUMP | LONG | 2026-08-29T05:00:00+00:00 | 3,04222 | €93,05 | 1,98 | TARGET |
| Master Adaptive Gb20 V1 | TRUMP | LONG | 2026-08-29T05:00:00+00:00 | 3,04222 | €91,82 | 1,98 | TARGET |
| Master Adaptive Gb20 Partial V1 | TRUMP | LONG | 2026-08-29T05:00:00+00:00 | 3,04222 | €93,41 | 1,98 | TARGET |
| Master Adaptive Gb20 Be V1 | TRUMP | LONG | 2026-08-29T05:00:00+00:00 | 3,04222 | €93,51 | 1,98 | TARGET |
| 1H Fast V3 No Esports Long Only V1 | TRUMP | LONG | 2026-08-29T04:30:00+00:00 | 2,97579 | €73,65 | 1,47 | TARGET |
| 1H Fast V3 Nohigh Range Only V1 | TRUMP | LONG | 2026-08-29T04:30:00+00:00 | 2,97579 | €75,05 | 1,47 | TARGET |
| 1H Fast V3 Long Only V1 | TRUMP | LONG | 2026-08-29T04:30:00+00:00 | 2,97579 | €71,67 | 1,47 | TARGET |
| Bilanciata 1H V2 | SUI | SHORT | 2026-08-29T00:30:00+00:00 | 0,74628 | €0,41 | 0,63 | STOP |
| 1H Fast V3 No Esports V1 | ENA | LONG | 2026-08-28T22:00:00+00:00 | 0,15748 | €-50,00 | -1,02 | STOP |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | LONG | 2026-08-28T22:00:00+00:00 | 0,15748 | €-49,95 | -1,02 | STOP |
| Rapida 1H V3 Filtered | ENA | LONG | 2026-08-28T22:00:00+00:00 | 0,15748 | €-49,63 | -1,02 | STOP |
| 1H Fast Tp2 V1 | ENA | LONG | 2026-08-28T22:00:00+00:00 | 0,15748 | €-50,68 | -1,02 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
