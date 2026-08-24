# Paper trading automatico KuCoin

Generato: 2026-08-24T05:33:00+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-24T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-24T05:05:29+00:00 | 2026-08-24T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-24T04:45:00+00:00 | 2026-08-24T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-24T04:00:00+00:00 | 2026-08-24T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-24T00:00:00+00:00 | 2026-08-24T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | SUI | 60m | LONG | 4,68 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | SUI | 60m | LONG | 4,68 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | SUI | 60m | LONG | 4,68 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,90 | 6,00 | 0,10 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 5,54 | 6,00 | 0,46 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,34 | 6,00 | 2,66 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | ENA | 60m | LONG | 7,00 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 V1 | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.813,31 | -1,87% | €64,97 | €3.000,00 | 2,17% | 6 | 51 | 37,25% | 0,87 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 51 | 2129 | PRIME INDICAZIONI | 100 (mancano 49) |

- Trade del Principale 4H chiusi: **51**; win rate **37,25%**; profit factor **0,87**.
- Expectancy: **€-3,76** per trade; P&L netto: **€-191,70**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.813,31 | €700,92 | €2.102,75 | €194,16 | €6,11 |
| TEST | Benchmark Donchian breakout 1H | 3 | €11.378,40 | €2.377,87 | €4.755,73 | €165,71 | €-61,71 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.325,48 | €1.224,43 | €3.673,28 | €225,61 | €-39,94 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €11.191,12 | €983,31 | €1.966,61 | €170,14 | €-42,94 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €11.110,51 | €2.321,88 | €4.643,76 | €161,81 | €-60,26 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.012,97 | €1.128,26 | €2.256,51 | €220,54 | €-32,78 |
| TEST | Main Side Regime Guard V1 | 6 | €10.837,07 | €677,33 | €2.031,99 | €163,22 | €46,06 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.708,56 | €1.285,81 | €3.857,42 | €214,19 | €-49,09 |
| TEST | Combo Adaptive | 6 | €10.681,29 | €1.366,21 | €2.732,43 | €212,26 | €-33,59 |
| TEST | Combo Adaptive Long Only V1 | 3 | €10.584,00 | €1.266,54 | €2.533,08 | €152,56 | €-29,84 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.493,30 | €702,19 | €1.404,39 | €112,68 | €-4,50 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.445,90 | €1.478,68 | €4.436,03 | €208,92 | €-44,16 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.433,40 | €1.264,39 | €2.528,78 | €208,30 | €-9,06 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.427,30 | €1.263,65 | €2.527,30 | €208,18 | €-9,06 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.378,79 | €1.469,18 | €4.407,53 | €207,58 | €-43,88 |
| TEST | Scanner Top10 Long | 5 | €10.347,42 | €2.774,91 | €5.549,82 | €206,57 | €-30,61 |
| TEST | Ampia 4H | 7 | €10.333,13 | €998,50 | €1.997,00 | €206,18 | €1,28 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.281,84 | €1.053,65 | €2.107,29 | €205,89 | €-30,58 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.270,10 | €1.223,91 | €3.671,73 | €205,42 | €-33,04 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.198,33 | €141,85 | €425,56 | €51,07 | €-14,72 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.182,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.168,90 | €330,98 | €661,97 | €50,82 | €4,72 |
| TEST | Sol Donchian 1H | 0 | €10.156,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €10.124,24 | €674,61 | €1.349,21 | €100,68 | €-22,13 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 6 | €10.099,73 | €1.463,70 | €4.391,10 | €202,01 | €-14,56 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.069,51 | €1.077,05 | €3.231,16 | €202,98 | €-13,21 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.053,56 | €1.193,26 | €3.579,78 | €201,07 | €-41,85 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.029,09 | €356,10 | €712,19 | €50,12 | €5,07 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.027,52 | €349,20 | €1.047,59 | €50,20 | €-10,86 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €10.020,91 | €545,14 | €1.090,27 | €100,72 | €-45,84 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.015,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.008,83 | €248,90 | €746,70 | €50,09 | €-8,41 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.003,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.952,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €9.951,56 | €1.654,66 | €3.309,32 | €200,40 | €-53,72 |
| TEST | Scanner Top20 Long | 7 | €9.951,56 | €1.654,66 | €3.309,32 | €200,40 | €-53,72 |
| TEST | Btc Ema 1H | 0 | €9.941,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.929,80 | €487,73 | €975,47 | €49,56 | €19,30 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.924,39 | €720,33 | €1.440,66 | €98,38 | €-15,46 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.897,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.894,87 | €538,28 | €1.076,56 | €99,45 | €-45,26 |
| TEST | Sol Adaptive 1H | 1 | €9.884,90 | €344,23 | €1.032,69 | €49,48 | €-10,70 |
| TEST | Sol Bollinger 1H | 0 | €9.873,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.871,67 | €1.305,96 | €3.917,88 | €197,46 | €-37,16 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.868,12 | €864,47 | €1.728,95 | €150,71 | €-6,89 |
| TEST | Eth Ema 1H | 0 | €9.866,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.864,56 | €1.010,88 | €2.021,77 | €197,54 | €-29,34 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.848,66 | €1.604,00 | €3.208,01 | €194,94 | €-47,65 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.801,99 | €843,27 | €1.686,53 | €97,62 | €-40,24 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.754,28 | €1.495,69 | €4.487,08 | €194,67 | €-34,00 |
| TEST | Eth Donchian 1H | 0 | €9.730,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 6 | €9.665,74 | €1.188,02 | €2.376,05 | €146,41 | €-26,32 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.638,72 | €987,74 | €1.975,48 | €193,02 | €-28,67 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.638,62 | €844,37 | €1.688,74 | €147,20 | €-6,73 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 1 | €9.626,03 | €350,27 | €1.050,81 | €48,13 | €-0,21 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.576,13 | €879,98 | €2.639,95 | €141,92 | €-1,49 |
| TEST | 1H Fast V3 Long Only V1 | 7 | €9.550,64 | €1.328,96 | €3.986,89 | €191,01 | €-38,57 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €9.547,78 | €1.247,34 | €2.494,67 | €144,18 | €21,79 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.525,12 | €1.008,33 | €3.025,00 | €189,53 | €-12,21 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 5 | €9.434,55 | €988,41 | €1.976,81 | €143,49 | €-6,17 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.381,70 | €1.210,83 | €2.421,66 | €138,78 | €22,05 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 1 | €9.370,10 | €340,96 | €1.022,87 | €46,85 | €-0,20 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 3 | €9.347,45 | €1.212,30 | €3.636,90 | €140,27 | €-5,54 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.319,54 | €879,76 | €1.759,52 | €96,67 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.305,36 | €878,42 | €1.756,85 | €96,53 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.233,75 | €871,66 | €1.743,33 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €9.193,60 | €1.129,99 | €2.259,98 | €139,26 | €-25,04 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.188,59 | €1.686,73 | €3.373,47 | €138,42 | €-36,80 |
| TEST | Combo Adaptive Mfe Trail | 4 | €9.185,50 | €957,91 | €1.915,82 | €91,47 | €-16,11 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.114,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.813,31 | €-191,70 | 51 | 51 | 37,25% | 0,87 | €-3,76 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.378,40 | €1.442,38 | 96 | 96 | 50,00% | 1,68 | €15,02 | 4,69% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.325,48 | €1.368,06 | 130 | 130 | 55,38% | 1,54 | €10,52 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.191,12 | €1.235,99 | 100 | 100 | 57,00% | 1,71 | €12,36 | 4,57% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.110,51 | €1.172,98 | 64 | 64 | 50,00% | 1,94 | €18,33 | 4,69% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.012,97 | €1.047,57 | 129 | 129 | 50,39% | 1,41 | €8,12 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.837,07 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 2,40% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.708,56 | €760,43 | 192 | 192 | 50,52% | 1,21 | €3,96 | 6,39% |
| TEST | Combo Adaptive | Combo Adaptive | €10.681,29 | €717,21 | 139 | 139 | 46,04% | 1,31 | €5,16 | 7,91% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.584,00 | €615,76 | 111 | 111 | 49,55% | 1,26 | €5,55 | 6,25% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.493,30 | €499,27 | 108 | 108 | 49,07% | 1,23 | €4,62 | 8,68% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.445,90 | €492,81 | 177 | 177 | 51,98% | 1,16 | €2,78 | 9,50% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.433,40 | €444,40 | 95 | 95 | 44,21% | 1,21 | €4,68 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.427,30 | €438,28 | 99 | 99 | 44,44% | 1,20 | €4,43 | 12,06% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.378,79 | €425,40 | 221 | 221 | 45,70% | 1,10 | €1,92 | 9,48% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.347,42 | €381,65 | 113 | 113 | 51,33% | 1,19 | €3,38 | 10,31% |
| TEST | Ampia 4H | Confluenza trend | €10.333,13 | €333,13 | 51 | 51 | 35,29% | 1,29 | €6,53 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.281,84 | €314,11 | 116 | 116 | 46,55% | 1,13 | €2,71 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.270,10 | €305,40 | 207 | 207 | 41,06% | 1,08 | €1,48 | 6,56% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.198,33 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,68% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.182,21 | €182,21 | 45 | 40 | 46,67% | 1,16 | €4,05 | 3,89% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.168,90 | €164,84 | 6 | 6 | 50,00% | 2,46 | €27,47 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.156,88 | €156,88 | 12 | 12 | 50,00% | 1,63 | €13,07 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.124,24 | €147,49 | 139 | 139 | 46,04% | 1,06 | €1,06 | 8,69% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.099,73 | €117,74 | 50 | 50 | 48,00% | 1,11 | €2,35 | 3,73% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.069,51 | €85,29 | 145 | 145 | 43,45% | 1,03 | €0,59 | 9,12% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.053,56 | €97,64 | 136 | 136 | 46,32% | 1,03 | €0,72 | 10,60% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,17 | €46,17 | 9 | 9 | 55,56% | 1,19 | €5,13 | 1,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Sol Ema 4H | Trend following EMA | €10.029,09 | €24,73 | 7 | 7 | 28,57% | 1,11 | €3,53 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Sol Ema 1H | Trend following EMA | €10.027,52 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.020,91 | €67,52 | 36 | 36 | 50,00% | 1,08 | €1,88 | 4,21% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.015,51 | €15,51 | 15 | 15 | 40,00% | 1,32 | €1,03 | 0,53% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Doge Ema 1H | Trend following EMA | €10.008,83 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.003,10 | €3,10 | 15 | 15 | 40,00% | 1,32 | €0,21 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,43 | €-47,57 | 15 | 15 | 40,00% | 0,45 | €-3,17 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.951,56 | €7,69 | 112 | 112 | 50,89% | 1,00 | €0,07 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.951,56 | €7,69 | 112 | 112 | 50,89% | 1,00 | €0,07 | 10,31% |
| TEST | Btc Ema 1H | Trend following EMA | €9.941,95 | €-58,05 | 11 | 11 | 36,36% | 0,82 | €-5,28 | 1,94% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Eth Ema 4H | Trend following EMA | €9.929,80 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.924,39 | €-58,95 | 52 | 52 | 48,08% | 0,95 | €-1,13 | 5,38% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.897,54 | €-102,46 | 12 | 12 | 41,67% | 0,74 | €-8,54 | 3,14% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.894,87 | €-59,11 | 36 | 36 | 44,44% | 0,93 | €-1,64 | 5,41% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.884,90 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.873,88 | €-126,12 | 10 | 10 | 40,00% | 0,69 | €-12,61 | 2,37% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.871,67 | €-88,75 | 193 | 193 | 45,08% | 0,98 | €-0,46 | 9,00% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.868,12 | €-123,80 | 97 | 97 | 41,24% | 0,95 | €-1,28 | 7,34% |
| TEST | Eth Ema 1H | Trend following EMA | €9.866,33 | €-133,67 | 17 | 17 | 41,18% | 0,77 | €-7,86 | 4,80% |
| TEST | Combo Scanner | Combo Scanner | €9.864,56 | €-104,47 | 120 | 120 | 45,83% | 0,96 | €-0,87 | 11,38% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.848,66 | €-101,42 | 75 | 75 | 41,33% | 0,94 | €-1,35 | 8,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.801,99 | €-156,48 | 104 | 99 | 42,31% | 0,95 | €-1,50 | 10,88% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.754,28 | €-208,93 | 90 | 90 | 46,67% | 0,89 | €-2,32 | 9,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.730,51 | €-269,49 | 12 | 12 | 25,00% | 0,51 | €-22,46 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.665,74 | €-305,73 | 15 | 15 | 26,67% | 0,44 | €-20,38 | 5,46% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.638,72 | €-331,03 | 108 | 108 | 45,37% | 0,85 | €-3,07 | 12,28% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.638,62 | €-353,48 | 114 | 114 | 42,11% | 0,87 | €-3,10 | 8,78% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.626,03 | €-373,13 | 130 | 130 | 41,54% | 0,89 | €-2,87 | 10,37% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.576,13 | €-420,44 | 99 | 91 | 43,43% | 0,80 | €-4,25 | 8,84% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.550,64 | €-408,32 | 149 | 149 | 41,61% | 0,88 | €-2,74 | 12,52% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.547,78 | €-471,84 | 62 | 62 | 38,71% | 0,75 | €-7,61 | 7,99% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.525,12 | €-460,26 | 102 | 102 | 44,12% | 0,77 | €-4,51 | 8,85% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | Combo Trend | Combo Trend | €9.434,55 | €-557,51 | 149 | 149 | 38,93% | 0,84 | €-3,74 | 10,85% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.381,70 | €-638,24 | 78 | 78 | 38,46% | 0,71 | €-8,18 | 7,27% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.370,10 | €-629,09 | 88 | 88 | 43,18% | 0,78 | €-7,15 | 10,69% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.347,45 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,84% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.319,54 | €-679,41 | 59 | 59 | 32,20% | 0,60 | €-11,52 | 8,31% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,36 | €-693,59 | 60 | 60 | 31,67% | 0,58 | €-11,56 | 8,31% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.233,75 | €-765,20 | 87 | 87 | 32,18% | 0,66 | €-8,80 | 9,41% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.193,60 | €-779,26 | 61 | 61 | 34,43% | 0,57 | €-12,77 | 11,72% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.188,59 | €-770,84 | 120 | 120 | 38,33% | 0,68 | €-6,42 | 12,31% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.185,50 | €-796,48 | 149 | 149 | 41,61% | 0,74 | €-5,35 | 15,45% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,32 | €-885,68 | 38 | 38 | 36,84% | 0,48 | €-23,31 | 10,65% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
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
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 76,47929 | 79,80100 | 78,92617 | 51,36859 | 86,46833 | €10,44 | €31,32 | €0,00 | €1,36 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,48800 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €4,53 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,47325 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €0,22 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,51 | €64,54 | €5,62 | €-2,39 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 81,52730 | 79,80100 | 78,98606 | 54,75917 | 86,60979 | €497,57 | €1.492,70 | €46,53 | €-31,61 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €184,87 | €554,60 | €48,28 | €-20,56 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 798,37964 | 831,89000 | 817,96285 | 536,24499 | 927,34406 | €8,81 | €26,44 | €0,00 | €1,11 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16380 | 0,16752 | 0,15392 | 0,11002 | 0,18358 | €263,92 | €791,77 | €47,79 | €17,97 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 831,89000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €17,37 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,47325 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €-0,31 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,77 | €26,32 | €2,02 | €0,04 |
| Bilanciata 1H V3 Filtered | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00497 | 0,00479 | 0,00351 | 0,00611 | €197,24 | €591,72 | €49,81 | €-29,76 |
| Bilanciata 1H V3 Filtered | SUI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,84147 | 0,82480 | 0,80853 | 0,56519 | 0,90734 | €9,48 | €28,45 | €1,11 | €-0,56 |
| 1H Fast Score 6 75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €350,27 | €1.050,81 | €48,13 | €-0,21 |
| 1H Fast Score 6 75 No Trend Up V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €340,96 | €1.022,87 | €46,85 | €-0,20 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,47399 | 1,47325 | 1,38051 | 0,99003 | 1,61422 | €284,39 | €853,18 | €54,11 | €-0,43 |
| 1H Fast Score 6 75 Cost Aware V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00523 | 0,00497 | 0,00489 | 0,00351 | 0,00574 | €260,23 | €780,70 | €51,11 | €-39,26 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €412,11 | €1.236,33 | €56,63 | €-0,25 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49738 | 1,47325 | 1,40463 | 1,00574 | 1,63650 | €272,47 | €817,41 | €50,63 | €-13,17 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09209 | 0,08782 | 0,06154 | 0,09732 | €406,05 | €1.218,14 | €50,55 | €6,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,83617 | 0,82480 | 0,81103 | 0,56163 | 0,87387 | €22,96 | €68,87 | €2,07 | €-0,94 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00516 | 0,00497 | 0,00489 | 0,00347 | 0,00557 | €9,37 | €28,12 | €1,47 | €-1,06 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €413,29 | €1.239,88 | €50,62 | €-5,46 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €339,56 | €1.018,68 | €46,66 | €-0,20 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49835 | 1,47325 | 1,43358 | 1,00639 | 1,59551 | €415,25 | €1.245,74 | €53,85 | €-20,87 |
| 1H Fast No Pepe V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00497 | 0,00480 | 0,00346 | 0,00567 | €266,74 | €800,21 | €53,85 | €-27,68 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €24,71 | €74,13 | €3,03 | €-0,33 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €358,96 | €1.076,89 | €49,33 | €-0,22 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09209 | 0,08782 | 0,06154 | 0,09922 | €9,51 | €28,53 | €1,18 | €0,15 |
| 1H Fast Tp2 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 99,21056 | €9,00 | €26,99 | €0,57 | €-0,31 |
| 1H Fast Tp2 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00497 | 0,00484 | 0,00346 | 0,00576 | €261,16 | €783,47 | €46,57 | €-27,10 |
| 1H Fast Tp2 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 903,79618 | €420,43 | €1.261,30 | €51,50 | €-5,55 |
| 1H Fast Tp2 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,18290 | €362,09 | €1.086,26 | €49,76 | €-0,22 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €262,56 | €787,69 | €51,10 | €-38,03 |
| Rapida 1H V3 Filtered | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 98,19868 | €10,94 | €32,83 | €0,70 | €-0,38 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €413,22 | €1.239,66 | €50,61 | €-5,46 |
| Rapida 1H V3 Filtered | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €20,47 | €61,41 | €2,81 | €-0,01 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €381,89 | €1.145,68 | €46,78 | €-5,04 |
| 1H Fast V3 Cap75 V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €340,18 | €1.020,53 | €46,75 | €-0,20 |
| 1H Fast V3 Cap75 V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,82496 | 0,82480 | 0,79875 | 0,55410 | 0,86429 | €490,23 | €1.470,69 | €46,74 | €-0,29 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €229,21 | €687,62 | €44,60 | €-33,20 |
| 1H Fast V3 Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 98,19868 | €9,77 | €29,31 | €0,62 | €-0,34 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €380,44 | €1.141,32 | €46,60 | €-5,02 |
| 1H Fast V3 Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €18,99 | €56,97 | €2,61 | €-0,01 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €252,96 | €758,88 | €49,23 | €-36,64 |
| 1H Fast V3 No Esports V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €359,25 | €1.077,76 | €49,37 | €-0,22 |
| 1H Fast V3 No Esports V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,82496 | 0,82480 | 0,79875 | 0,55410 | 0,86429 | €497,34 | €1.492,03 | €47,42 | €-0,30 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €249,75 | €749,26 | €48,60 | €-36,18 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €412,37 | €1.237,11 | €50,51 | €-5,44 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €365,83 | €1.097,49 | €50,27 | €-0,22 |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,82496 | 0,82480 | 0,79875 | 0,55410 | 0,86429 | €22,31 | €66,93 | €2,13 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €264,26 | €792,79 | €51,43 | €-38,28 |
| 1H Fast V3 No Esports Mfe Lock V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 98,19868 | €11,01 | €33,04 | €0,70 | €-0,38 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €415,89 | €1.247,68 | €50,94 | €-5,49 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €20,60 | €61,81 | €2,83 | €-0,01 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | SUI | LONG | Confluenza trend | 240m | 2,0x | 0,86357 | 0,82480 | 0,75994 | 0,43610 | 1,15373 | €215,46 | €430,92 | €51,71 | €-19,35 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2437,32000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,11 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 79,80100 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,17 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,48800 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €20,35 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €286,19 | €572,37 | €49,83 | €-21,22 |
| Forza relativa 1H V2 | PUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00510 | 0,00497 | 0,00476 | 0,00258 | 0,00586 | €356,70 | €713,40 | €47,79 | €-19,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00497 | 0,00474 | 0,00264 | 0,00643 | €312,08 | €624,15 | €57,84 | €-30,14 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2464,63283 | 2437,32000 | 2414,66831 | 1244,63958 | 2589,54414 | €1.424,54 | €2.849,08 | €57,76 | €-31,57 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00497 | 0,00474 | 0,00264 | 0,00643 | €304,73 | €609,46 | €56,48 | €-29,43 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2464,63283 | 2437,32000 | 2414,66831 | 1244,63958 | 2589,54414 | €1.391,00 | €2.782,00 | €56,40 | €-30,83 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 76719,31079 | 76954,40000 | 74671,22818 | 38743,25195 | 81225,09269 | €833,14 | €1.666,28 | €44,48 | €5,11 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 95,05001 | 94,06500 | 89,98943 | 48,00025 | 106,18327 | €434,46 | €868,92 | €46,26 | €-9,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 831,89000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €1,03 |
| Benchmark trend following EMA 1H | TRUMP | LONG | Trend following EMA | 60m | 2,0x | 2,70054 | 2,48800 | 2,42296 | 1,36377 | 3,31121 | €215,60 | €431,20 | €44,32 | €-33,94 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €322,02 | €644,04 | €56,06 | €-23,88 |
| Scanner Top 5 Long 1H | PUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €316,31 | €632,61 | €53,01 | €-7,05 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €-3,34 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18358 | €32,80 | €65,60 | €3,96 | €1,49 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,77 | €577,53 | €50,27 | €-21,42 |
| Scanner Top10 Long | SUI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,83617 | 0,82480 | 0,80385 | 0,42226 | 0,90081 | €14,11 | €28,22 | €1,09 | €-0,38 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2462,71244 | 2437,32000 | 2415,97708 | 1243,66978 | 2556,18319 | €1.366,78 | €2.733,55 | €51,88 | €-28,19 |
| Scanner Top10 Long | ENA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18358 | €426,83 | €853,65 | €51,52 | €19,37 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €-21,58 |
| Scanner Top15 Long | PUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €-6,50 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €-3,02 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 81,06421 | 79,80100 | 78,65294 | 40,93743 | 85,88675 | €677,13 | €1.354,27 | €40,28 | €-21,10 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2462,71244 | 2437,32000 | 2415,97708 | 1243,66978 | 2556,18319 | €73,71 | €147,42 | €2,80 | €-1,52 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €-21,58 |
| Scanner Top20 Long | PUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €-6,50 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €-3,02 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 81,06421 | 79,80100 | 78,65294 | 40,93743 | 85,88675 | €677,13 | €1.354,27 | €40,28 | €-21,10 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2462,71244 | 2437,32000 | 2415,97708 | 1243,66978 | 2556,18319 | €73,71 | €147,42 | €2,80 | €-1,52 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €300,64 | €601,28 | €52,34 | €-22,30 |
| Scanner Top 5 + forza BTC 1H | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €295,30 | €590,60 | €49,49 | €-6,58 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €-3,12 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18555 | €31,22 | €62,44 | €3,77 | €1,42 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €281,84 | €563,67 | €49,07 | €-20,90 |
| Scanner Top5 Btc Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €276,83 | €553,66 | €46,39 | €-6,17 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €-2,92 |
| Scanner Top5 Btc Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18555 | €29,27 | €58,53 | €3,53 | €1,33 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,88 | €69,75 | €6,07 | €-2,59 |
| Scanner Top5 Btc Guard V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €276,09 | €552,19 | €46,27 | €-6,16 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,48800 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €-0,69 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €343,20 | €686,40 | €48,35 | €2,54 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €285,92 | €571,84 | €0,00 | €24,00 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,47325 | 1,39078 | 0,76104 | 1,76273 | €297,64 | €595,28 | €45,91 | €-13,34 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €298,93 | €597,86 | €44,42 | €1,48 |
| Scanner Top5 Btc Btc Le3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09338 | 0,09209 | 0,08853 | 0,04716 | 0,10406 | €12,59 | €25,17 | €1,31 | €-0,35 |
| Scanner Top5 Btc Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00497 | 0,00486 | 0,00266 | 0,00618 | €14,29 | €28,58 | €2,23 | €-1,65 |
| Scanner Top5 Btc Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,31528 | €220,63 | €441,25 | €45,38 | €-35,18 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €300,60 | €601,20 | €0,00 | €25,23 |
| Scanner Top5 Btc Btc 2 3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,47325 | 1,39078 | 0,76104 | 1,76273 | €312,93 | €625,85 | €48,27 | €-14,02 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €314,28 | €628,56 | €46,70 | €1,55 |
| Scanner Top5 Btc Btc 2 3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09338 | 0,09209 | 0,08853 | 0,04716 | 0,10406 | €13,23 | €26,47 | €1,38 | €-0,37 |
| Scanner Top5 Btc Btc 2 3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00497 | 0,00486 | 0,00266 | 0,00618 | €15,02 | €30,05 | €2,35 | €-1,74 |
| Scanner Top5 Btc Btc 2 3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,31528 | €231,96 | €463,91 | €47,71 | €-36,99 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,07 | €68,13 | €5,93 | €-2,53 |
| Scanner Top5 Btc Guard Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €269,67 | €539,35 | €45,19 | €-6,01 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,48800 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €-0,67 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €335,22 | €670,44 | €47,23 | €2,48 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €297,01 | €594,01 | €0,00 | €24,93 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €313,56 | €627,12 | €46,59 | €1,55 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,47325 | 1,40541 | 0,75645 | 1,70147 | €13,15 | €26,30 | €1,62 | €-0,43 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €273,00 | €546,00 | €45,75 | €-6,09 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,48800 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €-0,67 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €337,92 | €675,84 | €47,61 | €2,50 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €291,91 | €583,82 | €0,00 | €24,50 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,18 | €616,36 | €45,79 | €1,52 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,47325 | 1,40541 | 0,75645 | 1,70147 | €12,92 | €25,84 | €1,60 | €-0,43 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €268,32 | €536,63 | €44,97 | €-5,98 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €329,50 | €659,00 | €46,42 | €2,43 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 831,89000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €0,59 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,79 | €607,58 | €52,89 | €-22,53 |
| Scanner Top5 Btc Runner25 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00629 | €300,08 | €600,16 | €50,29 | €-6,69 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,19346 | €431,33 | €862,66 | €52,07 | €19,58 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 831,89000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €0,59 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,97 | €607,94 | €52,92 | €-22,54 |
| Scanner Top5 Btc Tp3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00629 | €300,25 | €600,51 | €50,32 | €-6,69 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,19346 | €431,58 | €863,17 | €52,10 | €19,59 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 831,89000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €14,69 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €246,56 | €493,12 | €47,70 | €-18,29 |
| Combo Trend | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00498 | 0,00497 | 0,00455 | 0,00252 | 0,00595 | €266,27 | €532,54 | €46,71 | €-1,82 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2464,63283 | 2437,32000 | 2414,66831 | 1244,63958 | 2574,55479 | €34,26 | €68,51 | €1,39 | €-0,76 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,44 | €576,88 | €50,22 | €-21,39 |
| Combo Scanner | PUMP | LONG | Combo Scanner | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €283,32 | €566,63 | €47,48 | €-6,32 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €-2,99 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18555 | €29,95 | €59,91 | €3,62 | €1,36 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 831,89000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €18,26 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €306,63 | €613,26 | €53,38 | €-22,74 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,35487 | 94,06500 | 91,03919 | 47,64921 | 100,98622 | €14,11 | €28,23 | €0,99 | €-0,09 |
| Combo Adaptive | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00497 | 0,00478 | 0,00262 | 0,00604 | €329,34 | €658,69 | €53,47 | €-29,03 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 831,89000 | 808,90107 | 408,00543 | 948,00078 | €270,67 | €541,33 | €0,00 | €16,05 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €269,51 | €539,03 | €46,92 | €-19,99 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,49835 | 1,47325 | 1,41507 | 0,75667 | 1,66491 | €363,44 | €726,87 | €40,40 | €-12,18 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €283,16 | €566,31 | €49,30 | €-21,00 |
| Combo Adaptive Quality7 V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00497 | 0,00478 | 0,00262 | 0,00604 | €302,38 | €604,77 | €49,09 | €-26,65 |
| Combo Adaptive Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €294,95 | €589,90 | €49,43 | €-6,58 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €425,38 | €850,76 | €48,95 | €-8,88 |
| Combo Adaptive Quality7 Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €295,78 | €591,56 | €49,57 | €-6,59 |
| Combo Adaptive Quality7 Regime V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,25967 | €242,50 | €485,00 | €49,88 | €-38,67 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,39 | €616,77 | €53,69 | €-22,87 |
| Combo Adaptive Long Only V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €312,68 | €625,36 | €52,40 | €-6,97 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €292,79 | €585,58 | €50,97 | €-21,71 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,24985 | 94,06500 | 90,79388 | 47,59617 | 101,16178 | €12,54 | €25,08 | €0,92 | €-0,05 |
| Combo Adaptive Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €16,58 | €33,16 | €2,78 | €-0,37 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €299,55 | €599,09 | €50,20 | €-6,68 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,25967 | €245,59 | €491,18 | €50,52 | €-39,16 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 95,05001 | 94,06500 | 90,49549 | 63,84192 | 104,15904 | €349,20 | €1.047,59 | €50,20 | €-10,86 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,39968 | 94,06500 | 86,82624 | 47,16684 | 109,83325 | €356,10 | €712,19 | €50,12 | €5,07 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 95,05001 | 94,06500 | 90,49549 | 63,84192 | 104,15904 | €344,23 | €1.032,69 | €49,48 | €-10,70 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,39968 | 94,06500 | 86,22866 | 47,16684 | 111,32722 | €330,98 | €661,97 | €50,82 | €4,72 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2437,32000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €19,30 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09314 | 0,09209 | 0,08689 | 0,06256 | 0,10563 | €248,90 | €746,70 | €50,09 | €-8,41 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 831,89000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €18,14 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €304,59 | €609,17 | €53,03 | €-22,59 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,24985 | 94,06500 | 90,79388 | 47,59617 | 101,16178 | €14,20 | €28,40 | €1,04 | €-0,06 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00468 | 0,00497 | 0,00481 | 0,00314 | 0,00580 | €149,89 | €449,66 | €0,00 | €28,09 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 79,80100 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €17,92 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,47325 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €0,06 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2437,32000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,01 |
| Main Dynamic Asset Selector V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00515 | 0,00497 | 0,00453 | 0,00346 | 0,00638 | €141,85 | €425,56 | €51,07 | €-14,72 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 831,89000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €8,54 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €293,50 | €586,99 | €56,78 | €-21,77 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 94,24985 | 94,06500 | 90,40989 | 47,59617 | 102,69776 | €13,97 | €27,94 | €1,14 | €-0,05 |
| Combo Trend Side Regime Guard V1 | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00523 | 0,00497 | 0,00474 | 0,00264 | 0,00631 | €294,84 | €589,68 | €55,15 | €-29,65 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 831,89000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €16,43 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,47325 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €-0,30 |
| 1H Balanced V3 Long Only V1 | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00497 | 0,00479 | 0,00351 | 0,00611 | €184,35 | €553,04 | €46,55 | €-27,81 |
| 1H Balanced V3 Long Only V1 | SUI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,84147 | 0,82480 | 0,80853 | 0,56519 | 0,90734 | €9,09 | €27,28 | €1,07 | €-0,54 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | BTC | LONG | 2026-08-24T05:00:00+00:00 | 76820,29411 | €-0,51 | -1,12 | STOP |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | LONG | 2026-08-24T05:00:00+00:00 | 76820,29411 | €-0,58 | -1,12 | STOP |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | 2026-08-24T03:45:00+00:00 | 79,29354 | €-55,77 | -1,04 | STOP |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61608 | €-49,77 | -1,04 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61608 | €-48,61 | -1,04 | STOP |
| Benchmark trend following EMA 1H | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,33676 | €-1,51 | -1,04 | STOP |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61436 | €-57,76 | -1,04 | STOP |
| Benchmark Donchian breakout 1H | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61436 | €-59,15 | -1,04 | STOP |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | 2026-08-24T02:15:00+00:00 | 0,81569 | €-0,85 | -1,05 | STOP |
| 1H Fast Tp2 V1 | SUI | LONG | 2026-08-24T02:15:00+00:00 | 0,81569 | €-0,86 | -1,05 | STOP |
| 1H Balanced Long No Rhv V1 | XRP | LONG | 2026-08-24T02:15:00+00:00 | 1,46240 | €-1,13 | -1,04 | STOP |
| 1H Fast V3 No Esports V1 | SUI | LONG | 2026-08-24T02:00:00+00:00 | 0,82310 | €-1,48 | -1,05 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
