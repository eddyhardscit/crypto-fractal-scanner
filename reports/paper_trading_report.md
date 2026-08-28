# Paper trading automatico KuCoin

Generato: 2026-08-28T08:02:46+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-28T07:05:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-28T07:05:30+00:00 | 2026-08-28T07:05:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-28T06:45:00+00:00 | 2026-08-28T06:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-28T06:00:00+00:00 | 2026-08-28T06:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-28T00:00:00+00:00 | 2026-08-28T00:00:00+00:00 | 3,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,36 | 6,00 | 0,00 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | TAO | 240m | LONG | 5,82 | 6,00 | 0,18 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,49 | 6,00 | 1,51 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 3,60 | 6,00 | 2,40 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 2,60 | 6,00 | 3,40 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 2,30 | 6,00 | 3,70 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,53 | 6,00 | 4,47 | STALE_CANDLE | 3,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | 0,00 | 6,00 | 6,00 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Benchmark trend following EMA 1H | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Expanded V1 | TRUMP | 60m | LONG | 8,25 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Runner25 V1 | TRUMP | 60m | LONG | 8,25 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Side Regime Guard V1 | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 Loss Cap V1 | TRUMP | 60m | LONG | 8,25 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive No Alt V1 | ENA | 60m | LONG | 4,46 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Expanded V1 | ENA | 60m | LONG | 4,46 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | TRUMP | 60m | LONG | 8,25 | 5,50 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V1 | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | RISK_GATE | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: blocco perdita monthly raggiunto. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.864,93 | -1,35% | €116,59 | €3.000,00 | 3,89% | 6 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2382 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.864,93 | €699,00 | €2.096,99 | €194,16 | €56,81 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 5 | €11.345,14 | €563,84 | €1.691,51 | €170,37 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 3 | €11.190,04 | €921,22 | €1.842,43 | €109,41 | €-2,11 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.131,79 | €858,00 | €1.715,99 | €116,13 | €14,48 |
| TEST | Scanner Top 5 Long 1H | 4 | €11.070,19 | €511,90 | €1.023,79 | €110,47 | €55,24 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.926,58 | €899,53 | €1.799,06 | €106,84 | €-2,06 |
| TEST | Main Side Regime Guard V1 | 6 | €10.879,75 | €677,89 | €2.033,66 | €163,42 | €58,77 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.701,25 | €843,47 | €2.530,42 | €212,30 | €20,13 |
| TEST | Combo Adaptive | 6 | €10.675,17 | €985,07 | €1.970,13 | €162,16 | €-10,97 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.667,77 | €1.243,40 | €3.730,21 | €212,77 | €10,19 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.599,23 | €1.235,42 | €3.706,25 | €211,41 | €10,12 |
| TEST | Combo Adaptive Long Only V1 | 4 | €10.473,08 | €1.693,60 | €3.387,21 | €104,90 | €9,61 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 3 | €10.471,49 | €609,19 | €1.827,57 | €153,66 | €20,43 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €10.407,47 | €1.016,95 | €2.033,90 | €156,23 | €-14,03 |
| TEST | 1H Fast Tp2 V1 | 5 | €10.395,04 | €757,29 | €2.271,86 | €157,22 | €19,77 |
| TEST | Rapida 1H V2 | 0 | €10.359,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.344,68 | €1.057,57 | €2.115,14 | €205,57 | €65,26 |
| TEST | Sol Donchian 1H | 0 | €10.305,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.293,40 | €474,73 | €949,47 | €102,86 | €51,95 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.277,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.259,35 | €367,30 | €734,59 | €0,00 | €65,92 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.222,37 | €449,62 | €899,24 | €50,98 | €26,41 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.220,71 | €1.771,68 | €3.543,37 | €202,54 | €15,23 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.214,73 | €1.770,65 | €3.541,29 | €202,42 | €15,22 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 4 | €10.204,14 | €2.227,69 | €4.455,38 | €200,73 | €8,41 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.177,93 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.160,27 | €429,03 | €1.287,09 | €101,56 | €-0,41 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €10.153,18 | €1.920,85 | €3.841,70 | €147,19 | €76,05 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 3 | €10.140,52 | €413,61 | €1.240,82 | €148,08 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €10.137,17 | €597,50 | €1.792,49 | €150,44 | €19,78 |
| TEST | Sol Ema 4H | 1 | €10.126,43 | €395,27 | €790,53 | €0,00 | €70,93 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.058,90 | €648,94 | €1.297,88 | €50,35 | €-10,13 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.040,46 | €775,58 | €1.551,16 | €50,15 | €11,49 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.033,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.011,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.007,16 | €704,37 | €1.408,74 | €50,10 | €-10,99 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.992,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.988,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.962,53 | €361,10 | €722,20 | €49,74 | €15,12 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.954,28 | €487,73 | €975,47 | €0,00 | €44,17 |
| TEST | Btc Donchian 4H | 1 | €9.953,62 | €700,60 | €1.401,20 | €49,83 | €-10,93 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.931,32 | €478,97 | €957,94 | €49,65 | €1,25 |
| TEST | Doge Donchian 1H | 0 | €9.924,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €9.907,76 | €1.336,00 | €2.672,00 | €146,37 | €49,08 |
| TEST | Scanner Top20 Long | 7 | €9.907,76 | €1.336,00 | €2.672,00 | €146,37 | €49,08 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.905,36 | €581,14 | €1.743,42 | €147,13 | €19,32 |
| TEST | Combo Scanner | 4 | €9.889,79 | €458,53 | €917,05 | €98,83 | €49,93 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 3 | €9.888,18 | €403,32 | €1.209,95 | €144,39 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.874,22 | €1.549,75 | €3.099,50 | €147,54 | €14,99 |
| TEST | Eth Adaptive 1H | 0 | €9.873,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 3 | €9.850,95 | €1.031,61 | €3.094,83 | €100,21 | €-31,44 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.837,22 | €356,56 | €713,12 | €49,11 | €14,93 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.832,09 | €765,42 | €2.296,25 | €195,43 | €18,76 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.807,73 | €1.130,28 | €3.390,83 | €194,23 | €10,45 |
| TEST | Forza relativa 1H V2 | 4 | €9.804,86 | €961,34 | €1.922,67 | €146,29 | €14,88 |
| TEST | Btc Ema 1H | 1 | €9.803,39 | €1.138,16 | €3.414,47 | €49,17 | €-28,19 |
| TEST | Eth Ema 1H | 0 | €9.799,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.799,11 | €697,47 | €2.092,40 | €0,00 | €31,47 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.714,51 | €1.239,35 | €3.718,05 | €193,34 | €6,77 |
| TEST | Eth Donchian 1H | 0 | €9.709,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.708,45 | €1.370,09 | €2.740,18 | €144,99 | €7,98 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.679,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €9.649,56 | €445,04 | €890,08 | €96,43 | €48,70 |
| TEST | Master Adaptive Gb20 Be V1 | 6 | €9.619,28 | €2.958,17 | €5.916,35 | €191,69 | €15,16 |
| TEST | Master Adaptive Gb20 Partial V1 | 6 | €9.609,05 | €2.955,03 | €5.910,05 | €191,48 | €15,15 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.603,54 | €3.588,44 | €7.176,88 | €191,71 | €71,44 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 1 | €9.600,44 | €134,26 | €402,77 | €48,33 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 6 | €9.571,88 | €2.943,60 | €5.887,19 | €190,74 | €15,09 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.544,43 | €413,49 | €826,99 | €96,32 | €2,04 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.481,14 | €2.981,09 | €5.962,17 | €188,97 | €12,92 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.472,68 | €2.920,91 | €5.841,82 | €188,69 | €-5,15 |
| TEST | Bilanciata 1H V2 | 3 | €9.460,09 | €782,72 | €2.348,15 | €140,51 | €14,36 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.444,42 | €2.909,31 | €5.818,62 | €188,82 | €14,61 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 1 | €9.433,66 | €130,02 | €390,07 | €46,81 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 5 | €9.361,85 | €738,35 | €1.476,69 | €136,03 | €68,01 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 5 | €9.360,46 | €3.414,16 | €6.828,32 | €186,74 | €3,22 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €9.340,10 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.322,46 | €403,88 | €807,75 | €94,08 | €1,99 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 2 | €9.316,85 | €953,76 | €2.861,28 | €93,22 | €-28,47 |
| TEST | Combo Trend | 5 | €9.308,41 | €1.476,84 | €2.953,67 | €139,33 | €-22,13 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.215,49 | €12,70 | €25,40 | €2,60 | €2,44 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.198,97 | €1.286,85 | €2.573,71 | €139,56 | €-10,99 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 0 | €9.052,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €8.918,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €8.883,87 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.862,92 | €1.998,95 | €3.997,90 | €133,34 | €8,60 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.864,93 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.345,14 | €1.346,38 | 151 | 151 | 53,64% | 1,46 | €8,92 | 5,23% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.190,04 | €1.192,45 | 113 | 113 | 46,90% | 1,46 | €10,55 | 6,27% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.131,79 | €1.118,65 | 119 | 119 | 53,78% | 1,53 | €9,40 | 6,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.070,19 | €1.015,60 | 148 | 148 | 47,97% | 1,36 | €6,86 | 8,85% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.926,58 | €928,94 | 81 | 81 | 45,68% | 1,55 | €11,47 | 6,27% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.879,75 | €822,88 | 37 | 37 | 54,05% | 2,16 | €22,24 | 3,82% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.701,25 | €682,86 | 224 | 224 | 46,88% | 1,16 | €3,05 | 7,45% |
| TEST | Combo Adaptive | Combo Adaptive | €10.675,17 | €688,70 | 155 | 155 | 47,10% | 1,27 | €4,44 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.667,77 | €659,94 | 194 | 194 | 51,03% | 1,21 | €3,40 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.599,23 | €591,45 | 238 | 238 | 45,38% | 1,14 | €2,49 | 9,48% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.473,08 | €465,50 | 128 | 128 | 47,66% | 1,17 | €3,64 | 7,78% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.471,49 | €452,16 | 82 | 82 | 50,00% | 1,28 | €5,51 | 5,24% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.407,47 | €424,02 | 117 | 117 | 48,72% | 1,19 | €3,62 | 8,68% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.395,04 | €376,63 | 237 | 237 | 40,51% | 1,09 | €1,59 | 6,56% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.359,25 | €359,25 | 50 | 45 | 50,00% | 1,31 | €7,18 | 3,89% |
| TEST | Ampia 4H | Confluenza trend | €10.344,68 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.305,79 | €305,79 | 15 | 15 | 60,00% | 2,24 | €20,39 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.293,40 | €242,06 | 132 | 132 | 44,70% | 1,09 | €1,83 | 11,27% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.277,64 | €277,64 | 62 | 62 | 51,61% | 1,21 | €4,48 | 4,50% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.259,35 | €193,98 | 7 | 7 | 57,14% | 2,72 | €27,71 | 1,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.222,37 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.220,71 | €207,92 | 111 | 111 | 42,34% | 1,08 | €1,87 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.214,73 | €201,94 | 115 | 115 | 42,61% | 1,08 | €1,76 | 12,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.204,14 | €198,71 | 138 | 138 | 48,55% | 1,08 | €1,44 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Ema 1H | Trend following EMA | €10.177,93 | €177,93 | 17 | 17 | 47,06% | 1,41 | €10,47 | 3,33% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.160,27 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,17% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.153,18 | €79,41 | 159 | 159 | 45,28% | 1,03 | €0,50 | 8,69% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.140,52 | €141,36 | 152 | 152 | 42,76% | 1,05 | €0,93 | 7,10% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.137,17 | €118,57 | 164 | 164 | 43,90% | 1,03 | €0,72 | 10,60% |
| TEST | Sol Ema 4H | Trend following EMA | €10.126,43 | €56,08 | 8 | 8 | 37,50% | 1,26 | €7,01 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.058,90 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.040,46 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.033,18 | €33,18 | 18 | 18 | 44,44% | 1,07 | €1,84 | 4,59% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.011,54 | €11,54 | 73 | 73 | 42,47% | 1,01 | €0,16 | 4,16% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Btc Ema 4H | Trend following EMA | €10.007,16 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.992,60 | €-7,40 | 10 | 10 | 50,00% | 0,97 | €-0,74 | 1,89% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Doge Ema 1H | Trend following EMA | €9.988,85 | €-11,15 | 17 | 17 | 58,82% | 0,97 | €-0,66 | 2,77% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.962,53 | €-52,16 | 40 | 40 | 47,50% | 0,95 | €-1,30 | 4,21% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Eth Ema 4H | Trend following EMA | €9.954,28 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.953,62 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.931,32 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,84 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.907,76 | €-139,40 | 134 | 134 | 48,51% | 0,94 | €-1,04 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.907,76 | €-139,40 | 134 | 134 | 48,51% | 0,94 | €-1,04 | 10,31% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.905,36 | €-112,91 | 132 | 132 | 43,94% | 0,96 | €-0,86 | 7,10% |
| TEST | Combo Scanner | Combo Scanner | €9.889,79 | €-159,56 | 137 | 137 | 44,53% | 0,95 | €-1,16 | 11,38% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.888,18 | €-111,00 | 116 | 116 | 41,38% | 0,95 | €-0,96 | 7,10% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.874,22 | €-138,61 | 65 | 65 | 49,23% | 0,91 | €-2,13 | 5,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.873,49 | €-126,51 | 14 | 14 | 42,86% | 0,72 | €-9,04 | 3,14% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.850,95 | €-115,67 | 163 | 163 | 41,72% | 0,96 | €-0,71 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.837,22 | €-177,28 | 40 | 40 | 42,50% | 0,83 | €-4,43 | 5,41% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.832,09 | €-185,17 | 210 | 210 | 43,81% | 0,96 | €-0,88 | 9,00% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.807,73 | €-200,58 | 173 | 173 | 42,20% | 0,94 | €-1,16 | 12,52% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.804,86 | €-208,87 | 119 | 112 | 42,86% | 0,94 | €-1,76 | 10,88% |
| TEST | Btc Ema 1H | Trend following EMA | €9.803,39 | €-166,34 | 13 | 13 | 30,77% | 0,61 | €-12,80 | 2,10% |
| TEST | Eth Ema 1H | Trend following EMA | €9.799,26 | €-200,74 | 20 | 20 | 40,00% | 0,71 | €-10,04 | 4,80% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.799,11 | €-231,06 | 12 | 12 | 33,33% | 0,55 | €-19,26 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.714,51 | €-289,97 | 105 | 105 | 45,71% | 0,87 | €-2,76 | 9,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.709,98 | €-290,02 | 14 | 14 | 28,57% | 0,52 | €-20,72 | 3,74% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.708,45 | €-297,89 | 83 | 83 | 39,76% | 0,85 | €-3,59 | 8,88% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.679,31 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.649,56 | €-398,57 | 124 | 124 | 43,55% | 0,84 | €-3,21 | 12,28% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.619,28 | €-392,08 | 65 | 65 | 32,31% | 0,79 | €-6,03 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.609,05 | €-402,29 | 60 | 60 | 36,67% | 0,78 | €-6,70 | 7,98% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.603,54 | €-463,09 | 55 | 55 | 32,73% | 0,76 | €-8,42 | 8,18% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.600,44 | €-399,22 | 94 | 94 | 40,43% | 0,84 | €-4,25 | 6,64% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.571,88 | €-439,42 | 62 | 62 | 35,48% | 0,78 | €-7,09 | 7,80% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.544,43 | €-456,83 | 114 | 114 | 38,60% | 0,84 | €-4,01 | 7,34% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.481,14 | €-527,93 | 65 | 65 | 35,38% | 0,75 | €-8,12 | 7,26% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.472,68 | €-518,66 | 69 | 69 | 37,68% | 0,75 | €-7,52 | 7,96% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.460,09 | €-552,71 | 111 | 101 | 44,14% | 0,77 | €-4,98 | 8,85% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.444,42 | €-566,44 | 97 | 97 | 48,45% | 0,74 | €-5,84 | 9,02% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.433,66 | €-565,77 | 98 | 98 | 44,90% | 0,80 | €-5,77 | 8,22% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.361,85 | €-705,05 | 168 | 168 | 42,26% | 0,78 | €-4,20 | 15,45% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.360,46 | €-638,42 | 54 | 54 | 25,93% | 0,66 | €-11,82 | 11,41% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.340,10 | €-658,83 | 33 | 33 | 24,24% | 0,38 | €-19,96 | 8,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.322,46 | €-678,77 | 131 | 131 | 39,69% | 0,78 | €-5,18 | 8,78% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.316,85 | €-652,88 | 118 | 118 | 41,53% | 0,72 | €-5,53 | 8,85% |
| TEST | Combo Trend | Combo Trend | €9.308,41 | €-666,88 | 160 | 160 | 39,38% | 0,82 | €-4,17 | 10,85% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.215,49 | €-786,94 | 76 | 76 | 35,53% | 0,67 | €-10,35 | 10,16% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.198,97 | €-788,48 | 126 | 126 | 38,10% | 0,69 | €-6,26 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.052,49 | €-947,51 | 92 | 92 | 35,87% | 0,64 | €-10,30 | 9,48% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.918,97 | €-1.081,03 | 48 | 48 | 35,42% | 0,46 | €-22,52 | 12,56% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.883,87 | €-1.115,11 | 79 | 79 | 31,65% | 0,52 | €-14,12 | 13,85% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.862,92 | €-1.143,10 | 60 | 60 | 26,67% | 0,56 | €-19,05 | 11,95% |
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
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,80100 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €56,04 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,42154 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-0,69 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 83,35500 | 81,67793 | 52,97621 | 90,53117 | €8,52 | €25,56 | €0,00 | €1,45 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 246,10000 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €-6,70 |
| 1H Balanced Long No Rhv V1 | SOL | LONG | Confluenza trend | 60m | 3,0x | 108,77575 | 107,14300 | 105,75101 | 73,06105 | 114,82524 | €28,18 | €84,53 | €2,35 | €-1,27 |
| 1H Balanced Long No Rhv V1 | TRUMP | LONG | Confluenza trend | 60m | 3,0x | 2,74355 | 2,80100 | 2,55460 | 1,84275 | 3,12145 | €234,56 | €703,68 | €48,46 | €14,74 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19977 | €131,74 | €395,21 | €47,43 | €0,00 |
| Bilanciata 1H V2 | TRUMP | LONG | Confluenza trend V2 | 60m | 3,0x | 2,74355 | 2,80100 | 2,55460 | 1,84275 | 3,12145 | €228,59 | €685,78 | €47,23 | €14,36 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 84,90998 | 83,35500 | 82,34469 | 57,03120 | 90,04056 | €548,05 | €1.644,14 | €49,67 | €-30,11 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,44929 | 1,42154 | 1,41511 | 0,97344 | 1,51766 | €23,14 | €69,42 | €1,64 | €-1,33 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,02 | €417,05 | €50,05 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €132,75 | €398,25 | €47,79 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €-0,75 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €145,28 | €435,84 | €52,30 | €0,00 |
| 1H Fast No Pepe V1 | TRUMP | LONG | Momentum / breakout | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €332,30 | €996,90 | €53,40 | €20,88 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | TRUMP | LONG | Momentum / breakout | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 3,03747 | €314,71 | €944,14 | €50,57 | €19,77 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €-9,23 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,42 | €25,27 | €3,03 | €0,00 |
| Rapida 1H V3 Filtered | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €308,01 | €924,04 | €49,50 | €19,35 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €9,29 | €27,86 | €3,34 | €0,00 |
| 1H Fast V3 Nohigh V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €307,61 | €922,83 | €49,43 | €19,32 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €-8,67 |
| 1H Fast V3 Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €135,44 | €406,31 | €48,76 | €0,00 |
| 1H Fast V3 Long Only V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €304,28 | €912,85 | €48,90 | €19,12 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €134,26 | €402,77 | €48,33 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €-0,42 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €305,32 | €915,96 | €49,06 | €19,18 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,69 | €419,06 | €50,29 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €314,81 | €944,43 | €50,59 | €19,78 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €-9,29 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,48 | €25,43 | €3,05 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €310,01 | €930,02 | €49,82 | €19,48 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15804 | 0,15804 | 0,13908 | 0,10615 | 0,18649 | €130,02 | €390,07 | €46,81 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2498,26000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,06 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 83,35500 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,41 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,80100 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €75,95 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08789 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-13,16 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | BTR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,15974 | 0,15974 | 0,14057 | 0,08067 | 0,20191 | €200,93 | €401,87 | €48,22 | €0,00 |
| Forza relativa 1H V2 | TRUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,15924 | €355,39 | €710,77 | €48,95 | €14,88 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45759 | 1,42154 | 1,41723 | 0,73608 | 1,55848 | €42,73 | €85,47 | €2,37 | €-2,11 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45759 | 1,42154 | 1,41723 | 0,73608 | 1,55848 | €41,73 | €83,46 | €2,31 | €-2,06 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 790,17000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-0,77 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 107,93058 | 107,14300 | 104,51281 | 54,50494 | 115,44967 | €700,71 | €1.401,42 | €44,38 | €-10,23 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €56,35 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €37,02 | €74,04 | €2,06 | €-1,11 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €-7,07 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | BTR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €206,82 | €413,63 | €49,64 | €0,00 |
| Scanner Top10 Long | TRUMP | LONG | Scanner Top10 Long | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €369,58 | €739,16 | €50,91 | €15,48 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €-0,92 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €50,92 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | BTR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €14,08 | €28,16 | €0,78 | €-0,42 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 84,84797 | 83,35500 | 82,41506 | 42,84822 | 89,71377 | €14,05 | €28,10 | €0,81 | €-0,49 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €-0,92 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €50,92 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | BTR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €14,08 | €28,16 | €0,78 | €-0,42 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 84,84797 | 83,35500 | 82,41506 | 42,84822 | 89,71377 | €14,05 | €28,10 | €0,81 | €-0,49 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €52,61 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 89,32457 | €30,02 | €60,05 | €1,63 | €-0,66 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €49,32 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 89,32457 | €28,15 | €56,29 | €1,53 | €-0,62 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,80100 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €2,50 |
| Scanner Top5 Btc Guard V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €189,80 | €379,60 | €45,55 | €0,00 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,83196 | 83,35500 | 82,43497 | 42,84014 | 90,10534 | €13,39 | €26,78 | €0,76 | €-0,47 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,80100 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €2,44 |
| Scanner Top5 Btc Guard Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €185,39 | €370,78 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,83196 | 83,35500 | 82,43497 | 42,84014 | 90,10534 | €13,08 | €26,16 | €0,74 | €-0,46 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,80100 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €2,44 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,82 | €421,64 | €50,60 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,23 | €0,71 | €-0,29 |
| Scanner Top5 Btc Runner25 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,31040 | €370,24 | €740,48 | €51,00 | €15,51 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,94 | €421,89 | €50,63 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,25 | €0,71 | €-0,29 |
| Scanner Top5 Btc Tp3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,31040 | €370,46 | €740,92 | €51,03 | €15,52 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 790,17000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-10,89 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 83,35500 | 81,73954 | 42,56385 | 89,88454 | €13,36 | €26,72 | €0,81 | €-0,29 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 108,89978 | 107,14300 | 105,49381 | 54,99439 | 116,39291 | €725,00 | €1.450,01 | €45,35 | €-23,39 |
| Combo Trend | TRUMP | LONG | Combo Trend | 60m | 2,0x | 2,74355 | 2,80100 | 2,53360 | 1,38549 | 3,20543 | €297,16 | €594,31 | €45,48 | €12,45 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €50,47 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 89,32457 | €24,57 | €49,15 | €1,34 | €-0,54 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €-0,43 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 790,17000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-13,54 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €4,09 |
| Combo Adaptive | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €222,35 | €444,69 | €53,36 | €0,00 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 85,03100 | 83,35500 | 82,51607 | 42,94066 | 90,06086 | €27,91 | €55,81 | €1,65 | €-1,10 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €-0,57 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €69,16 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €163,28 | €326,55 | €39,19 | €0,00 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 85,03100 | 83,35500 | 82,51607 | 42,94066 | 90,06086 | €14,98 | €29,97 | €0,89 | €-0,59 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €-6,74 |
| Combo Adaptive Quality7 V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €351,63 | €703,25 | €48,43 | €14,73 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €204,79 | €409,58 | €49,15 | €0,00 |
| Combo Adaptive Regime V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €357,90 | €715,80 | €49,30 | €14,99 |
| Combo Adaptive Quality7 Regime V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €356,56 | €713,12 | €49,11 | €14,93 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €10,54 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €31,02 | €62,04 | €1,73 | €-0,93 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €76,05 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €361,10 | €722,20 | €49,74 | €15,12 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 80391,81515 | 79728,20000 | 79234,17301 | 53996,50251 | 82707,09942 | €1.138,16 | €3.414,47 | €49,17 | €-28,19 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 79728,20000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €-10,99 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 79728,20000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €-10,93 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 79728,20000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €11,49 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 79728,20000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €-10,13 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 98,32066 | 107,14300 | 105,07574 | 49,65193 | 113,95442 | €395,27 | €790,53 | €0,00 | €70,93 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 107,14300 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €26,41 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 108,77924 | 107,14300 | 108,09773 | 144,49509 | 104,97024 | €697,47 | €2.092,40 | €0,00 | €31,47 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 107,14300 | 112,84334 | 160,38740 | 97,27311 | €478,97 | €957,94 | €49,65 | €1,25 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 98,32066 | 107,14300 | 105,07574 | 49,65193 | 115,37567 | €367,30 | €734,59 | €0,00 | €65,92 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2498,26000 | 2464,86772 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €0,00 | €44,17 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.560,29 | €3.120,58 | €46,79 | €-5,05 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,23 | €382,45 | €45,89 | €0,00 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €863,53 | €1.727,06 | €47,46 | €4,44 |
| Master Adaptive V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €293,22 | €586,43 | €47,70 | €15,17 |
| Master Adaptive V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €12,58 | €25,16 | €1,73 | €0,53 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.565,03 | €3.130,05 | €46,93 | €-5,07 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,14959 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €343,00 | €686,01 | €47,25 | €14,37 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,91738 | 107,14300 | 103,99458 | 53,99328 | 112,76299 | €858,29 | €1.716,58 | €46,93 | €3,62 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.493,28 | €2.986,56 | €44,78 | €-4,83 |
| Master Adaptive Strict3 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €184,95 | €369,91 | €44,39 | €0,00 |
| Master Adaptive Strict3 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €320,71 | €641,43 | €44,18 | €13,43 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.572,67 | €3.145,34 | €47,16 | €-5,09 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16110 | 0,16110 | 0,14177 | 0,08136 | 0,19977 | €197,88 | €395,75 | €47,49 | €0,00 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 107,32546 | 107,14300 | 104,39936 | 54,19936 | 113,17765 | €18,64 | €37,29 | €1,02 | €-0,06 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.539,56 | €3.079,12 | €46,16 | €-4,98 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €188,69 | €377,37 | €45,28 | €0,00 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €852,06 | €1.704,12 | €46,83 | €4,38 |
| Master Adaptive Gb20 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €289,32 | €578,64 | €47,07 | €14,97 |
| Master Adaptive Gb20 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,78156 | 2,80100 | 2,59415 | 1,40469 | 3,15637 | €17,24 | €34,47 | €2,32 | €0,24 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 83,35500 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €64,44 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2614,85753 | €1.568,97 | €3.137,94 | €47,05 | €-5,08 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,43928 | 107,14300 | 103,65189 | 53,75184 | 114,80148 | €920,14 | €1.840,29 | €48,19 | €12,17 |
| Master Adaptive Runner25 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16525 | 0,15522 | 0,08370 | 0,19732 | €14,90 | €29,81 | €1,89 | €-0,09 |
| Master Adaptive Runner25 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15905 | 0,15905 | 0,13997 | 0,08032 | 0,21631 | €158,41 | €316,83 | €38,02 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 790,17000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-13,45 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €210,11 | €420,21 | €50,43 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 251,13022 | 246,10000 | 242,26367 | 126,82076 | 268,86331 | €14,43 | €28,86 | €1,02 | €-0,58 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.568,02 | €3.136,03 | €47,02 | €-5,08 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €192,17 | €384,35 | €46,12 | €0,00 |
| Master Adaptive Gb20 Be V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €867,81 | €1.735,61 | €47,70 | €4,46 |
| Master Adaptive Gb20 Be V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €294,67 | €589,34 | €47,94 | €15,25 |
| Master Adaptive Gb20 Be V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €12,64 | €25,28 | €1,74 | €0,53 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.566,35 | €3.132,70 | €46,97 | €-5,07 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,97 | €383,94 | €46,07 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €866,88 | €1.733,77 | €47,65 | €4,46 |
| Master Adaptive Gb20 Partial V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €294,36 | €588,71 | €47,89 | €15,23 |
| Master Adaptive Gb20 Partial V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €12,63 | €25,26 | €1,74 | €0,53 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2474,17356 | 1263,66673 | 2577,34181 | €1.829,31 | €3.658,61 | €41,14 | €-5,92 |
| Master Adaptive Gb20 Loss Cap V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,20861 | €188,78 | €377,55 | €45,31 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 104,66569 | 53,96853 | 112,74219 | €1.136,69 | €2.273,37 | €46,86 | €5,84 |
| Master Adaptive Gb20 Loss Cap V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,15126 | 0,08135 | 0,18729 | €63,69 | €127,37 | €7,77 | €3,30 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €325,19 | €975,57 | €52,26 | €20,43 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 83,35500 | 81,08374 | 52,16065 | 90,56048 | €216,52 | €649,56 | €0,00 | €47,65 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,42154 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-1,29 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2498,26000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,74 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16525 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €11,68 |
| Main Dynamic Asset Selector V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 84,46489 | 83,35500 | 79,49888 | 56,73225 | 94,39691 | €288,05 | €864,16 | €50,81 | €-11,36 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16525 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €10,94 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | LONG | Combo Trend | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €231,16 | €462,32 | €55,48 | €0,00 |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 83,35500 | 81,73954 | 42,56385 | 89,88454 | €32,97 | €65,95 | €1,99 | €-0,73 |
| Combo Trend Side Regime Guard V1 | TRUMP | LONG | Combo Trend | 60m | 2,0x | 2,74355 | 2,80100 | 2,53360 | 1,38549 | 3,20543 | €363,18 | €726,37 | €55,58 | €15,21 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €129,45 | €388,34 | €46,60 | €0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 84,90998 | 83,35500 | 82,34469 | 57,03120 | 90,04056 | €518,27 | €1.554,82 | €46,97 | €-28,47 |
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
| Scanner Top20 Long | ETH | LONG | 2026-08-28T04:15:00+00:00 | 2476,94587 | €-0,58 | -1,09 | STOP |
| Scanner Top15 Long | ETH | LONG | 2026-08-28T04:15:00+00:00 | 2476,94587 | €-0,58 | -1,09 | STOP |
| Master Adaptive Strict3 V1 | ENA | LONG | 2026-08-28T04:15:00+00:00 | 0,16043 | €-45,79 | -1,02 | STOP |
| Master Adaptive No Alt V1 | ENA | LONG | 2026-08-28T04:15:00+00:00 | 0,16043 | €-49,30 | -1,02 | STOP |
| Eth Ema 1H | ETH | LONG | 2026-08-28T04:15:00+00:00 | 2476,94587 | €-53,50 | -1,09 | STOP |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | 2026-08-28T04:15:00+00:00 | 82,96658 | €-4,61 | -1,04 | STOP |
| Benchmark Donchian breakout 1H | HYPE | LONG | 2026-08-28T04:15:00+00:00 | 82,96658 | €-4,72 | -1,04 | STOP |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | 2026-08-28T04:15:00+00:00 | 82,95105 | €-50,91 | -1,07 | STOP |
| 1H Fast Tp2 V1 | TAO | LONG | 2026-08-28T04:15:00+00:00 | 243,33545 | €-1,55 | -1,05 | STOP |
| 1H Balanced Long No Rhv V1 | XRP | LONG | 2026-08-28T04:15:00+00:00 | 1,42099 | €-1,01 | -1,06 | STOP |
| Sol Ema 1H | SOL | LONG | 2026-08-28T03:15:00+00:00 | 105,81324 | €-53,66 | -1,05 | STOP |
| Sol Adaptive 1H | SOL | LONG | 2026-08-28T03:15:00+00:00 | 105,81324 | €-52,90 | -1,05 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
