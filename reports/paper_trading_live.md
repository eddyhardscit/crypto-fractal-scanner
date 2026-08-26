# Paper trading automatico KuCoin

Generato: 2026-08-26T05:32:53+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-26T05:05:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-26T05:05:30+00:00 | 2026-08-26T05:05:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-26T04:45:00+00:00 | 2026-08-26T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-26T04:00:00+00:00 | 2026-08-26T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-26T00:00:00+00:00 | 2026-08-26T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend Side Regime Guard V1 | SUI | 60m | SHORT | -5,36 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | SUI | 60m | SHORT | -5,36 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | HYPE | 240m | LONG | 6,91 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PUMP | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,30 | 6,00 | 1,70 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,39 | 6,00 | 2,61 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,67 | 6,00 | 3,33 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 2,33 | 6,00 | 3,67 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 2,21 | 6,00 | 3,79 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 0,84 | 6,00 | 5,16 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 0,79 | 6,00 | 5,21 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Forza relativa 1H V2 | DOGE | 60m | SHORT | -5,77 | 5,50 | 0,00 | OPENED | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | READY | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom 5 Short 1H | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | READY | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom10 Short | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | READY | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom15 Short | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | READY | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom20 Short | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | READY | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | DOGE | 60m | SHORT | -5,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.808,60 | -1,91% | €60,25 | €3.000,00 | 2,01% | 6 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2231 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.808,60 | €699,00 | €2.096,99 | €196,05 | €0,45 |
| TEST | Benchmark Donchian breakout 1H | 4 | €11.285,53 | €1.871,31 | €3.742,61 | €170,21 | €-4,68 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 5 | €11.199,83 | €1.258,33 | €3.774,98 | €174,05 | €-4,86 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €11.019,83 | €1.827,25 | €3.654,50 | €166,20 | €-4,57 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.012,60 | €2.836,30 | €5.672,61 | €167,99 | €26,56 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.924,92 | €457,13 | €914,26 | €107,50 | €0,00 |
| TEST | Main Side Regime Guard V1 | 5 | €10.837,66 | €527,44 | €1.582,33 | €163,22 | €34,40 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.610,42 | €1.964,70 | €5.894,11 | €211,98 | €17,69 |
| TEST | Combo Adaptive | 6 | €10.585,52 | €2.664,63 | €5.329,27 | €211,75 | €-18,86 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 4 | €10.500,08 | €924,92 | €2.774,77 | €159,90 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 4 | €10.432,62 | €918,98 | €2.756,95 | €158,88 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 2 | €10.421,07 | €693,60 | €1.387,19 | €53,51 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.350,46 | €1.572,23 | €3.144,47 | €154,89 | €-18,21 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.334,46 | €1.562,14 | €4.686,42 | €205,69 | €49,04 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 6 | €10.279,33 | €1.569,55 | €4.708,64 | €205,31 | €34,80 |
| TEST | Ampia 4H | 7 | €10.278,20 | €1.057,57 | €2.115,14 | €205,57 | €-1,06 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.236,66 | €1.164,70 | €3.494,09 | €154,36 | €5,41 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 3 | €10.229,42 | €1.907,29 | €5.721,87 | €152,63 | €55,71 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 1 | €10.201,10 | €211,07 | €422,14 | €50,66 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 2 | €10.199,18 | €426,48 | €852,97 | €100,30 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 1 | €10.195,13 | €210,95 | €421,90 | €50,63 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.192,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.179,60 | €367,30 | €734,59 | €50,97 | €-13,90 |
| TEST | Scanner Top10 Long | 1 | €10.162,30 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.161,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.127,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.084,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.059,32 | €775,58 | €1.551,16 | €50,15 | €30,53 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €10.048,23 | €727,35 | €2.182,05 | €50,23 | €3,37 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.043,12 | €648,94 | €1.297,88 | €50,35 | €-26,05 |
| TEST | Sol Ema 4H | 1 | €10.040,61 | €395,27 | €790,53 | €50,28 | €-14,96 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 6 | €10.032,26 | €1.764,47 | €3.528,95 | €150,78 | €-2,33 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.023,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 6 | €10.023,53 | €1.530,49 | €4.591,47 | €200,20 | €33,94 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.015,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.013,19 | €435,50 | €871,00 | €49,91 | €31,93 |
| TEST | Btc Donchian 1H | 0 | €10.012,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.003,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.995,27 | €870,33 | €2.610,99 | €152,06 | €-34,37 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.990,04 | €704,37 | €1.408,74 | €50,10 | €-28,28 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.974,01 | €589,49 | €1.768,46 | €49,83 | €8,83 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.952,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €9.948,38 | €725,09 | €2.175,26 | €49,74 | €4,12 |
| TEST | Sol Adaptive 1H | 0 | €9.941,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.936,98 | €487,73 | €975,47 | €49,56 | €26,75 |
| TEST | Btc Donchian 4H | 1 | €9.936,59 | €700,60 | €1.401,20 | €49,83 | €-28,13 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.912,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €9.906,81 | €672,78 | €2.018,34 | €49,56 | €-3,92 |
| TEST | Btc Ema 1H | 0 | €9.887,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.844,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.835,37 | €969,22 | €1.938,44 | €0,00 | €48,08 |
| TEST | Sol Bollinger 1H | 0 | €9.821,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 3 | €9.816,45 | €321,20 | €642,40 | €57,78 | €0,00 |
| TEST | Scanner Top20 Long | 3 | €9.816,45 | €321,20 | €642,40 | €57,78 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.813,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.791,01 | €1.018,47 | €2.036,93 | €96,56 | €0,00 |
| TEST | Combo Scanner | 3 | €9.789,73 | €1.324,91 | €2.649,82 | €145,39 | €5,56 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.787,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 2 | €9.741,76 | €143,00 | €429,00 | €49,56 | €0,00 |
| TEST | Forza relativa 1H V2 | 5 | €9.724,87 | €2.238,80 | €4.477,61 | €146,44 | €3,22 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 4 | €9.716,00 | €460,10 | €1.380,29 | €146,37 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.678,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.669,32 | €849,28 | €1.698,56 | €0,00 | €42,13 |
| TEST | Scanner Top5 Btc Guard V1 | 2 | €9.647,51 | €210,30 | €420,60 | €50,01 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 4 | €9.624,03 | €1.506,53 | €4.519,60 | €190,59 | €11,79 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.614,55 | €1.453,22 | €4.359,66 | €191,37 | €45,62 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 2 | €9.561,23 | €399,81 | €799,61 | €94,02 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €9.542,06 | €627,21 | €1.254,41 | €94,97 | €-61,06 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.466,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.453,91 | €833,22 | €2.499,65 | €143,43 | €-31,42 |
| TEST | 1H Fast V3 Long Only V1 | 3 | €9.450,15 | €690,56 | €2.071,67 | €96,58 | €0,00 |
| TEST | Bilanciata 1H V2 | 1 | €9.430,84 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 2 | €9.423,14 | €205,41 | €410,82 | €48,85 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 2 | €9.409,53 | €898,96 | €1.797,92 | €55,27 | €32,48 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.403,80 | €863,12 | €1.726,23 | €46,86 | €32,44 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.393,80 | €862,20 | €1.724,40 | €46,81 | €32,40 |
| TEST | Master Adaptive No Alt V1 | 1 | €9.385,86 | €861,47 | €1.722,94 | €46,77 | €32,37 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 2 | €9.364,02 | €326,26 | €652,52 | €49,19 | €-29,50 |
| TEST | Master Adaptive V1 | 1 | €9.357,46 | €858,86 | €1.717,73 | €46,63 | €32,28 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.349,66 | €2.236,43 | €4.472,87 | €140,71 | €32,37 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.339,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 4 | €9.336,69 | €1.932,61 | €3.865,22 | €140,27 | €-5,69 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.259,64 | €1.267,77 | €2.535,55 | €140,48 | €1,66 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 1 | €9.233,14 | €847,45 | €1.694,91 | €46,01 | €31,85 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.202,49 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.200,83 | €308,18 | €616,36 | €45,79 | €-29,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 5 | €9.083,15 | €1.977,50 | €3.955,00 | €181,43 | €4,94 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 2 | €9.075,96 | €596,57 | €1.193,14 | €90,33 | €-58,08 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.009,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €8.986,17 | €720,09 | €1.440,17 | €45,25 | €-2,39 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.808,60 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.285,53 | €1.291,64 | 102 | 102 | 49,02% | 1,56 | €12,66 | 5,51% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.199,83 | €1.207,08 | 142 | 142 | 53,52% | 1,44 | €8,50 | 4,41% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.019,83 | €1.025,79 | 70 | 70 | 48,57% | 1,71 | €14,65 | 5,51% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.012,60 | €989,42 | 106 | 106 | 54,72% | 1,49 | €9,33 | 5,93% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.924,92 | €925,50 | 135 | 135 | 48,89% | 1,35 | €6,86 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.837,66 | €804,71 | 34 | 34 | 55,88% | 2,29 | €23,67 | 3,82% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.610,42 | €596,37 | 204 | 204 | 48,04% | 1,15 | €2,92 | 6,95% |
| TEST | Combo Adaptive | Combo Adaptive | €10.585,52 | €608,25 | 143 | 143 | 45,45% | 1,25 | €4,25 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.500,08 | €501,85 | 188 | 188 | 50,53% | 1,16 | €2,67 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.432,62 | €434,38 | 232 | 232 | 44,83% | 1,10 | €1,87 | 9,48% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.421,07 | €421,91 | 117 | 117 | 47,86% | 1,16 | €3,61 | 6,47% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.350,46 | €371,19 | 113 | 113 | 47,79% | 1,16 | €3,28 | 8,68% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.334,46 | €288,23 | 66 | 66 | 46,97% | 1,20 | €4,37 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.279,33 | €247,35 | 127 | 127 | 44,88% | 1,09 | €1,95 | 7,10% |
| TEST | Ampia 4H | Confluenza trend | €10.278,20 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.236,66 | €233,33 | 222 | 222 | 40,54% | 1,06 | €1,05 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.229,42 | €177,14 | 45 | 45 | 51,11% | 1,18 | €3,94 | 4,50% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.201,10 | €201,36 | 102 | 102 | 42,16% | 1,08 | €1,97 | 11,78% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.199,18 | €199,73 | 122 | 122 | 45,08% | 1,08 | €1,64 | 11,27% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.195,13 | €195,39 | 106 | 106 | 42,45% | 1,08 | €1,84 | 12,06% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.192,62 | €192,62 | 13 | 13 | 53,85% | 1,78 | €14,82 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.179,60 | €193,98 | 7 | 7 | 57,14% | 2,72 | €27,71 | 1,01% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.162,30 | €163,11 | 124 | 124 | 49,19% | 1,07 | €1,32 | 10,31% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.161,45 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,04% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.127,83 | €127,83 | 46 | 41 | 45,65% | 1,11 | €2,78 | 3,89% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 1H | Trend following EMA | €10.084,65 | €84,65 | 14 | 14 | 42,86% | 1,22 | €6,05 | 3,33% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.059,32 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.048,23 | €46,17 | 9 | 9 | 55,56% | 1,19 | €5,13 | 1,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.043,12 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Sol Ema 4H | Trend following EMA | €10.040,61 | €56,08 | 8 | 8 | 37,50% | 1,26 | €7,01 | 2,27% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.032,26 | €36,68 | 147 | 147 | 44,22% | 1,01 | €0,25 | 8,69% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.023,61 | €23,61 | 8 | 8 | 50,00% | 1,14 | €2,95 | 1,13% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.023,53 | €-7,65 | 91 | 91 | 43,96% | 1,00 | €-0,08 | 7,10% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.015,51 | €15,51 | 15 | 15 | 40,00% | 1,32 | €1,03 | 0,53% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.013,19 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,23% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.012,73 | €12,73 | 9 | 9 | 55,56% | 1,06 | €1,41 | 1,49% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.003,10 | €3,10 | 15 | 15 | 40,00% | 1,32 | €0,21 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.995,27 | €32,41 | 149 | 149 | 42,95% | 1,01 | €0,22 | 9,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Btc Ema 4H | Trend following EMA | €9.990,04 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Ema 1H | Trend following EMA | €9.974,01 | €-33,77 | 16 | 16 | 56,25% | 0,92 | €-2,11 | 2,77% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,43 | €-47,57 | 15 | 15 | 40,00% | 0,45 | €-3,17 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.948,38 | €-54,43 | 57 | 57 | 42,11% | 0,96 | €-0,95 | 3,73% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.941,22 | €-58,78 | 15 | 15 | 40,00% | 0,87 | €-3,92 | 4,59% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Eth Ema 4H | Trend following EMA | €9.936,98 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.936,59 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.912,24 | €-87,76 | 39 | 39 | 46,15% | 0,91 | €-2,25 | 4,21% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.906,81 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | Btc Ema 1H | Trend following EMA | €9.887,95 | €-112,05 | 12 | 12 | 33,33% | 0,70 | €-9,34 | 1,94% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.844,63 | €-155,37 | 13 | 13 | 38,46% | 0,66 | €-11,95 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.835,37 | €-211,74 | 56 | 56 | 46,43% | 0,85 | €-3,78 | 5,38% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.821,20 | €-178,80 | 11 | 11 | 36,36% | 0,61 | €-16,25 | 2,37% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.816,45 | €-183,14 | 121 | 121 | 48,76% | 0,92 | €-1,51 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.816,45 | €-183,14 | 121 | 121 | 48,76% | 0,92 | €-1,51 | 10,31% |
| TEST | Eth Ema 1H | Trend following EMA | €9.813,58 | €-186,42 | 18 | 18 | 38,89% | 0,71 | €-10,36 | 4,80% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.791,01 | €-207,77 | 79 | 79 | 39,24% | 0,89 | €-2,63 | 8,88% |
| TEST | Combo Scanner | Combo Scanner | €9.789,73 | €-214,22 | 126 | 126 | 44,44% | 0,93 | €-1,70 | 11,38% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.787,56 | €-212,44 | 39 | 39 | 41,03% | 0,79 | €-5,45 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.741,76 | €-257,98 | 151 | 151 | 43,05% | 0,92 | €-1,71 | 10,60% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.724,87 | €-275,66 | 109 | 103 | 41,28% | 0,92 | €-2,53 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.716,00 | €-283,05 | 202 | 202 | 43,56% | 0,93 | €-1,40 | 9,00% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.678,07 | €-321,93 | 13 | 13 | 23,08% | 0,47 | €-24,76 | 3,44% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.669,32 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,93% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.647,51 | €-352,24 | 104 | 104 | 39,42% | 0,86 | €-3,39 | 7,34% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.624,03 | €-384,98 | 97 | 97 | 45,36% | 0,82 | €-3,97 | 9,26% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.614,55 | €-428,45 | 116 | 116 | 41,38% | 0,84 | €-3,69 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.561,23 | €-438,26 | 114 | 114 | 43,86% | 0,81 | €-3,84 | 12,28% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.542,06 | €-395,00 | 20 | 20 | 25,00% | 0,39 | €-19,75 | 6,01% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.466,98 | €-533,02 | 79 | 79 | 39,24% | 0,76 | €-6,75 | 6,59% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.453,91 | €-512,05 | 105 | 105 | 42,86% | 0,75 | €-4,88 | 8,85% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.450,15 | €-548,61 | 163 | 163 | 40,49% | 0,85 | €-3,37 | 12,52% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.430,84 | €-568,34 | 103 | 94 | 42,72% | 0,75 | €-5,52 | 8,84% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.423,14 | €-576,61 | 121 | 121 | 40,50% | 0,80 | €-4,77 | 8,78% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.409,53 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.403,80 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.393,80 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.385,86 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.364,02 | €-605,46 | 67 | 67 | 37,31% | 0,71 | €-9,04 | 8,68% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.357,46 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.349,66 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.339,79 | €-660,21 | 84 | 84 | 44,05% | 0,74 | €-7,86 | 7,90% |
| TEST | Combo Trend | Combo Trend | €9.336,69 | €-654,75 | 153 | 153 | 38,56% | 0,82 | €-4,28 | 10,85% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.259,64 | €-740,48 | 124 | 124 | 38,71% | 0,71 | €-5,97 | 12,31% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.233,14 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.202,49 | €-797,27 | 43 | 43 | 23,26% | 0,52 | €-18,54 | 11,41% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.200,83 | €-769,18 | 83 | 83 | 37,35% | 0,67 | €-9,27 | 7,99% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.083,15 | €-919,43 | 156 | 156 | 40,38% | 0,71 | €-5,89 | 15,45% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.075,96 | €-864,17 | 66 | 66 | 33,33% | 0,55 | €-13,09 | 11,72% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.009,17 | €-990,83 | 54 | 54 | 27,78% | 0,58 | €-18,35 | 11,51% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.986,17 | €-1.010,57 | 45 | 45 | 35,56% | 0,47 | €-22,46 | 11,90% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
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
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,43118 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-0,52 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 81,86900 | 73,04357 | 52,97621 | 90,53117 | €8,52 | €25,56 | €1,89 | €0,97 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 81,26625 | 81,86900 | 78,80918 | 54,58383 | 86,18038 | €529,92 | €1.589,76 | €48,07 | €11,79 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 787,01000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €-15,17 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,43118 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €-17,94 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,77 | €26,32 | €2,02 | €-1,26 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08603 | 0,08620 | 0,08788 | 0,11428 | 0,08326 | €833,51 | €2.500,52 | €53,72 | €-4,86 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14368 | 0,14136 | 0,14879 | 0,19086 | 0,13602 | €479,05 | €1.437,14 | €51,08 | €23,24 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €28,33 | €85,00 | €2,49 | €0,11 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08378 | €771,97 | €2.315,90 | €50,76 | €11,57 |
| 1H Fast Nohigh Cap75 V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,75675 | 0,75980 | 0,77558 | 1,00521 | 0,72850 | €9,34 | €28,03 | €0,70 | €-0,11 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,71434 | 81,86900 | 79,84602 | 54,88480 | 84,51683 | €725,09 | €2.175,26 | €49,74 | €4,12 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08378 | €799,42 | €2.398,25 | €52,56 | €11,98 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,67433 | 81,86900 | 79,87515 | 54,85793 | 84,37311 | €799,39 | €2.398,18 | €52,83 | €5,72 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08284 | €31,76 | €95,27 | €2,09 | €0,48 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,67433 | 81,86900 | 79,87515 | 54,85793 | 85,27270 | €690,37 | €2.071,10 | €45,62 | €4,94 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08378 | €727,86 | €2.183,58 | €47,86 | €10,91 |
| 1H Fast V3 Nohigh V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14512 | 0,14136 | 0,15033 | 0,19277 | 0,13730 | €444,08 | €1.332,24 | €47,85 | €34,53 |
| 1H Fast V3 Nohigh V1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76265 | 0,75980 | 0,78221 | 1,01305 | 0,73331 | €17,04 | €51,11 | €1,31 | €0,19 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08378 | €773,95 | €2.321,85 | €50,89 | €11,60 |
| 1H Fast V3 No Esports Stress Guard V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14512 | 0,14136 | 0,15033 | 0,19277 | 0,13730 | €472,20 | €1.416,60 | €50,88 | €36,71 |
| 1H Fast V3 No Esports Stress Guard V1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76265 | 0,75980 | 0,78221 | 1,01305 | 0,73331 | €661,14 | €1.983,42 | €50,87 | €7,41 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2455,57000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,40 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 81,86900 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,89 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08620 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-2,35 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20989 | 0,20950 | 0,21617 | 0,31379 | 0,19609 | €816,97 | €1.633,95 | €48,86 | €3,07 |
| Forza relativa 1H V2 | ENA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14368 | 0,14136 | 0,15025 | 0,21481 | 0,12924 | €17,01 | €34,01 | €1,55 | €0,55 |
| Forza relativa 1H V2 | DOGE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,08618 | 0,08620 | 0,08820 | 0,12884 | 0,08173 | €999,81 | €1.999,61 | €46,91 | €-0,40 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 781,01377 | 787,01000 | 817,07631 | 1167,61558 | 690,85740 | €71,60 | €143,20 | €6,61 | €-1,10 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08603 | 0,08620 | 0,08867 | 0,12862 | 0,07943 | €921,23 | €1.842,45 | €56,55 | €-3,58 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 781,01377 | 787,01000 | 817,07631 | 1167,61558 | 690,85740 | €69,91 | €139,83 | €6,46 | €-1,07 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08603 | 0,08620 | 0,08867 | 0,12862 | 0,07943 | €899,54 | €1.799,07 | €55,22 | €-3,50 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 787,01000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-0,90 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,20989 | 0,20950 | 0,21687 | 0,31379 | 0,19455 | €681,63 | €1.363,26 | €45,30 | €2,56 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,43118 | 1,39078 | 0,76104 | 1,76273 | €297,64 | €595,28 | €45,91 | €-29,95 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €298,93 | €597,86 | €44,42 | €-28,13 |
| Scanner Top5 Btc Btc 2 3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,43118 | 1,39078 | 0,76104 | 1,76273 | €312,93 | €625,85 | €48,27 | €-31,49 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €314,28 | €628,56 | €46,70 | €-29,57 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €313,56 | €627,12 | €46,59 | €-29,50 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,18 | €616,36 | €45,79 | €-29,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08839 | 0,08620 | 0,08728 | 0,13215 | 0,08213 | €849,28 | €1.698,56 | €0,00 | €42,13 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 787,01000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-12,82 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08663 | 0,08620 | 0,08935 | 0,12952 | 0,08067 | €744,01 | €1.488,02 | €46,59 | €7,43 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,75965 | 0,75980 | 0,78302 | 1,13567 | 0,70823 | €747,28 | €1.494,56 | €45,98 | €-0,30 |
| Combo Mean Reversion | PEPE | LONG | Combo Mean Reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €720,09 | €1.440,17 | €45,25 | €-2,39 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,08646 | 0,08620 | 0,08878 | 0,12926 | 0,08136 | €915,73 | €1.831,46 | €49,17 | €5,56 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 787,01000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-15,95 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,75865 | 0,75980 | 0,78302 | 1,13418 | 0,70990 | €810,63 | €1.621,25 | €52,08 | €-2,46 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08618 | 0,08620 | 0,08820 | 0,12884 | 0,08214 | €1.119,19 | €2.238,39 | €52,51 | €-0,45 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,75865 | 0,75980 | 0,78302 | 1,13418 | 0,70990 | €707,81 | €1.415,61 | €45,48 | €-2,15 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08663 | 0,08620 | 0,08907 | 0,12952 | 0,08175 | €709,61 | €1.419,21 | €39,99 | €7,09 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Regime V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08839 | 0,08620 | 0,08703 | 0,13215 | 0,08388 | €969,22 | €1.938,44 | €0,00 | €48,08 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,75865 | 0,75980 | 0,78302 | 1,13418 | 0,70990 | €781,17 | €1.562,33 | €50,19 | €-2,37 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20989 | 0,20950 | 0,21617 | 0,31379 | 0,19734 | €18,50 | €37,00 | €1,11 | €0,07 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08618 | 0,08620 | 0,08820 | 0,12884 | 0,08214 | €57,16 | €114,31 | €2,68 | €-0,02 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 78742,20000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €-28,28 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 78742,20000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €-28,13 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 78742,20000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €30,53 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 78742,20000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €-26,05 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 98,32066 | 96,46000 | 92,06715 | 49,65193 | 113,95442 | €395,27 | €790,53 | €50,28 | €-14,96 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 100,13097 | 96,46000 | 105,86849 | 149,69580 | 89,80342 | €435,50 | €871,00 | €49,91 | €31,93 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 98,32066 | 96,46000 | 91,49865 | 49,65193 | 115,37567 | €367,30 | €734,59 | €50,97 | €-13,90 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2455,57000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €26,75 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08663 | 0,08620 | 0,08907 | 0,11508 | 0,08175 | €589,49 | €1.768,46 | €49,83 | €8,83 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,08603 | 0,08620 | 0,08815 | 0,11428 | 0,08181 | €672,78 | €2.018,34 | €49,56 | €-3,92 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08607 | 0,08620 | 0,08409 | 0,05781 | 0,08904 | €727,35 | €2.182,05 | €50,23 | €3,37 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 84,72212 | €858,86 | €1.717,73 | €46,63 | €32,28 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 84,72212 | €861,47 | €1.722,94 | €46,77 | €32,37 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 84,72212 | €861,38 | €1.722,77 | €46,77 | €32,37 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1225,56490 | 1225,56490 | 1201,34438 | 618,91027 | 1274,00594 | €1.177,55 | €2.355,09 | €46,54 | €0,00 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 84,72212 | €847,45 | €1.694,91 | €46,01 | €31,85 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €32,48 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 787,01000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-15,84 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,75865 | 0,75980 | 0,78302 | 1,13418 | 0,70990 | €779,82 | €1.559,63 | €50,11 | €-2,37 |
| Master Adaptive Gb20 Be V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 84,72212 | €863,12 | €1.726,23 | €46,86 | €32,44 |
| Master Adaptive Gb20 Partial V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 81,86900 | 78,17754 | 40,58133 | 84,72212 | €862,20 | €1.724,40 | €46,81 | €32,40 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08378 | €782,36 | €2.347,08 | €51,44 | €11,72 |
| 1H Fast V3 Nohigh Regime Guard V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14512 | 0,14136 | 0,15033 | 0,19277 | 0,13730 | €477,33 | €1.431,99 | €51,43 | €37,11 |
| 1H Fast V3 Nohigh Regime Guard V1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76265 | 0,75980 | 0,78221 | 1,01305 | 0,73331 | €18,45 | €55,34 | €1,42 | €0,21 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 81,86900 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €35,22 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,43118 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-1,04 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2455,57000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,22 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08663 | 0,08620 | 0,08935 | 0,12952 | 0,08067 | €881,95 | €1.763,89 | €55,22 | €8,81 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,44683 | 1,43118 | 1,49448 | 2,16301 | 1,34200 | €837,02 | €1.674,03 | €55,13 | €18,11 |
| Combo Trend Side Regime Guard V1 | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,75965 | 0,75980 | 0,78302 | 1,13567 | 0,70823 | €886,67 | €1.773,33 | €54,56 | €-0,35 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14368 | 0,14136 | 0,14879 | 0,19086 | 0,13602 | €467,13 | €1.401,38 | €49,81 | €22,66 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €27,63 | €82,88 | €2,43 | €0,10 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08663 | 0,08620 | 0,08853 | 0,11508 | 0,08378 | €752,76 | €2.258,27 | €49,49 | €11,28 |
| 1H Fast Nohigh Cap75 Short Only V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,75675 | 0,75980 | 0,77558 | 1,00521 | 0,72850 | €9,11 | €27,34 | €0,68 | €-0,11 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 787,01000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €-14,35 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,43118 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €-16,97 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08603 | 0,08620 | 0,08841 | 0,11428 | 0,08128 | €18,32 | €54,97 | €1,52 | €-0,11 |
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
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | 2026-08-25T21:15:00+00:00 | 764,28151 | €-2,39 | -1,04 | STOP |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | 2026-08-25T21:15:00+00:00 | 764,28151 | €-2,39 | -1,04 | STOP |
| Scanner Top5 Btc Guard Btc Le3 V1 | XRP | LONG | 2026-08-25T21:15:00+00:00 | 1,40513 | €-1,68 | -1,03 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XRP | LONG | 2026-08-25T21:15:00+00:00 | 1,40513 | €-1,65 | -1,03 | STOP |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | 2026-08-25T21:15:00+00:00 | 760,90122 | €-58,94 | -1,03 | STOP |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | 2026-08-25T21:15:00+00:00 | 0,00000 | €-58,14 | -1,02 | STOP |
| Combo Trend | PEPE | LONG | 2026-08-25T21:15:00+00:00 | 0,00000 | €-48,84 | -1,02 | STOP |
| Combo Mean Reversion | SUI | LONG | 2026-08-25T21:15:00+00:00 | 0,74848 | €-47,95 | -1,06 | STOP |
| Combo Mean Reversion | ZEC | LONG | 2026-08-25T21:15:00+00:00 | 754,11765 | €-47,22 | -1,04 | STOP |
| Combo Adaptive Mfe Trail | XRP | LONG | 2026-08-25T21:15:00+00:00 | 1,41479 | €-41,90 | -1,04 | STOP |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | 2026-08-25T21:15:00+00:00 | 0,20657 | €72,45 | 1,45 | TARGET |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | 2026-08-25T21:15:00+00:00 | 0,20657 | €68,00 | 1,45 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
