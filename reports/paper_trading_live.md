# Paper trading automatico KuCoin

Generato: 2026-09-05T08:22:54+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-05T08:05:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-05T08:05:33+00:00 | 2026-09-05T08:05:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-05T07:45:00+00:00 | 2026-09-05T07:45:00+00:00 | 6,0 min | 25,0 min | OK |
| 60m | 12 | 2026-09-05T07:00:00+00:00 | 2026-09-05T07:00:00+00:00 | 6,0 min | 45,0 min | OK |
| 240m | 12 | 2026-09-05T04:00:00+00:00 | 2026-09-05T04:00:00+00:00 | 6,0 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main Side Regime Guard V1 | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Loss Cap V1 | NEAR | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | NEAR | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Regime V1 | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | NEAR | 240m | LONG | 6,75 | 6,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | DASH | 240m | LONG | 6,25 | 6,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | USELESS | 240m | LONG | 6,25 | 6,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 6,0 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | ENA | 240m | LONG | 5,01 | 6,00 | 0,99 | BELOW_SCORE | 6,0 min | D: n/a | W: n/a | peso 0 | Punteggio +5.01; soglia ±6.00; mancano 0.99 punti. |
| Ampia 4H | AKE | 240m | LONG | 8,25 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | NEAR | 60m | LONG | 7,75 | 5,50 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top10 Long | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Guard V1 | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Guard Mfe V1 | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Scanner | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Mfe Trail | NEAR | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Quality7 V1 | NEAR | 60m | LONG | 7,75 | 7,00 | 0,00 | READY | 6,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.812,20 | -1,88% | €3,64 | €3.000,00 | 0,12% | 6 | 58 | 41,38% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 58 | 2971 | PRIME INDICAZIONI | 100 (mancano 42) |

- Trade del Principale 4H chiusi: **58**; win rate **41,38%**; profit factor **0,87**.
- Expectancy: **€-3,21** per trade; P&L netto: **€-186,03**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.812,20 | €699,89 | €2.099,67 | €196,23 | €-0,64 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.634,20 | €3.153,16 | €6.306,31 | €232,75 | €-20,41 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.360,28 | €3.078,92 | €6.157,84 | €227,27 | €-19,93 |
| TEST | Main Side Regime Guard V1 | 7 | €11.354,26 | €705,74 | €2.117,22 | €227,09 | €305,42 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 5 | €11.010,78 | €575,04 | €1.725,12 | €120,33 | €8,62 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.971,88 | €1.171,11 | €2.342,21 | €219,45 | €-0,68 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.652,04 | €2.351,87 | €4.703,74 | €211,26 | €85,81 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.644,98 | €1.353,45 | €2.706,91 | €161,34 | €-36,22 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.578,16 | €1.339,25 | €4.017,76 | €211,57 | €-0,08 |
| TEST | Rapida 1H V2 | 2 | €10.565,84 | €1.257,04 | €3.771,13 | €104,63 | €-0,30 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 7 | €10.445,09 | €978,68 | €2.936,03 | €158,23 | €-34,03 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 4 | €10.416,51 | €2.685,80 | €8.057,41 | €153,76 | €-39,63 |
| TEST | Scanner Top15 Long | 7 | €10.402,00 | €2.157,54 | €4.315,09 | €202,75 | €0,42 |
| TEST | Scanner Top20 Long | 7 | €10.402,00 | €2.157,54 | €4.315,09 | €202,75 | €0,42 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.397,05 | €1.562,50 | €4.687,49 | €207,96 | €0,00 |
| TEST | Combo Adaptive | 7 | €10.362,37 | €1.312,63 | €2.625,26 | €156,25 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €10.351,03 | €1.443,97 | €2.887,95 | €155,27 | €1,15 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €10.344,97 | €1.443,13 | €2.886,26 | €155,18 | €1,15 |
| TEST | Sol Donchian 1H | 1 | €10.335,10 | €1.010,51 | €3.031,53 | €51,78 | €-19,07 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.330,25 | €1.552,46 | €4.657,37 | €206,63 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.284,21 | €1.071,19 | €2.142,37 | €207,40 | €3,80 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.276,65 | €1.100,71 | €2.201,42 | €205,55 | €-0,85 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 2 | €10.231,45 | €876,12 | €2.628,37 | €51,20 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 7 | €10.216,45 | €555,81 | €1.667,42 | €153,79 | €-2,15 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.201,60 | €2.314,20 | €4.628,40 | €204,03 | €-0,01 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.180,28 | €282,12 | €846,37 | €101,56 | €23,09 |
| TEST | Combo Scanner | 7 | €10.170,88 | €1.424,39 | €2.848,79 | €203,42 | €-24,43 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.120,56 | €574,98 | €1.149,96 | €50,72 | €-23,60 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.095,47 | €985,68 | €1.971,36 | €50,34 | €28,14 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.072,32 | €910,20 | €2.730,61 | €108,10 | €8,89 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €10.056,69 | €1.075,61 | €3.226,84 | €101,77 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.054,77 | €1.966,66 | €3.933,32 | €151,23 | €-0,02 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.039,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.032,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.025,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.017,96 | €1.119,19 | €3.357,58 | €50,17 | €-13,48 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.007,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.992,43 | €817,27 | €1.634,54 | €50,09 | €-23,98 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.965,45 | €1.157,72 | €3.473,16 | €50,01 | €-35,16 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.950,64 | €864,62 | €2.593,86 | €49,84 | €-16,32 |
| TEST | Btc Ema 4H | 1 | €9.939,57 | €887,05 | €1.774,10 | €49,83 | €-26,03 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.927,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €9.909,57 | €1.086,26 | €2.172,53 | €99,07 | €10,16 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.886,39 | €882,31 | €1.764,61 | €49,57 | €-25,89 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.884,69 | €892,10 | €2.676,31 | €148,79 | €-1,53 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.879,91 | €1.231,95 | €3.695,84 | €197,62 | €-1,94 |
| TEST | Eth Ema 4H | 1 | €9.861,42 | €690,19 | €1.380,39 | €49,44 | €-24,85 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.836,05 | €841,97 | €1.683,94 | €99,44 | €-0,81 |
| TEST | Sol Bollinger 1H | 0 | €9.819,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.809,61 | €1.383,96 | €4.151,88 | €197,52 | €-60,99 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 5 | €9.806,46 | €1.358,25 | €4.074,75 | €197,44 | €-60,30 |
| TEST | Master Adaptive Gb20 Be V1 | 6 | €9.783,32 | €908,64 | €1.817,27 | €147,53 | €-0,06 |
| TEST | Master Adaptive Gb20 Partial V1 | 6 | €9.772,91 | €907,67 | €1.815,34 | €147,37 | €-0,06 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.750,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €9.749,02 | €1.077,20 | €2.154,41 | €97,67 | €-44,35 |
| TEST | Master Adaptive V1 | 6 | €9.735,11 | €904,16 | €1.808,32 | €146,80 | €-0,06 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.721,15 | €1.360,07 | €4.080,22 | €195,01 | €-58,71 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.719,02 | €1.004,71 | €3.014,12 | €145,58 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.716,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.705,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €9.698,11 | €1.024,80 | €2.049,60 | €193,99 | €-1,26 |
| TEST | Eth Donchian 1H | 0 | €9.693,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.667,74 | €1.515,66 | €3.031,33 | €48,50 | €-30,69 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.654,30 | €1.132,92 | €3.398,77 | €193,08 | €0,55 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.633,86 | €1.031,86 | €2.063,72 | €192,69 | €-0,79 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.626,40 | €1.063,65 | €2.127,31 | €96,44 | €-43,79 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.606,64 | €892,16 | €1.784,31 | €144,87 | €-0,05 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.565,50 | €1.385,25 | €2.770,50 | €191,33 | €-0,19 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.552,51 | €1.053,15 | €3.159,44 | €191,07 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.476,95 | €979,65 | €2.938,95 | €141,95 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.472,57 | €1.000,97 | €2.001,93 | €189,48 | €-1,23 |
| TEST | Btc Ema 1H | 0 | €9.463,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 5 | €9.461,84 | €3.251,16 | €6.502,32 | €189,25 | €-53,53 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.454,69 | €1.328,25 | €3.984,74 | €148,18 | €-1,36 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.435,13 | €1.403,33 | €4.210,00 | €144,98 | €-89,78 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 8 | €9.432,29 | €1.549,54 | €3.099,08 | €188,67 | €1,48 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.369,88 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.321,08 | €909,08 | €2.727,24 | €96,61 | €-23,29 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €9.317,14 | €648,00 | €1.296,00 | €140,76 | €-2,04 |
| TEST | Bilanciata 1H V1 | 7 | €9.272,80 | €1.119,14 | €3.357,42 | €140,05 | €7,08 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 3 | €9.253,55 | €627,91 | €1.883,74 | €49,23 | €-19,45 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.217,11 | €1.702,55 | €3.405,10 | €185,26 | €-5,55 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €9.208,40 | €2.015,23 | €4.030,45 | €140,50 | €-16,16 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.179,56 | €946,65 | €1.893,30 | €138,93 | €-0,29 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Combo Trend | 5 | €9.066,74 | €1.927,91 | €3.855,81 | €89,72 | €-0,35 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.047,75 | €1.111,82 | €2.223,65 | €146,74 | €-0,95 |
| TEST | Combo Adaptive Tp3 V1 | 6 | €9.036,14 | €1.977,54 | €3.955,08 | €137,87 | €-15,86 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €8.967,12 | €1.840,32 | €3.680,64 | €90,31 | €24,36 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €8.942,41 | €1.256,27 | €3.768,82 | €140,15 | €-1,29 |
| TEST | Master Adaptive Strict3 V1 | 5 | €8.930,05 | €1.182,45 | €2.364,90 | €179,03 | €13,40 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €8.896,55 | €1.170,34 | €2.340,67 | €88,84 | €10,58 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.891,17 | €1.157,95 | €3.473,85 | €133,67 | €-53,70 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 4 | €8.747,02 | €1.524,51 | €3.049,02 | €131,85 | €-21,40 |
| TEST | Combo Mean Reversion | 1 | €8.614,56 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Forza relativa 1H V1 | 7 | €8.544,85 | €1.422,39 | €2.844,78 | €88,16 | €18,94 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €8.424,32 | €570,99 | €1.141,97 | €42,44 | €-0,23 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.812,20 | €-186,03 | 58 | 58 | 41,38% | 0,87 | €-3,21 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.634,20 | €1.657,81 | 134 | 134 | 46,27% | 1,57 | €12,37 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.360,28 | €1.383,34 | 102 | 102 | 45,10% | 1,69 | €13,56 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.354,26 | €1.050,60 | 47 | 47 | 57,45% | 2,37 | €22,35 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.010,78 | €1.003,32 | 190 | 190 | 50,00% | 1,25 | €5,28 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.971,88 | €974,00 | 166 | 166 | 48,19% | 1,32 | €5,87 | 8,85% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.652,04 | €569,04 | 150 | 150 | 48,67% | 1,20 | €3,79 | 7,78% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.644,98 | €682,74 | 146 | 146 | 50,68% | 1,23 | €4,68 | 10,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.578,16 | €580,48 | 266 | 266 | 44,36% | 1,13 | €2,18 | 9,28% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.565,84 | €568,21 | 66 | 58 | 50,00% | 1,37 | €8,61 | 3,89% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.445,09 | €480,64 | 113 | 113 | 49,56% | 1,24 | €4,25 | 5,24% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.416,51 | €459,88 | 104 | 104 | 50,00% | 1,21 | €4,42 | 4,50% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.402,00 | €404,20 | 180 | 180 | 48,33% | 1,14 | €2,25 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.402,00 | €404,20 | 180 | 180 | 48,33% | 1,14 | €2,25 | 10,31% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.397,05 | €399,98 | 213 | 213 | 49,30% | 1,11 | €1,88 | 9,50% |
| TEST | Combo Adaptive | Combo Adaptive | €10.362,37 | €364,12 | 194 | 194 | 45,88% | 1,11 | €1,88 | 8,17% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.351,03 | €351,61 | 142 | 142 | 42,25% | 1,12 | €2,48 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.344,97 | €345,56 | 146 | 146 | 42,47% | 1,12 | €2,37 | 12,06% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.335,10 | €356,28 | 17 | 17 | 64,71% | 2,44 | €20,96 | 2,77% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.330,25 | €333,16 | 257 | 257 | 44,36% | 1,07 | €1,30 | 9,48% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Ampia 4H | Confluenza trend | €10.284,21 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.276,65 | €278,85 | 149 | 149 | 45,64% | 1,09 | €1,87 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.231,45 | €232,84 | 73 | 73 | 45,21% | 1,13 | €3,19 | 6,05% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.216,45 | €219,58 | 214 | 214 | 42,99% | 1,05 | €1,03 | 10,60% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.201,60 | €204,39 | 162 | 162 | 47,53% | 1,08 | €1,26 | 10,31% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.180,28 | €158,05 | 16 | 16 | 37,50% | 1,36 | €9,88 | 3,39% |
| TEST | Combo Scanner | Combo Scanner | €10.170,88 | €196,83 | 175 | 175 | 44,57% | 1,06 | €1,12 | 11,38% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.120,56 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.095,47 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.072,32 | €65,05 | 253 | 253 | 39,53% | 1,01 | €0,26 | 6,56% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.056,69 | €58,42 | 50 | 50 | 42,00% | 1,04 | €1,17 | 6,49% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.054,77 | €57,13 | 175 | 175 | 44,57% | 1,02 | €0,33 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.039,42 | €39,42 | 29 | 29 | 44,83% | 1,33 | €1,36 | 0,33% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.032,57 | €32,57 | 13 | 13 | 61,54% | 1,11 | €2,51 | 1,89% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,86 | €25,86 | 15 | 15 | 60,00% | 1,07 | €1,72 | 3,08% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Sol Ema 1H | Trend following EMA | €10.017,96 | €33,54 | 21 | 21 | 42,86% | 1,06 | €1,60 | 3,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.007,88 | €7,88 | 29 | 29 | 44,83% | 1,33 | €0,27 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.992,43 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Doge Ema 1H | Trend following EMA | €9.965,45 | €2,70 | 23 | 23 | 60,87% | 1,01 | €0,12 | 2,77% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.950,64 | €-31,24 | 22 | 22 | 45,45% | 0,95 | €-1,42 | 4,59% |
| TEST | Btc Ema 4H | Trend following EMA | €9.939,57 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.927,41 | €-72,59 | 29 | 29 | 44,83% | 0,56 | €-2,50 | 0,84% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.909,57 | €-99,04 | 146 | 146 | 44,52% | 0,97 | €-0,68 | 11,68% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.886,39 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.884,69 | €-112,19 | 214 | 214 | 42,52% | 0,97 | €-0,52 | 12,52% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.879,91 | €-116,22 | 165 | 165 | 44,85% | 0,96 | €-0,70 | 7,10% |
| TEST | Eth Ema 4H | Trend following EMA | €9.861,42 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.836,05 | €-161,84 | 136 | 129 | 40,44% | 0,95 | €-1,19 | 10,88% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.819,99 | €-180,01 | 16 | 16 | 43,75% | 0,68 | €-11,25 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.809,61 | €-126,91 | 133 | 133 | 44,36% | 0,96 | €-0,95 | 6,64% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.806,46 | €-130,80 | 112 | 112 | 41,07% | 0,95 | €-1,17 | 7,99% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.783,32 | €-216,75 | 99 | 99 | 33,33% | 0,92 | €-2,19 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.772,91 | €-227,15 | 94 | 94 | 36,17% | 0,91 | €-2,42 | 7,98% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.750,02 | €-249,98 | 18 | 18 | 38,89% | 0,59 | €-13,89 | 3,14% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.749,02 | €-205,60 | 51 | 51 | 47,06% | 0,84 | €-4,03 | 4,21% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.735,11 | €-264,96 | 96 | 96 | 35,42% | 0,90 | €-2,76 | 7,80% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.721,15 | €-217,69 | 137 | 137 | 45,99% | 0,94 | €-1,59 | 8,44% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.719,02 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,60% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.716,18 | €-283,82 | 9 | 9 | 33,33% | 0,35 | €-31,54 | 4,16% |
| TEST | Eth Ema 1H | Trend following EMA | €9.705,03 | €-294,97 | 26 | 26 | 38,46% | 0,65 | €-11,35 | 4,80% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.698,11 | €-299,91 | 138 | 138 | 39,13% | 0,90 | €-2,17 | 7,34% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.693,16 | €-306,84 | 17 | 17 | 29,41% | 0,54 | €-18,05 | 3,74% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.667,74 | €-299,76 | 20 | 20 | 35,00% | 0,50 | €-14,99 | 3,93% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.654,30 | €-344,15 | 120 | 120 | 44,17% | 0,85 | €-2,87 | 9,26% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.633,86 | €-364,09 | 141 | 141 | 44,68% | 0,86 | €-2,58 | 12,28% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.626,40 | €-328,80 | 51 | 51 | 43,14% | 0,75 | €-6,45 | 5,41% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.606,64 | €-393,43 | 130 | 130 | 45,38% | 0,86 | €-3,03 | 9,02% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.565,50 | €-433,82 | 80 | 80 | 32,50% | 0,82 | €-5,42 | 8,44% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.552,51 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.476,95 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,60% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.472,57 | €-525,49 | 155 | 155 | 40,00% | 0,85 | €-3,39 | 8,78% |
| TEST | Btc Ema 1H | Trend following EMA | €9.463,59 | €-536,41 | 20 | 20 | 20,00% | 0,33 | €-26,82 | 5,46% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.461,84 | €-480,75 | 80 | 80 | 46,25% | 0,76 | €-6,01 | 5,87% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.454,69 | €-541,77 | 187 | 187 | 40,11% | 0,86 | €-2,90 | 12,68% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.435,13 | €-472,56 | 170 | 170 | 41,76% | 0,90 | €-2,78 | 15,64% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.432,29 | €-568,96 | 84 | 84 | 26,19% | 0,76 | €-6,77 | 11,41% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,88 | €-629,45 | 85 | 85 | 34,12% | 0,73 | €-7,41 | 7,96% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.321,08 | €-653,42 | 147 | 134 | 42,18% | 0,79 | €-4,45 | 11,82% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.317,14 | €-680,54 | 95 | 95 | 37,89% | 0,75 | €-7,16 | 11,79% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.272,80 | €-732,01 | 155 | 155 | 38,71% | 0,76 | €-4,72 | 15,68% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.253,55 | €-725,87 | 128 | 128 | 42,97% | 0,81 | €-5,67 | 15,94% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.217,11 | €-775,81 | 95 | 95 | 33,68% | 0,74 | €-8,17 | 10,13% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.208,40 | €-772,80 | 127 | 127 | 36,22% | 0,70 | €-6,09 | 14,10% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.179,56 | €-819,04 | 151 | 151 | 38,41% | 0,71 | €-5,42 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Combo Trend | Combo Trend | €9.066,74 | €-930,33 | 188 | 188 | 38,83% | 0,78 | €-4,95 | 14,08% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.047,75 | €-949,99 | 209 | 209 | 41,15% | 0,76 | €-4,55 | 15,45% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.036,14 | €-945,42 | 107 | 107 | 35,51% | 0,59 | €-8,84 | 14,10% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.967,12 | €-1.055,14 | 45 | 45 | 22,22% | 0,30 | €-23,45 | 12,23% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €8.942,41 | €-1.054,24 | 141 | 141 | 39,72% | 0,64 | €-7,48 | 12,43% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.930,05 | €-1.082,43 | 77 | 77 | 28,57% | 0,64 | €-14,06 | 13,60% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.896,55 | €-1.113,23 | 119 | 119 | 36,97% | 0,66 | €-9,35 | 13,91% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.891,17 | €-1.053,05 | 172 | 172 | 37,79% | 0,76 | €-6,12 | 17,41% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.747,02 | €-1.229,96 | 94 | 94 | 35,11% | 0,53 | €-13,08 | 16,19% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.614,56 | €-1.384,14 | 58 | 58 | 32,76% | 0,42 | €-23,86 | 15,55% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.544,85 | €-1.472,15 | 131 | 131 | 31,30% | 0,57 | €-11,24 | 19,11% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.424,32 | €-1.574,77 | 104 | 104 | 39,42% | 0,54 | €-15,14 | 17,99% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,40195 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-1,03 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 986,71730 | 1000,44000 | 914,15390 | 662,74512 | 1131,84411 | €9,41 | €28,24 | €2,08 | €0,39 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €0,00 |
| Bilanciata 1H V1 | UNI | LONG | Confluenza trend | 60m | 3,0x | 6,29526 | 6,29526 | 6,00645 | 4,22832 | 6,87288 | €333,13 | €999,40 | €45,85 | €0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,08451 | 0,08551 | 0,08636 | 0,11226 | 0,08081 | €18,57 | €55,72 | €1,22 | €-0,66 |
| Bilanciata 1H V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 101,78064 | 102,09300 | 103,24628 | 135,19862 | 98,84936 | €16,94 | €50,82 | €0,73 | €-0,16 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,20444 | 2,22100 | 2,11218 | 1,48065 | 2,38896 | €350,15 | €1.050,46 | €43,96 | €7,89 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,20444 | 2,22100 | 2,11218 | 1,48065 | 2,38896 | €24,38 | €73,14 | €3,06 | €0,55 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,13495 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 1024,65489 | 1000,44000 | 975,86216 | 688,22653 | 1122,24036 | €326,10 | €978,30 | €46,59 | €-23,12 |
| Bilanciata 1H V2 | SOL | SHORT | Confluenza trend V2 | 60m | 3,0x | 101,68466 | 102,09300 | 103,20399 | 135,07112 | 98,64599 | €13,94 | €41,82 | €0,62 | €-0,17 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €0,00 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 101,68466 | 102,09300 | 103,20399 | 135,07112 | 98,64599 | €14,80 | €44,41 | €0,66 | €-0,18 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1016,76331 | 1000,44000 | 973,58489 | 682,92602 | 1103,12014 | €14,51 | €43,53 | €1,85 | €-0,70 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08465 | 0,08551 | 0,08587 | 0,11245 | 0,08222 | €16,02 | €48,07 | €0,69 | €-0,49 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €0,00 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1014,04277 | 1000,44000 | 981,68854 | 681,09873 | 1062,57411 | €496,46 | €1.489,37 | €47,52 | €-19,98 |
| 1H Fast Score 6 75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,28046 | 2,22100 | 2,20450 | 1,53171 | 2,39439 | €476,95 | €1.430,85 | €47,66 | €-37,31 |
| 1H Fast Score 6 75 V1 | DASH | LONG | Momentum / breakout | 60m | 3,0x | 68,92378 | 66,27000 | 65,10624 | 46,29381 | 74,65009 | €281,32 | €843,96 | €46,74 | €-32,49 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1014,04277 | 1000,44000 | 981,68854 | 681,09873 | 1062,57411 | €483,26 | €1.449,77 | €46,26 | €-19,45 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,22100 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €8,62 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €-0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1014,04277 | 1000,44000 | 981,68854 | 681,09873 | 1062,57411 | €513,53 | €1.540,60 | €49,15 | €-20,67 |
| 1H Fast Long Btc 1 3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,18058 | 0,18058 | 0,15891 | 0,12129 | 0,21308 | €136,45 | €409,35 | €49,12 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,28046 | 2,22100 | 2,20450 | 1,53171 | 2,39439 | €494,04 | €1.482,12 | €49,37 | €-38,64 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DASH | LONG | Momentum / breakout | 60m | 3,0x | 68,92378 | 66,27000 | 65,10624 | 46,29381 | 74,65009 | €8,55 | €25,66 | €1,42 | €-0,99 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,22344 | 2,22100 | 2,15077 | 1,49341 | 2,33246 | €23,87 | €71,62 | €2,34 | €-0,08 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08451 | 0,08551 | 0,08595 | 0,11226 | 0,08164 | €28,42 | €85,25 | €1,45 | €-1,01 |
| 1H Fast Tp2 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,20444 | 2,22100 | 2,20958 | 1,48065 | 2,34796 | €439,21 | €1.317,64 | €0,00 | €9,90 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V2 | NEAR | LONG | Momentum / breakout V2 | 60m | 3,0x | 2,22144 | 2,22100 | 2,14439 | 1,49207 | 2,33703 | €507,73 | €1.523,18 | €52,84 | €-0,30 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €-0,00 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1014,04277 | 1000,44000 | 981,68854 | 681,09873 | 1062,57411 | €463,92 | €1.391,77 | €44,41 | €-18,67 |
| 1H Fast V3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,18113 | 0,18113 | 0,15939 | 0,12166 | 0,21373 | €123,65 | €370,96 | €44,51 | €0,00 |
| 1H Fast V3 Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,28046 | 2,22100 | 2,20450 | 1,53171 | 2,39439 | €447,88 | €1.343,64 | €44,75 | €-35,03 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1024,89494 | 1000,44000 | 985,98442 | 688,38777 | 1083,26071 | €25,95 | €77,86 | €2,96 | €-1,86 |
| 1H Fast V3 Nohigh V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22344 | 2,22100 | 2,15077 | 1,49341 | 2,33246 | €25,86 | €77,58 | €2,54 | €-0,09 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1024,89494 | 1000,44000 | 985,98442 | 688,38777 | 1083,26071 | €21,31 | €63,93 | €2,43 | €-1,53 |
| 1H Fast V3 Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22144 | 2,22100 | 2,14439 | 1,49207 | 2,33703 | €9,64 | €28,92 | €1,00 | €-0,01 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1014,04277 | 1000,44000 | 981,68854 | 681,09873 | 1062,57411 | €511,92 | €1.535,77 | €49,00 | €-20,60 |
| 1H Fast V3 Long Nohigh Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,28046 | 2,22100 | 2,20450 | 1,53171 | 2,39439 | €494,23 | €1.482,70 | €49,38 | €-38,66 |
| 1H Fast V3 Long Nohigh Cap75 V1 | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 68,92378 | 66,27000 | 65,10624 | 46,29381 | 74,65009 | €14,96 | €44,89 | €2,49 | €-1,73 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1024,89494 | 1000,44000 | 985,98442 | 688,38777 | 1083,26071 | €29,98 | €89,94 | €3,41 | €-2,15 |
| 1H Fast V3 No Esports Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22144 | 2,22100 | 2,14439 | 1,49207 | 2,33703 | €9,92 | €29,77 | €1,03 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08487 | 0,08551 | 0,08632 | 0,11274 | 0,08270 | €1.001,35 | €3.004,06 | €51,28 | €-22,55 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1024,89494 | 1000,44000 | 985,98442 | 688,38777 | 1083,26071 | €451,20 | €1.353,60 | €51,39 | €-32,30 |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,19844 | 2,22100 | 2,20433 | 1,47662 | 2,31468 | €494,21 | €1.482,64 | €0,00 | €15,21 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1014,04277 | 1000,44000 | 981,68854 | 681,09873 | 1062,57411 | €507,22 | €1.521,66 | €48,55 | €-20,41 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,18058 | 0,18058 | 0,15891 | 0,12129 | 0,21308 | €8,54 | €25,63 | €3,08 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,28046 | 2,22100 | 2,20450 | 1,53171 | 2,39439 | €489,69 | €1.469,07 | €48,93 | €-38,30 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2454,35000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,38 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 84,46600 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,80 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08551 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €2,07 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 102,09300 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,44 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €0,00 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 6,38428 | 6,38428 | 6,10071 | 3,22406 | 7,00812 | €19,98 | €39,97 | €1,78 | €0,00 |
| Forza relativa 1H V1 | DOGE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,08451 | 0,08551 | 0,08636 | 0,12635 | 0,08044 | €23,93 | €47,85 | €1,05 | €-0,56 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,01620 | 0,01715 | 0,01620 | 0,00818 | 0,02048 | €173,99 | €347,98 | €0,00 | €20,31 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,28046 | 2,22100 | 2,18280 | 1,15163 | 2,49530 | €15,53 | €31,06 | €1,33 | €-0,81 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1031,18620 | 1000,44000 | 989,89687 | 520,74903 | 1122,02270 | €13,56 | €27,12 | €1,09 | €-0,81 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 101,45470 | 102,09300 | 103,62088 | 151,67478 | 96,03926 | €1.363,99 | €2.727,98 | €58,25 | €-17,16 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €-0,00 |
| Benchmark Donchian breakout 1H | ZEC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1039,04777 | 1000,44000 | 986,46311 | 524,71912 | 1170,50941 | €43,72 | €87,44 | €4,43 | €-3,25 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 101,45470 | 102,09300 | 103,62088 | 151,67478 | 96,03926 | €1.331,88 | €2.663,75 | €56,87 | €-16,76 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ZEC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1039,04777 | 1000,44000 | 986,46311 | 524,71912 | 1170,50941 | €42,69 | €85,38 | €4,32 | €-3,17 |
| Benchmark Bollinger mean reversion 1H | NEAR | SHORT | Bollinger mean reversion | 60m | 2,0x | 2,22056 | 2,22100 | 2,30308 | 3,31973 | 2,09677 | €570,99 | €1.141,97 | €42,44 | €-0,23 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €0,00 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 101,68466 | 102,09300 | 103,37281 | 152,01857 | 97,97073 | €36,35 | €72,71 | €1,21 | €-0,29 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1124,95054 | €14,35 | €28,69 | €1,40 | €-0,68 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €0,00 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 2,22144 | 2,22100 | 2,12346 | 1,12183 | 2,41742 | €32,93 | €65,86 | €2,91 | €-0,01 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,22100 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €2,25 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 6,38428 | 6,38428 | 6,10071 | 3,22406 | 6,95141 | €543,48 | €1.086,95 | €48,28 | €0,00 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1012,11238 | 1000,44000 | 973,83876 | 511,11675 | 1088,65965 | €79,49 | €158,98 | €6,01 | €-1,83 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,22100 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €2,25 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 6,38428 | 6,38428 | 6,10071 | 3,22406 | 6,95141 | €543,48 | €1.086,95 | €48,28 | €0,00 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1012,11238 | 1000,44000 | 973,83876 | 511,11675 | 1088,65965 | €79,49 | €158,98 | €6,01 | €-1,83 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €17,77 | €35,53 | €1,73 | €-0,85 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €16,65 | €33,31 | €1,63 | €-0,79 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €26,35 | €52,71 | €2,57 | €-1,26 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €448,24 | €896,49 | €43,76 | €-21,39 |
| Scanner Top5 Btc Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,22144 | 2,22100 | 2,12237 | 1,12183 | 2,43940 | €12,72 | €25,44 | €1,13 | €-0,01 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €457,17 | €914,33 | €44,63 | €-21,82 |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,12142 | 2,22100 | 2,19451 | 1,07132 | 2,32865 | €491,87 | €983,74 | €0,00 | €46,18 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €25,74 | €51,49 | €2,51 | €-1,23 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1039,04777 | 1000,44000 | 991,72157 | 524,71912 | 1143,16539 | €27,04 | €54,09 | €2,46 | €-2,01 |
| Scanner Top5 Btc Guard Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,22344 | 2,22100 | 2,13000 | 1,12284 | 2,42902 | €14,83 | €29,66 | €1,25 | €-0,03 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1039,04777 | 1000,44000 | 991,72157 | 524,71912 | 1143,16539 | €486,84 | €973,68 | €44,35 | €-36,18 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,12142 | 2,22100 | 2,19451 | 1,07132 | 2,32865 | €498,13 | €996,25 | €0,00 | €46,76 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 6,29526 | 6,29526 | 6,00645 | 3,17911 | 7,16168 | €16,24 | €32,48 | €1,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,13143 | 2,22100 | 2,19547 | 1,07637 | 2,41184 | €13,68 | €27,36 | €0,00 | €1,15 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 6,29526 | 6,29526 | 6,00645 | 3,17911 | 7,16168 | €16,25 | €32,50 | €1,49 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,13143 | 2,22100 | 2,19547 | 1,07637 | 2,41184 | €13,69 | €27,37 | €0,00 | €1,15 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08465 | 0,08551 | 0,08601 | 0,12656 | 0,08127 | €1.515,66 | €3.031,33 | €48,50 | €-30,69 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1014,75291 | 1000,44000 | 971,43704 | 512,45022 | 1110,04783 | €12,57 | €25,14 | €1,07 | €-0,35 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €0,00 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 6,44429 | 6,44429 | 6,15558 | 3,25437 | 7,07944 | €18,75 | €37,49 | €1,68 | €0,00 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1134,95611 | €511,68 | €1.023,36 | €49,95 | €-24,42 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 2,22144 | 2,22100 | 2,12346 | 1,12183 | 2,43702 | €40,95 | €81,89 | €3,61 | €-0,02 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €0,00 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,37427 | 6,37427 | 6,08628 | 3,21901 | 6,95026 | €22,51 | €45,01 | €2,03 | €0,00 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €0,00 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1124,95054 | €20,01 | €40,02 | €1,95 | €-0,95 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 101,45470 | 102,09300 | 103,40426 | 151,67478 | 97,55559 | €1.241,19 | €2.482,39 | €47,70 | €-15,62 |
| Combo Adaptive Regime V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08451 | 0,08551 | 0,08636 | 0,12635 | 0,08081 | €20,78 | €41,55 | €0,91 | €-0,49 |
| Combo Adaptive Regime V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1039,30782 | 1000,44000 | 990,17944 | 524,85045 | 1137,56458 | €497,65 | €995,29 | €47,05 | €-37,22 |
| Combo Adaptive Regime V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,22144 | 2,22100 | 2,12346 | 1,12183 | 2,41742 | €504,48 | €1.008,96 | €44,51 | €-0,20 |
| Combo Adaptive Quality7 Regime V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1039,30782 | 1000,44000 | 990,17944 | 524,85045 | 1137,56458 | €509,54 | €1.019,09 | €48,17 | €-38,11 |
| Combo Adaptive Quality7 Regime V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,23245 | 2,22100 | 2,13521 | 1,12739 | 2,42693 | €554,11 | €1.108,22 | €48,27 | €-5,68 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,22100 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €86,57 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €0,00 |
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,37427 | 6,37427 | 6,08628 | 3,21901 | 6,95026 | €20,62 | €41,23 | €1,86 | €0,00 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1124,95054 | €15,92 | €31,85 | €1,55 | €-0,76 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,22144 | 2,22100 | 2,12346 | 1,12183 | 2,41742 | €45,81 | €91,62 | €4,04 | €-0,02 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1039,30782 | 1000,44000 | 990,17944 | 524,85045 | 1137,56458 | €516,03 | €1.032,07 | €48,79 | €-38,60 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,23245 | 2,22100 | 2,13521 | 1,12739 | 2,42693 | €561,17 | €1.122,34 | €48,89 | €-5,75 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €0,00 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,29526 | 6,29526 | 6,00645 | 3,17911 | 7,16168 | €29,55 | €59,11 | €2,71 | €0,00 |
| Combo Adaptive Runner25 V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 101,45470 | 102,09300 | 103,40426 | 151,67478 | 95,60603 | €1.200,25 | €2.400,50 | €46,13 | €-15,10 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1174,97835 | €22,19 | €44,38 | €2,17 | €-1,06 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €0,00 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,29526 | 6,29526 | 6,00645 | 3,17911 | 7,16168 | €29,02 | €58,04 | €2,66 | €0,00 |
| Combo Adaptive Tp3 V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 101,45470 | 102,09300 | 103,40426 | 151,67478 | 95,60603 | €1.177,80 | €2.355,59 | €45,27 | €-14,82 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1024,89494 | 1000,44000 | 974,86713 | 517,57194 | 1174,97835 | €21,77 | €43,55 | €2,13 | €-1,04 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80800,35684 | 79615,00000 | 78530,68128 | 40804,18020 | 86474,54655 | €887,05 | €1.774,10 | €49,83 | €-26,03 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80800,35684 | 79615,00000 | 78530,68128 | 40804,18020 | 87155,44873 | €882,31 | €1.764,61 | €49,57 | €-25,89 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80768,04316 | 79615,00000 | 82830,55933 | 120748,22452 | 77055,51340 | €985,68 | €1.971,36 | €50,34 | €28,14 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80800,35684 | 79615,00000 | 78324,34707 | 40804,18020 | 86990,38168 | €817,27 | €1.634,54 | €50,09 | €-23,98 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 101,68466 | 102,09300 | 103,20399 | 135,07112 | 98,64599 | €1.119,19 | €3.357,58 | €50,17 | €-13,48 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 101,45470 | 102,09300 | 103,18765 | 134,76567 | 97,98882 | €1.010,51 | €3.031,53 | €51,78 | €-19,07 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 102,09300 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €-23,60 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 101,45470 | 102,09300 | 103,40426 | 134,76567 | 97,55559 | €864,62 | €2.593,86 | €49,84 | €-16,32 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2454,35000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €-24,85 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08465 | 0,08551 | 0,08587 | 0,11245 | 0,08222 | €1.157,72 | €3.473,16 | €50,01 | €-35,16 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €0,00 |
| Master Adaptive V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,44429 | 6,15558 | 3,25437 | 7,02170 | €13,59 | €27,17 | €1,22 | €0,00 |
| Master Adaptive V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22100 | 2,13000 | 1,12284 | 2,41033 | €25,40 | €50,81 | €2,14 | €-0,06 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 986,20720 | 1000,44000 | 946,04592 | 498,03464 | 1066,52976 | €569,23 | €1.138,47 | €46,36 | €16,43 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,12142 | 2,22100 | 2,02723 | 1,07132 | 2,30981 | €24,83 | €49,65 | €2,20 | €2,33 |
| Master Adaptive No Alt V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 66,27000 | 64,01551 | 34,80651 | 78,74032 | €315,67 | €631,34 | €44,96 | €-24,31 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 986,20720 | 1000,44000 | 946,04592 | 498,03464 | 1066,52976 | €547,71 | €1.095,42 | €44,61 | €15,81 |
| Master Adaptive Strict3 V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 66,27000 | 64,01551 | 34,80651 | 78,74032 | €31,26 | €62,52 | €4,45 | €-2,41 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €0,00 |
| Master Adaptive Gb20 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,44429 | 6,15558 | 3,25437 | 7,02170 | €13,41 | €26,82 | €1,20 | €0,00 |
| Master Adaptive Gb20 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22100 | 2,13000 | 1,12284 | 2,41033 | €24,97 | €49,93 | €2,10 | €-0,05 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,75415 | 0,73459 | 0,38085 | 0,81282 | €26,15 | €52,29 | €1,36 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €0,00 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,22100 | 2,12346 | 1,12183 | 2,51541 | €477,69 | €955,38 | €42,14 | €-0,19 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,22100 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €10,40 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 101,45470 | 102,09300 | 103,40426 | 151,67478 | 97,55559 | €18,99 | €37,99 | €0,73 | €-0,24 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €0,00 |
| Master Adaptive Gb20 Be V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,44429 | 6,15558 | 3,25437 | 7,02170 | €13,65 | €27,31 | €1,22 | €0,00 |
| Master Adaptive Gb20 Be V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22100 | 2,13000 | 1,12284 | 2,41033 | €25,53 | €51,06 | €2,15 | €-0,06 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €0,00 |
| Master Adaptive Gb20 Partial V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,44429 | 6,44429 | 6,15558 | 3,25437 | 7,02170 | €13,64 | €27,28 | €1,22 | €0,00 |
| Master Adaptive Gb20 Partial V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22100 | 2,13000 | 1,12284 | 2,41033 | €25,50 | €51,01 | €2,14 | €-0,06 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 6,29726 | 6,29726 | 6,08916 | 3,18012 | 6,85220 | €29,83 | €59,65 | €1,97 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 986,20720 | 1000,44000 | 956,08624 | 498,03464 | 1066,52976 | €60,66 | €121,33 | €3,71 | €1,75 |
| Master Adaptive Gb20 Loss Cap V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,22100 | 2,14795 | 1,12183 | 2,41742 | €689,28 | €1.378,56 | €45,61 | €-0,28 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08487 | 0,08551 | 0,08632 | 0,11274 | 0,08270 | €40,30 | €120,91 | €2,06 | €-0,91 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1024,65489 | 1000,44000 | 986,70498 | 688,22653 | 1081,57975 | €471,29 | €1.413,88 | €52,37 | €-33,41 |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,19844 | 2,22100 | 2,20433 | 1,47662 | 2,31468 | €9,45 | €28,36 | €0,00 | €0,29 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01715 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €297,37 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2454,35000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,20 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16389 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €7,87 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,86517 | 5,86517 | 5,34904 | 3,93944 | 6,89744 | €216,26 | €648,78 | €57,09 | €0,00 |
| Main Side Regime Guard V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1000,64009 | 1000,44000 | 928,00073 | 672,09659 | 1145,91879 | €28,12 | €84,36 | €6,12 | €-0,02 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16389 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €7,37 |
| Main Dynamic Asset Selector V1 | USELESS | LONG | Confluenza trend | 240m | 3,0x | 0,22449 | 0,23283 | 0,19756 | 0,15079 | 0,27837 | €141,14 | €423,43 | €50,81 | €15,72 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08451 | 0,08551 | 0,08657 | 0,12635 | 0,07999 | €24,43 | €48,87 | €1,19 | €-0,58 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 1039,30782 | 1000,44000 | 984,72072 | 524,85045 | 1159,39942 | €476,59 | €953,19 | €50,06 | €-35,65 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €0,00 |
| 1H Balanced V3 Long Only V1 | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 101,68466 | 102,09300 | 103,20399 | 135,07112 | 98,64599 | €14,00 | €42,00 | €0,63 | €-0,17 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1016,76331 | 1000,44000 | 973,58489 | 682,92602 | 1103,12014 | €13,72 | €41,17 | €1,75 | €-0,66 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08465 | 0,08551 | 0,08587 | 0,11245 | 0,08222 | €15,16 | €45,47 | €0,65 | €-0,46 |
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
| Scanner Top10 Long | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-3,18 | -1,07 | STOP_STRESS_SLIPPAGE |
| Master Adaptive V1 | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-52,48 | -1,07 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Runner25 V1 | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-46,18 | -1,07 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 V1 | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-51,79 | -1,07 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 Partial V1 | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-52,69 | -1,07 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 Be V1 | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-52,74 | -1,07 | STOP_STRESS_SLIPPAGE |
| Combo Adaptive Partial 1R V1 | DASH | LONG | 2026-09-05T07:45:00+00:00 | 66,85149 | €-4,43 | -1,07 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Tp3 V1 | DASH | LONG | 2026-09-05T07:15:00+00:00 | 68,32001 | €0,48 | 0,01 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Runner25 V1 | DASH | LONG | 2026-09-05T07:15:00+00:00 | 68,32001 | €0,48 | 0,01 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard Btc Le3 V1 | DASH | LONG | 2026-09-05T07:15:00+00:00 | 68,44732 | €22,16 | 0,48 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | DASH | LONG | 2026-09-05T07:15:00+00:00 | 68,44732 | €21,20 | 0,48 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Btc Le3 V1 | DASH | LONG | 2026-09-05T07:15:00+00:00 | 68,44732 | €20,50 | 0,48 | STOP_STRESS_SLIPPAGE |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
