# Paper trading automatico KuCoin

Generato: 2026-08-20T05:32:49+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-20T05:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-20T05:05:28+00:00 | 2026-08-20T05:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-20T04:45:00+00:00 | 2026-08-20T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-20T04:00:00+00:00 | 2026-08-20T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-20T00:00:00+00:00 | 2026-08-20T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Scanner | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Tp3 V1 | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | 60m | LONG | 6,77 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 6,45 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 6,32 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | LINK | 240m | LONG | 5,34 | 6,00 | 0,66 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,99 | 6,00 | 2,01 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 2,63 | 6,00 | 3,37 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 2,29 | 6,00 | 3,71 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTW | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 0,66 | 6,00 | 5,34 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 0,42 | 6,00 | 5,58 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | PEPE | 60m | LONG | 6,77 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | PEPE | 60m | LONG | 6,77 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 Cost Aware V1 | PEPE | 60m | LONG | 6,77 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | PEPE | 60m | LONG | 6,77 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | PEPE | 60m | LONG | 6,77 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | PEPE | 60m | LONG | 6,77 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | PEPE | 60m | LONG | 6,77 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | PEPE | 60m | LONG | 6,77 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.660,68 | -3,39% | €-87,67 | €3.000,00 | -2,92% | 5 | 46 | 34,78% | 0,76 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 46 | 1743 | PRIME INDICAZIONI | 100 (mancano 54) |

- Trade del Principale 4H chiusi: **46**; win rate **34,78%**; profit factor **0,76**.
- Expectancy: **€-7,25** per trade; P&L netto: **€-333,55**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.660,68 | €979,58 | €2.938,74 | €193,29 | €-4,27 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.826,81 | €3.389,80 | €6.779,61 | €212,54 | €-12,48 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.571,90 | €3.309,99 | €6.619,99 | €207,54 | €-12,19 |
| TEST | Main Side Regime Guard V1 | 2 | €10.476,87 | €288,21 | €864,64 | €103,76 | €0,00 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.428,49 | €2.685,33 | €8.055,98 | €208,22 | €-50,75 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.402,90 | €2.717,08 | €5.434,15 | €208,48 | €-52,47 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €10.293,73 | €2.200,12 | €4.400,24 | €154,46 | €-2,52 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.150,49 | €243,23 | €729,68 | €51,78 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €10.114,48 | €1.651,70 | €3.303,41 | €153,03 | €48,23 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.054,93 | €727,07 | €1.454,13 | €50,33 | €-10,53 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.043,64 | €797,18 | €1.594,36 | €50,17 | €10,91 |
| TEST | 1H Fast No Pepe V1 | 5 | €10.043,63 | €2.087,76 | €6.263,28 | €201,16 | €-13,55 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €10.040,93 | €333,06 | €999,18 | €49,31 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.038,66 | €665,34 | €1.330,67 | €50,25 | €-9,64 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 1 | €10.029,22 | €155,86 | €467,58 | €51,44 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.997,32 | €1.902,37 | €3.804,75 | €48,94 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.993,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.991,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.968,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.964,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €9.948,25 | €1.743,23 | €5.229,70 | €198,97 | €23,04 |
| TEST | Btc Ema 1H | 0 | €9.942,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.923,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.900,08 | €715,87 | €1.431,74 | €49,56 | €-10,37 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.892,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.874,30 | €1.584,85 | €4.754,55 | €147,68 | €-9,79 |
| TEST | Combo Adaptive | 5 | €9.867,01 | €2.865,18 | €5.730,36 | €197,54 | €-33,63 |
| TEST | Sol Ema 1H | 0 | €9.848,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.848,25 | €760,21 | €2.280,63 | €49,27 | €-5,29 |
| TEST | Eth Ema 4H | 1 | €9.837,98 | €577,20 | €1.154,41 | €49,21 | €-3,33 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 3 | €9.814,63 | €2.469,90 | €4.939,79 | €146,25 | €4,00 |
| TEST | Eth Bollinger 1H | 1 | €9.792,87 | €679,82 | €2.039,45 | €48,91 | €11,90 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 1 | €9.779,65 | €151,98 | €455,94 | €50,16 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.778,64 | €670,92 | €2.012,75 | €48,92 | €-4,67 |
| TEST | Scanner Bottom10 Short | 4 | €9.770,80 | €2.743,93 | €5.487,86 | €146,41 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.770,80 | €2.743,93 | €5.487,86 | €146,41 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.770,80 | €2.743,93 | €5.487,86 | €146,41 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 4 | €9.768,61 | €3.362,98 | €6.725,95 | €196,01 | €-78,06 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €9.730,39 | €404,89 | €809,78 | €48,76 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.720,29 | €563,60 | €1.690,79 | €48,66 | €-10,54 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.708,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.703,10 | €2.724,94 | €5.449,88 | €145,40 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.702,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.688,34 | €2.720,79 | €5.441,59 | €145,18 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.613,78 | €2.699,86 | €5.399,71 | €144,06 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.608,00 | €399,80 | €799,60 | €48,15 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €9.531,44 | €3.673,58 | €7.347,15 | €190,65 | €-67,49 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €9.480,27 | €2.469,72 | €4.939,44 | €189,99 | €-47,71 |
| TEST | Scanner Top15 Long | 5 | €9.480,27 | €2.469,72 | €4.939,44 | €189,99 | €-47,71 |
| TEST | Scanner Top20 Long | 5 | €9.480,27 | €2.469,72 | €4.939,44 | €189,99 | €-47,71 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €9.474,75 | €2.751,28 | €5.502,55 | €189,69 | €-32,29 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €9.457,41 | €1.970,74 | €5.912,22 | €189,15 | €-13,05 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.447,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.444,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.435,91 | €146,77 | €440,31 | €48,44 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.433,14 | €1.196,91 | €3.590,73 | €143,21 | €-27,12 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.406,54 | €3.005,65 | €6.011,30 | €188,10 | €-65,64 |
| TEST | Rapida 1H V3 Filtered | 5 | €9.395,63 | €1.949,53 | €5.848,60 | €187,35 | €-12,96 |
| TEST | Master Adaptive Runner25 V1 | 2 | €9.378,60 | €211,06 | €422,12 | €50,65 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.375,25 | €1.501,42 | €4.504,26 | €187,54 | €-25,26 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.339,50 | €1.499,02 | €4.497,05 | €139,68 | €-9,26 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €9.335,21 | €2.725,60 | €8.176,80 | €187,47 | €-37,64 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.304,10 | €973,38 | €1.946,77 | €47,25 | €-27,66 |
| TEST | Combo Adaptive Quality7 V1 | 1 | €9.288,56 | €371,68 | €743,36 | €47,16 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.250,16 | €1.924,27 | €5.772,82 | €184,45 | €-12,83 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €9.202,90 | €3.453,43 | €6.906,87 | €184,08 | €-49,03 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €9.197,52 | €3.451,41 | €6.902,83 | €183,98 | €-49,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.187,77 | €2.935,75 | €5.871,49 | €183,73 | €-64,11 |
| TEST | Bilanciata 1H V1 | 1 | €9.151,18 | €135,05 | €405,16 | €0,00 | €0,00 |
| TEST | Combo Scanner | 4 | €9.144,62 | €3.524,49 | €7.048,98 | €182,92 | €-64,75 |
| TEST | Combo Trend | 5 | €9.138,02 | €2.078,68 | €4.157,35 | €136,44 | €-8,22 |
| TEST | Combo Mean Reversion | 1 | €9.114,86 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.057,29 | €186,88 | €373,77 | €44,85 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €8.935,26 | €3.443,80 | €6.887,59 | €178,73 | €-63,27 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €8.888,13 | €2.595,07 | €7.785,20 | €178,49 | €-35,84 |
| TEST | Benchmark trend following EMA 1H | 5 | €8.872,53 | €2.019,96 | €4.039,92 | €132,96 | €-8,35 |
| TEST | Forza relativa 1H V1 | 1 | €8.800,06 | €1.513,47 | €3.026,93 | €45,42 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €8.741,01 | €202,90 | €405,81 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 4 | €8.512,61 | €2.662,51 | €5.325,01 | €170,37 | €-3,36 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.660,68 | €-333,55 | 46 | 46 | 34,78% | 0,76 | €-7,25 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.826,81 | €842,92 | 76 | 76 | 48,68% | 1,48 | €11,09 | 3,63% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.571,90 | €587,64 | 44 | 44 | 47,73% | 1,67 | €13,36 | 3,63% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.476,87 | €477,55 | 29 | 29 | 48,28% | 1,77 | €16,47 | 2,40% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.428,49 | €484,08 | 84 | 84 | 48,81% | 1,24 | €5,76 | 4,41% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.402,90 | €458,74 | 94 | 94 | 45,74% | 1,21 | €4,88 | 8,85% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.293,73 | €298,89 | 62 | 62 | 48,39% | 1,23 | €4,82 | 4,33% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.150,49 | €150,93 | 37 | 37 | 45,95% | 1,14 | €4,08 | 3,34% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Ampia 4H | Confluenza trend | €10.114,48 | €68,13 | 44 | 44 | 27,27% | 1,06 | €1,55 | 4,45% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.054,93 | €66,34 | 4 | 4 | 50,00% | 1,63 | €16,58 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.043,64 | €33,68 | 2 | 2 | 50,00% | 1,63 | €16,84 | 0,72% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.043,63 | €60,94 | 135 | 135 | 44,44% | 1,02 | €0,45 | 4,46% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.040,93 | €41,53 | 34 | 30 | 44,12% | 1,05 | €1,22 | 3,89% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.038,66 | €49,10 | 4 | 4 | 50,00% | 1,47 | €12,27 | 1,01% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.029,22 | €29,50 | 121 | 121 | 43,80% | 1,01 | €0,24 | 7,10% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.997,32 | €-0,41 | 37 | 37 | 43,24% | 1,00 | €-0,01 | 3,91% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.993,68 | €-6,32 | 13 | 13 | 30,77% | 0,36 | €-0,49 | 0,11% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,28 | €-8,72 | 13 | 13 | 61,54% | 0,97 | €-0,67 | 2,10% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.968,38 | €-31,62 | 13 | 13 | 30,77% | 0,36 | €-2,43 | 0,53% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.964,50 | €-35,50 | 10 | 10 | 40,00% | 0,86 | €-3,55 | 2,77% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.948,25 | €-128,00 | 157 | 156 | 35,67% | 0,96 | €-0,82 | 6,56% |
| TEST | Btc Ema 1H | Trend following EMA | €9.942,20 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.923,36 | €-76,64 | 13 | 13 | 30,77% | 0,11 | €-5,90 | 0,89% |
| TEST | Sol Ema 4H | Trend following EMA | €9.900,08 | €-88,69 | 5 | 5 | 20,00% | 0,57 | €-17,74 | 2,27% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.892,99 | €-107,01 | 8 | 8 | 37,50% | 0,66 | €-13,38 | 1,89% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.874,30 | €-113,06 | 115 | 115 | 38,26% | 0,96 | €-0,98 | 9,12% |
| TEST | Combo Adaptive | Combo Adaptive | €9.867,01 | €-95,93 | 97 | 97 | 39,18% | 0,95 | €-0,99 | 7,91% |
| TEST | Sol Ema 1H | Trend following EMA | €9.848,78 | €-151,22 | 11 | 11 | 27,27% | 0,61 | €-13,75 | 3,33% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.848,25 | €-145,10 | 8 | 8 | 25,00% | 0,56 | €-18,14 | 2,63% |
| TEST | Eth Ema 4H | Trend following EMA | €9.837,98 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,81% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.814,63 | €-186,41 | 72 | 72 | 40,28% | 0,88 | €-2,59 | 8,68% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.792,87 | €-217,80 | 4 | 4 | 25,00% | 0,07 | €-54,45 | 2,71% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,65 | €-220,08 | 85 | 85 | 42,35% | 0,88 | €-2,59 | 7,10% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.778,64 | €-215,49 | 9 | 9 | 33,33% | 0,34 | €-23,94 | 3,14% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.770,80 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.770,80 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.770,80 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.768,61 | €-149,30 | 67 | 67 | 40,30% | 0,91 | €-2,23 | 6,25% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.730,39 | €-272,05 | 25 | 25 | 40,00% | 0,64 | €-10,88 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Ema 1H | Trend following EMA | €9.720,29 | €-268,16 | 13 | 13 | 30,77% | 0,47 | €-20,63 | 4,80% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.708,70 | €-291,30 | 12 | 12 | 25,00% | 0,35 | €-24,27 | 4,59% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.703,10 | €-293,72 | 57 | 57 | 33,33% | 0,78 | €-5,15 | 5,27% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.702,33 | €-365,26 | 131 | 130 | 41,98% | 0,90 | €-2,79 | 9,66% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.688,34 | €-308,49 | 58 | 58 | 32,76% | 0,76 | €-5,32 | 5,27% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.613,78 | €-383,06 | 85 | 85 | 32,94% | 0,79 | €-4,51 | 6,41% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.608,00 | €-394,41 | 25 | 25 | 32,00% | 0,49 | €-15,78 | 5,41% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.531,44 | €-396,66 | 82 | 82 | 36,59% | 0,81 | €-4,84 | 11,27% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.480,27 | €-468,96 | 67 | 67 | 41,79% | 0,72 | €-7,00 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.480,27 | €-468,96 | 67 | 67 | 41,79% | 0,72 | €-7,00 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.480,27 | €-468,96 | 67 | 67 | 41,79% | 0,72 | €-7,00 | 10,31% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.474,75 | €-489,66 | 98 | 98 | 37,76% | 0,76 | €-5,00 | 8,69% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.457,41 | €-531,54 | 116 | 115 | 43,97% | 0,77 | €-4,58 | 9,50% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.447,55 | €-615,90 | 84 | 83 | 44,05% | 0,76 | €-7,33 | 7,69% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.444,37 | €-621,42 | 89 | 88 | 43,82% | 0,78 | €-6,98 | 9,98% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,91 | €-563,83 | 111 | 111 | 40,54% | 0,80 | €-5,08 | 6,91% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.433,14 | €-537,49 | 78 | 71 | 41,03% | 0,72 | €-6,89 | 8,81% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.406,54 | €-524,11 | 65 | 65 | 35,38% | 0,73 | €-8,06 | 7,34% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.395,63 | €-593,42 | 160 | 159 | 37,50% | 0,83 | €-3,71 | 9,48% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,60 | €-623,54 | 50 | 50 | 30,00% | 0,65 | €-12,47 | 8,18% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.375,25 | €-596,78 | 61 | 61 | 37,70% | 0,67 | €-9,78 | 9,26% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.339,50 | €-648,54 | 71 | 71 | 35,21% | 0,63 | €-9,13 | 8,85% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.335,21 | €-622,25 | 75 | 75 | 34,67% | 0,69 | €-8,30 | 10,60% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.304,10 | €-667,07 | 85 | 81 | 37,65% | 0,77 | €-7,85 | 10,84% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.288,56 | €-710,99 | 50 | 50 | 28,00% | 0,55 | €-14,22 | 8,87% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.250,16 | €-788,11 | 132 | 131 | 37,12% | 0,73 | €-5,97 | 9,00% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.202,90 | €-743,93 | 66 | 66 | 33,33% | 0,62 | €-11,27 | 11,78% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.197,52 | €-749,34 | 70 | 70 | 34,29% | 0,62 | €-10,70 | 12,06% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.187,77 | €-744,49 | 82 | 82 | 37,80% | 0,67 | €-9,08 | 8,78% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.151,18 | €-848,58 | 120 | 120 | 36,67% | 0,69 | €-7,07 | 13,99% |
| TEST | Combo Scanner | Combo Scanner | €9.144,62 | €-786,40 | 86 | 86 | 36,05% | 0,68 | €-9,14 | 11,38% |
| TEST | Combo Trend | Combo Trend | €9.138,02 | €-851,27 | 122 | 122 | 33,61% | 0,74 | €-6,98 | 10,85% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,86 | €-884,87 | 37 | 37 | 37,84% | 0,48 | €-23,92 | 10,64% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.057,29 | €-942,10 | 52 | 52 | 28,85% | 0,59 | €-18,12 | 11,51% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €8.935,26 | €-997,34 | 74 | 74 | 33,78% | 0,48 | €-13,48 | 12,28% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €8.888,13 | €-1.071,36 | 95 | 95 | 29,47% | 0,59 | €-11,28 | 12,52% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €8.872,53 | €-1.116,73 | 91 | 91 | 29,67% | 0,49 | €-12,27 | 12,31% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.800,06 | €-1.198,23 | 104 | 104 | 27,88% | 0,54 | €-11,52 | 13,92% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.741,01 | €-1.258,75 | 80 | 80 | 38,75% | 0,55 | €-15,73 | 14,60% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.512,61 | €-1.480,84 | 103 | 103 | 30,10% | 0,42 | €-14,38 | 15,45% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2258,11153 | 2251,60000 | 2170,60386 | 1516,69825 | 2433,12687 | €415,70 | €1.247,11 | €48,33 | €-3,60 |
| Principale 4H | LINK | LONG | Confluenza trend | 240m | 3,0x | 10,58112 | 10,44100 | 10,13407 | 7,10698 | 11,47522 | €16,96 | €50,87 | €2,15 | €-0,67 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 70,90318 | 71,00600 | 68,23231 | 47,62330 | 76,24492 | €415,85 | €1.247,54 | €46,99 | €1,81 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2265,72305 | 2251,60000 | 2200,51783 | 1521,81065 | 2396,13352 | €43,23 | €129,69 | €3,73 | €-0,81 |
| 1H Balanced Long No Rhv V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 561,75233 | 553,00000 | 543,45247 | 377,31031 | 598,35205 | €467,90 | €1.403,69 | €45,73 | €-21,87 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1209,81000 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €-4,40 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | SUI | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,65261 | 0,65261 | 0,66201 | 0,86688 | 0,63381 | €26,68 | €80,03 | €1,15 | €-0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 561,75233 | 553,00000 | 543,45247 | 377,31031 | 598,35205 | €484,09 | €1.452,26 | €47,31 | €-22,63 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1209,81000 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €-4,49 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 70,90318 | 71,00600 | 68,23231 | 47,62330 | 76,24492 | €440,14 | €1.320,43 | €49,74 | €1,91 |
| Bilanciata 1H V3 Filtered | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 10,71314 | 10,44100 | 10,42552 | 7,19566 | 11,28838 | €15,59 | €46,76 | €1,26 | €-1,19 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2251,60000 | 2181,35381 | 1510,45050 | 2383,72136 | €531,07 | €1.593,21 | €47,79 | €1,98 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1209,81000 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €-12,50 |
| 1H Fast Score 6 75 Range Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 70,90318 | 71,00600 | 68,82584 | 47,62330 | 74,01919 | €598,62 | €1.795,86 | €52,62 | €2,60 |
| 1H Fast Score 6 75 Cost Aware V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2248,80967 | 2251,60000 | 2196,34402 | 1510,45050 | 2327,50816 | €750,90 | €2.252,70 | €52,56 | €2,80 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €710,87 | €2.132,62 | €51,43 | €-39,19 |
| 1H Fast Score 6 75 Cost Aware V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1220,85412 | 1209,81000 | 1187,23972 | 820,00702 | 1271,27573 | €624,93 | €1.874,80 | €51,62 | €-16,96 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| 1H Fast No Pepe V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €695,36 | €2.086,09 | €50,30 | €-38,34 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 72,74112 | €505,03 | €1.515,09 | €50,29 | €37,50 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2264,89289 | 2251,60000 | 2215,55811 | 1521,25306 | 2338,89507 | €722,29 | €2.166,86 | €47,20 | €-12,72 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| 1H Fast Tp2 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2265,72305 | 2251,60000 | 2215,00788 | 1521,81065 | 2367,15340 | €742,72 | €2.228,16 | €49,87 | €-13,89 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 73,89121 | €494,31 | €1.482,92 | €49,23 | €36,71 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1204,83092 | 1209,81000 | 1170,97389 | 809,24477 | 1272,54496 | €18,91 | €56,74 | €1,59 | €0,23 |
| 1H Fast Tp2 V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,56 | €73,68 | €1,66 | €-0,01 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V3 Filtered | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €650,52 | €1.951,56 | €47,06 | €-35,86 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 72,74112 | €472,46 | €1.417,39 | €47,05 | €35,08 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2264,89289 | 2251,60000 | 2215,55811 | 1521,25306 | 2338,89507 | €657,98 | €1.973,93 | €43,00 | €-11,59 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1209,81000 | 1187,23972 | 820,00702 | 1271,27573 | €21,81 | €65,43 | €1,80 | €-0,59 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €617,12 | €1.851,37 | €44,64 | €-34,02 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 72,74112 | €448,21 | €1.344,62 | €44,64 | €33,28 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2264,89289 | 2251,60000 | 2215,55811 | 1521,25306 | 2338,89507 | €682,97 | €2.048,92 | €44,63 | €-12,03 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11119 | 1,10110 | 1,09169 | 0,74635 | 1,14044 | €846,77 | €2.540,30 | €44,58 | €-23,07 |
| 1H Fast V3 No Esports V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| 1H Fast V3 No Esports V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €640,45 | €1.921,36 | €46,33 | €-35,31 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 72,74112 | €465,15 | €1.395,46 | €46,32 | €34,54 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2264,89289 | 2251,60000 | 2215,55811 | 1521,25306 | 2338,89507 | €657,07 | €1.971,22 | €42,94 | €-11,57 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1209,81000 | 1187,23972 | 820,00702 | 1271,27573 | €18,11 | €54,34 | €1,50 | €-0,49 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €648,16 | €1.944,49 | €46,89 | €-35,73 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 72,74112 | €470,75 | €1.412,25 | €46,88 | €34,96 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2264,89289 | 2251,60000 | 2215,55811 | 1521,25306 | 2338,89507 | €717,33 | €2.151,98 | €46,88 | €-12,63 |
| 1H Fast V3 No Esports Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11119 | 1,10110 | 1,09169 | 0,74635 | 1,14044 | €889,36 | €2.668,07 | €46,82 | €-24,23 |
| 1H Fast V3 No Esports Mfe Lock V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 563,35265 | 553,00000 | 549,76815 | 378,38520 | 583,72940 | €654,80 | €1.964,40 | €47,37 | €-36,10 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,29086 | 71,00600 | 66,99068 | 46,54036 | 72,74112 | €475,57 | €1.426,71 | €47,36 | €35,32 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2264,89289 | 2251,60000 | 2215,55811 | 1521,25306 | 2338,89507 | €662,31 | €1.986,92 | €43,28 | €-11,66 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1209,81000 | 1187,23972 | 820,00702 | 1271,27573 | €21,95 | €65,86 | €1,81 | €-0,60 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,38 | €25,15 | €0,57 | €-0,01 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,65521 | 0,65521 | 0,67955 | 0,97953 | 0,58704 | €31,61 | €63,21 | €2,35 | €-0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 9,97398 | 10,44100 | 10,38253 | 5,03686 | 11,21104 | €560,46 | €1.120,91 | €0,00 | €52,49 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2251,60000 | 2144,35158 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €50,68 | €-2,90 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 565,27303 | 553,00000 | 531,45855 | 285,46288 | 659,95358 | €31,20 | €62,41 | €3,73 | €-1,35 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,65491 | 0,65491 | 0,66473 | 0,97909 | 0,63329 | €1.513,47 | €3.026,93 | €45,42 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SUI | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,65001 | 0,65001 | 0,65937 | 0,97176 | 0,62942 | €20,45 | €40,91 | €0,59 | €-0,00 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 601,77738 | €752,55 | €1.505,11 | €46,66 | €-27,66 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1209,81000 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €38,74 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2251,60000 | 2195,88092 | 1139,69979 | 2409,20720 | €999,19 | €1.998,39 | €53,97 | €-4,63 |
| Benchmark Donchian breakout 1H | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,44100 | 10,39356 | 5,41014 | 11,51209 | €910,44 | €1.820,87 | €54,32 | €-46,26 |
| Benchmark Donchian breakout 1H | PEPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €838,92 | €1.677,85 | €54,14 | €-0,34 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1209,81000 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €37,83 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2251,60000 | 2195,88092 | 1139,69979 | 2409,20720 | €975,67 | €1.951,34 | €52,70 | €-4,52 |
| Donchian 1H Gb20 120R V1 | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,44100 | 10,39356 | 5,41014 | 11,51209 | €889,00 | €1.778,00 | €53,04 | €-45,17 |
| Donchian 1H Gb20 120R V1 | PEPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €819,17 | €1.638,34 | €52,87 | €-0,33 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €21,92 | €43,84 | €0,72 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 69,29086 | 71,00600 | 66,00489 | 34,99188 | 76,51998 | €468,29 | €936,58 | €44,42 | €23,18 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2264,89289 | 2251,60000 | 2194,41461 | 1143,77091 | 2419,94510 | €713,61 | €1.427,21 | €44,41 | €-8,38 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 563,35265 | 553,00000 | 543,94622 | 284,49309 | 606,04680 | €630,03 | €1.260,05 | €43,41 | €-23,16 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €694,13 | €1.388,25 | €52,29 | €2,01 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2265,72305 | 2251,60000 | 2200,51783 | 1144,19014 | 2396,13352 | €95,49 | €190,98 | €5,50 | €-1,19 |
| Scanner Top 5 Long 1H | LINK | LONG | Scanner Top 5 Long | 60m | 2,0x | 10,57611 | 10,44100 | 10,27850 | 5,34094 | 11,17135 | €897,38 | €1.794,76 | €50,51 | €-22,93 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €826,05 | €1.652,09 | €51,22 | €-30,36 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.627,25 | €3.254,49 | €48,28 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €632,56 | €1.265,11 | €47,66 | €1,83 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2265,72305 | 2251,60000 | 2200,51783 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €4,53 | €-0,98 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 10,57611 | 10,44100 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €-20,90 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €752,74 | €1.505,47 | €46,67 | €-27,67 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €632,56 | €1.265,11 | €47,66 | €1,83 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2265,72305 | 2251,60000 | 2200,51783 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €4,53 | €-0,98 |
| Scanner Top15 Long | LINK | LONG | Scanner Top15 Long | 60m | 2,0x | 10,57611 | 10,44100 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €-20,90 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €752,74 | €1.505,47 | €46,67 | €-27,67 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €632,56 | €1.265,11 | €47,66 | €1,83 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2265,72305 | 2251,60000 | 2200,51783 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €4,53 | €-0,98 |
| Scanner Top20 Long | LINK | LONG | Scanner Top20 Long | 60m | 2,0x | 10,57611 | 10,44100 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €-20,90 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €752,74 | €1.505,47 | €46,67 | €-27,67 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2377,51300 | €996,44 | €1.992,87 | €48,44 | €-4,62 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 90,05113 | €1.131,85 | €2.263,69 | €48,39 | €-30,33 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 604,79730 | €742,15 | €1.484,30 | €47,17 | €-32,23 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €803,14 | €1.606,29 | €46,65 | €-0,32 |
| Scanner Top5 Btc Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2377,51300 | €934,11 | €1.868,22 | €45,41 | €-4,33 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 90,05113 | €1.061,05 | €2.122,10 | €45,37 | €-28,43 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 604,79730 | €695,73 | €1.391,46 | €44,22 | €-30,21 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €752,91 | €1.505,82 | €43,73 | €-0,30 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2377,51300 | €977,21 | €1.954,43 | €47,50 | €-4,53 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 90,05113 | €1.108,06 | €2.216,13 | €47,38 | €-29,69 |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 604,79730 | €723,60 | €1.447,20 | €46,00 | €-31,42 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2377,51300 | €954,49 | €1.908,97 | €46,40 | €-4,42 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 90,05113 | €1.082,29 | €2.164,59 | €46,27 | €-29,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 604,79730 | €706,77 | €1.413,54 | €44,93 | €-30,69 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2421,39727 | €964,53 | €1.929,06 | €46,89 | €-4,47 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 91,52201 | €12,51 | €25,03 | €0,54 | €-0,34 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 619,16975 | €730,27 | €1.460,53 | €46,42 | €-31,71 |
| Scanner Top5 Btc Runner25 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,10808 | 1,10110 | 1,08231 | 0,55958 | 1,18540 | €965,82 | €1.931,64 | €44,93 | €-12,17 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €778,28 | €1.556,56 | €45,20 | €-0,31 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2421,39727 | €965,10 | €1.930,19 | €46,92 | €-4,47 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 91,52201 | €12,52 | €25,04 | €0,54 | €-0,34 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 619,16975 | €730,69 | €1.461,39 | €46,45 | €-31,73 |
| Scanner Top5 Btc Tp3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,10808 | 1,10110 | 1,08231 | 0,55958 | 1,18540 | €966,39 | €1.932,77 | €44,95 | €-12,18 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €778,74 | €1.557,47 | €45,23 | €-0,31 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €29,12 | €58,23 | €0,96 | €-0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 69,29086 | 71,00600 | 66,00489 | 34,99188 | 76,51998 | €482,28 | €964,56 | €45,74 | €23,88 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2264,89289 | 2251,60000 | 2194,41461 | 1143,77091 | 2419,94510 | €734,93 | €1.469,85 | €45,74 | €-8,63 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 563,35265 | 553,00000 | 543,94622 | 284,49309 | 606,04680 | €638,64 | €1.277,28 | €44,00 | €-23,47 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2377,51300 | €956,00 | €1.911,99 | €46,47 | €-4,43 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 86,00620 | 84,85400 | 84,16759 | 43,43313 | 90,05113 | €1.085,91 | €2.171,82 | €46,43 | €-29,10 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 565,27303 | 553,00000 | 547,30746 | 285,46288 | 604,79730 | €712,03 | €1.424,06 | €45,26 | €-30,92 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €770,55 | €1.541,10 | €44,76 | €-0,31 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2366,54194 | €1.019,03 | €2.038,05 | €49,54 | €-4,72 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €657,43 | €1.314,85 | €49,53 | €1,91 |
| Combo Adaptive | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71314 | 10,44100 | 10,42552 | 5,41014 | 11,28838 | €44,00 | €88,00 | €2,36 | €-2,24 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €777,43 | €1.554,85 | €48,21 | €-28,57 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 69,29086 | 71,00600 | 66,33349 | 34,99188 | 75,20559 | €499,01 | €998,02 | €42,60 | €24,70 |
| Combo Adaptive Mfe Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2264,89289 | 2251,60000 | 2201,46243 | 1143,77091 | 2391,75377 | €760,41 | €1.520,81 | €42,59 | €-8,93 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €686,79 | €1.373,59 | €42,59 | €-25,24 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €716,30 | €1.432,60 | €42,59 | €6,11 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Regime V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,65421 | 0,65421 | 0,66363 | 0,97804 | 0,63537 | €1.699,46 | €3.398,92 | €48,94 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2366,54194 | €1.013,64 | €2.027,27 | €49,28 | €-4,70 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €653,95 | €1.307,90 | €49,27 | €1,90 |
| Combo Adaptive Long Only V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71314 | 10,44100 | 10,42552 | 5,41014 | 11,28838 | €920,99 | €1.841,98 | €49,45 | €-46,79 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €774,40 | €1.548,80 | €48,02 | €-28,46 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2366,54194 | €978,51 | €1.957,03 | €47,57 | €-4,54 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €631,29 | €1.262,58 | €47,56 | €1,83 |
| Combo Adaptive Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71314 | 10,44100 | 10,42552 | 5,41014 | 11,28838 | €42,25 | €84,51 | €2,27 | €-2,15 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 563,35265 | 553,00000 | 545,88686 | 284,49309 | 598,28422 | €746,52 | €1.493,04 | €46,29 | €-27,44 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 85,47309 | 84,85400 | 82,51462 | 43,16391 | 92,86927 | €715,87 | €1.431,74 | €49,56 | €-10,37 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 85,47309 | 84,85400 | 82,51462 | 43,16391 | 93,75681 | €727,07 | €1.454,13 | €50,33 | €-10,53 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 85,43891 | 84,85400 | 88,12735 | 127,73117 | 80,59971 | €797,18 | €1.594,36 | €50,17 | €10,91 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 85,47309 | 84,85400 | 82,24567 | 43,16391 | 93,54165 | €665,34 | €1.330,67 | €50,25 | €-9,64 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2265,72305 | 2251,60000 | 2200,51783 | 1521,81065 | 2396,13352 | €563,60 | €1.690,79 | €48,66 | €-10,54 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2258,11153 | 2251,60000 | 2161,85309 | 1140,34632 | 2498,75762 | €577,20 | €1.154,41 | €49,21 | €-3,33 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2256,83128 | 2251,60000 | 2208,07099 | 1515,83834 | 2354,35187 | €760,21 | €2.280,63 | €49,27 | €-5,29 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2264,81695 | 2251,60000 | 2319,13290 | 3008,43184 | 2183,34301 | €679,82 | €2.039,45 | €48,91 | €11,90 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1515,83834 | 2366,54194 | €670,92 | €2.012,75 | €48,92 | €-4,67 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2251,60000 | 2201,97595 | 1139,69979 | 2366,54194 | €1.016,16 | €2.032,33 | €49,40 | €-4,71 |
| Combo Adaptive Side Regime Guard V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 71,00600 | 68,23231 | 35,80610 | 76,24492 | €655,47 | €1.310,95 | €49,38 | €1,90 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €798,26 | €1.596,51 | €47,47 | €6,81 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | Combo Trend | 60m | 2,0x | 70,90318 | 71,00600 | 67,93555 | 35,80610 | 77,43197 | €617,91 | €1.235,82 | €51,72 | €1,79 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2265,72305 | 2251,60000 | 2193,27280 | 1144,19014 | 2425,11361 | €812,72 | €1.625,45 | €51,98 | €-10,13 |
| Combo Trend Side Regime Guard V1 | LINK | LONG | Combo Trend | 60m | 2,0x | 10,71314 | 10,44100 | 10,39356 | 5,41014 | 11,41622 | €12,55 | €25,10 | €0,75 | €-0,64 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €756,93 | €1.513,87 | €50,01 | €6,45 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 70,90318 | 71,00600 | 68,23231 | 47,62330 | 76,24492 | €416,31 | €1.248,92 | €47,05 | €1,81 |
| 1H Balanced V3 Long Only V1 | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 10,71314 | 10,44100 | 10,42552 | 7,19566 | 11,28838 | €14,74 | €44,23 | €1,19 | €-1,12 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2251,60000 | 2181,35381 | 1510,45050 | 2383,72136 | €502,31 | €1.506,93 | €45,20 | €1,87 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1209,81000 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €-11,82 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.639,87 | €3.279,73 | €48,65 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.642,36 | €3.284,73 | €48,72 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | 2026-08-20T05:05:45+00:00 | 550,71968 | €-54,03 | -1,04 | STOP |
| Scanner Top5 Btc Tp3 V1 | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-58,17 | -1,24 | STOP_GAP_STRESS |
| Scanner Top5 Btc Runner25 V1 | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-58,14 | -1,24 | STOP_GAP_STRESS |
| Scanner Top5 Btc Mfe V1 | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-56,31 | -1,24 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard V1 | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-1,37 | -1,24 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Mfe V1 | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-1,34 | -1,24 | STOP_GAP_STRESS |
| Scanner Top 5 + forza BTC 1H | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-60,06 | -1,24 | STOP_GAP_STRESS |
| Donchian 1H Gb20 120R V1 | ZEC | LONG | 2026-08-20T04:06:36+00:00 | 551,15112 | €-5,52 | -1,16 | STOP_GAP_STRESS |
| Benchmark Donchian breakout 1H | ZEC | LONG | 2026-08-20T04:06:36+00:00 | 551,15112 | €-5,65 | -1,16 | STOP_GAP_STRESS |
| Combo Scanner | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-57,63 | -1,24 | STOP_GAP_STRESS |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | 2026-08-20T04:06:36+00:00 | 551,15112 | €-0,99 | -1,29 | STOP_GAP_STRESS |
| Combo Adaptive Side Regime Guard V1 | LINK | LONG | 2026-08-20T04:06:36+00:00 | 10,39256 | €-61,25 | -1,24 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
