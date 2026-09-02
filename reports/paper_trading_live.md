# Paper trading automatico KuCoin

Generato: 2026-09-02T07:16:48+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-02T07:05:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-02T07:05:32+00:00 | 2026-09-02T07:05:32+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-02T06:45:00+00:00 | 2026-09-02T06:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-02T06:00:00+00:00 | 2026-09-02T06:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-02T00:00:00+00:00 | 2026-09-02T00:00:00+00:00 | 3,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend — Side × Regime Guard | UNI | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Range Only | UNI | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Side × Regime Guard | SOL | 60m | SHORT | -5,77 | 5,00 | 0,00 | OPENED | 5,8 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Ema 1H | DOGE | 60m | SHORT | -5,04 | 5,00 | 0,00 | OPENED | 5,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | DOGE | 60m | SHORT | -5,04 | 5,00 | 0,00 | OPENED | 5,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | 60m | SHORT | -5,04 | 5,00 | 0,00 | OPENED | 5,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | DOGE | 240m | SHORT | -5,58 | 6,00 | 0,42 | STALE_CANDLE | 3,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -4,74 | 6,00 | 1,26 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,46 | 6,00 | 1,54 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,33 | 6,00 | 3,67 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTR | 240m | SHORT | -1,06 | 6,00 | 4,94 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 3,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -0,87 | 6,00 | 5,13 | STALE_CANDLE | 3,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,19 | 6,00 | 5,81 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | BTR | 60m | SHORT | -9,00 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | BTR | 60m | SHORT | -9,00 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | BTR | 60m | SHORT | -9,00 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | BTR | 60m | SHORT | -9,00 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered — madre | BTR | 60m | SHORT | -9,00 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — no volatilità HIGH | BTR | 60m | SHORT | -9,00 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — senza ESPORTS | BTR | 60m | SHORT | -9,00 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 senza ESPORTS — MFE Lock | BTR | 60m | SHORT | -9,00 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | BTR | 60m | SHORT | -9,00 | 4,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | BTR | 60m | SHORT | -9,00 | 5,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | BTR | 60m | SHORT | -9,00 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.811,25 | -1,89% | €2,69 | €3.000,00 | 0,09% | 6 | 56 | 41,07% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 56 | 2695 | PRIME INDICAZIONI | 100 (mancano 44) |

- Trade del Principale 4H chiusi: **56**; win rate **41,07%**; profit factor **0,87**.
- Expectancy: **€-3,30** per trade; P&L netto: **€-184,95**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.811,25 | €701,54 | €2.104,63 | €196,25 | €-2,68 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.208,88 | €4.071,45 | €8.142,91 | €225,68 | €-16,87 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.956,62 | €751,96 | €2.255,89 | €218,34 | €-29,12 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €10.944,98 | €3.975,60 | €7.951,19 | €220,37 | €-16,47 |
| TEST | Rapida score 6–7,5 — Cost Aware | 6 | €10.914,13 | €1.083,77 | €3.251,31 | €218,28 | €5,41 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.852,64 | €1.133,45 | €2.266,91 | €217,07 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.777,37 | €2.066,57 | €4.133,15 | €163,28 | €0,87 |
| TEST | Rapida V1 — senza PEPE | 7 | €10.574,82 | €1.337,57 | €4.012,72 | €211,52 | €-1,01 |
| TEST | Combo Adaptive — Long Only | 6 | €10.456,53 | €2.300,74 | €4.601,48 | €209,12 | €0,64 |
| TEST | Rapida 1H V2 | 1 | €10.363,82 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 4 | €10.362,46 | €2.947,67 | €8.843,02 | €206,07 | €-14,52 |
| TEST | Sol Donchian 1H | 1 | €10.320,92 | €1.019,77 | €3.059,30 | €51,67 | €-10,55 |
| TEST | Ampia 4H | 8 | €10.305,90 | €1.071,19 | €2.142,37 | €207,40 | €25,97 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 5 | €10.273,48 | €2.160,68 | €6.482,05 | €205,36 | €-23,09 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 4 | €10.256,57 | €2.089,77 | €6.269,30 | €204,47 | €-22,85 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.246,90 | €1.220,23 | €3.660,70 | €204,95 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 8 | €10.238,55 | €2.132,44 | €4.264,88 | €204,65 | €18,39 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €10.199,69 | €1.803,17 | €3.606,35 | €201,46 | €5,63 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.193,72 | €1.802,12 | €3.604,24 | €201,34 | €5,63 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.181,06 | €1.212,39 | €3.637,18 | €203,63 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.162,09 | €449,62 | €899,24 | €50,98 | €-34,29 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.154,80 | €1.063,56 | €2.127,11 | €203,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.112,51 | €888,04 | €2.664,11 | €50,62 | €-9,18 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 6 | €10.088,02 | €2.278,02 | €4.556,04 | €201,75 | €0,59 |
| TEST | Btc Bollinger 4H | 1 | €10.082,94 | €775,58 | €1.551,16 | €0,00 | €52,58 |
| TEST | Doge Bollinger 1H | 1 | €10.072,73 | €1.204,04 | €3.612,13 | €0,00 | €53,85 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.065,19 | €1.750,21 | €5.250,64 | €201,76 | €-21,90 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.063,95 | €1.942,68 | €3.885,36 | €151,43 | €-0,79 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.053,68 | €1.081,41 | €3.244,23 | €50,29 | €-1,95 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.049,95 | €140,98 | €422,93 | €50,75 | €-7,75 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.025,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 7 | €10.014,30 | €1.025,27 | €3.075,81 | €199,88 | €21,19 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 9 | €9.998,31 | €1.821,70 | €3.643,40 | €199,80 | €15,27 |
| TEST | Scanner Top20 Long | 9 | €9.998,31 | €1.821,70 | €3.643,40 | €199,80 | €15,27 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 6 | €9.996,26 | €1.336,68 | €2.673,35 | €147,94 | €31,91 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.993,58 | €478,97 | €957,94 | €0,00 | €63,98 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.992,42 | €877,49 | €2.632,47 | €50,02 | €-9,08 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.974,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 5 | €9.968,62 | €720,81 | €2.162,44 | €149,09 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.946,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 7 | €9.907,24 | €925,48 | €1.850,95 | €149,79 | €13,40 |
| TEST | Eth Ema 4H | 0 | €9.887,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €9.881,01 | €1.338,71 | €4.016,13 | €198,07 | €-21,54 |
| TEST | Btc Donchian 1H | 1 | €9.880,43 | €1.289,36 | €3.868,07 | €49,51 | €-19,74 |
| TEST | Sol Bollinger 1H | 1 | €9.867,85 | €1.037,93 | €3.113,80 | €49,30 | €9,48 |
| TEST | Rapida V3 — no volatilità HIGH | 6 | €9.861,65 | €1.217,21 | €3.651,63 | €197,24 | €-0,50 |
| TEST | Eth Adaptive 1H | 0 | €9.857,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 7 | €9.851,37 | €1.505,66 | €3.011,32 | €197,02 | €0,21 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 6 | €9.799,72 | €1.367,36 | €4.102,07 | €195,60 | €20,83 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.748,20 | €1.363,98 | €2.727,96 | €48,77 | €-3,64 |
| TEST | Eth Donchian 1H | 0 | €9.747,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.722,03 | €1.098,91 | €3.296,73 | €48,65 | €-6,79 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.653,19 | €1.124,13 | €3.372,38 | €193,06 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.649,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 4 | €9.635,12 | €1.305,40 | €3.916,19 | €193,14 | €-21,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2 | €9.561,10 | €791,57 | €2.374,70 | €95,73 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.552,66 | €1.107,32 | €3.321,96 | €47,84 | €-12,78 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.550,07 | €2.270,08 | €6.810,24 | €191,30 | €-37,58 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 4 | €9.548,64 | €886,36 | €2.659,08 | €190,86 | €0,83 |
| TEST | Combo Adaptive — Trend/Transition | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 6 | €9.519,63 | €997,03 | €1.994,07 | €190,41 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Top 5 + BTC — Guard | 5 | €9.491,50 | €1.103,75 | €2.207,51 | €189,83 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.412,84 | €734,78 | €2.204,35 | €188,27 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 5 | €9.375,37 | €1.356,06 | €2.712,12 | €187,71 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.369,98 | €1.580,60 | €3.161,20 | €187,40 | €-0,06 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 5 | €9.365,40 | €1.354,62 | €2.709,24 | €187,51 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 4 | €9.353,58 | €868,43 | €2.605,28 | €186,96 | €0,81 |
| TEST | Master Adaptive V1 | 5 | €9.329,18 | €1.349,38 | €2.698,76 | €186,79 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.304,40 | €955,13 | €2.865,38 | €140,57 | €10,41 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €9.274,70 | €1.466,40 | €4.399,21 | €138,42 | €26,57 |
| TEST | Top 5 + BTC — Guard + MFE | 5 | €9.270,76 | €1.078,08 | €2.156,17 | €185,42 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.223,03 | €1.288,13 | €2.576,26 | €184,63 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.206,07 | €1.331,51 | €2.663,01 | €184,32 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.189,55 | €1.063,07 | €2.126,13 | €138,86 | €12,53 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.158,33 | €1.384,13 | €2.768,25 | €182,92 | €12,47 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 6 | €9.157,30 | €1.263,51 | €2.527,01 | €183,20 | €0,00 |
| TEST | Combo Trend | 7 | €9.125,87 | €2.130,08 | €4.260,15 | €135,65 | €6,64 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 5 | €9.102,17 | €1.091,72 | €2.183,43 | €182,04 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 8 | €9.096,07 | €1.327,21 | €2.654,42 | €181,53 | €8,79 |
| TEST | Bilanciata V3 · LONG only | 4 | €9.032,62 | €2.147,08 | €6.441,23 | €180,94 | €-35,55 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €9.028,11 | €1.427,41 | €4.282,24 | €134,74 | €25,87 |
| TEST | Bilanciata 1H V1 | 5 | €8.994,49 | €2.069,18 | €6.207,53 | €179,76 | €-12,60 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 8 | €8.976,94 | €1.363,03 | €2.726,05 | €135,13 | €123,98 |
| TEST | Rapida V3 — score <7,5 | 4 | €8.963,58 | €1.417,34 | €4.252,03 | €133,89 | €25,64 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €8.959,01 | €1.370,15 | €2.740,30 | €91,08 | €0,00 |
| TEST | Combo Mean Reversion | 4 | €8.824,91 | €5.439,63 | €10.879,27 | €131,04 | €54,84 |
| TEST | Combo Adaptive — target pieno 3R | 7 | €8.809,17 | €1.339,90 | €2.679,81 | €132,61 | €121,60 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 6 | €8.754,40 | €1.265,20 | €2.530,40 | €174,68 | €29,28 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €8.736,86 | €3.571,47 | €7.142,95 | €87,54 | €36,32 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.704,25 | €1.184,13 | €2.368,27 | €173,50 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €8.612,89 | €1.990,67 | €3.981,33 | €172,29 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €8.404,41 | €1.959,17 | €3.918,34 | €167,95 | €11,39 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.811,25 | €-184,95 | 56 | 56 | 41,07% | 0,87 | €-3,30 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.208,88 | €1.229,80 | 121 | 121 | 45,45% | 1,45 | €10,16 | 6,75% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.956,62 | €987,59 | 42 | 42 | 57,14% | 2,39 | €23,51 | 3,82% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.944,98 | €965,41 | 89 | 89 | 43,82% | 1,53 | €10,85 | 6,75% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.914,13 | €910,79 | 172 | 172 | 50,00% | 1,25 | €5,30 | 6,72% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.852,64 | €854,12 | 158 | 158 | 46,84% | 1,28 | €5,41 | 8,85% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.777,37 | €778,02 | 135 | 135 | 51,85% | 1,30 | €5,76 | 8,10% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.574,82 | €578,07 | 258 | 258 | 44,57% | 1,13 | €2,24 | 7,89% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.456,53 | €458,74 | 141 | 141 | 46,81% | 1,16 | €3,25 | 7,78% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.363,82 | €364,97 | 58 | 52 | 48,28% | 1,27 | €6,29 | 3,89% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.362,46 | €382,18 | 83 | 83 | 50,60% | 1,22 | €4,60 | 4,50% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.320,92 | €333,40 | 16 | 16 | 62,50% | 2,35 | €20,84 | 2,77% |
| TEST | Ampia 4H | Confluenza trend | €10.305,90 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.273,48 | €300,29 | 95 | 95 | 46,32% | 1,16 | €3,16 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.256,57 | €283,09 | 63 | 63 | 47,62% | 1,19 | €4,49 | 4,19% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.246,90 | €249,29 | 208 | 208 | 49,04% | 1,07 | €1,20 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.238,55 | €222,72 | 180 | 180 | 44,44% | 1,07 | €1,24 | 7,91% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.199,69 | €196,31 | 123 | 123 | 40,65% | 1,07 | €1,60 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.193,72 | €190,34 | 127 | 127 | 40,94% | 1,07 | €1,50 | 12,06% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.181,06 | €183,45 | 252 | 252 | 44,05% | 1,04 | €0,73 | 9,48% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.162,09 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,18% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.154,80 | €156,19 | 141 | 141 | 43,97% | 1,05 | €1,11 | 11,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Ema 1H | Trend following EMA | €10.112,51 | €123,38 | 18 | 18 | 44,44% | 1,25 | €6,85 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.088,02 | €90,24 | 153 | 153 | 47,06% | 1,03 | €0,59 | 10,31% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.082,94 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.072,73 | €21,05 | 12 | 12 | 58,33% | 1,07 | €1,75 | 1,89% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.065,19 | €90,14 | 47 | 47 | 42,55% | 1,07 | €1,92 | 4,60% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.063,95 | €67,05 | 166 | 166 | 45,18% | 1,03 | €0,40 | 8,69% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.053,68 | €57,57 | 21 | 21 | 61,90% | 1,13 | €2,74 | 2,77% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.049,95 | €58,16 | 15 | 15 | 33,33% | 1,13 | €3,88 | 3,39% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,86 | €25,86 | 15 | 15 | 60,00% | 1,07 | €1,72 | 3,08% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.014,30 | €-5,05 | 195 | 195 | 42,05% | 1,00 | €-0,03 | 10,60% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.998,31 | €-14,66 | 152 | 152 | 46,71% | 0,99 | €-0,10 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.998,31 | €-14,66 | 152 | 152 | 46,71% | 0,99 | €-0,10 | 10,31% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.996,26 | €-34,09 | 137 | 137 | 45,26% | 0,99 | €-0,25 | 10,02% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.993,58 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.992,42 | €3,16 | 20 | 20 | 45,00% | 1,01 | €0,16 | 4,59% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,27 | €-10,73 | 17 | 17 | 35,29% | 0,33 | €-0,63 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.974,38 | €-25,62 | 17 | 17 | 35,29% | 0,71 | €-1,51 | 0,71% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.968,62 | €-30,00 | 247 | 247 | 38,87% | 0,99 | €-0,12 | 6,56% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.946,36 | €-53,64 | 17 | 17 | 35,29% | 0,33 | €-3,16 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.907,24 | €-105,04 | 130 | 123 | 41,54% | 0,97 | €-0,81 | 10,88% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,30 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.881,01 | €-95,04 | 180 | 180 | 40,00% | 0,97 | €-0,53 | 8,83% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.880,43 | €-97,74 | 11 | 11 | 45,45% | 0,71 | €-8,89 | 1,91% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.867,85 | €-139,86 | 14 | 14 | 42,86% | 0,72 | €-9,99 | 2,91% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.861,65 | €-135,93 | 152 | 152 | 43,42% | 0,95 | €-0,89 | 7,10% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.857,66 | €-142,34 | 16 | 16 | 43,75% | 0,72 | €-8,90 | 3,14% |
| TEST | Combo Scanner | Combo Scanner | €9.851,37 | €-146,92 | 152 | 152 | 44,08% | 0,96 | €-0,97 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.799,72 | €-218,65 | 196 | 196 | 41,33% | 0,95 | €-1,12 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.748,20 | €-246,75 | 19 | 19 | 36,84% | 0,55 | €-12,99 | 3,93% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.747,26 | €-252,74 | 16 | 16 | 31,25% | 0,58 | €-15,80 | 3,74% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Ema 1H | Trend following EMA | €9.722,03 | €-269,38 | 23 | 23 | 39,13% | 0,66 | €-11,71 | 4,80% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.653,19 | €-344,72 | 115 | 115 | 44,35% | 0,84 | €-3,00 | 9,26% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.649,49 | €-350,51 | 8 | 8 | 25,00% | 0,19 | €-43,81 | 4,16% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.635,12 | €-341,52 | 144 | 144 | 38,19% | 0,88 | €-2,37 | 8,83% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.561,10 | €-437,48 | 99 | 99 | 38,38% | 0,82 | €-4,42 | 7,99% |
| TEST | Btc Ema 1H | Trend following EMA | €9.552,66 | €-432,76 | 18 | 18 | 22,22% | 0,38 | €-24,04 | 4,61% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.550,07 | €-408,45 | 176 | 176 | 40,34% | 0,89 | €-2,32 | 10,71% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.548,64 | €-450,49 | 115 | 115 | 40,87% | 0,85 | €-3,92 | 6,64% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.519,63 | €-479,07 | 133 | 133 | 42,86% | 0,82 | €-3,60 | 12,28% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.491,50 | €-507,47 | 126 | 126 | 37,30% | 0,84 | €-4,03 | 7,34% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.412,84 | €-585,64 | 220 | 220 | 41,82% | 0,87 | €-2,66 | 10,92% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.375,37 | €-623,94 | 83 | 83 | 28,92% | 0,74 | €-7,52 | 8,39% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,98 | €-629,27 | 82 | 82 | 34,15% | 0,73 | €-7,67 | 7,96% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.365,40 | €-633,91 | 78 | 78 | 32,05% | 0,73 | €-8,13 | 7,98% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.353,58 | €-645,58 | 118 | 118 | 43,22% | 0,81 | €-5,47 | 8,24% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.329,18 | €-670,13 | 80 | 80 | 31,25% | 0,73 | €-8,38 | 7,80% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.304,40 | €-703,99 | 130 | 118 | 42,31% | 0,75 | €-5,42 | 11,21% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.274,70 | €-749,14 | 143 | 143 | 39,16% | 0,81 | €-5,24 | 14,70% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.270,76 | €-728,23 | 143 | 143 | 38,46% | 0,79 | €-5,09 | 8,78% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.223,03 | €-776,38 | 70 | 70 | 30,00% | 0,67 | €-11,09 | 8,25% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.206,07 | €-793,24 | 114 | 114 | 43,86% | 0,71 | €-6,96 | 9,02% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.189,55 | €-821,73 | 138 | 138 | 37,68% | 0,70 | €-5,95 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.158,33 | €-852,30 | 82 | 82 | 31,71% | 0,68 | €-10,39 | 9,97% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.157,30 | €-842,66 | 72 | 72 | 22,22% | 0,64 | €-11,70 | 11,41% |
| TEST | Combo Trend | Combo Trend | €9.125,87 | €-878,19 | 174 | 174 | 37,93% | 0,78 | €-5,05 | 11,90% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.102,17 | €-896,81 | 88 | 88 | 35,23% | 0,66 | €-10,19 | 11,79% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.096,07 | €-911,13 | 189 | 189 | 40,74% | 0,75 | €-4,82 | 15,45% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.032,62 | €-928,15 | 130 | 130 | 40,00% | 0,66 | €-7,14 | 10,45% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.028,11 | €-995,10 | 101 | 101 | 39,60% | 0,69 | €-9,85 | 15,00% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €8.994,49 | €-989,64 | 128 | 128 | 35,16% | 0,65 | €-7,73 | 15,68% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.976,94 | €-1.145,20 | 99 | 99 | 30,30% | 0,51 | €-11,57 | 14,10% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €8.963,58 | €-1.059,41 | 146 | 146 | 34,93% | 0,72 | €-7,26 | 16,28% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €8.959,01 | €-1.039,15 | 41 | 41 | 19,51% | 0,28 | €-25,35 | 11,76% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.824,91 | €-1.223,12 | 51 | 51 | 33,33% | 0,43 | €-23,98 | 14,46% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.809,17 | €-1.310,62 | 80 | 80 | 28,75% | 0,36 | €-16,38 | 14,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.754,40 | €-1.273,76 | 104 | 104 | 33,65% | 0,59 | €-12,25 | 13,91% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.736,86 | €-1.295,27 | 85 | 85 | 38,82% | 0,55 | €-15,24 | 15,18% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.704,25 | €-1.294,33 | 71 | 71 | 25,35% | 0,56 | €-18,23 | 13,50% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.612,89 | €-1.384,66 | 84 | 84 | 29,76% | 0,46 | €-16,48 | 16,16% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.404,41 | €-1.604,88 | 109 | 109 | 27,52% | 0,48 | €-14,72 | 19,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,34622 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-2,01 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 852,88054 | 835,88000 | 799,15184 | 572,85143 | 960,33794 | €11,06 | €33,19 | €2,09 | €-0,66 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €634,36 | €1.903,09 | €44,20 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,10991 | 0,10991 | 0,10273 | 0,07382 | 0,12428 | €230,61 | €691,82 | €45,23 | €0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 77204,03610 | 77600,50000 | 78315,77422 | 102552,69462 | 74980,55986 | €8,80 | €26,39 | €0,38 | €-0,14 |
| Bilanciata 1H V1 | USELESS | LONG | Confluenza trend | 60m | 3,0x | 0,11591 | 0,11382 | 0,10466 | 0,07786 | 0,13843 | €154,36 | €463,09 | €44,98 | €-8,36 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 2417,02650 | 2420,20000 | 2451,83168 | 3210,61686 | 2347,41613 | €1.041,05 | €3.123,14 | €44,97 | €-4,10 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,11110 | 0,11110 | 0,10386 | 0,07462 | 0,12560 | €15,59 | €46,76 | €3,05 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | XMR | LONG | Confluenza trend V2 | 60m | 3,0x | 520,62410 | 520,62410 | 498,16818 | 349,68586 | 565,53596 | €358,56 | €1.075,68 | €46,40 | €0,00 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,49 | €28,46 | €0,69 | €-0,00 |
| Bilanciata 1H V2 | USELESS | LONG | Confluenza trend V2 | 60m | 3,0x | 0,11116 | 0,11382 | 0,09999 | 0,07466 | 0,13351 | €152,70 | €458,10 | €46,04 | €10,95 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16057 | 0,15813 | 0,15346 | 0,10785 | 0,17479 | €12,00 | €35,99 | €1,59 | €-0,55 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | USELESS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,11591 | 0,11382 | 0,10466 | 0,07786 | 0,13843 | €161,07 | €483,22 | €46,93 | €-8,73 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77600,50000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.088,71 | €3.266,12 | €47,03 | €-28,86 |
| Rapida V1 — score 6–7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €300,38 | €901,14 | €46,37 | €0,00 |
| Rapida V1 — score 6–7,5 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11367 | 0,11382 | 0,10544 | 0,07635 | 0,12603 | €211,09 | €633,27 | €45,88 | €0,82 |
| Rapida V1 — score 6–7,5 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €446,88 | €1.340,64 | €46,17 | €-20,39 |
| Rapida V1 — score 6–7,5 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 6,13623 | 6,32200 | 6,14911 | 4,12150 | 6,41501 | €508,05 | €1.524,15 | €0,00 | €46,14 |
| Rapida score 6–7,5 — senza Trend Up | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €292,39 | €877,18 | €45,14 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11367 | 0,11382 | 0,10544 | 0,07635 | 0,12603 | €205,48 | €616,43 | €44,66 | €0,80 |
| Rapida score 6–7,5 — senza Trend Up | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €435,00 | €1.305,00 | €44,94 | €-19,85 |
| Rapida score 6–7,5 — senza Trend Up | UNI | LONG | Momentum / breakout | 60m | 3,0x | 6,13623 | 6,32200 | 6,14911 | 4,12150 | 6,41501 | €494,54 | €1.483,63 | €0,00 | €44,92 |
| Rapida score 6–7,5 — Range Only | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| Rapida score 6–7,5 — Range Only | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| Rapida score 6–7,5 — Range Only | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €326,57 | €979,72 | €50,41 | €0,00 |
| Rapida score 6–7,5 — Range Only | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €479,90 | €1.439,69 | €49,58 | €-21,90 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11008 | 0,11382 | 0,10173 | 0,07394 | 0,12260 | €240,53 | €721,59 | €54,72 | €24,50 |
| Rapida score 6–7,5 — Cost Aware | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €418,42 | €1.255,26 | €43,23 | €-19,09 |
| Rapida V1 — no HIGH + score <7,5 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,13541 | 527,13541 | 512,43358 | 354,05928 | 549,18814 | €585,79 | €1.757,38 | €49,01 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €472,06 | €1.416,18 | €48,77 | €-21,54 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,17541 | 527,17541 | 512,97206 | 354,08615 | 548,48045 | €585,90 | €1.757,69 | €47,36 | €0,00 |
| Rapida V1 — senza PEPE | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| Rapida V1 — senza PEPE | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| Rapida V1 — senza PEPE | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| Rapida V1 — senza PEPE | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| Rapida V1 — senza PEPE | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €22,20 | €66,59 | €2,29 | €-1,01 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| Rapida V1 — target pieno 2R | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| Rapida V1 — target pieno 2R | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,12109 | €278,24 | €834,72 | €42,44 | €0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered — madre | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered — madre | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €293,41 | €880,24 | €44,76 | €0,00 |
| Rapida V3 — score <7,5 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €290,81 | €872,44 | €44,89 | €0,00 |
| Rapida V3 — score <7,5 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11382 | 0,10544 | 0,07635 | 0,12603 | €204,16 | €612,48 | €44,38 | €0,79 |
| Rapida V3 — score <7,5 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €431,89 | €1.295,68 | €44,62 | €-19,71 |
| Rapida V3 — score <7,5 | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,13623 | 6,32200 | 6,14911 | 4,12150 | 6,41501 | €490,48 | €1.471,44 | €0,00 | €44,55 |
| Rapida V3 — no volatilità HIGH | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| Rapida V3 — no volatilità HIGH | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| Rapida V3 — no volatilità HIGH | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €26,13 | €78,40 | €3,99 | €0,00 |
| Rapida V3 — no volatilità HIGH | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €10,94 | €32,83 | €1,13 | €-0,50 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| Rapida V3 — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| Rapida V3 — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| Rapida V3 — Long Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €19,73 | €59,20 | €2,04 | €-0,90 |
| Rapida V3 — Long Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,22925 | 6,32200 | 6,02355 | 4,18398 | 6,53780 | €486,47 | €1.459,41 | €48,19 | €21,73 |
| Rapida V3 — Long + no HIGH + score <7,5 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €310,83 | €932,49 | €47,98 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11382 | 0,10544 | 0,07635 | 0,12603 | €212,69 | €638,08 | €46,23 | €0,83 |
| Rapida V3 — senza ESPORTS | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| Rapida V3 — senza ESPORTS | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| Rapida V3 — senza ESPORTS | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €274,69 | €824,06 | €41,90 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €17,27 | €51,82 | €1,78 | €-0,79 |
| Rapida V3 senza ESPORTS — Long Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,22925 | 6,32200 | 6,02355 | 4,18398 | 6,53780 | €492,09 | €1.476,28 | €48,75 | €21,98 |
| Rapida V3 senza ESPORTS — MFE Lock | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €295,31 | €885,93 | €45,05 | €0,00 |
| Rapida V3 senza ESPORTS — Stress Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| Rapida V3 senza ESPORTS — Stress Guard | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 99,69706 | 100,11700 | 101,13696 | 132,43092 | 97,53720 | €1.183,21 | €3.549,63 | €51,27 | €-14,95 |
| Rapida V3 senza ESPORTS — Stress Guard | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €502,45 | €1.507,35 | €51,91 | €-22,92 |
| Rapida V3 senza ESPORTS — Stress Guard | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,22925 | 6,32200 | 6,02355 | 4,18398 | 6,53780 | €522,98 | €1.568,93 | €51,81 | €23,36 |
| Rapida V3 — qualità completa + profit lock | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| Rapida V3 — qualità completa + profit lock | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| Rapida V3 — qualità completa + profit lock | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €304,49 | €913,46 | €47,00 | €0,00 |
| Rapida V3 — qualità completa + profit lock | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11382 | 0,10544 | 0,07635 | 0,12603 | €209,32 | €627,96 | €45,50 | €0,81 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2420,20000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,15 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 83,18700 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,35 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08181 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €25,73 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 100,11700 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,96 |
| Forza relativa 1H V1 | XMR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 522,67451 | 522,67451 | 500,84717 | 263,95063 | 570,69467 | €505,06 | €1.010,12 | €42,18 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €869,59 | €1.739,17 | €40,40 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,10812 | 0,10812 | 0,10113 | 0,05460 | 0,12350 | €321,13 | €642,27 | €41,51 | €0,00 |
| Forza relativa 1H V1 | SOL | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 99,89102 | 100,11700 | 101,70108 | 149,33707 | 95,90889 | €13,28 | €26,56 | €0,48 | €-0,06 |
| Forza relativa 1H V1 | ENA | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,16057 | 0,15813 | 0,15346 | 0,08109 | 0,17621 | €16,43 | €32,85 | €1,45 | €-0,50 |
| Forza relativa 1H V1 | USELESS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,11098 | 0,11382 | 0,10103 | 0,05605 | 0,13289 | €233,68 | €467,36 | €41,93 | €11,95 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 570,02714 | €13,24 | €26,48 | €1,14 | €0,00 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,16057 | 0,15813 | 0,15346 | 0,08109 | 0,17621 | €16,83 | €33,66 | €1,49 | €-0,51 |
| Forza relativa 1H V2 | USELESS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,11098 | 0,11382 | 0,10103 | 0,05605 | 0,13289 | €272,01 | €544,03 | €48,80 | €13,91 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 2415,46681 | 2420,20000 | 2454,11428 | 3611,12288 | 2318,84814 | €1.754,61 | €3.509,21 | €56,15 | €-6,88 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 100,11700 | 101,87931 | 149,16070 | 94,50736 | €1.329,55 | €2.659,09 | €56,14 | €-9,17 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,33090 | 1,34622 | 1,35970 | 1,98970 | 1,25890 | €35,95 | €71,89 | €1,56 | €-0,83 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 2415,46681 | 2420,20000 | 2454,11428 | 3611,12288 | 2318,84814 | €1.713,30 | €3.426,59 | €54,83 | €-6,71 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 100,11700 | 101,87931 | 149,16070 | 94,50736 | €1.298,24 | €2.596,49 | €54,81 | €-8,95 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,33090 | 1,34622 | 1,35970 | 1,98970 | 1,25890 | €35,10 | €70,20 | €1,52 | €-0,81 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 99,81296 | 100,11700 | 98,23262 | 50,40554 | 102,18346 | €1.381,04 | €2.762,08 | €43,73 | €8,41 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,08061 | 0,08181 | 0,08109 | 0,04071 | 0,08229 | €1.571,36 | €3.142,73 | €0,00 | €46,85 |
| Benchmark Bollinger mean reversion 1H | UNI | SHORT | Bollinger mean reversion | 60m | 2,0x | 6,22675 | 6,32200 | 6,44706 | 9,30900 | 5,89630 | €619,07 | €1.238,13 | €43,81 | €-18,94 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | USELESS | LONG | Trend following EMA | 60m | 2,0x | 0,11591 | 0,11382 | 0,10340 | 0,05854 | 0,14343 | €17,31 | €34,63 | €3,74 | €-0,63 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 100,01299 | 100,11700 | 101,99785 | 149,51943 | 95,64631 | €16,08 | €32,17 | €0,64 | €-0,03 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,08148 | 0,08181 | 0,08296 | 0,12181 | 0,07823 | €14,32 | €28,63 | €0,52 | €-0,12 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 6,22925 | 6,32200 | 5,93539 | 3,14577 | 6,87573 | €446,63 | €893,25 | €42,14 | €13,30 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 568,11972 | €14,50 | €28,99 | €1,35 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €415,84 | €831,69 | €52,53 | €0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 568,11972 | €12,79 | €25,57 | €1,20 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €386,28 | €772,56 | €48,79 | €0,00 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,75819 | €19,78 | €39,56 | €1,68 | €0,59 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top15 Long | ENA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,15596 | 0,15813 | 0,14889 | 0,07876 | 0,17010 | €21,88 | €43,77 | €1,98 | €0,61 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,11098 | 0,11382 | 0,10103 | 0,05605 | 0,13089 | €278,22 | €556,44 | €49,92 | €14,23 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,75819 | €14,47 | €28,94 | €1,23 | €0,43 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top20 Long | ENA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,15596 | 0,15813 | 0,14889 | 0,07876 | 0,17010 | €21,88 | €43,77 | €1,98 | €0,61 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,11098 | 0,11382 | 0,10103 | 0,05605 | 0,13089 | €278,22 | €556,44 | €49,92 | €14,23 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,75819 | €14,47 | €28,94 | €1,23 | €0,43 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 572,97530 | €16,38 | €32,76 | €1,53 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €389,11 | €778,23 | €49,15 | €0,00 |
| Top 5 + BTC — solo MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Top 5 + BTC — solo MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Top 5 + BTC — solo MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 572,97530 | €15,36 | €30,72 | €1,44 | €0,00 |
| Top 5 + BTC — solo MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €364,77 | €729,55 | €46,07 | €0,00 |
| Top 5 + BTC — Guard | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Top 5 + BTC — Guard | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Top 5 + BTC — Guard | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Top 5 + BTC — Guard | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Top 5 + BTC — Guard | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €506,36 | €1.012,72 | €46,92 | €0,00 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Top 5 + BTC — BTC≤3 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 524,45487 | 524,45487 | 505,31170 | 264,84971 | 566,56985 | €595,92 | €1.191,84 | €43,50 | €0,00 |
| Top 5 + BTC — BTC≤3 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €331,20 | €662,40 | €41,83 | €0,00 |
| Top 5 + BTC — BTC 2–3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Top 5 + BTC — BTC 2–3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 576,70983 | €478,87 | €957,73 | €45,40 | €0,00 |
| Top 5 + BTC — Guard + MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Top 5 + BTC — Guard + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Top 5 + BTC — Guard + MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Top 5 + BTC — Guard + MFE | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Top 5 + BTC — Guard + MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €494,59 | €989,17 | €45,82 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €485,59 | €971,18 | €44,99 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €325,70 | €651,40 | €41,14 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,90516 | 525,90516 | 508,26113 | 265,58211 | 564,72203 | €17,51 | €35,02 | €1,17 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11026 | 0,11382 | 0,09902 | 0,05568 | 0,13500 | €212,03 | €424,06 | €43,25 | €13,68 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15596 | 0,15813 | 0,14889 | 0,07876 | 0,17152 | €13,48 | €26,97 | €1,22 | €0,38 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,81108 | €511,11 | €1.022,21 | €43,40 | €15,22 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,51 | €781,02 | €50,94 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,69614 | 6,32200 | 6,09722 | 2,87655 | 6,44709 | €25,63 | €51,25 | €0,00 | €5,63 |
| Top 5 + BTC — target pieno 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Top 5 + BTC — target pieno 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,74 | €781,47 | €50,97 | €0,00 |
| Top 5 + BTC — target pieno 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,69614 | 6,32200 | 6,09722 | 2,87655 | 6,44709 | €25,64 | €51,28 | €0,00 | €5,63 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08170 | 0,08181 | 0,08316 | 0,12214 | 0,07805 | €1.363,98 | €2.727,96 | €48,77 | €-3,64 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | ETH | SHORT | Combo Trend | 60m | 2,0x | 2415,22686 | 2420,20000 | 2454,83114 | 3610,76415 | 2328,09740 | €14,37 | €28,74 | €0,47 | €-0,06 |
| Combo Trend | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,11591 | 0,11382 | 0,10340 | 0,05854 | 0,14343 | €204,72 | €409,44 | €44,18 | €-7,39 |
| Combo Trend | SOL | SHORT | Combo Trend | 60m | 2,0x | 100,01299 | 100,11700 | 101,99785 | 149,51943 | 95,64631 | €20,08 | €40,16 | €0,80 | €-0,04 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08148 | 0,08181 | 0,08296 | 0,12181 | 0,07823 | €13,24 | €26,47 | €0,48 | €-0,11 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 6,22925 | 6,32200 | 5,93539 | 3,14577 | 6,87573 | €478,14 | €956,29 | €45,11 | €14,24 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Mean Reversion | SOL | LONG | Combo Mean Reversion | 60m | 2,0x | 99,81296 | 100,11700 | 98,23262 | 50,40554 | 102,34150 | €1.393,28 | €2.786,55 | €44,12 | €8,49 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 77237,45440 | 77600,50000 | 76310,60495 | 39004,91447 | 78720,41353 | €1.763,77 | €3.527,53 | €42,33 | €16,58 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,33144 | 1,34622 | 1,33864 | 0,67238 | 1,36601 | €1.340,59 | €2.681,19 | €0,00 | €29,77 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 527,13541 | 527,13541 | 508,23306 | 266,20338 | 568,72055 | €660,18 | €1.320,37 | €47,35 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12705 | €377,46 | €754,92 | €49,24 | €0,00 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16057 | 0,15813 | 0,15346 | 0,08109 | 0,17621 | €13,38 | €26,75 | €1,18 | €-0,41 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,81108 | €20,69 | €41,39 | €1,76 | €0,62 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive — madre | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive — madre | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive — madre | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,77304 | 100,11700 | 101,66869 | 149,16070 | 95,98175 | €14,76 | €29,52 | €0,56 | €-0,10 |
| Combo Adaptive — madre | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11008 | 0,11382 | 0,09935 | 0,05559 | 0,13155 | €260,60 | €521,20 | €50,82 | €17,70 |
| Combo Adaptive — madre | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,13623 | 6,32200 | 5,89727 | 3,09879 | 6,61413 | €13,14 | €26,28 | €1,02 | €0,80 |
| Combo Adaptive — madre | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €1.186,93 | €2.373,86 | €48,90 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive — MFE Trail esistente | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11591 | 0,11382 | 0,10466 | 0,05854 | 0,13843 | €182,25 | €364,50 | €35,40 | €-6,58 |
| Combo Adaptive — MFE Trail esistente | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 100,01299 | 100,11700 | 101,79936 | 149,51943 | 96,44025 | €23,91 | €47,81 | €0,85 | €-0,05 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08148 | 0,08181 | 0,08281 | 0,12181 | 0,07882 | €16,73 | €33,46 | €0,55 | €-0,14 |
| Combo Adaptive — MFE Trail esistente | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,75819 | €522,51 | €1.045,03 | €44,37 | €15,56 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive — Quality7 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive — Quality7 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive — Trend/Transition | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive — Long Only | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive — Long Only | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12560 | €400,65 | €801,31 | €52,27 | €0,00 |
| Combo Adaptive — Long Only | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,22925 | 6,32200 | 5,96477 | 3,14577 | 6,75819 | €21,41 | €42,82 | €1,82 | €0,64 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive — parziale 1R | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive — parziale 1R | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11591 | 0,11382 | 0,10466 | 0,05854 | 0,13843 | €21,83 | €43,65 | €4,24 | €-0,79 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €350,40 | €700,80 | €44,26 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,69614 | 6,32200 | 6,11264 | 2,87655 | 6,44709 | €505,26 | €1.010,52 | €0,00 | €111,03 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,61607 | 100,11700 | 101,40716 | 148,92603 | 94,24282 | €20,98 | €41,95 | €0,75 | €-0,21 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,42 | €28,84 | €0,64 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11079 | 0,11382 | 0,10052 | 0,05595 | 0,14161 | €240,28 | €480,55 | €44,56 | €13,13 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,34849 | 1,34622 | 1,37340 | 2,01599 | 1,27376 | €12,53 | €25,07 | €0,46 | €0,04 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08176 | 0,08181 | 0,08303 | 0,12223 | 0,07796 | €14,97 | €29,94 | €0,46 | €-0,02 |
| Combo Adaptive — target pieno 3R | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive — target pieno 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €343,85 | €687,70 | €43,43 | €0,00 |
| Combo Adaptive — target pieno 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,69614 | 6,32200 | 6,11264 | 2,87655 | 6,44709 | €495,82 | €991,64 | €0,00 | €108,96 |
| Combo Adaptive — target pieno 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,61607 | 100,11700 | 101,40716 | 148,92603 | 94,24282 | €20,58 | €41,17 | €0,74 | €-0,21 |
| Combo Adaptive — target pieno 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,15 | €28,30 | €0,63 | €-0,00 |
| Combo Adaptive — target pieno 3R | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11079 | 0,11382 | 0,10052 | 0,05595 | 0,14161 | €235,79 | €471,58 | €43,73 | €12,89 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08176 | 0,08181 | 0,08303 | 0,12223 | 0,07796 | €29,33 | €58,66 | €0,91 | €-0,04 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77303,06629 | 77600,50000 | 78416,23045 | 102684,23973 | 75076,73798 | €1.107,32 | €3.321,96 | €47,84 | €-12,78 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 77206,56560 | 77600,50000 | 78194,80964 | 102556,05464 | 75230,07752 | €1.289,36 | €3.868,07 | €49,51 | €-19,74 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 77600,50000 | 78401,16314 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €52,58 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 99,77304 | 100,11700 | 101,66869 | 132,53186 | 95,98175 | €888,04 | €2.664,11 | €50,62 | €-9,18 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 99,77304 | 100,11700 | 101,45806 | 132,53186 | 96,40301 | €1.019,77 | €3.059,30 | €51,67 | €-10,55 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 100,11700 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €-34,29 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 99,81296 | 100,11700 | 98,23262 | 67,04104 | 102,18346 | €1.037,93 | €3.113,80 | €49,30 | €9,48 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 100,11700 | 102,35930 | 160,38740 | 97,27311 | €478,97 | €957,94 | €0,00 | €63,98 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 99,77304 | 100,11700 | 101,66869 | 132,53186 | 95,98175 | €877,49 | €2.632,47 | €50,02 | €-9,08 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 2415,22686 | 2420,20000 | 2450,87073 | 3208,22634 | 2343,93912 | €1.098,91 | €3.296,73 | €48,65 | €-6,79 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08176 | 0,08181 | 0,08303 | 0,10861 | 0,07923 | €1.081,41 | €3.244,23 | €50,29 | €-1,95 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08061 | 0,08181 | 0,08101 | 0,05414 | 0,08229 | €1.204,04 | €3.612,13 | €0,00 | €53,85 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €529,71 | €1.059,43 | €45,70 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €364,80 | €729,60 | €46,08 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,40286 | 493,14790 | 259,77344 | 556,91277 | €554,63 | €1.109,27 | €45,83 | €0,00 |
| Master Adaptive No Alt V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,36 | €718,72 | €45,39 | €0,00 |
| Master Adaptive No Alt V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16077 | 0,15813 | 0,15357 | 0,08119 | 0,17517 | €14,18 | €28,36 | €1,27 | €-0,47 |
| Master Adaptive No Alt V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,11098 | 0,11382 | 0,10103 | 0,05605 | 0,13089 | €253,05 | €506,09 | €45,40 | €12,94 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 524,22482 | 524,22482 | 504,57786 | 264,73354 | 563,51875 | €580,65 | €1.161,30 | €43,52 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 83,34267 | 83,18700 | 81,78515 | 42,08805 | 86,45769 | €17,30 | €34,61 | €0,65 | €-0,06 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €522,62 | €1.045,25 | €45,08 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,99 | €719,98 | €45,47 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 587,99187 | €446,15 | €892,30 | €38,49 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €360,46 | €720,91 | €45,53 | €0,00 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive — Side × Regime Guard | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11008 | 0,11382 | 0,09935 | 0,05559 | 0,13155 | €237,09 | €474,18 | €46,23 | €16,10 |
| Combo Adaptive — Side × Regime Guard | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,23925 | 6,32200 | 5,98083 | 3,15082 | 6,75608 | €596,36 | €1.192,72 | €49,40 | €15,82 |
| Combo Adaptive — Side × Regime Guard | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 100,09698 | 100,11700 | 101,74088 | 149,64498 | 96,80917 | €16,70 | €33,40 | €0,55 | €-0,01 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €532,34 | €1.064,67 | €45,92 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,61 | €733,22 | €46,31 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €531,77 | €1.063,54 | €45,87 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,22 | €732,44 | €46,26 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,40286 | 498,46164 | 259,77344 | 556,91277 | €32,91 | €65,81 | €2,04 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10448 | 0,05539 | 0,12353 | €480,15 | €960,31 | €45,49 | €0,00 |
| Rapida V3 NoHigh — Range Only | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| Rapida V3 NoHigh — Range Only | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €330,06 | €990,17 | €50,95 | €0,00 |
| Rapida V3 NoHigh — Range Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €493,88 | €1.481,64 | €51,02 | €-22,53 |
| Rapida V3 NoHigh — Range Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,32326 | 6,32200 | 6,11741 | 4,24713 | 6,63205 | €525,14 | €1.575,42 | €51,29 | €-0,32 |
| Rapida V3 NoHigh — Regime Guard | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €333,52 | €1.000,56 | €50,87 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 77206,56560 | 77600,50000 | 78071,27913 | 102556,05464 | 75909,49530 | €1.508,59 | €4.525,78 | €50,69 | €-23,09 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,34622 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-3,25 |
| MAIN — Side × Regime Guard | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2420,20000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,22 |
| MAIN — Side × Regime Guard | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,15813 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €-8,27 |
| MAIN — Side × Regime Guard | ZEC | LONG | Confluenza trend | 240m | 3,0x | 852,88054 | 835,88000 | 799,15184 | 572,85143 | 960,33794 | €290,60 | €871,79 | €54,92 | €-17,38 |
| MAIN — Dynamic Asset Selector | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,15813 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €-7,75 |
| Combo Trend — Side × Regime Guard | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend — Side × Regime Guard | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,71926 | 0,72480 | 0,73823 | 1,07529 | 0,67752 | €1.029,16 | €2.058,32 | €54,29 | €-15,87 |
| Combo Trend — Side × Regime Guard | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,11008 | 0,11382 | 0,09816 | 0,05559 | 0,13632 | €249,64 | €499,29 | €54,09 | €16,95 |
| Combo Trend — Side × Regime Guard | UNI | LONG | Combo Trend | 60m | 2,0x | 6,32326 | 6,32200 | 6,02918 | 3,19325 | 6,97025 | €557,09 | €1.114,19 | €51,82 | €-0,22 |
| FAST NoHigh <7,5 · SHORT only | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,13541 | 527,13541 | 512,43358 | 354,05928 | 549,18814 | €571,22 | €1.713,65 | €47,79 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,15813 | 0,15504 | 0,10785 | 0,16887 | €460,31 | €1.380,94 | €47,56 | €-21,00 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| Bilanciata V3 · LONG only | USELESS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,11591 | 0,11382 | 0,10466 | 0,07786 | 0,13843 | €152,34 | €457,03 | €44,39 | €-8,25 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77600,50000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.029,72 | €3.089,16 | €44,48 | €-27,29 |
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
| Rapida V3 NoHigh — Range Only | BTR | SHORT | 2026-09-02T06:30:00+00:00 | 0,07117 | €75,84 | 1,49 | TARGET |
| Bilanciata 1H V2 | BTR | SHORT | 2026-09-02T07:00:00+00:00 | 0,06596 | €86,91 | 1,99 | TARGET |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | 2026-09-02T05:30:00+00:00 | 0,08189 | €26,33 | 0,51 | STOP |
| Combo Trend — Side × Regime Guard | UNI | LONG | 2026-09-02T05:30:00+00:00 | 6,35208 | €2,49 | 2,17 | TARGET |
| Bilanciata 1H V1 | DOGE | SHORT | 2026-09-02T05:30:00+00:00 | 0,08190 | €-1,01 | -1,11 | STOP |
| Top 5 + BTC — Guard + BTC≤3 + MFE | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22173 | €90,39 | 2,16 | TARGET |
| Forza relativa 1H V2 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,27314 | €104,19 | 2,16 | TARGET |
| Forza relativa 1H V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22173 | €89,83 | 2,16 | TARGET |
| Benchmark trend following EMA 1H | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,32649 | €89,82 | 2,16 | TARGET |
| Combo Trend | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,32649 | €95,94 | 2,16 | TARGET |
| Combo Scanner | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,24559 | €3,77 | 2,16 | TARGET |
| Combo Adaptive — MFE Trail esistente | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22949 | €86,11 | 1,96 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 628/30 | 33/30 | 0,86 | 2,04 | -0,07R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 583/30 | 20/30 | 0,83 | 1,90 | -0,09R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 265/30 | 22/30 | 0,88 | 1,74 | -0,06R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 267/30 | 22/30 | 0,82 | 1,57 | -0,09R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 536/30 | 31/30 | 0,94 | 0,62 | -0,03R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 493/30 | 11/30 | 0,93 | 0,00 | -0,03R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 155/30 | 8/30 | 0,87 | 1,02 | -0,06R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 351/30 | 17/30 | 0,70 | 4,50 | -0,16R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 535/30 | 24/30 | 0,74 | 0,64 | -0,13R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 493/30 | 7/30 | 0,67 | 0,02 | -0,17R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 536/30 | 30/30 | 0,96 | 1,02 | -0,02R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 896/30 | 55/30 | 0,89 | 1,12 | -0,05R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 176/30 | 15/30 | 0,65 | 0,99 | -0,21R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 787/30 | 44/30 | 0,81 | 1,20 | -0,09R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 791/30 | 37/30 | 0,81 | 0,76 | -0,09R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 732/30 | 23/30 | 0,77 | 1,12 | -0,12R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 367/30 | 56/30 | 0,78 | 0,87 | -0,13R | €-3,30 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 15/30 | 0,00 | 1,13 | 0,00R | €3,88 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 42/30 | 0,00 | 2,39 | 0,00R | €23,51 | 3,82% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 31/30 | 17/30 | 0,49 | 0,71 | -0,25R | €-1,51 | 0,71% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 50/30 | 28/30 | 0,67 | 0,60 | -0,18R | €-2,16 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 928/30 | 128/30 | 0,92 | 0,65 | -0,04R | €-7,73 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 115/30 | 0,00 | 0,84 | 0,00R | €-3,00 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 305/30 | 118/30 | 1,17 | 0,75 | 0,09R | €-5,42 | 11,21% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 589/30 | 176/30 | 1,01 | 0,89 | 0,00R | €-2,32 | 10,71% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 510/30 | 130/30 | 0,95 | 0,66 | -0,02R | €-7,14 | 10,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 278/30 | 99/30 | 0,86 | 0,82 | -0,07R | €-4,42 | 7,99% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 564/30 | 144/30 | 0,86 | 0,88 | -0,07R | €-2,37 | 8,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 631/30 | 180/30 | 0,89 | 0,97 | -0,06R | €-0,53 | 8,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1043/30 | 258/30 | 0,83 | 1,13 | -0,09R | €2,24 | 7,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 172/30 | 0,00 | 1,25 | 0,00R | €5,30 | 6,72% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 101/30 | 0,00 | 0,69 | 0,00R | €-9,85 | 15,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 47/30 | 0,00 | 1,07 | 0,00R | €1,92 | 4,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 595/30 | 143/30 | 0,92 | 0,81 | -0,04R | €-5,24 | 14,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1003/30 | 247/30 | 0,82 | 0,99 | -0,09R | €-0,12 | 6,56% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 76/30 | 52/30 | 0,87 | 1,27 | -0,07R | €6,29 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 969/30 | 252/30 | 0,85 | 1,04 | -0,07R | €0,73 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 727/30 | 146/30 | 0,90 | 0,72 | -0,05R | €-7,26 | 16,28% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 310/30 | 118/30 | 0,97 | 0,81 | -0,02R | €-5,47 | 8,24% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 312/30 | 115/30 | 0,93 | 0,85 | -0,04R | €-3,92 | 6,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 613/30 | 196/30 | 0,95 | 0,95 | -0,02R | €-1,12 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 63/30 | 0,00 | 1,19 | 0,00R | €4,49 | 4,19% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 95/30 | 0,00 | 1,16 | 0,00R | €3,16 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 650/30 | 152/30 | 0,80 | 0,95 | -0,10R | €-0,89 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 195/30 | 0,00 | 1,00 | 0,00R | €-0,03 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 208/30 | 0,00 | 1,07 | 0,00R | €1,20 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 83/30 | 0,00 | 1,22 | 0,00R | €4,60 | 4,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 922/30 | 220/30 | 0,83 | 0,87 | -0,09R | €-2,66 | 10,92% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 343/30 | 52/30 | 0,84 | 1,24 | -0,10R | €5,39 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 316/30 | 85/30 | 1,20 | 0,55 | 0,09R | €-15,24 | 15,18% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 15/30 | 9/30 | 0,64 | 0,86 | -0,19R | €-3,49 | 1,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 3/30 | 3/30 | 1,15 | 1,17 | 0,10R | €5,87 | 0,96% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 9/30 | 6/30 | 3,40 | 4,66 | 0,60R | €34,87 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 2/30 | 2/30 | 1,56 | 1,54 | 0,31R | €14,72 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 18/30 | 11/30 | 0,30 | 0,71 | -0,57R | €-8,89 | 1,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 7/30 | 5/30 | 0,42 | 0,61 | -0,53R | €-17,29 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 24/30 | 18/30 | 0,55 | 0,38 | -0,31R | €-24,04 | 4,61% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 5/30 | 4/30 | 0,56 | 0,78 | -0,37R | €-8,28 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 764/30 | 180/30 | 0,99 | 1,07 | -0,00R | €1,24 | 7,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 475/30 | 141/30 | 1,06 | 1,16 | 0,03R | €3,25 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 845/30 | 189/30 | 0,99 | 0,75 | -0,00R | €-4,82 | 15,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 705/30 | 166/30 | 0,94 | 1,03 | -0,03R | €0,40 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 89/30 | 46/30 | 1,27 | 0,79 | 0,12R | €-5,95 | 4,21% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 89/30 | 46/30 | 1,26 | 0,69 | 0,12R | €-8,61 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 248/30 | 98/30 | 0,96 | 0,80 | -0,02R | €-4,94 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 262/30 | 77/30 | 1,02 | 0,76 | 0,01R | €-5,94 | 5,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 99/30 | 0,74 | 0,51 | -0,20R | €-11,57 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 137/30 | 0,00 | 0,99 | 0,00R | €-0,25 | 10,02% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 80/30 | 0,74 | 0,36 | -0,20R | €-16,38 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 117/30 | 51/30 | 1,20 | 0,43 | 0,09R | €-23,98 | 14,46% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 482/30 | 152/30 | 1,10 | 0,96 | 0,05R | €-0,97 | 11,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 634/30 | 174/30 | 0,97 | 0,78 | -0,02R | €-5,05 | 11,90% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 135/30 | 0,00 | 1,30 | 0,00R | €5,76 | 8,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 15/30 | 12/30 | 1,92 | 1,07 | 0,28R | €1,75 | 1,89% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 20/30 | 15/30 | 0,57 | 1,07 | -0,29R | €1,72 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 32/30 | 21/30 | 0,52 | 1,13 | -0,31R | €2,74 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 335/30 | 121/30 | 0,84 | 1,45 | -0,10R | €10,16 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 265/30 | 89/30 | 0,83 | 1,53 | -0,10R | €10,85 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 645/30 | 138/30 | 0,96 | 0,70 | -0,02R | €-5,95 | 12,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 25/30 | 16/30 | 0,59 | 0,72 | -0,29R | €-8,90 | 3,14% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 17/30 | 8/30 | 1,75 | 0,19 | 0,30R | €-43,81 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 24/30 | 16/30 | 0,47 | 0,58 | -0,39R | €-15,80 | 3,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 36/30 | 23/30 | 0,50 | 0,66 | -0,35R | €-11,71 | 4,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 6/30 | 7/30 | 0,46 | 0,57 | -0,38R | €-16,10 | 1,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 16/30 | 19/30 | 1,07 | 0,55 | 0,04R | €-12,99 | 3,93% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 319/30 | 82/30 | 1,03 | 0,73 | 0,02R | €-7,67 | 7,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 83/30 | 0,00 | 0,74 | 0,00R | €-7,52 | 8,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 72/30 | 0,00 | 0,64 | 0,00R | €-11,70 | 11,41% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 78/30 | 0,00 | 0,73 | 0,00R | €-8,13 | 7,98% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 594/30 | 114/30 | 1,33 | 0,71 | 0,11R | €-6,96 | 9,02% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 278/30 | 82/30 | 1,03 | 0,68 | 0,02R | €-10,39 | 9,97% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 290/30 | 70/30 | 1,03 | 0,67 | 0,02R | €-11,09 | 8,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 198/30 | 71/30 | 0,94 | 0,56 | -0,04R | €-18,23 | 13,50% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 305/30 | 80/30 | 1,01 | 0,73 | 0,01R | €-8,38 | 7,80% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 773/30 | 109/30 | 0,92 | 0,48 | -0,04R | €-14,72 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 303/30 | 123/30 | 1,15 | 0,97 | 0,08R | €-0,81 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 255/30 | 70/30 | 0,51 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 255/30 | 70/30 | 0,51 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 255/30 | 70/30 | 0,51 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 285/30 | 89/30 | 0,65 | 0,64 | -0,20R | €-9,30 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 304/30 | 61/30 | 0,76 | 0,58 | -0,11R | €-12,17 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 277/30 | 62/30 | 0,68 | 0,56 | -0,15R | €-12,20 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 473/30 | 153/30 | 1,05 | 1,03 | 0,02R | €0,59 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 474/30 | 152/30 | 1,05 | 0,99 | 0,02R | €-0,10 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 474/30 | 152/30 | 1,05 | 0,99 | 0,02R | €-0,10 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 464/30 | 141/30 | 1,10 | 1,05 | 0,06R | €1,11 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 167/30 | 41/30 | 0,69 | 0,28 | -0,19R | €-25,35 | 11,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 343/30 | 84/30 | 0,87 | 0,46 | -0,07R | €-16,48 | 16,16% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 362/30 | 104/30 | 1,06 | 0,59 | 0,02R | €-12,25 | 13,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 303/30 | 88/30 | 0,93 | 0,66 | -0,04R | €-10,19 | 11,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 467/30 | 143/30 | 1,14 | 0,79 | 0,06R | €-5,09 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 381/30 | 126/30 | 1,09 | 0,84 | 0,05R | €-4,03 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 523/30 | 133/30 | 1,06 | 0,82 | 0,02R | €-3,60 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 411/30 | 127/30 | 1,05 | 1,07 | 0,03R | €1,50 | 12,06% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 387/30 | 123/30 | 1,07 | 1,07 | 0,04R | €1,60 | 11,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 511/30 | 158/30 | 1,12 | 1,28 | 0,06R | €5,41 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 34/30 | 20/30 | 0,80 | 1,01 | -0,13R | €0,16 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 10/30 | 9/30 | 1,92 | 2,16 | 0,39R | €21,25 | 1,01% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 25/30 | 14/30 | 0,82 | 0,72 | -0,10R | €-9,99 | 2,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 5/30 | 4/30 | 1,99 | 0,56 | 0,41R | €-17,33 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 27/30 | 16/30 | 1,10 | 2,35 | 0,06R | €20,84 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 7/30 | 6/30 | 1,26 | 2,73 | 0,16R | €32,74 | 1,18% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 31/30 | 18/30 | 0,94 | 1,25 | -0,04R | €6,85 | 3,33% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 11/30 | 10/30 | 0,73 | 1,22 | -0,18R | €5,77 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08181**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 31.8 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 77600.5 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, stop_within_limit**
- High **0.08181**; close **0.08174**; wick alta **6.2%**; volume **x0.20**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=477; LEGACY_RESEARCH_EVIDENCE_V3=5315; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **RANGE**
- Famiglia: **RANGE**
- Confidenza: **86,80%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 33%, ADX 15.7.
- BTC trend score: **0,00**; ADX: **15,74**; breadth sopra EMA50: **33,33%**
- Mediana alt vs BTC: **-0,52%**; dispersione: **21,17%**

- Aperti in questo ciclo: **29**
- Chiusi in questo ciclo: **34**
- Posizioni research aperte: **979**
- Trade research chiusi: **37546**
- Eventi di mercato indipendenti chiusi: **5049**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **99783**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 14 | 628 | 628 | 35,67% | 0,86 | -0,07R | €-414,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 15 | 583 | 583 | 34,82% | 0,83 | -0,09R | €-498,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 6 | 265 | 265 | 47,92% | 0,88 | -0,06R | €-169,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 6 | 267 | 267 | 35,21% | 0,82 | -0,09R | €-239,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 9 | 536 | 536 | 36,75% | 0,94 | -0,03R | €-163,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 9 | 493 | 493 | 37,12% | 0,93 | -0,03R | €-172,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 6 | 155 | 155 | 37,42% | 0,87 | -0,06R | €-95,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 8 | 351 | 351 | 30,77% | 0,70 | -0,16R | €-562,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 11 | 535 | 535 | 31,78% | 0,74 | -0,13R | €-700,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 11 | 493 | 493 | 30,63% | 0,67 | -0,17R | €-850,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 9 | 536 | 536 | 37,13% | 0,96 | -0,02R | €-103,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 13 | 896 | 896 | 40,29% | 0,89 | -0,05R | €-448,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 176 | 176 | 35,23% | 0,65 | -0,21R | €-368,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 14 | 787 | 787 | 33,29% | 0,81 | -0,09R | €-742,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 14 | 791 | 791 | 33,25% | 0,81 | -0,09R | €-743,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 14 | 732 | 732 | 32,65% | 0,77 | -0,12R | €-858,07 |
| MAIN | 23 | 367 | 367 | 28,61% | 0,78 | -0,13R | €-486,14 |
| RSI_EXTREME_LONG_15M | 0 | 31 | 31 | 41,94% | 0,49 | -0,25R | €-78,48 |
| RSI_EXTREME_SHORT_15M | 0 | 50 | 50 | 38,00% | 0,67 | -0,18R | €-87,69 |
| Bilanciata 1H V1 | 28 | 928 | 928 | 36,10% | 0,92 | -0,04R | €-390,43 |
| Bilanciata 1H V2 | 12 | 349 | 305 | 40,69% | 1,17 | 0,09R | €300,25 |
| Bilanciata 1H V3 Filtered | 20 | 589 | 589 | 37,86% | 1,01 | 0,00R | €18,21 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 20 | 510 | 510 | 37,65% | 0,95 | -0,02R | €-127,13 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 4 | 278 | 278 | 37,77% | 0,86 | -0,07R | €-192,11 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 13 | 564 | 564 | 36,17% | 0,86 | -0,07R | €-390,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 13 | 631 | 631 | 36,93% | 0,89 | -0,06R | €-356,52 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 17 | 1043 | 1043 | 35,95% | 0,83 | -0,09R | €-917,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 14 | 595 | 595 | 38,49% | 0,92 | -0,04R | €-247,86 |
| SHADOW_1H_FAST_TP2_V1 | 17 | 1003 | 1003 | 33,70% | 0,82 | -0,09R | €-921,45 |
| Rapida 1H V2 | 2 | 87 | 76 | 42,53% | 0,87 | -0,07R | €-57,73 |
| Rapida 1H V3 Filtered | 14 | 969 | 969 | 36,53% | 0,85 | -0,07R | €-717,25 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 14 | 727 | 727 | 38,65% | 0,90 | -0,05R | €-340,49 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 6 | 310 | 310 | 49,03% | 0,97 | -0,02R | €-54,28 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 6 | 312 | 312 | 38,78% | 0,93 | -0,04R | €-113,16 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 9 | 613 | 613 | 39,48% | 0,95 | -0,02R | €-148,43 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 11 | 650 | 650 | 34,92% | 0,80 | -0,10R | €-659,44 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 14 | 922 | 922 | 36,01% | 0,83 | -0,09R | €-799,21 |
| SHADOW_4H_WIDE | 35 | 343 | 343 | 23,91% | 0,84 | -0,10R | €-358,46 |
| SHADOW_BOLLINGER_MR_1H | 5 | 316 | 316 | 49,68% | 1,20 | 0,09R | €271,80 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 15 | 15 | 46,67% | 0,64 | -0,19R | €-28,10 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 3 | 3 | 33,33% | 1,15 | 0,10R | €3,08 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 9 | 9 | 77,78% | 3,40 | 0,60R | €54,38 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 18 | 18 | 27,78% | 0,30 | -0,57R | €-102,87 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 7 | 7 | 14,29% | 0,42 | -0,53R | €-37,20 |
| SHADOW_BTC_EMA_1H | 1 | 24 | 24 | 37,50% | 0,55 | -0,31R | €-75,02 |
| SHADOW_BTC_EMA_4H | 0 | 5 | 5 | 20,00% | 0,56 | -0,37R | €-18,62 |
| SHADOW_COMBO_ADAPTIVE | 22 | 764 | 764 | 38,87% | 0,99 | -0,00R | €-26,90 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 12 | 475 | 475 | 40,21% | 1,06 | 0,03R | €147,92 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 20 | 845 | 845 | 40,95% | 0,99 | -0,00R | €-36,80 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 22 | 705 | 705 | 40,99% | 0,94 | -0,03R | €-200,22 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 89 | 89 | 46,07% | 1,27 | 0,12R | €107,17 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 89 | 89 | 40,45% | 1,26 | 0,12R | €104,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 9 | 248 | 248 | 36,69% | 0,96 | -0,02R | €-44,62 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 1 | 262 | 262 | 40,08% | 1,02 | 0,01R | €24,07 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 4 | 117 | 117 | 48,72% | 1,20 | 0,09R | €102,01 |
| SHADOW_COMBO_SCANNER | 13 | 482 | 482 | 37,97% | 1,10 | 0,05R | €251,87 |
| SHADOW_COMBO_TREND | 24 | 634 | 634 | 35,17% | 0,97 | -0,02R | €-115,72 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 15 | 15 | 66,67% | 1,92 | 0,28R | €41,36 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 20 | 20 | 40,00% | 0,57 | -0,29R | €-57,12 |
| SHADOW_DOGE_EMA_1H | 1 | 32 | 32 | 34,38% | 0,52 | -0,31R | €-99,35 |
| SHADOW_DONCHIAN_1H | 13 | 335 | 335 | 32,84% | 0,84 | -0,10R | €-327,77 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 13 | 265 | 265 | 34,72% | 0,83 | -0,10R | €-262,68 |
| SHADOW_EMA_TREND_1H | 24 | 645 | 645 | 35,04% | 0,96 | -0,02R | €-144,44 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 25 | 25 | 36,00% | 0,59 | -0,29R | €-71,29 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 17 | 17 | 58,82% | 1,75 | 0,30R | €50,23 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 24 | 24 | 29,17% | 0,47 | -0,39R | €-94,21 |
| SHADOW_ETH_EMA_1H | 1 | 36 | 36 | 36,11% | 0,50 | -0,35R | €-125,74 |
| SHADOW_ETH_EMA_4H | 1 | 6 | 6 | 33,33% | 0,46 | -0,38R | €-22,83 |
| SHADOW_GLOBAL_PURE | 1 | 16 | 16 | 50,00% | 1,07 | 0,04R | €5,72 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 10 | 319 | 319 | 33,23% | 1,03 | 0,02R | €59,23 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 9 | 594 | 594 | 65,99% | 1,33 | 0,11R | €630,71 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 9 | 278 | 278 | 33,09% | 1,03 | 0,02R | €56,08 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 9 | 290 | 290 | 32,07% | 1,03 | 0,02R | €53,70 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 8 | 198 | 198 | 31,31% | 0,94 | -0,04R | €-71,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | 9 | 305 | 305 | 32,79% | 1,01 | 0,01R | €16,91 |
| Forza relativa 1H V1 | 24 | 773 | 773 | 32,47% | 0,92 | -0,04R | €-345,19 |
| Forza relativa 1H V2 | 14 | 326 | 303 | 37,73% | 1,15 | 0,08R | €254,02 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 14 | 255 | 255 | 26,67% | 0,51 | -0,28R | €-719,50 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 14 | 255 | 255 | 26,67% | 0,51 | -0,28R | €-719,50 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 14 | 255 | 255 | 26,67% | 0,51 | -0,28R | €-719,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 13 | 285 | 285 | 28,77% | 0,65 | -0,20R | €-557,81 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 14 | 304 | 304 | 52,63% | 0,76 | -0,11R | €-322,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 14 | 277 | 277 | 51,62% | 0,68 | -0,15R | €-403,72 |
| SHADOW_SCANNER_TOP10_LONG | 13 | 473 | 473 | 39,32% | 1,05 | 0,02R | €110,29 |
| SHADOW_SCANNER_TOP15_LONG | 13 | 474 | 474 | 39,45% | 1,05 | 0,02R | €107,36 |
| SHADOW_SCANNER_TOP20_LONG | 13 | 474 | 474 | 39,45% | 1,05 | 0,02R | €107,36 |
| SHADOW_SCANNER_TOP5_BTC | 12 | 464 | 464 | 37,50% | 1,10 | 0,06R | €257,25 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 5 | 167 | 167 | 28,74% | 0,69 | -0,19R | €-315,42 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 11 | 343 | 343 | 32,94% | 0,87 | -0,07R | €-236,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 9 | 362 | 362 | 42,54% | 1,06 | 0,02R | €88,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 10 | 303 | 303 | 34,32% | 0,93 | -0,04R | €-107,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 10 | 467 | 467 | 44,11% | 1,14 | 0,06R | €275,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 11 | 381 | 381 | 37,80% | 1,09 | 0,05R | €180,19 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 11 | 523 | 523 | 43,21% | 1,06 | 0,02R | €129,21 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 12 | 411 | 411 | 36,50% | 1,05 | 0,03R | €107,79 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 12 | 387 | 387 | 35,92% | 1,07 | 0,04R | €135,64 |
| SHADOW_SCANNER_TOP5_LONG | 12 | 511 | 511 | 39,14% | 1,12 | 0,06R | €313,54 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 34 | 34 | 38,24% | 0,80 | -0,13R | €-45,82 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 10 | 10 | 60,00% | 1,92 | 0,39R | €38,66 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 25 | 25 | 48,00% | 0,82 | -0,10R | €-25,26 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 5 | 5 | 60,00% | 1,99 | 0,41R | €20,58 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 27 | 27 | 48,15% | 1,10 | 0,06R | €15,78 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 7 | 7 | 42,86% | 1,26 | 0,16R | €10,86 |
| SHADOW_SOL_EMA_1H | 1 | 31 | 31 | 38,71% | 0,94 | -0,04R | €-13,23 |
| SHADOW_SOL_EMA_4H | 0 | 11 | 11 | 36,36% | 0,73 | -0,18R | €-20,11 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 2 | 94 | 94 | 27,66% | 0,51 | -0,29R | €-270,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 3 | 157 | 157 | 45,86% | 1,21 | 0,09R | €147,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 6 | 135 | 135 | 35,56% | 0,75 | -0,12R | €-163,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 20 | 20 | 30,00% | 0,64 | -0,19R | €-38,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 2 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 58 | 58 | 34,48% | 1,17 | 0,07R | €40,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 59 | 59 | 22,03% | 0,47 | -0,26R | €-153,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 2 | 88 | 88 | 27,27% | 0,42 | -0,36R | €-316,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 3 | 139 | 139 | 44,60% | 1,19 | 0,09R | €120,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 7 | 127 | 127 | 34,65% | 0,67 | -0,16R | €-204,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 19 | 19 | 26,32% | 0,63 | -0,21R | €-40,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 2 | 5 | 5 | 80,00% | 5,04 | 0,82R | €41,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 57 | 57 | 35,09% | 1,25 | 0,10R | €57,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 56 | 56 | 21,43% | 0,36 | -0,33R | €-185,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 12 | 12 | 41,67% | 0,62 | -0,24R | €-28,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 65 | 65 | 52,31% | 1,14 | 0,07R | €45,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 5 | 72 | 72 | 41,67% | 0,59 | -0,25R | €-177,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 36 | 36 | 58,33% | 1,46 | 0,17R | €62,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 44 | 44 | 45,45% | 0,79 | -0,10R | €-44,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,66 | -0,20R | €-21,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 67 | 67 | 40,30% | 0,98 | -0,01R | €-5,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 5 | 74 | 74 | 35,14% | 0,58 | -0,23R | €-172,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 36 | 36 | 33,33% | 1,25 | 0,09R | €31,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 43 | 43 | 30,23% | 0,81 | -0,08R | €-32,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 41 | 41 | 31,71% | 0,70 | -0,13R | €-51,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 3 | 185 | 185 | 40,00% | 0,95 | -0,03R | €-46,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 5 | 96 | 96 | 37,50% | 0,81 | -0,10R | €-98,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 50 | 50 | 34,00% | 1,29 | 0,11R | €55,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 63 | 63 | 31,75% | 0,74 | -0,12R | €-76,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 40 | 40 | 32,50% | 0,67 | -0,14R | €-57,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 3 | 167 | 167 | 40,72% | 1,01 | 0,00R | €4,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 5 | 84 | 84 | 39,29% | 0,78 | -0,11R | €-92,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 49 | 49 | 34,69% | 1,34 | 0,13R | €61,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 58 | 58 | 31,03% | 0,56 | -0,21R | €-120,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 6 | 151 | 151 | 37,09% | 0,86 | -0,06R | €-95,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 2 | 31 | 31 | 25,81% | 0,36 | -0,47R | €-146,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 73 | 73 | 32,88% | 0,72 | -0,17R | €-124,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 6 | 134 | 134 | 36,57% | 0,88 | -0,06R | €-80,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 40 | 40 | 25,00% | 0,83 | -0,08R | €-32,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 2 | 52 | 52 | 26,92% | 0,46 | -0,34R | €-174,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 86 | 86 | 36,05% | 0,89 | -0,06R | €-51,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 7 | 172 | 172 | 35,47% | 0,79 | -0,11R | €-182,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 2 | 8 | 8 | 62,50% | 2,61 | 0,61R | €49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 59 | 59 | 27,12% | 0,89 | -0,05R | €-28,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 80 | 80 | 26,25% | 0,61 | -0,20R | €-156,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 2 | 50 | 50 | 26,00% | 0,41 | -0,38R | €-191,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 73 | 73 | 35,62% | 0,85 | -0,09R | €-63,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 7 | 160 | 160 | 34,38% | 0,72 | -0,14R | €-218,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 2 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 58 | 58 | 27,59% | 0,85 | -0,06R | €-36,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 75 | 75 | 25,33% | 0,47 | -0,27R | €-205,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 41 | 41 | 31,71% | 0,70 | -0,13R | €-51,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 3 | 186 | 186 | 40,32% | 0,97 | -0,01R | €-26,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 5 | 96 | 96 | 39,58% | 0,92 | -0,04R | €-38,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 50 | 50 | 34,00% | 1,29 | 0,11R | €55,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 63 | 63 | 31,75% | 0,74 | -0,12R | €-76,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 138 | 138 | 36,23% | 0,58 | -0,22R | €-299,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 2 | 221 | 221 | 42,08% | 1,01 | 0,01R | €11,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 7 | 193 | 193 | 39,38% | 0,93 | -0,03R | €-61,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 32 | 32 | 34,38% | 0,58 | -0,23R | €-73,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 2 | 7 | 7 | 42,86% | 0,81 | -0,11R | €-7,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 76 | 76 | 46,05% | 1,36 | 0,12R | €87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 91 | 91 | 41,76% | 0,83 | -0,08R | €-71,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 29,03% | 0,44 | -0,42R | €-129,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 28 | 28 | 28,57% | 0,61 | -0,28R | €-77,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 3 | 64 | 64 | 43,75% | 0,87 | -0,06R | €-38,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 10 | 10 | 50,00% | 1,26 | 0,14R | €14,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 29 | 29 | 24,14% | 0,38 | -0,42R | €-121,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 2 | 116 | 116 | 25,86% | 0,47 | -0,30R | €-344,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 3 | 197 | 197 | 39,59% | 0,98 | -0,01R | €-21,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 7 | 168 | 168 | 35,12% | 0,77 | -0,11R | €-187,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 2 | 8 | 8 | 62,50% | 2,61 | 0,61R | €49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 69 | 69 | 33,33% | 1,27 | 0,11R | €73,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 79 | 79 | 25,32% | 0,56 | -0,22R | €-176,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 2 | 116 | 116 | 25,86% | 0,47 | -0,30R | €-344,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 3 | 199 | 199 | 39,70% | 0,99 | -0,01R | €-11,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 7 | 169 | 169 | 34,91% | 0,76 | -0,12R | €-198,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 2 | 8 | 8 | 62,50% | 2,61 | 0,61R | €49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 69 | 69 | 33,33% | 1,27 | 0,11R | €73,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 79 | 79 | 25,32% | 0,56 | -0,22R | €-176,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 110 | 110 | 26,36% | 0,45 | -0,32R | €-350,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 3 | 177 | 177 | 40,11% | 1,00 | 0,00R | €2,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 7 | 158 | 158 | 33,54% | 0,65 | -0,17R | €-269,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 28 | 28 | 25,00% | 0,63 | -0,20R | €-56,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 2 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 68 | 68 | 33,82% | 1,31 | 0,12R | €81,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 74 | 74 | 24,32% | 0,40 | -0,31R | €-230,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 4 | 33 | 33 | 27,27% | 0,70 | -0,17R | €-55,49 |
| MAIN | ALT_ROTATION_UP | 6 | 86 | 86 | 29,07% | 0,60 | -0,25R | €-218,66 |
| MAIN | RANGE | 5 | 79 | 79 | 22,78% | 0,67 | -0,20R | €-158,53 |
| MAIN | RANGE_HIGH_VOL | 1 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 3 | 38 | 38 | 26,32% | 0,70 | -0,19R | €-71,12 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 2 | 44 | 44 | 29,55% | 1,00 | 0,00R | €0,45 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 16 | 16 | 37,50% | 0,17 | -0,50R | €-79,41 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 22 | 22 | 45,45% | 1,09 | 0,04R | €7,83 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 111 | 111 | 25,23% | 0,44 | -0,37R | €-413,69 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 5 | 210 | 210 | 44,29% | 1,13 | 0,07R | €142,70 |
| Bilanciata 1H V1 | RANGE | 14 | 193 | 193 | 40,41% | 1,12 | 0,06R | €113,96 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 27,66% | 0,51 | -0,32R | €-151,94 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 3 | 9 | 9 | 33,33% | 1,14 | 0,08R | €7,38 |
| Bilanciata 1H V1 | TRANSITION | 0 | 106 | 106 | 36,79% | 1,14 | 0,07R | €72,43 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 121 | 121 | 29,75% | 0,84 | -0,08R | €-101,88 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 4 | 114 | 96 | 49,12% | 1,55 | 0,24R | €274,68 |
| Bilanciata 1H V2 | RANGE | 8 | 144 | 131 | 36,11% | 0,92 | -0,04R | €-63,89 |
| Bilanciata 1H V2 | TRANSITION | 0 | 91 | 78 | 37,36% | 1,19 | 0,10R | €89,47 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 84 | 84 | 26,19% | 0,42 | -0,39R | €-327,44 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 4 | 122 | 122 | 45,08% | 1,36 | 0,18R | €215,41 |
| Bilanciata 1H V3 Filtered | RANGE | 11 | 135 | 135 | 42,22% | 1,17 | 0,08R | €109,99 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 18 | 18 | 27,78% | 0,56 | -0,28R | €-50,80 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 2 | 5 | 5 | 40,00% | 1,84 | 0,36R | €18,00 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 56 | 56 | 33,93% | 1,03 | 0,01R | €7,36 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 70 | 70 | 32,86% | 1,07 | 0,04R | €26,04 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 73 | 73 | 23,29% | 0,28 | -0,49R | €-360,81 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 120 | 120 | 45,83% | 1,41 | 0,20R | €236,41 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 11 | 113 | 113 | 40,71% | 0,99 | -0,01R | €-6,17 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 16 | 16 | 31,25% | 0,69 | -0,19R | €-29,97 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 2 | 5 | 5 | 40,00% | 1,84 | 0,36R | €18,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 48 | 48 | 33,33% | 1,01 | 0,00R | €1,68 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 49 | 49 | 28,57% | 0,85 | -0,07R | €-34,79 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 30 | 30 | 23,33% | 0,53 | -0,23R | €-70,34 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 2 | 80 | 80 | 45,00% | 0,97 | -0,01R | €-11,16 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 1 | 53 | 53 | 41,51% | 0,98 | -0,01R | €-6,71 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -1,10R | €-76,85 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 31 | 31 | 41,94% | 1,20 | 0,09R | €26,98 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 57 | 57 | 31,58% | 0,77 | -0,10R | €-57,44 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 49 | 49 | 32,65% | 0,80 | -0,10R | €-48,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 2 | 98 | 98 | 40,82% | 0,89 | -0,05R | €-53,79 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 6 | 174 | 174 | 37,36% | 0,87 | -0,06R | €-110,54 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 3 | 10 | 10 | 70,00% | 2,77 | 0,56R | €56,29 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 68 | 68 | 39,71% | 1,10 | 0,04R | €26,93 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 85 | 85 | 30,59% | 0,81 | -0,08R | €-72,12 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 67 | 67 | 29,85% | 0,66 | -0,19R | €-130,23 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 99 | 99 | 41,41% | 0,92 | -0,04R | €-39,90 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 204 | 204 | 40,69% | 1,04 | 0,02R | €34,65 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 3 | 10 | 10 | 70,00% | 2,77 | 0,56R | €56,29 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 70 | 70 | 41,43% | 1,21 | 0,08R | €56,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 101 | 101 | 29,70% | 0,71 | -0,14R | €-144,33 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 150 | 150 | 28,00% | 0,55 | -0,27R | €-404,71 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 5 | 239 | 239 | 39,75% | 0,86 | -0,07R | €-170,60 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 7 | 240 | 240 | 38,75% | 0,90 | -0,05R | €-118,20 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 40 | 40 | 37,50% | 0,86 | -0,07R | €-29,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 3 | 10 | 10 | 50,00% | 1,42 | 0,17R | €17,50 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 96 | 96 | 40,62% | 1,29 | 0,11R | €103,66 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 117 | 117 | 29,06% | 0,70 | -0,16R | €-183,10 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 49 | 49 | 46,94% | 1,55 | 0,20R | €97,83 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 2 | 87 | 87 | 26,44% | 0,42 | -0,39R | €-336,54 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 142 | 142 | 44,37% | 1,08 | 0,04R | €52,33 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 6 | 134 | 134 | 43,28% | 1,18 | 0,08R | €111,93 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 0,87 | -0,07R | €-11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 2 | 6 | 6 | 100,00% | ∞ | 1,01R | €60,81 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 55 | 55 | 40,00% | 1,32 | 0,11R | €63,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 67 | 67 | 29,85% | 0,68 | -0,17R | €-110,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 2 | 149 | 149 | 27,52% | 0,56 | -0,25R | €-379,40 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 5 | 242 | 242 | 40,08% | 0,98 | -0,01R | €-26,39 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 7 | 220 | 220 | 36,82% | 0,88 | -0,06R | €-133,04 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 39 | 39 | 28,21% | 0,64 | -0,20R | €-78,08 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 3 | 9 | 9 | 44,44% | 1,46 | 0,21R | €18,89 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 90 | 90 | 37,78% | 1,34 | 0,13R | €118,42 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 107 | 107 | 22,43% | 0,49 | -0,28R | €-296,86 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 25 | 23 | 44,00% | 0,88 | -0,07R | €-18,54 |
| Rapida 1H V2 | RANGE | 2 | 53 | 44 | 39,62% | 0,86 | -0,07R | €-37,42 |
| Rapida 1H V2 | TRANSITION | 0 | 9 | 9 | 55,56% | 0,95 | -0,02R | €-1,77 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 144 | 144 | 27,78% | 0,49 | -0,30R | €-436,02 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 3 | 217 | 217 | 42,40% | 1,01 | 0,00R | €6,50 |
| Rapida 1H V3 Filtered | RANGE | 7 | 215 | 215 | 38,14% | 0,90 | -0,05R | €-110,92 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 34 | 34 | 38,24% | 0,87 | -0,07R | €-23,20 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 2 | 9 | 9 | 55,56% | 1,87 | 0,31R | €27,68 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 83 | 83 | 37,35% | 1,13 | 0,05R | €44,82 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 117 | 117 | 37,61% | 0,99 | -0,00R | €-3,29 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 60 | 60 | 36,67% | 0,90 | -0,05R | €-32,12 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 116 | 116 | 29,31% | 0,49 | -0,31R | €-364,95 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 172 | 172 | 47,09% | 1,18 | 0,08R | €132,03 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 6 | 166 | 166 | 39,16% | 0,97 | -0,01R | €-24,82 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 1 | 23 | 23 | 39,13% | 0,86 | -0,07R | €-16,45 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 2 | 7 | 7 | 85,71% | 5,99 | 0,72R | €50,67 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 61 | 61 | 39,34% | 1,14 | 0,06R | €35,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 77 | 77 | 31,17% | 0,72 | -0,14R | €-111,48 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,24 | -0,58R | €-110,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 73 | 73 | 53,42% | 1,04 | 0,02R | €12,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 5 | 87 | 87 | 44,83% | 0,90 | -0,06R | €-47,90 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 37 | 37 | 59,46% | 1,63 | 0,21R | €79,27 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 55 | 55 | 50,91% | 1,02 | 0,01R | €5,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 16,67% | 0,23 | -0,58R | €-104,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 73 | 73 | 41,10% | 0,91 | -0,04R | €-32,51 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 5 | 89 | 89 | 41,57% | 0,98 | -0,01R | €-7,62 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 40,54% | 1,40 | 0,14R | €51,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 56 | 56 | 35,71% | 0,96 | -0,02R | €-9,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 51 | 51 | 25,49% | 0,40 | -0,32R | €-165,73 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 205 | 205 | 41,95% | 0,97 | -0,01R | €-29,29 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 5 | 116 | 116 | 43,10% | 1,04 | 0,02R | €24,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 54 | 54 | 40,74% | 1,31 | 0,11R | €61,61 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 76 | 76 | 35,53% | 0,90 | -0,05R | €-37,86 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 44,74% | 1,30 | 0,13R | €50,46 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 74 | 74 | 28,38% | 0,50 | -0,32R | €-236,34 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 92 | 92 | 38,04% | 0,83 | -0,09R | €-84,93 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 7 | 217 | 217 | 39,17% | 0,94 | -0,03R | €-62,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 2 | 9 | 9 | 55,56% | 1,87 | 0,31R | €27,68 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 66 | 66 | 33,33% | 0,99 | -0,01R | €-3,99 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 103 | 103 | 33,01% | 0,80 | -0,11R | €-108,47 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 143 | 143 | 27,97% | 0,50 | -0,30R | €-424,59 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 216 | 216 | 41,67% | 0,97 | -0,02R | €-34,62 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 7 | 213 | 213 | 38,03% | 0,88 | -0,06R | €-125,66 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,92 | -0,04R | €-13,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 2 | 9 | 9 | 55,56% | 1,87 | 0,31R | €27,68 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 78 | 78 | 37,18% | 1,16 | 0,06R | €47,58 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 100 | 100 | 32,00% | 0,76 | -0,13R | €-126,03 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 42,50% | 1,23 | 0,10R | €40,19 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 6 | 29 | 29 | 24,14% | 1,05 | 0,03R | €8,39 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 8 | 70 | 70 | 38,57% | 1,06 | 0,04R | €25,10 |
| SHADOW_4H_WIDE | RANGE | 5 | 76 | 76 | 15,79% | 0,66 | -0,22R | €-169,87 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 1 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 39 | 39 | 15,38% | 0,45 | -0,40R | €-156,04 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 7 | 41 | 41 | 24,39% | 1,06 | 0,04R | €15,74 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 3 | 19 | 19 | 21,05% | 0,75 | -0,17R | €-31,47 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 37 | 37 | 54,05% | 1,25 | 0,10R | €37,88 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 1 | 97 | 97 | 51,55% | 1,32 | 0,12R | €118,06 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 3 | 74 | 74 | 44,59% | 0,94 | -0,03R | €-22,24 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 60,00% | 2,25 | 0,41R | €41,08 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 15 | 15 | 60,00% | 2,13 | 0,41R | €60,85 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 43 | 43 | 41,86% | 0,82 | -0,09R | €-37,81 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 0,99 | -0,00R | €-0,60 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 0,83 | -0,08R | €-4,03 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,32 | 0,69R | €13,75 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 1,54 | 0,20R | €6,15 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 33,33% | 0,43 | -0,43R | €-25,78 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 1 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 1,28 | 0,20R | €5,87 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,28 | -0,68R | €-47,66 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,23 | -0,57R | €-17,06 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 5 | 95 | 95 | 28,42% | 0,58 | -0,26R | €-248,35 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 4 | 172 | 172 | 43,60% | 1,13 | 0,07R | €118,39 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 10 | 158 | 158 | 43,04% | 1,01 | 0,01R | €8,74 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 33 | 33 | 39,39% | 0,91 | -0,04R | €-14,24 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 2 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 81 | 81 | 40,74% | 1,34 | 0,15R | €123,63 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 75 | 75 | 34,67% | 0,89 | -0,05R | €-37,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 102 | 102 | 36,27% | 1,05 | 0,03R | €25,67 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 34 | 34 | 26,47% | 0,57 | -0,25R | €-84,35 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 164 | 164 | 43,29% | 1,10 | 0,05R | €85,67 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 5 | 77 | 77 | 50,65% | 1,38 | 0,17R | €132,41 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 44 | 44 | 43,18% | 1,81 | 0,27R | €118,35 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 61 | 61 | 29,51% | 0,62 | -0,19R | €-113,97 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 114 | 114 | 35,09% | 0,67 | -0,17R | €-189,46 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 4 | 196 | 196 | 39,29% | 0,96 | -0,02R | €-41,61 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 9 | 163 | 163 | 41,10% | 1,20 | 0,08R | €132,87 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 2 | 39 | 39 | 41,03% | 0,79 | -0,09R | €-33,46 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 2 | 11 | 11 | 36,36% | 0,59 | -0,23R | €-25,44 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 72 | 72 | 45,83% | 1,21 | 0,09R | €62,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 98 | 98 | 36,73% | 0,88 | -0,05R | €-46,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 105 | 105 | 50,48% | 1,26 | 0,11R | €114,10 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 5 | 95 | 95 | 28,42% | 0,60 | -0,24R | €-232,21 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 4 | 170 | 170 | 44,12% | 1,06 | 0,03R | €51,64 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 10 | 146 | 146 | 45,89% | 1,06 | 0,03R | €43,35 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 31 | 31 | 45,16% | 1,09 | 0,04R | €12,23 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 2 | 9 | 9 | 44,44% | 0,89 | -0,06R | €-5,61 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 64 | 64 | 45,31% | 1,27 | 0,12R | €75,68 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 75 | 75 | 38,67% | 0,90 | -0,05R | €-33,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 81 | 81 | 37,04% | 0,72 | -0,13R | €-107,93 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 39 | 39 | 33,33% | 0,79 | -0,13R | €-48,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 32 | 32 | 53,12% | 1,57 | 0,21R | €67,06 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,69 | 0,49R | €88,88 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 39 | 39 | 33,33% | 0,77 | -0,13R | €-51,40 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 32 | 32 | 40,62% | 1,37 | 0,14R | €43,41 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 55,56% | 3,14 | 0,62R | €112,49 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 23 | 23 | 21,74% | 0,25 | -0,45R | €-102,77 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 3 | 71 | 71 | 42,25% | 1,03 | 0,02R | €12,40 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 3 | 46 | 46 | 39,13% | 1,03 | 0,02R | €7,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 32 | 32 | 31,25% | 0,81 | -0,11R | €-34,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 24 | 24 | 37,50% | 1,07 | 0,03R | €6,04 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 97 | 97 | 40,21% | 1,08 | 0,04R | €36,41 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 114 | 114 | 35,96% | 0,78 | -0,10R | €-118,34 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 51 | 51 | 49,02% | 1,43 | 0,21R | €105,99 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 27 | 27 | 37,04% | 0,69 | -0,14R | €-38,44 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 1,93 | 0,35R | €31,68 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 4 | 35 | 35 | 45,71% | 1,13 | 0,07R | €24,66 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 7 | 7 | 71,43% | 5,11 | 0,67R | €47,21 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 2 | 37 | 37 | 18,92% | 0,22 | -0,57R | €-209,93 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 3 | 131 | 131 | 43,51% | 1,24 | 0,13R | €170,60 |
| SHADOW_COMBO_SCANNER | RANGE | 7 | 88 | 88 | 47,73% | 1,57 | 0,26R | €225,45 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 14 | 14 | 35,71% | 0,54 | -0,25R | €-35,18 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 63 | 63 | 41,27% | 1,61 | 0,27R | €171,33 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 69 | 69 | 28,99% | 0,96 | -0,02R | €-14,52 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 5 | 73 | 73 | 27,40% | 0,45 | -0,37R | €-268,87 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 3 | 147 | 147 | 42,86% | 1,13 | 0,07R | €105,43 |
| SHADOW_COMBO_TREND | RANGE | 12 | 136 | 136 | 36,03% | 1,11 | 0,06R | €78,93 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 24 | 24 | 37,50% | 1,18 | 0,08R | €19,31 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 3 | 7 | 7 | 42,86% | 1,33 | 0,14R | €10,03 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 70 | 70 | 34,29% | 1,18 | 0,09R | €66,11 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 67 | 67 | 29,85% | 0,70 | -0,16R | €-107,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 79 | 79 | 30,38% | 1,03 | 0,02R | €13,39 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 0,93 | -0,03R | €-1,47 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 71,29 | 0,77R | €30,62 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 1 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,06 | -0,84R | €-41,90 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,19 | -0,64R | €-25,79 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,11 | -0,66R | €-59,71 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,61R | €-42,76 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 10 | 10 | 50,00% | 1,15 | 0,08R | €8,11 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,55R | €5,45 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 50 | 50 | 20,00% | 0,39 | -0,48R | €-242,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 85 | 85 | 35,29% | 0,70 | -0,20R | €-168,40 |
| SHADOW_DONCHIAN_1H | RANGE | 8 | 71 | 71 | 33,80% | 1,03 | 0,02R | €12,83 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 28 | 28 | 39,29% | 1,47 | 0,23R | €64,33 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 41 | 41 | 26,83% | 1,03 | 0,02R | €7,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 23 | 23 | 52,17% | 1,69 | 0,35R | €80,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 17,50% | 0,24 | -0,63R | €-250,48 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 1 | 77 | 77 | 37,66% | 0,76 | -0,15R | €-117,98 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 8 | 51 | 51 | 35,29% | 0,99 | -0,00R | €-2,24 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 21 | 21 | 47,62% | 2,13 | 0,45R | €93,60 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 27 | 27 | 22,22% | 0,83 | -0,07R | €-19,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 58,82% | 2,03 | 0,44R | €75,25 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 5 | 79 | 79 | 26,58% | 0,40 | -0,41R | €-325,25 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 3 | 146 | 146 | 43,84% | 1,20 | 0,10R | €151,83 |
| SHADOW_EMA_TREND_1H | RANGE | 12 | 133 | 133 | 35,34% | 1,11 | 0,06R | €74,99 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 3 | 7 | 7 | 42,86% | 1,33 | 0,14R | €10,03 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 68 | 68 | 32,35% | 1,04 | 0,02R | €15,69 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 84 | 84 | 28,57% | 0,89 | -0,06R | €-48,54 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,55 | -0,34R | €-34,23 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,74 | -0,17R | €-8,58 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 62,50% | 3,25 | 0,61R | €48,51 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,23 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,21 | -0,60R | €-18,01 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,29 | -0,66R | €-46,36 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,55 | -0,30R | €-20,91 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 0,76 | -0,14R | €-18,29 |
| SHADOW_ETH_EMA_1H | RANGE | 1 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,57 | -0,30R | €-8,95 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,35R | €3,51 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 7 | 7 | 42,86% | 0,94 | -0,04R | €-2,75 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 34,78% | 1,09 | 0,05R | €12,63 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 3 | 46 | 46 | 34,78% | 1,04 | 0,02R | €10,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 6 | 87 | 87 | 31,03% | 0,97 | -0,02R | €-16,78 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 41 | 41 | 41,46% | 1,52 | 0,28R | €114,10 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 65 | 65 | 27,69% | 0,77 | -0,16R | €-103,17 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 33 | 33 | 54,55% | 0,92 | -0,03R | €-11,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 3 | 102 | 102 | 70,59% | 1,65 | 0,18R | €179,66 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 5 | 162 | 162 | 67,28% | 1,46 | 0,14R | €227,04 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 86 | 86 | 69,77% | 1,58 | 0,16R | €133,79 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 119 | 119 | 60,50% | 0,98 | -0,01R | €-7,11 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 33,33% | 1,11 | 0,06R | €13,44 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 7 | 88 | 88 | 32,95% | 1,06 | 0,04R | €31,77 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 40 | 40 | 37,50% | 1,28 | 0,16R | €63,73 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 76 | 76 | 26,32% | 0,72 | -0,21R | €-156,71 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 41,18% | 1,59 | 0,33R | €55,43 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 49 | 49 | 30,61% | 0,85 | -0,11R | €-51,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 5 | 77 | 77 | 31,17% | 1,14 | 0,08R | €63,67 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 37 | 37 | 37,84% | 1,33 | 0,19R | €68,83 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 61 | 61 | 22,95% | 0,63 | -0,27R | €-166,79 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,15 | -0,75R | €-104,34 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 7 | 60 | 60 | 36,67% | 1,16 | 0,10R | €60,95 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 31 | 31 | 41,94% | 1,73 | 0,35R | €107,67 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 54 | 54 | 29,63% | 0,85 | -0,10R | €-55,36 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 33,33% | 1,03 | 0,02R | €3,57 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 3 | 48 | 48 | 35,42% | 1,06 | 0,04R | €18,54 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 5 | 81 | 81 | 33,33% | 1,10 | 0,06R | €47,44 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 40 | 40 | 37,50% | 1,28 | 0,16R | €64,16 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 64 | 64 | 23,44% | 0,62 | -0,28R | €-181,57 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 7 | 93 | 93 | 29,03% | 0,59 | -0,25R | €-233,24 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 4 | 167 | 167 | 41,92% | 1,18 | 0,10R | €160,07 |
| Forza relativa 1H V1 | RANGE | 8 | 180 | 180 | 30,56% | 0,82 | -0,10R | €-178,67 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 29 | 29 | 27,59% | 0,49 | -0,28R | €-81,70 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,68 |
| Forza relativa 1H V1 | TRANSITION | 1 | 81 | 81 | 35,80% | 1,31 | 0,16R | €128,39 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 75 | 75 | 28,00% | 0,87 | -0,07R | €-51,18 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 103 | 103 | 26,21% | 0,88 | -0,07R | €-67,74 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 27,27% | 0,81 | -0,12R | €-39,63 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 3 | 41 | 39 | 34,15% | 0,53 | -0,28R | €-113,51 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 3 | 63 | 58 | 47,62% | 1,66 | 0,31R | €197,99 |
| Forza relativa 1H V2 | RANGE | 6 | 81 | 78 | 33,33% | 0,91 | -0,05R | €-40,49 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 7 | 6 | 28,57% | 0,87 | -0,06R | €-4,22 |
| Forza relativa 1H V2 | TRANSITION | 0 | 46 | 41 | 36,96% | 1,48 | 0,24R | €109,19 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 35 | 34 | 28,57% | 0,95 | -0,02R | €-7,36 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 41 | 37 | 46,34% | 1,70 | 0,32R | €131,11 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 61 | 61 | 16,39% | 0,21 | -0,60R | €-367,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 8 | 71 | 71 | 25,35% | 0,43 | -0,30R | €-212,33 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 24 | 24 | 45,83% | 1,34 | 0,18R | €42,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 61 | 61 | 16,39% | 0,21 | -0,60R | €-367,60 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 8 | 71 | 71 | 25,35% | 0,43 | -0,30R | €-212,33 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 24 | 24 | 45,83% | 1,34 | 0,18R | €42,90 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 61 | 61 | 16,39% | 0,21 | -0,60R | €-367,60 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 8 | 71 | 71 | 25,35% | 0,43 | -0,30R | €-212,33 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 24 | 24 | 45,83% | 1,34 | 0,18R | €42,90 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 54 | 54 | 22,22% | 0,39 | -0,42R | €-228,68 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 46,67% | 1,70 | 0,29R | €44,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 7 | 84 | 84 | 28,57% | 0,66 | -0,18R | €-147,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 19 | 19 | 47,37% | 1,39 | 0,15R | €28,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 40 | 40 | 40,00% | 1,11 | 0,06R | €24,19 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 2 | 62 | 62 | 41,94% | 0,43 | -0,32R | €-200,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 45,45% | 1,12 | 0,06R | €6,29 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 8 | 85 | 85 | 58,82% | 0,84 | -0,06R | €-50,69 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 23 | 23 | 65,22% | 1,43 | 0,16R | €35,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 31 | 31 | 61,29% | 1,51 | 0,21R | €65,37 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 2 | 53 | 53 | 37,74% | 0,27 | -0,44R | €-234,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,55 | 0,22R | €28,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 8 | 79 | 79 | 59,49% | 0,61 | -0,15R | €-114,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 21 | 21 | 61,90% | 1,24 | 0,10R | €20,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 30 | 30 | 63,33% | 1,77 | 0,30R | €89,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 2 | 31 | 31 | 32,26% | 0,64 | -0,20R | €-62,50 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 4 | 171 | 171 | 42,11% | 1,04 | 0,02R | €38,91 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 6 | 69 | 69 | 52,17% | 1,54 | 0,22R | €152,80 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 48 | 48 | 37,50% | 1,46 | 0,17R | €80,53 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 57 | 57 | 26,32% | 0,52 | -0,25R | €-142,81 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 2 | 31 | 31 | 32,26% | 0,64 | -0,20R | €-62,44 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 174 | 174 | 43,10% | 1,05 | 0,02R | €43,15 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 6 | 69 | 69 | 52,17% | 1,54 | 0,22R | €152,80 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 48 | 48 | 37,50% | 1,46 | 0,17R | €80,53 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 57 | 57 | 26,32% | 0,52 | -0,25R | €-142,81 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 2 | 31 | 31 | 32,26% | 0,64 | -0,20R | €-62,44 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 174 | 174 | 43,10% | 1,05 | 0,02R | €43,15 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 6 | 69 | 69 | 52,17% | 1,54 | 0,22R | €152,80 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 48 | 48 | 37,50% | 1,46 | 0,17R | €80,53 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 57 | 57 | 26,32% | 0,52 | -0,25R | €-142,81 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 2 | 34 | 34 | 20,59% | 0,25 | -0,52R | €-177,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 3 | 131 | 131 | 43,51% | 1,24 | 0,13R | €171,19 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 6 | 81 | 81 | 48,15% | 1,67 | 0,29R | €237,50 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 58 | 58 | 39,66% | 1,60 | 0,27R | €156,64 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 68 | 68 | 27,94% | 0,91 | -0,05R | €-35,23 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 6,25% | 0,04 | -0,82R | €-131,23 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 1 | 52 | 52 | 34,62% | 0,77 | -0,15R | €-75,79 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 2 | 6 | 6 | 16,67% | 0,08 | -0,84R | €-50,21 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 25 | 25 | 48,00% | 2,20 | 0,45R | €111,32 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 55 | 55 | 25,45% | 0,71 | -0,16R | €-88,97 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 28 | 28 | 17,86% | 0,17 | -0,58R | €-163,20 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 66 | 66 | 33,33% | 0,79 | -0,13R | €-86,04 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 7 | 77 | 77 | 46,75% | 1,48 | 0,22R | €171,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 45 | 45 | 44,44% | 2,26 | 0,43R | €195,33 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 49 | 49 | 18,37% | 0,43 | -0,34R | €-168,64 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 25 | 25 | 28,00% | 0,45 | -0,25R | €-62,51 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 38,33% | 0,95 | -0,02R | €-14,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 7 | 95 | 95 | 45,26% | 1,49 | 0,19R | €177,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,63 | -0,15R | €-29,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 46 | 46 | 45,65% | 1,21 | 0,09R | €39,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 49 | 49 | 48,98% | 1,15 | 0,07R | €33,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 0,38 | -0,38R | €-18,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 22 | 22 | 22,73% | 0,17 | -0,54R | €-118,82 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 34,00% | 0,92 | -0,05R | €-24,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 8 | 80 | 80 | 48,75% | 1,57 | 0,25R | €201,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,47 | -0,31R | €-45,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 42 | 42 | 35,71% | 1,52 | 0,22R | €91,50 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 38 | 38 | 21,05% | 0,57 | -0,25R | €-93,78 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,85R | €-51,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 32 | 32 | 34,38% | 0,55 | -0,21R | €-68,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 2 | 131 | 131 | 42,75% | 1,16 | 0,07R | €93,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 6 | 96 | 96 | 45,83% | 1,53 | 0,20R | €189,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,63 | -0,15R | €-29,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 49 | 49 | 42,86% | 1,15 | 0,06R | €29,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 55 | 55 | 49,09% | 1,22 | 0,09R | €49,40 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 22,22% | 0,21 | -0,54R | €-144,62 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 2 | 108 | 108 | 46,30% | 1,44 | 0,22R | €242,01 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 7 | 79 | 79 | 49,37% | 1,63 | 0,27R | €214,40 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,47 | -0,31R | €-45,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 44 | 44 | 34,09% | 1,36 | 0,16R | €71,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 43 | 43 | 20,93% | 0,61 | -0,22R | €-94,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 41 | 41 | 34,15% | 0,51 | -0,22R | €-90,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 3 | 152 | 152 | 41,45% | 0,99 | -0,01R | €-9,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 5 | 88 | 88 | 46,59% | 1,55 | 0,21R | €181,81 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 1 | 17 | 17 | 29,41% | 0,61 | -0,16R | €-26,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 55 | 55 | 45,45% | 1,23 | 0,09R | €51,51 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 68 | 68 | 48,53% | 1,18 | 0,07R | €49,16 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 27 | 27 | 25,93% | 0,33 | -0,46R | €-123,58 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 131 | 131 | 42,75% | 1,25 | 0,13R | €174,42 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 6 | 72 | 72 | 45,83% | 1,57 | 0,26R | €187,50 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 47 | 47 | 38,30% | 1,58 | 0,24R | €114,40 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 51 | 51 | 19,61% | 0,52 | -0,27R | €-136,82 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 2 | 26 | 26 | 23,08% | 0,25 | -0,53R | €-138,05 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 124 | 124 | 41,94% | 1,24 | 0,13R | €159,02 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 6 | 66 | 66 | 43,94% | 1,54 | 0,26R | €173,39 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 41 | 41 | 36,59% | 1,84 | 0,32R | €131,54 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 50 | 50 | 22,00% | 0,64 | -0,19R | €-95,97 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 2 | 40 | 40 | 27,50% | 0,47 | -0,33R | €-130,84 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 3 | 137 | 137 | 41,61% | 1,07 | 0,04R | €52,99 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 6 | 83 | 83 | 50,60% | 1,62 | 0,26R | €217,99 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 61 | 61 | 39,34% | 1,51 | 0,21R | €126,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 87 | 87 | 35,63% | 1,06 | 0,03R | €25,24 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,10R | €-65,85 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 60,00% | 2,05 | 0,45R | €45,46 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 9 | 9 | 44,44% | 0,83 | -0,10R | €-9,30 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 100,00% | ∞ | 1,14R | €34,32 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 80,00% | 2,30 | 0,28R | €13,97 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,41 | -0,45R | €-45,27 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 6 | 6 | 33,33% | 0,60 | -0,30R | €-18,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,51 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,16 | -0,75R | €-37,55 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 50,00% | 1,36 | 0,20R | €15,94 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 7 | 7 | 71,43% | 2,92 | 0,62R | €43,29 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,72R | €27,23 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,20 | 0,10R | €2,07 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-54,77 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 66,67% | 2,76 | 0,63R | €56,57 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 8 | 8 | 37,50% | 1,02 | 0,01R | €1,11 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 1,81 | 0,28R | €8,45 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-02T07:09:16+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **480**
- Scenari virtuali ancora attivi: **11162**
- Gruppi in attesa dell'uscita originale: **418**
- Gruppi con originale chiuso ma Shadow ancora attive: **62**
- Confronti completati: **467662**

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

Generato: 2026-09-02T07:11:23+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **467662**
- Valutazioni prodotte: **27397**
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

# Forward Exit Challengers — verifica pulita

Generato: 2026-09-02T07:16:30+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Operativo | Identità | Gross cert. | Net cert. | Pending | Gap | Conflict | Formal review NET | PF storico | PnL storico | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,16 | +€67,59 | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,01 | +€2,56 | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,11 | +€95,26 | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,09 | +€75,72 | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | 90 | 110 | 24 | 0 | 10 | 75 | 1 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,55 | +€846,28 | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | 38 | 67 | 19 | 0 | 11 | 35 | 2 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 5,77 | +€1.682,13 | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | 154 | 158 | 28 | 0 | 6 | 121 | 3 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,65 | +€1.253,39 | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 0,00 | €0,00 | COLLECTING |

## Regole di valutazione

- Il campione operativo resta esposto per continuità storica, ma non è il campione formale.
- La soglia 50 usa esclusivamente NET_CERTIFIED_CLOSED_PAIRS.
- P0C produce FORMAL_CERTIFIED_OUTCOME; Block-3 produce SIMULATION_RUNTIME_OUTCOME.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-02T07:06:15+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **20**
- Simulazioni bloccate attive: **25**
- Simulazioni completate nel ciclo: **9**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **673.92 R**
- Profitto virtuale mancato: **1359.31 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 297 | 0 | 19791.45 |
| DOWN_20 | 297 | 0 | 39582.91 |
| DOWN_30 | 297 | 2 | 59376.50 |
| DOWN_40 | 297 | 101 | 73835.94 |
| UP_10 | 117 | 0 | 11398.04 |
| UP_20 | 117 | 0 | 22796.08 |
| UP_30 | 117 | 0 | 34194.12 |
| UP_40 | 117 | 42 | 41414.19 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-02T07:05:19+00:00

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

Generato: 2026-09-02T07:16:40+00:00

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

Generato: 2026-09-02T07:16:40+00:00

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

Generato: 2026-09-02T07:16:40+00:00

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

Generato: 2026-09-02T07:16:40+00:00

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
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 22.9 | E | 135 | 1.54 | 0.260 | 20.77 |
| 2 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 22.1 | E | 42 | 1.97 | 0.421 | 4.71 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 20.9 | E | 172 | 1.25 | 0.120 | 22.59 |
| 4 | SHADOW_COMBO_ADAPTIVE | BASELINE | 19.7 | E | 180 | 1.20 | 0.100 | 22.09 |
| 5 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 19.2 | E | 208 | 1.11 | 0.056 | 30.08 |
| 6 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 18.8 | E | 258 | 1.12 | 0.062 | 31.78 |
| 7 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | BASELINE | 18.5 | E | 166 | 1.08 | 0.047 | 22.70 |
| 8 | SHADOW_1H_FAST_V3 | BASELINE | 18.4 | E | 252 | 1.10 | 0.049 | 29.54 |
| 9 | SHADOW_DONCHIAN_1H | BASELINE | 18.4 | E | 121 | 1.31 | 0.179 | 17.21 |
| 10 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 17.9 | E | 137 | 1.14 | 0.078 | 21.13 |

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

Generato: 2026-09-02T07:16:40+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **1100**
- Strategie preferite nel regime corrente: **5**
- Strategie da evitare nel regime corrente: **4**
- Memorie contestuali: **525**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | shadow-combo-trend-side-regime-guard-v1 | OBSERVING | 82.9 | 16 | 4.19 | 0.900 | 2.10 |
| 2 | SHADOW_1H_FAST | shadow-1h-fast | COMPATIBLE | 81.7 | 33 | 1.98 | 0.336 | 2.65 |
| 3 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.089 | 0.00 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | momentum_breakout_v3_filtered | INSUFFICIENT | 80.5 | 5 | 6.05 | 1.042 | 1.03 |
| 5 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | momentum_breakout_v3_filtered | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.959 | 0.00 |
| 6 | SHADOW_SOL_ADAPTIVE_4H | shadow-sol-adaptive-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.682 | 0.00 |
| 7 | SHADOW_SOL_DONCHIAN_4H | shadow-sol-donchian-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.744 | 0.00 |
| 8 | EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | momentum_breakout_v3_filtered | INSUFFICIENT | 78.9 | 5 | 15.19 | 1.196 | 0.42 |
| 9 | MAIN_SIDE_REGIME_GUARD_V1 | main-side-regime-guard-v1 | INSUFFICIENT | 77.3 | 8 | 7.87 | 0.930 | 1.03 |
| 10 | SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | shadow-combo-adaptive-long-only-v1 | OBSERVING | 75.7 | 19 | 1.90 | 0.410 | 3.25 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-02T07:16:41+00:00

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

Generato: 2026-09-02T07:06:15+00:00

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
