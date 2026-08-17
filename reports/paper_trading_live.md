# Paper trading automatico KuCoin

Generato: 2026-08-17T02:08:38+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-17T02:05:27+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-17T02:05:27+00:00 | 2026-08-17T02:05:27+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-17T01:45:00+00:00 | 2026-08-17T01:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-17T01:00:00+00:00 | 2026-08-17T01:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-16T20:00:00+00:00 | 2026-08-16T20:00:00+00:00 | 2,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive — parziale 1R | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Trend/Transition | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — qualità completa + profit lock | AKE | 60m | LONG | 6,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | 60m | LONG | 6,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — senza Trend Up | BEAT | 60m | SHORT | -7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — score 6–7,5 | BEAT | 60m | SHORT | -7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | DOGE | 240m | SHORT | -7,57 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -7,09 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | H | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,18 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | SHORT | -5,50 | 6,00 | 0,50 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -5,25 | 6,00 | 0,75 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HEMI | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,13 | 6,00 | 1,87 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,27 | 6,00 | 4,73 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | HYPE | 60m | LONG | 8,23 | 5,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | HYPE | 60m | LONG | 8,23 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — target pieno 2R | HYPE | 60m | LONG | 8,23 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | HYPE | 60m | LONG | 8,23 | 4,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Donchian 1H Gb20 120R V1 | HYPE | 60m | LONG | 8,23 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.650,09 | -3,50% | €-98,26 | €3.000,00 | -3,28% | 6 | 41 | 34,15% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 41 | 1429 | PRIME INDICAZIONI | 50 (mancano 9) |

- Trade del Principale 4H chiusi: **41**; win rate **34,15%**; profit factor **0,72**.
- Expectancy: **€-9,22** per trade; P&L netto: **€-378,20**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.650,09 | €1.293,51 | €3.880,53 | €193,20 | €27,66 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.619,54 | €5.505,59 | €11.011,19 | €213,51 | €-35,46 |
| TEST | Rapida score 6–7,5 — Cost Aware | 3 | €10.587,16 | €1.864,71 | €5.594,13 | €105,00 | €-9,29 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.509,17 | €2.167,54 | €6.502,61 | €210,37 | €37,00 |
| TEST | Rapida V1 — score 6–7,5 | 5 | €10.426,46 | €608,36 | €1.825,07 | €206,57 | €6,58 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.369,52 | €5.375,97 | €10.751,94 | €208,48 | €-34,63 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.355,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.296,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 4 | €10.293,01 | €490,02 | €1.470,06 | €104,03 | €-28,13 |
| TEST | Combo Trend — Side × Regime Guard | 6 | €10.284,94 | €3.684,62 | €7.369,25 | €206,35 | €9,12 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 10 | €10.248,35 | €1.345,70 | €4.037,11 | €204,97 | €0,27 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 6 | €10.211,42 | €654,60 | €1.963,80 | €151,71 | €-4,60 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 5 | €10.149,25 | €592,18 | €1.776,55 | €201,08 | €6,41 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 6 | €10.142,56 | €626,91 | €1.880,73 | €201,83 | €-1,92 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 5 | €10.043,07 | €4.351,33 | €13.053,98 | €200,79 | €-17,47 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €10.015,02 | €1.305,90 | €3.917,70 | €50,15 | €-11,96 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €10.005,51 | €1.384,76 | €4.154,29 | €49,85 | €37,70 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.995,18 | €1.155,63 | €3.466,88 | €49,92 | €10,18 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €9.990,92 | €3.844,94 | €7.689,89 | €150,64 | €21,29 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 1 | €9.989,93 | €10,00 | €150,00 | €0,00 | €0,26 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €9.981,94 | €4.545,42 | €9.090,84 | €151,22 | €54,60 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.980,90 | €1.413,45 | €2.826,90 | €49,75 | €29,01 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 1 | €9.973,84 | €498,55 | €2.492,76 | €0,00 | €4,29 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 8 | €9.967,74 | €988,83 | €2.966,50 | €199,20 | €-17,54 |
| TEST | Sol Donchian 4H | 1 | €9.965,22 | €1.374,20 | €2.748,40 | €49,92 | €-18,13 |
| TEST | Sol Adaptive 4H | 1 | €9.963,96 | €1.259,31 | €2.518,63 | €49,91 | €-16,61 |
| TEST | Scanner Bottom10 Short | 10 | €9.960,03 | €1.923,72 | €3.847,44 | €198,95 | €14,09 |
| TEST | Scanner Bottom15 Short | 10 | €9.960,03 | €1.923,72 | €3.847,44 | €198,95 | €14,09 |
| TEST | Scanner Bottom20 Short | 10 | €9.960,03 | €1.923,72 | €3.847,44 | €198,95 | €14,09 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 6 | €9.957,31 | €638,31 | €1.914,94 | €147,94 | €-4,49 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 1 | €9.949,64 | €50,00 | €750,00 | €0,00 | €1,29 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €9.925,53 | €1.295,48 | €3.886,44 | €49,75 | €-23,02 |
| TEST | Sol Donchian 1H | 1 | €9.923,05 | €1.293,08 | €3.879,24 | €49,65 | €-5,49 |
| TEST | Btc Donchian 4H | 1 | €9.922,97 | €1.406,00 | €2.812,00 | €49,49 | €22,92 |
| TEST | Ampia 4H | 6 | €9.919,48 | €1.657,67 | €3.315,33 | €149,67 | €101,50 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 9 | €9.892,51 | €1.914,29 | €3.828,57 | €197,57 | €13,73 |
| TEST | Btc Ema 1H | 1 | €9.890,22 | €1.146,03 | €3.438,09 | €49,51 | €-10,44 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 9 | €9.877,46 | €1.911,37 | €3.822,75 | €197,27 | €13,71 |
| TEST | Rapida V1 — target pieno 2R | 10 | €9.849,57 | €1.281,72 | €3.845,16 | €193,62 | €12,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 2 | €9.826,50 | €2.936,08 | €8.808,25 | €98,65 | €-31,88 |
| TEST | Sol Ema 4H | 1 | €9.826,28 | €1.355,04 | €2.710,08 | €49,23 | €-17,88 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 8 | €9.809,52 | €3.868,40 | €7.736,79 | €195,48 | €-13,64 |
| TEST | Scanner Bottom 5 Short 1H | 9 | €9.801,45 | €1.896,67 | €3.793,33 | €195,75 | €13,61 |
| TEST | Sol Ema 1H | 1 | €9.796,62 | €1.135,84 | €3.407,53 | €49,07 | €-15,87 |
| TEST | Eth Donchian 1H | 1 | €9.784,57 | €1.278,28 | €3.834,84 | €49,09 | €-30,32 |
| TEST | Rapida 1H V2 | 1 | €9.766,31 | €1.454,10 | €4.362,29 | €48,86 | €-2,62 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 3 | €9.757,24 | €5.821,37 | €11.642,74 | €93,21 | €74,26 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.742,42 | €4.923,45 | €9.846,91 | €95,07 | €50,69 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 9 | €9.738,87 | €1.913,81 | €5.741,43 | €147,29 | €-3,02 |
| TEST | Bilanciata 1H V1 | 9 | €9.731,45 | €657,11 | €1.971,33 | €194,46 | €7,71 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 5 | €9.709,77 | €3.369,30 | €6.738,59 | €193,92 | €14,04 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.686,58 | €1.512,09 | €3.024,18 | €48,39 | €8,88 |
| TEST | Rapida 1H V3 Filtered — madre | 9 | €9.675,23 | €1.901,30 | €5.703,91 | €146,33 | €-3,00 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.664,59 | €4.625,03 | €9.250,06 | €193,37 | €-18,98 |
| TEST | Bilanciata 1H V2 | 4 | €9.657,94 | €1.427,74 | €4.283,23 | €97,20 | €-4,75 |
| TEST | Sol Adaptive 1H | 1 | €9.644,95 | €1.119,69 | €3.359,08 | €48,37 | €-27,20 |
| TEST | Rapida V3 — no volatilità HIGH | 6 | €9.625,05 | €3.042,14 | €9.126,41 | €188,84 | €-56,72 |
| TEST | Combo Adaptive — Long Only | 4 | €9.621,09 | €3.163,00 | €6.326,00 | €50,16 | €60,83 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 4 | €9.610,72 | €1.367,72 | €2.735,44 | €145,82 | €-16,97 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 5 | €9.609,45 | €2.603,97 | €7.811,92 | €142,09 | €-3,05 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €9.604,73 | €3.379,40 | €6.758,80 | €146,98 | €-0,18 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 4 | €9.596,86 | €3.066,13 | €9.198,40 | €95,52 | €-2,66 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 9 | €9.595,44 | €3.269,21 | €6.538,43 | €188,83 | €-13,35 |
| TEST | Eth Ema 1H | 1 | €9.583,94 | €1.113,68 | €3.341,04 | €48,11 | €-36,78 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €9.555,00 | €1.353,76 | €2.707,53 | €147,11 | €-3,74 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.524,41 | €2.291,91 | €4.583,81 | €190,23 | €13,02 |
| TEST | Rapida V3 — qualità completa + profit lock | 5 | €9.491,42 | €3.386,17 | €10.158,50 | €189,84 | €-3,02 |
| TEST | Combo Adaptive — Quality7 + Regime | 4 | €9.489,84 | €1.350,52 | €2.701,03 | €143,99 | €-16,76 |
| TEST | Combo Trend | 9 | €9.478,15 | €2.488,09 | €4.976,18 | €147,25 | €68,44 |
| TEST | Rapida V3 — senza ESPORTS | 9 | €9.465,04 | €1.285,78 | €3.857,33 | €186,14 | €-2,81 |
| TEST | Top 5 + BTC — Guard | 4 | €9.439,04 | €1.337,33 | €2.674,67 | €145,32 | €-3,70 |
| TEST | Master Adaptive Expanded V1 | 7 | €9.437,46 | €3.338,91 | €6.677,82 | €188,71 | €2,15 |
| TEST | Bilanciata V3 · LONG only | 8 | €9.427,88 | €935,28 | €2.805,83 | €188,41 | €-16,59 |
| TEST | Combo Adaptive — parziale 1R | 8 | €9.419,54 | €3.714,61 | €7.429,22 | €187,71 | €-13,10 |
| TEST | Combo Adaptive — target pieno 3R | 9 | €9.416,18 | €3.208,14 | €6.416,28 | €185,30 | €-13,10 |
| TEST | Master Adaptive No Alt V1 | 7 | €9.403,35 | €3.819,60 | €7.639,20 | €141,71 | €52,26 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €9.391,06 | €1.330,54 | €2.661,07 | €144,58 | €-3,68 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 5 | €9.330,79 | €4.431,98 | €8.863,96 | €185,92 | €36,56 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 5 | €9.320,87 | €4.427,27 | €8.854,53 | €185,72 | €36,52 |
| TEST | Forza relativa 1H V1 | 6 | €9.287,24 | €2.857,07 | €5.714,14 | €185,51 | €11,88 |
| TEST | Master Adaptive V1 | 5 | €9.284,82 | €4.410,14 | €8.820,28 | €185,01 | €36,38 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €9.283,03 | €3.252,19 | €6.504,38 | €141,63 | €-0,18 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €9.277,60 | €3.250,28 | €6.500,57 | €141,54 | €-0,18 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.253,29 | €2.685,00 | €8.055,00 | €139,52 | €52,94 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.223,10 | €2.060,02 | €4.120,04 | €141,94 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.219,52 | €1.306,23 | €2.612,46 | €141,94 | €-3,61 |
| TEST | Benchmark trend following EMA 1H | 11 | €9.203,18 | €3.821,95 | €7.643,90 | €184,16 | €-3,91 |
| TEST | Scanner Top10 Long | 5 | €9.194,70 | €3.972,35 | €7.944,69 | €139,27 | €50,31 |
| TEST | Scanner Top15 Long | 5 | €9.194,70 | €3.972,35 | €7.944,69 | €139,27 | €50,31 |
| TEST | Scanner Top20 Long | 5 | €9.194,70 | €3.972,35 | €7.944,69 | €139,27 | €50,31 |
| TEST | Top 5 + BTC — BTC≤3 | 5 | €9.178,29 | €3.229,36 | €6.458,71 | €140,45 | €-0,17 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.161,46 | €4.351,55 | €8.703,09 | €182,55 | €35,89 |
| TEST | Rapida V3 — Long Only | 4 | €9.137,25 | €2.919,29 | €8.757,88 | €90,95 | €-2,53 |
| TEST | Combo Scanner | 5 | €9.123,17 | €4.368,98 | €8.737,97 | €182,54 | €-1,19 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 1 | €9.069,67 | €1.805,69 | €3.611,39 | €39,00 | €43,38 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.003,05 | €3.167,70 | €6.335,40 | €137,77 | €-0,17 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.899,45 | €1.878,70 | €3.757,40 | €137,45 | €-3,33 |
| TEST | Combo Adaptive — MFE Trail esistente | 6 | €8.841,50 | €1.894,68 | €3.789,36 | €130,26 | €-21,92 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.650,09 | €-378,20 | 41 | 41 | 34,15% | 0,72 | €-9,22 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.619,54 | €660,35 | 60 | 60 | 48,33% | 1,46 | €11,01 | 3,63% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.587,16 | €602,09 | 68 | 68 | 51,47% | 1,42 | €8,85 | 3,35% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.509,17 | €470,38 | 21 | 21 | 52,38% | 2,09 | €22,40 | 2,40% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.426,46 | €357,44 | 118 | 117 | 44,07% | 1,13 | €3,03 | 4,89% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.369,52 | €409,36 | 28 | 28 | 46,43% | 1,71 | €14,62 | 3,63% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.355,43 | €355,43 | 33 | 33 | 48,48% | 1,52 | €10,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.296,26 | €296,26 | 31 | 31 | 51,61% | 1,36 | €9,56 | 2,31% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.293,01 | €324,68 | 51 | 51 | 49,02% | 1,31 | €6,37 | 5,24% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.284,94 | €279,20 | 44 | 44 | 52,27% | 1,35 | €6,35 | 2,94% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.248,35 | €245,97 | 111 | 111 | 43,24% | 1,12 | €2,22 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.211,42 | €219,82 | 108 | 108 | 43,52% | 1,09 | €2,04 | 6,52% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.149,25 | €82,06 | 76 | 75 | 47,37% | 1,04 | €1,08 | 5,23% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.142,56 | €149,56 | 108 | 108 | 42,59% | 1,06 | €1,38 | 6,72% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.043,07 | €65,90 | 8 | 8 | 37,50% | 1,47 | €8,24 | 1,59% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.015,02 | €29,32 | 6 | 6 | 66,67% | 1,27 | €4,89 | 1,49% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.005,51 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Ema 1H | Trend following EMA | €9.995,18 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.990,92 | €-28,36 | 54 | 54 | 44,44% | 0,97 | €-0,53 | 6,65% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,93 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €9.981,94 | €-66,79 | 71 | 71 | 42,25% | 0,97 | €-0,94 | 8,85% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Ema 4H | Trend following EMA | €9.980,90 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.973,84 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.967,74 | €-12,96 | 90 | 90 | 37,78% | 0,99 | €-0,14 | 6,82% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.965,22 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.963,96 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.960,03 | €-47,42 | 50 | 50 | 36,00% | 0,95 | €-0,95 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.960,03 | €-47,42 | 50 | 50 | 36,00% | 0,95 | €-0,95 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.960,03 | €-47,42 | 50 | 50 | 36,00% | 0,95 | €-0,95 | 5,27% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.957,31 | €-34,49 | 72 | 72 | 41,67% | 0,98 | €-0,48 | 6,52% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.949,64 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.925,53 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 2,06% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.923,05 | €-69,14 | 7 | 7 | 42,86% | 0,63 | €-9,88 | 2,28% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.922,97 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Ampia 4H | Confluenza trend | €9.919,48 | €-182,43 | 36 | 36 | 22,22% | 0,81 | €-5,07 | 4,45% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.892,51 | €-114,64 | 42 | 42 | 35,71% | 0,87 | €-2,73 | 5,27% |
| TEST | Btc Ema 1H | Trend following EMA | €9.890,22 | €-98,30 | 8 | 8 | 37,50% | 0,63 | €-12,29 | 1,72% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.877,46 | €-129,68 | 43 | 43 | 34,88% | 0,84 | €-3,02 | 5,27% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.849,57 | €-214,75 | 126 | 126 | 35,71% | 0,92 | €-1,70 | 3,95% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.826,50 | €-137,96 | 35 | 35 | 45,71% | 0,84 | €-3,94 | 4,50% |
| TEST | Sol Ema 4H | Trend following EMA | €9.826,28 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,76% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.809,52 | €-171,64 | 71 | 71 | 36,62% | 0,87 | €-2,42 | 5,36% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.801,45 | €-205,64 | 70 | 70 | 34,29% | 0,85 | €-2,94 | 6,41% |
| TEST | Sol Ema 1H | Trend following EMA | €9.796,62 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 3,07% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.784,57 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,40% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.766,31 | €-228,46 | 30 | 27 | 36,67% | 0,72 | €-7,62 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.757,24 | €-308,68 | 30 | 30 | 36,67% | 0,70 | €-10,29 | 5,09% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.742,42 | €-301,34 | 69 | 69 | 43,48% | 0,83 | €-4,37 | 6,53% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.738,87 | €-261,65 | 90 | 90 | 46,67% | 0,85 | €-2,91 | 7,17% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.731,45 | €-275,20 | 102 | 102 | 40,20% | 0,86 | €-2,70 | 8,61% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.709,77 | €-299,45 | 72 | 69 | 38,89% | 0,87 | €-4,16 | 8,11% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.686,58 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.675,23 | €-325,28 | 134 | 134 | 38,06% | 0,89 | €-2,43 | 7,14% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.664,59 | €-309,48 | 30 | 30 | 36,67% | 0,60 | €-10,32 | 3,91% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.657,94 | €-332,08 | 66 | 60 | 42,42% | 0,79 | €-5,03 | 6,62% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.644,95 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 4,23% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.625,05 | €-314,46 | 96 | 96 | 42,71% | 0,87 | €-3,28 | 6,10% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.621,09 | €-435,61 | 43 | 43 | 32,56% | 0,64 | €-10,13 | 5,16% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.610,72 | €-373,59 | 21 | 21 | 33,33% | 0,51 | €-17,79 | 4,14% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.609,45 | €-382,69 | 67 | 67 | 40,30% | 0,80 | €-5,71 | 5,23% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.604,73 | €-391,03 | 62 | 62 | 33,87% | 0,77 | €-6,31 | 9,76% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.596,86 | €-396,84 | 62 | 62 | 35,48% | 0,75 | €-6,40 | 8,59% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.595,44 | €-386,76 | 75 | 75 | 32,00% | 0,74 | €-5,16 | 6,78% |
| TEST | Eth Ema 1H | Trend following EMA | €9.583,94 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 4,18% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.555,00 | €-439,52 | 43 | 43 | 34,88% | 0,70 | €-10,22 | 6,91% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.524,41 | €-485,91 | 40 | 40 | 27,50% | 0,54 | €-12,15 | 7,10% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.491,42 | €-562,35 | 73 | 73 | 43,84% | 0,75 | €-7,70 | 6,85% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.489,84 | €-494,67 | 21 | 21 | 23,81% | 0,36 | €-23,56 | 5,35% |
| TEST | Combo Trend | Combo Trend | €9.478,15 | €-587,66 | 99 | 99 | 32,32% | 0,78 | €-5,94 | 9,82% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.465,04 | €-587,53 | 108 | 108 | 37,96% | 0,76 | €-5,44 | 7,03% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.439,04 | €-555,54 | 48 | 48 | 31,25% | 0,65 | €-11,57 | 6,51% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.437,46 | €-560,78 | 44 | 44 | 29,55% | 0,65 | €-12,74 | 5,92% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.427,88 | €-553,85 | 46 | 46 | 32,61% | 0,46 | €-12,04 | 6,55% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.419,54 | €-562,36 | 72 | 72 | 34,72% | 0,61 | €-7,81 | 6,16% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.416,18 | €-566,35 | 56 | 56 | 30,36% | 0,54 | €-10,11 | 6,78% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.403,35 | €-643,92 | 43 | 43 | 27,91% | 0,62 | €-14,97 | 6,80% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.391,06 | €-603,55 | 58 | 58 | 36,21% | 0,66 | €-10,41 | 6,18% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.330,79 | €-700,47 | 42 | 42 | 21,43% | 0,49 | €-16,68 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.320,87 | €-710,36 | 37 | 37 | 27,03% | 0,46 | €-19,20 | 7,98% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.287,24 | €-721,88 | 83 | 83 | 28,92% | 0,64 | €-8,70 | 9,65% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.284,82 | €-746,29 | 39 | 39 | 25,64% | 0,50 | €-19,14 | 7,80% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.283,03 | €-712,89 | 47 | 47 | 27,66% | 0,53 | €-15,17 | 10,10% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.277,60 | €-718,32 | 51 | 51 | 29,41% | 0,53 | €-14,08 | 10,40% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.253,29 | €-797,68 | 44 | 44 | 29,55% | 0,48 | €-18,13 | 9,05% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.223,10 | €-777,92 | 39 | 39 | 23,08% | 0,50 | €-19,95 | 8,05% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.219,52 | €-775,19 | 65 | 65 | 35,38% | 0,60 | €-11,93 | 7,96% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.203,18 | €-788,96 | 67 | 67 | 26,87% | 0,54 | €-11,78 | 8,76% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.194,70 | €-851,26 | 43 | 43 | 32,56% | 0,41 | €-19,80 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.194,70 | €-851,26 | 43 | 43 | 32,56% | 0,41 | €-19,80 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.194,70 | €-851,26 | 43 | 43 | 32,56% | 0,41 | €-19,80 | 10,31% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.178,29 | €-817,66 | 43 | 43 | 27,91% | 0,42 | €-19,02 | 10,22% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.161,46 | €-869,24 | 74 | 74 | 47,30% | 0,49 | €-11,75 | 9,02% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.137,25 | €-856,75 | 82 | 82 | 29,27% | 0,62 | €-10,45 | 10,56% |
| TEST | Combo Scanner | Combo Scanner | €9.123,17 | €-873,51 | 67 | 67 | 32,84% | 0,57 | €-13,04 | 10,70% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.069,67 | €-971,54 | 32 | 32 | 15,62% | 0,30 | €-30,36 | 11,09% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.003,05 | €-992,98 | 55 | 55 | 29,09% | 0,34 | €-18,05 | 10,78% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.899,45 | €-1.094,57 | 45 | 45 | 24,44% | 0,48 | €-24,32 | 11,51% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €8.841,50 | €-1.133,70 | 83 | 83 | 30,12% | 0,43 | €-13,66 | 11,70% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99750 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €27,41 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63026,30000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €0,42 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,06993 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,17 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,06993 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €-0,03 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 0,99750 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €0,43 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,03281 | 0,03281 | 0,03675 | 0,04359 | 0,02494 | €125,03 | €375,08 | €45,01 | €-0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 487,26746 | 489,40000 | 494,28412 | 647,25361 | 473,23416 | €24,62 | €73,85 | €1,06 | €-0,32 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63004,39660 | 63026,30000 | 63911,65991 | 83690,84015 | 61189,86998 | €18,78 | €56,35 | €0,81 | €-0,02 |
| Bilanciata 1H V1 | ACE | SHORT | Confluenza trend | 60m | 3,0x | 0,14042 | 0,14042 | 0,15727 | 0,18652 | 0,10672 | €129,09 | €387,27 | €46,47 | €-0,00 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,57999 | €135,05 | €405,16 | €48,62 | €-1,78 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 0,36815 | 0,35962 | 0,41233 | 0,48902 | 0,27979 | €135,05 | €405,14 | €48,62 | €9,39 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1889,17209 | 1888,46000 | 1916,37617 | 2509,45026 | 1834,76393 | €43,74 | €131,21 | €1,89 | €0,05 |
| Bilanciata 1H — LONG senza Range High Vol | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1182,39901 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1632,05865 | 1632,05865 | 1586,54905 | 1096,19939 | 1723,07784 | €570,53 | €1.711,58 | €47,73 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HYPE | LONG | Confluenza trend | 60m | 3,0x | 57,28235 | 58,26300 | 57,75626 | 38,47464 | 58,93208 | €1.030,75 | €3.092,25 | €0,00 | €52,94 |
| Bilanciata 1H — SHORT Trend Down stretto | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| Bilanciata 1H — SHORT Trend Down stretto | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,06993 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €10,18 |
| Bilanciata 1H — SHORT Trend Down stretto | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,71805 | 75,06600 | 75,79399 | 99,25048 | 72,56617 | €1.131,56 | €3.394,68 | €48,88 | €-15,81 |
| Bilanciata 1H — SHORT Trend Down stretto | BTC | SHORT | Confluenza trend | 60m | 3,0x | 62929,63156 | 63026,30000 | 63835,81825 | 83591,52725 | 61117,25817 | €34,60 | €103,79 | €1,49 | €-0,16 |
| Bilanciata 1H — SHORT Trend Down stretto | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 0,99750 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €-11,68 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 0,99750 | 1,00538 | 1,33548 | 0,97642 | €37,09 | €111,28 | €0,00 | €0,87 |
| Bilanciata 1H V2 | ACE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,11641 | €136,55 | €409,66 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,00998 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €-3,61 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 58,29796 | 58,26300 | 57,45847 | 39,15679 | 59,97694 | €1.118,28 | €3.354,85 | €48,31 | €-2,01 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06993 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,18 |
| Bilanciata 1H V3 Filtered | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €457,69 | €1.373,07 | €49,01 | €0,00 |
| Bilanciata 1H V3 Filtered | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €127,78 | €383,34 | €46,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | CYS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,72026 | 0,76650 | 0,80669 | 0,95674 | 0,54739 | €138,39 | €415,18 | €49,82 | €-26,66 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99750 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €0,22 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 62892,88891 | 63026,30000 | 63798,54651 | 83542,72076 | 61081,57371 | €40,14 | €120,43 | €1,73 | €-0,26 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,36815 | 0,35962 | 0,41233 | 0,48902 | 0,27979 | €134,23 | €402,68 | €48,32 | €9,33 |
| Rapida V1 — score 6–7,5 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €0,00 | €0,00 |
| Rapida V1 — score 6–7,5 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €144,97 | €434,90 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €146,27 | €438,81 | €52,66 | €-0,00 |
| Rapida V1 — score 6–7,5 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,77873 | 0,76650 | 0,87218 | 1,03442 | 0,63856 | €144,96 | €434,87 | €52,18 | €6,83 |
| Rapida V1 — score 6–7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,35940 | 0,35962 | 0,40201 | 0,47741 | 0,29550 | €139,31 | €417,92 | €49,54 | €-0,25 |
| Rapida score 6–7,5 — senza Trend Up | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €0,00 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €141,11 | €423,34 | €50,80 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €142,38 | €427,15 | €51,26 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,77873 | 0,76650 | 0,87218 | 1,03442 | 0,63856 | €141,10 | €423,30 | €50,80 | €6,65 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,35940 | 0,35962 | 0,40201 | 0,47741 | 0,29550 | €135,60 | €406,81 | €48,22 | €-0,24 |
| Rapida score 6–7,5 — Cost Aware | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99774 | 0,99750 | 1,00892 | 1,32533 | 0,98098 | €1.572,34 | €4.717,02 | €52,83 | €1,14 |
| Rapida score 6–7,5 — Cost Aware | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €147,46 | €442,37 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,74855 | 0,76650 | 0,83838 | 0,99432 | 0,61381 | €144,91 | €434,74 | €52,17 | €-10,42 |
| Rapida V1 — no HIGH + score <7,5 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €0,00 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €140,04 | €420,12 | €50,41 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €138,95 | €416,85 | €0,00 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,15 | €75,44 | €0,84 | €-0,05 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,00998 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €-2,70 |
| Rapida V1 — no HIGH + score <7,5 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,62578 | €140,65 | €421,95 | €50,63 | €-1,86 |
| Rapida V1 — senza PEPE | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €771,03 | €2.313,08 | €50,17 | €0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €142,21 | €426,63 | €51,20 | €-0,00 |
| Rapida V1 — senza PEPE | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1191,94474 | 1191,94474 | 1171,66933 | 800,58955 | 1222,35785 | €47,86 | €143,59 | €2,44 | €0,00 |
| Rapida V1 — senza PEPE | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €10,42 | €31,26 | €0,35 | €-0,20 |
| Rapida V1 — senza PEPE | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06539 | 0,06539 | 0,05878 | 0,04392 | 0,07530 | €166,06 | €498,19 | €50,35 | €0,00 |
| Rapida V1 — senza PEPE | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06949 | 0,06993 | 0,07027 | 0,09230 | 0,06832 | €13,76 | €41,29 | €0,46 | €-0,26 |
| Rapida V1 — senza PEPE | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €30,07 | €90,22 | €1,01 | €-0,06 |
| Rapida V1 — senza PEPE | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,76835 | 0,76650 | 0,86055 | 1,02062 | 0,63004 | €133,17 | €399,52 | €47,94 | €0,96 |
| Rapida V1 — senza PEPE | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99419 | 0,99750 | 1,00533 | 1,32062 | 0,97749 | €13,10 | €39,31 | €0,44 | €-0,13 |
| Rapida V1 — senza PEPE | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,29796 | 58,26300 | 57,64502 | 39,15679 | 59,27736 | €18,01 | €54,02 | €0,61 | €-0,03 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03778 | 0,03531 | 0,05019 | 0,02871 | €9,36 | €28,07 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1182,39901 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €0,00 |
| Rapida V1 — target pieno 2R | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,91916 | 1632,91916 | 1597,68836 | 1096,77737 | 1703,38077 | €753,45 | €2.260,36 | €48,77 | €0,00 |
| Rapida V1 — target pieno 2R | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,08248 | €168,46 | €505,38 | €48,56 | €0,00 |
| Rapida V1 — target pieno 2R | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06949 | 0,06993 | 0,07027 | 0,09230 | 0,06793 | €25,03 | €75,08 | €0,84 | €-0,48 |
| Rapida V1 — target pieno 2R | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,10258 | €139,64 | €418,91 | €50,27 | €-0,00 |
| Rapida V1 — target pieno 2R | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 62929,63156 | 63026,30000 | 63634,44343 | 83591,52725 | 61520,00781 | €21,81 | €65,43 | €0,73 | €-0,10 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,37290 | 0,35962 | 0,41764 | 0,49533 | 0,28340 | €118,31 | €354,93 | €42,59 | €12,64 |
| Rapida V1 — target pieno 2R | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1931,97597 | €9,62 | €28,86 | €0,32 | €-0,02 |
| Rapida V1 — target pieno 2R | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 58,29796 | 58,26300 | 57,64502 | 39,15679 | 59,60383 | €20,17 | €60,50 | €0,68 | €-0,04 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 58,29796 | 58,26300 | 57,64502 | 39,15679 | 59,27736 | €1.454,10 | €4.362,29 | €48,86 | €-2,62 |
| Rapida 1H V3 Filtered — madre | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €0,00 | €0,00 |
| Rapida 1H V3 Filtered — madre | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €752,55 | €2.257,65 | €48,96 | €0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €136,31 | €408,92 | €49,07 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,43 | €169,29 | €1,90 | €-1,11 |
| Rapida 1H V3 Filtered — madre | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,48 | €49,45 | €4,75 | €0,00 |
| Rapida 1H V3 Filtered — madre | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06949 | 0,06993 | 0,07027 | 0,09230 | 0,06832 | €11,75 | €35,26 | €0,39 | €-0,22 |
| Rapida 1H V3 Filtered — madre | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,31 | €75,93 | €0,85 | €-0,05 |
| Rapida 1H V3 Filtered — madre | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99419 | 0,99750 | 1,00533 | 1,32062 | 0,97749 | €15,63 | €46,89 | €0,53 | €-0,16 |
| Rapida 1H V3 Filtered — madre | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,62578 | €110,76 | €332,29 | €39,87 | €-1,46 |
| Rapida V3 — score <7,5 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €0,00 | €0,00 |
| Rapida V3 — score <7,5 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03283 | 0,03283 | 0,03677 | 0,04361 | 0,02692 | €139,04 | €417,11 | €50,05 | €-0,00 |
| Rapida V3 — score <7,5 | APR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €136,16 | €408,49 | €49,02 | €-0,00 |
| Rapida V3 — score <7,5 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €142,42 | €427,26 | €51,27 | €-0,00 |
| Rapida V3 — score <7,5 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €53,48 | €160,43 | €1,80 | €-0,10 |
| Rapida V3 — score <7,5 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,62578 | €138,02 | €414,05 | €49,69 | €-1,82 |
| Rapida V3 — no volatilità HIGH | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,00 | €0,00 |
| Rapida V3 — no volatilità HIGH | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €0,00 | €0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €135,40 | €406,20 | €48,74 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.450,98 | €4.352,95 | €48,75 | €-28,51 |
| Rapida V3 — no volatilità HIGH | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,72026 | 0,76650 | 0,80669 | 0,95674 | 0,59061 | €133,88 | €401,65 | €48,20 | €-25,79 |
| Rapida V3 — no volatilità HIGH | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.284,05 | €3.852,15 | €43,14 | €-2,42 |
| Rapida V3 — Long Only | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €0,00 | €0,00 |
| Rapida V3 — Long Only | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €0,00 | €0,00 |
| Rapida V3 — Long Only | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €135,06 | €405,19 | €45,82 | €0,00 |
| Rapida V3 — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.343,18 | €4.029,53 | €45,13 | €-2,53 |
| Rapida V3 — Long + no HIGH + score <7,5 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €0,00 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €0,00 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €144,03 | €432,09 | €48,86 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.430,90 | €4.292,71 | €48,08 | €-2,70 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00998 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €-0,35 |
| Rapida V3 — senza ESPORTS | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €0,00 | €0,00 |
| Rapida V3 — senza ESPORTS | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €736,66 | €2.209,98 | €47,93 | €0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €133,42 | €400,27 | €48,03 | €-0,00 |
| Rapida V3 — senza ESPORTS | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €47,04 | €141,11 | €1,58 | €-0,92 |
| Rapida V3 — senza ESPORTS | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €163,10 | €489,29 | €47,02 | €0,00 |
| Rapida V3 — senza ESPORTS | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06949 | 0,06993 | 0,07027 | 0,09230 | 0,06832 | €11,73 | €35,19 | €0,39 | €-0,22 |
| Rapida V3 — senza ESPORTS | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,33 | €75,98 | €0,85 | €-0,05 |
| Rapida V3 — senza ESPORTS | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99419 | 0,99750 | 1,00533 | 1,32062 | 0,97749 | €15,56 | €46,67 | €0,52 | €-0,16 |
| Rapida V3 — senza ESPORTS | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,62578 | €110,59 | €331,77 | €39,81 | €-1,46 |
| Rapida V3 senza ESPORTS — Long Only | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €0,00 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €0,00 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €141,86 | €425,58 | €48,12 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.410,74 | €4.232,21 | €47,40 | €-2,66 |
| Rapida V3 senza ESPORTS — MFE Lock | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €0,00 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €757,50 | €2.272,50 | €49,29 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €137,20 | €411,61 | €49,39 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,80 | €170,41 | €1,91 | €-1,12 |
| Rapida V3 senza ESPORTS — MFE Lock | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,59 | €49,77 | €4,78 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06949 | 0,06993 | 0,07027 | 0,09230 | 0,06832 | €11,83 | €35,50 | €0,40 | €-0,23 |
| Rapida V3 senza ESPORTS — MFE Lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €25,48 | €76,43 | €0,86 | €-0,05 |
| Rapida V3 senza ESPORTS — MFE Lock | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99419 | 0,99750 | 1,00533 | 1,32062 | 0,97749 | €15,73 | €47,20 | €0,53 | €-0,16 |
| Rapida V3 senza ESPORTS — MFE Lock | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,62578 | €111,49 | €334,48 | €40,14 | €-1,47 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.483,05 | €4.449,14 | €49,83 | €-29,14 |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.453,04 | €4.359,11 | €48,82 | €-2,74 |
| Rapida V3 — qualità completa + profit lock | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €0,00 |
| Rapida V3 — qualità completa + profit lock | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €0,00 |
| Rapida V3 — qualità completa + profit lock | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 9,38563 | 9,38563 | 9,22869 | 6,30401 | 9,62103 | €949,50 | €2.848,50 | €47,63 | €0,00 |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €-2,67 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00998 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €-0,35 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 0,99750 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €21,34 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63026,30000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €0,71 |
| Ampia 4H | BEAT | SHORT | Confluenza trend | 240m | 2,0x | 0,44779 | 0,35962 | 0,44779 | 0,66945 | 0,29733 | €202,71 | €405,42 | €0,00 | €79,83 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,06993 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,38 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €79,48 | €158,95 | €3,52 | €0,00 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,03281 | 0,03281 | 0,03675 | 0,04906 | 0,02415 | €186,76 | €373,52 | €44,82 | €-0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,27445 | €166,87 | €333,74 | €40,05 | €11,88 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02493 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,27445 | €197,18 | €394,37 | €47,32 | €14,04 |
| Scalp RSI Long 25 · €10 · 15x | BTC | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 62918,05109 | 63026,30000 | 62962,35805 | 59038,10461 | 63295,55940 | €10,00 | €150,00 | €0,00 | €0,26 |
| Scalp RSI Long 25 · €50 · 15x | BTC | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 62918,05109 | 63026,30000 | 62962,35805 | 59038,10461 | 63295,55940 | €50,00 | €750,00 | €0,00 | €1,29 |
| Scalp RSI Long 25 · prudente · 5x | BTC | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 62918,05109 | 63026,30000 | 62954,36531 | 50649,03113 | 63421,39550 | €498,55 | €2.492,76 | €0,00 | €4,29 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06993 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-19,77 |
| Benchmark Donchian breakout 1H | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €858,65 | €1.717,31 | €52,93 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,06600 | 75,91354 | 111,70349 | 71,72933 | €1.657,45 | €3.314,90 | €53,04 | €-15,44 |
| Benchmark Donchian breakout 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1873,64520 | 1888,46000 | 1903,62352 | 2801,09957 | 1798,69939 | €16,00 | €32,01 | €0,51 | €-0,25 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06993 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-19,31 |
| Donchian 1H Gb20 120R V1 | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €838,44 | €1.676,87 | €51,68 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,06600 | 75,91354 | 111,70349 | 71,72933 | €1.618,43 | €3.236,85 | €51,79 | €-15,07 |
| Donchian 1H Gb20 120R V1 | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1873,64520 | 1888,46000 | 1903,62352 | 2801,09957 | 1798,69939 | €15,63 | €31,26 | €0,50 | €-0,25 |
| Benchmark Bollinger mean reversion 1H | SNDK | SHORT | Bollinger mean reversion | 60m | 2,0x | 1630,10135 | 1630,10135 | 1667,98054 | 2437,00152 | 1573,28257 | €1.043,30 | €2.086,60 | €48,49 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 74,39088 | 75,06600 | 74,77238 | 37,56739 | 75,72991 | €1.939,28 | €3.878,55 | €0,00 | €35,20 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 0,99354 | 0,99750 | 0,98161 | 0,50174 | 1,01142 | €1.940,88 | €3.881,75 | €46,58 | €15,49 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,06993 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,14 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,00 |
| Benchmark trend following EMA 1H | SNDK | LONG | Trend following EMA | 60m | 2,0x | 1632,05865 | 1632,05865 | 1581,49243 | 824,18962 | 1743,30434 | €724,64 | €1.449,29 | €44,90 | €0,00 |
| Benchmark trend following EMA 1H | ETH | SHORT | Trend following EMA | 60m | 2,0x | 1867,89635 | 1888,46000 | 1897,78269 | 2792,50504 | 1802,14639 | €18,13 | €36,25 | €0,58 | €-0,40 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 62898,88771 | 63026,30000 | 63905,26991 | 94033,83712 | 60684,84686 | €27,47 | €54,94 | €0,88 | €-0,11 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 0,99750 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €0,11 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 57,44244 | 58,26300 | 56,52337 | 29,00843 | 59,46442 | €13,41 | €26,81 | €0,43 | €0,38 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 74,94501 | 75,06600 | 76,14413 | 112,04279 | 72,30694 | €1.248,89 | €2.497,78 | €39,96 | €-4,03 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.146,19 | €2.292,38 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 57,22031 | 58,26300 | 57,80524 | 28,89626 | 58,86826 | €1.654,13 | €3.308,27 | €0,00 | €60,28 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €-5,69 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €0,50 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €200,12 | €400,25 | €48,03 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,06600 | 75,79399 | 111,70349 | 72,56617 | €21,64 | €43,28 | €0,62 | €-0,20 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,06993 | 0,07049 | 0,10388 | 0,06749 | €69,53 | €139,06 | €2,00 | €-0,88 |
| Scanner Bottom 5 Short 1H | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €204,10 | €408,20 | €48,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €203,89 | €407,78 | €48,93 | €14,52 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63026,30000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,05 | €90,11 | €1,30 | €-0,01 |
| Scanner Bottom 5 Short 1H | ETH | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1874,85495 | 1888,46000 | 1901,85287 | 2802,90816 | 1820,85913 | €21,78 | €43,56 | €0,63 | €-0,32 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top10 Long | SNDK | LONG | Scanner Top10 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 57,22031 | 58,26300 | 57,80524 | 28,89626 | 58,86826 | €1.524,24 | €3.048,49 | €0,00 | €55,55 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €-5,24 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,51 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,16396 | 75,06600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €0,04 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06949 | 0,06993 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,75 |
| Scanner Bottom10 Short | ACE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom10 Short | ETH | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1878,76417 | 1888,46000 | 1905,81838 | 2808,75244 | 1824,65576 | €16,54 | €33,07 | €0,48 | €-0,17 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €207,19 | €414,39 | €49,73 | €14,75 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63018,79372 | 63026,30000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,01 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 486,37271 | 489,40000 | 493,37647 | 727,12720 | 472,36517 | €23,05 | €46,11 | €0,66 | €-0,29 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top15 Long | SNDK | LONG | Scanner Top15 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 57,22031 | 58,26300 | 57,80524 | 28,89626 | 58,86826 | €1.524,24 | €3.048,49 | €0,00 | €55,55 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €-5,24 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,51 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,16396 | 75,06600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €0,04 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06949 | 0,06993 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,75 |
| Scanner Bottom15 Short | ACE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom15 Short | ETH | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1878,76417 | 1888,46000 | 1905,81838 | 2808,75244 | 1824,65576 | €16,54 | €33,07 | €0,48 | €-0,17 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €207,19 | €414,39 | €49,73 | €14,75 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63018,79372 | 63026,30000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,01 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 486,37271 | 489,40000 | 493,37647 | 727,12720 | 472,36517 | €23,05 | €46,11 | €0,66 | €-0,29 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top20 Long | SNDK | LONG | Scanner Top20 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 57,22031 | 58,26300 | 57,80524 | 28,89626 | 58,86826 | €1.524,24 | €3.048,49 | €0,00 | €55,55 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €-5,24 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,51 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,16396 | 75,06600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €0,04 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06949 | 0,06993 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,75 |
| Scanner Bottom20 Short | ACE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom20 Short | ETH | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1878,76417 | 1888,46000 | 1905,81838 | 2808,75244 | 1824,65576 | €16,54 | €33,07 | €0,48 | €-0,17 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €207,19 | €414,39 | €49,73 | €14,75 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63018,79372 | 63026,30000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,01 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 486,37271 | 489,40000 | 493,37647 | 727,12720 | 472,36517 | €23,05 | €46,11 | €0,66 | €-0,29 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €22,01 | €44,02 | €1,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €200,15 | €400,30 | €48,04 | €1,82 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 60,14484 | €1.668,18 | €3.336,37 | €48,04 | €-2,00 |
| Top 5 + BTC — solo MFE | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €0,00 |
| Top 5 + BTC — solo MFE | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €20,63 | €41,26 | €1,12 | €0,00 |
| Top 5 + BTC — solo MFE | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €187,61 | €375,22 | €45,03 | €1,70 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 60,14484 | €1.563,68 | €3.127,36 | €45,03 | €-1,88 |
| Top 5 + BTC — Guard | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €0,00 |
| Top 5 + BTC — Guard | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €890,44 | €1.780,87 | €48,44 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €-5,49 |
| Top 5 + BTC — Guard | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €196,57 | €393,15 | €47,18 | €1,79 |
| Top 5 + BTC — BTC≤3 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €0,00 |
| Top 5 + BTC — BTC≤3 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €21,03 | €42,07 | €1,14 | €0,00 |
| Top 5 + BTC — BTC≤3 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €191,26 | €382,53 | €45,90 | €1,74 |
| Top 5 + BTC — BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 60,14484 | €1.594,12 | €3.188,23 | €45,91 | €-1,91 |
| Top 5 + BTC — Guard + MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €0,00 |
| Top 5 + BTC — Guard + MFE | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €869,73 | €1.739,45 | €47,32 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €-5,36 |
| Top 5 + BTC — Guard + MFE | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €192,00 | €384,00 | €46,08 | €1,74 |
| Top 5 + BTC — Guard + BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €901,37 | €1.802,75 | €49,04 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €-5,55 |
| Top 5 + BTC — Guard + BTC≤3 | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €198,99 | €397,98 | €47,76 | €1,81 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €885,91 | €1.771,82 | €48,20 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,00998 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €-5,46 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €195,57 | €391,15 | €46,94 | €1,78 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,67 | €0,92 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,19042 | €193,33 | €386,66 | €46,40 | €1,76 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 60,81643 | €1.611,37 | €3.222,73 | €46,41 | €-1,93 |
| Top 5 + BTC — target pieno 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €0,00 |
| Top 5 + BTC — target pieno 3R | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,69 | €0,92 | €0,00 |
| Top 5 + BTC — target pieno 3R | H | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,19042 | €193,45 | €386,89 | €46,43 | €1,76 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 60,81643 | €1.612,31 | €3.224,62 | €46,43 | €-1,93 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,06993 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €8,88 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,06993 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,17 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,00 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1618,90076 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €0,00 |
| Combo Trend | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02351 | €194,61 | €389,21 | €46,71 | €-0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 57,05121 | 58,26300 | 57,72276 | 28,81086 | 59,05941 | €1.283,49 | €2.566,97 | €0,00 | €54,52 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,27445 | €193,08 | €386,15 | €46,34 | €13,75 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 63026,30000 | 62072,20924 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €46,71 | €12,40 |
| Combo Mean Reversion | SOL | LONG | Combo Mean Reversion | 60m | 2,0x | 74,39088 | 75,06600 | 74,77238 | 37,56739 | 75,81918 | €1.937,79 | €3.875,57 | €0,00 | €35,17 |
| Combo Mean Reversion | DOGE | LONG | Combo Mean Reversion | 60m | 2,0x | 0,06945 | 0,06993 | 0,06862 | 0,03507 | 0,07079 | €1.937,17 | €3.874,33 | €46,49 | €26,68 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,06993 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €-1,11 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €1.034,30 | €2.068,59 | €45,78 | €0,00 |
| Combo Scanner | H | LONG | Combo Scanner | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17698 | €190,03 | €380,07 | €45,61 | €1,73 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 60,14484 | €1.504,84 | €3.009,69 | €43,34 | €-1,80 |
| Combo Adaptive — madre | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive — madre | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06993 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,18 |
| Combo Adaptive — madre | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,00 | €0,00 |
| Combo Adaptive — madre | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €686,66 | €1.373,32 | €49,73 | €0,00 |
| Combo Adaptive — madre | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €194,92 | €389,84 | €46,78 | €13,88 |
| Combo Adaptive — madre | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 74,46310 | 75,06600 | 75,53537 | 111,32234 | 72,31857 | €1.705,67 | €3.411,35 | €49,12 | €-27,62 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 59,97694 | €69,65 | €139,29 | €2,01 | €-0,08 |
| Combo Adaptive — MFE Trail esistente | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €15,03 | €30,05 | €0,67 | €0,00 |
| Combo Adaptive — MFE Trail esistente | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €619,25 | €1.238,49 | €44,85 | €0,00 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,06993 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,12 |
| Combo Adaptive — MFE Trail esistente | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,41543 | 58,26300 | 57,82834 | 28,99479 | 59,06899 | €13,65 | €27,29 | €0,00 | €0,40 |
| Combo Adaptive — MFE Trail esistente | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,72026 | 0,76650 | 0,80669 | 1,07678 | 0,54739 | €172,90 | €345,80 | €41,50 | €-22,20 |
| Combo Adaptive — Quality7 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1175,20470 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €0,00 |
| Combo Adaptive — Quality7 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1632,91916 | 1632,91916 | 1587,62241 | 824,62418 | 1723,51265 | €880,79 | €1.761,58 | €48,87 | €0,00 |
| Combo Adaptive — Quality7 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02574 | €203,75 | €407,50 | €48,90 | €-0,00 |
| Combo Adaptive — Quality7 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €182,81 | €365,62 | €43,87 | €13,02 |
| Combo Adaptive — Trend/Transition | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive — Trend/Transition | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,76650 | 0,82382 | 1,09965 | 0,55902 | €202,91 | €405,83 | €48,70 | €-17,07 |
| Combo Adaptive — Trend/Transition | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 59,97694 | €1.588,45 | €3.176,91 | €45,75 | €-1,91 |
| Combo Adaptive — Quality7 + Regime | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive — Quality7 + Regime | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €919,84 | €1.839,67 | €46,79 | €0,00 |
| Combo Adaptive — Quality7 + Regime | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,76650 | 0,82382 | 1,09965 | 0,55902 | €199,19 | €398,38 | €47,81 | €-16,76 |
| Combo Adaptive — Long Only | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €0,00 |
| Combo Adaptive — Long Only | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1652,37083 | 1652,37083 | 1605,97924 | 834,44727 | 1745,15401 | €13,30 | €26,61 | €0,75 | €0,00 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,22031 | 58,26300 | 57,83794 | 28,89626 | 58,86826 | €1.669,05 | €3.338,11 | €0,00 | €60,83 |
| Combo Adaptive — parziale 1R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive — parziale 1R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06993 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,18 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,00 | €0,00 |
| Combo Adaptive — parziale 1R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €659,36 | €1.318,73 | €47,75 | €0,00 |
| Combo Adaptive — parziale 1R | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €187,17 | €374,34 | €44,92 | €13,33 |
| Combo Adaptive — parziale 1R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 74,46310 | 75,06600 | 75,53537 | 111,32234 | 72,31857 | €1.637,86 | €3.275,73 | €47,17 | €-26,52 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 58,29796 | 58,26300 | 57,45847 | 29,44047 | 59,97694 | €66,88 | €133,76 | €1,93 | €-0,08 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €931,55 | €1.863,10 | €47,39 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,76650 | 0,82382 | 1,09965 | 0,55902 | €201,73 | €403,45 | €48,41 | €-16,97 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06993 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,18 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,00 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,35 | €34,70 | €1,24 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €204,60 | €409,21 | €49,10 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,41543 | 58,26300 | 57,82834 | 28,99479 | 59,89578 | €14,35 | €28,70 | €0,00 | €0,42 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,23865 | €183,50 | €367,00 | €44,04 | €13,07 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 74,46310 | 75,06600 | 75,53537 | 111,32234 | 71,24630 | €1.668,43 | €3.336,86 | €48,05 | €-27,02 |
| Combo Adaptive — target pieno 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive — target pieno 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06993 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,18 |
| Combo Adaptive — target pieno 3R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,00 | €0,00 |
| Combo Adaptive — target pieno 3R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,03 | €34,05 | €1,22 | €0,00 |
| Combo Adaptive — target pieno 3R | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Combo Adaptive — target pieno 3R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,41543 | 58,26300 | 57,82834 | 28,99479 | 59,89578 | €14,08 | €28,17 | €0,00 | €0,42 |
| Combo Adaptive — target pieno 3R | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,23865 | €180,07 | €360,14 | €43,22 | €12,82 |
| Combo Adaptive — target pieno 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 74,46310 | 75,06600 | 75,53537 | 111,32234 | 71,24630 | €1.637,26 | €3.274,53 | €47,15 | €-26,51 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62835,53038 | 63026,30000 | 63740,36202 | 83466,52952 | 61025,86711 | €1.146,03 | €3.438,09 | €49,51 | €-10,44 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63026,30000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €29,01 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 62834,55058 | 63026,30000 | 63638,83282 | 83465,22802 | 61225,98608 | €1.305,90 | €3.917,70 | €50,15 | €-11,96 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63026,30000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €22,92 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 74,71805 | 75,06600 | 75,79399 | 99,25048 | 72,56617 | €1.135,84 | €3.407,53 | €49,07 | €-15,87 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 74,57408 | 75,06600 | 75,92873 | 111,48825 | 71,18746 | €1.355,04 | €2.710,08 | €49,23 | €-17,88 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 74,96000 | 75,06600 | 75,91949 | 99,57187 | 73,04103 | €1.293,08 | €3.879,24 | €49,65 | €-5,49 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 74,57408 | 75,06600 | 75,92873 | 111,48825 | 70,78107 | €1.374,20 | €2.748,40 | €49,92 | €-18,13 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 74,39088 | 75,06600 | 73,49818 | 49,96587 | 75,72991 | €1.384,76 | €4.154,29 | €49,85 | €37,70 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 74,46310 | 75,06600 | 75,53537 | 98,91182 | 72,31857 | €1.119,69 | €3.359,08 | €48,37 | €-27,20 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 74,57408 | 75,06600 | 76,05188 | 111,48825 | 70,87959 | €1.259,31 | €2.518,63 | €49,91 | €-16,61 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1867,89635 | 1888,46000 | 1894,79405 | 2481,18898 | 1814,10093 | €1.113,68 | €3.341,04 | €48,11 | €-36,78 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 1873,64520 | 1888,46000 | 1897,62785 | 2488,82537 | 1825,67988 | €1.278,28 | €3.834,84 | €49,09 | €-30,32 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,06993 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €10,18 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,06993 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-23,02 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,93 | €73,85 | €1,65 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €626,90 | €1.253,80 | €44,76 | €0,00 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,26300 | 56,74249 | 29,07362 | 59,22958 | €1.514,30 | €3.028,59 | €43,61 | €36,38 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68062 | 829,90965 | 1732,79507 | €22,94 | €45,88 | €1,25 | €0,00 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,28235 | 58,26300 | 56,45748 | 28,92759 | 58,93208 | €1.526,97 | €3.053,94 | €43,98 | €52,28 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1888,46000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €-0,02 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1167,82027 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1655,75286 | 1655,75286 | 1602,89078 | 836,15519 | 1761,47701 | €734,74 | €1.469,49 | €46,92 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,00998 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €-3,33 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.101,72 | €2.203,44 | €48,77 | €0,00 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,19029 | 58,26300 | 56,36675 | 28,88110 | 58,83737 | €14,67 | €29,33 | €0,42 | €0,55 |
| Master Adaptive Expanded V1 | H | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14001 | 0,14065 | 0,12321 | 0,07071 | 0,17362 | €176,03 | €352,07 | €42,25 | €1,60 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,43 | €72,87 | €1,62 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €618,57 | €1.237,14 | €44,16 | €0,00 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,26300 | 56,74249 | 29,07362 | 59,22958 | €1.494,18 | €2.988,35 | €43,03 | €35,89 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1165,32878 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,00 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54904 | 824,18962 | 1768,58749 | €850,90 | €1.701,80 | €47,45 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Combo Adaptive — Side × Regime Guard | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive — Side × Regime Guard | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,06993 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €-1,14 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €23,19 |
| Combo Adaptive — Side × Regime Guard | ACE | SHORT | Combo Adaptive | 60m | 2,0x | 0,15317 | 0,15317 | 0,15317 | 0,22899 | 0,11641 | €207,74 | €415,49 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 74,46310 | 75,06600 | 75,53537 | 111,32234 | 72,31857 | €47,34 | €94,69 | €1,36 | €-0,77 |
| Master Adaptive GB20 — Breakeven 0,5R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,11 | €74,22 | €1,65 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €630,00 | €1.260,01 | €44,98 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,26300 | 56,74249 | 29,07362 | 59,22958 | €1.521,79 | €3.043,59 | €43,83 | €36,56 |
| Master Adaptive GB20 — 50% a 0,75R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,07 | €74,14 | €1,65 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €629,33 | €1.258,67 | €44,93 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,26300 | 56,74249 | 29,07362 | 59,22958 | €1.520,18 | €3.040,35 | €43,78 | €36,52 |
| Master Adaptive GB20 — Loss Cap 0,75R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,57152 | 58,26300 | 56,94975 | 29,07362 | 59,22958 | €1.805,69 | €3.611,39 | €39,00 | €43,38 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €143,50 | €430,49 | €51,66 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63026,30000 | 63317,47541 | 83175,15148 | 61564,22253 | €63,81 | €191,43 | €2,14 | €-1,25 |
| Rapida V3 NoHigh — Regime Guard | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €143,19 | €429,58 | €0,00 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,72026 | 0,76650 | 0,80669 | 0,95674 | 0,59061 | €139,52 | €418,56 | €50,23 | €-26,87 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99750 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €28,76 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63026,30000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €19,13 |
| MAIN — Side × Regime Guard | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,00998 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €-9,96 |
| MAIN — Side × Regime Guard | SOL | SHORT | Confluenza trend | 240m | 3,0x | 74,57408 | 75,06600 | 75,80558 | 99,05924 | 72,11109 | €47,14 | €141,41 | €2,34 | €-0,93 |
| Combo Trend — Side × Regime Guard | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,06993 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-11,91 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 0,99750 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €21,67 |
| Combo Trend — Side × Regime Guard | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| Combo Trend — Side × Regime Guard | ACE | SHORT | Combo Trend | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,09934 | €214,51 | €429,02 | €51,48 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTC | SHORT | Combo Trend | 60m | 2,0x | 62834,55058 | 63026,30000 | 63839,90339 | 93937,65311 | 60622,77440 | €105,21 | €210,42 | €3,37 | €-0,64 |
| FAST NoHigh <7,5 · SHORT only | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €0,00 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €136,56 | €409,67 | €49,16 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €135,49 | €406,48 | €0,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1889,64785 | 1888,46000 | 1868,48380 | 1269,21348 | 1921,39394 | €24,52 | €73,57 | €0,82 | €-0,05 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,00998 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €-2,63 |
| FAST NoHigh <7,5 · SHORT only | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,76314 | 0,76650 | 0,85472 | 1,01371 | 0,62578 | €137,15 | €411,45 | €49,37 | €-1,81 |
| Bilanciata V3 · LONG only | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| Bilanciata V3 · LONG only | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06993 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,17 |
| Bilanciata V3 · LONG only | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €432,90 | €1.298,70 | €46,36 | €0,00 |
| Bilanciata V3 · LONG only | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €120,86 | €362,58 | €43,51 | €-0,00 |
| Bilanciata V3 · LONG only | CYS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,72026 | 0,76650 | 0,80669 | 0,95674 | 0,54739 | €130,90 | €392,69 | €47,12 | €-25,21 |
| Bilanciata V3 · LONG only | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99750 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €0,21 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 62892,88891 | 63026,30000 | 63798,54651 | 83542,72076 | 61081,57371 | €37,97 | €113,91 | €1,64 | €-0,24 |
| Bilanciata V3 · LONG only | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,36815 | 0,35962 | 0,41233 | 0,48902 | 0,27979 | €126,96 | €380,87 | €45,70 | €8,82 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €0,50 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,68 | €403,35 | €48,40 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,06600 | 75,79399 | 111,70349 | 72,56617 | €21,81 | €43,62 | €0,63 | €-0,20 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,06993 | 0,07049 | 0,10388 | 0,06749 | €70,07 | €140,14 | €2,02 | €-0,89 |
| Scanner Bottom5 Short Profit Lock V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €205,68 | €411,36 | €49,36 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €205,47 | €410,94 | €49,31 | €14,63 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63026,30000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,40 | €90,81 | €1,31 | €-0,01 |
| Scanner Bottom5 Short Profit Lock V1 | ETH | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1874,85495 | 1888,46000 | 1901,85287 | 2802,90816 | 1820,85913 | €21,95 | €43,90 | €0,63 | €-0,32 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 0,99750 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €0,51 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,98 | €403,97 | €48,48 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,06600 | 75,79399 | 111,70349 | 72,56617 | €21,84 | €43,69 | €0,63 | €-0,20 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,06993 | 0,07049 | 0,10388 | 0,06749 | €70,18 | €140,35 | €2,02 | €-0,89 |
| Scanner Bottom5 Short Mfe Trail V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €205,99 | €411,99 | €49,44 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,35962 | 0,41764 | 0,55748 | 0,28340 | €205,79 | €411,57 | €49,39 | €14,65 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63026,30000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,47 | €90,94 | €1,31 | €-0,01 |
| Scanner Bottom5 Short Mfe Trail V1 | ETH | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1874,85495 | 1888,46000 | 1901,85287 | 2802,90816 | 1820,85913 | €21,98 | €43,96 | €0,63 | €-0,32 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FAST NoHigh <7,5 · SHORT only | ZEC | SHORT | 2026-08-17T02:05:57+00:00 | 492,12068 | €-1,25 | -1,13 | STOP |
| Master Adaptive Runner25 V1 | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,23524 | €2,00 | 2,83 | TARGET |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,34498 | €0,85 | 1,33 | TARGET |
| Rapida V3 senza ESPORTS — Long Only | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,34498 | €1,00 | 1,33 | TARGET |
| Rapida V3 — senza ESPORTS | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,34498 | €0,84 | 1,33 | TARGET |
| Rapida V3 — Long Only | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,34498 | €0,95 | 1,33 | TARGET |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,34498 | €1,99 | 1,33 | TARGET |
| Rapida 1H V3 Filtered — madre | HYPE | LONG | 2026-08-17T02:05:57+00:00 | 58,34498 | €0,84 | 1,33 | TARGET |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | 2026-08-17T02:05:57+00:00 | 492,12068 | €-1,28 | -1,13 | STOP |
| Bilanciata 1H — SHORT Trend Down stretto | ETH | SHORT | 2026-08-17T02:05:57+00:00 | 1901,43644 | €-1,40 | -1,39 | STOP_GAP_STRESS |
| Rapida V3 — senza ESPORTS | SOL | SHORT | 2026-08-17T01:05:42+00:00 | 74,98418 | €-5,50 | -0,14 | STOP_GAP_STRESS |
| Rapida V3 senza ESPORTS — MFE Lock | SOL | SHORT | 2026-08-17T01:05:42+00:00 | 74,98418 | €-5,54 | -0,14 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🧪 Validazione congiunta Research + Paper

I due campioni vengono letti insieme ma **non sommati**: il paper è normalmente un sottoinsieme dei segnali Research. La soglia usa gli **eventi di mercato indipendenti**.

Requisiti per la revisione live: almeno **30 eventi indipendenti per lato**, PF almeno **1,10**, expectancy positiva e max drawdown paper non superiore a **15,00%**.

| Profilo | Conto paper di riferimento | Research eventi | Paper eventi | PF Research | PF Paper | Exp. Research | Exp. Paper | DD Paper | Accordo | Stato |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 368/30 | 33/30 | 0,69 | 2,04 | -0,16R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 336/30 | 20/30 | 0,61 | 1,90 | -0,21R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 211/30 | 22/30 | 0,78 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 213/30 | 22/30 | 0,75 | 1,57 | -0,13R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 284/30 | 31/30 | 0,78 | 0,62 | -0,11R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 254/30 | 11/30 | 0,69 | 0,00 | -0,16R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 120/30 | 8/30 | 0,67 | 1,02 | -0,17R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 272/30 | 17/30 | 0,60 | 4,50 | -0,23R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 408/30 | 24/30 | 0,70 | 0,64 | -0,16R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 372/30 | 7/30 | 0,61 | 0,02 | -0,21R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 284/30 | 30/30 | 0,82 | 1,02 | -0,09R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 516/30 | 55/30 | 0,83 | 1,12 | -0,08R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 119/30 | 15/30 | 0,43 | 0,99 | -0,39R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 459/30 | 44/30 | 0,70 | 1,20 | -0,15R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 463/30 | 37/30 | 0,70 | 0,76 | -0,15R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 423/30 | 23/30 | 0,61 | 1,12 | -0,20R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 260/30 | 41/30 | 0,72 | 0,72 | -0,17R | €-9,22 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 21/30 | 0,00 | 2,09 | 0,00R | €22,40 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 14/30 | 0,53 | 0,61 | -0,26R | €-2,07 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 629/30 | 102/30 | 0,89 | 0,86 | -0,06R | €-2,70 | 8,61% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 44/30 | 0,00 | 0,48 | 0,00R | €-18,13 | 9,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 8/30 | 0,00 | 1,47 | 0,00R | €8,24 | 1,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 220/30 | 60/30 | 1,05 | 0,79 | 0,02R | €-5,03 | 6,62% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 394/30 | 90/30 | 0,91 | 0,99 | -0,05R | €-0,14 | 6,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 315/30 | 46/30 | 0,80 | 0,46 | -0,11R | €-12,04 | 6,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 172/30 | 29/30 | 0,95 | 1,05 | -0,02R | €1,12 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 428/30 | 72/30 | 0,80 | 0,98 | -0,10R | €-0,48 | 6,52% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 495/30 | 108/30 | 0,85 | 1,09 | -0,08R | €2,04 | 6,52% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 644/30 | 111/30 | 0,78 | 1,12 | -0,12R | €2,22 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 68/30 | 0,00 | 1,42 | 0,00R | €8,85 | 3,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 75/30 | 0,00 | 1,04 | 0,00R | €1,08 | 5,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 31/30 | 0,00 | 1,36 | 0,00R | €9,56 | 2,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 383/30 | 117/30 | 0,82 | 1,13 | -0,10R | €3,03 | 4,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 608/30 | 126/30 | 0,74 | 0,92 | -0,14R | €-1,70 | 3,95% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 48/30 | 27/30 | 0,57 | 0,72 | -0,25R | €-7,62 | 3,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 620/30 | 134/30 | 0,80 | 0,89 | -0,10R | €-2,43 | 7,14% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 453/30 | 108/30 | 0,79 | 1,06 | -0,11R | €1,38 | 6,72% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 252/30 | 73/30 | 0,92 | 0,75 | -0,04R | €-7,70 | 6,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 255/30 | 67/30 | 0,89 | 0,80 | -0,06R | €-5,71 | 5,23% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 345/30 | 82/30 | 0,85 | 0,62 | -0,08R | €-10,45 | 10,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 33/30 | 0,00 | 1,52 | 0,00R | €10,77 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 51/30 | 0,00 | 1,31 | 0,00R | €6,37 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 517/30 | 96/30 | 0,77 | 0,87 | -0,12R | €-3,28 | 6,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 62/30 | 0,00 | 0,75 | 0,00R | €-6,40 | 8,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 90/30 | 0,00 | 0,85 | 0,00R | €-2,91 | 7,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 35/30 | 0,00 | 0,84 | 0,00R | €-3,94 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 573/30 | 108/30 | 0,76 | 0,76 | -0,13R | €-5,44 | 7,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 243/30 | 36/30 | 0,73 | 0,81 | -0,19R | €-5,07 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 178/30 | 69/30 | 1,12 | 0,83 | 0,06R | €-4,37 | 6,53% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 10/30 | 5/30 | 0,72 | 0,89 | -0,13R | €-2,34 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 13/30 | 6/30 | 0,24 | 1,27 | -0,59R | €4,89 | 1,49% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 4/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 14/30 | 8/30 | 0,89 | 0,63 | -0,06R | €-12,29 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,23% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 506/30 | 71/30 | 0,98 | 0,87 | -0,01R | €-2,42 | 5,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 278/30 | 43/30 | 0,98 | 0,64 | -0,01R | €-10,13 | 5,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 540/30 | 83/30 | 0,97 | 0,43 | -0,01R | €-13,66 | 11,70% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 447/30 | 72/30 | 0,93 | 0,61 | -0,04R | €-7,81 | 6,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 60/30 | 21/30 | 1,19 | 0,51 | 0,09R | €-17,79 | 4,14% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 60/30 | 21/30 | 1,13 | 0,36 | 0,06R | €-23,56 | 5,35% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 146/30 | 40/30 | 0,88 | 0,54 | -0,06R | €-12,15 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 186/30 | 30/30 | 0,85 | 0,60 | -0,08R | €-10,32 | 3,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 75/30 | 0,74 | 0,74 | -0,20R | €-5,16 | 6,78% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 54/30 | 0,00 | 0,97 | 0,00R | €-0,53 | 6,65% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 56/30 | 0,74 | 0,54 | -0,20R | €-10,11 | 6,78% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 84/30 | 30/30 | 1,20 | 0,70 | 0,09R | €-10,29 | 5,09% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 317/30 | 67/30 | 1,07 | 0,57 | 0,04R | €-13,04 | 10,70% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 418/30 | 99/30 | 0,90 | 0,78 | -0,06R | €-5,94 | 9,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 44/30 | 0,00 | 1,35 | 0,00R | €6,35 | 2,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 12/30 | 9/30 | 0,51 | 0,77 | -0,36R | €-5,63 | 2,06% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 18/30 | 12/30 | 0,40 | 0,94 | -0,41R | €-1,28 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 199/30 | 60/30 | 0,80 | 1,46 | -0,13R | €11,01 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 129/30 | 28/30 | 0,75 | 1,71 | -0,15R | €14,62 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 421/30 | 67/30 | 0,88 | 0,54 | -0,07R | €-11,78 | 8,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 14/30 | 8/30 | 0,30 | 0,05 | -0,56R | €-38,45 | 3,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 12/30 | 6/30 | 0,31 | 0,34 | -0,58R | €-30,47 | 2,40% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 20/30 | 10/30 | 0,29 | 0,12 | -0,55R | €-37,78 | 4,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 12/30 | 15/30 | 0,89 | 0,35 | -0,07R | €-21,51 | 3,52% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 256/30 | 44/30 | 0,97 | 0,65 | -0,02R | €-12,74 | 5,92% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 42/30 | 0,00 | 0,49 | 0,00R | €-16,68 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 32/30 | 0,00 | 0,30 | 0,00R | €-30,36 | 11,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 37/30 | 0,00 | 0,46 | 0,00R | €-19,20 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 481/30 | 74/30 | 1,38 | 0,49 | 0,12R | €-11,75 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 226/30 | 43/30 | 0,99 | 0,62 | -0,01R | €-14,97 | 6,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 235/30 | 39/30 | 0,95 | 0,50 | -0,03R | €-19,95 | 8,05% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 162/30 | 45/30 | 0,97 | 0,48 | -0,02R | €-24,32 | 11,51% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 248/30 | 39/30 | 0,94 | 0,50 | -0,04R | €-19,14 | 7,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 531/30 | 83/30 | 0,85 | 0,64 | -0,09R | €-8,70 | 9,65% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 212/30 | 69/30 | 1,17 | 0,87 | 0,09R | €-4,16 | 8,11% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 184/30 | 50/30 | 0,51 | 0,95 | -0,27R | €-0,95 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 184/30 | 50/30 | 0,51 | 0,95 | -0,27R | €-0,95 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 184/30 | 50/30 | 0,51 | 0,95 | -0,27R | €-0,95 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 218/30 | 70/30 | 0,70 | 0,85 | -0,16R | €-2,94 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 219/30 | 42/30 | 0,75 | 0,87 | -0,11R | €-2,73 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 196/30 | 43/30 | 0,65 | 0,84 | -0,16R | €-3,02 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 255/30 | 43/30 | 1,00 | 0,41 | -0,00R | €-19,80 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 256/30 | 43/30 | 0,99 | 0,41 | -0,01R | €-19,80 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 256/30 | 43/30 | 0,99 | 0,41 | -0,01R | €-19,80 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 305/30 | 62/30 | 1,08 | 0,77 | 0,04R | €-6,31 | 9,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 125/30 | 10/30 | 0,87 | 0,87 | -0,07R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 258/30 | 43/30 | 0,92 | 0,42 | -0,04R | €-19,02 | 10,22% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 271/30 | 58/30 | 1,17 | 0,66 | 0,07R | €-10,41 | 6,18% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 226/30 | 43/30 | 1,05 | 0,70 | 0,02R | €-10,22 | 6,91% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 282/30 | 65/30 | 1,17 | 0,60 | 0,07R | €-11,93 | 7,96% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 234/30 | 48/30 | 1,05 | 0,65 | 0,03R | €-11,57 | 6,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 321/30 | 55/30 | 1,06 | 0,34 | 0,03R | €-18,05 | 10,78% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 254/30 | 51/30 | 0,97 | 0,53 | -0,02R | €-14,08 | 10,40% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 240/30 | 47/30 | 0,97 | 0,53 | -0,02R | €-15,17 | 10,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 333/30 | 71/30 | 1,11 | 0,97 | 0,06R | €-0,94 | 8,85% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 20/30 | 9/30 | 0,38 | 0,17 | -0,51R | €-36,20 | 4,23% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 2/30 | 2/30 | 1,18 | 0,65 | 0,10R | €-8,96 | 0,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 11/30 | 5/30 | 0,61 | 0,82 | -0,24R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 15/30 | 7/30 | 0,55 | 0,63 | -0,34R | €-9,88 | 2,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 2/30 | 2/30 | 1,29 | 0,71 | 0,15R | €-7,50 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 18/30 | 8/30 | 0,54 | 0,43 | -0,36R | €-23,29 | 3,07% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,05R | €-51,41 | 1,76% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06993**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.6 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63026.3 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07012**; close **0.06996**; wick alta **18.8%**; volume **x0.15**

### Gestione

- TP1 0,07107: chiude 25% e porta lo stop residuo al pareggio costi.
- TP2 0,06961: chiude 25% e porta lo stop residuo a TP1.
- TP3 0,06400: chiude 25% e porta lo stop residuo a TP2.
- TP4 0,06000: chiude l’ultimo 25%.
- Stop iniziale dinamico: almeno 0,08060, sopra il massimo della rejection con buffer 0,2%, mai oltre 0,08120.
- Politica conservativa: se stop e target sono toccati nella stessa candela, prevale lo stop.

## 🔬 Research All Signals

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **TRANSITION**
- Famiglia: **TRANSITION**
- Confidenza: **78,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Segnali contrastanti tra trend BTC, breadth e forza delle altcoin.
- BTC trend score: **-3,00**; ADX: **28,39**; breadth sopra EMA50: **58,33%**
- Mediana alt vs BTC: **0,46%**; dispersione: **6,29%**

- Aperti in questo ciclo: **63**
- Chiusi in questo ciclo: **33**
- Posizioni research aperte: **739**
- Trade research chiusi: **24729**
- Eventi di mercato indipendenti chiusi: **3430**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **64291**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 8 | 368 | 368 | 29,89% | 0,69 | -0,16R | €-601,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 8 | 336 | 336 | 28,87% | 0,61 | -0,21R | €-702,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 3 | 211 | 211 | 45,97% | 0,78 | -0,12R | €-244,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 3 | 213 | 213 | 31,92% | 0,75 | -0,13R | €-269,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 5 | 284 | 284 | 31,69% | 0,78 | -0,11R | €-321,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 5 | 254 | 254 | 31,50% | 0,69 | -0,16R | €-398,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 120 | 120 | 34,17% | 0,67 | -0,17R | €-207,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 3 | 272 | 272 | 26,84% | 0,60 | -0,23R | €-621,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 13 | 408 | 408 | 29,41% | 0,70 | -0,16R | €-644,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 13 | 372 | 372 | 28,23% | 0,61 | -0,21R | €-765,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 5 | 284 | 284 | 32,39% | 0,82 | -0,09R | €-262,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 12 | 516 | 516 | 40,12% | 0,83 | -0,08R | €-403,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 119 | 119 | 27,73% | 0,43 | -0,39R | €-459,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 13 | 459 | 459 | 29,19% | 0,70 | -0,15R | €-709,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 13 | 463 | 463 | 29,16% | 0,70 | -0,15R | €-709,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 13 | 423 | 423 | 27,90% | 0,61 | -0,20R | €-852,91 |
| MAIN | 21 | 260 | 260 | 25,77% | 0,72 | -0,17R | €-436,27 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 18 | 629 | 629 | 33,23% | 0,89 | -0,06R | €-370,84 |
| Bilanciata 1H V2 | 6 | 252 | 220 | 36,90% | 1,05 | 0,02R | €62,36 |
| Bilanciata 1H V3 Filtered | 12 | 394 | 394 | 34,01% | 0,91 | -0,05R | €-196,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 12 | 315 | 315 | 32,70% | 0,80 | -0,11R | €-342,09 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 172 | 172 | 37,79% | 0,95 | -0,02R | €-41,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 9 | 428 | 428 | 34,58% | 0,80 | -0,10R | €-423,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 9 | 495 | 495 | 35,76% | 0,85 | -0,08R | €-388,88 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 14 | 644 | 644 | 33,70% | 0,78 | -0,12R | €-762,39 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 7 | 383 | 383 | 34,99% | 0,82 | -0,10R | €-367,03 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 608 | 608 | 30,59% | 0,74 | -0,14R | €-848,05 |
| Rapida 1H V2 | 1 | 56 | 48 | 35,71% | 0,57 | -0,25R | €-140,57 |
| Rapida 1H V3 Filtered | 13 | 620 | 620 | 34,35% | 0,80 | -0,10R | €-648,25 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 8 | 453 | 453 | 34,44% | 0,79 | -0,11R | €-510,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 252 | 252 | 47,62% | 0,92 | -0,04R | €-103,24 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 255 | 255 | 36,86% | 0,89 | -0,06R | €-144,54 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 5 | 345 | 345 | 36,23% | 0,85 | -0,08R | €-263,92 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 13 | 517 | 517 | 33,66% | 0,77 | -0,12R | €-616,21 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 13 | 573 | 573 | 33,33% | 0,76 | -0,13R | €-730,21 |
| SHADOW_4H_WIDE | 31 | 243 | 243 | 20,58% | 0,73 | -0,19R | €-452,63 |
| SHADOW_BOLLINGER_MR_1H | 2 | 178 | 178 | 48,31% | 1,12 | 0,06R | €101,01 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 10 | 10 | 60,00% | 0,72 | -0,13R | €-12,66 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 13 | 13 | 30,77% | 0,24 | -0,59R | €-76,75 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,93 |
| SHADOW_BTC_EMA_1H | 1 | 14 | 14 | 50,00% | 0,89 | -0,06R | €-8,68 |
| SHADOW_BTC_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 17 | 506 | 506 | 36,56% | 0,98 | -0,01R | €-62,24 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 8 | 278 | 278 | 35,97% | 0,98 | -0,01R | €-30,76 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 16 | 540 | 540 | 40,74% | 0,97 | -0,01R | €-74,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 17 | 447 | 447 | 39,15% | 0,93 | -0,04R | €-159,24 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 4 | 60 | 60 | 45,00% | 1,19 | 0,09R | €51,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 4 | 60 | 60 | 36,67% | 1,13 | 0,06R | €34,12 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 6 | 146 | 146 | 31,51% | 0,88 | -0,06R | €-87,92 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 8 | 186 | 186 | 34,41% | 0,85 | -0,08R | €-142,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 3 | 84 | 84 | 48,81% | 1,20 | 0,09R | €74,89 |
| SHADOW_COMBO_SCANNER | 9 | 317 | 317 | 34,70% | 1,07 | 0,04R | €113,23 |
| SHADOW_COMBO_TREND | 18 | 418 | 418 | 31,10% | 0,90 | -0,06R | €-231,60 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 12 | 12 | 33,33% | 0,51 | -0,36R | €-43,62 |
| SHADOW_DOGE_EMA_1H | 0 | 18 | 18 | 27,78% | 0,40 | -0,41R | €-73,66 |
| SHADOW_DONCHIAN_1H | 10 | 199 | 199 | 29,15% | 0,80 | -0,13R | €-256,40 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 10 | 129 | 129 | 31,01% | 0,75 | -0,15R | €-191,32 |
| SHADOW_EMA_TREND_1H | 19 | 421 | 421 | 30,64% | 0,88 | -0,07R | €-281,04 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 14 | 14 | 28,57% | 0,30 | -0,56R | €-77,90 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 12 | 12 | 25,00% | 0,31 | -0,58R | €-70,11 |
| SHADOW_ETH_EMA_1H | 0 | 20 | 20 | 30,00% | 0,29 | -0,55R | €-110,17 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 1 | 12 | 12 | 41,67% | 0,89 | -0,07R | €-8,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 11 | 256 | 256 | 32,03% | 0,97 | -0,02R | €-47,38 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 481 | 481 | 66,11% | 1,38 | 0,12R | €594,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 10 | 226 | 226 | 32,30% | 0,99 | -0,01R | €-15,64 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 10 | 235 | 235 | 30,21% | 0,95 | -0,03R | €-78,89 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 8 | 162 | 162 | 32,10% | 0,97 | -0,02R | €-34,45 |
| SHADOW_MASTER_ADAPTIVE_V1 | 10 | 248 | 248 | 31,45% | 0,94 | -0,04R | €-93,14 |
| Forza relativa 1H V1 | 18 | 531 | 531 | 28,63% | 0,85 | -0,09R | €-461,84 |
| Forza relativa 1H V2 | 8 | 227 | 212 | 36,12% | 1,17 | 0,09R | €201,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 10 | 184 | 184 | 26,63% | 0,51 | -0,27R | €-503,23 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 10 | 184 | 184 | 26,63% | 0,51 | -0,27R | €-503,23 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 10 | 184 | 184 | 26,63% | 0,51 | -0,27R | €-503,23 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 218 | 218 | 29,36% | 0,70 | -0,16R | €-351,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 10 | 219 | 219 | 52,51% | 0,75 | -0,11R | €-248,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 10 | 196 | 196 | 51,53% | 0,65 | -0,16R | €-304,09 |
| SHADOW_SCANNER_TOP10_LONG | 8 | 255 | 255 | 34,51% | 1,00 | -0,00R | €-4,13 |
| SHADOW_SCANNER_TOP15_LONG | 8 | 256 | 256 | 34,38% | 0,99 | -0,01R | €-15,24 |
| SHADOW_SCANNER_TOP20_LONG | 8 | 256 | 256 | 34,38% | 0,99 | -0,01R | €-15,24 |
| SHADOW_SCANNER_TOP5_BTC | 9 | 305 | 305 | 34,10% | 1,08 | 0,04R | €134,26 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 125 | 125 | 31,20% | 0,87 | -0,07R | €-91,35 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 9 | 258 | 258 | 32,17% | 0,92 | -0,04R | €-108,28 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 6 | 271 | 271 | 45,39% | 1,17 | 0,07R | €192,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 8 | 226 | 226 | 34,07% | 1,05 | 0,02R | €55,72 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 6 | 282 | 282 | 45,04% | 1,17 | 0,07R | €204,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 8 | 234 | 234 | 33,76% | 1,05 | 0,03R | €66,54 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 8 | 321 | 321 | 43,61% | 1,06 | 0,03R | €90,10 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 9 | 254 | 254 | 31,50% | 0,97 | -0,02R | €-40,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 9 | 240 | 240 | 30,83% | 0,97 | -0,02R | €-38,62 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 333 | 333 | 36,04% | 1,11 | 0,06R | €185,31 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 20 | 20 | 25,00% | 0,38 | -0,51R | €-102,79 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,93 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 11 | 11 | 45,45% | 0,61 | -0,24R | €-26,43 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 15 | 15 | 33,33% | 0,55 | -0,34R | €-50,34 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 2 | 2 | 50,00% | 1,29 | 0,15R | €3,02 |
| SHADOW_SOL_EMA_1H | 1 | 18 | 18 | 27,78% | 0,54 | -0,36R | €-65,49 |
| SHADOW_SOL_EMA_4H | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,62 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 36 | 36 | 22,22% | 0,48 | -0,32R | €-116,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 53 | 53 | 41,51% | 1,26 | 0,13R | €66,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 109 | 109 | 33,94% | 0,64 | -0,19R | €-202,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,22 | -0,53R | €-42,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 3 | 49 | 49 | 30,61% | 0,92 | -0,04R | €-17,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 5 | 54 | 54 | 29,63% | 0,59 | -0,24R | €-131,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 52 | 52 | 17,31% | 0,47 | -0,26R | €-137,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 35 | 35 | 20,00% | 0,30 | -0,49R | €-170,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 40 | 40 | 42,50% | 1,39 | 0,18R | €70,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 102 | 102 | 33,33% | 0,53 | -0,24R | €-249,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,17 | -0,64R | €-44,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 3 | 48 | 48 | 31,25% | 1,04 | 0,02R | €9,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 5 | 50 | 50 | 28,00% | 0,55 | -0,26R | €-129,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 49 | 49 | 16,33% | 0,31 | -0,36R | €-177,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,78 | -0,12R | €-7,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 64 | 64 | 39,06% | 0,48 | -0,33R | €-208,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 2 | 28 | 28 | 57,14% | 1,11 | 0,05R | €13,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 1 | 29 | 29 | 44,83% | 0,70 | -0,17R | €-49,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 1,08 | 0,04R | €1,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-207,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 2 | 28 | 28 | 28,57% | 0,94 | -0,02R | €-6,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 1 | 29 | 29 | 31,03% | 0,68 | -0,20R | €-58,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 51 | 51 | 37,25% | 1,00 | -0,00R | €-0,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 78 | 78 | 33,33% | 0,62 | -0,22R | €-170,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 3 | 39 | 39 | 33,33% | 1,22 | 0,09R | €34,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 2 | 38 | 38 | 34,21% | 0,83 | -0,09R | €-35,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,18 | -0,48R | €-43,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 43 | 43 | 37,21% | 1,03 | 0,01R | €5,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 68 | 68 | 35,29% | 0,55 | -0,24R | €-163,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,92R | €-55,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 3 | 38 | 38 | 34,21% | 1,31 | 0,12R | €46,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 2 | 35 | 35 | 31,43% | 0,61 | -0,22R | €-76,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 118 | 118 | 33,90% | 0,65 | -0,18R | €-216,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,73 | -0,16R | €-83,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 104 | 104 | 32,69% | 0,66 | -0,19R | €-193,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 31 | 31 | 19,35% | 0,69 | -0,16R | €-49,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 3 | 52 | 52 | 26,92% | 0,64 | -0,19R | €-100,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,14 | -0,67R | €-161,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 133 | 133 | 33,08% | 0,65 | -0,19R | €-249,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 4 | 46 | 46 | 23,91% | 0,72 | -0,13R | €-58,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 9 | 69 | 69 | 31,88% | 0,74 | -0,13R | €-90,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 71 | 71 | 23,94% | 0,65 | -0,17R | €-119,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,09 | -0,71R | €-171,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 0 | 124 | 124 | 32,26% | 0,58 | -0,22R | €-275,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 4 | 45 | 45 | 24,44% | 0,72 | -0,13R | €-56,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 9 | 63 | 63 | 30,16% | 0,69 | -0,16R | €-97,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 66 | 66 | 22,73% | 0,47 | -0,27R | €-176,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 52 | 52 | 38,46% | 1,07 | 0,04R | €18,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 78 | 78 | 35,90% | 0,74 | -0,14R | €-110,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 3 | 39 | 39 | 33,33% | 1,22 | 0,09R | €34,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 2 | 38 | 38 | 34,21% | 0,83 | -0,09R | €-35,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 0 | 53 | 53 | 32,08% | 0,42 | -0,35R | €-184,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 66 | 66 | 45,45% | 1,02 | 0,01R | €7,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 147 | 147 | 38,10% | 0,80 | -0,09R | €-134,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 18 | 18 | 33,33% | 0,47 | -0,34R | €-61,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 4 | 62 | 62 | 46,77% | 1,35 | 0,11R | €69,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 8 | 82 | 82 | 41,46% | 0,88 | -0,05R | €-39,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 81 | 81 | 40,74% | 0,84 | -0,07R | €-56,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 48 | 48 | 37,50% | 0,47 | -0,32R | €-151,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 1 | 12 | 12 | 33,33% | 0,57 | -0,20R | €-24,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 0 | 60 | 60 | 35,00% | 0,99 | -0,01R | €-4,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 129 | 129 | 32,56% | 0,64 | -0,20R | €-254,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,35 | -0,42R | €-76,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 4 | 56 | 56 | 32,14% | 1,19 | 0,08R | €42,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 9 | 69 | 69 | 31,88% | 0,74 | -0,13R | €-90,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 130 | 130 | 32,31% | 0,63 | -0,20R | €-264,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,35 | -0,42R | €-76,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 4 | 56 | 56 | 32,14% | 1,19 | 0,08R | €42,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 9 | 69 | 69 | 31,88% | 0,74 | -0,13R | €-90,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,26 | -0,48R | €-230,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 0 | 122 | 122 | 31,15% | 0,50 | -0,27R | €-325,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,36 | -0,44R | €-61,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 4 | 55 | 55 | 32,73% | 1,28 | 0,11R | €62,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 9 | 63 | 63 | 30,16% | 0,69 | -0,16R | €-97,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 65 | 65 | 21,54% | 0,39 | -0,31R | €-201,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,89 | -0,05R | €-10,79 |
| MAIN | ALT_ROTATION_UP | 3 | 39 | 39 | 17,95% | 0,31 | -0,51R | €-196,95 |
| MAIN | RANGE | 2 | 71 | 71 | 22,54% | 0,65 | -0,22R | €-154,64 |
| MAIN | RANGE_HIGH_VOL | 0 | 10 | 10 | 30,00% | 1,06 | 0,03R | €2,61 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 4 | 35 | 35 | 25,71% | 0,65 | -0,23R | €-79,75 |
| MAIN | TREND_DOWN | 10 | 37 | 37 | 24,32% | 0,74 | -0,15R | €-55,68 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 1 | 38 | 38 | 31,58% | 1,05 | 0,03R | €11,82 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,42 | 0,25R | €17,52 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 0,85 | -0,07R | €-9,35 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 21,43% | 0,44 | -0,39R | €-221,17 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 82 | 82 | 35,37% | 0,96 | -0,02R | €-18,44 |
| Bilanciata 1H V1 | RANGE | 0 | 167 | 167 | 38,92% | 1,07 | 0,04R | €62,38 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 28 | 28 | 17,86% | 0,35 | -0,47R | €-131,64 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 5 | 91 | 91 | 38,46% | 1,23 | 0,11R | €103,63 |
| Bilanciata 1H V1 | TREND_DOWN | 13 | 74 | 74 | 32,43% | 0,76 | -0,12R | €-89,61 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 109 | 109 | 30,28% | 0,92 | -0,04R | €-40,50 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 58 | 49 | 37,93% | 1,12 | 0,06R | €34,42 |
| Bilanciata 1H V2 | RANGE | 0 | 119 | 107 | 34,45% | 0,82 | -0,11R | €-128,12 |
| Bilanciata 1H V2 | TRANSITION | 6 | 75 | 64 | 40,00% | 1,44 | 0,21R | €156,07 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 42 | 42 | 26,19% | 0,54 | -0,30R | €-128,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 45 | 45 | 31,11% | 1,08 | 0,05R | €21,32 |
| Bilanciata 1H V3 Filtered | RANGE | 0 | 114 | 114 | 40,35% | 1,09 | 0,04R | €49,41 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,49 | -0,33R | €-26,67 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 4 | 50 | 50 | 36,00% | 1,15 | 0,07R | €35,73 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 8 | 53 | 53 | 33,96% | 0,54 | -0,27R | €-142,16 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 62 | 62 | 30,65% | 1,06 | 0,03R | €18,24 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 19,35% | 0,26 | -0,52R | €-161,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 32,56% | 1,18 | 0,10R | €42,31 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 0 | 92 | 92 | 38,04% | 0,86 | -0,07R | €-66,75 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,82 | -0,10R | €-5,84 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 4 | 42 | 42 | 35,71% | 1,16 | 0,07R | €30,04 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 8 | 54 | 54 | 33,33% | 0,52 | -0,28R | €-153,27 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 41 | 41 | 24,39% | 0,78 | -0,10R | €-42,60 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,25 | -0,50R | €-54,74 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 48,84% | 1,27 | 0,11R | €46,79 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 42 | 42 | 38,10% | 0,93 | -0,04R | €-16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 30,61% | 0,80 | -0,08R | €-38,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 15,79% | 0,25 | -0,52R | €-99,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 64 | 64 | 45,31% | 1,11 | 0,05R | €33,16 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 0 | 142 | 142 | 35,21% | 0,79 | -0,11R | €-156,31 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 3 | 53 | 53 | 37,74% | 0,99 | -0,00R | €-1,19 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 6 | 74 | 74 | 31,08% | 0,64 | -0,21R | €-158,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 73 | 73 | 27,40% | 0,74 | -0,12R | €-84,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 18,92% | 0,33 | -0,49R | €-181,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 0 | 172 | 172 | 39,53% | 0,99 | -0,01R | €-11,12 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 3 | 55 | 55 | 40,00% | 1,13 | 0,05R | €28,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 6 | 74 | 74 | 31,08% | 0,64 | -0,21R | €-158,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 89 | 89 | 26,97% | 0,65 | -0,18R | €-156,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 77 | 77 | 20,78% | 0,38 | -0,43R | €-330,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 72 | 72 | 38,89% | 0,87 | -0,07R | €-51,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 0 | 193 | 193 | 36,79% | 0,83 | -0,09R | €-177,92 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 20 | 20 | 40,00% | 0,96 | -0,02R | €-4,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 4 | 78 | 78 | 39,74% | 1,18 | 0,07R | €57,61 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 10 | 91 | 91 | 31,87% | 0,68 | -0,17R | €-153,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 104 | 104 | 27,88% | 0,70 | -0,15R | €-160,49 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 22,73% | 0,37 | -0,46R | €-202,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 37,25% | 0,89 | -0,06R | €-29,33 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 112 | 112 | 42,86% | 1,13 | 0,06R | €70,10 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 50,00% | 1,08 | 0,04R | €3,46 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 3 | 49 | 49 | 38,78% | 1,17 | 0,07R | €34,01 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 4 | 55 | 55 | 29,09% | 0,57 | -0,24R | €-134,59 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,60 | -0,22R | €-127,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 75 | 75 | 20,00% | 0,42 | -0,40R | €-298,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 40,54% | 1,06 | 0,03R | €24,26 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 177 | 177 | 34,46% | 0,78 | -0,12R | €-213,07 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,51 | -0,30R | €-57,10 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 4 | 73 | 73 | 36,99% | 1,31 | 0,13R | €92,57 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 10 | 84 | 84 | 30,95% | 0,68 | -0,17R | €-146,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 95 | 95 | 21,05% | 0,53 | -0,25R | €-237,49 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 0 | 40 | 33 | 37,50% | 0,73 | -0,14R | €-57,99 |
| Rapida 1H V2 | TRANSITION | 1 | 6 | 6 | 50,00% | 0,58 | -0,17R | €-10,03 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 74 | 74 | 20,27% | 0,37 | -0,43R | €-315,89 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 69 | 69 | 39,13% | 0,94 | -0,03R | €-22,82 |
| Rapida 1H V3 Filtered | RANGE | 0 | 172 | 172 | 37,21% | 0,83 | -0,09R | €-157,33 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 19 | 19 | 36,84% | 0,84 | -0,09R | €-17,03 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 4 | 70 | 70 | 37,14% | 1,05 | 0,02R | €16,26 |
| Rapida 1H V3 Filtered | TREND_DOWN | 9 | 80 | 80 | 31,25% | 0,70 | -0,16R | €-124,69 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 108 | 108 | 37,04% | 1,00 | 0,00R | €0,97 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-232,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 41,67% | 1,03 | 0,01R | €8,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 140 | 140 | 38,57% | 0,92 | -0,04R | €-58,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,84 | -0,08R | €-8,44 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 3 | 52 | 52 | 36,54% | 0,95 | -0,02R | €-11,22 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 5 | 60 | 60 | 30,00% | 0,64 | -0,20R | €-122,51 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 69 | 69 | 28,99% | 0,67 | -0,17R | €-116,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 23,08% | 0,19 | -0,65R | €-84,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 79 | 79 | 43,04% | 0,86 | -0,08R | €-63,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 2 | 29 | 29 | 58,62% | 1,39 | 0,16R | €45,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 1 | 32 | 32 | 43,75% | 0,84 | -0,09R | €-30,04 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 16,67% | 0,19 | -0,63R | €-75,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 81 | 81 | 39,51% | 0,94 | -0,03R | €-27,15 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 2 | 29 | 29 | 37,93% | 1,17 | 0,07R | €19,97 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 32 | 32 | 34,38% | 0,76 | -0,15R | €-46,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 5,56% | 0,10 | -0,73R | €-131,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 38,33% | 0,88 | -0,07R | €-39,77 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 97 | 97 | 40,21% | 0,92 | -0,04R | €-38,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,27 | -0,57R | €-40,24 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 3 | 44 | 44 | 40,91% | 1,21 | 0,08R | €36,94 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 2 | 45 | 45 | 35,56% | 0,79 | -0,12R | €-52,58 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 17,39% | 0,32 | -0,51R | €-234,33 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 0 | 174 | 174 | 38,51% | 0,88 | -0,06R | €-109,28 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 4 | 54 | 54 | 31,48% | 0,86 | -0,06R | €-32,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 9 | 80 | 80 | 31,25% | 0,70 | -0,16R | €-124,69 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 94 | 94 | 31,91% | 0,79 | -0,11R | €-104,22 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 73 | 73 | 20,55% | 0,38 | -0,42R | €-304,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 68 | 68 | 36,76% | 0,83 | -0,09R | €-63,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 170 | 170 | 37,06% | 0,81 | -0,10R | €-172,06 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 38,89% | 0,93 | -0,04R | €-6,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 4 | 65 | 65 | 36,92% | 1,07 | 0,03R | €19,02 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 9 | 80 | 80 | 31,25% | 0,70 | -0,16R | €-124,69 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 91 | 91 | 30,77% | 0,75 | -0,13R | €-121,78 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 1,26 | 0,13R | €18,79 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 34 | 34 | 23,53% | 0,48 | -0,41R | €-138,96 |
| SHADOW_4H_WIDE | RANGE | 4 | 64 | 64 | 15,62% | 0,62 | -0,27R | €-173,23 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 7 | 7 | 28,57% | 1,10 | 0,07R | €5,07 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 36 | 36 | 13,89% | 0,39 | -0,45R | €-163,12 |
| SHADOW_4H_WIDE | TREND_DOWN | 12 | 35 | 35 | 28,57% | 1,18 | 0,11R | €37,52 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 38 | 38 | 23,68% | 1,04 | 0,02R | €8,48 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 0,99 | -0,00R | €-0,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 64 | 64 | 48,44% | 1,13 | 0,06R | €37,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-3,07 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 12 | 12 | 58,33% | 2,20 | 0,43R | €51,27 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 2 | 16 | 16 | 62,50% | 2,41 | 0,38R | €60,82 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 1 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,56 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,62 | -0,24R | €-109,67 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 59 | 59 | 35,59% | 0,97 | -0,01R | €-8,05 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 2 | 138 | 138 | 42,03% | 0,97 | -0,01R | €-19,04 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,83 | -0,09R | €-14,56 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 3 | 70 | 70 | 41,43% | 1,45 | 0,21R | €147,85 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 12 | 63 | 63 | 34,92% | 0,89 | -0,05R | €-34,05 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 94 | 94 | 36,17% | 1,12 | 0,05R | €48,17 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 15,38% | 0,48 | -0,33R | €-42,51 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 35,85% | 1,00 | -0,00R | €-1,04 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 67 | 67 | 47,76% | 1,21 | 0,10R | €70,23 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,56 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 3 | 37 | 37 | 45,95% | 2,06 | 0,35R | €130,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 4 | 40 | 40 | 35,00% | 1,06 | 0,03R | €11,08 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,58 | -0,25R | €-135,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 67 | 67 | 38,81% | 0,91 | -0,05R | €-30,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 1 | 137 | 137 | 41,61% | 1,11 | 0,05R | €68,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 18 | 18 | 44,44% | 0,79 | -0,10R | €-17,63 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 3 | 60 | 60 | 46,67% | 1,24 | 0,10R | €61,80 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 12 | 86 | 86 | 37,21% | 0,86 | -0,05R | €-44,34 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 96 | 96 | 50,00% | 1,33 | 0,13R | €127,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,65 | -0,22R | €-102,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 57 | 57 | 36,84% | 1,01 | 0,00R | €2,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 2 | 126 | 126 | 45,24% | 1,04 | 0,02R | €27,43 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 40,00% | 1,14 | 0,06R | €9,01 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 3 | 53 | 53 | 45,28% | 1,34 | 0,15R | €80,67 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 12 | 63 | 63 | 38,10% | 0,89 | -0,05R | €-31,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 73 | 73 | 36,99% | 0,73 | -0,12R | €-87,95 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 4 | 30 | 30 | 33,33% | 0,80 | -0,12R | €-34,81 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 4 | 30 | 30 | 33,33% | 0,82 | -0,11R | €-32,35 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 23,53% | 0,44 | -0,34R | €-57,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 38 | 38 | 39,47% | 1,17 | 0,09R | €34,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,65 | -0,18R | €-10,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 3 | 25 | 25 | 36,00% | 1,06 | 0,03R | €8,29 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 2 | 26 | 26 | 26,92% | 0,68 | -0,15R | €-39,75 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 8 | 74 | 74 | 37,84% | 1,05 | 0,03R | €19,17 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 99 | 99 | 34,34% | 0,80 | -0,09R | €-93,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,36 | -0,53R | €-68,31 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,42 | -0,30R | €-33,27 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 2,02 | 0,45R | €22,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 32 | 32 | 50,00% | 1,38 | 0,18R | €57,26 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,79R | €-23,63 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 5 | 5 | 80,00% | 4,65 | 0,83R | €41,31 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 3 | 11 | 11 | 54,55% | 0,97 | -0,01R | €-1,62 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,21 | -0,55R | €-82,64 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 1,09 | 0,05R | €25,32 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 76 | 76 | 44,74% | 1,40 | 0,20R | €150,28 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,23 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 5 | 52 | 52 | 42,31% | 1,58 | 0,28R | €144,99 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 3 | 41 | 41 | 29,27% | 0,72 | -0,16R | €-65,73 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 0 | 35 | 35 | 25,71% | 0,65 | -0,21R | €-73,73 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,77 | -0,15R | €-76,54 |
| SHADOW_COMBO_TREND | RANGE | 4 | 114 | 114 | 33,33% | 0,92 | -0,05R | €-54,84 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 12 | 12 | 33,33% | 1,06 | 0,03R | €3,37 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 59 | 59 | 35,59% | 1,30 | 0,16R | €93,33 |
| SHADOW_COMBO_TREND | TREND_DOWN | 11 | 56 | 56 | 30,36% | 0,75 | -0,14R | €-75,89 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 72 | 72 | 29,17% | 1,03 | 0,01R | €9,60 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-52,46 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,61 | -0,25R | €-17,63 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -0,75R | €-45,24 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,97 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 27 | 27 | 22,22% | 0,51 | -0,37R | €-98,95 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 22 | 22 | 18,18% | 0,23 | -0,63R | €-139,43 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 55 | 55 | 29,09% | 0,81 | -0,13R | €-70,05 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 9 | 9 | 44,44% | 1,63 | 0,28R | €25,45 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 23 | 23 | 39,13% | 1,50 | 0,25R | €58,19 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 5 | 17 | 17 | 29,41% | 0,38 | -0,41R | €-69,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 38 | 38 | 28,95% | 1,09 | 0,05R | €18,84 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,23 | -0,63R | €-107,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 21,43% | 0,16 | -0,64R | €-89,01 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 35 | 35 | 28,57% | 0,62 | -0,24R | €-85,11 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 57,14% | 3,24 | 0,65R | €45,72 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 16 | 16 | 50,00% | 2,41 | 0,55R | €87,46 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 5 | 15 | 15 | 33,33% | 0,42 | -0,40R | €-59,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 2 | 24 | 24 | 25,00% | 0,92 | -0,03R | €-8,14 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 0 | 37 | 37 | 24,32% | 0,57 | -0,27R | €-100,46 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 49 | 49 | 28,57% | 0,72 | -0,19R | €-91,58 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 114 | 114 | 34,21% | 1,00 | 0,00R | €2,10 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 13 | 13 | 38,46% | 1,56 | 0,23R | €29,62 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 57 | 57 | 35,09% | 1,18 | 0,10R | €57,65 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 11 | 58 | 58 | 31,03% | 0,73 | -0,14R | €-83,40 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 75 | 75 | 28,00% | 0,95 | -0,03R | €-21,00 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-53,00 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,10 | -0,75R | €-29,95 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,18 | -0,69R | €-27,47 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,50R | €5,03 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,11R | €1,10 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 20,00% | 0,15 | -0,77R | €-38,41 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,66 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,08 | -0,77R | €-30,63 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 6 | 6 | 33,33% | 0,68 | -0,24R | €-14,10 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 0,02R | €0,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,69 | -0,22R | €-35,19 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 32,35% | 0,94 | -0,04R | €-13,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 2 | 74 | 74 | 31,08% | 0,96 | -0,02R | €-16,92 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 5 | 28 | 28 | 42,86% | 1,53 | 0,29R | €82,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 4 | 44 | 44 | 34,09% | 1,06 | 0,04R | €16,28 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 44,44% | 0,85 | -0,08R | €-14,12 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 137 | 137 | 64,96% | 1,36 | 0,12R | €162,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 3 | 69 | 69 | 73,91% | 1,82 | 0,21R | €143,65 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 3 | 74 | 74 | 64,86% | 1,33 | 0,12R | €86,36 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,63 | -0,24R | €-34,08 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 2 | 76 | 76 | 34,21% | 1,11 | 0,07R | €50,71 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 5 | 27 | 27 | 33,33% | 1,01 | 0,01R | €2,09 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 3 | 41 | 41 | 36,59% | 1,15 | 0,10R | €39,02 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 1,36 | 0,21R | €18,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 68 | 68 | 30,88% | 1,10 | 0,07R | €44,75 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 5 | 25 | 25 | 36,00% | 1,15 | 0,10R | €23,89 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 3 | 38 | 38 | 36,84% | 1,17 | 0,11R | €41,45 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,90R | €-71,98 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 57 | 57 | 36,84% | 1,14 | 0,09R | €51,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 5 | 20 | 20 | 45,00% | 1,90 | 0,42R | €84,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 2 | 30 | 30 | 23,33% | 0,62 | -0,29R | €-86,54 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,57 | -0,31R | €-43,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 2 | 71 | 71 | 33,80% | 1,11 | 0,06R | €45,44 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 5 | 27 | 27 | 37,04% | 1,19 | 0,12R | €32,06 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 3 | 39 | 39 | 35,90% | 1,12 | 0,08R | €29,29 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 19,57% | 0,44 | -0,37R | €-168,98 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 67 | 67 | 32,84% | 0,87 | -0,08R | €-53,81 |
| Forza relativa 1H V1 | RANGE | 3 | 158 | 158 | 31,01% | 0,86 | -0,08R | €-124,70 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 13 | 13 | 7,69% | 0,26 | -0,48R | €-62,75 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 4 | 69 | 69 | 36,23% | 1,34 | 0,17R | €119,52 |
| Forza relativa 1H V1 | TREND_DOWN | 10 | 65 | 65 | 27,69% | 0,79 | -0,11R | €-72,72 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 95 | 95 | 25,26% | 0,91 | -0,05R | €-45,58 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,64 | -0,21R | €-41,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 26 | 23 | 38,46% | 1,35 | 0,18R | €47,67 |
| Forza relativa 1H V2 | RANGE | 2 | 66 | 64 | 36,36% | 0,95 | -0,03R | €-19,55 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 3 | 38 | 33 | 42,11% | 1,91 | 0,40R | €150,29 |
| Forza relativa 1H V2 | TREND_DOWN | 3 | 32 | 31 | 31,25% | 1,02 | 0,01R | €3,60 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 0 | 57 | 57 | 24,56% | 0,36 | -0,36R | €-205,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 9 | 36 | 36 | 30,56% | 0,39 | -0,34R | €-121,65 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 0 | 57 | 57 | 24,56% | 0,36 | -0,36R | €-205,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 9 | 36 | 36 | 30,56% | 0,39 | -0,34R | €-121,65 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 0 | 57 | 57 | 24,56% | 0,36 | -0,36R | €-205,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 9 | 36 | 36 | 30,56% | 0,39 | -0,34R | €-121,65 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,07 | 0,03R | €4,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 70 | 70 | 30,00% | 0,66 | -0,18R | €-125,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 1,42 | 0,16R | €21,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 34 | 34 | 41,18% | 1,16 | 0,08R | €28,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 7 | 34 | 34 | 29,41% | 0,35 | -0,36R | €-122,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 23 | 23 | 4,35% | 0,16 | -0,42R | €-97,06 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 29,63% | 0,29 | -0,48R | €-128,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 0 | 62 | 62 | 56,45% | 0,72 | -0,12R | €-73,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 68,75% | 1,69 | 0,22R | €34,79 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 2 | 25 | 25 | 60,00% | 1,46 | 0,20R | €49,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 8 | 58 | 58 | 56,90% | 0,67 | -0,13R | €-76,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 19 | 19 | 42,11% | 0,65 | -0,16R | €-29,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,22 | -0,52R | €-124,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 0 | 55 | 55 | 56,36% | 0,43 | -0,23R | €-128,49 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 61,54% | 1,54 | 0,21R | €27,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 1 | 25 | 25 | 64,00% | 1,73 | 0,28R | €69,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 9 | 47 | 47 | 55,32% | 0,58 | -0,17R | €-79,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 18 | 18 | 38,89% | 0,34 | -0,31R | €-55,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 50 | 50 | 32,00% | 0,86 | -0,08R | €-38,14 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 59 | 59 | 49,15% | 1,52 | 0,22R | €130,47 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 4 | 40 | 40 | 40,00% | 1,56 | 0,22R | €86,29 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 4 | 41 | 41 | 29,27% | 0,95 | -0,03R | €-11,56 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 51 | 51 | 31,37% | 0,82 | -0,10R | €-49,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 59 | 59 | 49,15% | 1,52 | 0,22R | €130,47 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 4 | 40 | 40 | 40,00% | 1,56 | 0,22R | €86,29 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 4 | 41 | 41 | 29,27% | 0,95 | -0,03R | €-11,56 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 51 | 51 | 31,37% | 0,82 | -0,10R | €-49,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 59 | 59 | 49,15% | 1,52 | 0,22R | €130,47 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 4 | 40 | 40 | 40,00% | 1,56 | 0,22R | €86,29 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 4 | 41 | 41 | 29,27% | 0,95 | -0,03R | €-11,56 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,23 | -0,51R | €-71,62 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 1,09 | 0,05R | €25,90 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 71 | 71 | 45,07% | 1,55 | 0,26R | €183,27 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,23 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 5 | 48 | 48 | 41,67% | 1,63 | 0,30R | €142,56 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 3 | 40 | 40 | 27,50% | 0,72 | -0,17R | €-66,15 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 62 | 62 | 29,03% | 0,95 | -0,02R | €-14,90 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,64R | €-31,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 47 | 47 | 27,66% | 0,81 | -0,10R | €-47,19 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 0,00% | 0,00 | -0,77R | €-92,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 49 | 49 | 36,73% | 1,02 | 0,01R | €5,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 66 | 66 | 43,94% | 1,40 | 0,20R | €130,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 5 | 36 | 36 | 44,44% | 1,96 | 0,38R | €138,38 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 3 | 40 | 40 | 27,50% | 0,72 | -0,17R | €-66,15 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,04 | -0,54R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 39 | 39 | 48,72% | 1,37 | 0,16R | €61,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,34 | -0,35R | €-14,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 39 | 39 | 48,72% | 1,38 | 0,15R | €59,85 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 4 | 47 | 47 | 46,81% | 0,93 | -0,03R | €-14,70 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -0,75R | €-82,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 33 | 33 | 39,39% | 1,40 | 0,20R | €65,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 3 | 34 | 34 | 38,24% | 1,69 | 0,29R | €99,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 4 | 36 | 36 | 30,56% | 0,78 | -0,13R | €-46,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,54 | -0,25R | €-38,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 39 | 39 | 48,72% | 1,37 | 0,16R | €61,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,34 | -0,35R | €-14,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 41 | 41 | 46,34% | 1,30 | 0,12R | €49,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 4 | 47 | 47 | 46,81% | 0,93 | -0,03R | €-14,70 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,26 | -0,47R | €-61,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 33 | 33 | 39,39% | 1,40 | 0,20R | €65,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 3 | 35 | 35 | 37,14% | 1,57 | 0,25R | €88,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 4 | 36 | 36 | 30,56% | 0,78 | -0,13R | €-46,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,48 | -0,30R | €-48,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 54 | 54 | 44,44% | 0,99 | -0,00R | €-1,94 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,40 | 0,16R | €119,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,34 | -0,35R | €-14,14 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 4 | 45 | 45 | 48,89% | 1,31 | 0,13R | €58,28 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 4 | 53 | 53 | 43,40% | 0,88 | -0,05R | €-28,56 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,51 | -0,29R | €-20,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 33,96% | 1,05 | 0,03R | €13,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 62 | 62 | 41,94% | 1,42 | 0,21R | €129,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 5 | 36 | 36 | 41,67% | 1,73 | 0,31R | €111,88 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 3 | 39 | 39 | 28,21% | 0,76 | -0,14R | €-54,51 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,60R | €-41,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 35,85% | 1,00 | -0,00R | €-1,34 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 58 | 58 | 41,38% | 1,44 | 0,23R | €131,53 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 5 | 30 | 30 | 40,00% | 2,09 | 0,41R | €124,30 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 3 | 36 | 36 | 27,78% | 0,78 | -0,12R | €-42,88 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,35 | -0,47R | €-74,87 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 52 | 52 | 34,62% | 0,97 | -0,02R | €-9,35 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 74 | 74 | 48,65% | 1,62 | 0,27R | €200,99 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -0,85R | €-42,37 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 4 | 53 | 53 | 41,51% | 1,58 | 0,25R | €132,34 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 4 | 41 | 41 | 29,27% | 0,95 | -0,03R | €-11,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 78 | 78 | 34,62% | 1,08 | 0,04R | €29,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,84 | -0,09R | €-1,73 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,41 | -0,47R | €-32,89 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,86 | 0,38R | €19,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-17T02:06:09+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **793**
- Scenari virtuali ancora attivi: **15067**
- Gruppi in attesa dell'uscita originale: **465**
- Gruppi con originale chiuso ma Shadow ancora attive: **328**
- Confronti completati: **217026**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 5199 | 5268 | +€8,71 | 51,6% | 1429 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5199 | 5268 | +€7,75 | 50,9% | 1412 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5199 | 5268 | +€5,20 | 48,9% | 1576 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5198 | 5267 | +€6,40 | 49,4% | 1425 | 120 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5197 | 5266 | +€4,97 | 49,5% | 1356 | 182 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 5192 | 5265 | +€0,42 | 47,0% | 1092 | 705 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5188 | 5261 | +€0,77 | 42,9% | 626 | 1025 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5164 | 5233 | +€6,03 | 43,2% | 1248 | 98 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5162 | 5235 | €-3,88 | 34,4% | 337 | 1426 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5158 | 5227 | +€8,03 | 45,2% | 1128 | 102 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5158 | 5227 | +€6,75 | 45,0% | 1075 | 173 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5157 | 5226 | +€2,69 | 37,8% | 588 | 905 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5155 | 5224 | +€5,66 | 44,2% | 974 | 285 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5154 | 5223 | +€1,95 | 35,6% | 456 | 1137 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5145 | 5214 | +€3,75 | 42,7% | 847 | 501 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5123 | 5192 | €-2,48 | 32,7% | 397 | 1291 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5121 | 5190 | +€6,04 | 35,4% | 684 | 486 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5115 | 5184 | €-4,27 | 35,3% | 849 | 1043 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5060 | 5126 | +€6,27 | 39,2% | 337 | 749 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 4969 | 5038 | €-7,85 | 27,4% | 361 | 1468 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-17T02:06:19+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **217026**
- Valutazioni prodotte: **19199**
- Candidature al Blocco 5: **51**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 227 | 0,614 | 0,384 | 0,511 | 68,7% | 98,3 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 3786 | 0,250 | 0,149 | 0,216 | 55,0% | 88,0 | VALIDATING |
| GB30_R040 | 3786 | 0,235 | 0,140 | 0,201 | 54,8% | 87,8 | VALIDATING |
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

Generato: 2026-08-17T02:08:29+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 59 | 100,00% | 0,87 | €-107,43 | €-1,82 | 2,58% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 59 | 100,00% | 0,89 | €-91,59 | €-1,55 | 2,75% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 29 | 96,67% | 0,98 | €-18,13 | €-0,63 | 2,95% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 25 | 96,15% | 0,00 | €-281,64 | €-11,27 | 2,82% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 55 | 98,21% | 1,12 | +€118,11 | +€2,15 | 2,13% | NOT_READY_FOR_PROMOTION |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-17T02:05:57+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **140**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **557.04 R**
- Profitto virtuale mancato: **903.98 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 227 | 2 | 26396.83 |
| DOWN_20 | 227 | 3 | 52733.66 |
| DOWN_30 | 227 | 3 | 78821.21 |
| DOWN_40 | 227 | 75 | 99430.25 |
| UP_10 | 236 | 0 | 21528.38 |
| UP_20 | 236 | 0 | 43056.75 |
| UP_30 | 236 | 5 | 64653.89 |
| UP_40 | 236 | 99 | 80331.27 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-17T02:05:15+00:00

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

Generato: 2026-08-17T02:08:32+00:00

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

Generato: 2026-08-17T02:08:32+00:00

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

Generato: 2026-08-17T02:08:32+00:00

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

Generato: 2026-08-17T02:08:32+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 17.6 | E | 111 | 1.18 | 0.078 | 8.02 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 16.2 | E | 68 | 1.29 | 0.132 | 5.98 |
| 3 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 16.2 | E | 44 | 1.49 | 0.209 | 5.48 |
| 4 | SHADOW_1H_FAST_V3 | BASELINE | 14.2 | E | 134 | 0.93 | -0.032 | 16.45 |
| 5 | SHADOW_DONCHIAN_1H | BASELINE | 13.9 | E | 60 | 1.24 | 0.136 | 8.55 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 13.8 | E | 118 | 0.98 | -0.011 | 16.32 |
| 7 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 11.9 | E | 96 | 0.96 | -0.023 | 12.98 |
| 8 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 11.8 | E | 108 | 0.90 | -0.057 | 23.13 |
| 9 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 11.3 | E | 108 | 0.87 | -0.073 | 21.34 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | BASELINE | 11.2 | E | 33 | 1.22 | 0.113 | 7.64 |

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

Generato: 2026-08-17T02:08:32+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **640**
- Strategie preferite nel regime corrente: **3**
- Strategie da evitare nel regime corrente: **20**
- Memorie contestuali: **302**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.6 | 4 | 99.00 | 0.972 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.5 | 12 | 2.82 | 0.322 | 1.04 |
| 5 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 70.0 | 8 | 2.44 | 0.587 | 2.16 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | COMPATIBLE | 67.5 | 46 | 1.45 | 0.200 | 5.17 |
| 7 | SHADOW_RSI_LONG_5X_RSI20 | shadow-rsi-long-5x-rsi20 | INSUFFICIENT | 65.1 | 9 | 1.80 | 0.319 | 2.40 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 60.0 | 8 | 1.57 | 0.236 | 2.21 |
| 9 | SHADOW_1H_FAST_NO_PEPE_V1 | shadow-1h-fast-no-pepe-v1 | COMPATIBLE | 58.9 | 78 | 1.16 | 0.078 | 6.07 |
| 10 | MAIN_SIDE_REGIME_GUARD_V1 | main-side-regime-guard-v1 | OBSERVING | 58.1 | 15 | 1.60 | 0.298 | 5.28 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-17T02:08:33+00:00

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

Generato: 2026-08-17T02:05:57+00:00

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
