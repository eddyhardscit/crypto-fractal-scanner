# Paper trading automatico KuCoin

Generato: 2026-08-11T05:23:09+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-11T05:08:36+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-11T05:08:36+00:00 | 2026-08-11T05:08:36+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-11T04:45:00+00:00 | 2026-08-11T04:45:00+00:00 | 8,9 min | 25,0 min | OK |
| 60m | 12 | 2026-08-11T04:00:00+00:00 | 2026-08-11T04:00:00+00:00 | 8,9 min | 45,0 min | OK |
| 240m | 12 | 2026-08-11T00:00:00+00:00 | 2026-08-11T00:00:00+00:00 | 1,15 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Strict3 V1 | SPCX | 60m | LONG | 5,89 | 0,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | SPCX | 60m | LONG | 5,89 | 5,50 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | SPCX | 60m | LONG | 5,89 | 5,50 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced Long No Rhv V1 | SPCX | 60m | LONG | 5,89 | 5,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BEAT | 240m | SHORT | -9,75 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SPCX | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,20 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,28 | 6,00 | 2,72 | STALE_CANDLE | 1,15 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,15 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,41 | 6,00 | 4,59 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,12 | 6,00 | 4,88 | STALE_CANDLE | 1,15 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,94 | 6,00 | 5,06 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -0,85 | 6,00 | 5,15 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOXL | 240m | SHORT | -0,25 | 6,00 | 5,75 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Benchmark trend following EMA 1H | HYPE | 60m | LONG | 6,61 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | HYPE | 60m | LONG | 6,61 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Side Regime Guard V1 | HYPE | 60m | LONG | 6,61 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V1 | BEAT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | BEAT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Cap75 V1 | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.802,53 | -1,97% | €54,18 | €3.000,00 | 1,81% | 4 | 33 | 36,36% | 0,83 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 33 | 1041 | PRIME INDICAZIONI | 100 (mancano 67) |

- Trade del Principale 4H chiusi: **33**; win rate **36,36%**; profit factor **0,83**.
- Expectancy: **€-5,31** per trade; P&L netto: **€-175,07**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.802,53 | €1.619,55 | €4.858,66 | €194,15 | €-24,49 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.510,79 | €3.285,77 | €6.571,55 | €158,30 | €-48,02 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 3 | €10.461,10 | €2.794,65 | €8.383,96 | €157,41 | €-40,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 2 | €10.453,42 | €328,49 | €985,47 | €104,92 | €-38,09 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.435,20 | €2.962,76 | €8.888,29 | €209,08 | €-45,02 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.419,03 | €2.884,53 | €8.653,58 | €207,84 | €-15,81 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.373,00 | €2.499,17 | €4.998,35 | €155,32 | €20,48 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 1 | €10.365,76 | €144,44 | €433,33 | €52,00 | €-33,87 |
| TEST | Bilanciata 1H V1 | 5 | €10.347,75 | €2.867,82 | €8.603,45 | €155,23 | €47,86 |
| TEST | Main Side Regime Guard V1 | 1 | €10.310,14 | €747,08 | €2.241,25 | €51,13 | €-5,84 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.271,29 | €3.242,25 | €9.726,76 | €205,48 | €-1,67 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.263,33 | €3.208,41 | €6.416,83 | €154,57 | €-46,89 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 1 | €10.261,93 | €143,00 | €428,99 | €51,48 | €-33,53 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.257,93 | €5.318,44 | €10.636,89 | €205,70 | €-55,25 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.241,48 | €2.467,49 | €4.934,97 | €153,35 | €20,23 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €10.205,79 | €3.428,49 | €10.285,47 | €203,89 | €-5,25 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 2 | €10.193,29 | €320,32 | €960,95 | €102,31 | €-37,14 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.184,54 | €141,92 | €425,75 | €51,09 | €-33,28 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.157,75 | €2.883,99 | €8.651,97 | €203,52 | €-43,82 |
| TEST | Combo Adaptive | 4 | €10.154,76 | €3.979,00 | €7.958,01 | €202,39 | €14,73 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 4 | €10.107,15 | €2.240,68 | €6.722,04 | €202,31 | €-8,82 |
| TEST | Combo Adaptive Runner25 V1 | 5 | €10.103,12 | €2.735,23 | €5.470,46 | €153,63 | €98,53 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.074,30 | €1.168,55 | €3.505,64 | €50,48 | €-19,83 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €10.035,65 | €6.026,02 | €12.052,04 | €200,51 | €-29,88 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 4 | €10.027,42 | €3.588,75 | €10.766,24 | €199,78 | €2,11 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €10.020,66 | €6.699,40 | €13.398,80 | €150,09 | €9,23 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €10.005,42 | €6.689,21 | €13.378,42 | €149,86 | €9,21 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.003,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.000,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.997,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.996,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.983,90 | €6.681,70 | €13.363,40 | €149,69 | €0,20 |
| TEST | Scanner Bottom15 Short | 4 | €9.983,90 | €6.681,70 | €13.363,40 | €149,69 | €0,20 |
| TEST | Scanner Bottom20 Short | 4 | €9.983,90 | €6.681,70 | €13.363,40 | €149,69 | €0,20 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.983,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.972,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 4 | €9.961,90 | €3.565,30 | €10.695,89 | €198,48 | €2,09 |
| TEST | Btc Adaptive 1H | 0 | €9.959,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.953,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 3 | €9.952,78 | €2.422,29 | €4.844,57 | €148,96 | €23,83 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.945,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 5 | €9.936,50 | €1.922,32 | €3.844,65 | €98,60 | €74,60 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.928,42 | €6.637,73 | €13.275,47 | €148,71 | €9,14 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 3 | €9.927,94 | €2.066,85 | €6.200,54 | €148,63 | €6,84 |
| TEST | Forza relativa 1H V2 | 3 | €9.926,23 | €2.976,40 | €5.952,81 | €148,95 | €-4,43 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.925,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.921,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 1 | €9.914,48 | €207,25 | €414,51 | €49,74 | €-33,39 |
| TEST | Combo Adaptive Tp3 V1 | 5 | €9.914,38 | €2.684,13 | €5.368,26 | €150,76 | €96,69 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.898,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 4 | €9.897,68 | €2.194,24 | €6.582,72 | €198,12 | €-8,64 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.867,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €9.859,98 | €2.375,57 | €4.751,14 | €147,64 | €19,47 |
| TEST | Btc Ema 1H | 1 | €9.858,94 | €1.141,05 | €3.423,15 | €49,29 | €2,32 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.854,74 | €2.728,30 | €8.184,91 | €196,58 | €-14,96 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €9.854,21 | €2.374,18 | €4.748,36 | €147,55 | €19,46 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.840,12 | €1.759,32 | €3.518,64 | €49,16 | €9,67 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.838,04 | €137,09 | €411,27 | €49,35 | €-32,15 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.824,22 | €2.366,96 | €4.733,91 | €147,10 | €19,40 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 3 | €9.810,16 | €2.775,65 | €5.551,31 | €147,03 | €10,32 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.806,06 | €2.774,49 | €5.548,99 | €146,97 | €10,31 |
| TEST | Master Adaptive Gb20 Partial V1 | 3 | €9.799,73 | €2.772,70 | €5.545,40 | €146,87 | €10,31 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.786,76 | €2.357,93 | €4.715,86 | €146,54 | €19,33 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.778,65 | €2.766,74 | €5.533,48 | €146,56 | €10,28 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.765,85 | €2.763,12 | €5.526,23 | €146,37 | €10,27 |
| TEST | Global Confluence puro 1H | 1 | €9.765,36 | €1.528,83 | €3.057,65 | €48,92 | €-17,30 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.761,96 | €1.952,30 | €3.904,60 | €46,86 | €2,81 |
| TEST | Master Adaptive V1 | 3 | €9.761,82 | €2.761,98 | €5.523,95 | €146,31 | €10,27 |
| TEST | 1H Fast V3 No Esports V1 | 4 | €9.759,12 | €3.492,72 | €10.478,17 | €194,44 | €2,05 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €9.751,06 | €3.820,82 | €7.641,64 | €194,35 | €14,15 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 4 | €9.713,67 | €5.214,25 | €10.428,49 | €194,31 | €11,47 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.705,00 | €2.338,23 | €4.676,46 | €145,32 | €19,17 |
| TEST | Combo Scanner | 4 | €9.697,14 | €4.007,41 | €8.014,82 | €193,43 | €8,95 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 3 | €9.687,71 | €3.456,41 | €6.912,81 | €140,82 | €12,79 |
| TEST | Forza relativa 1H V1 | 4 | €9.663,22 | €2.526,29 | €5.052,59 | €192,86 | €-6,55 |
| TEST | 1H Balanced Long No Rhv V1 | 3 | €9.656,65 | €1.886,59 | €5.659,76 | €144,85 | €3,30 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.655,66 | €2.326,35 | €4.652,69 | €144,58 | €19,07 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.632,12 | €2.725,28 | €5.450,56 | €144,36 | €10,13 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €9.599,91 | €2.312,91 | €4.625,82 | €143,74 | €18,96 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 3 | €9.554,34 | €2.301,93 | €4.603,87 | €143,06 | €18,87 |
| TEST | Scanner Top15 Long | 3 | €9.554,34 | €2.301,93 | €4.603,87 | €143,06 | €18,87 |
| TEST | Scanner Top20 Long | 3 | €9.554,34 | €2.301,93 | €4.603,87 | €143,06 | €18,87 |
| TEST | Combo Trend | 5 | €9.524,56 | €3.845,62 | €7.691,23 | €190,81 | €-42,15 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.479,29 | €2.283,85 | €4.567,70 | €141,94 | €18,72 |
| TEST | 1H Fast V3 Long Only V1 | 3 | €9.452,48 | €1.967,86 | €5.903,59 | €141,51 | €6,51 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.397,49 | €2.817,86 | €5.635,72 | €141,02 | €-4,19 |
| TEST | Combo Adaptive Mfe Trail | 4 | €9.371,26 | €3.672,00 | €7.344,00 | €186,78 | €13,59 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.802,53 | €-175,07 | 33 | 33 | 36,36% | 0,83 | €-5,31 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.510,79 | €562,76 | 40 | 40 | 52,50% | 1,62 | €14,07 | 3,09% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.461,10 | €506,14 | 36 | 36 | 52,78% | 1,93 | €14,06 | 1,96% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.453,42 | €492,11 | 64 | 64 | 46,88% | 1,41 | €7,69 | 2,83% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.435,20 | €485,55 | 75 | 75 | 44,00% | 1,37 | €6,47 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.419,03 | €440,04 | 66 | 66 | 39,39% | 1,33 | €6,67 | 2,82% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.373,00 | €355,52 | 50 | 50 | 44,00% | 1,30 | €7,11 | 5,09% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.365,76 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.347,75 | €305,06 | 75 | 75 | 45,33% | 1,24 | €4,07 | 3,56% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.310,14 | €317,32 | 18 | 18 | 50,00% | 1,84 | €17,63 | 2,40% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.271,29 | €278,80 | 41 | 39 | 51,22% | 1,36 | €6,80 | 2,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.263,33 | €314,07 | 8 | 8 | 62,50% | 6,29 | €39,26 | 1,61% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.261,93 | €295,72 | 12 | 12 | 58,33% | 2,80 | €24,64 | 1,78% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.257,93 | €319,56 | 35 | 35 | 54,29% | 1,76 | €9,13 | 1,58% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.241,48 | €224,22 | 41 | 41 | 39,02% | 1,25 | €5,47 | 4,25% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.205,79 | €217,21 | 68 | 68 | 44,12% | 1,16 | €3,19 | 4,04% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.193,29 | €231,01 | 28 | 28 | 46,43% | 1,69 | €8,25 | 1,76% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.184,54 | €218,07 | 13 | 13 | 53,85% | 1,74 | €16,77 | 2,28% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.157,75 | €206,76 | 33 | 33 | 51,52% | 1,32 | €6,27 | 3,20% |
| TEST | Combo Adaptive | Combo Adaptive | €10.154,76 | €144,81 | 42 | 42 | 42,86% | 1,24 | €3,45 | 3,05% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.107,15 | €120,01 | 73 | 73 | 43,84% | 1,09 | €1,64 | 2,79% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.103,12 | €7,88 | 44 | 44 | 36,36% | 1,01 | €0,18 | 2,31% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Doge Ema 1H | Trend following EMA | €10.074,30 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.035,65 | €72,76 | 32 | 32 | 50,00% | 1,14 | €2,27 | 2,89% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.027,42 | €31,78 | 60 | 60 | 50,00% | 1,03 | €0,53 | 4,01% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €10.020,66 | €19,47 | 21 | 21 | 42,86% | 1,06 | €0,93 | 1,38% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €10.005,42 | €4,23 | 22 | 22 | 40,91% | 1,01 | €0,19 | 1,53% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.003,85 | €3,85 | 23 | 23 | 43,48% | 1,04 | €0,17 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,77 | €0,77 | 23 | 23 | 43,48% | 1,04 | €0,03 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.997,70 | €-2,30 | 7 | 7 | 42,86% | 0,94 | €-0,33 | 0,36% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.996,69 | €-3,31 | 7 | 7 | 28,57% | 0,24 | €-0,47 | 0,04% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,44 | €-5,56 | 11 | 11 | 27,27% | 0,38 | €-0,51 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,04 | €-10,96 | 13 | 13 | 30,77% | 0,26 | €-0,84 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.983,90 | €-8,28 | 27 | 27 | 40,74% | 0,98 | €-0,31 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.983,90 | €-8,28 | 27 | 27 | 40,74% | 0,98 | €-0,31 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.983,90 | €-8,28 | 27 | 27 | 40,74% | 0,98 | €-0,31 | 2,72% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.983,45 | €-16,55 | 7 | 7 | 28,57% | 0,24 | €-2,36 | 0,19% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.972,22 | €-27,78 | 11 | 11 | 27,27% | 0,38 | €-2,53 | 0,53% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.961,90 | €-33,78 | 104 | 104 | 37,50% | 0,98 | €-0,32 | 3,98% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.959,54 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 0,89% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.953,21 | €-46,79 | 13 | 13 | 30,77% | 0,37 | €-3,60 | 0,71% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.952,78 | €-68,14 | 20 | 20 | 25,00% | 0,81 | €-3,41 | 2,34% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.945,22 | €-54,78 | 13 | 13 | 30,77% | 0,26 | €-4,21 | 0,72% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Ampia 4H | Confluenza trend | €9.936,50 | €-135,92 | 27 | 27 | 25,93% | 0,82 | €-5,03 | 4,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.928,42 | €-72,76 | 49 | 49 | 36,73% | 0,92 | €-1,48 | 5,48% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.927,94 | €-75,18 | 36 | 36 | 38,89% | 0,90 | €-2,09 | 4,81% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.926,23 | €-65,77 | 55 | 54 | 38,18% | 0,96 | €-1,20 | 5,53% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.925,12 | €-74,88 | 11 | 11 | 27,27% | 0,10 | €-6,81 | 0,89% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.921,51 | €-78,49 | 23 | 23 | 43,48% | 0,39 | €-3,41 | 0,84% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.914,48 | €-51,88 | 27 | 27 | 33,33% | 0,88 | €-1,92 | 2,73% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.914,38 | €-179,09 | 25 | 25 | 36,00% | 0,61 | €-7,16 | 2,55% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.898,26 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,48% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.897,68 | €-89,74 | 80 | 80 | 35,00% | 0,94 | €-1,12 | 2,94% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Sol Ema 1H | Trend following EMA | €9.867,86 | €-132,14 | 7 | 7 | 28,57% | 0,52 | €-18,88 | 2,09% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.859,98 | €-156,64 | 26 | 26 | 30,77% | 0,80 | €-6,02 | 4,98% |
| TEST | Btc Ema 1H | Trend following EMA | €9.858,94 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,57% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.854,74 | €-125,39 | 22 | 22 | 31,82% | 0,72 | €-5,70 | 2,51% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.854,21 | €-162,40 | 30 | 30 | 33,33% | 0,79 | €-5,41 | 5,29% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.840,12 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,63% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.838,04 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.824,22 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,66% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.810,16 | €-196,83 | 22 | 22 | 18,18% | 0,66 | €-8,95 | 3,42% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.806,06 | €-200,92 | 22 | 22 | 31,82% | 0,74 | €-9,13 | 3,64% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.799,73 | €-207,25 | 17 | 17 | 29,41% | 0,62 | €-12,19 | 2,99% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.786,76 | €-229,74 | 22 | 22 | 31,82% | 0,64 | €-10,44 | 4,73% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.778,65 | €-228,32 | 21 | 21 | 28,57% | 0,68 | €-10,87 | 3,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.765,85 | €-241,11 | 19 | 19 | 26,32% | 0,66 | €-12,69 | 4,03% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.765,36 | €-215,51 | 13 | 13 | 30,77% | 0,44 | €-16,58 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,96 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.761,82 | €-245,13 | 19 | 19 | 26,32% | 0,66 | €-12,90 | 4,07% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.759,12 | €-236,64 | 78 | 78 | 37,18% | 0,85 | €-3,03 | 3,95% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.751,06 | €-258,50 | 43 | 43 | 39,53% | 0,67 | €-6,01 | 3,97% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.713,67 | €-291,54 | 46 | 46 | 30,43% | 0,71 | €-6,34 | 3,97% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.705,00 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 4,25% |
| TEST | Combo Scanner | Combo Scanner | €9.697,14 | €-307,00 | 50 | 50 | 36,00% | 0,77 | €-6,14 | 5,37% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.687,71 | €-320,93 | 19 | 19 | 21,05% | 0,55 | €-16,89 | 4,72% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.663,22 | €-327,20 | 54 | 54 | 27,78% | 0,75 | €-6,06 | 7,55% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.656,65 | €-343,26 | 20 | 20 | 25,00% | 0,47 | €-17,16 | 4,33% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.655,66 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.632,12 | €-374,74 | 54 | 54 | 55,56% | 0,59 | €-6,94 | 4,27% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.599,91 | €-416,27 | 34 | 34 | 32,35% | 0,46 | €-12,24 | 5,33% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.554,34 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,61% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.554,34 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,61% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.554,34 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,61% |
| TEST | Combo Trend | Combo Trend | €9.524,56 | €-428,67 | 64 | 64 | 31,25% | 0,77 | €-6,70 | 7,64% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.479,29 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,73% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.452,48 | €-550,49 | 56 | 56 | 28,57% | 0,62 | €-9,83 | 6,86% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.397,49 | €-594,93 | 27 | 27 | 22,22% | 0,49 | €-22,03 | 6,23% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.371,26 | €-637,93 | 52 | 52 | 28,85% | 0,48 | €-12,27 | 7,57% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,07003 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €3,24 |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01310 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €-5,56 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 137,17000 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €3,81 |
| Principale 4H | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,31391 | 1,39730 | 1,47158 | 1,74531 | 0,99857 | €136,42 | €409,27 | €49,11 | €-25,98 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 137,17000 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €3,61 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 55,32406 | 55,42000 | 54,37122 | 37,15933 | 57,22974 | €997,04 | €2.991,13 | €51,52 | €5,19 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,02104 | 1,01310 | 1,01832 | 1,35628 | 0,99163 | €1.192,22 | €3.576,67 | €0,00 | €27,80 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,28356 | 1,31820 | 1,12953 | 0,86212 | 1,59161 | €142,82 | €428,45 | €51,41 | €11,56 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €17,86 | €53,57 | €0,77 | €-0,30 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 55,29106 | 55,42000 | 54,45225 | 37,13716 | 56,96867 | €1.060,90 | €3.182,69 | €48,28 | €7,42 |
| 1H Balanced Long No Rhv V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,32770 | 1,31820 | 1,16837 | 0,89177 | 1,64634 | €134,09 | €402,26 | €48,27 | €-2,88 |
| 1H Balanced Long No Rhv V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 137,25230 | 137,17000 | 134,05746 | 92,18780 | 143,64199 | €691,60 | €2.074,81 | €48,30 | €-1,24 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,01393 | 1,01310 | 1,02853 | 1,34683 | 0,98473 | €1.189,68 | €3.569,03 | €51,39 | €2,91 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,32770 | 1,31820 | 1,16837 | 0,89177 | 1,64634 | €142,72 | €428,16 | €51,38 | €-3,06 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 55,42308 | 55,42000 | 54,61538 | 37,22584 | 57,03848 | €1.174,31 | €3.522,93 | €51,34 | €-0,20 |
| Bilanciata 1H V2 | SPCX | LONG | Confluenza trend V2 | 60m | 3,0x | 137,25230 | 137,17000 | 134,05746 | 92,18780 | 143,64199 | €735,55 | €2.206,64 | €51,36 | €-1,32 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 137,17000 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €3,66 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,37122 | 37,15933 | 57,22974 | €1.010,10 | €3.030,31 | €52,19 | €5,25 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €1.207,28 | €3.621,85 | €52,15 | €-20,49 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,17163 | 0,89426 | 1,65093 | €142,48 | €427,43 | €51,29 | €-4,24 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.304,60 | €3.913,81 | €52,43 | €6,79 |
| 1H Fast Score 6 75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €175,99 | €527,96 | €52,23 | €-5,23 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.337,47 | €4.012,40 | €52,32 | €-12,64 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €144,71 | €434,12 | €52,09 | €-33,93 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.269,92 | €3.809,75 | €51,03 | €6,61 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €171,31 | €513,92 | €50,84 | €-5,09 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.301,91 | €3.905,72 | €50,93 | €-12,30 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €140,86 | €422,58 | €50,71 | €-33,03 |
| 1H Fast Score 6 75 Range Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €141,92 | €425,75 | €51,09 | €-33,28 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.307,16 | €3.921,49 | €52,53 | €6,80 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.341,98 | €4.025,95 | €52,50 | €-12,68 |
| 1H Fast Score 6 75 Cost Aware V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €145,51 | €436,52 | €52,38 | €-34,12 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €145,72 | €437,17 | €52,46 | €-34,17 |
| 1H Fast Nohigh Cap75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,32770 | 1,31820 | 1,20067 | 0,89177 | 1,51824 | €182,77 | €548,30 | €52,46 | €-3,92 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.267,13 | €3.801,40 | €50,92 | €6,59 |
| 1H Fast No Pepe V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,28356 | 1,31820 | 1,14107 | 0,86212 | 1,49729 | €152,86 | €458,58 | €50,91 | €12,38 |
| 1H Fast No Pepe V1 | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €682,89 | €2.048,66 | €50,88 | €5,51 |
| 1H Fast No Pepe V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29313 | 1,39730 | 1,44831 | 1,71771 | 1,06037 | €137,80 | €413,39 | €49,61 | €-33,30 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,80626 | €1.240,87 | €3.722,61 | €49,87 | €6,46 |
| 1H Fast Tp2 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,28356 | 1,31820 | 1,14107 | 0,86212 | 1,56853 | €149,69 | €449,08 | €49,85 | €12,12 |
| 1H Fast Tp2 V1 | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 143,59705 | €668,73 | €2.006,20 | €49,82 | €5,40 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29313 | 1,39730 | 1,44831 | 1,71771 | 0,98278 | €134,94 | €404,82 | €48,58 | €-32,61 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.247,94 | €3.743,81 | €50,15 | €6,49 |
| Rapida 1H V3 Filtered | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €672,56 | €2.017,68 | €50,11 | €5,43 |
| Rapida 1H V3 Filtered | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01197 | 1,01310 | 1,02330 | 1,34423 | 0,99497 | €1.481,61 | €4.444,83 | €49,78 | €-4,97 |
| Rapida 1H V3 Filtered | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €163,19 | €489,56 | €48,43 | €-4,85 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.271,22 | €3.813,65 | €51,09 | €6,61 |
| 1H Fast V3 Cap75 V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €685,11 | €2.055,32 | €51,04 | €5,53 |
| 1H Fast V3 Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €171,42 | €514,25 | €50,88 | €-5,10 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.300,75 | €3.902,26 | €50,89 | €-12,29 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €137,09 | €411,27 | €49,35 | €-32,15 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.175,70 | €3.527,10 | €47,25 | €6,12 |
| 1H Fast V3 Long Only V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €633,63 | €1.900,88 | €47,21 | €5,11 |
| 1H Fast V3 Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €158,54 | €475,61 | €47,05 | €-4,71 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.222,54 | €3.667,61 | €49,13 | €6,36 |
| 1H Fast V3 No Esports V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €658,87 | €1.976,61 | €49,09 | €5,32 |
| 1H Fast V3 No Esports V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01197 | 1,01310 | 1,02330 | 1,34423 | 0,99497 | €1.451,45 | €4.354,36 | €48,77 | €-4,87 |
| 1H Fast V3 No Esports V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €159,86 | €479,59 | €47,45 | €-4,75 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.234,84 | €3.704,51 | €49,62 | €6,42 |
| 1H Fast V3 No Esports Long Only V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €665,50 | €1.996,50 | €49,58 | €5,37 |
| 1H Fast V3 No Esports Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €166,51 | €499,53 | €49,42 | €-4,95 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.256,15 | €3.768,44 | €50,48 | €6,53 |
| 1H Fast V3 No Esports Mfe Lock V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €676,98 | €2.030,95 | €50,44 | €5,46 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01197 | 1,01310 | 1,02330 | 1,34423 | 0,99497 | €1.491,36 | €4.474,07 | €50,11 | €-5,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €164,26 | €492,78 | €48,75 | €-4,88 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07003 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,01 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,01310 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €-4,33 |
| Ampia 4H | BEAT | SHORT | Confluenza trend | 240m | 2,0x | 1,71466 | 1,39730 | 1,71466 | 2,56341 | 1,13853 | €205,47 | €410,93 | €0,00 | €76,06 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 137,17000 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €2,88 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €3,37 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.397,93 | €2.795,86 | €48,15 | €4,85 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €200,59 | €401,18 | €48,14 | €10,83 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,31391 | 1,39730 | 1,47158 | 1,96429 | 0,96704 | €201,67 | €403,34 | €48,40 | €-25,60 |
| Forza relativa 1H V2 | CYS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,67821 | €206,96 | €413,93 | €49,67 | €-2,96 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 55,42308 | 55,42000 | 54,61538 | 27,98866 | 57,20002 | €1.703,07 | €3.406,15 | €49,64 | €-0,19 |
| Forza relativa 1H V2 | SPCX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 137,25230 | 137,17000 | 134,05746 | 69,31241 | 144,28095 | €1.066,37 | €2.132,73 | €49,64 | €-1,28 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97149 | €1.650,43 | €3.300,86 | €52,81 | €-3,69 |
| Benchmark Donchian breakout 1H | BEAT | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,29313 | 1,39730 | 1,44831 | 1,93323 | 0,90519 | €219,77 | €439,54 | €52,74 | €-35,41 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 468,56302 | €1.415,57 | €2.831,15 | €52,74 | €-8,92 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97149 | €1.611,57 | €3.223,15 | €51,57 | €-3,61 |
| Donchian 1H Gb20 120R V1 | BEAT | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,29313 | 1,39730 | 1,44831 | 1,93323 | 0,90519 | €214,59 | €429,19 | €51,50 | €-34,57 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 468,56302 | €1.382,25 | €2.764,49 | €51,50 | €-8,71 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,01237 | 1,01310 | 1,00022 | 0,51125 | 1,03060 | €1.952,30 | €3.904,60 | €46,86 | €2,81 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 64026,93000 | 65095,57044 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €48,54 | €2,06 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 137,17000 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €3,06 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,02104 | 1,01310 | 1,03737 | 1,52645 | 0,98510 | €1.516,32 | €3.032,64 | €48,52 | €23,57 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06718 | €1.522,48 | €3.044,96 | €48,72 | €-17,23 |
| Scanner Top 5 Long 1H | CYS | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €215,74 | €431,48 | €51,78 | €11,65 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €3,63 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.502,84 | €3.005,68 | €51,77 | €5,21 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.717,56 | €3.435,12 | €0,00 | €26,70 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €49,45 | €2,33 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.722,95 | €3.445,90 | €49,62 | €-10,56 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.480,14 | €2.960,29 | €49,63 | €-9,33 |
| Scanner Top10 Long | CYS | LONG | Scanner Top10 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €198,71 | €397,43 | €47,69 | €10,73 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €3,34 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.384,23 | €2.768,46 | €47,68 | €4,80 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.728,78 | €3.457,57 | €0,00 | €26,87 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €2,35 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06964 | 0,07003 | 0,07064 | 0,10411 | 0,06763 | €1.736,20 | €3.472,41 | €50,00 | €-19,64 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.488,41 | €2.976,82 | €49,91 | €-9,38 |
| Scanner Top15 Long | CYS | LONG | Scanner Top15 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €198,71 | €397,43 | €47,69 | €10,73 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €3,34 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.384,23 | €2.768,46 | €47,68 | €4,80 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.728,78 | €3.457,57 | €0,00 | €26,87 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €2,35 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06964 | 0,07003 | 0,07064 | 0,10411 | 0,06763 | €1.736,20 | €3.472,41 | €50,00 | €-19,64 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.488,41 | €2.976,82 | €49,91 | €-9,38 |
| Scanner Top20 Long | CYS | LONG | Scanner Top20 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €198,71 | €397,43 | €47,69 | €10,73 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €3,34 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.384,23 | €2.768,46 | €47,68 | €4,80 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.728,78 | €3.457,57 | €0,00 | €26,87 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €2,35 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06964 | 0,07003 | 0,07064 | 0,10411 | 0,06763 | €1.736,20 | €3.472,41 | €50,00 | €-19,64 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.488,41 | €2.976,82 | €49,91 | €-9,38 |
| Scanner Top 5 + forza BTC 1H | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €213,00 | €426,01 | €51,12 | €11,50 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €3,58 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.483,78 | €2.967,57 | €51,11 | €5,15 |
| Scanner Top5 Btc Mfe V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €199,66 | €399,32 | €47,92 | €10,78 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €3,36 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.390,83 | €2.781,67 | €47,91 | €4,82 |
| Scanner Top5 Btc Guard V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €201,85 | €403,69 | €48,44 | €10,90 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €3,39 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.406,06 | €2.812,12 | €48,43 | €4,88 |
| Scanner Top5 Btc Btc Le3 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €203,55 | €407,09 | €48,85 | €10,99 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €3,42 |
| Scanner Top5 Btc Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.417,90 | €2.835,81 | €48,84 | €4,92 |
| Scanner Top5 Btc Guard Mfe V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €197,15 | €394,30 | €47,32 | €10,64 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €3,31 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.373,36 | €2.746,72 | €47,31 | €4,76 |
| Scanner Top5 Btc Guard Btc Le3 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €204,33 | €408,65 | €49,04 | €11,03 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €3,44 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.423,33 | €2.846,66 | €49,03 | €4,94 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €200,82 | €401,64 | €48,20 | €10,84 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €3,38 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.398,91 | €2.797,82 | €48,19 | €4,85 |
| Scanner Top5 Btc Runner25 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €204,95 | €409,90 | €49,19 | €11,06 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €3,45 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 58,18259 | €1.427,68 | €2.855,35 | €49,18 | €4,95 |
| Scanner Top5 Btc Tp3 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €205,07 | €410,14 | €49,22 | €11,07 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €3,45 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 58,18259 | €1.428,51 | €2.857,02 | €49,21 | €4,95 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06685 | €1.528,83 | €3.057,65 | €48,92 | €-17,30 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 137,17000 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €3,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06718 | €1.488,74 | €2.977,49 | €47,64 | €-16,84 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97635 | €1.480,58 | €2.961,16 | €47,38 | €-3,31 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 471,30966 | €34,52 | €69,05 | €1,29 | €-0,22 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,31391 | 1,39730 | 1,47158 | 1,96429 | 0,96704 | €195,22 | €390,44 | €46,85 | €-24,78 |
| Combo Mean Reversion | ZEC | LONG | Combo Mean Reversion | 60m | 2,0x | 491,64831 | 493,00000 | 484,77896 | 248,28240 | 502,63927 | €1.759,32 | €3.518,64 | €49,16 | €9,67 |
| Combo Scanner | CYS | LONG | Combo Scanner | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €201,94 | €403,87 | €48,46 | €10,90 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €3,39 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.406,69 | €2.813,38 | €48,45 | €4,88 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06760 | €1.668,13 | €3.336,26 | €48,04 | €-10,22 |
| Combo Adaptive | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €210,67 | €421,33 | €50,56 | €11,37 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €3,54 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.493,31 | €2.986,63 | €50,55 | €9,35 |
| Combo Adaptive | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.512,79 | €3.025,57 | €50,73 | €-9,53 |
| Combo Adaptive Mfe Trail | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €194,41 | €388,82 | €46,66 | €10,49 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €3,27 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.378,10 | €2.756,19 | €46,65 | €8,63 |
| Combo Adaptive Mfe Trail | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.396,07 | €2.792,13 | €46,81 | €-8,80 |
| Combo Adaptive Quality7 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,29313 | 1,39730 | 1,44831 | 1,93323 | 0,98278 | €207,25 | €414,51 | €49,74 | €-33,39 |
| Combo Adaptive Long Only V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €206,91 | €413,83 | €49,66 | €11,17 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €3,48 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.466,71 | €2.933,42 | €49,65 | €9,18 |
| Combo Adaptive Partial 1R V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €202,29 | €404,58 | €48,55 | €10,92 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €3,40 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.433,95 | €2.867,89 | €48,54 | €8,98 |
| Combo Adaptive Partial 1R V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.452,65 | €2.905,29 | €48,71 | €-9,15 |
| Combo Adaptive Runner25 V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €209,83 | €419,66 | €50,36 | €11,33 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €3,53 |
| Combo Adaptive Runner25 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 58,05212 | €1.487,37 | €2.974,74 | €50,35 | €9,31 |
| Combo Adaptive Runner25 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,71466 | 1,39730 | 1,50962 | 2,56341 | 1,09738 | €202,19 | €404,38 | €0,00 | €74,84 |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 466,73193 | €76,64 | €153,27 | €2,57 | €-0,48 |
| Combo Adaptive Tp3 V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €205,91 | €411,82 | €49,42 | €11,11 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €3,46 |
| Combo Adaptive Tp3 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 58,05212 | €1.459,58 | €2.919,17 | €49,41 | €9,14 |
| Combo Adaptive Tp3 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,71466 | 1,39730 | 1,50962 | 2,56341 | 1,09738 | €198,41 | €396,82 | €0,00 | €73,45 |
| Combo Adaptive Tp3 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 466,73193 | €75,20 | €150,41 | €2,52 | €-0,47 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 64026,93000 | 64993,05773 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €49,29 | €2,32 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €1.168,55 | €3.505,64 | €50,48 | €-19,83 |
| Master Adaptive V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €203,23 | €406,45 | €48,77 | €-2,91 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €5,68 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.607,06 | €3.214,12 | €48,76 | €7,50 |
| Master Adaptive No Alt V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €203,31 | €406,62 | €48,79 | €-2,91 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €5,68 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.607,72 | €3.215,45 | €48,78 | €7,50 |
| Master Adaptive Strict3 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €195,94 | €391,88 | €47,03 | €-2,80 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,42308 | 55,42000 | 54,61538 | 27,98866 | 57,03848 | €1.612,35 | €3.224,71 | €46,99 | €-0,18 |
| Master Adaptive Strict3 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 137,25230 | 137,17000 | 134,05746 | 69,31241 | 143,64199 | €1.009,56 | €2.019,13 | €47,00 | €-1,21 |
| Master Adaptive Expanded V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €204,15 | €408,29 | €49,00 | €-2,92 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €5,70 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.614,34 | €3.228,69 | €48,98 | €7,53 |
| Master Adaptive Gb20 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €200,53 | €401,05 | €48,13 | €-2,87 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €5,60 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.585,71 | €3.171,42 | €48,11 | €7,40 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,80567 | €203,58 | €407,15 | €48,86 | €-2,91 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €5,69 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 57,80747 | €1.609,83 | €3.219,66 | €48,84 | €7,51 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,01197 | 1,01310 | 1,02654 | 1,51289 | 0,98282 | €1.785,27 | €3.570,54 | €51,42 | €-4,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.784,78 | €3.569,55 | €51,40 | €-10,94 |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.534,08 | €3.068,15 | €51,44 | €-9,67 |
| Combo Adaptive Side Regime Guard V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,30406 | 1,39730 | 1,46055 | 1,94957 | 0,99108 | €214,32 | €428,65 | €51,44 | €-30,65 |
| Master Adaptive Gb20 Be V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €204,23 | €408,47 | €49,02 | €-2,92 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €5,71 |
| Master Adaptive Gb20 Be V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.615,02 | €3.230,04 | €49,00 | €7,53 |
| Master Adaptive Gb20 Partial V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €204,02 | €408,03 | €48,96 | €-2,92 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €5,70 |
| Master Adaptive Gb20 Partial V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.613,30 | €3.226,60 | €48,95 | €7,52 |
| Master Adaptive Gb20 Loss Cap V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,20521 | 0,67049 | 1,65434 | €262,28 | €524,56 | €48,40 | €-3,75 |
| Master Adaptive Gb20 Loss Cap V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 134,13373 | 69,06481 | 143,77074 | €1.259,04 | €2.518,08 | €48,39 | €7,51 |
| Master Adaptive Gb20 Loss Cap V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,66195 | 27,92198 | 56,96866 | €1.935,08 | €3.870,17 | €44,03 | €9,03 |
| 1H Fast V3 Nohigh Range Only V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €143,00 | €428,99 | €51,48 | €-33,53 |
| 1H Fast V3 Nohigh Regime Guard V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €144,44 | €433,33 | €52,00 | €-33,87 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01310 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €-5,84 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06718 | €1.566,82 | €3.133,64 | €50,14 | €-17,73 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97635 | €1.565,11 | €3.130,22 | €50,08 | €-3,50 |
| Combo Trend Side Regime Guard V1 | ZEC | SHORT | Combo Trend | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 471,30966 | €1.345,98 | €2.691,96 | €50,15 | €-8,48 |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | Combo Trend | 60m | 2,0x | 55,42308 | 55,42000 | 54,52564 | 27,98866 | 57,39746 | €1.548,11 | €3.096,22 | €50,14 | €-0,17 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €142,10 | €426,29 | €51,16 | €-33,32 |
| 1H Fast Nohigh Cap75 Short Only V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,32770 | 1,31820 | 1,20067 | 0,89177 | 1,51824 | €178,22 | €534,66 | €51,15 | €-3,82 |
| 1H Balanced V3 Long Only V1 | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 137,17000 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €3,46 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,37122 | 37,15933 | 57,22974 | €955,40 | €2.866,19 | €49,36 | €4,97 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €1.141,90 | €3.425,69 | €49,33 | €-19,38 |
| 1H Balanced V3 Long Only V1 | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,17163 | 0,89426 | 1,65093 | €134,76 | €404,29 | €48,51 | €-4,01 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.730,88 | €3.461,76 | €0,00 | €26,91 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €49,84 | €2,35 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.736,31 | €3.472,62 | €50,01 | €-10,64 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.491,62 | €2.983,24 | €50,02 | €-9,40 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.733,52 | €3.467,03 | €0,00 | €26,95 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €49,91 | €2,35 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.738,95 | €3.477,91 | €50,08 | €-10,66 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.493,89 | €2.987,79 | €50,09 | €-9,41 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Main Side Regime Guard V1 | DOGE | SHORT | 2026-08-11T04:10:31+00:00 | 0,07008 | €5,48 | 0,11 | TIME_EXIT |
| Forza relativa 1H V1 | BEAT | SHORT | 2026-08-11T03:24:37+00:00 | 1,26224 | €101,52 | 2,19 | TARGET |
| Combo Trend Side Regime Guard V1 | BEAT | SHORT | 2026-08-11T03:24:37+00:00 | 1,26224 | €109,10 | 2,19 | TARGET |
| Combo Trend | BEAT | SHORT | 2026-08-11T03:24:37+00:00 | 1,26224 | €102,11 | 2,19 | TARGET |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €98,25 | 1,99 | TARGET |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €98,40 | 1,99 | TARGET |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,49 | 1,99 | TARGET |
| Scanner Bottom20 Short | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,66 | 1,99 | TARGET |
| Scanner Bottom15 Short | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,66 | 1,99 | TARGET |
| Scanner Bottom10 Short | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,66 | 1,99 | TARGET |
| Combo Adaptive Side Regime Guard V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €101,75 | 1,99 | TARGET |
| Combo Adaptive Partial 1R V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €93,09 | 1,99 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
