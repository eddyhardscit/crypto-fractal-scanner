# Paper trading automatico KuCoin

Generato: 2026-08-16T05:35:19+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-16T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-16T05:05:29+00:00 | 2026-08-16T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-16T04:45:00+00:00 | 2026-08-16T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-16T04:00:00+00:00 | 2026-08-16T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-16T00:00:00+00:00 | 2026-08-16T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Nohigh Regime Guard V1 | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Tp3 V1 | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Runner25 V1 | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | HEMI | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | HEMI | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,52 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,26 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -5,25 | 6,00 | 0,75 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,63 | 6,00 | 1,37 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 3,12 | 6,00 | 2,88 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ACE | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | SHORT | -2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,50 | 6,00 | 4,50 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,24 | 6,00 | 5,76 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | CYS | 60m | SHORT | -8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Short Trend Down Strict V1 | CYS | 60m | SHORT | -8,25 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | 60m | SHORT | -8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.643,73 | -3,56% | €-104,62 | €3.000,00 | -3,49% | 5 | 41 | 34,15% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 41 | 1383 | PRIME INDICAZIONI | 100 (mancano 59) |

- Trade del Principale 4H chiusi: **41**; win rate **34,15%**; profit factor **0,72**.
- Expectancy: **€-9,22** per trade; P&L netto: **€-378,20**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.643,73 | €1.282,24 | €3.846,72 | €192,66 | €21,36 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 3 | €10.696,38 | €1.867,00 | €5.600,99 | €105,82 | €12,28 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.610,05 | €5.489,59 | €10.979,18 | €213,00 | €-43,92 |
| TEST | Main Side Regime Guard V1 | 5 | €10.505,70 | €2.120,40 | €6.361,19 | €208,03 | €33,96 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.454,97 | €1.868,84 | €5.606,51 | €156,75 | €-18,14 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.372,20 | €630,99 | €1.892,98 | €154,78 | €24,03 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.360,25 | €5.360,34 | €10.720,69 | €207,98 | €-42,89 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.355,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.296,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.273,29 | €3.579,41 | €7.158,82 | €202,98 | €-5,55 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €10.263,80 | €465,20 | €1.395,61 | €102,78 | €19,43 |
| TEST | 1H Fast No Pepe V1 | 8 | €10.256,67 | €1.305,83 | €3.917,48 | €205,14 | €-0,55 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.177,00 | €1.819,15 | €5.457,44 | €152,58 | €-17,66 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €10.167,10 | €488,12 | €1.464,35 | €152,11 | €-11,44 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €10.074,56 | €2.835,57 | €8.506,72 | €201,46 | €-0,07 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 5 | €10.052,43 | €3.308,92 | €9.926,77 | €199,99 | €-15,15 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.029,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.028,52 | €3.797,60 | €7.595,20 | €149,28 | €57,31 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €10.008,39 | €453,63 | €1.360,88 | €100,22 | €18,95 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.001,40 | €1.155,63 | €3.466,88 | €49,92 | €17,10 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €9.990,37 | €5.854,36 | €11.708,72 | €199,89 | €-5,80 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 8 | €9.980,64 | €1.262,35 | €3.787,06 | €196,18 | €-38,64 |
| TEST | Btc Ema 4H | 1 | €9.978,94 | €1.413,45 | €2.826,90 | €49,75 | €27,27 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 9 | €9.970,18 | €2.948,63 | €5.897,26 | €198,70 | €0,12 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 9 | €9.966,82 | €2.459,86 | €7.379,59 | €200,26 | €-28,14 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 7 | €9.942,70 | €3.411,19 | €6.822,38 | €198,03 | €-12,11 |
| TEST | Scanner Bottom15 Short | 7 | €9.942,70 | €3.411,19 | €6.822,38 | €198,03 | €-12,11 |
| TEST | Scanner Bottom20 Short | 7 | €9.942,70 | €3.411,19 | €6.822,38 | €198,03 | €-12,11 |
| TEST | Doge Donchian 1H | 1 | €9.932,58 | €1.295,48 | €3.886,44 | €49,75 | €-15,19 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.930,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.920,72 | €1.406,00 | €2.812,00 | €49,49 | €21,19 |
| TEST | Btc Ema 1H | 1 | €9.887,79 | €1.146,03 | €3.438,09 | €49,51 | €-12,58 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 7 | €9.875,30 | €3.392,69 | €6.785,37 | €196,69 | €-12,42 |
| TEST | Bilanciata 1H V2 | 5 | €9.870,91 | €3.350,44 | €10.051,32 | €147,47 | €39,68 |
| TEST | Ampia 4H | 5 | €9.869,61 | €1.622,85 | €3.245,70 | €197,51 | €-3,48 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 7 | €9.860,28 | €3.387,52 | €6.775,05 | €196,39 | €-12,40 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.850,28 | €4.450,10 | €8.900,20 | €197,60 | €-28,11 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 5 | €9.836,15 | €4.525,18 | €9.050,36 | €195,78 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 1 | €9.798,81 | €1.483,05 | €4.449,14 | €49,83 | €-31,92 |
| TEST | Scanner Bottom 5 Short 1H | 7 | €9.784,40 | €3.361,46 | €6.722,91 | €194,88 | €-12,30 |
| TEST | Rapida 1H V2 | 1 | €9.783,68 | €1.457,13 | €4.371,38 | €48,96 | €-5,37 |
| TEST | Sol Ema 1H | 1 | €9.780,36 | €1.135,84 | €3.407,53 | €49,07 | €-31,74 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 7 | €9.752,96 | €1.878,98 | €5.636,93 | €148,20 | €-1,45 |
| TEST | Combo Adaptive Runner25 V1 | 9 | €9.748,17 | €2.377,64 | €4.755,28 | €194,27 | €0,07 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 4 | €9.704,33 | €1.368,77 | €2.737,53 | €146,07 | €-27,69 |
| TEST | Combo Mean Reversion | 1 | €9.702,79 | €1.946,42 | €3.892,84 | €46,71 | €14,82 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.697,24 | €1.885,33 | €5.655,99 | €191,50 | €-51,76 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.696,38 | €1.043,30 | €2.086,60 | €48,49 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.692,01 | €1.512,09 | €3.024,18 | €48,39 | €14,92 |
| TEST | Rapida 1H V3 Filtered | 7 | €9.689,23 | €1.866,70 | €5.600,09 | €147,23 | €-1,44 |
| TEST | Sol Adaptive 1H | 0 | €9.674,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.658,10 | €3.058,79 | €6.117,59 | €193,41 | €-14,24 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 4 | €9.649,85 | €1.110,67 | €3.332,00 | €97,18 | €-14,58 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.643,07 | €3.389,16 | €6.778,32 | €192,89 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €9.635,16 | €1.788,40 | €5.365,19 | €96,00 | €-14,44 |
| TEST | Combo Adaptive Long Only V1 | 6 | €9.629,52 | €5.081,16 | €10.162,32 | €192,05 | €-5,85 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €9.609,01 | €2.281,77 | €4.563,53 | €102,02 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.597,36 | €1.113,68 | €3.341,04 | €48,11 | €-23,01 |
| TEST | Combo Adaptive Quality7 Regime V1 | 4 | €9.582,27 | €1.351,55 | €2.703,10 | €144,24 | €-27,34 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 9 | €9.573,81 | €2.831,41 | €5.662,82 | €190,80 | €0,12 |
| TEST | Combo Adaptive Tp3 V1 | 9 | €9.566,05 | €2.333,22 | €4.666,45 | €190,64 | €0,07 |
| TEST | Combo Trend | 10 | €9.553,67 | €2.513,21 | €5.026,42 | €190,59 | €3,14 |
| TEST | Master Adaptive Expanded V1 | 7 | €9.541,95 | €3.348,54 | €6.697,07 | €191,02 | €-9,21 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.540,89 | €3.021,67 | €6.043,35 | €191,07 | €-14,07 |
| TEST | 1H Balanced V3 Long Only V1 | 7 | €9.528,92 | €2.682,00 | €8.045,99 | €190,54 | €-0,07 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.492,39 | €3.006,31 | €6.012,63 | €190,10 | €-14,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.483,25 | €3.302,21 | €9.906,62 | €190,47 | €4,08 |
| TEST | 1H Fast V3 No Esports V1 | 7 | €9.479,05 | €1.251,22 | €3.753,66 | €187,05 | €-1,24 |
| TEST | Master Adaptive No Alt V1 | 7 | €9.444,47 | €4.002,37 | €8.004,73 | €189,52 | €-22,96 |
| TEST | Forza relativa 1H V1 | 6 | €9.395,55 | €3.858,68 | €7.717,35 | €187,94 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 11 | €9.330,89 | €2.753,96 | €5.507,92 | €186,63 | €-0,45 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.319,00 | €2.951,40 | €5.902,80 | €186,62 | €-13,74 |
| TEST | Master Adaptive Gb20 Be V1 | 4 | €9.296,06 | €2.910,18 | €5.820,37 | €142,09 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 4 | €9.287,16 | €2.188,42 | €4.376,84 | €97,98 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 4 | €9.286,18 | €2.907,09 | €5.814,18 | €141,94 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 4 | €9.281,72 | €2.187,14 | €4.374,28 | €97,92 | €0,00 |
| TEST | Master Adaptive V1 | 4 | €9.250,26 | €2.895,85 | €5.791,69 | €141,39 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.222,16 | €2.084,57 | €4.169,14 | €142,64 | €1,11 |
| TEST | Scanner Top10 Long | 5 | €9.202,44 | €5.178,05 | €10.356,10 | €184,12 | €-5,34 |
| TEST | Scanner Top15 Long | 5 | €9.202,44 | €5.178,05 | €10.356,10 | €184,12 | €-5,34 |
| TEST | Scanner Top20 Long | 5 | €9.202,44 | €5.178,05 | €10.356,10 | €184,12 | €-5,34 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.191,87 | €2.685,00 | €8.055,00 | €184,05 | €-8,76 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 4 | €9.182,37 | €2.180,46 | €4.360,91 | €97,49 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €9.173,72 | €1.702,75 | €5.108,25 | €91,40 | €-13,75 |
| TEST | Combo Scanner | 4 | €9.132,55 | €3.404,76 | €6.809,52 | €142,05 | €5,38 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.127,36 | €2.857,37 | €5.714,74 | €139,51 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 0 | €9.028,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €9.007,06 | €2.138,83 | €4.277,65 | €95,62 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 7 | €8.992,59 | €2.607,91 | €5.215,81 | €179,86 | €-0,29 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.973,84 | €3.002,71 | €6.005,42 | €179,89 | €0,78 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.643,73 | €-378,20 | 41 | 41 | 34,15% | 0,72 | €-9,22 | 6,36% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.696,38 | €687,07 | 65 | 65 | 52,31% | 1,52 | €10,57 | 3,35% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.610,05 | €660,35 | 60 | 60 | 48,33% | 1,46 | €11,01 | 3,63% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.505,70 | €470,38 | 21 | 21 | 52,38% | 2,09 | €22,40 | 2,40% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.454,97 | €409,12 | 115 | 114 | 44,35% | 1,16 | €3,56 | 4,89% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.372,20 | €349,26 | 48 | 48 | 50,00% | 1,35 | €7,28 | 5,24% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.360,25 | €409,36 | 28 | 28 | 46,43% | 1,71 | €14,62 | 3,63% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.355,43 | €355,43 | 33 | 33 | 48,48% | 1,52 | €10,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.296,26 | €296,26 | 31 | 31 | 51,61% | 1,36 | €9,56 | 2,31% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.273,29 | €279,20 | 44 | 44 | 52,27% | 1,35 | €6,35 | 2,94% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.263,80 | €245,14 | 103 | 103 | 43,69% | 1,11 | €2,38 | 6,52% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.256,67 | €255,06 | 107 | 107 | 43,93% | 1,13 | €2,38 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.177,00 | €132,36 | 73 | 72 | 47,95% | 1,07 | €1,81 | 5,23% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.167,10 | €179,42 | 105 | 105 | 42,86% | 1,08 | €1,71 | 6,72% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.074,56 | €79,75 | 86 | 86 | 38,37% | 1,04 | €0,93 | 6,13% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.052,43 | €72,16 | 6 | 6 | 50,00% | 1,54 | €12,03 | 1,59% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.029,32 | €29,32 | 6 | 6 | 66,67% | 1,27 | €4,89 | 1,49% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.028,52 | €-28,36 | 54 | 54 | 44,44% | 0,97 | €-0,53 | 6,65% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.008,39 | €-9,80 | 67 | 67 | 41,79% | 0,99 | €-0,15 | 6,52% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Doge Ema 1H | Trend following EMA | €10.001,40 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €9.990,37 | €3,17 | 70 | 70 | 42,86% | 1,00 | €0,05 | 8,24% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.980,64 | €-36,86 | 122 | 122 | 36,89% | 0,99 | €-0,30 | 3,95% |
| TEST | Btc Ema 4H | Trend following EMA | €9.978,94 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Combo Adaptive | Combo Adaptive | €9.970,18 | €-26,42 | 66 | 66 | 39,39% | 0,98 | €-0,40 | 5,27% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.966,82 | €-0,69 | 95 | 95 | 42,11% | 1,00 | €-0,01 | 6,96% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.942,70 | €-40,50 | 48 | 48 | 37,50% | 0,96 | €-0,84 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.942,70 | €-40,50 | 48 | 48 | 37,50% | 0,96 | €-0,84 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.942,70 | €-40,50 | 48 | 48 | 37,50% | 0,96 | €-0,84 | 5,27% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.932,58 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 2,06% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.930,86 | €-69,14 | 7 | 7 | 42,86% | 0,63 | €-9,88 | 2,20% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.920,72 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Btc Ema 1H | Trend following EMA | €9.887,79 | €-98,30 | 8 | 8 | 37,50% | 0,63 | €-12,29 | 1,72% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.875,30 | €-107,61 | 40 | 40 | 37,50% | 0,87 | €-2,69 | 5,27% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.870,91 | €-162,81 | 62 | 57 | 45,16% | 0,89 | €-2,63 | 5,74% |
| TEST | Ampia 4H | Confluenza trend | €9.869,61 | €-127,20 | 35 | 35 | 22,86% | 0,86 | €-3,63 | 4,36% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.860,28 | €-122,66 | 41 | 41 | 36,59% | 0,85 | €-2,99 | 5,27% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.850,28 | €-114,85 | 27 | 27 | 40,74% | 0,80 | €-4,25 | 2,91% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.836,15 | €-157,59 | 70 | 67 | 40,00% | 0,93 | €-2,25 | 8,11% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.798,81 | €-167,76 | 34 | 34 | 44,12% | 0,81 | €-4,93 | 4,17% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.784,40 | €-198,67 | 68 | 68 | 35,29% | 0,86 | €-2,92 | 6,41% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.783,68 | €-208,11 | 29 | 26 | 37,93% | 0,74 | €-7,18 | 3,89% |
| TEST | Sol Ema 1H | Trend following EMA | €9.780,36 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 3,07% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.752,96 | €-249,15 | 86 | 86 | 47,67% | 0,85 | €-2,90 | 7,17% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.748,17 | €-249,10 | 71 | 71 | 33,80% | 0,82 | €-3,51 | 6,25% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.704,33 | €-269,24 | 19 | 19 | 36,84% | 0,59 | €-14,17 | 3,78% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.702,79 | €-308,68 | 30 | 30 | 36,67% | 0,70 | €-10,29 | 4,90% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.697,24 | €-248,82 | 91 | 91 | 42,86% | 0,89 | €-2,73 | 6,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.696,38 | €-301,34 | 69 | 69 | 43,48% | 0,83 | €-4,37 | 6,53% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.692,01 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.689,23 | €-312,87 | 130 | 130 | 38,46% | 0,89 | €-2,41 | 7,14% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.674,16 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 3,94% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.658,10 | €-324,63 | 40 | 40 | 37,50% | 0,76 | €-8,12 | 6,54% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.649,85 | €-333,68 | 66 | 66 | 40,91% | 0,82 | €-5,06 | 4,70% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.643,07 | €-352,86 | 38 | 38 | 28,95% | 0,62 | €-9,29 | 5,72% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.635,16 | €-349,28 | 60 | 60 | 35,00% | 0,77 | €-5,82 | 8,59% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.629,52 | €-359,17 | 41 | 41 | 34,15% | 0,68 | €-8,76 | 4,74% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.609,01 | €-388,92 | 61 | 61 | 34,43% | 0,77 | €-6,38 | 9,72% |
| TEST | Eth Ema 1H | Trend following EMA | €9.597,36 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 4,10% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.582,27 | €-391,64 | 19 | 19 | 26,32% | 0,42 | €-20,61 | 4,99% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.573,81 | €-422,92 | 67 | 67 | 37,31% | 0,68 | €-6,31 | 6,07% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.566,05 | €-431,26 | 52 | 52 | 32,69% | 0,61 | €-8,29 | 6,25% |
| TEST | Combo Trend | Combo Trend | €9.553,67 | €-447,01 | 96 | 96 | 33,33% | 0,82 | €-4,66 | 9,82% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.541,95 | €-444,92 | 42 | 42 | 30,95% | 0,70 | €-10,59 | 4,86% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.540,89 | €-442,05 | 45 | 45 | 33,33% | 0,70 | €-9,82 | 6,13% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.528,92 | €-466,17 | 42 | 42 | 33,33% | 0,50 | €-11,10 | 5,85% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.492,39 | €-490,63 | 55 | 55 | 38,18% | 0,70 | €-8,92 | 5,80% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.483,25 | €-577,79 | 71 | 71 | 43,66% | 0,74 | €-8,14 | 6,61% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.479,05 | €-575,14 | 104 | 104 | 38,46% | 0,76 | €-5,53 | 7,03% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.444,47 | €-527,38 | 41 | 41 | 29,27% | 0,66 | €-12,86 | 6,03% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.395,55 | €-600,43 | 81 | 81 | 29,63% | 0,68 | €-7,41 | 8,96% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.330,89 | €-665,98 | 64 | 64 | 28,12% | 0,58 | €-10,41 | 7,60% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.319,00 | €-664,33 | 62 | 62 | 37,10% | 0,64 | €-10,72 | 7,59% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.296,06 | €-700,47 | 42 | 42 | 21,43% | 0,49 | €-16,68 | 8,35% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.287,16 | €-710,85 | 46 | 46 | 28,26% | 0,54 | €-15,45 | 10,06% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.286,18 | €-710,36 | 37 | 37 | 27,03% | 0,46 | €-19,20 | 7,95% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.281,72 | €-716,29 | 50 | 50 | 30,00% | 0,53 | €-14,33 | 10,36% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.250,26 | €-746,29 | 39 | 39 | 25,64% | 0,50 | €-19,14 | 7,76% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.222,16 | €-779,92 | 38 | 38 | 21,05% | 0,50 | €-20,52 | 8,05% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.202,44 | €-786,82 | 42 | 42 | 33,33% | 0,43 | €-18,73 | 9,70% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.202,44 | €-786,82 | 42 | 42 | 33,33% | 0,43 | €-18,73 | 9,70% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.202,44 | €-786,82 | 42 | 42 | 33,33% | 0,43 | €-18,73 | 9,70% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.191,87 | €-797,68 | 44 | 44 | 29,55% | 0,48 | €-18,13 | 9,05% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.182,37 | €-815,65 | 42 | 42 | 28,57% | 0,42 | €-19,42 | 10,18% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.173,72 | €-811,47 | 80 | 80 | 28,75% | 0,63 | €-10,14 | 10,56% |
| TEST | Combo Scanner | Combo Scanner | €9.132,55 | €-871,50 | 66 | 66 | 33,33% | 0,57 | €-13,20 | 10,63% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.127,36 | €-869,24 | 74 | 74 | 47,30% | 0,49 | €-11,75 | 8,99% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.028,46 | €-971,54 | 32 | 32 | 15,62% | 0,30 | €-30,36 | 11,05% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.007,06 | €-991,00 | 54 | 54 | 29,63% | 0,34 | €-18,35 | 10,74% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.992,59 | €-1.003,97 | 79 | 79 | 31,65% | 0,46 | €-12,71 | 11,05% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.973,84 | €-1.023,08 | 44 | 44 | 25,00% | 0,50 | €-23,25 | 10,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00054 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €20,98 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63065,37000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €0,38 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,06979 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €0,12 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00054 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €0,24 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,03281 | 0,03281 | 0,03675 | 0,04359 | 0,02494 | €125,03 | €375,08 | €45,01 | €-0,00 |
| Bilanciata 1H V1 | LINK | LONG | Confluenza trend | 60m | 3,0x | 9,55473 | 9,55473 | 9,38106 | 6,41759 | 9,90208 | €916,82 | €2.750,47 | €49,99 | €0,00 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 57,05121 | 57,12000 | 56,22967 | 38,31940 | 58,69429 | €46,83 | €140,50 | €2,02 | €0,17 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 0,37325 | 0,39873 | 0,41804 | 0,49579 | 0,28367 | €138,89 | €416,67 | €50,00 | €-28,45 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 487,26746 | 488,39000 | 494,28412 | 647,25361 | 473,23416 | €24,62 | €73,85 | €1,06 | €-0,17 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63004,39660 | 63065,37000 | 63911,65991 | 83690,84015 | 61189,86998 | €18,78 | €56,35 | €0,81 | €-0,05 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1182,39901 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1632,05865 | 1632,05865 | 1586,54905 | 1096,19939 | 1723,07784 | €570,53 | €1.711,58 | €47,73 | €0,00 |
| 1H Balanced Long No Rhv V1 | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 57,28235 | 57,12000 | 56,45748 | 38,47464 | 58,93208 | €1.030,75 | €3.092,25 | €44,53 | €-8,76 |
| 1H Balanced Short Trend Down Strict V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,06979 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €17,11 |
| 1H Balanced Short Trend Down Strict V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1866,05671 | 1880,76000 | 1892,92793 | 2478,74534 | 1812,31428 | €23,32 | €69,97 | €1,01 | €-0,55 |
| 1H Balanced Short Trend Down Strict V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,71805 | 75,41400 | 75,79399 | 99,25048 | 72,56617 | €1.131,56 | €3.394,68 | €48,88 | €-31,62 |
| 1H Balanced Short Trend Down Strict V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,56510 | €139,62 | €418,87 | €50,26 | €-0,08 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00054 | 1,01986 | 1,33548 | 0,97642 | €37,09 | €111,28 | €1,60 | €0,54 |
| Bilanciata 1H V2 | LINK | LONG | Confluenza trend V2 | 60m | 3,0x | 9,57674 | 9,57674 | 9,40948 | 6,43238 | 9,91127 | €938,54 | €2.815,61 | €49,18 | €0,00 |
| Bilanciata 1H V2 | ACE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,15317 | 0,13880 | 0,15317 | 0,20346 | 0,11641 | €136,55 | €409,66 | €0,00 | €38,43 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 57,10724 | 57,12000 | 56,28490 | 38,35703 | 58,75193 | €1.058,58 | €3.175,75 | €45,73 | €0,71 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06979 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,10 |
| Bilanciata 1H V3 Filtered | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €457,69 | €1.373,07 | €49,01 | €0,00 |
| Bilanciata 1H V3 Filtered | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €127,78 | €383,34 | €46,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 9,57674 | 9,57674 | 9,40948 | 6,43238 | 9,91127 | €961,53 | €2.884,60 | €50,38 | €0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 57,10724 | 57,12000 | 56,28490 | 38,35703 | 58,75193 | €39,44 | €118,32 | €1,70 | €0,03 |
| 1H Fast Score 6 75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €0,00 | €0,00 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,19029 | 57,12000 | 56,54976 | 38,41281 | 58,15109 | €1.544,74 | €4.634,22 | €51,90 | €-5,70 |
| 1H Fast Score 6 75 V1 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €144,97 | €434,90 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13880 | 0,15117 | 0,17929 | 0,11068 | €146,27 | €438,81 | €52,66 | €-12,44 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €0,00 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,19029 | 57,12000 | 56,54976 | 38,41281 | 58,15109 | €1.503,67 | €4.511,01 | €50,52 | €-5,54 |
| 1H Fast Score 6 75 No Trend Up V1 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €141,11 | €423,34 | €50,80 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13880 | 0,15117 | 0,17929 | 0,11068 | €142,38 | €427,15 | €51,26 | €-12,11 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99774 | 1,00054 | 1,00892 | 1,32533 | 0,98098 | €1.572,34 | €4.717,02 | €52,83 | €-13,24 |
| 1H Fast Score 6 75 Cost Aware V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,13880 | 0,15317 | 0,20346 | 0,12560 | €147,46 | €442,37 | €0,00 | €41,50 |
| 1H Fast Score 6 75 Cost Aware V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01047 | 0,01009 | 0,00921 | 0,00703 | 0,01235 | €147,20 | €441,60 | €52,99 | €-15,99 |
| 1H Fast Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €140,04 | €420,12 | €50,41 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,19029 | 57,12000 | 56,54976 | 38,41281 | 58,15109 | €15,46 | €46,37 | €0,52 | €-0,06 |
| 1H Fast Nohigh Cap75 V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,13880 | 0,15317 | 0,20346 | 0,12560 | €138,95 | €416,85 | €0,00 | €39,11 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01055 | 0,01009 | 0,00934 | 0,00709 | 0,01236 | €150,59 | €451,77 | €51,85 | €-19,61 |
| 1H Fast No Pepe V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €771,03 | €2.313,08 | €50,17 | €0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €142,21 | €426,63 | €51,20 | €-0,00 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1191,94474 | 1191,94474 | 1171,66933 | 800,58955 | 1222,35785 | €47,86 | €143,59 | €2,44 | €0,00 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €10,42 | €31,26 | €0,35 | €-0,22 |
| 1H Fast No Pepe V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06539 | 0,06539 | 0,05878 | 0,04392 | 0,07530 | €166,06 | €498,19 | €50,35 | €0,00 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,19029 | 57,12000 | 56,54976 | 38,41281 | 58,15109 | €16,68 | €50,04 | €0,56 | €-0,06 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06949 | 0,06979 | 0,07027 | 0,09230 | 0,06832 | €13,76 | €41,29 | €0,46 | €-0,18 |
| 1H Fast No Pepe V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,60971 | €137,80 | €413,41 | €49,61 | €-0,08 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03778 | 0,03531 | 0,05019 | 0,02871 | €9,36 | €28,07 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1182,39901 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €0,00 |
| 1H Fast Tp2 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1632,91916 | 1632,91916 | 1597,68836 | 1096,77737 | 1703,38077 | €753,45 | €2.260,36 | €48,77 | €0,00 |
| 1H Fast Tp2 V1 | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,08248 | €168,46 | €505,38 | €48,56 | €0,00 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,28235 | 57,12000 | 56,64079 | 38,47464 | 58,56547 | €22,40 | €67,20 | €0,75 | €-0,19 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,37325 | 0,39873 | 0,41804 | 0,49579 | 0,28367 | €128,14 | €384,41 | €46,13 | €-26,25 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06949 | 0,06979 | 0,07027 | 0,09230 | 0,06793 | €25,03 | €75,08 | €0,84 | €-0,33 |
| 1H Fast Tp2 V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13880 | 0,15117 | 0,17929 | 0,10258 | €139,64 | €418,91 | €50,27 | €-11,88 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 57,19029 | 57,12000 | 56,54976 | 38,41281 | 58,15109 | €1.457,13 | €4.371,38 | €48,96 | €-5,37 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €0,00 | €0,00 |
| Rapida 1H V3 Filtered | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €752,55 | €2.257,65 | €48,96 | €0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €136,31 | €408,92 | €49,07 | €-0,00 |
| Rapida 1H V3 Filtered | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,43 | €169,29 | €1,90 | €-1,21 |
| Rapida 1H V3 Filtered | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,48 | €49,45 | €4,75 | €0,00 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06949 | 0,06979 | 0,07027 | 0,09230 | 0,06832 | €11,75 | €35,26 | €0,39 | €-0,15 |
| Rapida 1H V3 Filtered | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,60971 | €117,10 | €351,30 | €42,16 | €-0,07 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €0,00 | €0,00 |
| 1H Fast V3 Cap75 V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03283 | 0,03283 | 0,03677 | 0,04361 | 0,02692 | €139,04 | €417,11 | €50,05 | €-0,00 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,87611 | 57,12000 | 56,23909 | 38,20178 | 57,83162 | €52,70 | €158,10 | €1,77 | €0,68 |
| 1H Fast V3 Cap75 V1 | APR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €136,16 | €408,49 | €49,02 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13497 | 0,13880 | 0,15117 | 0,17929 | 0,11068 | €142,42 | €427,26 | €51,27 | €-12,11 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €135,40 | €406,20 | €48,74 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.450,98 | €4.352,95 | €48,75 | €-31,23 |
| 1H Fast V3 Nohigh V1 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13207 | 0,13880 | 0,14792 | 0,17544 | 0,10830 | €133,86 | €401,59 | €48,19 | €-20,45 |
| 1H Fast V3 Nohigh V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,60971 | €127,26 | €381,79 | €45,81 | €-0,08 |
| 1H Fast V3 Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €135,06 | €405,19 | €45,82 | €0,00 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01047 | 0,01009 | 0,00921 | 0,00703 | 0,01235 | €126,63 | €379,89 | €45,59 | €-13,75 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €0,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €144,03 | €432,09 | €48,86 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01047 | 0,01009 | 0,00921 | 0,00703 | 0,01235 | €134,23 | €402,69 | €48,32 | €-14,58 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €0,00 | €0,00 |
| 1H Fast V3 No Esports V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €736,66 | €2.209,98 | €47,93 | €0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €133,42 | €400,27 | €48,03 | €-0,00 |
| 1H Fast V3 No Esports V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €47,04 | €141,11 | €1,58 | €-1,01 |
| 1H Fast V3 No Esports V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €163,10 | €489,29 | €47,02 | €0,00 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06949 | 0,06979 | 0,07027 | 0,09230 | 0,06832 | €11,73 | €35,19 | €0,39 | €-0,15 |
| 1H Fast V3 No Esports V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,60971 | €116,91 | €350,74 | €42,09 | €-0,07 |
| 1H Fast V3 No Esports Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €141,86 | €425,58 | €48,12 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01047 | 0,01009 | 0,00921 | 0,00703 | 0,01235 | €133,00 | €399,00 | €47,88 | €-14,44 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1177,17118 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1632,05865 | 1632,05865 | 1596,66230 | 1096,19939 | 1685,15317 | €757,50 | €2.272,50 | €49,29 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €137,20 | €411,61 | €49,39 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €56,80 | €170,41 | €1,91 | €-1,22 |
| 1H Fast V3 No Esports Mfe Lock V1 | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,59 | €49,77 | €4,78 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06949 | 0,06979 | 0,07027 | 0,09230 | 0,06832 | €11,83 | €35,50 | €0,40 | €-0,15 |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,60971 | €117,87 | €353,61 | €42,43 | €-0,07 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €1.483,05 | €4.449,14 | €49,83 | €-31,92 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1165,32878 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1618,90076 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 9,38563 | 9,38563 | 9,22869 | 6,30401 | 9,62103 | €949,50 | €2.848,50 | €47,63 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,87611 | 57,12000 | 56,23909 | 38,20178 | 57,83162 | €1.396,89 | €4.190,66 | €46,94 | €17,97 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01047 | 0,01009 | 0,00921 | 0,00703 | 0,01235 | €127,95 | €383,84 | €46,06 | €-13,89 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00054 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €16,34 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63065,37000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €0,64 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,01062 | 0,01009 | 0,00934 | 0,00536 | 0,01419 | €205,94 | €411,89 | €49,43 | €-20,46 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €79,48 | €158,95 | €3,52 | €0,00 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,03281 | 0,03281 | 0,03675 | 0,04906 | 0,02415 | €186,76 | €373,52 | €44,82 | €-0,00 |
| Forza relativa 1H V1 | LINK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 9,55473 | 9,55473 | 9,38106 | 4,82514 | 9,93681 | €1.168,48 | €2.336,96 | €42,48 | €0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02493 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Forza relativa 1H V2 | LINK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 9,55473 | 9,55473 | 9,38106 | 4,82514 | 9,93681 | €1.353,07 | €2.706,14 | €49,19 | €0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06979 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-13,05 |
| Benchmark Donchian breakout 1H | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €858,65 | €1.717,31 | €52,93 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,41400 | 75,91354 | 111,70349 | 71,72933 | €1.657,45 | €3.314,90 | €53,04 | €-30,88 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06979 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-12,74 |
| Donchian 1H Gb20 120R V1 | SNDK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1632,91916 | 1632,91916 | 1582,58944 | 824,62418 | 1758,74346 | €838,44 | €1.676,87 | €51,68 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 74,71805 | 75,41400 | 75,91354 | 111,70349 | 71,72933 | €1.618,43 | €3.236,85 | €51,79 | €-30,15 |
| Benchmark Bollinger mean reversion 1H | SNDK | SHORT | Bollinger mean reversion | 60m | 2,0x | 1630,10135 | 1630,10135 | 1667,98054 | 2437,00152 | 1573,28257 | €1.043,30 | €2.086,60 | €48,49 | €-0,00 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,06979 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,23 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,00 |
| Benchmark trend following EMA 1H | SNDK | LONG | Trend following EMA | 60m | 2,0x | 1632,05865 | 1632,05865 | 1581,49243 | 824,18962 | 1743,30434 | €724,64 | €1.449,29 | €44,90 | €0,00 |
| Benchmark trend following EMA 1H | ETH | SHORT | Trend following EMA | 60m | 2,0x | 1867,89635 | 1880,76000 | 1897,78269 | 2792,50504 | 1802,14639 | €18,13 | €36,25 | €0,58 | €-0,25 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 62898,88771 | 63065,37000 | 63905,26991 | 94033,83712 | 60684,84686 | €27,47 | €54,94 | €0,88 | €-0,15 |
| Benchmark trend following EMA 1H | LINK | LONG | Trend following EMA | 60m | 2,0x | 9,53572 | 9,53572 | 9,32866 | 4,81554 | 9,99124 | €19,22 | €38,44 | €0,83 | €0,00 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 1,00054 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €-0,07 |
| Benchmark trend following EMA 1H | HEMI | LONG | Trend following EMA | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01028 | €175,09 | €350,18 | €42,02 | €-0,21 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.146,19 | €2.292,38 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | LINK | LONG | Scanner Top 5 Long | 60m | 2,0x | 9,48969 | 9,48969 | 9,33289 | 4,79229 | 9,80330 | €1.512,97 | €3.025,95 | €50,00 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 57,22031 | 57,12000 | 56,39634 | 28,89626 | 58,86826 | €1.654,13 | €3.308,27 | €47,64 | €-5,80 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €0,28 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €200,12 | €400,25 | €48,03 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,41400 | 75,79399 | 111,70349 | 72,56617 | €21,64 | €43,28 | €0,62 | €-0,40 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,06979 | 0,07049 | 0,10388 | 0,06749 | €69,53 | €139,06 | €2,00 | €-0,60 |
| Scanner Bottom 5 Short 1H | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,10258 | €204,10 | €408,20 | €48,98 | €-11,57 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top10 Long | SNDK | LONG | Scanner Top10 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 9,48969 | 9,48969 | 9,33289 | 4,79229 | 9,80330 | €1.393,65 | €2.787,29 | €46,06 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 57,22031 | 57,12000 | 56,39634 | 28,89626 | 58,86826 | €1.524,24 | €3.048,49 | €43,90 | €-5,34 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,28 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,16396 | 75,41400 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,11 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06949 | 0,06979 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,51 |
| Scanner Bottom10 Short | ACE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-11,76 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top15 Long | SNDK | LONG | Scanner Top15 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top15 Long | LINK | LONG | Scanner Top15 Long | 60m | 2,0x | 9,48969 | 9,48969 | 9,33289 | 4,79229 | 9,80330 | €1.393,65 | €2.787,29 | €46,06 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 57,22031 | 57,12000 | 56,39634 | 28,89626 | 58,86826 | €1.524,24 | €3.048,49 | €43,90 | €-5,34 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,28 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,16396 | 75,41400 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,11 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06949 | 0,06979 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,51 |
| Scanner Bottom15 Short | ACE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-11,76 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €0,00 |
| Scanner Top20 Long | SNDK | LONG | Scanner Top20 Long | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54905 | 824,18962 | 1723,07784 | €837,75 | €1.675,49 | €46,72 | €0,00 |
| Scanner Top20 Long | LINK | LONG | Scanner Top20 Long | 60m | 2,0x | 9,48969 | 9,48969 | 9,33289 | 4,79229 | 9,80330 | €1.393,65 | €2.787,29 | €46,06 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 57,22031 | 57,12000 | 56,39634 | 28,89626 | 58,86826 | €1.524,24 | €3.048,49 | €43,90 | €-5,34 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,28 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,16396 | 75,41400 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,11 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06949 | 0,06979 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,51 |
| Scanner Bottom20 Short | ACE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-11,76 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €22,01 | €44,02 | €1,20 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €20,63 | €41,26 | €1,12 | €0,00 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €0,00 |
| Scanner Top5 Btc Guard V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €890,44 | €1.780,87 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 9,94568 | €1.153,03 | €2.306,05 | €45,07 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01047 | 0,01009 | 0,00921 | 0,00529 | 0,01323 | €194,33 | €388,66 | €46,64 | €-14,07 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €21,03 | €42,07 | €1,14 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €869,73 | €1.739,45 | €47,32 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 9,94568 | €1.126,21 | €2.252,42 | €44,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01047 | 0,01009 | 0,00921 | 0,00529 | 0,01323 | €189,81 | €379,63 | €45,56 | €-13,74 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €901,37 | €1.802,75 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 9,94568 | €1.167,19 | €2.334,38 | €45,62 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01047 | 0,01009 | 0,00921 | 0,00529 | 0,01323 | €196,72 | €393,44 | €47,21 | €-14,24 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68064 | 829,90965 | 1741,73601 | €885,91 | €1.771,82 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 9,94568 | €1.147,16 | €2.294,33 | €44,84 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01047 | 0,01009 | 0,00921 | 0,00529 | 0,01323 | €193,34 | €386,69 | €46,40 | €-14,00 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,67 | €0,92 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €12,84 | €25,69 | €0,92 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,06979 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €14,92 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,06979 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,29 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1175,20470 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,00 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1618,90076 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €0,00 |
| Combo Trend | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02351 | €194,61 | €389,21 | €46,71 | €-0,00 |
| Combo Trend | LINK | LONG | Combo Trend | 60m | 2,0x | 9,53572 | 9,53572 | 9,32866 | 4,81554 | 9,99124 | €19,15 | €38,30 | €0,83 | €0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 57,05121 | 57,12000 | 56,13839 | 28,81086 | 59,05941 | €1.283,49 | €2.566,97 | €41,07 | €3,10 |
| Combo Trend | HEMI | LONG | Combo Trend | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01028 | €199,04 | €398,09 | €47,77 | €-0,24 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 63065,37000 | 62072,20924 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €46,71 | €14,82 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,06979 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €5,38 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1247,25345 | €1.034,30 | €2.068,59 | €45,78 | €0,00 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06979 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,31 |
| Combo Adaptive | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,00 | €0,00 |
| Combo Adaptive | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €686,66 | €1.373,32 | €49,73 | €0,00 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,07222 | 57,12000 | 56,25038 | 28,82147 | 58,71590 | €32,27 | €64,54 | €0,93 | €0,05 |
| Combo Adaptive | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,48969 | 9,48969 | 9,33289 | 4,79229 | 9,80330 | €56,97 | €113,94 | €1,88 | €0,00 |
| Combo Adaptive | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01008 | €199,00 | €397,99 | €47,76 | €-0,24 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive Mfe Trail | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €15,03 | €30,05 | €0,67 | €0,00 |
| Combo Adaptive Mfe Trail | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €619,25 | €1.238,49 | €44,85 | €0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,06979 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,07 |
| Combo Adaptive Mfe Trail | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 9,90841 | €13,34 | €26,68 | €0,52 | €0,00 |
| Combo Adaptive Mfe Trail | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01008 | €183,00 | €366,01 | €43,92 | €-0,22 |
| Combo Adaptive Quality7 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1175,20470 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €0,00 |
| Combo Adaptive Quality7 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1632,91916 | 1632,91916 | 1587,62241 | 824,62418 | 1723,51265 | €880,79 | €1.761,58 | €48,87 | €0,00 |
| Combo Adaptive Quality7 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02574 | €203,75 | €407,50 | €48,90 | €-0,00 |
| Combo Adaptive Quality7 V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,55473 | 9,55473 | 9,38106 | 4,82514 | 9,90208 | €1.280,06 | €2.560,13 | €46,53 | €0,00 |
| Combo Adaptive Regime V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37325 | 0,39873 | 0,41804 | 0,55800 | 0,28367 | €205,84 | €411,68 | €49,40 | €-28,11 |
| Combo Adaptive Regime V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,57674 | 9,57674 | 9,40948 | 4,83626 | 9,91127 | €1.410,60 | €2.821,20 | €49,27 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €919,84 | €1.839,67 | €46,79 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37325 | 0,39873 | 0,41804 | 0,55800 | 0,28367 | €200,22 | €400,44 | €48,05 | €-27,34 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €0,00 |
| Combo Adaptive Long Only V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1652,37083 | 1652,37083 | 1605,97924 | 834,44727 | 1745,15401 | €13,30 | €26,61 | €0,75 | €0,00 |
| Combo Adaptive Long Only V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,57474 | 9,57474 | 9,39396 | 4,83524 | 9,93631 | €1.169,50 | €2.339,00 | €44,16 | €0,00 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,22031 | 57,12000 | 56,39634 | 28,89626 | 58,86826 | €1.669,05 | €3.338,11 | €48,07 | €-5,85 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06979 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,30 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,00 | €0,00 |
| Combo Adaptive Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1623,18333 | 1564,40406 | 819,70758 | 1740,74186 | €659,36 | €1.318,73 | €47,75 | €0,00 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,07222 | 57,12000 | 56,25038 | 28,82147 | 58,71590 | €30,99 | €61,97 | €0,89 | €0,05 |
| Combo Adaptive Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,48969 | 9,48969 | 9,33289 | 4,79229 | 9,80330 | €54,70 | €109,41 | €1,81 | €0,00 |
| Combo Adaptive Partial 1R V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01008 | €191,09 | €382,17 | €45,86 | €-0,23 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1646,22714 | 1646,22714 | 1604,35529 | 831,34471 | 1729,97087 | €931,55 | €1.863,10 | €47,39 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37325 | 0,39873 | 0,41804 | 0,55800 | 0,28367 | €202,77 | €405,54 | €48,67 | €-27,69 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive Runner25 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06979 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,30 |
| Combo Adaptive Runner25 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,00 | €0,00 |
| Combo Adaptive Runner25 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,35 | €34,70 | €1,24 | €0,00 |
| Combo Adaptive Runner25 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €204,60 | €409,21 | €49,10 | €-0,00 |
| Combo Adaptive Runner25 V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 10,09476 | €22,65 | €45,29 | €0,89 | €0,00 |
| Combo Adaptive Runner25 V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01106 | €192,86 | €385,72 | €46,29 | €-0,23 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive Tp3 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06979 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,30 |
| Combo Adaptive Tp3 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1177,05643 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,00 | €0,00 |
| Combo Adaptive Tp3 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72441 | 825,72069 | 1810,18864 | €17,03 | €34,05 | €1,22 | €0,00 |
| Combo Adaptive Tp3 V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,53572 | 9,53572 | 9,34937 | 4,81554 | 10,09476 | €22,22 | €44,45 | €0,87 | €0,00 |
| Combo Adaptive Tp3 V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,00813 | 0,00813 | 0,00715 | 0,00411 | 0,01106 | €189,26 | €378,51 | €45,42 | €-0,23 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62835,53038 | 63065,37000 | 63740,36202 | 83466,52952 | 61025,86711 | €1.146,03 | €3.438,09 | €49,51 | €-12,58 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63065,37000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €27,27 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63065,37000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €21,19 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 74,71805 | 75,41400 | 75,79399 | 99,25048 | 72,56617 | €1.135,84 | €3.407,53 | €49,07 | €-31,74 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1867,89635 | 1880,76000 | 1894,79405 | 2481,18898 | 1814,10093 | €1.113,68 | €3.341,04 | €48,11 | €-23,01 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,06979 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €17,10 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,06979 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-15,19 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,93 | €73,85 | €1,65 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €626,90 | €1.253,80 | €44,76 | €0,00 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1643,38544 | 1643,38544 | 1598,68062 | 829,90965 | 1732,79507 | €22,94 | €45,88 | €1,25 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01046 | 0,01009 | 0,00921 | 0,00528 | 0,01297 | €201,41 | €402,81 | €48,34 | €-14,30 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,28235 | 57,12000 | 56,45748 | 28,92759 | 58,93208 | €1.526,97 | €3.053,94 | €43,98 | €-8,66 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1167,82027 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1655,75286 | 1655,75286 | 1602,89078 | 836,15519 | 1761,47701 | €734,74 | €1.469,49 | €46,92 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01009 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,78 |
| Master Adaptive Strict3 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,57474 | 9,57474 | 9,39396 | 4,83524 | 9,93631 | €1.124,01 | €2.248,02 | €42,45 | €0,00 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1618,90076 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.101,72 | €2.203,44 | €48,77 | €0,00 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,19029 | 57,12000 | 56,36675 | 28,88110 | 58,83737 | €14,67 | €29,33 | €0,42 | €-0,04 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01035 | 0,01009 | 0,00910 | 0,00522 | 0,01283 | €185,66 | €371,32 | €44,56 | €-9,18 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,43 | €72,87 | €1,62 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €618,57 | €1.237,14 | €44,16 | €0,00 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 57,12000 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €1,11 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1165,32878 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,00 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1632,05865 | 1632,05865 | 1586,54904 | 824,18962 | 1768,58749 | €850,90 | €1.701,80 | €47,45 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,06979 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €5,51 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €12,82 |
| Combo Adaptive Side Regime Guard V1 | ACE | SHORT | Combo Adaptive | 60m | 2,0x | 0,15317 | 0,13880 | 0,15317 | 0,22899 | 0,11641 | €207,74 | €415,49 | €0,00 | €38,98 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,11 | €74,22 | €1,65 | €0,00 |
| Master Adaptive Gb20 Be V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €630,00 | €1.260,01 | €44,98 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,07 | €74,14 | €1,65 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1635,09047 | 1576,72439 | 825,72069 | 1751,82260 | €629,33 | €1.258,67 | €44,93 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €143,50 | €430,49 | €51,66 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 62616,17426 | 63065,37000 | 63317,47541 | 83175,15148 | 61564,22253 | €63,81 | €191,43 | €2,14 | €-1,37 |
| 1H Fast V3 Nohigh Regime Guard V1 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15317 | 0,13880 | 0,15317 | 0,20346 | 0,12560 | €143,19 | €429,58 | €0,00 | €40,30 |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01047 | 0,01009 | 0,00921 | 0,00703 | 0,01235 | €136,43 | €409,28 | €49,11 | €-14,82 |
| 1H Fast V3 Nohigh Regime Guard V1 | CYS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,74355 | 0,74370 | 0,83278 | 0,98768 | 0,60971 | €144,06 | €432,19 | €51,86 | €-0,09 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00054 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €22,02 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63065,37000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €17,15 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01009 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €-5,21 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,06979 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-5,59 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00054 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €12,20 |
| Combo Trend Side Regime Guard V1 | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ACE | SHORT | Combo Trend | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,09934 | €214,51 | €429,02 | €51,48 | €-12,16 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1618,90076 | 1619,81688 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €0,00 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €136,56 | €409,67 | €49,16 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,19029 | 57,12000 | 56,54976 | 38,41281 | 58,15109 | €15,07 | €45,21 | €0,51 | €-0,06 |
| 1H Fast Nohigh Cap75 Short Only V1 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,13880 | 0,15317 | 0,20346 | 0,12560 | €135,49 | €406,48 | €0,00 | €38,13 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01055 | 0,01009 | 0,00934 | 0,00709 | 0,01236 | €146,84 | €440,52 | €50,56 | €-19,13 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06979 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,09 |
| 1H Balanced V3 Long Only V1 | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1635,09047 | 1576,72441 | 1098,23576 | 1751,82258 | €432,90 | €1.298,70 | €46,36 | €0,00 |
| 1H Balanced V3 Long Only V1 | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €120,86 | €362,58 | €43,51 | €-0,00 |
| 1H Balanced V3 Long Only V1 | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 9,57674 | 9,57674 | 9,40948 | 6,43238 | 9,91127 | €909,46 | €2.728,37 | €47,65 | €0,00 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 57,10724 | 57,12000 | 56,28490 | 38,35703 | 58,75193 | €37,30 | €111,91 | €1,61 | €0,02 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €0,28 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,68 | €403,35 | €48,40 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,41400 | 75,79399 | 111,70349 | 72,56617 | €21,81 | €43,62 | €0,63 | €-0,41 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,06979 | 0,07049 | 0,10388 | 0,06749 | €70,07 | €140,14 | €2,02 | €-0,61 |
| Scanner Bottom5 Short Profit Lock V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,10258 | €205,68 | €411,36 | €49,36 | €-11,66 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00054 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €0,28 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,98 | €403,97 | €48,48 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 74,71805 | 75,41400 | 75,79399 | 111,70349 | 72,56617 | €21,84 | €43,69 | €0,63 | €-0,41 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,06979 | 0,07049 | 0,10388 | 0,06749 | €70,18 | €140,35 | €2,02 | €-0,61 |
| Scanner Bottom5 Short Mfe Trail V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13880 | 0,15117 | 0,20178 | 0,10258 | €205,99 | €411,99 | €49,44 | €-11,68 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-9,31 | -0,22 | STOP_GAP_STRESS |
| Combo Trend | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-73,30 | -1,52 | STOP_GAP_STRESS |
| Combo Adaptive Tp3 V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-9,84 | -0,22 | STOP_GAP_STRESS |
| Combo Adaptive Runner25 V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-10,02 | -0,22 | STOP_GAP_STRESS |
| Combo Adaptive Partial 1R V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-10,16 | -0,22 | STOP_GAP_STRESS |
| Combo Adaptive Mfe Trail | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-9,51 | -0,22 | STOP_GAP_STRESS |
| Combo Adaptive | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-10,58 | -0,22 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-9,20 | -0,22 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports Mfe Lock V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-9,28 | -0,22 | STOP_GAP_STRESS |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-10,07 | -0,22 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-63,89 | -1,25 | STOP_GAP_STRESS |
| Rapida 1H V3 Filtered | BEAT | SHORT | 2026-08-16T05:06:14+00:00 | 0,40074 | €-9,22 | -0,22 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
