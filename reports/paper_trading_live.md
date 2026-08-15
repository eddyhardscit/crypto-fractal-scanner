# Paper trading automatico KuCoin

Generato: 2026-08-15T05:34:43+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-15T05:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-15T05:05:31+00:00 | 2026-08-15T05:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-15T04:45:00+00:00 | 2026-08-15T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-15T04:00:00+00:00 | 2026-08-15T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-15T00:00:00+00:00 | 2026-08-15T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Partial 1R V1 | LINK | 60m | LONG | 7,95 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | LINK | 60m | LONG | 7,95 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ACE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | CAP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | LINK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,12 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,46 | 6,00 | 3,54 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,55 | 6,00 | 4,45 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,05 | 6,00 | 4,95 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 0,83 | 6,00 | 5,17 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,19 | 6,00 | 5,81 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | CAP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | CAP | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | CAP | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | CAP | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | CAP | 60m | LONG | 8,25 | 4,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | CAP | 60m | LONG | 8,25 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | CAP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | CAP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.634,28 | -3,66% | €-114,07 | €3.000,00 | -3,80% | 5 | 41 | 34,15% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 41 | 1346 | PRIME INDICAZIONI | 100 (mancano 59) |

- Trade del Principale 4H chiusi: **41**; win rate **34,15%**; profit factor **0,72**.
- Expectancy: **€-9,22** per trade; P&L netto: **€-378,20**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.634,28 | €1.282,24 | €3.846,72 | €192,66 | €12,02 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.583,05 | €5.489,59 | €10.979,18 | €213,00 | €-70,68 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.432,40 | €2.016,51 | €6.049,54 | €208,18 | €-23,56 |
| TEST | Main Side Regime Guard V1 | 5 | €10.395,72 | €2.118,53 | €6.355,60 | €155,48 | €27,72 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.355,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.333,88 | €5.360,34 | €10.720,69 | €207,98 | €-69,01 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.296,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €10.288,28 | €1.830,67 | €5.492,01 | €203,41 | €-13,30 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.278,76 | €1.286,79 | €3.860,36 | €205,26 | €-4,74 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.208,98 | €3.676,96 | €7.353,91 | €204,21 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.137,54 | €630,70 | €1.892,11 | €201,74 | €8,61 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €10.124,69 | €1.983,39 | €5.950,17 | €200,92 | €-39,50 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.077,90 | €2.359,26 | €7.077,78 | €201,57 | €-0,42 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.029,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.027,11 | €3.574,44 | €7.148,87 | €151,50 | €-30,10 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €10.014,74 | €1.782,00 | €5.345,99 | €198,00 | €-12,95 |
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
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 8 | €9.988,64 | €2.889,80 | €5.779,60 | €199,06 | €-10,93 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €9.985,79 | €592,29 | €1.776,86 | €198,31 | €17,15 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.977,14 | €1.413,45 | €2.826,90 | €49,75 | €25,79 |
| TEST | Doge Ema 1H | 1 | €9.976,16 | €1.155,63 | €3.466,88 | €49,92 | €-8,11 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €9.960,90 | €1.302,35 | €3.907,04 | €50,01 | €-39,06 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €9.960,13 | €3.797,91 | €7.595,82 | €199,21 | €-15,84 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.918,77 | €1.406,00 | €2.812,00 | €49,49 | €19,71 |
| TEST | Doge Donchian 1H | 1 | €9.904,04 | €1.295,48 | €3.886,44 | €49,75 | €-43,70 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 5 | €9.903,39 | €3.307,41 | €9.922,22 | €149,72 | €-42,68 |
| TEST | Bilanciata 1H V1 | 6 | €9.898,61 | €1.970,97 | €5.912,90 | €147,90 | €-0,46 |
| TEST | Btc Ema 1H | 1 | €9.885,57 | €1.146,03 | €3.438,09 | €49,51 | €-14,41 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.884,81 | €2.099,14 | €4.198,28 | €197,60 | €4,88 |
| TEST | Ampia 4H | 5 | €9.884,28 | €1.961,33 | €3.922,65 | €148,09 | €9,68 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.872,74 | €1.934,03 | €5.802,10 | €195,92 | €-38,52 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 6 | €9.844,01 | €2.647,66 | €5.295,31 | €197,03 | €-10,60 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €9.835,75 | €2.791,09 | €8.373,26 | €99,34 | €-64,02 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 7 | €9.809,13 | €1.262,84 | €3.788,53 | €193,37 | €-32,07 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €9.809,03 | €2.673,74 | €5.347,47 | €196,09 | €4,85 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.805,12 | €1.246,78 | €3.740,33 | €146,18 | €-12,90 |
| TEST | Combo Mean Reversion | 2 | €9.792,12 | €3.892,85 | €7.785,69 | €46,71 | €65,18 |
| TEST | Rapida 1H V2 | 0 | €9.791,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.788,87 | €3.237,84 | €6.475,68 | €195,92 | €-7,10 |
| TEST | Sol Ema 1H | 1 | €9.777,80 | €1.135,84 | €3.407,53 | €49,07 | €-34,06 |
| TEST | Combo Adaptive Runner25 V1 | 8 | €9.767,69 | €2.359,91 | €4.719,82 | €194,56 | €4,66 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €9.766,74 | €1.869,50 | €5.608,49 | €148,65 | €-12,73 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.764,85 | €2.073,66 | €4.147,33 | €195,21 | €4,83 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.760,08 | €3.330,35 | €6.660,69 | €146,06 | €-0,05 |
| TEST | Scanner Bottom15 Short | 5 | €9.760,08 | €3.330,35 | €6.660,69 | €146,06 | €-0,05 |
| TEST | Scanner Bottom20 Short | 5 | €9.760,08 | €3.330,35 | €6.660,69 | €146,06 | €-0,05 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.751,89 | €3.350,59 | €6.701,19 | €194,62 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €9.745,47 | €1.341,76 | €4.025,27 | €97,56 | €0,05 |
| TEST | Forza relativa 1H V2 | 5 | €9.732,38 | €3.372,39 | €6.744,77 | €146,59 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.715,77 | €2.977,52 | €5.955,05 | €48,49 | €47,98 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.715,21 | €2.063,12 | €4.126,24 | €194,21 | €4,80 |
| TEST | Rapida 1H V3 Filtered | 6 | €9.702,91 | €1.857,28 | €5.571,84 | €147,68 | €-12,65 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.693,87 | €3.317,86 | €6.635,71 | €145,23 | €-0,48 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.679,13 | €3.312,81 | €6.625,62 | €145,01 | €-0,48 |
| TEST | Sol Adaptive 1H | 0 | €9.674,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.669,99 | €1.512,09 | €3.024,18 | €48,39 | €-7,07 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 5 | €9.659,65 | €1.836,52 | €5.509,57 | €98,24 | €-13,88 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 4 | €9.657,64 | €1.539,16 | €3.078,32 | €193,21 | €6,45 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.656,90 | €2.659,21 | €5.318,42 | €192,78 | €-10,40 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.651,72 | €2.305,85 | €4.611,71 | €193,58 | €-7,06 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.622,79 | €3.130,95 | €9.392,84 | €191,07 | €-67,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.604,64 | €3.287,32 | €6.574,63 | €143,89 | €-0,48 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.594,30 | €2.370,73 | €7.112,20 | €191,79 | €-24,26 |
| TEST | Eth Ema 1H | 1 | €9.593,15 | €1.113,68 | €3.341,04 | €48,11 | €-27,07 |
| TEST | Combo Adaptive Partial 1R V1 | 8 | €9.591,54 | €2.774,92 | €5.549,83 | €191,14 | €-10,49 |
| TEST | Combo Adaptive Tp3 V1 | 8 | €9.585,21 | €2.315,82 | €4.631,64 | €190,93 | €4,57 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.537,75 | €2.025,44 | €4.050,87 | €190,67 | €4,71 |
| TEST | Combo Adaptive Quality7 Regime V1 | 4 | €9.536,16 | €1.519,80 | €3.039,60 | €190,78 | €6,37 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.532,08 | €2.231,48 | €6.694,45 | €190,65 | €-0,39 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.493,31 | €3.109,30 | €6.218,60 | €189,88 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.483,21 | €3.105,99 | €6.211,99 | €189,68 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €9.479,92 | €2.569,79 | €5.139,58 | €189,51 | €4,77 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €9.474,38 | €2.568,29 | €5.136,57 | €189,40 | €4,76 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €9.472,28 | €1.241,72 | €3.725,16 | €187,45 | €-31,05 |
| TEST | Master Adaptive V1 | 5 | €9.446,53 | €3.093,98 | €6.187,96 | €188,95 | €0,00 |
| TEST | Combo Trend | 9 | €9.435,42 | €1.377,00 | €2.753,99 | €188,63 | €4,37 |
| TEST | Scanner Top10 Long | 5 | €9.403,80 | €3.171,75 | €6.343,50 | €188,08 | €0,00 |
| TEST | Scanner Top15 Long | 5 | €9.403,80 | €3.171,75 | €6.343,50 | €188,08 | €0,00 |
| TEST | Scanner Top20 Long | 5 | €9.403,80 | €3.171,75 | €6.343,50 | €188,08 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €9.373,51 | €2.555,02 | €5.110,05 | €187,38 | €4,63 |
| TEST | Benchmark trend following EMA 1H | 9 | €9.349,11 | €2.713,64 | €5.427,28 | €186,89 | €3,88 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.345,94 | €2.243,88 | €4.487,75 | €186,79 | €39,44 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.335,02 | €1.786,12 | €5.358,36 | €187,00 | €4,79 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.321,02 | €3.052,87 | €6.105,74 | €186,44 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €9.307,62 | €2.859,77 | €5.719,53 | €186,16 | €0,00 |
| TEST | Combo Scanner | 5 | €9.293,02 | €3.590,77 | €7.181,54 | €186,69 | €-18,25 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.197,04 | €1.748,57 | €5.245,71 | €93,53 | €-13,21 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.194,55 | €2.506,24 | €5.012,48 | €183,80 | €4,55 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.168,38 | €2.069,67 | €4.139,33 | €183,28 | €4,54 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 0 | €9.028,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.009,09 | €2.598,92 | €5.197,83 | €180,38 | €-9,93 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.634,28 | €-378,20 | 41 | 41 | 34,15% | 0,72 | €-9,22 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.583,05 | €660,35 | 60 | 60 | 48,33% | 1,46 | €11,01 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.432,40 | €459,52 | 61 | 61 | 50,82% | 1,35 | €7,53 | 3,35% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.395,72 | €367,24 | 20 | 20 | 50,00% | 1,85 | €18,36 | 2,40% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.355,43 | €355,43 | 33 | 33 | 48,48% | 1,52 | €10,77 | 3,55% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.333,88 | €409,36 | 28 | 28 | 46,43% | 1,71 | €14,62 | 3,63% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.296,26 | €296,26 | 31 | 31 | 51,61% | 1,36 | €9,56 | 2,31% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.288,28 | €304,86 | 107 | 107 | 42,99% | 1,13 | €2,85 | 4,44% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.278,76 | €284,68 | 102 | 102 | 45,10% | 1,14 | €2,79 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.208,98 | €212,94 | 68 | 68 | 44,12% | 1,13 | €3,13 | 7,66% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.137,54 | €130,01 | 44 | 44 | 47,73% | 1,13 | €2,95 | 5,21% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.124,69 | €164,93 | 97 | 97 | 42,27% | 1,07 | €1,70 | 6,52% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.077,90 | €81,91 | 85 | 85 | 38,82% | 1,04 | €0,96 | 5,68% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.029,32 | €29,32 | 6 | 6 | 66,67% | 1,27 | €4,89 | 1,49% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.027,11 | €57,88 | 42 | 42 | 50,00% | 1,07 | €1,38 | 2,94% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.014,74 | €30,88 | 65 | 65 | 46,15% | 1,02 | €0,48 | 4,78% |
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
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Combo Adaptive | Combo Adaptive | €9.988,64 | €3,02 | 62 | 62 | 40,32% | 1,00 | €0,05 | 5,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.985,79 | €-30,29 | 99 | 99 | 41,41% | 0,99 | €-0,31 | 6,72% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Ema 4H | Trend following EMA | €9.977,14 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Doge Ema 1H | Trend following EMA | €9.976,16 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.960,90 | €2,03 | 6 | 6 | 50,00% | 1,02 | €0,34 | 1,99% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.960,13 | €-23,21 | 53 | 53 | 45,28% | 0,98 | €-0,44 | 6,59% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.918,77 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.904,04 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 2,06% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.903,39 | €-49,12 | 3 | 3 | 33,33% | 0,13 | €-16,37 | 1,59% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.898,61 | €-98,17 | 93 | 93 | 41,94% | 0,94 | €-1,06 | 6,96% |
| TEST | Btc Ema 1H | Trend following EMA | €9.885,57 | €-98,30 | 8 | 8 | 37,50% | 0,63 | €-12,29 | 1,72% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.884,81 | €-117,96 | 38 | 38 | 39,47% | 0,90 | €-3,10 | 6,54% |
| TEST | Ampia 4H | Confluenza trend | €9.884,28 | €-125,24 | 34 | 34 | 23,53% | 0,86 | €-3,68 | 4,36% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.872,74 | €-88,02 | 61 | 61 | 39,34% | 0,93 | €-1,44 | 6,52% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.844,01 | €-142,63 | 39 | 39 | 35,90% | 0,84 | €-3,66 | 4,45% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.835,75 | €-95,59 | 33 | 33 | 45,45% | 0,88 | €-2,90 | 3,94% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.809,13 | €-156,53 | 115 | 115 | 36,52% | 0,94 | €-1,36 | 3,95% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.809,03 | €-193,05 | 59 | 59 | 35,59% | 0,87 | €-3,27 | 8,46% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.805,12 | €-179,72 | 64 | 64 | 42,19% | 0,90 | €-2,81 | 4,70% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.792,12 | €-267,90 | 28 | 28 | 35,71% | 0,72 | €-9,57 | 4,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.791,89 | €-208,11 | 29 | 26 | 37,93% | 0,74 | €-7,18 | 3,89% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.788,87 | €-198,74 | 25 | 25 | 40,00% | 0,65 | €-7,95 | 2,73% |
| TEST | Sol Ema 1H | Trend following EMA | €9.777,80 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 3,07% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.767,69 | €-234,18 | 69 | 69 | 34,78% | 0,83 | €-3,39 | 6,25% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.766,74 | €-218,33 | 83 | 83 | 49,40% | 0,87 | €-2,63 | 7,17% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.764,85 | €-237,89 | 43 | 43 | 34,88% | 0,81 | €-5,53 | 6,13% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.760,08 | €-235,30 | 46 | 46 | 34,78% | 0,77 | €-5,12 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.760,08 | €-235,30 | 46 | 46 | 34,78% | 0,77 | €-5,12 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.760,08 | €-235,30 | 46 | 46 | 34,78% | 0,77 | €-5,12 | 5,27% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.751,89 | €-244,06 | 41 | 41 | 31,71% | 0,81 | €-5,95 | 4,45% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.745,47 | €-252,25 | 61 | 56 | 44,26% | 0,82 | €-4,14 | 5,74% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.732,38 | €-262,78 | 69 | 66 | 39,13% | 0,88 | €-3,81 | 8,11% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.715,77 | €-327,61 | 68 | 68 | 42,65% | 0,82 | €-4,82 | 6,53% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.715,21 | €-287,51 | 53 | 53 | 39,62% | 0,80 | €-5,42 | 5,80% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.702,91 | €-282,25 | 127 | 127 | 39,37% | 0,90 | €-2,22 | 7,14% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.693,87 | €-301,10 | 38 | 38 | 34,21% | 0,65 | €-7,92 | 5,27% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.679,13 | €-315,85 | 39 | 39 | 33,33% | 0,60 | €-8,10 | 5,27% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.674,16 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 3,94% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.669,99 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.659,65 | €-325,27 | 56 | 56 | 37,50% | 0,79 | €-5,81 | 8,59% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.657,64 | €-346,97 | 17 | 17 | 35,29% | 0,46 | €-20,41 | 3,78% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.656,90 | €-329,41 | 40 | 40 | 30,00% | 0,76 | €-8,24 | 6,03% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.651,72 | €-338,45 | 37 | 37 | 29,73% | 0,63 | €-9,15 | 5,31% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.622,79 | €-307,51 | 87 | 87 | 42,53% | 0,86 | €-3,53 | 6,10% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.604,64 | €-390,38 | 66 | 66 | 33,33% | 0,72 | €-5,91 | 6,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.594,30 | €-377,15 | 67 | 67 | 44,78% | 0,81 | €-5,63 | 5,63% |
| TEST | Eth Ema 1H | Trend following EMA | €9.593,15 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 4,10% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.591,54 | €-394,65 | 63 | 63 | 38,10% | 0,69 | €-6,26 | 6,07% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.585,21 | €-416,62 | 50 | 50 | 34,00% | 0,62 | €-8,33 | 6,25% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.537,75 | €-464,92 | 60 | 60 | 38,33% | 0,72 | €-7,75 | 7,59% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.536,16 | €-468,38 | 17 | 17 | 23,53% | 0,29 | €-27,55 | 4,99% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.532,08 | €-464,13 | 41 | 41 | 34,15% | 0,50 | €-11,32 | 5,40% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.493,31 | €-502,86 | 41 | 41 | 21,95% | 0,57 | €-12,26 | 6,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.483,21 | €-512,96 | 36 | 36 | 27,78% | 0,55 | €-14,25 | 6,27% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.479,92 | €-522,19 | 44 | 44 | 29,55% | 0,61 | €-11,87 | 9,16% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.474,38 | €-527,73 | 48 | 48 | 31,25% | 0,61 | €-10,99 | 9,46% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.472,28 | €-495,53 | 101 | 101 | 39,60% | 0,79 | €-4,91 | 7,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.446,53 | €-549,65 | 38 | 38 | 26,32% | 0,58 | €-14,46 | 6,08% |
| TEST | Combo Trend | Combo Trend | €9.435,42 | €-567,88 | 92 | 92 | 32,61% | 0,77 | €-6,17 | 9,82% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.403,80 | €-593,61 | 40 | 40 | 35,00% | 0,50 | €-14,84 | 9,13% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.403,80 | €-593,61 | 40 | 40 | 35,00% | 0,50 | €-14,84 | 9,13% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.403,80 | €-593,61 | 40 | 40 | 35,00% | 0,50 | €-14,84 | 9,13% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.373,51 | €-628,48 | 40 | 40 | 30,00% | 0,48 | €-15,71 | 8,92% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.349,11 | €-652,13 | 62 | 62 | 29,03% | 0,59 | €-10,52 | 7,38% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.345,94 | €-691,82 | 37 | 37 | 21,62% | 0,53 | €-18,70 | 7,51% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.335,02 | €-667,17 | 43 | 43 | 30,23% | 0,53 | €-15,52 | 7,54% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.321,02 | €-675,22 | 73 | 73 | 47,95% | 0,55 | €-9,25 | 7,33% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.307,62 | €-689,58 | 80 | 80 | 28,75% | 0,64 | €-8,62 | 8,96% |
| TEST | Combo Scanner | Combo Scanner | €9.293,02 | €-686,81 | 65 | 65 | 33,85% | 0,63 | €-10,57 | 10,13% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.197,04 | €-788,60 | 76 | 76 | 30,26% | 0,64 | €-10,38 | 10,56% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.194,55 | €-807,40 | 52 | 52 | 30,77% | 0,39 | €-15,53 | 9,50% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.168,38 | €-833,46 | 43 | 43 | 25,58% | 0,55 | €-19,38 | 9,06% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.028,46 | €-971,54 | 32 | 32 | 15,62% | 0,30 | €-30,36 | 11,05% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.009,09 | €-977,84 | 77 | 77 | 32,47% | 0,47 | €-12,70 | 11,05% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00494 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €11,68 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63098,87000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €0,34 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,04289 | 1,04289 | 1,03001 | 1,38531 | 0,79260 | €139,17 | €417,52 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,07030 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €-0,42 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00494 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €-0,04 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,03281 | 0,03281 | 0,03675 | 0,04359 | 0,02494 | €125,03 | €375,08 | €45,01 | €-0,00 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | APR | LONG | Confluenza trend | 60m | 3,0x | 0,49291 | 0,49291 | 0,43376 | 0,33107 | 0,61121 | €131,87 | €395,61 | €47,47 | €0,00 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1182,39901 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1632,05865 | 1632,05865 | 1586,54905 | 1096,19939 | 1723,07784 | €570,53 | €1.711,58 | €47,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06625 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €4,79 |
| 1H Balanced Short Trend Down Strict V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,03900 | 1,03900 | 1,03001 | 1,38014 | 0,78964 | €138,10 | €414,31 | €0,00 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,07030 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €-8,11 |
| 1H Balanced Short Trend Down Strict V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1866,05671 | 1883,03000 | 1892,92793 | 2478,74534 | 1812,31428 | €23,32 | €69,97 | €1,01 | €-0,64 |
| 1H Balanced Short Trend Down Strict V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,71805 | 75,46500 | 75,79399 | 99,25048 | 72,56617 | €1.131,56 | €3.394,68 | €48,88 | €-33,94 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00494 | 1,01986 | 1,33548 | 0,97642 | €37,09 | €111,28 | €1,60 | €0,05 |
| Bilanciata 1H V2 | BEAT | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,96465 | 0,96465 | 1,08040 | 1,28137 | 0,73313 | €124,99 | €374,96 | €45,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07030 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,42 |
| Bilanciata 1H V3 Filtered | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €457,69 | €1.373,07 | €49,01 | €0,00 |
| Bilanciata 1H V3 Filtered | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €127,78 | €383,34 | €46,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €142,15 | €426,45 | €51,17 | €-0,00 |
| 1H Fast Score 6 75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €0,00 | €0,00 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.363,48 | €4.090,45 | €51,61 | €-30,98 |
| 1H Fast Score 6 75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €155,29 | €465,86 | €51,35 | €5,26 |
| 1H Fast Score 6 75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00989 | 0,01019 | 0,00871 | 0,00664 | 0,01167 | €136,89 | €410,68 | €49,28 | €12,42 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €138,37 | €415,11 | €49,81 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €0,00 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.327,23 | €3.981,70 | €50,24 | €-30,16 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €151,16 | €453,47 | €49,98 | €5,12 |
| 1H Fast Score 6 75 No Trend Up V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00989 | 0,01019 | 0,00871 | 0,00664 | 0,01167 | €133,25 | €399,76 | €47,97 | €12,09 |
| 1H Fast Score 6 75 Cost Aware V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95974 | 0,95974 | 1,07491 | 1,27485 | 0,78699 | €145,66 | €436,97 | €52,44 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99774 | 1,00494 | 1,00892 | 1,32533 | 0,98098 | €1.572,34 | €4.717,02 | €52,83 | €-34,04 |
| 1H Fast Score 6 75 Cost Aware V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01007 | 0,01019 | 0,00886 | 0,00676 | 0,01188 | €143,17 | €429,50 | €51,54 | €5,22 |
| 1H Fast Score 6 75 Cost Aware V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €155,35 | €466,05 | €51,37 | €5,27 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,07030 | 0,07069 | 0,09286 | 0,06873 | €1.537,89 | €4.613,67 | €51,67 | €-26,00 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €143,81 | €431,44 | €47,91 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €140,04 | €420,12 | €50,41 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €141,48 | €424,43 | €50,93 | €-13,50 |
| 1H Fast No Pepe V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €771,03 | €2.313,08 | €50,17 | €0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €142,21 | €426,63 | €51,20 | €-0,00 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1191,94474 | 1191,94474 | 1171,66933 | 800,58955 | 1222,35785 | €47,86 | €143,59 | €2,44 | €0,00 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €10,42 | €31,26 | €0,35 | €-0,24 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €140,02 | €420,07 | €50,41 | €-10,85 |
| 1H Fast No Pepe V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06539 | 0,06625 | 0,05878 | 0,04392 | 0,07530 | €166,06 | €498,19 | €50,35 | €6,56 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €9,18 | €27,54 | €0,35 | €-0,21 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,68886 | €146,30 | €438,91 | €48,73 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03778 | 0,03531 | 0,05019 | 0,02871 | €9,36 | €28,07 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1182,39901 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €0,00 |
| 1H Fast Tp2 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,91916 | 1632,91916 | 1597,68836 | 1096,77737 | 1703,38077 | €753,45 | €2.260,36 | €48,77 | €0,00 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01297 | €124,29 | €372,86 | €44,74 | €-9,63 |
| 1H Fast Tp2 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 510,22784 | €45,10 | €135,30 | €1,71 | €-1,02 |
| 1H Fast Tp2 V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,08248 | €168,46 | €505,38 | €48,56 | €-21,41 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €0,00 | €0,00 |
| Rapida 1H V3 Filtered | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €752,55 | €2.257,65 | €48,96 | €0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €136,31 | €408,92 | €49,07 | €-0,00 |
| Rapida 1H V3 Filtered | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,43 | €169,29 | €1,90 | €-1,31 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €119,44 | €358,31 | €43,00 | €-9,25 |
| Rapida 1H V3 Filtered | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,07915 | €16,48 | €49,45 | €4,75 | €-2,10 |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €152,00 | €456,00 | €50,63 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €0,00 | €0,00 |
| 1H Fast V3 Cap75 V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03283 | 0,03283 | 0,03677 | 0,04361 | 0,02692 | €139,04 | €417,11 | €50,05 | €-0,00 |
| 1H Fast V3 Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €150,74 | €452,23 | €49,85 | €5,11 |
| 1H Fast V3 Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00989 | 0,01019 | 0,00871 | 0,00664 | 0,01167 | €132,72 | €398,15 | €47,78 | €12,04 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06991 | 0,07030 | 0,07069 | 0,09286 | 0,06873 | €1.375,16 | €4.125,47 | €46,21 | €-23,25 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €135,40 | €406,20 | €48,74 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.450,98 | €4.352,95 | €48,75 | €-33,56 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €131,59 | €394,76 | €47,37 | €-10,19 |
| 1H Fast V3 Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €135,06 | €405,19 | €45,82 | €0,00 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €127,85 | €383,56 | €46,03 | €-12,20 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €44,60 | €133,79 | €1,69 | €-1,01 |
| 1H Fast V3 Long Nohigh Cap75 V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,15 | €405,45 | €48,65 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €144,03 | €432,09 | €48,86 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €135,19 | €405,57 | €48,67 | €-12,90 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €0,00 | €0,00 |
| 1H Fast V3 No Esports V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €736,66 | €2.209,98 | €47,93 | €0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €133,42 | €400,27 | €48,03 | €-0,00 |
| 1H Fast V3 No Esports V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €47,04 | €141,11 | €1,58 | €-1,09 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €119,14 | €357,43 | €42,89 | €-9,23 |
| 1H Fast V3 No Esports V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,07915 | €163,10 | €489,29 | €47,02 | €-20,73 |
| 1H Fast V3 No Esports Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €141,86 | €425,58 | €48,12 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €134,28 | €402,85 | €48,34 | €-12,81 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €46,84 | €140,52 | €1,77 | €-1,06 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €757,50 | €2.272,50 | €49,29 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €137,20 | €411,61 | €49,39 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,80 | €170,41 | €1,91 | €-1,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01046 | 0,01019 | 0,00921 | 0,00703 | 0,01235 | €120,22 | €360,66 | €43,28 | €-9,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06625 | 0,06253 | 0,04647 | 0,07915 | €16,59 | €49,77 | €4,78 | €-2,11 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.483,05 | €4.449,14 | €49,83 | €-34,30 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.308,04 | €3.924,12 | €49,51 | €-29,72 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,37 | €406,10 | €48,73 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 497,66951 | 493,90000 | 491,39035 | 334,26802 | 507,08825 | €1.271,08 | €3.813,23 | €48,11 | €-28,88 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €136,42 | €409,26 | €45,11 | €4,62 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00494 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €9,10 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63098,87000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €0,58 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €169,57 | €339,13 | €40,70 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €79,48 | €158,95 | €3,52 | €0,00 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,03281 | 0,03281 | 0,03675 | 0,04906 | 0,02415 | €186,76 | €373,52 | €44,82 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €200,27 | €400,55 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02493 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07030 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-37,54 |
| Benchmark Donchian breakout 1H | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €858,65 | €1.717,31 | €52,93 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,46500 | 75,91354 | 111,70349 | 71,72933 | €1.657,45 | €3.314,90 | €53,04 | €-33,14 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07030 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-36,66 |
| Donchian 1H Gb20 120R V1 | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €838,44 | €1.676,87 | €51,68 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,46500 | 75,91354 | 111,70349 | 71,72933 | €1.618,43 | €3.236,85 | €51,79 | €-32,36 |
| Benchmark Bollinger mean reversion 1H | SNDK | SHORT | Bollinger mean reversion | 60m | 2,0x | 1630,10135 | 1630,10135 | 1667,98054 | 2437,00152 | 1573,28257 | €1.043,30 | €2.086,60 | €48,49 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 0,99263 | 1,00494 | 1,00079 | 0,50128 | 1,01050 | €1.934,23 | €3.868,45 | €0,00 | €47,98 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07030 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €-0,11 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,00 |
| Benchmark trend following EMA 1H | SNDK | LONG | Trend following EMA | 60m | 2,0x | 1632,05865 | 1632,05865 | 1581,49243 | 824,18962 | 1743,30434 | €724,64 | €1.449,29 | €44,90 | €0,00 |
| Benchmark trend following EMA 1H | ETH | SHORT | Trend following EMA | 60m | 2,0x | 1867,89635 | 1883,03000 | 1897,78269 | 2792,50504 | 1802,14639 | €18,13 | €36,25 | €0,58 | €-0,29 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 62898,88771 | 63098,87000 | 63905,26991 | 94033,83712 | 60684,84686 | €27,47 | €54,94 | €0,88 | €-0,17 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €183,61 | €367,22 | €44,07 | €4,46 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | APR | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €209,11 | €418,21 | €50,19 | €0,00 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.146,19 | €2.292,38 | €50,74 | €0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €199,49 | €398,98 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €-0,05 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €200,12 | €400,25 | €48,03 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,46500 | 75,79399 | 111,70349 | 72,56617 | €21,64 | €43,28 | €0,62 | €-0,43 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | APR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top10 Long | SNDK | LONG | Scanner Top10 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,05 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | APR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top15 Long | SNDK | LONG | Scanner Top15 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,05 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | APR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top20 Long | SNDK | LONG | Scanner Top20 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,05 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €192,28 | €384,55 | €46,15 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €22,01 | €44,02 | €1,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €199,69 | €399,39 | €47,93 | €4,85 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €180,23 | €360,46 | €43,26 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €20,63 | €41,26 | €1,12 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €187,18 | €374,37 | €44,92 | €4,55 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €200,65 | €401,31 | €48,16 | €0,00 |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €0,00 |
| Scanner Top5 Btc Guard V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €890,44 | €1.780,87 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €198,69 | €397,39 | €47,69 | €4,83 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €183,74 | €367,48 | €44,10 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €21,03 | €42,07 | €1,14 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €190,83 | €381,65 | €45,80 | €4,63 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €195,99 | €391,97 | €47,04 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €869,73 | €1.739,45 | €47,32 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €194,07 | €388,15 | €46,58 | €4,71 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €203,12 | €406,24 | €48,75 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €901,37 | €1.802,75 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €201,14 | €402,27 | €48,27 | €4,88 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €199,63 | €399,27 | €47,91 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €885,91 | €1.771,82 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €197,68 | €395,37 | €47,44 | €4,80 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,01 | €370,01 | €44,40 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,67 | €0,92 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €196,14 | €392,28 | €47,07 | €4,76 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,11 | €370,23 | €44,43 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,69 | €0,92 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €196,25 | €392,51 | €47,10 | €4,77 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07030 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €-7,07 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €179,75 | €359,50 | €43,14 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07030 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €-0,14 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,00 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1618,90076 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €0,00 |
| Combo Trend | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02351 | €194,61 | €389,21 | €46,71 | €-0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01273 | €185,72 | €371,43 | €44,57 | €4,51 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 63098,87000 | 62072,20924 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €46,71 | €16,90 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 0,99263 | 1,00494 | 1,00079 | 0,50128 | 1,01169 | €1.946,43 | €3.892,85 | €0,00 | €48,28 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,07030 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €-18,25 |
| Combo Scanner | APR | LONG | Combo Scanner | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €186,01 | €372,01 | €44,64 | €0,00 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €1.034,30 | €2.068,59 | €45,78 | €0,00 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €-0,15 |
| Combo Adaptive | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,00 | €0,00 |
| Combo Adaptive | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €686,66 | €1.373,32 | €49,73 | €0,00 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €208,34 | €416,67 | €50,00 | €-10,76 |
| Combo Adaptive | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,52871 | 9,52300 | 9,31805 | 4,81200 | 9,95005 | €21,07 | €42,14 | €0,93 | €-0,03 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive Mfe Trail | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €15,03 | €30,05 | €0,67 | €0,00 |
| Combo Adaptive Mfe Trail | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €619,25 | €1.238,49 | €44,85 | €0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,07030 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,26 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €187,35 | €374,71 | €44,96 | €-9,67 |
| Combo Adaptive Quality7 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1175,20470 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €0,00 |
| Combo Adaptive Quality7 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1632,91916 | 1632,91916 | 1587,62241 | 824,62418 | 1723,51265 | €880,79 | €1.761,58 | €48,87 | €0,00 |
| Combo Adaptive Quality7 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02574 | €203,75 | €407,50 | €48,90 | €-0,00 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01038 | 0,01019 | 0,00913 | 0,00524 | 0,01287 | €196,76 | €393,51 | €47,22 | €-7,06 |
| Combo Adaptive Regime V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,96465 | 0,96465 | 1,08040 | 1,44215 | 0,73313 | €206,23 | €412,46 | €49,50 | €-0,00 |
| Combo Adaptive Regime V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01038 | 0,01019 | 0,00913 | 0,00524 | 0,01287 | €197,95 | €395,89 | €47,51 | €-7,10 |
| Combo Adaptive Quality7 Regime V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €200,62 | €401,23 | €48,15 | €-10,36 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06625 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €12,24 |
| Combo Adaptive Quality7 Regime V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,41758 | 1,43360 | 1,24747 | 0,71588 | 1,75780 | €198,74 | €397,48 | €47,70 | €4,49 |
| Combo Adaptive Quality7 Regime V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €919,84 | €1.839,67 | €46,79 | €0,00 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | APR | LONG | Combo Adaptive | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €199,74 | €399,48 | €47,94 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €205,31 | €410,62 | €49,27 | €-10,60 |
| Combo Adaptive Long Only V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1652,37083 | 1652,37083 | 1605,97924 | 834,44727 | 1745,15401 | €13,30 | €26,61 | €0,75 | €0,00 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €-0,14 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,00 | €0,00 |
| Combo Adaptive Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €659,36 | €1.318,73 | €47,75 | €0,00 |
| Combo Adaptive Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €200,05 | €400,11 | €48,01 | €-10,33 |
| Combo Adaptive Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,52871 | 9,52300 | 9,31805 | 4,81200 | 9,95005 | €20,23 | €40,46 | €0,89 | €-0,02 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €203,17 | €406,34 | €48,76 | €-10,49 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06625 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €12,40 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,41758 | 1,43360 | 1,24747 | 0,71588 | 1,75780 | €201,27 | €402,54 | €48,31 | €4,55 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €931,55 | €1.863,10 | €47,39 | €0,00 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive Runner25 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €-0,14 |
| Combo Adaptive Runner25 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,00 | €0,00 |
| Combo Adaptive Runner25 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,35 | €34,70 | €1,24 | €0,00 |
| Combo Adaptive Runner25 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €204,60 | €409,21 | €49,10 | €-0,00 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €197,77 | €395,55 | €47,47 | €4,80 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive Tp3 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07030 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €-0,14 |
| Combo Adaptive Tp3 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,00 | €0,00 |
| Combo Adaptive Tp3 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,03 | €34,05 | €1,22 | €0,00 |
| Combo Adaptive Tp3 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01370 | €194,08 | €388,16 | €46,58 | €4,71 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62835,53038 | 63098,87000 | 63740,36202 | 83466,52952 | 61025,86711 | €1.146,03 | €3.438,09 | €49,51 | €-14,41 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63098,87000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €25,79 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63098,87000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €19,71 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 74,71805 | 75,46500 | 75,79399 | 99,25048 | 72,56617 | €1.135,84 | €3.407,53 | €49,07 | €-34,06 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 74,71805 | 75,46500 | 75,67444 | 99,25048 | 72,80527 | €1.302,35 | €3.907,04 | €50,01 | €-39,06 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1867,89635 | 1883,03000 | 1894,79405 | 2481,18898 | 1814,10093 | €1.113,68 | €3.341,04 | €48,11 | €-27,07 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,07030 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €-8,11 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,07030 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-43,70 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,13 | €396,27 | €47,55 | €0,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,93 | €73,85 | €1,65 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €626,90 | €1.253,80 | €44,76 | €0,00 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,48 | €398,96 | €47,88 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68062 | 829,90965 | 1732,79507 | €22,94 | €45,88 | €1,25 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01046 | 0,01019 | 0,00921 | 0,00528 | 0,01297 | €201,41 | €402,81 | €48,34 | €-10,40 |
| Master Adaptive Strict3 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €190,97 | €381,94 | €45,83 | €0,00 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1167,82027 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1655,75286 | 1655,75286 | 1602,89078 | 836,15519 | 1761,47701 | €734,74 | €1.469,49 | €46,92 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €4,54 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €202,38 | €404,77 | €48,57 | €0,00 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.101,72 | €2.203,44 | €48,77 | €0,00 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €195,50 | €391,00 | €46,92 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,43 | €72,87 | €1,62 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €618,57 | €1.237,14 | €44,16 | €0,00 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,43360 | 1,15611 | 0,66345 | 1,78672 | €188,92 | €377,85 | €45,34 | €34,47 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,23400 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €0,33 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1165,32878 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,00 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54904 | 824,18962 | 1768,58749 | €850,90 | €1.701,80 | €47,45 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06625 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €4,64 |
| Combo Adaptive Side Regime Guard V1 | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,07030 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €-18,71 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €-2,19 |
| Combo Adaptive Side Regime Guard V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,01007 | 0,01019 | 0,00886 | 0,00509 | 0,01249 | €208,05 | €416,11 | €49,93 | €5,05 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,12 | €398,23 | €47,79 | €0,00 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,11 | €74,22 | €1,65 | €0,00 |
| Master Adaptive Gb20 Be V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €630,00 | €1.260,01 | €44,98 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,90 | €397,81 | €47,74 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,07 | €74,14 | €1,65 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €629,33 | €1.258,67 | €44,93 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93367 | 0,93367 | 1,04571 | 1,24023 | 0,76561 | €135,90 | €407,70 | €48,92 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €143,50 | €430,49 | €51,66 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63098,87000 | 63317,47541 | 83175,15148 | 61564,22253 | €63,81 | €191,43 | €2,14 | €-1,48 |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01007 | 0,01019 | 0,00886 | 0,00676 | 0,01188 | €134,46 | €403,39 | €48,41 | €4,90 |
| 1H Fast V3 Nohigh Regime Guard V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41758 | 1,43360 | 1,26133 | 0,95214 | 1,65196 | €153,03 | €459,10 | €50,60 | €5,19 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00494 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €12,26 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63098,87000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €15,46 |
| Main Side Regime Guard V1 | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,03900 | 1,03900 | 1,03900 | 1,38014 | 0,78964 | €144,10 | €432,31 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €209,53 | €419,07 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07030 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-28,60 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00494 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €-1,50 |
| Combo Trend Side Regime Guard V1 | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,07030 | 0,07069 | 0,09286 | 0,06873 | €1.499,62 | €4.498,86 | €50,39 | €-25,36 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €140,23 | €420,70 | €46,71 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €136,56 | €409,67 | €49,16 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01053 | 0,01019 | 0,00926 | 0,00707 | 0,01242 | €137,96 | €413,87 | €49,66 | €-13,16 |
| 1H Balanced V3 Long Only V1 | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07030 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,39 |
| 1H Balanced V3 Long Only V1 | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €432,90 | €1.298,70 | €46,36 | €0,00 |
| 1H Balanced V3 Long Only V1 | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €120,86 | €362,58 | €43,51 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,04 | €402,07 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €-0,05 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,68 | €403,35 | €48,40 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,46500 | 75,79399 | 111,70349 | 72,56617 | €21,81 | €43,62 | €0,63 | €-0,44 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,34 | €402,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00494 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €-0,05 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,98 | €403,97 | €48,48 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,46500 | 75,79399 | 111,70349 | 72,56617 | €21,84 | €43,69 | €0,63 | €-0,44 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-54,60 | -1,14 | STOP |
| 1H Fast V3 No Esports Stress Guard V1 | SOL | SHORT | 2026-08-15T03:07:29+00:00 | 75,91019 | €-76,04 | -1,53 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-5,60 | -1,14 | STOP |
| 1H Fast V3 Nohigh Regime Guard V1 | XRP | SHORT | 2026-08-15T03:07:29+00:00 | 1,00892 | €-0,83 | -1,61 | STOP_GAP_STRESS |
| 1H Fast V3 Nohigh Regime Guard V1 | SOL | SHORT | 2026-08-15T03:07:29+00:00 | 75,91019 | €-78,87 | -1,53 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | XRP | SHORT | 2026-08-15T03:07:29+00:00 | 1,00892 | €-80,61 | -1,61 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-57,05 | -1,14 | STOP |
| Rapida 1H V3 Filtered | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-5,56 | -1,14 | STOP |
| 1H Fast Tp2 V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07055 | €-1,20 | -1,60 | STOP_GAP_STRESS |
| 1H Fast Tp2 V1 | SOL | SHORT | 2026-08-15T03:07:29+00:00 | 75,91019 | €-74,38 | -1,53 | STOP_GAP_STRESS |
| 1H Fast Score 6 75 V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-59,29 | -1,14 | STOP |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | SHORT | 2026-08-15T03:07:29+00:00 | 0,07034 | €-57,71 | -1,14 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
