# Paper trading automatico KuCoin

Generato: 2026-09-03T05:33:04+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-03T05:05:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-03T05:05:32+00:00 | 2026-09-03T05:05:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-03T04:45:00+00:00 | 2026-09-03T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-09-03T04:00:00+00:00 | 2026-09-03T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-09-03T00:00:00+00:00 | 2026-09-03T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Guard Btc Le3 V1 | SUI | 60m | LONG | 5,68 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | SUI | 60m | LONG | 5,68 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | SUI | 60m | LONG | 5,68 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | SUI | 60m | LONG | 5,68 | 4,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | 60m | LONG | 5,30 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | XMR | 240m | LONG | 4,66 | 6,00 | 1,34 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 4,49 | 6,00 | 1,51 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,57 | 6,00 | 4,43 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 1,30 | 6,00 | 4,70 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -1,21 | 6,00 | 4,79 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,09 | 6,00 | 4,91 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 0,51 | 6,00 | 5,49 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -0,41 | 6,00 | 5,59 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | USELESS | 60m | LONG | 6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | USELESS | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 V1 | USELESS | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 No Trend Up V1 | USELESS | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 Range Only V1 | USELESS | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 Cost Aware V1 | USELESS | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Nohigh Cap75 V1 | USELESS | 60m | LONG | 6,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Long Btc 1 3 Cap75 V1 | USELESS | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | USELESS | 60m | LONG | 6,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | USELESS | 60m | LONG | 6,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Cap75 V1 | USELESS | 60m | LONG | 6,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.809,99 | -1,90% | €1,43 | €3.000,00 | 0,05% | 6 | 57 | 40,35% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 57 | 2785 | PRIME INDICAZIONI | 100 (mancano 43) |

- Trade del Principale 4H chiusi: **57**; win rate **40,35%**; profit factor **0,87**.
- Expectancy: **€-3,28** per trade; P&L netto: **€-187,09**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.809,99 | €699,62 | €2.098,86 | €196,19 | €-1,79 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.288,54 | €2.562,45 | €5.124,89 | €225,59 | €37,31 |
| TEST | Main Side Regime Guard V1 | 7 | €11.147,42 | €698,16 | €2.094,48 | €228,36 | €113,50 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.022,76 | €2.502,12 | €5.004,23 | €220,28 | €36,43 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €10.886,41 | €1.225,09 | €3.675,26 | €163,41 | €12,89 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.852,42 | €1.144,19 | €2.288,39 | €215,72 | €1,21 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.573,35 | €1.324,46 | €3.973,37 | €209,22 | €2,40 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.536,17 | €1.506,37 | €3.012,74 | €158,25 | €37,58 |
| TEST | Combo Adaptive Long Only V1 | 6 | €10.455,65 | €2.313,66 | €4.627,31 | €207,30 | €1,65 |
| TEST | Rapida 1H V2 | 1 | €10.402,25 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.356,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 3 | €10.316,49 | €2.599,85 | €7.799,56 | €154,34 | €15,57 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 6 | €10.303,28 | €800,56 | €2.401,68 | €154,67 | €2,92 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.298,64 | €1.071,19 | €2.142,37 | €207,40 | €18,56 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.246,90 | €1.220,23 | €3.660,70 | €204,95 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.196,22 | €1.791,15 | €3.582,29 | €203,91 | €0,96 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.190,26 | €1.790,10 | €3.580,20 | €203,79 | €0,96 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 7 | €10.184,25 | €1.166,73 | €2.333,45 | €152,31 | €18,76 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.181,06 | €1.212,39 | €3.637,18 | €203,63 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.154,56 | €1.075,74 | €2.151,48 | €201,58 | €1,37 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.144,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 5 | €10.115,46 | €1.424,05 | €4.272,14 | €102,78 | €54,92 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.092,54 | €2.259,58 | €4.519,16 | €201,80 | €2,49 |
| TEST | Sol Ema 1H | 0 | €10.088,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.080,97 | €775,58 | €1.551,16 | €0,00 | €50,23 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 7 | €10.071,29 | €748,72 | €2.246,17 | €151,05 | €55,28 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.066,48 | €280,67 | €842,00 | €101,04 | €9,06 |
| TEST | Scanner Top15 Long | 7 | €10.061,35 | €1.836,79 | €3.673,58 | €200,88 | €41,90 |
| TEST | Scanner Top20 Long | 7 | €10.061,35 | €1.836,79 | €3.673,58 | €200,88 | €41,90 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.057,11 | €1.943,42 | €3.886,84 | €151,25 | €1,60 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.032,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.025,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.002,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.987,77 | €478,97 | €957,94 | €0,00 | €58,24 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €9.982,43 | €1.402,19 | €4.206,57 | €152,18 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.968,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 5 | €9.968,62 | €720,81 | €2.162,44 | €149,09 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €9.891,19 | €1.075,88 | €2.151,76 | €197,47 | €41,72 |
| TEST | Eth Ema 4H | 0 | €9.887,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.861,62 | €1.222,99 | €3.668,98 | €197,23 | €0,34 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €9.860,07 | €1.855,44 | €3.710,88 | €98,68 | €-0,33 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.856,25 | €1.100,92 | €3.302,75 | €147,83 | €54,34 |
| TEST | Forza relativa 1H V2 | 6 | €9.839,02 | €858,58 | €1.717,15 | €99,61 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.819,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.789,19 | €1.134,67 | €3.404,01 | €49,02 | €-12,45 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.748,76 | €1.129,98 | €3.389,95 | €48,82 | €-12,40 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.716,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.706,27 | €1.115,27 | €3.345,80 | €145,47 | €-7,18 |
| TEST | Global Confluence puro 1H | 0 | €9.700,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.693,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.653,19 | €1.124,13 | €3.372,38 | €193,06 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 4 | €9.636,33 | €1.392,27 | €4.176,80 | €192,46 | €14,46 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 6 | €9.549,87 | €1.073,86 | €2.147,72 | €190,45 | €41,17 |
| TEST | Btc Ema 1H | 1 | €9.548,22 | €1.107,32 | €3.321,96 | €47,84 | €-18,02 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 4 | €9.539,77 | €2.328,48 | €6.985,45 | €190,85 | €13,56 |
| TEST | Master Adaptive Gb20 Partial V1 | 6 | €9.539,72 | €1.072,72 | €2.145,43 | €190,25 | €41,12 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €9.531,47 | €837,93 | €1.675,86 | €190,63 | €39,91 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.519,40 | €1.008,45 | €2.016,90 | €188,97 | €1,29 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Master Adaptive V1 | 6 | €9.502,82 | €1.068,57 | €2.137,14 | €189,51 | €40,96 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.498,44 | €2.870,74 | €8.612,21 | €190,99 | €-34,03 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.464,73 | €1.087,52 | €3.262,55 | €141,85 | €-7,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €9.439,88 | €1.366,31 | €4.098,93 | €188,54 | €14,23 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.412,84 | €734,78 | €2.204,35 | €188,27 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.377,39 | €1.054,33 | €2.108,66 | €187,01 | €40,41 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.369,37 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.309,80 | €818,44 | €1.636,88 | €186,20 | €38,98 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.276,56 | €1.052,64 | €2.105,27 | €185,02 | €93,72 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €9.193,50 | €2.081,11 | €6.243,32 | €137,09 | €13,88 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 6 | €9.162,63 | €1.243,77 | €2.487,54 | €183,21 | €2,32 |
| TEST | Bilanciata 1H V2 | 6 | €9.143,12 | €1.237,03 | €3.711,09 | €136,08 | €48,48 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €9.140,49 | €836,80 | €1.673,60 | €182,81 | €38,27 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.130,59 | €1.399,67 | €2.799,33 | €138,93 | €-2,75 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.128,34 | €1.573,33 | €3.146,67 | €137,20 | €-0,22 |
| TEST | Bilanciata 1H V1 | 7 | €9.047,06 | €1.190,68 | €3.572,04 | €90,96 | €25,27 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €8.983,79 | €2.715,19 | €8.145,56 | €180,65 | €-32,18 |
| TEST | Combo Trend | 6 | €8.950,60 | €1.835,95 | €3.671,89 | €87,11 | €13,98 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €8.949,06 | €2.025,77 | €6.077,32 | €133,44 | €13,51 |
| TEST | Combo Adaptive Mfe Trail | 8 | €8.942,66 | €1.001,12 | €2.002,24 | €144,29 | €16,37 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €8.912,04 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.884,86 | €2.009,38 | €6.028,14 | €132,46 | €13,41 |
| TEST | Combo Adaptive Runner25 V1 | 5 | €8.855,19 | €996,69 | €1.993,38 | €132,88 | €17,34 |
| TEST | Master Adaptive Strict3 V1 | 5 | €8.782,76 | €842,44 | €1.684,88 | €175,14 | €38,54 |
| TEST | Combo Mean Reversion | 1 | €8.757,80 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €8.748,02 | €2.247,68 | €4.495,36 | €87,47 | €5,73 |
| TEST | Combo Adaptive Tp3 V1 | 5 | €8.689,53 | €978,05 | €1.956,10 | €130,40 | €17,02 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €8.686,45 | €751,35 | €1.502,69 | €129,01 | €38,39 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €8.649,83 | €1.615,15 | €3.230,30 | €171,86 | €37,24 |
| TEST | Forza relativa 1H V1 | 5 | €8.309,28 | €1.577,75 | €3.155,50 | €42,40 | €51,48 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.809,99 | €-187,09 | 57 | 57 | 40,35% | 0,87 | €-3,28 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.288,54 | €1.253,91 | 124 | 124 | 45,16% | 1,46 | €10,11 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.147,42 | €1.035,68 | 45 | 45 | 55,56% | 2,35 | €23,02 | 3,82% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.022,76 | €988,95 | 92 | 92 | 43,48% | 1,54 | €10,75 | 6,75% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.886,41 | €875,85 | 178 | 178 | 49,44% | 1,23 | €4,92 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.852,42 | €852,70 | 159 | 159 | 46,54% | 1,28 | €5,36 | 8,85% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.573,35 | €573,16 | 261 | 261 | 44,06% | 1,13 | €2,20 | 7,89% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.536,17 | €500,56 | 140 | 140 | 50,00% | 1,17 | €3,58 | 10,10% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.455,65 | €456,86 | 142 | 142 | 46,48% | 1,16 | €3,22 | 7,78% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.402,25 | €403,40 | 62 | 55 | 48,39% | 1,27 | €6,51 | 3,89% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.356,28 | €356,28 | 17 | 17 | 64,71% | 2,44 | €20,96 | 2,77% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.316,49 | €305,41 | 90 | 90 | 48,89% | 1,16 | €3,39 | 4,50% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.303,28 | €302,02 | 97 | 97 | 46,39% | 1,16 | €3,11 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Ampia 4H | Confluenza trend | €10.298,64 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.246,90 | €249,29 | 208 | 208 | 49,04% | 1,07 | €1,20 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.196,22 | €197,49 | 125 | 125 | 40,80% | 1,07 | €1,58 | 11,78% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.190,26 | €191,52 | 129 | 129 | 41,09% | 1,07 | €1,48 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Adaptive | Combo Adaptive | €10.184,25 | €167,06 | 187 | 187 | 44,39% | 1,05 | €0,89 | 8,17% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.181,06 | €183,45 | 252 | 252 | 44,05% | 1,04 | €0,73 | 9,48% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.154,56 | €154,58 | 142 | 142 | 43,66% | 1,05 | €1,09 | 11,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.144,72 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,24% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.115,46 | €63,04 | 68 | 68 | 44,12% | 1,04 | €0,93 | 4,92% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.092,54 | €92,84 | 156 | 156 | 46,79% | 1,03 | €0,60 | 10,31% |
| TEST | Sol Ema 1H | Trend following EMA | €10.088,56 | €88,56 | 20 | 20 | 45,00% | 1,16 | €4,43 | 3,33% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.080,97 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.071,29 | €17,38 | 199 | 199 | 42,21% | 1,00 | €0,09 | 10,60% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.066,48 | €58,16 | 15 | 15 | 33,33% | 1,13 | €3,88 | 3,39% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.061,35 | €21,79 | 159 | 159 | 45,91% | 1,01 | €0,14 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.061,35 | €21,79 | 159 | 159 | 45,91% | 1,01 | €0,14 | 10,31% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.057,11 | €57,82 | 168 | 168 | 44,64% | 1,02 | €0,34 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.032,57 | €32,57 | 13 | 13 | 61,54% | 1,11 | €2,51 | 1,89% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,86 | €25,86 | 15 | 15 | 60,00% | 1,07 | €1,72 | 3,08% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Doge Ema 1H | Trend following EMA | €10.002,70 | €2,70 | 23 | 23 | 60,87% | 1,01 | €0,12 | 2,77% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.987,77 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €9.982,43 | €-15,15 | 49 | 49 | 40,82% | 0,99 | €-0,31 | 4,94% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.968,76 | €-31,24 | 22 | 22 | 45,45% | 0,95 | €-1,42 | 4,59% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.968,62 | €-30,00 | 247 | 247 | 38,87% | 0,99 | €-0,12 | 6,56% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | Combo Scanner | Combo Scanner | €9.891,19 | €-149,11 | 157 | 157 | 43,31% | 0,96 | €-0,95 | 11,38% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,30 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.861,62 | €-136,78 | 155 | 155 | 43,23% | 0,95 | €-0,88 | 7,10% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.860,07 | €-137,14 | 141 | 141 | 44,68% | 0,95 | €-0,97 | 11,06% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.856,25 | €-196,08 | 200 | 200 | 41,50% | 0,95 | €-0,98 | 12,52% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.839,02 | €-159,67 | 133 | 126 | 40,60% | 0,95 | €-1,20 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.819,99 | €-180,01 | 16 | 16 | 43,75% | 0,68 | €-11,25 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.789,19 | €-196,45 | 17 | 17 | 41,18% | 0,65 | €-11,56 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Ema 1H | Trend following EMA | €9.748,76 | €-236,94 | 24 | 24 | 41,67% | 0,70 | €-9,87 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.716,18 | €-283,82 | 9 | 9 | 33,33% | 0,35 | €-31,54 | 4,16% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.706,27 | €-284,54 | 187 | 187 | 39,04% | 0,93 | €-1,52 | 10,20% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.700,24 | €-299,76 | 20 | 20 | 35,00% | 0,50 | €-14,99 | 3,93% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.693,16 | €-306,84 | 17 | 17 | 29,41% | 0,54 | €-18,05 | 3,74% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.653,19 | €-344,72 | 115 | 115 | 44,35% | 0,84 | €-3,00 | 9,26% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.636,33 | €-375,53 | 118 | 118 | 41,53% | 0,88 | €-3,18 | 6,64% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.549,87 | €-491,14 | 86 | 86 | 30,23% | 0,80 | €-5,71 | 8,39% |
| TEST | Btc Ema 1H | Trend following EMA | €9.548,22 | €-432,76 | 18 | 18 | 22,22% | 0,38 | €-24,04 | 4,62% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.539,77 | €-469,60 | 102 | 102 | 38,24% | 0,81 | €-4,60 | 7,99% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.539,72 | €-501,25 | 81 | 81 | 33,33% | 0,79 | €-6,19 | 7,98% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.531,47 | €-507,91 | 128 | 128 | 37,50% | 0,84 | €-3,97 | 7,34% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.519,40 | €-480,58 | 134 | 134 | 42,54% | 0,82 | €-3,59 | 12,28% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.502,82 | €-538,00 | 83 | 83 | 32,53% | 0,79 | €-6,48 | 7,80% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.498,44 | €-463,38 | 177 | 177 | 40,11% | 0,88 | €-2,62 | 11,10% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.464,73 | €-526,31 | 151 | 151 | 37,09% | 0,82 | €-3,49 | 10,20% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.439,88 | €-571,80 | 121 | 121 | 43,80% | 0,84 | €-4,73 | 8,44% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.412,84 | €-585,64 | 220 | 220 | 41,82% | 0,87 | €-2,66 | 10,92% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.377,39 | €-662,88 | 117 | 117 | 44,44% | 0,76 | €-5,67 | 9,02% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,37 | €-629,96 | 83 | 83 | 33,73% | 0,73 | €-7,59 | 7,96% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.309,80 | €-728,67 | 145 | 145 | 38,62% | 0,79 | €-5,03 | 8,78% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.276,56 | €-817,04 | 71 | 71 | 29,58% | 0,66 | €-11,51 | 8,44% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.193,50 | €-816,84 | 151 | 151 | 39,07% | 0,81 | €-5,41 | 15,64% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.162,63 | €-839,68 | 74 | 74 | 22,97% | 0,64 | €-11,35 | 11,41% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.143,12 | €-902,32 | 135 | 122 | 40,74% | 0,70 | €-6,68 | 11,82% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.140,49 | €-897,24 | 90 | 90 | 35,56% | 0,67 | €-9,97 | 11,79% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.130,59 | €-864,91 | 89 | 89 | 31,46% | 0,70 | €-9,72 | 10,13% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.128,34 | €-869,58 | 142 | 142 | 37,32% | 0,68 | €-6,12 | 12,31% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.047,06 | €-976,50 | 134 | 134 | 35,07% | 0,67 | €-7,29 | 15,68% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €8.983,79 | €-980,11 | 131 | 131 | 39,69% | 0,64 | €-7,48 | 10,85% |
| TEST | Combo Trend | Combo Trend | €8.950,60 | €-1.060,91 | 181 | 181 | 37,57% | 0,75 | €-5,86 | 12,55% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €8.949,06 | €-1.060,99 | 109 | 109 | 39,45% | 0,69 | €-9,73 | 15,94% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.942,66 | €-1.072,53 | 198 | 198 | 40,40% | 0,72 | €-5,42 | 15,45% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.912,04 | €-1.086,89 | 42 | 42 | 19,05% | 0,27 | €-25,88 | 12,22% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.884,86 | €-1.125,12 | 154 | 154 | 35,06% | 0,72 | €-7,31 | 17,41% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.855,19 | €-1.160,89 | 108 | 108 | 31,48% | 0,53 | €-10,75 | 14,10% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.782,76 | €-1.254,75 | 73 | 73 | 26,03% | 0,58 | €-17,19 | 13,60% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.757,80 | €-1.240,91 | 55 | 55 | 34,55% | 0,45 | €-22,56 | 14,81% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.748,02 | €-1.255,01 | 91 | 91 | 40,66% | 0,58 | €-13,79 | 15,18% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.689,53 | €-1.326,25 | 88 | 88 | 29,55% | 0,39 | €-15,07 | 14,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.686,45 | €-1.351,43 | 111 | 111 | 33,33% | 0,58 | €-12,18 | 13,91% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.649,83 | €-1.385,38 | 86 | 86 | 30,23% | 0,47 | €-16,11 | 16,19% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.309,28 | €-1.740,74 | 116 | 116 | 26,72% | 0,46 | €-15,01 | 19,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,36776 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-1,63 |
| Principale 4H | XMR | LONG | Confluenza trend | 240m | 3,0x | 512,59737 | 509,63000 | 474,66794 | 344,29457 | 588,45625 | €9,14 | €27,43 | €2,03 | €-0,16 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €634,36 | €1.903,09 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,10991 | 0,10991 | 0,10273 | 0,07382 | 0,12428 | €230,61 | €691,82 | €45,23 | €0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 77204,03610 | 77722,30000 | 78315,77422 | 102552,69462 | 74980,55986 | €8,80 | €26,39 | €0,38 | €-0,18 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 2383,24326 | 2405,92000 | 2417,56196 | 3165,74146 | 2314,60585 | €19,16 | €57,49 | €0,83 | €-0,55 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 81,38172 | 82,46100 | 82,88669 | 108,10205 | 78,37177 | €13,39 | €40,16 | €0,74 | €-0,53 |
| Bilanciata 1H V1 | USELESS | LONG | Confluenza trend | 60m | 3,0x | 0,12778 | 0,13490 | 0,11602 | 0,08582 | 0,15129 | €158,58 | €475,74 | €43,78 | €26,53 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,11110 | 0,11110 | 0,10386 | 0,07462 | 0,12560 | €15,59 | €46,76 | €3,05 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,49 | €28,46 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | USELESS | LONG | Confluenza trend V2 | 60m | 3,0x | 0,12397 | 0,13490 | 0,11113 | 0,08327 | 0,14966 | €147,75 | €443,24 | €45,92 | €39,06 |
| Bilanciata 1H V2 | ETH | SHORT | Confluenza trend V2 | 60m | 3,0x | 2383,24326 | 2405,92000 | 2417,56196 | 3165,74146 | 2314,60585 | €25,73 | €77,19 | €1,11 | €-0,73 |
| Bilanciata 1H V2 | SUI | LONG | Confluenza trend V2 | 60m | 3,0x | 0,76715 | 0,77230 | 0,74527 | 0,51527 | 0,81093 | €504,73 | €1.514,19 | €43,20 | €10,16 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77722,30000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.088,71 | €3.266,12 | €47,03 | €-34,03 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €761,73 | €2.285,18 | €46,62 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €300,38 | €901,14 | €46,37 | €0,00 |
| 1H Fast Score 6 75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €964,38 | €2.893,15 | €44,81 | €-0,00 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €689,59 | €2.068,77 | €45,90 | €13,88 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €292,39 | €877,18 | €45,14 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €938,74 | €2.816,22 | €43,62 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €671,26 | €2.013,77 | €44,68 | €13,51 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €326,57 | €979,72 | €50,41 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,79 | €29,37 | €0,47 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €640,26 | €1.920,77 | €42,62 | €12,89 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,77495 | 0,77230 | 0,75825 | 0,52051 | 0,80001 | €698,80 | €2.096,39 | €45,19 | €-7,18 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €715,82 | €2.147,45 | €47,65 | €14,41 |
| 1H Fast Long Btc 1 3 Cap75 V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,13493 | 0,13490 | 0,12604 | 0,09063 | 0,14826 | €241,51 | €724,54 | €47,72 | €-0,14 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,47749 | 82,46100 | 81,36622 | 55,39738 | 84,14441 | €1.165,48 | €3.496,44 | €47,11 | €-0,70 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,12397 | 0,13490 | 0,12447 | 0,08327 | 0,13896 | €9,08 | €27,24 | €0,00 | €2,40 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,12109 | €278,24 | €834,72 | €42,44 | €0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €293,41 | €880,24 | €44,76 | €0,00 |
| 1H Fast V3 Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €290,81 | €872,44 | €44,89 | €0,00 |
| 1H Fast V3 Cap75 V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €929,63 | €2.788,90 | €43,20 | €-0,00 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €666,44 | €1.999,32 | €44,36 | €13,41 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €26,13 | €78,40 | €3,99 | €0,00 |
| 1H Fast V3 Nohigh V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €16,73 | €50,18 | €1,11 | €0,34 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12397 | 0,13490 | 0,12447 | 0,08327 | 0,13896 | €202,71 | €608,13 | €0,00 | €53,59 |
| 1H Fast V3 Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €37,05 | €111,16 | €2,47 | €0,75 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €310,83 | €932,49 | €47,98 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €718,60 | €2.155,79 | €47,84 | €14,46 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €274,69 | €824,06 | €41,90 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12397 | 0,13490 | 0,12447 | 0,08327 | 0,13896 | €207,16 | €621,48 | €0,00 | €54,77 |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €25,66 | €76,98 | €1,71 | €0,52 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €295,31 | €885,93 | €45,05 | €0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.086,99 | €3.260,97 | €51,74 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €773,82 | €2.321,47 | €51,51 | €15,57 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €304,49 | €913,46 | €47,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76715 | 0,77230 | 0,75013 | 0,51527 | 0,79269 | €707,20 | €2.121,61 | €47,08 | €14,23 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2405,92000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,37 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 82,46100 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,10 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08292 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €18,63 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 100,76000 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,79 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €869,59 | €1.739,17 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,10812 | 0,10812 | 0,10113 | 0,05460 | 0,12350 | €321,13 | €642,27 | €41,51 | €0,00 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | USELESS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,11927 | 0,13490 | 0,12195 | 0,06023 | 0,14696 | €196,49 | €392,98 | €0,00 | €51,48 |
| Forza relativa 1H V1 | SUI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,77245 | 0,77230 | 0,75068 | 0,39009 | 0,82035 | €15,83 | €31,65 | €0,89 | €-0,01 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €30,16 | €60,33 | €1,25 | €-0,00 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 100,76000 | 101,87931 | 149,16070 | 94,50736 | €1.329,55 | €2.659,09 | €56,14 | €-26,30 |
| Benchmark Donchian breakout 1H | USELESS | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,11927 | 0,13490 | 0,10529 | 0,06023 | 0,15422 | €234,07 | €468,14 | €54,87 | €61,33 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,75415 | 0,77230 | 0,73242 | 0,38085 | 0,80848 | €47,47 | €94,95 | €2,74 | €2,28 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 100,76000 | 101,87931 | 149,16070 | 94,50736 | €1.298,24 | €2.596,49 | €54,81 | €-25,68 |
| Donchian 1H Gb20 120R V1 | USELESS | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,11927 | 0,13490 | 0,10529 | 0,06023 | 0,15422 | €228,56 | €457,12 | €53,58 | €59,89 |
| Donchian 1H Gb20 120R V1 | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,75415 | 0,77230 | 0,73242 | 0,38085 | 0,80848 | €46,36 | €92,71 | €2,67 | €2,23 |
| Benchmark Bollinger mean reversion 1H | PEPE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.301,20 | €2.602,41 | €43,75 | €0,00 |
| Benchmark Bollinger mean reversion 1H | SUI | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,77465 | 0,77230 | 0,79254 | 1,15809 | 0,74781 | €946,48 | €1.892,95 | €43,72 | €5,73 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €991,95 | €1.983,90 | €44,97 | €-0,00 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 77061,73457 | 77722,30000 | 78294,72232 | 115207,29318 | 74349,16151 | €12,66 | €25,31 | €0,40 | €-0,22 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €415,84 | €831,69 | €52,53 | €0,00 |
| Scanner Top 5 Long 1H | SUI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,75415 | 0,77230 | 0,76064 | 0,38085 | 0,79327 | €25,24 | €50,48 | €0,00 | €1,21 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €386,28 | €772,56 | €48,79 | €0,00 |
| Scanner Top10 Long | USELESS | LONG | Scanner Top10 Long | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,14966 | €14,13 | €28,25 | €2,93 | €2,49 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,14966 | €241,90 | €483,80 | €50,12 | €42,64 |
| Scanner Top15 Long | SUI | LONG | Scanner Top15 Long | 60m | 2,0x | 0,77495 | 0,77230 | 0,75348 | 0,39135 | 0,81791 | €107,30 | €214,60 | €5,95 | €-0,74 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,14966 | €241,90 | €483,80 | €50,12 | €42,64 |
| Scanner Top20 Long | SUI | LONG | Scanner Top20 Long | 60m | 2,0x | 0,77495 | 0,77230 | 0,75348 | 0,39135 | 0,81791 | €107,30 | €214,60 | €5,95 | €-0,74 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €389,11 | €778,23 | €49,15 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,75415 | 0,77230 | 0,76064 | 0,38085 | 0,79718 | €28,56 | €57,13 | €0,00 | €1,37 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €364,77 | €729,55 | €46,07 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,75415 | 0,77230 | 0,76064 | 0,38085 | 0,79718 | €26,78 | €53,55 | €0,00 | €1,29 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,15223 | €226,48 | €452,96 | €46,92 | €39,92 |
| Scanner Top5 Btc Guard V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,77245 | 0,77230 | 0,75068 | 0,39009 | 0,82035 | €14,06 | €28,12 | €0,79 | €-0,01 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €331,20 | €662,40 | €41,83 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,15223 | €207,86 | €415,72 | €43,06 | €36,63 |
| Scanner Top5 Btc Btc Le3 V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,75415 | 0,77230 | 0,76064 | 0,38085 | 0,79718 | €12,55 | €25,10 | €0,00 | €0,60 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,15223 | €221,21 | €442,43 | €45,83 | €38,99 |
| Scanner Top5 Btc Guard Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,77245 | 0,77230 | 0,75068 | 0,39009 | 0,82035 | €13,73 | €27,46 | €0,77 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,15223 | €217,19 | €434,38 | €45,00 | €38,28 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,77245 | 0,77230 | 0,75068 | 0,39009 | 0,82035 | €13,48 | €26,96 | €0,76 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €325,70 | €651,40 | €41,14 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,15223 | €209,39 | €418,78 | €43,38 | €36,90 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,75415 | 0,77230 | 0,76064 | 0,38085 | 0,79718 | €30,88 | €61,77 | €0,00 | €1,49 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,51 | €781,02 | €50,94 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,16540 | €13,61 | €27,22 | €2,44 | €0,96 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,74 | €781,47 | €50,97 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,16540 | €13,62 | €27,23 | €2,45 | €0,96 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €15,51 | €31,02 | €0,71 | €-0,00 |
| Combo Trend | ETH | SHORT | Combo Trend | 60m | 2,0x | 2383,24326 | 2405,92000 | 2421,37515 | 3562,94867 | 2299,35309 | €28,00 | €56,00 | €0,90 | €-0,53 |
| Combo Trend | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,13029 | 0,13490 | 0,11728 | 0,06579 | 0,15890 | €204,87 | €409,73 | €40,90 | €14,51 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12705 | €377,46 | €754,92 | €49,24 | €0,00 |
| Combo Scanner | USELESS | LONG | Combo Scanner | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,15223 | €237,74 | €475,47 | €49,25 | €41,90 |
| Combo Scanner | SUI | LONG | Combo Scanner | 60m | 2,0x | 0,77495 | 0,77230 | 0,75348 | 0,39135 | 0,82220 | €26,73 | €53,47 | €1,48 | €-0,18 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €32,33 | €64,67 | €1,38 | €-0,00 |
| Combo Adaptive | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,15369 | €264,88 | €529,75 | €47,59 | €18,76 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €17,73 | €35,47 | €0,71 | €-0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ETH | SHORT | Combo Adaptive | 60m | 2,0x | 2383,24326 | 2405,92000 | 2417,56196 | 3562,94867 | 2314,60585 | €21,91 | €43,81 | €0,63 | €-0,42 |
| Combo Adaptive Mfe Trail | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,15369 | €237,04 | €474,07 | €42,59 | €16,79 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12560 | €400,65 | €801,31 | €52,27 | €0,00 |
| Combo Adaptive Long Only V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,75415 | 0,77230 | 0,76176 | 0,38085 | 0,79327 | €34,33 | €68,66 | €0,00 | €1,65 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,15369 | €22,57 | €45,14 | €4,06 | €1,60 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €350,40 | €700,80 | €44,26 | €0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,42 | €28,84 | €0,64 | €-0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,16540 | €244,85 | €489,70 | €43,99 | €17,34 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €343,85 | €687,70 | €43,43 | €0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,15 | €28,30 | €0,63 | €-0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,13029 | 0,13490 | 0,11858 | 0,06579 | 0,16540 | €240,27 | €480,55 | €43,17 | €17,02 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77303,06629 | 77722,30000 | 78416,23045 | 102684,23973 | 75076,73798 | €1.107,32 | €3.321,96 | €47,84 | €-18,02 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 77722,30000 | 78321,88645 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €50,23 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 100,76000 | 101,43990 | 160,38740 | 97,27311 | €478,97 | €957,94 | €0,00 | €58,24 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 2397,15047 | 2405,92000 | 2431,66944 | 3184,21488 | 2328,11254 | €1.129,98 | €3.389,95 | €48,82 | €-12,40 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 2397,15047 | 2405,92000 | 2431,66944 | 3184,21488 | 2328,11254 | €1.134,67 | €3.404,01 | €49,02 | €-12,45 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €364,80 | €729,60 | €46,08 | €0,00 |
| Master Adaptive V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12401 | 0,13490 | 0,11112 | 0,06263 | 0,14981 | €227,47 | €454,94 | €47,31 | €39,93 |
| Master Adaptive V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,77230 | 0,73459 | 0,38085 | 0,79327 | €21,43 | €42,87 | €1,11 | €1,03 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,36 | €718,72 | €45,39 | €0,00 |
| Master Adaptive No Alt V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12159 | 0,13490 | 0,10862 | 0,06141 | 0,14755 | €13,24 | €26,48 | €2,83 | €2,90 |
| Master Adaptive No Alt V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,77495 | 0,77230 | 0,75348 | 0,39135 | 0,81791 | €824,16 | €1.648,32 | €45,68 | €-5,65 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12397 | 0,13490 | 0,11113 | 0,06261 | 0,14966 | €211,03 | €422,07 | €43,72 | €37,19 |
| Master Adaptive Strict3 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,77230 | 0,73459 | 0,38085 | 0,79327 | €27,92 | €55,84 | €1,45 | €1,34 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,99 | €719,98 | €45,47 | €0,00 |
| Master Adaptive Gb20 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12401 | 0,13490 | 0,11112 | 0,06263 | 0,14981 | €224,47 | €448,93 | €46,69 | €39,40 |
| Master Adaptive Gb20 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,77230 | 0,73459 | 0,38085 | 0,79327 | €20,98 | €41,95 | €1,09 | €1,01 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €360,46 | €720,91 | €45,53 | €0,00 |
| Master Adaptive Runner25 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10787 | 0,13490 | 0,09691 | 0,05448 | 0,14077 | €184,51 | €369,02 | €37,52 | €92,46 |
| Master Adaptive Runner25 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,77230 | 0,73459 | 0,38085 | 0,81282 | €26,15 | €52,29 | €1,36 | €1,26 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €1.156,08 | €2.312,16 | €46,42 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ETH | SHORT | Combo Adaptive | 60m | 2,0x | 2383,24326 | 2405,92000 | 2417,56196 | 3562,94867 | 2314,60585 | €17,26 | €34,53 | €0,50 | €-0,33 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,61 | €733,22 | €46,31 | €0,00 |
| Master Adaptive Gb20 Be V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12401 | 0,13490 | 0,11112 | 0,06263 | 0,14981 | €228,59 | €457,19 | €47,55 | €40,13 |
| Master Adaptive Gb20 Be V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,77230 | 0,73459 | 0,38085 | 0,79327 | €21,54 | €43,08 | €1,12 | €1,04 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,22 | €732,44 | €46,26 | €0,00 |
| Master Adaptive Gb20 Partial V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12401 | 0,13490 | 0,11112 | 0,06263 | 0,14981 | €228,35 | €456,70 | €47,49 | €40,09 |
| Master Adaptive Gb20 Partial V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,77230 | 0,73459 | 0,38085 | 0,79327 | €21,52 | €43,03 | €1,12 | €1,04 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10448 | 0,05539 | 0,12353 | €480,15 | €960,31 | €45,49 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,12397 | 0,13490 | 0,11434 | 0,06261 | 0,14966 | €13,17 | €26,34 | €2,05 | €2,32 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €330,06 | €990,17 | €50,95 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12397 | 0,13490 | 0,12447 | 0,08327 | 0,13896 | €208,12 | €624,37 | €0,00 | €55,02 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,77495 | 0,77230 | 0,75825 | 0,52051 | 0,80001 | €9,74 | €29,23 | €0,63 | €-0,10 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €333,52 | €1.000,56 | €50,87 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12226 | 0,13490 | 0,12416 | 0,08212 | 0,13753 | €9,42 | €28,25 | €0,00 | €2,92 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01303 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €120,66 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2405,92000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,39 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,86517 | 5,74300 | 5,34904 | 3,93944 | 6,89744 | €216,26 | €648,78 | €57,09 | €-13,51 |
| Main Side Regime Guard V1 | USELESS | LONG | Confluenza trend | 240m | 3,0x | 0,12159 | 0,13490 | 0,10700 | 0,08167 | 0,15078 | €20,54 | €61,63 | €7,40 | €6,74 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | USELESS | LONG | Confluenza trend | 240m | 3,0x | 0,13205 | 0,13490 | 0,11620 | 0,08869 | 0,16374 | €139,69 | €419,07 | €50,29 | €9,06 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,12226 | 0,13490 | 0,10772 | 0,06174 | 0,15425 | €209,76 | €419,53 | €49,89 | €43,36 |
| Combo Trend Side Regime Guard V1 | SUI | LONG | Combo Trend | 60m | 2,0x | 0,77495 | 0,77230 | 0,75109 | 0,39135 | 0,82745 | €843,75 | €1.687,49 | €51,96 | €-5,78 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,77495 | 0,77230 | 0,75825 | 0,52051 | 0,80001 | €681,41 | €2.044,22 | €44,06 | €-7,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77722,30000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.029,72 | €3.089,16 | €44,48 | €-32,18 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €720,45 | €2.161,36 | €44,09 | €-0,00 |
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
| Sol Ema 1H | SOL | SHORT | 2026-09-03T02:45:00+00:00 | 100,76510 | €-54,74 | -1,08 | STOP |
| Sol Adaptive 1H | SOL | SHORT | 2026-09-03T02:45:00+00:00 | 100,76510 | €-54,09 | -1,08 | STOP |
| Forza relativa 1H V1 | SOL | SHORT | 2026-09-03T02:45:00+00:00 | 100,76510 | €-1,02 | -1,08 | STOP |
| Global Confluence puro 1H | DOGE | SHORT | 2026-09-03T02:45:00+00:00 | 0,08321 | €-53,01 | -1,09 | STOP |
| Benchmark trend following EMA 1H | DOGE | SHORT | 2026-09-03T02:45:00+00:00 | 0,08301 | €-0,57 | -1,09 | STOP |
| Combo Trend | DOGE | SHORT | 2026-09-03T02:45:00+00:00 | 0,08301 | €-0,52 | -1,09 | STOP |
| Combo Mean Reversion | ZEC | LONG | 2026-09-03T02:45:00+00:00 | 827,14554 | €66,81 | 1,54 | TARGET |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | 2026-09-03T02:45:00+00:00 | 0,01375 | €-49,35 | -1,04 | STOP_STRESS_SLIPPAGE |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | 2026-09-03T02:45:00+00:00 | 0,01375 | €-48,12 | -1,04 | STOP_STRESS_SLIPPAGE |
| 1H Fast Long Btc 1 3 Cap75 V1 | AKE | LONG | 2026-09-03T02:45:00+00:00 | 0,01375 | €-49,68 | -1,04 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V2 | DOGE | SHORT | 2026-09-03T02:45:00+00:00 | 0,08292 | €-50,85 | -1,12 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | 2026-09-03T02:30:00+00:00 | 0,01403 | €-45,28 | -1,04 | STOP_STRESS_SLIPPAGE |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
