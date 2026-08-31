# Paper trading automatico KuCoin

Generato: 2026-08-31T02:15:11+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-31T02:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-31T02:05:31+00:00 | 2026-08-31T02:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-31T01:45:00+00:00 | 2026-08-31T01:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-31T01:00:00+00:00 | 2026-08-31T01:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-30T20:00:00+00:00 | 2026-08-30T20:00:00+00:00 | 2,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sol Adaptive 1H | SOL | 60m | SHORT | -6,31 | 5,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 1H | SOL | 60m | SHORT | -6,31 | 5,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Ema 1H | SOL | 60m | SHORT | -6,31 | 5,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Btc Ema 1H | BTC | 60m | SHORT | -5,75 | 5,00 | 0,00 | OPENED | 5,7 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Quality7 | XMR | 60m | LONG | 7,10 | 7,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | SKR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,85 | 6,00 | 1,15 | STALE_CANDLE | 2,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -4,52 | 6,00 | 1,48 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,73 | 6,00 | 3,27 | STALE_CANDLE | 2,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,50 | 6,00 | 4,50 | STALE_CANDLE | 2,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,30 | 6,00 | 4,70 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 0,75 | 6,00 | 5,25 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,53 | 6,00 | 5,47 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,32 | 6,00 | 5,68 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Rapida V1 — senza PEPE | DOGE | 60m | SHORT | -7,52 | 4,50 | 0,00 | OPENED | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom 5 Short 1H | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom10 Short | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom15 Short | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom20 Short | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — madre | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — parziale 1R | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | 60m | SHORT | -7,52 | 5,00 | 0,00 | READY | 5,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | XMR | 60m | LONG | 7,10 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.807,72 | -1,92% | €59,37 | €3.000,00 | 1,98% | 6 | 55 | 40,00% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 55 | 2570 | PRIME INDICAZIONI | 100 (mancano 45) |

- Trade del Principale 4H chiusi: **55**; win rate **40,00%**; profit factor **0,87**.
- Expectancy: **€-3,43** per trade; P&L netto: **€-188,91**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.807,72 | €699,80 | €2.099,39 | €196,16 | €-2,26 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.416,30 | €3.844,50 | €7.689,00 | €172,07 | €90,69 |
| TEST | Rapida score 6–7,5 — Cost Aware | 6 | €11.271,39 | €1.972,37 | €5.917,10 | €225,24 | €10,71 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.147,51 | €3.753,99 | €7.507,97 | €168,02 | €88,56 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.960,45 | €2.518,60 | €5.037,21 | €111,50 | €71,16 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.905,48 | €1.470,51 | €2.941,02 | €217,32 | €-11,73 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.832,48 | €709,59 | €2.128,78 | €216,87 | €-47,91 |
| TEST | Rapida V1 — senza PEPE | 8 | €10.532,96 | €2.163,53 | €6.490,59 | €210,66 | €36,84 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.469,25 | €1.977,46 | €5.932,39 | €209,15 | €13,89 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.401,99 | €1.964,76 | €5.894,27 | €207,80 | €13,80 |
| TEST | Combo Adaptive — madre | 6 | €10.362,71 | €3.644,93 | €7.289,85 | €208,07 | €-40,43 |
| TEST | Rapida V3 NoHigh — Regime Guard | 3 | €10.357,35 | €318,57 | €955,71 | €103,80 | €0,00 |
| TEST | Combo Adaptive — Long Only | 5 | €10.349,08 | €2.522,24 | €5.044,48 | €206,79 | €-2,27 |
| TEST | Sol Donchian 1H | 0 | €10.333,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 1 | €10.315,19 | €740,69 | €2.222,07 | €51,20 | €0,00 |
| TEST | Ampia 4H | 8 | €10.305,80 | €1.071,19 | €2.142,37 | €207,40 | €26,14 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €10.282,28 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 1 | €10.222,39 | €739,04 | €2.217,11 | €51,09 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.217,25 | €943,74 | €2.831,23 | €101,77 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.209,82 | €407,92 | €815,83 | €51,22 | €-33,03 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.194,24 | €1.375,42 | €2.750,84 | €203,03 | €-10,97 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 5 | €10.178,12 | €1.434,27 | €4.302,82 | €153,04 | €13,08 |
| TEST | Sol Ema 1H | 1 | €10.175,95 | €828,58 | €2.485,73 | €50,89 | €-0,50 |
| TEST | Sol Donchian 4H | 1 | €10.174,34 | €449,62 | €899,24 | €50,98 | €-21,69 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.158,68 | €2.487,49 | €4.974,98 | €151,52 | €-11,43 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.129,18 | €2.597,73 | €5.195,46 | €202,37 | €-11,06 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.094,01 | €830,52 | €2.491,56 | €50,43 | €9,45 |
| TEST | Btc Bollinger 4H | 1 | €10.081,85 | €775,58 | €1.551,16 | €0,00 | €52,18 |
| TEST | Sol Ema 4H | 1 | €10.073,11 | €439,17 | €878,34 | €50,55 | €-35,56 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.064,91 | €1.984,50 | €3.969,00 | €151,45 | €-0,59 |
| TEST | Sol Adaptive 1H | 1 | €10.055,11 | €818,74 | €2.456,21 | €50,29 | €-0,49 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €10.043,24 | €2.011,34 | €4.022,68 | €200,72 | €-2,20 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €10.037,37 | €2.010,16 | €4.020,33 | €200,60 | €-2,20 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 1 | €10.029,43 | €154,73 | €773,67 | €10,03 | €1,22 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.021,41 | €140,98 | €422,93 | €50,75 | €-36,37 |
| TEST | Doge Donchian 1H | 0 | €10.021,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 2 | €10.003,72 | €280,86 | €842,57 | €100,28 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 1 | €9.999,47 | €10,00 | €150,00 | €1,94 | €0,24 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 1 | €9.997,37 | €50,00 | €750,00 | €9,72 | €1,18 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 1 | €9.990,08 | €10,00 | €150,00 | €0,75 | €-0,28 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.985,48 | €997,92 | €2.993,77 | €50,02 | €-16,74 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 1 | €9.982,55 | €400,80 | €2.004,00 | €9,99 | €-3,73 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.980,84 | €478,97 | €957,94 | €0,00 | €50,96 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.960,49 | €1.296,50 | €3.889,51 | €49,79 | €5,68 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 1 | €9.950,40 | €50,00 | €750,00 | €3,74 | €-1,39 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €9.936,33 | €857,68 | €2.573,04 | €151,82 | €-2,80 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.887,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.857,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.853,05 | €1.179,97 | €2.359,93 | €148,73 | €11,64 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.836,97 | €961,21 | €2.883,62 | €49,20 | €-0,58 |
| TEST | Scanner Top15 Long | 6 | €9.834,32 | €2.419,46 | €4.838,93 | €195,45 | €-12,85 |
| TEST | Scanner Top20 Long | 6 | €9.834,32 | €2.419,46 | €4.838,93 | €195,45 | €-12,85 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.816,06 | €2.255,54 | €4.511,08 | €195,59 | €7,04 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2 | €9.807,05 | €728,45 | €2.185,35 | €97,43 | €-2,76 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €9.805,78 | €983,82 | €2.951,45 | €142,78 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.783,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.768,62 | €964,56 | €1.929,13 | €0,00 | €89,49 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 2 | €9.754,78 | €273,87 | €821,61 | €97,79 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.752,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 5 | €9.735,13 | €1.380,10 | €4.140,29 | €194,06 | €-2,74 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.703,60 | €1.816,76 | €5.450,29 | €194,03 | €-17,03 |
| TEST | Btc Ema 1H | 1 | €9.670,48 | €1.119,58 | €3.358,74 | €48,37 | €-0,67 |
| TEST | Eth Bollinger 1H | 0 | €9.649,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.647,31 | €1.132,87 | €3.398,61 | €192,95 | €-0,13 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.619,67 | €1.439,13 | €4.317,40 | €192,17 | €12,92 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.590,48 | €362,84 | €1.088,52 | €96,64 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.556,60 | €1.289,39 | €2.578,78 | €190,33 | €-10,28 |
| TEST | Combo Adaptive — Trend/Transition | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Top 5 + BTC — Guard | 4 | €9.534,09 | €1.074,48 | €2.148,96 | €144,02 | €-10,23 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.513,80 | €2.341,06 | €4.682,13 | €190,30 | €-6,86 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.428,71 | €235,01 | €470,01 | €49,36 | €-0,22 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 3 | €9.418,69 | €234,76 | €469,51 | €49,30 | €-0,22 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 3 | €9.382,25 | €233,85 | €467,70 | €49,11 | €-0,22 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.370,56 | €1.341,06 | €2.682,13 | €140,82 | €-0,20 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.317,29 | €354,62 | €1.063,86 | €94,46 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.312,36 | €1.049,49 | €2.098,99 | €140,67 | €-9,99 |
| TEST | Bilanciata 1H V2 | 1 | €9.279,70 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 4 | €9.264,55 | €1.111,87 | €2.223,74 | €101,16 | €-1,55 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.258,45 | €230,80 | €461,59 | €48,47 | €-0,21 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 3 | €9.210,85 | €440,80 | €881,59 | €89,62 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.177,83 | €1.718,32 | €5.154,97 | €183,52 | €-16,11 |
| TEST | Combo Adaptive — MFE Trail esistente | 6 | €9.173,50 | €2.196,00 | €4.392,00 | €183,45 | €1,79 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 2 | €9.163,81 | €202,91 | €405,81 | €45,03 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.163,43 | €1.423,81 | €2.847,61 | €95,92 | €50,75 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.151,97 | €417,79 | €835,58 | €91,85 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 5 | €9.148,53 | €2.696,38 | €5.392,76 | €91,45 | €63,23 |
| TEST | Top 5 + BTC — BTC 2–3 | 1 | €9.148,37 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €8.909,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €8.823,89 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.705,70 | €408,40 | €816,80 | €87,39 | €-0,46 |
| TEST | Top 5 + BTC — BTC≤3 | 1 | €8.701,51 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.807,72 | €-188,91 | 55 | 55 | 40,00% | 0,87 | €-3,43 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.416,30 | €1.328,45 | 115 | 115 | 46,96% | 1,52 | €11,55 | 6,75% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.271,39 | €1.264,35 | 162 | 162 | 52,47% | 1,39 | €7,80 | 5,23% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.147,51 | €1.061,73 | 83 | 83 | 45,78% | 1,63 | €12,79 | 6,75% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.960,45 | €891,35 | 129 | 129 | 51,94% | 1,37 | €6,91 | 6,42% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.905,48 | €919,00 | 154 | 154 | 47,40% | 1,32 | €5,97 | 8,85% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.832,48 | €882,05 | 41 | 41 | 56,10% | 2,24 | €21,51 | 3,82% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.532,96 | €499,84 | 243 | 243 | 45,68% | 1,11 | €2,06 | 7,86% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.469,25 | €459,03 | 204 | 204 | 50,00% | 1,14 | €2,25 | 9,50% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.401,99 | €391,84 | 248 | 248 | 44,76% | 1,09 | €1,58 | 9,48% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.362,71 | €407,51 | 170 | 170 | 45,29% | 1,14 | €2,40 | 7,91% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.357,35 | €357,91 | 90 | 90 | 47,78% | 1,20 | €3,98 | 5,24% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.349,08 | €354,38 | 139 | 139 | 46,04% | 1,12 | €2,55 | 7,78% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.333,40 | €333,40 | 16 | 16 | 62,50% | 2,35 | €20,84 | 2,77% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.315,19 | €316,33 | 52 | 52 | 48,08% | 1,26 | €6,08 | 3,97% |
| TEST | Ampia 4H | Confluenza trend | €10.305,80 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.282,28 | €283,43 | 54 | 49 | 48,15% | 1,22 | €5,25 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.222,39 | €223,53 | 77 | 77 | 49,35% | 1,13 | €2,90 | 4,50% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.217,25 | €218,75 | 42 | 42 | 45,24% | 1,21 | €5,21 | 3,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.209,82 | €243,28 | 8 | 8 | 62,50% | 3,16 | €30,41 | 1,01% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.194,24 | €206,88 | 137 | 137 | 44,53% | 1,07 | €1,51 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.178,12 | €167,62 | 243 | 243 | 39,51% | 1,04 | €0,69 | 6,56% |
| TEST | Sol Ema 1H | Trend following EMA | €10.175,95 | €177,93 | 17 | 17 | 47,06% | 1,41 | €10,47 | 3,33% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.174,34 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.158,68 | €173,06 | 133 | 133 | 46,62% | 1,06 | €1,30 | 8,68% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.129,18 | €143,36 | 147 | 147 | 46,94% | 1,06 | €0,98 | 10,31% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.094,01 | €86,06 | 18 | 18 | 61,11% | 1,21 | €4,78 | 2,77% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.081,85 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Sol Ema 4H | Trend following EMA | €10.073,11 | €109,13 | 9 | 9 | 44,44% | 1,51 | €12,13 | 2,27% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.064,91 | €67,87 | 163 | 163 | 44,79% | 1,03 | €0,42 | 8,69% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.055,11 | €57,07 | 19 | 19 | 47,37% | 1,11 | €3,00 | 4,59% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.043,24 | €47,86 | 122 | 122 | 40,16% | 1,02 | €0,39 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.037,37 | €41,98 | 126 | 126 | 40,48% | 1,02 | €0,33 | 12,06% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.029,43 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.021,41 | €58,16 | 15 | 15 | 33,33% | 1,13 | €3,88 | 3,39% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.021,07 | €21,07 | 14 | 14 | 57,14% | 1,06 | €1,51 | 3,08% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.003,72 | €4,23 | 172 | 172 | 40,70% | 1,00 | €0,02 | 7,31% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,47 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.997,37 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,08 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.985,48 | €4,01 | 11 | 11 | 54,55% | 1,01 | €0,36 | 1,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.982,55 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,84 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.960,49 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.950,40 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.936,33 | €-59,33 | 184 | 184 | 42,39% | 0,99 | €-0,32 | 10,60% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,30 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.857,66 | €-142,34 | 16 | 16 | 43,75% | 0,72 | €-8,90 | 3,14% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.853,05 | €-157,18 | 127 | 120 | 41,73% | 0,95 | €-1,24 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.836,97 | €-160,72 | 13 | 13 | 38,46% | 0,68 | €-12,36 | 2,91% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.834,32 | €-149,89 | 146 | 146 | 46,58% | 0,94 | €-1,03 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.834,32 | €-149,89 | 146 | 146 | 46,58% | 0,94 | €-1,03 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Scanner | Combo Scanner | €9.816,06 | €-188,25 | 145 | 145 | 44,14% | 0,94 | €-1,30 | 11,38% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.807,05 | €-188,87 | 89 | 89 | 40,45% | 0,91 | €-2,12 | 4,20% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.805,78 | €-192,73 | 145 | 145 | 43,45% | 0,94 | €-1,33 | 7,10% |
| TEST | Eth Ema 1H | Trend following EMA | €9.783,55 | €-216,45 | 22 | 22 | 40,91% | 0,71 | €-9,84 | 4,80% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.768,62 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.754,78 | €-244,72 | 136 | 136 | 38,97% | 0,90 | €-1,80 | 7,31% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.752,59 | €-247,41 | 15 | 15 | 33,33% | 0,59 | €-16,49 | 3,74% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.735,13 | €-259,65 | 191 | 191 | 41,36% | 0,93 | €-1,36 | 12,52% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.703,60 | €-276,31 | 170 | 170 | 40,59% | 0,92 | €-1,63 | 9,70% |
| TEST | Btc Ema 1H | Trend following EMA | €9.670,48 | €-326,84 | 16 | 16 | 25,00% | 0,45 | €-20,43 | 3,40% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.649,49 | €-350,51 | 8 | 8 | 25,00% | 0,19 | €-43,81 | 4,16% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.647,31 | €-350,46 | 114 | 114 | 43,86% | 0,84 | €-3,07 | 9,26% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.619,67 | €-390,54 | 216 | 216 | 42,59% | 0,91 | €-1,81 | 9,00% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.590,48 | €-408,86 | 111 | 111 | 41,44% | 0,86 | €-3,68 | 6,64% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.556,60 | €-431,55 | 129 | 129 | 43,41% | 0,83 | €-3,35 | 12,28% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.534,09 | €-454,39 | 122 | 122 | 37,70% | 0,85 | €-3,72 | 7,34% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.513,80 | €-476,53 | 95 | 95 | 38,95% | 0,79 | €-5,02 | 8,88% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.428,71 | €-570,79 | 80 | 80 | 30,00% | 0,76 | €-7,13 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.418,69 | €-580,81 | 75 | 75 | 33,33% | 0,75 | €-7,74 | 7,98% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.382,25 | €-617,25 | 77 | 77 | 32,47% | 0,75 | €-8,02 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.370,56 | €-627,64 | 80 | 80 | 35,00% | 0,73 | €-7,85 | 7,96% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.317,29 | €-682,07 | 114 | 114 | 42,98% | 0,79 | €-5,98 | 8,22% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.312,36 | €-676,39 | 139 | 139 | 38,85% | 0,79 | €-4,87 | 8,78% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.279,70 | €-719,48 | 124 | 112 | 41,94% | 0,74 | €-5,80 | 10,25% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.264,55 | €-731,22 | 67 | 67 | 29,85% | 0,68 | €-10,91 | 8,18% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.258,45 | €-741,06 | 111 | 111 | 45,05% | 0,72 | €-6,68 | 9,02% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.210,85 | €-788,62 | 68 | 68 | 23,53% | 0,65 | €-11,60 | 11,41% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.177,83 | €-803,17 | 124 | 124 | 40,32% | 0,69 | €-6,48 | 9,43% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.173,50 | €-825,67 | 181 | 181 | 40,88% | 0,76 | €-4,56 | 15,45% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.163,81 | €-835,95 | 79 | 79 | 31,65% | 0,68 | €-10,58 | 8,62% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.163,43 | €-886,37 | 132 | 132 | 36,36% | 0,67 | €-6,71 | 12,31% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.151,97 | €-847,53 | 85 | 85 | 35,29% | 0,67 | €-9,97 | 10,89% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Combo Trend | Combo Trend | €9.148,53 | €-912,22 | 168 | 168 | 37,50% | 0,77 | €-5,43 | 10,98% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.148,37 | €-850,56 | 37 | 37 | 21,62% | 0,33 | €-22,99 | 9,89% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.909,65 | €-1.090,35 | 96 | 96 | 34,38% | 0,61 | €-11,36 | 10,90% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.823,89 | €-1.174,82 | 50 | 50 | 34,00% | 0,44 | €-23,50 | 13,49% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.705,70 | €-1.293,35 | 70 | 70 | 25,71% | 0,56 | €-18,48 | 13,24% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.701,51 | €-1.297,48 | 83 | 83 | 30,12% | 0,48 | €-15,63 | 14,88% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,34389 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-2,06 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,15403 | 5,11600 | 4,78412 | 3,46179 | 5,89386 | €9,32 | €27,96 | €2,01 | €-0,21 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | UNI | LONG | Confluenza trend | 60m | 3,0x | 5,12502 | 5,11600 | 4,91893 | 3,44231 | 5,53722 | €24,33 | €72,99 | €2,94 | €-0,13 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 5,22905 | 5,11600 | 5,03952 | 3,51218 | 5,60809 | €434,79 | €1.304,38 | €47,28 | €-28,20 |
| Bilanciata 1H V3 Filtered | ENA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,14884 | 0,14723 | 0,15578 | 0,19771 | 0,13496 | €346,84 | €1.040,52 | €48,51 | €11,26 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 80,12897 | 80,28700 | 81,74951 | 106,43798 | 76,88789 | €14,83 | €44,49 | €0,90 | €-0,09 |
| Rapida score 6–7,5 — Range Only | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| Rapida score 6–7,5 — Range Only | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14884 | 0,14723 | 0,15424 | 0,19771 | 0,14074 | €517,69 | €1.553,08 | €56,32 | €16,80 |
| Rapida score 6–7,5 — Cost Aware | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 80,12897 | 80,28700 | 81,38939 | 106,43798 | 78,23834 | €1.029,86 | €3.089,57 | €48,60 | €-6,09 |
| Rapida V1 — no HIGH + score <7,5 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 5,12502 | 5,11600 | 4,96473 | 3,44231 | 5,36547 | €522,78 | €1.568,34 | €49,05 | €-2,76 |
| Rapida V1 — senza PEPE | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| Rapida V1 — senza PEPE | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| Rapida V1 — senza PEPE | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| Rapida V1 — senza PEPE | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,35993 | 1,34389 | 1,38296 | 1,80644 | 1,32537 | €1.032,92 | €3.098,76 | €52,49 | €36,54 |
| Rapida V1 — senza PEPE | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14884 | 0,14723 | 0,15424 | 0,19771 | 0,14074 | €9,98 | €29,94 | €1,09 | €0,32 |
| Rapida V1 — senza PEPE | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08162 | 0,08167 | 0,08292 | 0,10842 | 0,07967 | €15,66 | €46,99 | €0,75 | €-0,03 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| Rapida V1 — target pieno 2R | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| Rapida V1 — target pieno 2R | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08203 | 0,08167 | 0,08331 | 0,10896 | 0,07947 | €991,70 | €2.975,10 | €46,39 | €13,08 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered — madre | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered — madre | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08203 | 0,08167 | 0,08331 | 0,10896 | 0,08011 | €1.045,77 | €3.137,32 | €48,92 | €13,80 |
| Rapida V3 — no volatilità HIGH | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| Rapida V3 — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| Rapida V3 — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| Rapida V3 — Long Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 5,12502 | 5,11600 | 4,96473 | 3,44231 | 5,36547 | €518,95 | €1.556,84 | €48,69 | €-2,74 |
| Rapida V3 — Long + no HIGH + score <7,5 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| Rapida V3 — senza ESPORTS | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| Rapida V3 — senza ESPORTS | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| Rapida V3 — senza ESPORTS | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08203 | 0,08167 | 0,08331 | 0,10896 | 0,08011 | €979,04 | €2.937,11 | €45,80 | €12,92 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 5,12502 | 5,11600 | 4,96473 | 3,44231 | 5,36547 | €529,67 | €1.589,01 | €49,70 | €-2,80 |
| Rapida V3 senza ESPORTS — MFE Lock | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08203 | 0,08167 | 0,08331 | 0,10896 | 0,08011 | €1.052,54 | €3.157,62 | €49,24 | €13,89 |
| Rapida V3 senza ESPORTS — Stress Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| Rapida V3 — qualità completa + profit lock | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| Rapida V3 — qualità completa + profit lock | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2413,98000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,25 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 80,28700 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,34 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08167 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €26,63 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 101,57500 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,58 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | ENA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14884 | 0,14723 | 0,15578 | 0,22252 | 0,13357 | €527,76 | €1.055,51 | €49,21 | €11,42 |
| Forza relativa 1H V2 | DOGE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,08198 | 0,08167 | 0,08364 | 0,12256 | 0,07833 | €28,81 | €57,63 | €1,17 | €0,22 |
| Scalp RSI Long 20 · €10 · 15x | HYPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 80,16103 | 80,28700 | 79,12194 | 75,21777 | 81,71966 | €10,00 | €150,00 | €1,94 | €0,24 |
| Scalp RSI Long 25 · €10 · 15x | BTC | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 77765,81005 | 77621,20000 | 77378,24314 | 72970,25177 | 78347,16081 | €10,00 | €150,00 | €0,75 | €-0,28 |
| Scalp RSI Long 20 · €50 · 15x | HYPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 80,16103 | 80,28700 | 79,12194 | 75,21777 | 81,71966 | €50,00 | €750,00 | €9,72 | €1,18 |
| Scalp RSI Long 25 · €50 · 15x | BTC | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 77765,81005 | 77621,20000 | 77378,24314 | 72970,25177 | 78347,16081 | €50,00 | €750,00 | €3,74 | €-1,39 |
| Scalp RSI Long 20 · prudente · 5x | HYPE | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 80,16103 | 80,28700 | 79,12194 | 64,52963 | 82,23920 | €154,73 | €773,67 | €10,03 | €1,22 |
| Scalp RSI Long 25 · prudente · 5x | BTC | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 77765,81005 | 77621,20000 | 77378,24314 | 62601,47709 | 78540,94465 | €400,80 | €2.004,00 | €9,99 | €-3,73 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08518 | 0,08167 | 0,08330 | 0,12735 | 0,07945 | €1.039,92 | €2.079,84 | €0,00 | €85,77 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 77734,70995 | 77621,20000 | 78978,46531 | 116213,39137 | 74625,32155 | €1.781,81 | €3.563,61 | €57,02 | €5,20 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 80,12897 | 80,28700 | 81,92957 | 119,79281 | 75,62746 | €71,42 | €142,84 | €3,21 | €-0,28 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08518 | 0,08167 | 0,08330 | 0,12735 | 0,07945 | €1.015,44 | €2.030,87 | €0,00 | €83,75 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 77734,70995 | 77621,20000 | 78978,46531 | 116213,39137 | 74625,32155 | €1.739,86 | €3.479,71 | €55,68 | €5,08 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 80,12897 | 80,28700 | 81,92957 | 119,79281 | 75,62746 | €69,74 | €139,47 | €3,13 | €-0,28 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,08437 | 0,08167 | 0,08318 | 0,12614 | 0,07944 | €800,03 | €1.600,05 | €0,00 | €51,26 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €55,06 | €110,11 | €4,09 | €-0,51 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 533,45802 | €767,40 | €1.534,80 | €54,13 | €-11,73 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 533,45802 | €719,05 | €1.438,09 | €50,72 | €-10,99 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,53722 | €19,51 | €39,02 | €1,57 | €-0,07 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 533,45802 | €700,00 | €1.399,99 | €49,38 | €-10,70 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,53722 | €610,91 | €1.221,82 | €49,13 | €-2,15 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 533,45802 | €700,00 | €1.399,99 | €49,38 | €-10,70 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,53722 | €610,91 | €1.221,82 | €49,13 | €-2,15 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 536,97294 | €717,36 | €1.434,72 | €50,60 | €-10,97 |
| Top 5 + BTC — solo MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Top 5 + BTC — solo MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Top 5 + BTC — solo MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 536,97294 | €672,49 | €1.344,98 | €47,44 | €-10,28 |
| Top 5 + BTC — Guard | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Top 5 + BTC — Guard | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Top 5 + BTC — Guard | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Top 5 + BTC — Guard | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 536,97294 | €669,15 | €1.338,30 | €47,20 | €-10,23 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Top 5 + BTC — BTC 2–3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Top 5 + BTC — Guard + MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Top 5 + BTC — Guard + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Top 5 + BTC — Guard + MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Top 5 + BTC — Guard + MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 498,30881 | 494,50000 | 480,73420 | 251,64595 | 536,97294 | €653,59 | €1.307,18 | €46,10 | €-9,99 |
| Top 5 + BTC — Guard + BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,74332 | €624,18 | €1.248,36 | €50,20 | €-2,20 |
| Top 5 + BTC — target pieno 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Top 5 + BTC — target pieno 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,74332 | €624,55 | €1.249,09 | €50,23 | €-2,20 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08564 | 0,08167 | 0,08308 | 0,12804 | 0,08027 | €964,56 | €1.929,13 | €0,00 | €89,49 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08437 | 0,08167 | 0,08318 | 0,12614 | 0,07944 | €840,25 | €1.680,50 | €0,00 | €53,84 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | ENA | SHORT | Combo Trend | 60m | 2,0x | 0,14884 | 0,14723 | 0,15655 | 0,22252 | 0,13188 | €440,69 | €881,38 | €45,66 | €9,54 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €15,91 | €31,83 | €1,18 | €-0,15 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,08198 | 0,08167 | 0,08364 | 0,12256 | 0,07833 | €1.211,83 | €2.423,66 | €49,06 | €9,19 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,57844 | €609,76 | €1.219,51 | €49,04 | €-2,15 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive — madre | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive — madre | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €778,20 | €1.556,40 | €52,04 | €-7,23 |
| Combo Adaptive — madre | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 80,12897 | 80,28700 | 81,74951 | 119,79281 | 76,88789 | €1.286,30 | €2.572,60 | €52,03 | €-5,07 |
| Combo Adaptive — madre | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,36047 | 1,34389 | 1,33084 | 0,68704 | 1,41973 | €1.153,55 | €2.307,10 | €50,25 | €-28,12 |
| Combo Adaptive — MFE Trail esistente | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive — MFE Trail esistente | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €685,98 | €1.371,95 | €45,87 | €-6,38 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08203 | 0,08167 | 0,08368 | 0,12264 | 0,07874 | €928,21 | €1.856,43 | €37,22 | €8,16 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive — Quality7 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €712,04 | €1.424,09 | €47,61 | €-6,62 |
| Combo Adaptive — Quality7 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 494,59890 | 494,50000 | 475,91469 | 249,77244 | 531,96731 | €610,55 | €1.221,11 | €46,13 | €-0,24 |
| Combo Adaptive — Trend/Transition | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive — Long Only | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive — Long Only | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,12502 | 5,11600 | 4,91893 | 2,58814 | 5,53722 | €643,56 | €1.287,13 | €51,76 | €-2,27 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive — parziale 1R | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive — parziale 1R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €63,65 | €127,30 | €4,26 | €-0,59 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77605,67576 | 77621,20000 | 78723,19749 | 103086,20597 | 75370,63230 | €1.119,58 | €3.358,74 | €48,37 | €-0,67 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 77734,70995 | 77621,20000 | 78729,71424 | 103257,60638 | 75744,70137 | €1.296,50 | €3.889,51 | €49,79 | €5,68 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 77621,20000 | 79375,01684 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €52,18 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 101,55469 | 101,57500 | 103,63379 | 134,89847 | 97,39648 | €828,58 | €2.485,73 | €50,89 | €-0,50 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 105,86117 | 101,57500 | 99,76922 | 53,45989 | 121,09104 | €439,17 | €878,34 | €50,55 | €-35,56 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 101,57500 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €-21,69 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 101,59531 | 101,57500 | 99,86203 | 68,23819 | 104,19524 | €961,21 | €2.883,62 | €49,20 | €-0,58 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 101,57500 | 105,65046 | 160,38740 | 97,27311 | €478,97 | €957,94 | €0,00 | €50,96 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 101,55469 | 101,57500 | 103,63379 | 134,89847 | 97,39648 | €818,74 | €2.456,21 | €50,29 | €-0,49 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,86117 | 101,57500 | 99,21540 | 53,45989 | 122,47558 | €407,92 | €815,83 | €51,22 | €-33,03 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08198 | 0,08167 | 0,08364 | 0,10890 | 0,07866 | €830,52 | €2.491,56 | €50,43 | €9,45 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08213 | 0,08167 | 0,08076 | 0,05516 | 0,08419 | €997,92 | €2.993,77 | €50,02 | €-16,74 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 5,15209 | 5,11600 | 4,98477 | 2,60181 | 5,48672 | €15,52 | €31,05 | €1,01 | €-0,22 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 5,19712 | 5,11600 | 5,03154 | 2,62454 | 5,52827 | €14,75 | €29,50 | €0,94 | €-0,46 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 5,15209 | 5,11600 | 4,98477 | 2,60181 | 5,48672 | €14,01 | €28,02 | €0,91 | €-0,20 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 5,15209 | 5,11600 | 4,98477 | 2,60181 | 5,48672 | €15,32 | €30,64 | €0,99 | €-0,21 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,28700 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €-1,55 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive — Side × Regime Guard | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 80,12897 | 80,28700 | 81,74951 | 119,79281 | 76,88789 | €1.257,47 | €2.514,94 | €50,86 | €-4,96 |
| Combo Adaptive — Side × Regime Guard | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €743,49 | €1.486,98 | €48,90 | €-6,47 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 5,15209 | 5,11600 | 4,98477 | 2,60181 | 5,48672 | €15,60 | €31,20 | €1,01 | €-0,22 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 5,15209 | 5,11600 | 4,98477 | 2,60181 | 5,48672 | €15,58 | €31,17 | €1,01 | €-0,22 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Rapida V3 NoHigh — Range Only | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,34389 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-3,31 |
| MAIN — Side × Regime Guard | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2413,98000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,29 |
| MAIN — Side × Regime Guard | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,14723 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €-38,81 |
| MAIN — Side × Regime Guard | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,15403 | 5,11600 | 4,78412 | 3,46179 | 5,89386 | €248,23 | €744,68 | €53,45 | €-5,49 |
| MAIN — Dynamic Asset Selector | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,14723 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €-36,37 |
| Combo Trend — Side × Regime Guard | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08437 | 0,08167 | 0,08318 | 0,12614 | 0,07944 | €1.036,98 | €2.073,96 | €0,00 | €66,44 |
| Combo Trend — Side × Regime Guard | ENA | SHORT | Combo Trend | 60m | 2,0x | 0,14884 | 0,14723 | 0,15655 | 0,22252 | 0,13188 | €528,31 | €1.056,62 | €54,74 | €11,43 |
| Combo Trend — Side × Regime Guard | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €722,64 | €1.445,27 | €53,69 | €-6,72 |
| FAST NoHigh <7,5 · SHORT only | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| Bilanciata V3 · LONG only | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 5,22905 | 5,11600 | 5,03952 | 3,51218 | 5,60809 | €411,23 | €1.233,70 | €44,71 | €-26,67 |
| Bilanciata V3 · LONG only | ENA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,14884 | 0,14723 | 0,15578 | 0,19771 | 0,13496 | €328,05 | €984,14 | €45,88 | €10,65 |
| Bilanciata V3 · LONG only | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 80,12897 | 80,28700 | 81,74951 | 106,43798 | 76,88789 | €14,03 | €42,08 | €0,85 | €-0,08 |
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
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | 2026-08-31T00:00:00+00:00 | 0,00000 | €135,22 | 2,48 | TARGET |
| Benchmark Donchian breakout 1H | PEPE | SHORT | 2026-08-31T00:00:00+00:00 | 0,00000 | €138,49 | 2,48 | TARGET |
| Doge Ema 1H | DOGE | SHORT | 2026-08-31T00:00:00+00:00 | 0,08111 | €97,21 | 1,95 | TARGET |
| Combo Trend — Side × Regime Guard | UNI | LONG | 2026-08-31T00:00:00+00:00 | 5,06349 | €-56,64 | -1,03 | STOP |
| Forza relativa 1H V2 | UNI | LONG | 2026-08-30T23:45:00+00:00 | 5,07303 | €-1,26 | -1,04 | STOP |
| Master Adaptive V1 | ZEC | LONG | 2026-08-30T23:45:00+00:00 | 841,95022 | €-49,43 | -1,06 | STOP |
| Master Adaptive V1 | ENA | LONG | 2026-08-30T23:45:00+00:00 | 0,14795 | €-48,67 | -1,02 | STOP |
| Master Adaptive Strict3 V1 | ZEC | LONG | 2026-08-30T23:45:00+00:00 | 841,95022 | €-46,18 | -1,06 | STOP |
| Master Adaptive Gb20 V1 | ZEC | LONG | 2026-08-30T23:45:00+00:00 | 841,95022 | €-48,77 | -1,06 | STOP |
| Master Adaptive Gb20 V1 | ENA | LONG | 2026-08-30T23:45:00+00:00 | 0,14795 | €-48,02 | -1,02 | STOP |
| Master Adaptive GB20 — 50% a 0,75R | ZEC | LONG | 2026-08-30T23:45:00+00:00 | 841,95022 | €-49,62 | -1,06 | STOP |
| Master Adaptive GB20 — 50% a 0,75R | ENA | LONG | 2026-08-30T23:45:00+00:00 | 0,14795 | €-48,85 | -1,02 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 597/30 | 33/30 | 0,89 | 2,04 | -0,06R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 553/30 | 20/30 | 0,85 | 1,90 | -0,07R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 259/30 | 22/30 | 0,89 | 1,74 | -0,06R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 262/30 | 22/30 | 0,83 | 1,57 | -0,08R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 518/30 | 31/30 | 0,94 | 0,62 | -0,03R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 475/30 | 11/30 | 0,92 | 0,00 | -0,04R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 142/30 | 8/30 | 0,82 | 1,02 | -0,09R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 335/30 | 17/30 | 0,69 | 4,50 | -0,17R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 516/30 | 24/30 | 0,74 | 0,64 | -0,14R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 475/30 | 7/30 | 0,66 | 0,02 | -0,18R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 518/30 | 30/30 | 0,96 | 1,02 | -0,02R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 850/30 | 55/30 | 0,91 | 1,12 | -0,04R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 168/30 | 15/30 | 0,62 | 0,99 | -0,24R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 749/30 | 44/30 | 0,82 | 1,20 | -0,09R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 753/30 | 37/30 | 0,82 | 0,76 | -0,09R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 695/30 | 23/30 | 0,77 | 1,12 | -0,11R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 357/30 | 55/30 | 0,77 | 0,87 | -0,14R | €-3,43 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 15/30 | 0,00 | 1,13 | 0,00R | €3,88 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 41/30 | 0,00 | 2,24 | 0,00R | €21,51 | 3,82% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 27/30 | 15/30 | 0,48 | 0,83 | -0,29R | €-0,83 | 0,71% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 50/30 | 28/30 | 0,67 | 0,60 | -0,18R | €-2,16 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 894/30 | 121/30 | 0,93 | 0,69 | -0,04R | €-7,02 | 13,99% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 114/30 | 0,00 | 0,84 | 0,00R | €-3,07 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 293/30 | 112/30 | 1,18 | 0,74 | 0,09R | €-5,80 | 10,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 563/30 | 170/30 | 1,02 | 0,92 | 0,01R | €-1,63 | 9,70% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 484/30 | 124/30 | 0,96 | 0,69 | -0,02R | €-6,48 | 9,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 263/30 | 89/30 | 0,89 | 0,91 | -0,05R | €-2,12 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 546/30 | 136/30 | 0,85 | 0,90 | -0,07R | €-1,80 | 7,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 613/30 | 172/30 | 0,88 | 1,00 | -0,06R | €0,02 | 7,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1000/30 | 243/30 | 0,83 | 1,11 | -0,08R | €2,06 | 7,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 162/30 | 0,00 | 1,39 | 0,00R | €7,80 | 5,23% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 95/30 | 0,00 | 0,72 | 0,00R | €-8,78 | 12,64% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 42/30 | 0,00 | 1,21 | 0,00R | €5,21 | 3,79% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 569/30 | 137/30 | 0,93 | 0,84 | -0,04R | €-4,26 | 12,33% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 961/30 | 243/30 | 0,83 | 1,04 | -0,08R | €0,69 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 71/30 | 49/30 | 0,87 | 1,22 | -0,07R | €5,25 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 928/30 | 248/30 | 0,86 | 1,09 | -0,07R | €1,58 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 696/30 | 136/30 | 0,92 | 0,75 | -0,04R | €-6,57 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 304/30 | 114/30 | 0,97 | 0,79 | -0,01R | €-5,98 | 8,22% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 307/30 | 111/30 | 0,93 | 0,86 | -0,03R | €-3,68 | 6,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 595/30 | 191/30 | 0,95 | 0,93 | -0,02R | €-1,36 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 52/30 | 0,00 | 1,26 | 0,00R | €6,08 | 3,97% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 90/30 | 0,00 | 1,20 | 0,00R | €3,98 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 628/30 | 145/30 | 0,80 | 0,94 | -0,11R | €-1,33 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 184/30 | 0,00 | 0,99 | 0,00R | €-0,32 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 204/30 | 0,00 | 1,14 | 0,00R | €2,25 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 77/30 | 0,00 | 1,13 | 0,00R | €2,90 | 4,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 881/30 | 216/30 | 0,84 | 0,91 | -0,08R | €-1,81 | 9,00% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 337/30 | 52/30 | 0,85 | 1,24 | -0,09R | €5,39 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 304/30 | 81/30 | 1,17 | 0,55 | 0,08R | €-15,55 | 14,60% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 15/30 | 9/30 | 0,64 | 0,86 | -0,19R | €-3,49 | 1,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 3/30 | 3/30 | 1,15 | 1,17 | 0,10R | €5,87 | 0,96% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 9/30 | 6/30 | 3,40 | 4,66 | 0,60R | €34,87 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 2/30 | 2/30 | 1,56 | 1,54 | 0,31R | €14,72 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 17/30 | 10/30 | 0,32 | 0,85 | -0,54R | €-4,29 | 1,49% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 7/30 | 5/30 | 0,42 | 0,61 | -0,53R | €-17,29 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 22/30 | 16/30 | 0,63 | 0,45 | -0,24R | €-20,43 | 3,40% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 5/30 | 4/30 | 0,56 | 0,78 | -0,37R | €-8,28 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 738/30 | 170/30 | 1,01 | 1,14 | 0,01R | €2,40 | 7,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 463/30 | 139/30 | 1,06 | 1,12 | 0,03R | €2,55 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 812/30 | 181/30 | 1,01 | 0,76 | 0,01R | €-4,56 | 15,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 679/30 | 163/30 | 0,96 | 1,03 | -0,02R | €0,42 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 89/30 | 46/30 | 1,27 | 0,79 | 0,12R | €-5,95 | 4,21% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 89/30 | 46/30 | 1,26 | 0,69 | 0,12R | €-8,61 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 241/30 | 95/30 | 0,97 | 0,79 | -0,01R | €-5,02 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 261/30 | 77/30 | 1,00 | 0,76 | 0,00R | €-5,94 | 5,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 94/30 | 0,74 | 0,53 | -0,20R | €-11,02 | 12,67% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 133/30 | 0,00 | 1,06 | 0,00R | €1,30 | 8,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 75/30 | 0,74 | 0,38 | -0,20R | €-16,04 | 12,67% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 111/30 | 50/30 | 1,17 | 0,44 | 0,08R | €-23,50 | 13,49% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 467/30 | 145/30 | 1,10 | 0,94 | 0,05R | €-1,30 | 11,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 610/30 | 168/30 | 1,00 | 0,77 | -0,00R | €-5,43 | 10,98% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 129/30 | 0,00 | 1,37 | 0,00R | €6,91 | 6,42% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 14/30 | 11/30 | 1,83 | 1,01 | 0,27R | €0,36 | 1,89% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 18/30 | 14/30 | 0,61 | 1,06 | -0,26R | €1,51 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 29/30 | 18/30 | 0,52 | 1,21 | -0,33R | €4,78 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 323/30 | 115/30 | 0,88 | 1,52 | -0,08R | €11,55 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 253/30 | 83/30 | 0,88 | 1,63 | -0,07R | €12,79 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 619/30 | 132/30 | 0,99 | 0,67 | -0,00R | €-6,71 | 12,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 25/30 | 16/30 | 0,59 | 0,72 | -0,29R | €-8,90 | 3,14% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 17/30 | 8/30 | 1,75 | 0,19 | 0,30R | €-43,81 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 23/30 | 15/30 | 0,48 | 0,59 | -0,40R | €-16,49 | 3,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 35/30 | 22/30 | 0,53 | 0,71 | -0,33R | €-9,84 | 4,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 6/30 | 7/30 | 0,46 | 0,57 | -0,38R | €-16,10 | 1,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 14/30 | 17/30 | 0,90 | 0,41 | -0,07R | €-18,86 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 312/30 | 80/30 | 1,02 | 0,73 | 0,01R | €-7,85 | 7,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 80/30 | 0,00 | 0,76 | 0,00R | €-7,13 | 8,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 68/30 | 0,00 | 0,65 | 0,00R | €-11,60 | 11,41% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 75/30 | 0,00 | 0,75 | 0,00R | €-7,74 | 7,98% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 578/30 | 111/30 | 1,34 | 0,72 | 0,11R | €-6,68 | 9,02% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 273/30 | 79/30 | 1,03 | 0,68 | 0,02R | €-10,58 | 8,62% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 285/30 | 67/30 | 1,01 | 0,68 | 0,01R | €-10,91 | 8,18% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 197/30 | 70/30 | 0,93 | 0,56 | -0,05R | €-18,48 | 13,24% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 299/30 | 77/30 | 1,00 | 0,75 | -0,00R | €-8,02 | 7,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 742/30 | 105/30 | 0,93 | 0,47 | -0,04R | €-14,80 | 17,39% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 288/30 | 120/30 | 1,20 | 0,95 | 0,10R | €-1,24 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 236/30 | 70/30 | 0,53 | 0,65 | -0,27R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 236/30 | 70/30 | 0,53 | 0,65 | -0,27R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 236/30 | 70/30 | 0,53 | 0,65 | -0,27R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 268/30 | 89/30 | 0,68 | 0,64 | -0,18R | €-9,30 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 280/30 | 61/30 | 0,78 | 0,58 | -0,10R | €-12,17 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 252/30 | 62/30 | 0,70 | 0,56 | -0,14R | €-12,20 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 460/30 | 147/30 | 1,05 | 1,06 | 0,02R | €0,98 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 461/30 | 146/30 | 1,04 | 0,94 | 0,02R | €-1,03 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 461/30 | 146/30 | 1,04 | 0,94 | 0,02R | €-1,03 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 452/30 | 137/30 | 1,10 | 1,07 | 0,05R | €1,51 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 161/30 | 37/30 | 0,71 | 0,33 | -0,18R | €-22,99 | 9,89% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 333/30 | 83/30 | 0,87 | 0,48 | -0,07R | €-15,63 | 14,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 349/30 | 96/30 | 1,08 | 0,61 | 0,03R | €-11,36 | 10,90% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 294/30 | 85/30 | 0,95 | 0,67 | -0,03R | €-9,97 | 10,89% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 449/30 | 139/30 | 1,15 | 0,79 | 0,07R | €-4,87 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 369/30 | 122/30 | 1,10 | 0,85 | 0,05R | €-3,72 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 504/30 | 129/30 | 1,06 | 0,83 | 0,03R | €-3,35 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 399/30 | 126/30 | 1,04 | 1,02 | 0,02R | €0,33 | 12,06% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 376/30 | 122/30 | 1,07 | 1,02 | 0,03R | €0,39 | 11,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 498/30 | 154/30 | 1,12 | 1,32 | 0,06R | €5,97 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 33/30 | 19/30 | 0,84 | 1,11 | -0,11R | €3,00 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 9/30 | 8/30 | 2,54 | 3,16 | 0,54R | €30,41 | 1,01% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 24/30 | 13/30 | 0,79 | 0,68 | -0,12R | €-12,36 | 2,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 5/30 | 4/30 | 1,99 | 0,56 | 0,41R | €-17,33 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 27/30 | 16/30 | 1,10 | 2,35 | 0,06R | €20,84 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 7/30 | 6/30 | 1,26 | 2,73 | 0,16R | €32,74 | 1,05% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 30/30 | 17/30 | 0,99 | 1,41 | -0,01R | €10,47 | 3,33% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 10/30 | 9/30 | 0,85 | 1,51 | -0,10R | €12,13 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08167**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 30.2 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 77621.2 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, stop_within_limit**
- High **0.08188**; close **0.08155**; wick alta **35.0%**; volume **x0.25**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=476; LEGACY_RESEARCH_EVIDENCE_V3=3889; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_DOWN**
- Famiglia: **ALT_ROTATION**
- Confidenza: **90,00%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -2.92%, 64% sotto -1%.
- BTC trend score: **1,00**; ADX: **19,11**; breadth sopra EMA50: **25,00%**
- Mediana alt vs BTC: **-2,92%**; dispersione: **48,07%**

- Aperti in questo ciclo: **76**
- Chiusi in questo ciclo: **2**
- Posizioni research aperte: **823**
- Trade research chiusi: **36123**
- Eventi di mercato indipendenti chiusi: **4846**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **94430**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 17 | 597 | 597 | 36,01% | 0,89 | -0,06R | €-333,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 17 | 553 | 553 | 35,26% | 0,85 | -0,07R | €-407,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 2 | 259 | 259 | 47,88% | 0,89 | -0,06R | €-143,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 2 | 262 | 262 | 35,11% | 0,83 | -0,08R | €-214,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 7 | 518 | 518 | 36,87% | 0,94 | -0,03R | €-157,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 7 | 475 | 475 | 37,26% | 0,92 | -0,04R | €-181,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 1 | 142 | 142 | 36,62% | 0,82 | -0,09R | €-122,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 3 | 335 | 335 | 30,15% | 0,69 | -0,17R | €-569,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 6 | 516 | 516 | 31,20% | 0,74 | -0,14R | €-704,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 6 | 475 | 475 | 30,11% | 0,66 | -0,18R | €-844,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 7 | 518 | 518 | 37,26% | 0,96 | -0,02R | €-97,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 17 | 850 | 850 | 40,71% | 0,91 | -0,04R | €-354,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 168 | 168 | 34,52% | 0,62 | -0,24R | €-395,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 18 | 749 | 749 | 33,38% | 0,82 | -0,09R | €-679,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 18 | 753 | 753 | 33,33% | 0,82 | -0,09R | €-679,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 18 | 695 | 695 | 32,81% | 0,77 | -0,11R | €-794,64 |
| MAIN | 20 | 357 | 357 | 28,57% | 0,77 | -0,14R | €-482,05 |
| RSI_EXTREME_LONG_15M | 1 | 27 | 27 | 40,74% | 0,48 | -0,29R | €-78,32 |
| RSI_EXTREME_SHORT_15M | 0 | 50 | 50 | 38,00% | 0,67 | -0,18R | €-87,69 |
| Bilanciata 1H V1 | 24 | 894 | 894 | 35,91% | 0,93 | -0,04R | €-341,64 |
| Bilanciata 1H V2 | 3 | 337 | 293 | 40,95% | 1,18 | 0,09R | €308,36 |
| Bilanciata 1H V3 Filtered | 18 | 563 | 563 | 37,66% | 1,02 | 0,01R | €55,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 18 | 484 | 484 | 37,40% | 0,96 | -0,02R | €-90,22 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 4 | 263 | 263 | 38,78% | 0,89 | -0,05R | €-143,85 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 8 | 546 | 546 | 35,90% | 0,85 | -0,07R | €-401,66 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 8 | 613 | 613 | 36,70% | 0,88 | -0,06R | €-367,32 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 20 | 1000 | 1000 | 36,20% | 0,83 | -0,08R | €-844,02 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 17 | 569 | 569 | 38,66% | 0,93 | -0,04R | €-207,32 |
| SHADOW_1H_FAST_TP2_V1 | 21 | 961 | 961 | 33,92% | 0,83 | -0,08R | €-814,25 |
| Rapida 1H V2 | 1 | 81 | 71 | 43,21% | 0,87 | -0,07R | €-53,27 |
| Rapida 1H V3 Filtered | 18 | 928 | 928 | 36,85% | 0,86 | -0,07R | €-641,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 17 | 696 | 696 | 39,08% | 0,92 | -0,04R | €-277,06 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 304 | 304 | 49,01% | 0,97 | -0,01R | €-41,12 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 307 | 307 | 38,76% | 0,93 | -0,03R | €-97,83 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 7 | 595 | 595 | 39,66% | 0,95 | -0,02R | €-136,88 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 6 | 628 | 628 | 34,71% | 0,80 | -0,11R | €-660,74 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 18 | 881 | 881 | 36,32% | 0,84 | -0,08R | €-722,96 |
| SHADOW_4H_WIDE | 31 | 337 | 337 | 24,33% | 0,85 | -0,09R | €-317,66 |
| SHADOW_BOLLINGER_MR_1H | 9 | 304 | 304 | 48,68% | 1,17 | 0,08R | €228,21 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 15 | 15 | 46,67% | 0,64 | -0,19R | €-28,10 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 3 | 3 | 33,33% | 1,15 | 0,10R | €3,08 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 9 | 9 | 77,78% | 3,40 | 0,60R | €54,38 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 17 | 17 | 29,41% | 0,32 | -0,54R | €-91,62 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 7 | 7 | 14,29% | 0,42 | -0,53R | €-37,20 |
| SHADOW_BTC_EMA_1H | 1 | 22 | 22 | 40,91% | 0,63 | -0,24R | €-52,80 |
| SHADOW_BTC_EMA_4H | 0 | 5 | 5 | 20,00% | 0,56 | -0,37R | €-18,62 |
| SHADOW_COMBO_ADAPTIVE | 20 | 738 | 738 | 38,75% | 1,01 | 0,01R | €42,24 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 8 | 463 | 463 | 39,74% | 1,06 | 0,03R | €128,92 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 19 | 812 | 812 | 41,63% | 1,01 | 0,01R | €48,03 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 20 | 679 | 679 | 40,94% | 0,96 | -0,02R | €-141,29 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 89 | 89 | 46,07% | 1,27 | 0,12R | €107,17 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 89 | 89 | 40,45% | 1,26 | 0,12R | €104,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 6 | 241 | 241 | 36,93% | 0,97 | -0,01R | €-32,50 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 2 | 261 | 261 | 39,85% | 1,00 | 0,00R | €4,52 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 6 | 111 | 111 | 47,75% | 1,17 | 0,08R | €87,35 |
| SHADOW_COMBO_SCANNER | 8 | 467 | 467 | 37,69% | 1,10 | 0,05R | €246,07 |
| SHADOW_COMBO_TREND | 21 | 610 | 610 | 35,57% | 1,00 | -0,00R | €-10,04 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 14 | 14 | 64,29% | 1,83 | 0,27R | €37,37 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 18 | 18 | 38,89% | 0,61 | -0,26R | €-47,65 |
| SHADOW_DOGE_EMA_1H | 1 | 29 | 29 | 31,03% | 0,52 | -0,33R | €-94,74 |
| SHADOW_DONCHIAN_1H | 13 | 323 | 323 | 33,44% | 0,88 | -0,08R | €-245,50 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 13 | 253 | 253 | 35,57% | 0,88 | -0,07R | €-180,42 |
| SHADOW_EMA_TREND_1H | 22 | 619 | 619 | 35,54% | 0,99 | -0,00R | €-18,42 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 25 | 25 | 36,00% | 0,59 | -0,29R | €-71,29 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 17 | 17 | 58,82% | 1,75 | 0,30R | €50,23 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 23 | 23 | 30,43% | 0,48 | -0,40R | €-92,96 |
| SHADOW_ETH_EMA_1H | 0 | 35 | 35 | 37,14% | 0,53 | -0,33R | €-114,81 |
| SHADOW_ETH_EMA_4H | 1 | 6 | 6 | 33,33% | 0,46 | -0,38R | €-22,83 |
| SHADOW_GLOBAL_PURE | 1 | 14 | 14 | 42,86% | 0,90 | -0,07R | €-9,14 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 4 | 312 | 312 | 33,01% | 1,02 | 0,01R | €44,19 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 4 | 578 | 578 | 66,26% | 1,34 | 0,11R | €636,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 4 | 273 | 273 | 32,97% | 1,03 | 0,02R | €50,35 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 4 | 285 | 285 | 31,58% | 1,01 | 0,01R | €17,80 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 2 | 197 | 197 | 30,96% | 0,93 | -0,05R | €-90,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | 4 | 299 | 299 | 32,44% | 1,00 | -0,00R | €-8,73 |
| Forza relativa 1H V1 | 25 | 742 | 742 | 32,48% | 0,93 | -0,04R | €-295,52 |
| Forza relativa 1H V2 | 13 | 310 | 288 | 38,71% | 1,20 | 0,10R | €305,66 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 15 | 236 | 236 | 27,12% | 0,53 | -0,27R | €-631,58 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 15 | 236 | 236 | 27,12% | 0,53 | -0,27R | €-631,58 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 15 | 236 | 236 | 27,12% | 0,53 | -0,27R | €-631,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 14 | 268 | 268 | 29,48% | 0,68 | -0,18R | €-476,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 14 | 280 | 280 | 52,86% | 0,78 | -0,10R | €-268,63 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 14 | 252 | 252 | 51,59% | 0,70 | -0,14R | €-340,54 |
| SHADOW_SCANNER_TOP10_LONG | 8 | 460 | 460 | 38,91% | 1,05 | 0,02R | €104,43 |
| SHADOW_SCANNER_TOP15_LONG | 8 | 461 | 461 | 39,05% | 1,04 | 0,02R | €101,49 |
| SHADOW_SCANNER_TOP20_LONG | 8 | 461 | 461 | 39,05% | 1,04 | 0,02R | €101,49 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 452 | 452 | 37,17% | 1,10 | 0,05R | €244,66 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 2 | 161 | 161 | 29,19% | 0,71 | -0,18R | €-282,75 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 6 | 333 | 333 | 32,73% | 0,87 | -0,07R | €-237,59 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 3 | 349 | 349 | 43,27% | 1,08 | 0,03R | €114,05 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 3 | 294 | 294 | 34,35% | 0,95 | -0,03R | €-77,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 449 | 449 | 44,54% | 1,15 | 0,07R | €292,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 369 | 369 | 37,67% | 1,10 | 0,05R | €199,57 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 504 | 504 | 43,45% | 1,06 | 0,03R | €128,71 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 399 | 399 | 36,09% | 1,04 | 0,02R | €91,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 376 | 376 | 35,64% | 1,07 | 0,03R | €128,69 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 498 | 498 | 38,76% | 1,12 | 0,06R | €307,68 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 33 | 33 | 39,39% | 0,84 | -0,11R | €-35,04 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 9 | 9 | 66,67% | 2,54 | 0,54R | €48,91 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 24 | 24 | 45,83% | 0,79 | -0,12R | €-29,47 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 5 | 5 | 60,00% | 1,99 | 0,41R | €20,58 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 27 | 27 | 48,15% | 1,10 | 0,06R | €15,78 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 7 | 7 | 42,86% | 1,26 | 0,16R | €10,86 |
| SHADOW_SOL_EMA_1H | 1 | 30 | 30 | 40,00% | 0,99 | -0,01R | €-2,44 |
| SHADOW_SOL_EMA_4H | 1 | 10 | 10 | 40,00% | 0,85 | -0,10R | €-9,83 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 10 | 78 | 78 | 30,77% | 0,57 | -0,25R | €-194,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 3 | 153 | 153 | 45,75% | 1,24 | 0,11R | €162,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 2 | 125 | 125 | 34,40% | 0,71 | -0,15R | €-182,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,71 | -0,15R | €-28,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 2 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 58 | 58 | 34,48% | 1,17 | 0,07R | €40,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 59 | 59 | 22,03% | 0,47 | -0,26R | €-153,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 10 | 72 | 72 | 30,56% | 0,45 | -0,34R | €-245,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 3 | 135 | 135 | 44,44% | 1,23 | 0,10R | €135,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 2 | 118 | 118 | 33,90% | 0,65 | -0,18R | €-209,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,69 | -0,17R | €-30,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 2 | 5 | 5 | 80,00% | 5,04 | 0,82R | €41,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 57 | 57 | 35,09% | 1,25 | 0,10R | €57,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 56 | 56 | 21,43% | 0,36 | -0,33R | €-185,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 12 | 12 | 41,67% | 0,62 | -0,24R | €-28,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 61 | 61 | 52,46% | 1,21 | 0,10R | €63,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 70 | 70 | 41,43% | 0,60 | -0,24R | €-169,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 36 | 36 | 58,33% | 1,46 | 0,17R | €62,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 44 | 44 | 45,45% | 0,79 | -0,10R | €-44,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,66 | -0,20R | €-21,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 63 | 63 | 39,68% | 1,03 | 0,01R | €8,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 1 | 73 | 73 | 35,62% | 0,60 | -0,22R | €-162,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 36 | 36 | 33,33% | 1,25 | 0,09R | €31,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 43 | 43 | 30,23% | 0,81 | -0,08R | €-32,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 2 | 29 | 29 | 34,48% | 0,61 | -0,18R | €-50,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 3 | 181 | 181 | 39,78% | 0,96 | -0,02R | €-32,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 1 | 94 | 94 | 37,23% | 0,78 | -0,11R | €-107,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 50 | 50 | 34,00% | 1,29 | 0,11R | €55,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 63 | 63 | 31,75% | 0,74 | -0,12R | €-76,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 2 | 28 | 28 | 35,71% | 0,49 | -0,24R | €-66,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 3 | 163 | 163 | 40,49% | 1,02 | 0,01R | €18,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 1 | 82 | 82 | 39,02% | 0,73 | -0,13R | €-106,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 49 | 49 | 34,69% | 1,34 | 0,13R | €61,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 58 | 58 | 31,03% | 0,56 | -0,21R | €-120,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 1 | 138 | 138 | 36,23% | 0,82 | -0,09R | €-123,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 2 | 31 | 31 | 25,81% | 0,36 | -0,47R | €-146,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 69 | 69 | 33,33% | 0,77 | -0,14R | €-94,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 1 | 122 | 122 | 35,25% | 0,81 | -0,10R | €-117,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 40 | 40 | 25,00% | 0,83 | -0,08R | €-32,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 2 | 52 | 52 | 26,92% | 0,46 | -0,34R | €-174,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 80 | 80 | 36,25% | 0,96 | -0,02R | €-16,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 2 | 159 | 159 | 33,96% | 0,73 | -0,14R | €-221,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 2 | 8 | 8 | 62,50% | 2,61 | 0,61R | €49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 59 | 59 | 27,12% | 0,89 | -0,05R | €-28,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 80 | 80 | 26,25% | 0,61 | -0,20R | €-156,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 2 | 50 | 50 | 26,00% | 0,41 | -0,38R | €-191,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 67 | 67 | 35,82% | 0,92 | -0,04R | €-28,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 2 | 148 | 148 | 33,11% | 0,67 | -0,17R | €-248,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 2 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 58 | 58 | 27,59% | 0,85 | -0,06R | €-36,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 75 | 75 | 25,33% | 0,47 | -0,27R | €-205,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 2 | 29 | 29 | 34,48% | 0,61 | -0,18R | €-50,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 3 | 182 | 182 | 40,11% | 0,99 | -0,01R | €-12,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 1 | 94 | 94 | 39,36% | 0,90 | -0,05R | €-47,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 50 | 50 | 34,00% | 1,29 | 0,11R | €55,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 63 | 63 | 31,75% | 0,74 | -0,12R | €-76,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 11 | 115 | 115 | 39,13% | 0,66 | -0,17R | €-198,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 2 | 216 | 216 | 42,13% | 1,03 | 0,01R | €28,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 2 | 175 | 175 | 38,86% | 0,89 | -0,05R | €-85,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 32 | 32 | 34,38% | 0,58 | -0,23R | €-73,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 2 | 7 | 7 | 42,86% | 0,81 | -0,11R | €-7,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 76 | 76 | 46,05% | 1,36 | 0,12R | €87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 91 | 91 | 41,76% | 0,83 | -0,08R | €-71,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 29,03% | 0,44 | -0,42R | €-129,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 27 | 27 | 29,63% | 0,64 | -0,25R | €-67,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 1 | 57 | 57 | 42,11% | 0,74 | -0,13R | €-76,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 10 | 10 | 50,00% | 1,26 | 0,14R | €14,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 29 | 29 | 24,14% | 0,38 | -0,42R | €-121,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 11 | 96 | 96 | 28,12% | 0,50 | -0,28R | €-266,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 3 | 192 | 192 | 39,58% | 1,00 | 0,00R | €4,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 2 | 155 | 155 | 33,55% | 0,72 | -0,15R | €-227,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 2 | 8 | 8 | 62,50% | 2,61 | 0,61R | €49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 69 | 69 | 33,33% | 1,27 | 0,11R | €73,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 79 | 79 | 25,32% | 0,56 | -0,22R | €-176,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 11 | 96 | 96 | 28,12% | 0,50 | -0,28R | €-266,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 3 | 194 | 194 | 39,69% | 1,01 | 0,01R | €13,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 2 | 156 | 156 | 33,33% | 0,71 | -0,15R | €-237,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 2 | 8 | 8 | 62,50% | 2,61 | 0,61R | €49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 69 | 69 | 33,33% | 1,27 | 0,11R | €73,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 79 | 79 | 25,32% | 0,56 | -0,22R | €-176,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 11 | 90 | 90 | 28,89% | 0,46 | -0,31R | €-283,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 3 | 172 | 172 | 40,12% | 1,03 | 0,02R | €27,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 2 | 146 | 146 | 32,19% | 0,60 | -0,20R | €-298,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 28 | 28 | 25,00% | 0,63 | -0,20R | €-56,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 2 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 68 | 68 | 33,82% | 1,31 | 0,12R | €81,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 74 | 74 | 24,32% | 0,40 | -0,31R | €-230,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 4 | 28 | 28 | 28,57% | 0,71 | -0,16R | €-44,58 |
| MAIN | ALT_ROTATION_UP | 6 | 85 | 85 | 29,41% | 0,62 | -0,25R | €-208,51 |
| MAIN | RANGE | 1 | 77 | 77 | 22,08% | 0,65 | -0,22R | €-165,89 |
| MAIN | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 2 | 4 | 4 | 75,00% | 4,02 | 0,76R | €30,60 |
| MAIN | TRANSITION | 3 | 38 | 38 | 26,32% | 0,70 | -0,19R | €-71,12 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 3 | 43 | 43 | 27,91% | 0,93 | -0,04R | €-19,30 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -0,70R | €-13,91 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
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
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 12 | 94 | 94 | 26,60% | 0,51 | -0,31R | €-289,50 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 5 | 202 | 202 | 43,07% | 1,11 | 0,06R | €115,00 |
| Bilanciata 1H V1 | RANGE | 2 | 185 | 185 | 40,00% | 1,07 | 0,04R | €70,61 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 46 | 46 | 26,09% | 0,50 | -0,34R | €-156,31 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 3 | 9 | 9 | 33,33% | 1,14 | 0,08R | €7,38 |
| Bilanciata 1H V1 | TRANSITION | 0 | 106 | 106 | 36,79% | 1,14 | 0,07R | €72,43 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 121 | 121 | 29,75% | 0,84 | -0,08R | €-101,88 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 111 | 93 | 49,55% | 1,61 | 0,26R | €293,89 |
| Bilanciata 1H V2 | RANGE | 2 | 135 | 122 | 36,30% | 0,90 | -0,06R | €-75,00 |
| Bilanciata 1H V2 | TRANSITION | 0 | 91 | 78 | 37,36% | 1,19 | 0,10R | €89,47 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 10 | 70 | 70 | 27,14% | 0,47 | -0,34R | €-236,57 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 4 | 118 | 118 | 44,07% | 1,34 | 0,17R | €202,29 |
| Bilanciata 1H V3 Filtered | RANGE | 2 | 127 | 127 | 40,94% | 1,11 | 0,05R | €69,16 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,56 | -0,28R | €-50,80 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 2 | 5 | 5 | 40,00% | 1,84 | 0,36R | €18,00 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 56 | 56 | 33,93% | 1,03 | 0,01R | €7,36 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 70 | 70 | 32,86% | 1,07 | 0,04R | €26,04 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 10 | 59 | 59 | 23,73% | 0,30 | -0,46R | €-269,95 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 116 | 116 | 44,83% | 1,39 | 0,19R | €223,28 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 2 | 105 | 105 | 39,05% | 0,91 | -0,04R | €-47,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 31,25% | 0,69 | -0,19R | €-29,97 |
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
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 19 | 19 | 26,32% | 0,58 | -0,23R | €-43,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 79 | 79 | 45,57% | 1,00 | 0,00R | €0,76 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 51 | 51 | 41,18% | 0,97 | -0,01R | €-6,96 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,70 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 31 | 31 | 41,94% | 1,20 | 0,09R | €26,98 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 57 | 57 | 31,58% | 0,77 | -0,10R | €-57,44 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 49 | 49 | 32,65% | 0,80 | -0,10R | €-48,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 1 | 90 | 90 | 41,11% | 0,93 | -0,03R | €-30,64 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 2 | 164 | 164 | 36,59% | 0,82 | -0,09R | €-144,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 3 | 10 | 10 | 70,00% | 2,77 | 0,56R | €56,29 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 68 | 68 | 39,71% | 1,10 | 0,04R | €26,93 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 85 | 85 | 30,59% | 0,81 | -0,08R | €-72,12 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 67 | 67 | 29,85% | 0,66 | -0,19R | €-130,23 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 91 | 91 | 41,76% | 0,96 | -0,02R | €-16,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 2 | 194 | 194 | 40,21% | 1,00 | 0,00R | €0,70 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 3 | 10 | 10 | 70,00% | 2,77 | 0,56R | €56,29 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 70 | 70 | 41,43% | 1,21 | 0,08R | €56,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 101 | 101 | 29,70% | 0,71 | -0,14R | €-144,33 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 11 | 129 | 129 | 30,23% | 0,60 | -0,24R | €-304,79 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 4 | 233 | 233 | 39,48% | 0,86 | -0,07R | €-169,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 2 | 224 | 224 | 38,39% | 0,87 | -0,07R | €-146,55 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 40 | 40 | 37,50% | 0,86 | -0,07R | €-29,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 3 | 10 | 10 | 50,00% | 1,42 | 0,17R | €17,50 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 96 | 96 | 40,62% | 1,29 | 0,11R | €103,66 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 117 | 117 | 29,06% | 0,70 | -0,16R | €-183,10 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 49 | 49 | 46,94% | 1,55 | 0,20R | €97,83 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 10 | 75 | 75 | 28,00% | 0,46 | -0,36R | €-266,88 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 138 | 138 | 44,20% | 1,09 | 0,04R | €56,41 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 2 | 124 | 124 | 42,74% | 1,14 | 0,06R | €78,71 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 41,18% | 0,87 | -0,07R | €-11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 2 | 6 | 6 | 100,00% | ∞ | 1,01R | €60,81 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 55 | 55 | 40,00% | 1,32 | 0,11R | €63,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 67 | 67 | 29,85% | 0,68 | -0,17R | €-110,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 12 | 126 | 126 | 30,16% | 0,62 | -0,21R | €-268,12 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 4 | 235 | 235 | 40,00% | 0,99 | -0,00R | €-9,89 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 208 | 208 | 36,06% | 0,86 | -0,07R | €-153,62 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 39 | 39 | 28,21% | 0,64 | -0,20R | €-78,08 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 3 | 9 | 9 | 44,44% | 1,46 | 0,21R | €18,89 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 90 | 90 | 37,78% | 1,34 | 0,13R | €118,42 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 107 | 107 | 22,43% | 0,49 | -0,28R | €-296,86 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 25 | 23 | 44,00% | 0,88 | -0,07R | €-18,54 |
| Rapida 1H V2 | RANGE | 1 | 47 | 39 | 40,43% | 0,86 | -0,07R | €-32,96 |
| Rapida 1H V2 | TRANSITION | 0 | 9 | 9 | 55,56% | 0,95 | -0,02R | €-1,77 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 11 | 124 | 124 | 29,84% | 0,53 | -0,28R | €-348,33 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 3 | 212 | 212 | 42,45% | 1,02 | 0,01R | €22,57 |
| Rapida 1H V3 Filtered | RANGE | 2 | 199 | 199 | 37,69% | 0,86 | -0,07R | €-138,43 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 34 | 34 | 38,24% | 0,87 | -0,07R | €-23,20 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 2 | 9 | 9 | 55,56% | 1,87 | 0,31R | €27,68 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 83 | 83 | 37,35% | 1,13 | 0,05R | €44,82 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 117 | 117 | 37,61% | 0,99 | -0,00R | €-3,29 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 60 | 60 | 36,67% | 0,90 | -0,05R | €-32,12 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 10 | 100 | 100 | 32,00% | 0,54 | -0,28R | €-284,43 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 168 | 168 | 47,02% | 1,19 | 0,08R | €137,90 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 2 | 156 | 156 | 38,46% | 0,92 | -0,04R | €-57,93 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 22 | 22 | 40,91% | 0,94 | -0,03R | €-6,30 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 2 | 7 | 7 | 85,71% | 5,99 | 0,72R | €50,67 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 61 | 61 | 39,34% | 1,14 | 0,06R | €35,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 77 | 77 | 31,17% | 0,72 | -0,14R | €-111,48 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,24 | -0,58R | €-110,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 53,62% | 1,05 | 0,03R | €17,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 85 | 85 | 44,71% | 0,92 | -0,05R | €-39,66 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 37 | 37 | 59,46% | 1,63 | 0,21R | €79,27 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 55 | 55 | 50,91% | 1,02 | 0,01R | €5,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 16,67% | 0,23 | -0,58R | €-104,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 40,58% | 0,92 | -0,04R | €-27,39 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 1 | 88 | 88 | 42,05% | 1,01 | 0,00R | €2,59 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 40,54% | 1,40 | 0,14R | €51,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 56 | 56 | 35,71% | 0,96 | -0,02R | €-9,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 39 | 39 | 25,64% | 0,34 | -0,40R | €-155,10 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 201 | 201 | 41,79% | 0,98 | -0,01R | €-24,11 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 1 | 114 | 114 | 42,98% | 1,04 | 0,02R | €20,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 54 | 54 | 40,74% | 1,31 | 0,11R | €61,61 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 76 | 76 | 35,53% | 0,90 | -0,05R | €-37,86 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 44,74% | 1,30 | 0,13R | €50,46 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 74 | 74 | 28,38% | 0,50 | -0,32R | €-236,34 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 86 | 86 | 38,37% | 0,87 | -0,07R | €-58,73 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 2 | 201 | 201 | 38,81% | 0,91 | -0,04R | €-90,38 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 2 | 9 | 9 | 55,56% | 1,87 | 0,31R | €27,68 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 66 | 66 | 33,33% | 0,99 | -0,01R | €-3,99 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 103 | 103 | 33,01% | 0,80 | -0,11R | €-108,47 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 11 | 123 | 123 | 30,08% | 0,54 | -0,27R | €-336,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 211 | 211 | 41,71% | 0,98 | -0,01R | €-18,55 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 2 | 197 | 197 | 37,56% | 0,85 | -0,08R | €-153,16 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,92 | -0,04R | €-13,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 2 | 9 | 9 | 55,56% | 1,87 | 0,31R | €27,68 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 78 | 78 | 37,18% | 1,16 | 0,06R | €47,58 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 100 | 100 | 32,00% | 0,76 | -0,13R | €-126,03 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 42,50% | 1,23 | 0,10R | €40,19 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 6 | 26 | 26 | 26,92% | 1,20 | 0,11R | €28,79 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 7 | 70 | 70 | 38,57% | 1,06 | 0,04R | €25,10 |
| SHADOW_4H_WIDE | RANGE | 2 | 74 | 74 | 16,22% | 0,68 | -0,22R | €-159,60 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 2 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,40 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 39 | 39 | 15,38% | 0,45 | -0,40R | €-156,04 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 7 | 41 | 41 | 24,39% | 1,06 | 0,04R | €15,74 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 3 | 19 | 19 | 21,05% | 0,75 | -0,17R | €-31,47 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 8 | 29 | 29 | 44,83% | 0,93 | -0,04R | €-10,55 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 1 | 95 | 95 | 51,58% | 1,32 | 0,12R | €113,36 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 72 | 72 | 44,44% | 0,96 | -0,02R | €-12,70 |
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
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 40,00% | 0,57 | -0,29R | €-14,53 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
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
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 20,00% | 0,43 | -0,51R | €-25,44 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,23 | -0,57R | €-17,06 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 11 | 80 | 80 | 28,75% | 0,66 | -0,20R | €-161,26 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 4 | 167 | 167 | 43,11% | 1,13 | 0,07R | €114,11 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 2 | 153 | 153 | 42,48% | 1,00 | -0,00R | €-0,02 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 32 | 32 | 37,50% | 0,88 | -0,06R | €-19,15 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 2 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 81 | 81 | 40,74% | 1,34 | 0,15R | €123,63 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 75 | 75 | 34,67% | 0,89 | -0,05R | €-37,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 102 | 102 | 36,27% | 1,05 | 0,03R | €25,67 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 28 | 28 | 21,43% | 0,52 | -0,28R | €-79,43 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 159 | 159 | 42,77% | 1,09 | 0,05R | €81,39 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 76 | 76 | 50,00% | 1,32 | 0,15R | €112,77 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 44 | 44 | 43,18% | 1,81 | 0,27R | €118,35 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 61 | 61 | 29,51% | 0,62 | -0,19R | €-113,97 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 10 | 97 | 97 | 38,14% | 0,77 | -0,11R | €-104,17 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 4 | 189 | 189 | 39,15% | 0,97 | -0,02R | €-30,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 2 | 155 | 155 | 41,94% | 1,18 | 0,08R | €120,51 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 38 | 38 | 42,11% | 0,80 | -0,09R | €-32,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 2 | 11 | 11 | 36,36% | 0,59 | -0,23R | €-25,44 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 72 | 72 | 45,83% | 1,21 | 0,09R | €62,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 98 | 98 | 36,73% | 0,88 | -0,05R | €-46,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 105 | 105 | 50,48% | 1,26 | 0,11R | €114,10 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 11 | 80 | 80 | 28,75% | 0,67 | -0,19R | €-152,49 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 4 | 165 | 165 | 43,64% | 1,06 | 0,03R | €48,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 2 | 141 | 141 | 45,39% | 1,05 | 0,02R | €34,34 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 30 | 30 | 43,33% | 1,03 | 0,01R | €3,78 |
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
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 3 | 20 | 20 | 20,00% | 0,13 | -0,51R | €-101,53 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 2 | 70 | 70 | 42,86% | 1,06 | 0,03R | €22,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 43 | 43 | 39,53% | 1,04 | 0,02R | €8,30 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 32 | 32 | 31,25% | 0,81 | -0,11R | €-34,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 24 | 24 | 37,50% | 1,07 | 0,03R | €6,04 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 2 | 96 | 96 | 39,58% | 1,04 | 0,02R | €16,87 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 5 | 22 | 22 | 27,27% | 0,47 | -0,29R | €-64,40 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 1,93 | 0,35R | €31,68 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 1 | 34 | 34 | 47,06% | 1,21 | 0,11R | €35,96 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 7 | 7 | 71,43% | 5,11 | 0,67R | €47,21 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 3 | 29 | 29 | 17,24% | 0,18 | -0,59R | €-169,78 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 3 | 127 | 127 | 42,52% | 1,22 | 0,12R | €150,30 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 86 | 86 | 47,67% | 1,51 | 0,24R | €204,17 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 63 | 63 | 41,27% | 1,61 | 0,27R | €171,33 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 69 | 69 | 28,99% | 0,96 | -0,02R | €-14,52 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 11 | 60 | 60 | 31,67% | 0,60 | -0,24R | €-142,92 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 3 | 143 | 143 | 41,96% | 1,11 | 0,06R | €86,68 |
| SHADOW_COMBO_TREND | RANGE | 2 | 131 | 131 | 36,64% | 1,10 | 0,05R | €70,46 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 23 | 23 | 34,78% | 1,15 | 0,07R | €15,88 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 3 | 7 | 7 | 42,86% | 1,33 | 0,14R | €10,03 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 69 | 69 | 34,78% | 1,21 | 0,11R | €76,50 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 67 | 67 | 29,85% | 0,70 | -0,16R | €-107,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 79 | 79 | 30,38% | 1,03 | 0,02R | €13,39 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 1 | 4 | 4 | 50,00% | 0,75 | -0,14R | €-5,46 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 71,29 | 0,77R | €30,62 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 4 | 4 | 25,00% | 0,07 | -0,78R | €-31,00 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,19 | -0,64R | €-25,79 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 50,00% | 1,04 | 0,02R | €1,62 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 1 | 8 | 8 | 12,50% | 0,13 | -0,61R | €-48,91 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,61R | €-42,76 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 9 | 9 | 44,44% | 1,13 | 0,08R | €7,37 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 7 | 43 | 43 | 23,26% | 0,46 | -0,41R | €-178,25 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 83 | 83 | 34,94% | 0,71 | -0,20R | €-162,48 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 68 | 68 | 33,82% | 1,06 | 0,04R | €25,42 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 28 | 28 | 39,29% | 1,47 | 0,23R | €64,33 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 41 | 41 | 26,83% | 1,03 | 0,02R | €7,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 23 | 23 | 52,17% | 1,69 | 0,35R | €80,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 7 | 33 | 33 | 21,21% | 0,30 | -0,57R | €-186,73 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 1 | 75 | 75 | 37,33% | 0,77 | -0,15R | €-112,06 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 48 | 48 | 35,42% | 1,04 | 0,02R | €10,36 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 21 | 21 | 47,62% | 2,13 | 0,45R | €93,60 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 27 | 27 | 22,22% | 0,83 | -0,07R | €-19,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 58,82% | 2,03 | 0,44R | €75,25 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 11 | 64 | 64 | 29,69% | 0,52 | -0,30R | €-191,68 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 3 | 143 | 143 | 43,36% | 1,18 | 0,10R | €138,00 |
| SHADOW_EMA_TREND_1H | RANGE | 3 | 126 | 126 | 35,71% | 1,11 | 0,06R | €70,87 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 3 | 7 | 7 | 42,86% | 1,33 | 0,14R | €10,03 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 67 | 67 | 32,84% | 1,07 | 0,04R | €26,08 |
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
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,56 | -0,33R | €-19,66 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,98 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 0,76 | -0,14R | €-18,29 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,57 | -0,30R | €-8,95 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 6 | 6 | 33,33% | 0,68 | -0,24R | €-14,10 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 34,78% | 1,09 | 0,05R | €12,63 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 2 | 42 | 42 | 33,33% | 0,97 | -0,02R | €-7,68 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 1 | 84 | 84 | 30,95% | 0,97 | -0,02R | €-13,32 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 41 | 41 | 41,46% | 1,52 | 0,28R | €114,10 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 65 | 65 | 27,69% | 0,77 | -0,16R | €-103,17 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 33 | 33 | 54,55% | 0,92 | -0,03R | €-11,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 95 | 95 | 72,63% | 1,73 | 0,19R | €185,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 154 | 154 | 66,88% | 1,48 | 0,15R | €225,51 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 85 | 85 | 70,59% | 1,59 | 0,16R | €135,31 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 119 | 119 | 60,50% | 0,98 | -0,01R | €-7,11 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 33,33% | 1,11 | 0,06R | €13,44 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 1 | 84 | 84 | 33,33% | 1,09 | 0,05R | €45,58 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 40 | 40 | 37,50% | 1,28 | 0,16R | €63,73 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 75 | 75 | 25,33% | 0,68 | -0,24R | €-176,26 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 41,18% | 1,59 | 0,33R | €55,43 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 45 | 45 | 28,89% | 0,79 | -0,15R | €-68,61 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 1 | 76 | 76 | 30,26% | 1,09 | 0,06R | €44,64 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 37 | 37 | 37,84% | 1,33 | 0,19R | €68,83 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 61 | 61 | 22,95% | 0,63 | -0,27R | €-166,79 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,15 | -0,75R | €-104,34 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 59 | 59 | 35,59% | 1,11 | 0,07R | €41,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 31 | 31 | 41,94% | 1,73 | 0,35R | €107,67 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 54 | 54 | 29,63% | 0,85 | -0,10R | €-55,36 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 33,33% | 1,03 | 0,02R | €3,57 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 2 | 44 | 44 | 34,09% | 1,00 | 0,00R | €0,04 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 1 | 79 | 79 | 32,91% | 1,09 | 0,05R | €40,31 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 40 | 40 | 37,50% | 1,28 | 0,16R | €64,16 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 64 | 64 | 23,44% | 0,62 | -0,28R | €-181,57 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 13 | 75 | 75 | 30,67% | 0,68 | -0,19R | €-145,55 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 4 | 163 | 163 | 41,10% | 1,16 | 0,09R | €142,89 |
| Forza relativa 1H V1 | RANGE | 2 | 173 | 173 | 30,64% | 0,80 | -0,11R | €-188,39 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 28 | 28 | 28,57% | 0,53 | -0,25R | €-70,96 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 3 | 9 | 9 | 22,22% | 0,49 | -0,35R | €-31,55 |
| Forza relativa 1H V1 | TRANSITION | 1 | 81 | 81 | 35,80% | 1,31 | 0,16R | €128,39 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 75 | 75 | 28,00% | 0,87 | -0,07R | €-51,18 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 103 | 103 | 26,21% | 0,88 | -0,07R | €-67,74 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 27,27% | 0,81 | -0,12R | €-39,63 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 6 | 34 | 33 | 41,18% | 0,76 | -0,12R | €-40,32 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 2 | 60 | 55 | 48,33% | 1,71 | 0,33R | €197,36 |
| Forza relativa 1H V2 | RANGE | 3 | 75 | 72 | 33,33% | 0,86 | -0,08R | €-61,41 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 7 | 6 | 28,57% | 0,87 | -0,06R | €-4,22 |
| Forza relativa 1H V2 | TRANSITION | 0 | 46 | 41 | 36,96% | 1,48 | 0,24R | €109,19 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 35 | 34 | 28,57% | 0,95 | -0,02R | €-7,36 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 41 | 37 | 46,34% | 1,70 | 0,32R | €131,11 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 10 | 51 | 51 | 19,61% | 0,27 | -0,51R | €-260,17 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 63 | 63 | 23,81% | 0,37 | -0,36R | €-227,47 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 24 | 24 | 45,83% | 1,34 | 0,18R | €42,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 10 | 51 | 51 | 19,61% | 0,27 | -0,51R | €-260,17 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 63 | 63 | 23,81% | 0,37 | -0,36R | €-227,47 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 24 | 24 | 45,83% | 1,34 | 0,18R | €42,90 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 10 | 51 | 51 | 19,61% | 0,27 | -0,51R | €-260,17 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 63 | 63 | 23,81% | 0,37 | -0,36R | €-227,47 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 24 | 24 | 45,83% | 1,34 | 0,18R | €42,90 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 9 | 45 | 45 | 26,67% | 0,52 | -0,29R | €-132,19 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 46,67% | 1,70 | 0,29R | €44,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 77 | 77 | 28,57% | 0,63 | -0,21R | €-158,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,33 | 0,13R | €23,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 40 | 40 | 40,00% | 1,11 | 0,06R | €24,19 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 9 | 53 | 53 | 49,06% | 0,59 | -0,20R | €-104,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 45,45% | 1,12 | 0,06R | €6,29 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 71 | 71 | 54,93% | 0,70 | -0,13R | €-92,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 22 | 22 | 63,64% | 1,42 | 0,16R | €34,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 31 | 31 | 61,29% | 1,51 | 0,21R | €65,37 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 9 | 44 | 44 | 45,45% | 0,38 | -0,31R | €-137,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,55 | 0,22R | €28,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 64 | 64 | 54,69% | 0,45 | -0,23R | €-146,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 60,00% | 1,23 | 0,10R | €19,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 30 | 30 | 63,33% | 1,77 | 0,30R | €89,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 2 | 24 | 24 | 29,17% | 0,66 | -0,19R | €-45,74 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 4 | 166 | 166 | 41,57% | 1,04 | 0,02R | €35,92 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 68 | 68 | 51,47% | 1,47 | 0,20R | €133,16 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 48 | 48 | 37,50% | 1,46 | 0,17R | €80,53 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 57 | 57 | 26,32% | 0,52 | -0,25R | €-142,81 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 2 | 24 | 24 | 29,17% | 0,66 | -0,19R | €-45,67 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 169 | 169 | 42,60% | 1,05 | 0,02R | €40,16 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 68 | 68 | 51,47% | 1,47 | 0,20R | €133,16 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 48 | 48 | 37,50% | 1,46 | 0,17R | €80,53 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 57 | 57 | 26,32% | 0,52 | -0,25R | €-142,81 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 2 | 24 | 24 | 29,17% | 0,66 | -0,19R | €-45,67 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 169 | 169 | 42,60% | 1,05 | 0,02R | €40,16 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 68 | 68 | 51,47% | 1,47 | 0,20R | €133,16 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 48 | 48 | 37,50% | 1,46 | 0,17R | €80,53 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 57 | 57 | 26,32% | 0,52 | -0,25R | €-142,81 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 2 | 27 | 27 | 18,52% | 0,20 | -0,55R | €-147,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 3 | 127 | 127 | 42,52% | 1,22 | 0,12R | €150,89 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 80 | 80 | 47,50% | 1,61 | 0,27R | €215,86 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 58 | 58 | 39,66% | 1,60 | 0,27R | €156,64 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 68 | 68 | 27,94% | 0,91 | -0,05R | €-35,23 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,05 | -0,75R | €-89,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 1 | 52 | 52 | 34,62% | 0,77 | -0,15R | €-75,79 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 24 | 24 | 45,83% | 1,97 | 0,37R | €89,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 55 | 55 | 25,45% | 0,71 | -0,16R | €-88,97 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 21 | 21 | 14,29% | 0,08 | -0,64R | €-133,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 66 | 66 | 33,33% | 0,79 | -0,13R | €-86,04 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 75 | 75 | 46,67% | 1,48 | 0,22R | €162,62 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 44 | 44 | 43,18% | 2,12 | 0,39R | €173,79 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 49 | 49 | 18,37% | 0,43 | -0,34R | €-168,64 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 26,32% | 0,39 | -0,27R | €-50,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 38,33% | 0,95 | -0,02R | €-14,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 1 | 90 | 90 | 46,67% | 1,53 | 0,20R | €179,43 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 46 | 46 | 45,65% | 1,21 | 0,09R | €39,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 49 | 49 | 48,98% | 1,15 | 0,07R | €33,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 0,38 | -0,38R | €-18,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 17,65% | 0,11 | -0,59R | €-100,19 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 34,00% | 0,92 | -0,05R | €-24,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 78 | 78 | 48,72% | 1,56 | 0,25R | €192,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 42 | 42 | 35,71% | 1,52 | 0,22R | €91,50 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 38 | 38 | 21,05% | 0,57 | -0,25R | €-93,78 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,85R | €-51,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 26 | 26 | 34,62% | 0,57 | -0,20R | €-52,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 2 | 126 | 126 | 42,06% | 1,14 | 0,07R | €83,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 1 | 91 | 91 | 47,25% | 1,57 | 0,21R | €189,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 49 | 49 | 42,86% | 1,15 | 0,06R | €29,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 55 | 55 | 49,09% | 1,22 | 0,09R | €49,40 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 22 | 22 | 22,73% | 0,26 | -0,48R | €-104,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 2 | 104 | 104 | 45,19% | 1,41 | 0,21R | €221,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 78 | 78 | 48,72% | 1,56 | 0,25R | €192,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 44 | 44 | 34,09% | 1,36 | 0,16R | €71,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 43 | 43 | 20,93% | 0,61 | -0,22R | €-94,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 2 | 32 | 32 | 34,38% | 0,47 | -0,25R | €-81,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 3 | 146 | 146 | 41,10% | 0,99 | -0,01R | €-8,68 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 1 | 84 | 84 | 47,62% | 1,53 | 0,20R | €170,91 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,61 | -0,16R | €-26,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 55 | 55 | 45,45% | 1,23 | 0,09R | €51,51 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 68 | 68 | 48,53% | 1,18 | 0,07R | €49,16 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 20 | 20 | 25,00% | 0,28 | -0,48R | €-96,23 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 127 | 127 | 41,73% | 1,22 | 0,12R | €152,12 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 71 | 71 | 45,07% | 1,50 | 0,23R | €166,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 47 | 47 | 38,30% | 1,58 | 0,24R | €114,40 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 51 | 51 | 19,61% | 0,52 | -0,27R | €-136,82 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 2 | 19 | 19 | 21,05% | 0,12 | -0,61R | €-116,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 120 | 120 | 40,83% | 1,20 | 0,11R | €130,73 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 66 | 66 | 43,94% | 1,54 | 0,26R | €173,39 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 41 | 41 | 36,59% | 1,84 | 0,32R | €131,54 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 50 | 50 | 22,00% | 0,64 | -0,19R | €-95,97 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 2 | 33 | 33 | 24,24% | 0,45 | -0,35R | €-114,07 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 3 | 132 | 132 | 40,91% | 1,07 | 0,04R | €50,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 82 | 82 | 50,00% | 1,56 | 0,24R | €198,36 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 61 | 61 | 39,34% | 1,51 | 0,21R | €126,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 87 | 87 | 35,63% | 1,06 | 0,03R | €25,24 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 60,00% | 2,05 | 0,45R | €45,46 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 9 | 9 | 44,44% | 0,83 | -0,10R | €-9,30 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 100,00% | ∞ | 1,14R | €34,32 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 1 | 4 | 4 | 75,00% | 1,91 | 0,24R | €9,76 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,41 | -0,45R | €-45,27 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,60 | -0,30R | €-18,00 |
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
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 71,43% | 2,92 | 0,62R | €43,29 |
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
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 66,67% | 2,76 | 0,63R | €56,57 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 1,02 | 0,01R | €1,11 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 1,81 | 0,28R | €8,45 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-31T02:08:49+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **348**
- Scenari virtuali ancora attivi: **8102**
- Gruppi in attesa dell'uscita originale: **297**
- Gruppi con originale chiuso ma Shadow ancora attive: **51**
- Confronti completati: **449028**

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

Generato: 2026-08-31T02:10:06+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **449028**
- Valutazioni prodotte: **26183**
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

Generato: 2026-08-31T02:14:55+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Operativo | Identità | Gross cert. | Net cert. | Pending | Gap | Conflict | Formal review NET | PF storico | PnL storico | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,16 | +€67,59 | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,01 | +€2,56 | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,11 | +€95,26 | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,09 | +€75,72 | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | 90 | 105 | 21 | 0 | 8 | 76 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,55 | +€846,28 | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | 38 | 62 | 17 | 0 | 9 | 35 | 1 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 5,77 | +€1.682,13 | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | 154 | 154 | 26 | 0 | 5 | 121 | 2 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,65 | +€1.253,39 | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 0,00 | €0,00 | COLLECTING |

## Regole di valutazione

- Il campione operativo resta esposto per continuità storica, ma non è il campione formale.
- La soglia 50 usa esclusivamente NET_CERTIFIED_CLOSED_PAIRS.
- P0C produce FORMAL_CERTIFIED_OUTCOME; Block-3 produce SIMULATION_RUNTIME_OUTCOME.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-31T02:05:49+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **33**
- Simulazioni bloccate attive: **41**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **630.48 R**
- Profitto virtuale mancato: **1212.82 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 175 | 4 | 11434.52 |
| DOWN_20 | 175 | 6 | 22749.04 |
| DOWN_30 | 175 | 10 | 33817.07 |
| DOWN_40 | 175 | 60 | 42406.03 |
| UP_10 | 116 | 0 | 11907.15 |
| UP_20 | 116 | 0 | 23814.29 |
| UP_30 | 116 | 0 | 35721.44 |
| UP_40 | 116 | 42 | 44162.07 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-31T02:05:18+00:00

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

Generato: 2026-08-31T02:15:03+00:00

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

Generato: 2026-08-31T02:15:04+00:00

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

Generato: 2026-08-31T02:15:04+00:00

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

Generato: 2026-08-31T02:15:04+00:00

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
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 22.6 | E | 129 | 1.57 | 0.272 | 18.12 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 22.5 | E | 162 | 1.38 | 0.173 | 16.35 |
| 3 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 20.8 | E | 41 | 1.87 | 0.383 | 4.71 |
| 4 | SHADOW_COMBO_ADAPTIVE | BASELINE | 20.6 | E | 170 | 1.27 | 0.131 | 17.44 |
| 5 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 19.9 | E | 204 | 1.16 | 0.079 | 30.08 |
| 6 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 19.2 | E | 243 | 1.15 | 0.075 | 28.04 |
| 7 | SHADOW_1H_FAST_V3 | BASELINE | 19.0 | E | 248 | 1.14 | 0.067 | 29.54 |
| 8 | SHADOW_DONCHIAN_1H | BASELINE | 18.9 | E | 115 | 1.38 | 0.221 | 17.00 |
| 9 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | BASELINE | 18.5 | E | 163 | 1.09 | 0.048 | 22.70 |
| 10 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 18.4 | E | 133 | 1.21 | 0.112 | 21.13 |

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

Generato: 2026-08-31T02:15:04+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BEAR_TREND**
- Righe di performance: **1100**
- Strategie preferite nel regime corrente: **1**
- Strategie da evitare nel regime corrente: **17**
- Memorie contestuali: **525**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_RSI_SHORT_15X_10_RSI75 | shadow-rsi-short-15x-10-rsi75 | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.742 | 0.00 |
| 2 | SHADOW_RSI_SHORT_15X_50_RSI75 | shadow-rsi-short-15x-50-rsi75 | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.742 | 0.00 |
| 3 | SHADOW_RSI_SHORT_15X_10_RSI80 | shadow-rsi-short-15x-10-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.583 | 0.00 |
| 4 | SHADOW_RSI_SHORT_15X_50_RSI80 | shadow-rsi-short-15x-50-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.583 | 0.00 |
| 5 | SHADOW_RSI_SHORT_5X_RSI80 | shadow-rsi-short-5x-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.498 | 0.00 |
| 6 | SHADOW_ETH_EMA_4H | shadow-eth-ema-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.574 | 0.00 |
| 7 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 80.3 | 21 | 2.54 | 0.432 | 3.16 |
| 8 | MAIN | main | INSUFFICIENT | 77.4 | 8 | 2.28 | 0.345 | 1.07 |
| 9 | SHADOW_RSI_LONG_15X_10_RSI25 | shadow-rsi-long-15x-10-rsi25 | INSUFFICIENT | 76.2 | 3 | 4.04 | 0.576 | 0.57 |
| 10 | SHADOW_RSI_LONG_15X_50_RSI25 | shadow-rsi-long-15x-50-rsi25 | INSUFFICIENT | 76.2 | 3 | 4.04 | 0.576 | 0.57 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-31T02:15:04+00:00

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

Generato: 2026-08-31T02:05:49+00:00

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
