# Paper trading automatico KuCoin

Generato: 2026-08-17T13:09:30+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-17T13:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-17T13:05:28+00:00 | 2026-08-17T13:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-17T12:45:00+00:00 | 2026-08-17T12:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-17T12:00:00+00:00 | 2026-08-17T12:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-17T08:00:00+00:00 | 2026-08-17T08:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | ZEC | 60m | LONG | 5,12 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BEAT | 240m | SHORT | -8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTW | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -6,88 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,12 | 6,00 | 0,88 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,68 | 6,00 | 1,32 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,07 | 6,00 | 1,93 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,82 | 6,00 | 2,18 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,46 | 6,00 | 2,54 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | H | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,67 | 6,00 | 3,33 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,25 | 6,00 | 5,75 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Benchmark trend following EMA 1H | BEAT | 60m | SHORT | -8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — MFE Trail esistente | BEAT | 60m | SHORT | -8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | PEPE | 60m | SHORT | -6,80 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — score <7,5 | PEPE | 60m | SHORT | -6,80 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | PEPE | 60m | SHORT | -6,80 | 4,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | PEPE | 60m | SHORT | -6,80 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata V3 · LONG only | PEPE | 60m | SHORT | -6,80 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | ZEC | 60m | LONG | 5,12 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.650,19 | -3,50% | €-98,16 | €3.000,00 | -3,27% | 6 | 41 | 34,15% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 41 | 1496 | PRIME INDICAZIONI | 50 (mancano 9) |

- Trade del Principale 4H chiusi: **41**; win rate **34,15%**; profit factor **0,72**.
- Expectancy: **€-9,22** per trade; P&L netto: **€-378,20**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.650,19 | €1.293,51 | €3.880,53 | €193,20 | €27,65 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.726,23 | €4.573,29 | €9.146,58 | €104,61 | €73,40 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.663,43 | €1.719,80 | €5.159,39 | €52,83 | €2,37 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.531,02 | €1.866,27 | €5.598,80 | €157,77 | €17,69 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.496,27 | €2.140,55 | €6.421,66 | €209,71 | €26,50 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.473,69 | €4.465,62 | €8.931,24 | €102,14 | €71,67 |
| TEST | Rapida V1 — senza PEPE | 7 | €10.392,36 | €560,90 | €1.682,71 | €105,65 | €56,03 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.348,78 | €386,22 | €1.158,67 | €51,78 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.332,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 3 | €10.293,25 | €468,63 | €1.405,90 | €100,23 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.282,53 | €3.665,13 | €7.330,26 | €205,66 | €4,76 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €10.251,02 | €1.816,65 | €5.449,94 | €153,57 | €17,22 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 3 | €10.236,70 | €1.795,51 | €5.386,53 | €102,36 | €-11,94 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 5 | €10.158,24 | €1.992,88 | €5.978,65 | €203,27 | €-2,69 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 7 | €10.123,71 | €761,36 | €1.522,72 | €102,71 | €96,51 |
| TEST | Scanner Bottom15 Short | 7 | €10.123,71 | €761,36 | €1.522,72 | €102,71 | €96,51 |
| TEST | Scanner Bottom20 Short | 7 | €10.123,71 | €761,36 | €1.522,72 | €102,71 | €96,51 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 3 | €10.101,03 | €2.361,30 | €7.083,89 | €102,01 | €-5,46 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €10.059,36 | €1.988,64 | €5.965,91 | €100,82 | €140,95 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €10.053,78 | €766,73 | €1.533,45 | €102,32 | €95,50 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €10.039,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €10.038,49 | €765,56 | €1.531,12 | €102,16 | €95,36 |
| TEST | FAST NoHigh <7,5 · SHORT only | 3 | €10.037,11 | €456,97 | €1.370,92 | €97,74 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.021,36 | €4.647,03 | €9.294,06 | €151,02 | €1,43 |
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
| TEST | Doge Ema 1H | 1 | €9.991,92 | €1.155,63 | €3.466,88 | €49,92 | €6,23 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 4 | €9.987,85 | €3.797,60 | €7.595,20 | €149,28 | €19,14 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €9.984,81 | €1.662,17 | €3.324,34 | €199,40 | €31,07 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.973,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 6 | €9.965,70 | €1.026,77 | €2.053,54 | €4,35 | €155,81 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.961,24 | €759,67 | €1.519,34 | €101,38 | €94,62 |
| TEST | Btc Ema 4H | 1 | €9.960,39 | €1.413,45 | €2.826,90 | €49,75 | €8,33 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.956,33 | €1.259,31 | €2.518,63 | €49,91 | €-24,25 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 5 | €9.933,36 | €557,11 | €1.671,33 | €103,32 | €84,57 |
| TEST | Sol Donchian 4H | 0 | €9.931,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.902,34 | €1.406,00 | €2.812,00 | €49,49 | €2,31 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €9.892,10 | €2.119,98 | €4.239,96 | €97,11 | €92,67 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €9.880,81 | €365,19 | €1.095,56 | €58,92 | €56,82 |
| TEST | Sol Donchian 1H | 0 | €9.875,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.848,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.838,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 6 | €9.816,24 | €362,80 | €1.088,40 | €58,54 | €56,45 |
| TEST | Bilanciata 1H V1 | 10 | €9.813,09 | €694,42 | €2.083,27 | €99,03 | €90,88 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €9.811,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.805,38 | €1.690,92 | €3.381,84 | €49,43 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.792,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.775,43 | €204,24 | €408,49 | €49,02 | €-4,35 |
| TEST | Eth Donchian 1H | 0 | €9.762,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.760,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 3 | €9.720,12 | €436,17 | €872,34 | €50,02 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 3 | €9.692,88 | €1.411,12 | €2.822,23 | €48,90 | €85,92 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €9.689,76 | €400,32 | €1.200,95 | €48,89 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 8 | €9.687,67 | €1.721,85 | €3.443,70 | €56,06 | €180,84 |
| TEST | Global Confluence puro 1H | 1 | €9.683,73 | €1.512,09 | €3.024,18 | €48,39 | €5,43 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €9.682,26 | €1.572,93 | €4.718,79 | €96,21 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 2 | €9.668,53 | €350,52 | €1.051,56 | €96,76 | €0,00 |
| TEST | Combo Adaptive — Long Only | 4 | €9.653,79 | €4.504,41 | €9.008,83 | €145,17 | €3,30 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.631,30 | €340,67 | €1.022,00 | €94,01 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.621,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.610,35 | €202,90 | €405,81 | €0,00 | €45,92 |
| TEST | Combo Trend | 9 | €9.598,54 | €2.624,05 | €5.248,09 | €144,92 | €100,64 |
| TEST | Combo Adaptive — Quality7 + Regime | 3 | €9.597,86 | €430,68 | €861,36 | €49,39 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 6 | €9.592,44 | €482,95 | €1.448,85 | €99,16 | €50,84 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 6 | €9.569,52 | €985,95 | €1.971,91 | €4,18 | €149,62 |
| TEST | Eth Ema 1H | 0 | €9.548,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €9.541,68 | €2.823,50 | €5.647,00 | €96,67 | €1,51 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €9.515,42 | €3.073,53 | €6.147,06 | €138,04 | €9,61 |
| TEST | Bilanciata V3 · LONG only | 7 | €9.514,55 | €1.880,93 | €5.642,79 | €95,36 | €133,32 |
| TEST | Rapida V3 — qualità completa + profit lock | 4 | €9.512,33 | €2.591,80 | €7.775,40 | €141,13 | €18,49 |
| TEST | Combo Adaptive — target pieno 3R | 8 | €9.506,69 | €1.689,68 | €3.379,36 | €55,01 | €177,46 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.434,23 | €4.591,20 | €9.182,41 | €141,98 | €1,47 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 5 | €9.423,52 | €3.626,15 | €7.252,31 | €141,24 | €48,44 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 5 | €9.413,50 | €3.622,30 | €7.244,59 | €141,09 | €48,39 |
| TEST | Top 5 + BTC — Guard | 4 | €9.399,94 | €3.036,23 | €6.072,45 | €136,36 | €9,49 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.379,86 | €1.244,74 | €3.734,22 | €137,28 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.377,09 | €3.608,29 | €7.216,57 | €140,55 | €48,21 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.358,59 | €3.828,36 | €7.656,71 | €143,72 | €1,65 |
| TEST | Forza relativa 1H V1 | 7 | €9.355,15 | €2.902,61 | €5.805,21 | €143,54 | €78,46 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €9.352,16 | €3.020,79 | €6.041,59 | €135,67 | €9,44 |
| TEST | Benchmark trend following EMA 1H | 10 | €9.324,11 | €4.372,07 | €8.744,14 | €140,23 | €74,63 |
| TEST | Scanner Top10 Long | 5 | €9.311,34 | €4.542,03 | €9.084,06 | €183,76 | €-6,14 |
| TEST | Scanner Top15 Long | 5 | €9.311,34 | €4.542,03 | €9.084,06 | €183,76 | €-6,14 |
| TEST | Scanner Top20 Long | 5 | €9.311,34 | €4.542,03 | €9.084,06 | €183,76 | €-6,14 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.293,92 | €4.183,19 | €8.366,38 | €181,68 | €77,04 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.252,50 | €3.560,34 | €7.120,69 | €138,68 | €47,57 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €9.222,11 | €2.736,18 | €5.472,35 | €93,25 | €2,46 |
| TEST | Rapida V3 — Long Only | 2 | €9.218,56 | €1.497,60 | €4.492,80 | €91,60 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €9.216,72 | €2.734,58 | €5.469,15 | €93,20 | €2,46 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.181,33 | €2.965,61 | €5.931,23 | €133,19 | €9,27 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €9.118,03 | €2.698,14 | €5.396,27 | €92,38 | €1,44 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 2 | €9.112,68 | €3.642,04 | €7.284,08 | €78,67 | €-10,08 |
| TEST | Combo Scanner | 3 | €9.060,67 | €3.897,54 | €7.795,08 | €91,21 | €-3,41 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.946,76 | €3.297,63 | €6.595,26 | €178,31 | €45,75 |
| TEST | Top 5 + BTC — solo MFE | 3 | €8.943,94 | €2.646,62 | €5.293,24 | €90,62 | €1,42 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €8.893,68 | €261,11 | €522,22 | €46,56 | €-0,32 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.650,19 | €-378,20 | 41 | 41 | 34,15% | 0,72 | €-9,22 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.726,23 | €657,21 | 63 | 63 | 47,62% | 1,44 | €10,43 | 3,63% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.663,43 | €665,67 | 70 | 70 | 51,43% | 1,46 | €9,51 | 3,35% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.531,02 | €453,16 | 123 | 122 | 44,72% | 1,17 | €3,68 | 4,89% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.496,27 | €467,84 | 22 | 22 | 50,00% | 2,08 | €21,27 | 2,40% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.473,69 | €406,30 | 31 | 31 | 45,16% | 1,64 | €13,11 | 3,63% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.392,36 | €333,97 | 119 | 119 | 43,70% | 1,16 | €2,81 | 3,64% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.348,78 | €349,47 | 33 | 33 | 51,52% | 1,41 | €10,59 | 2,31% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.332,02 | €332,02 | 34 | 34 | 47,06% | 1,47 | €9,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.293,25 | €297,01 | 112 | 112 | 44,64% | 1,13 | €2,65 | 6,52% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.282,53 | €280,64 | 45 | 45 | 53,33% | 1,36 | €6,24 | 2,94% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.251,02 | €175,23 | 81 | 80 | 48,15% | 1,09 | €2,16 | 5,23% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.236,70 | €254,87 | 54 | 54 | 46,30% | 1,23 | €4,72 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.158,24 | €168,47 | 113 | 113 | 42,48% | 1,07 | €1,49 | 6,72% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €10.123,71 | €31,71 | 54 | 54 | 35,19% | 1,03 | €0,59 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €10.123,71 | €31,71 | 54 | 54 | 35,19% | 1,03 | €0,59 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €10.123,71 | €31,71 | 54 | 54 | 35,19% | 1,03 | €0,59 | 5,27% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.101,03 | €107,35 | 10 | 10 | 40,00% | 1,56 | €10,74 | 1,80% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.059,36 | €-78,31 | 94 | 94 | 37,23% | 0,96 | €-0,83 | 7,10% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €10.053,78 | €-37,24 | 46 | 46 | 34,78% | 0,96 | €-0,81 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.039,30 | €39,30 | 6 | 6 | 50,00% | 1,24 | €6,55 | 1,89% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €10.038,49 | €-52,40 | 47 | 47 | 34,04% | 0,94 | €-1,11 | 5,27% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.037,11 | €40,78 | 76 | 76 | 43,42% | 1,03 | €0,54 | 6,52% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.021,36 | €24,97 | 73 | 73 | 43,84% | 1,01 | €0,34 | 8,85% |
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
| TEST | Doge Ema 1H | Trend following EMA | €9.991,92 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,10% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.987,85 | €-29,86 | 55 | 55 | 43,64% | 0,97 | €-0,54 | 6,65% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Ampia 4H | Confluenza trend | €9.984,81 | €-46,73 | 37 | 37 | 24,32% | 0,95 | €-1,26 | 4,45% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.973,77 | €-26,23 | 7 | 7 | 57,14% | 0,84 | €-3,75 | 1,49% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.965,70 | €-189,06 | 75 | 75 | 37,33% | 0,87 | €-2,52 | 5,40% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.961,24 | €-128,95 | 74 | 74 | 33,78% | 0,91 | €-1,74 | 6,41% |
| TEST | Btc Ema 4H | Trend following EMA | €9.960,39 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.956,33 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.933,36 | €-204,87 | 135 | 135 | 35,56% | 0,93 | €-1,52 | 3,95% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.931,19 | €-68,81 | 3 | 3 | 33,33% | 0,35 | €-22,94 | 0,87% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.902,34 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.892,10 | €-198,16 | 73 | 70 | 39,73% | 0,91 | €-2,71 | 8,11% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.880,81 | €-181,11 | 99 | 99 | 45,45% | 0,90 | €-1,83 | 7,17% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.875,62 | €-124,38 | 8 | 8 | 37,50% | 0,49 | €-15,55 | 2,74% |
| TEST | Btc Ema 1H | Trend following EMA | €9.848,58 | €-151,42 | 9 | 9 | 33,33% | 0,53 | €-16,82 | 1,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.838,66 | €-161,34 | 31 | 28 | 38,71% | 0,80 | €-5,20 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.816,24 | €-245,27 | 143 | 143 | 37,76% | 0,92 | €-1,72 | 7,14% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.813,09 | €-276,93 | 104 | 104 | 39,42% | 0,86 | €-2,66 | 8,81% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.811,70 | €-188,30 | 38 | 38 | 44,74% | 0,80 | €-4,96 | 4,50% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.805,38 | €-192,61 | 32 | 32 | 40,62% | 0,75 | €-6,02 | 3,91% |
| TEST | Sol Ema 4H | Trend following EMA | €9.792,72 | €-207,28 | 4 | 4 | 0,00% | 0,00 | €-51,82 | 2,10% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.775,43 | €-219,97 | 33 | 33 | 42,42% | 0,79 | €-6,67 | 5,09% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.762,69 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Sol Ema 1H | Trend following EMA | €9.760,52 | €-239,48 | 9 | 9 | 22,22% | 0,37 | €-26,61 | 3,16% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.720,12 | €-282,28 | 22 | 22 | 36,36% | 0,63 | €-12,83 | 4,21% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.692,88 | €-391,47 | 41 | 41 | 29,27% | 0,63 | €-9,55 | 7,10% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.689,76 | €-306,78 | 68 | 62 | 42,65% | 0,81 | €-4,51 | 6,62% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.687,67 | €-490,86 | 78 | 78 | 32,05% | 0,69 | €-6,29 | 6,85% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.683,73 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,53% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.682,26 | €-314,91 | 66 | 66 | 36,36% | 0,80 | €-4,77 | 8,59% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.668,53 | €-330,84 | 103 | 103 | 42,72% | 0,87 | €-3,21 | 6,10% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.653,79 | €-344,11 | 45 | 45 | 35,56% | 0,71 | €-7,65 | 5,16% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.631,30 | €-368,09 | 71 | 71 | 40,85% | 0,81 | €-5,18 | 5,23% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.621,05 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,47% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.610,35 | €-435,33 | 73 | 73 | 42,47% | 0,78 | €-5,96 | 6,53% |
| TEST | Combo Trend | Combo Trend | €9.598,54 | €-499,69 | 103 | 103 | 33,98% | 0,81 | €-4,85 | 9,82% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.597,86 | €-404,51 | 22 | 22 | 27,27% | 0,48 | €-18,39 | 5,41% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.592,44 | €-514,08 | 117 | 117 | 37,61% | 0,80 | €-4,39 | 7,03% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.569,52 | €-579,09 | 76 | 76 | 35,53% | 0,63 | €-7,62 | 6,20% |
| TEST | Eth Ema 1H | Trend following EMA | €9.548,70 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,51% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.541,68 | €-456,45 | 65 | 65 | 35,38% | 0,74 | €-7,02 | 10,37% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.515,42 | €-490,31 | 45 | 45 | 35,56% | 0,69 | €-10,90 | 7,74% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.514,55 | €-615,67 | 50 | 50 | 32,00% | 0,44 | €-12,31 | 6,83% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.512,33 | €-564,16 | 75 | 75 | 44,00% | 0,75 | €-7,52 | 6,85% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.506,69 | €-668,51 | 59 | 59 | 30,51% | 0,50 | €-11,33 | 6,85% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.434,23 | €-561,48 | 46 | 46 | 30,43% | 0,67 | €-12,21 | 6,80% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.423,52 | €-620,30 | 44 | 44 | 22,73% | 0,55 | €-14,10 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.413,50 | €-630,28 | 39 | 39 | 28,21% | 0,53 | €-16,16 | 7,98% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.399,94 | €-605,72 | 50 | 50 | 32,00% | 0,64 | €-12,11 | 7,34% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.379,86 | €-620,37 | 46 | 46 | 32,61% | 0,60 | €-13,49 | 9,05% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.377,09 | €-666,52 | 41 | 41 | 26,83% | 0,56 | €-16,26 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.358,59 | €-638,88 | 49 | 49 | 32,65% | 0,62 | €-13,04 | 6,90% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.355,15 | €-720,61 | 85 | 85 | 29,41% | 0,64 | €-8,48 | 9,65% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.352,16 | €-653,48 | 60 | 60 | 36,67% | 0,64 | €-10,89 | 7,02% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.324,11 | €-745,43 | 70 | 70 | 28,57% | 0,57 | €-10,65 | 9,01% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.311,34 | €-676,97 | 45 | 45 | 35,56% | 0,53 | €-15,04 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.311,34 | €-676,97 | 45 | 45 | 35,56% | 0,53 | €-15,04 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.311,34 | €-676,97 | 45 | 45 | 35,56% | 0,53 | €-15,04 | 10,31% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.293,92 | €-781,07 | 40 | 40 | 22,50% | 0,50 | €-19,53 | 8,18% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.252,50 | €-790,53 | 76 | 76 | 47,37% | 0,53 | €-10,40 | 9,02% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.222,11 | €-777,07 | 49 | 49 | 28,57% | 0,52 | €-15,86 | 10,71% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.218,56 | €-778,74 | 86 | 86 | 30,23% | 0,65 | €-9,06 | 10,56% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.216,72 | €-782,46 | 53 | 53 | 30,19% | 0,52 | €-14,76 | 11,00% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.181,33 | €-824,20 | 67 | 67 | 35,82% | 0,59 | €-12,30 | 8,78% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.118,03 | €-880,18 | 46 | 46 | 30,43% | 0,41 | €-19,13 | 10,82% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.112,68 | €-872,67 | 33 | 33 | 18,18% | 0,37 | €-26,44 | 11,09% |
| TEST | Combo Scanner | Combo Scanner | €9.060,67 | €-935,23 | 70 | 70 | 34,29% | 0,56 | €-13,36 | 11,38% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.946,76 | €-1.094,57 | 45 | 45 | 24,44% | 0,48 | €-24,32 | 11,51% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €8.943,94 | €-1.054,30 | 58 | 58 | 31,03% | 0,34 | €-18,18 | 11,38% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €8.893,68 | €-1.105,71 | 89 | 89 | 31,46% | 0,47 | €-12,42 | 11,89% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99724 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €27,96 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63492,10000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €-0,10 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,07001 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,21 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,07001 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €-0,11 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 0,99724 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €0,44 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,03281 | 0,03281 | 0,03675 | 0,04359 | 0,02494 | €125,03 | €375,08 | €45,01 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63004,39660 | 63492,10000 | 63911,65991 | 83690,84015 | 61189,86998 | €18,78 | €56,35 | €0,81 | €-0,44 |
| Bilanciata 1H V1 | ACE | SHORT | Confluenza trend | 60m | 3,0x | 0,14042 | 0,14042 | 0,15727 | 0,18652 | 0,10672 | €129,09 | €387,27 | €46,47 | €-0,00 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 0,36815 | 0,28527 | 0,31949 | 0,48902 | 0,27979 | €135,05 | €405,14 | €0,00 | €91,21 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1889,17209 | 1897,77000 | 1916,37617 | 2509,45026 | 1834,76393 | €43,74 | €131,21 | €1,89 | €-0,60 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,93 | €104,79 | €1,51 | €0,39 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 509,54189 | 509,44000 | 501,00074 | 342,24230 | 526,62418 | €27,00 | €81,00 | €1,36 | €-0,02 |
| Bilanciata 1H — LONG senza Range High Vol | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1182,39901 | 1197,94321 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,00 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| Bilanciata 1H — SHORT Trend Down stretto | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,07001 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €6,23 |
| Bilanciata 1H — SHORT Trend Down stretto | BTC | SHORT | Confluenza trend | 60m | 3,0x | 62929,63156 | 63492,10000 | 63835,81825 | 83591,52725 | 61117,25817 | €34,60 | €103,79 | €1,49 | €-0,93 |
| Bilanciata 1H — SHORT Trend Down stretto | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 0,99724 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €-10,76 |
| Bilanciata 1H V2 | ACE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,11641 | €136,55 | €409,66 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07001 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,23 |
| Bilanciata 1H V3 Filtered | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1698,82000 | 1682,47471 | 1098,23576 | 1751,82258 | €457,69 | €1.373,07 | €0,00 | €53,52 |
| Bilanciata 1H V3 Filtered | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €127,78 | €383,34 | €46,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99724 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €0,26 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 62892,88891 | 63492,10000 | 63798,54651 | 83542,72076 | 61081,57371 | €40,14 | €120,43 | €1,73 | €-1,15 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,36815 | 0,28527 | 0,31949 | 0,48902 | 0,27979 | €134,23 | €402,68 | €0,00 | €90,65 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.164,76 | €3.494,29 | €50,32 | €-2,10 |
| Rapida V1 — score 6–7,5 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €144,97 | €434,90 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €146,27 | €438,81 | €52,66 | €-0,00 |
| Rapida V1 — score 6–7,5 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.575,03 | €4.725,08 | €52,92 | €17,69 |
| Rapida score 6–7,5 — senza Trend Up | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €141,11 | €423,34 | €50,80 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €142,38 | €427,15 | €51,26 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.533,15 | €4.599,45 | €51,51 | €17,22 |
| Rapida score 6–7,5 — Range Only | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99774 | 0,99724 | 1,00892 | 1,32533 | 0,98098 | €1.572,34 | €4.717,02 | €52,83 | €2,37 |
| Rapida score 6–7,5 — Cost Aware | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €147,46 | €442,37 | €0,00 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €140,04 | €420,12 | €50,41 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €138,95 | €416,85 | €0,00 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €142,21 | €426,63 | €51,20 | €-0,00 |
| Rapida V1 — senza PEPE | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1191,94474 | 1191,94474 | 1202,08391 | 800,58955 | 1222,35785 | €47,86 | €143,59 | €0,00 | €0,00 |
| Rapida V1 — senza PEPE | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06539 | 0,06539 | 0,05878 | 0,04392 | 0,07530 | €166,06 | €498,19 | €50,35 | €0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| Rapida V1 — senza PEPE | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,33071 | 0,28527 | 0,31438 | 0,43930 | 0,27166 | €137,71 | €413,13 | €0,00 | €56,77 |
| Rapida V1 — senza PEPE | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 59,42488 | 59,07000 | 58,75932 | 39,91371 | 60,42322 | €42,68 | €128,04 | €1,43 | €-0,76 |
| Rapida V1 — senza PEPE | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 509,15181 | 509,44000 | 502,05689 | 341,98030 | 519,79419 | €14,75 | €44,25 | €0,62 | €0,03 |
| Rapida V1 — target pieno 2R | CAP | LONG | Momentum / breakout | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,08248 | €168,46 | €505,38 | €48,56 | €0,00 |
| Rapida V1 — target pieno 2R | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,10258 | €139,64 | €418,91 | €50,27 | €-0,00 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,37290 | 0,28527 | 0,32028 | 0,49533 | 0,28340 | €118,31 | €354,93 | €0,00 | €83,40 |
| Rapida V1 — target pieno 2R | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €115,44 | €346,32 | €3,88 | €1,30 |
| Rapida V1 — target pieno 2R | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 510,90216 | 509,44000 | 504,08853 | 343,15595 | 524,52942 | €15,26 | €45,78 | €0,61 | €-0,13 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €136,31 | €408,92 | €49,07 | €-0,00 |
| Rapida 1H V3 Filtered — madre | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,48 | €49,45 | €4,75 | €0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered — madre | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33071 | 0,28527 | 0,31438 | 0,43930 | 0,27166 | €136,27 | €408,82 | €0,00 | €56,17 |
| Rapida 1H V3 Filtered — madre | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,60192 | 1220,60192 | 1206,93118 | 819,83762 | 1241,10803 | €37,58 | €112,74 | €1,26 | €0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,35 | €73,04 | €0,82 | €0,27 |
| Rapida V3 — score <7,5 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03283 | 0,03283 | 0,03677 | 0,04361 | 0,02692 | €139,04 | €417,11 | €50,05 | €-0,00 |
| Rapida V3 — score <7,5 | APR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €136,16 | €408,49 | €49,02 | €-0,00 |
| Rapida V3 — score <7,5 | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13497 | 0,13497 | 0,15117 | 0,17929 | 0,11068 | €142,42 | €427,26 | €51,27 | €-0,00 |
| Rapida V3 — score <7,5 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,60192 | 1220,60192 | 1206,93118 | 819,83762 | 1241,10803 | €80,60 | €241,80 | €2,71 | €0,00 |
| Rapida V3 — score <7,5 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.494,66 | €4.483,99 | €50,22 | €-2,69 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €135,40 | €406,20 | €48,74 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| Rapida V3 — Long Only | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €135,06 | €405,19 | €45,82 | €0,00 |
| Rapida V3 — Long Only | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,60192 | 1220,60192 | 1206,93118 | 819,83762 | 1241,10803 | €1.362,54 | €4.087,61 | €45,78 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €144,03 | €432,09 | €48,86 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €133,42 | €400,27 | €48,03 | €-0,00 |
| Rapida V3 — senza ESPORTS | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €163,10 | €489,29 | €47,02 | €0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| Rapida V3 — senza ESPORTS | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33071 | 0,28527 | 0,31438 | 0,43930 | 0,27166 | €122,83 | €368,49 | €0,00 | €50,63 |
| Rapida V3 — senza ESPORTS | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,60192 | 1220,60192 | 1206,93118 | 819,83762 | 1241,10803 | €34,85 | €104,56 | €1,17 | €0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,35 | €55,04 | €0,62 | €0,21 |
| Rapida V3 senza ESPORTS — Long Only | EDEN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06225 | 0,06225 | 0,05521 | 0,04181 | 0,07281 | €141,86 | €425,58 | €48,12 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,60192 | 1220,60192 | 1206,93118 | 819,83762 | 1241,10803 | €1.431,07 | €4.293,21 | €48,08 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €137,20 | €411,61 | €49,39 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | CAP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06918 | 0,06918 | 0,06253 | 0,04647 | 0,07915 | €16,59 | €49,77 | €4,78 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33071 | 0,28527 | 0,31438 | 0,43930 | 0,27166 | €137,17 | €411,50 | €0,00 | €56,54 |
| Rapida V3 senza ESPORTS — MFE Lock | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,60192 | 1220,60192 | 1206,93118 | 819,83762 | 1241,10803 | €37,83 | €113,48 | €1,27 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,51 | €73,52 | €0,82 | €0,28 |
| Rapida V3 — qualità completa + profit lock | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 9,38563 | 9,38563 | 9,22869 | 6,30401 | 9,62103 | €949,50 | €2.848,50 | €47,63 | €0,00 |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1897,77000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €18,22 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 59,07000 | 58,25395 | 39,57042 | 59,90353 | €33,51 | €100,52 | €1,13 | €0,27 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 0,99724 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €21,77 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63492,10000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €-0,17 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,07001 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,47 |
| Ampia 4H | BTW | LONG | Confluenza trend | 240m | 2,0x | 0,32695 | 0,33478 | 0,28771 | 0,16511 | 0,43680 | €207,21 | €414,42 | €49,73 | €9,93 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1189,34318 | 1189,34318 | 1197,37127 | 600,61830 | 1247,25345 | €79,48 | €158,95 | €0,00 | €0,00 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,03281 | 0,03281 | 0,03675 | 0,04906 | 0,02415 | €186,76 | €373,52 | €44,82 | €-0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37290 | 0,28527 | 0,32903 | 0,55748 | 0,27445 | €166,87 | €333,74 | €0,00 | €78,43 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €48,73 | €97,46 | €1,75 | €0,06 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,49 | €-0,02 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1182,39901 | 1196,37701 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €0,00 | €0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02493 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,37290 | 0,28527 | 0,32903 | 0,55748 | 0,27445 | €197,18 | €394,37 | €0,00 | €92,67 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €0,00 | €108,50 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07001 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-23,61 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 59,28285 | 59,07000 | 58,33433 | 29,93784 | 61,65417 | €1.599,80 | €3.199,61 | €51,19 | €-11,49 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €0,00 | €105,95 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07001 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-23,06 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 59,28285 | 59,07000 | 58,33433 | 29,93784 | 61,65417 | €1.562,14 | €3.124,27 | €49,99 | €-11,22 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,12104 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €45,92 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €0,00 | €87,26 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07001 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,08 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1175,20470 | 1195,76393 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 62898,88771 | 63492,10000 | 63905,26991 | 94033,83712 | 60684,84686 | €27,47 | €54,94 | €0,88 | €-0,52 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 0,99724 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €0,13 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 74,94501 | 75,29200 | 76,14413 | 112,04279 | 72,30694 | €1.248,89 | €2.497,78 | €39,96 | €-11,56 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 59,17783 | 59,07000 | 58,23099 | 29,88481 | 61,26089 | €74,07 | €148,13 | €2,37 | €-0,27 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 509,54189 | 509,44000 | 500,05173 | 257,31865 | 530,42024 | €1.232,23 | €2.464,45 | €45,90 | €-0,49 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1189,34318 | 1189,34318 | 1198,87118 | 600,61830 | 1241,98888 | €1.146,19 | €2.292,38 | €0,00 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.703,71 | €3.407,43 | €49,07 | €1,80 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 510,90216 | 509,44000 | 502,14178 | 258,00559 | 528,42292 | €65,48 | €130,96 | €2,25 | €-0,37 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €0,52 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €200,12 | €400,25 | €48,03 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,07001 | 0,07049 | 0,10388 | 0,06749 | €69,53 | €139,06 | €2,00 | €-1,04 |
| Scanner Bottom 5 Short 1H | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €204,10 | €408,20 | €48,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,28527 | 0,32611 | 0,55748 | 0,28340 | €203,89 | €407,78 | €0,00 | €95,82 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63492,10000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,05 | €90,11 | €1,30 | €-0,68 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,00 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €1,66 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 510,90216 | 509,44000 | 502,14178 | 258,00559 | 528,42292 | €1.361,74 | €2.723,49 | €46,70 | €-7,79 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,53 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,16396 | 75,29200 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,06 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06949 | 0,07001 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,89 |
| Scanner Bottom10 Short | ACE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,37290 | 0,28527 | 0,32611 | 0,55748 | 0,28340 | €207,19 | €414,39 | €0,00 | €97,38 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63018,79372 | 63492,10000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,45 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,00 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €1,66 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 510,90216 | 509,44000 | 502,14178 | 258,00559 | 528,42292 | €1.361,74 | €2.723,49 | €46,70 | €-7,79 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,53 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,16396 | 75,29200 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,06 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06949 | 0,07001 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,89 |
| Scanner Bottom15 Short | ACE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,37290 | 0,28527 | 0,32611 | 0,55748 | 0,28340 | €207,19 | €414,39 | €0,00 | €97,38 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63018,79372 | 63492,10000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,45 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,00 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €1,66 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 510,90216 | 509,44000 | 502,14178 | 258,00559 | 528,42292 | €1.361,74 | €2.723,49 | €46,70 | €-7,79 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,53 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €203,35 | €406,71 | €48,80 | €-0,00 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,16396 | 75,29200 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,06 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06949 | 0,07001 | 0,07049 | 0,10388 | 0,06749 | €58,96 | €117,92 | €1,70 | €-0,89 |
| Scanner Bottom20 Short | ACE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €207,40 | €414,80 | €49,78 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,37290 | 0,28527 | 0,32611 | 0,55748 | 0,28340 | €207,19 | €414,39 | €0,00 | €97,38 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63018,79372 | 63492,10000 | 63926,26435 | 94213,09661 | 61203,85246 | €29,72 | €59,44 | €0,86 | €-0,45 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,00 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.334,44 | €2.668,88 | €47,82 | €1,51 |
| Top 5 + BTC — solo MFE | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,00 | €0,00 |
| Top 5 + BTC — solo MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.250,84 | €2.501,69 | €44,82 | €1,42 |
| Top 5 + BTC — Guard | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €0,00 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Top 5 + BTC — Guard | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,07000 | 58,06542 | 29,75146 | 60,78017 | €1.519,74 | €3.039,48 | €43,77 | €8,06 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.266,16 | €2.532,33 | €45,37 | €1,43 |
| Top 5 + BTC — BTC≤3 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,00 | €0,00 |
| Top 5 + BTC — BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.275,19 | €2.550,38 | €45,69 | €1,44 |
| Top 5 + BTC — Guard + MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €0,00 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,07000 | 58,06542 | 29,75146 | 60,78017 | €1.484,39 | €2.968,79 | €42,75 | €7,87 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.236,72 | €2.473,43 | €44,31 | €1,40 |
| Top 5 + BTC — Guard + BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €0,00 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,07000 | 58,06542 | 29,75146 | 60,78017 | €1.538,41 | €3.076,82 | €44,31 | €8,16 |
| Top 5 + BTC — Guard + BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.281,72 | €2.563,44 | €45,93 | €1,45 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €0,00 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,07000 | 58,06542 | 29,75146 | 60,78017 | €1.512,01 | €3.024,03 | €43,55 | €8,02 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.259,73 | €2.519,45 | €45,14 | €1,43 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,00 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1698,82000 | 1682,47471 | 825,72069 | 1810,18864 | €12,84 | €25,67 | €0,00 | €1,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 536,51792 | €1.288,99 | €2.577,98 | €46,19 | €1,46 |
| Top 5 + BTC — target pieno 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1182,39901 | 1197,94321 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,00 | €0,00 |
| Top 5 + BTC — target pieno 3R | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1635,09047 | 1698,82000 | 1682,47471 | 825,72069 | 1810,18864 | €12,84 | €25,69 | €0,00 | €1,00 |
| Top 5 + BTC — target pieno 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 536,51792 | €1.289,74 | €2.579,49 | €46,21 | €1,46 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07001 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €5,43 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07001 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,10 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1175,20470 | 1195,76393 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,00 | €0,00 |
| Combo Trend | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02351 | €194,61 | €389,21 | €46,71 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,37290 | 0,28527 | 0,32903 | 0,55748 | 0,27445 | €193,08 | €386,15 | €0,00 | €90,74 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 58,85077 | 59,07000 | 57,90916 | 29,71964 | 60,92231 | €1.350,47 | €2.700,94 | €43,22 | €10,06 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 510,90216 | 509,44000 | 501,16840 | 258,00559 | 532,31642 | €21,03 | €42,06 | €0,80 | €-0,12 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €118,87 | €237,73 | €3,80 | €-0,14 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,28834 | 0,28527 | 0,25374 | 0,14561 | 0,34370 | €204,24 | €408,49 | €49,02 | €-4,35 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,07001 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €-4,82 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1189,34318 | 1189,34318 | 1198,87118 | 600,61830 | 1247,25345 | €1.034,30 | €2.068,59 | €0,00 | €0,00 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 529,22029 | €1.243,73 | €2.487,45 | €44,57 | €1,41 |
| Combo Adaptive — madre | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07001 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,11 |
| Combo Adaptive — madre | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1198,84431 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,00 | €0,00 |
| Combo Adaptive — madre | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1698,82000 | 1685,26109 | 819,70758 | 1740,74186 | €686,66 | €1.373,32 | €0,00 | €63,99 |
| Combo Adaptive — madre | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,28527 | 0,32320 | 0,55748 | 0,28340 | €194,92 | €389,84 | €0,00 | €91,61 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 527,39588 | €85,87 | €171,74 | €3,08 | €0,10 |
| Combo Adaptive — MFE Trail esistente | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1189,34318 | 1189,34318 | 1200,37110 | 600,61830 | 1241,98888 | €15,03 | €30,05 | €0,00 | €0,00 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,07001 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,15 |
| Combo Adaptive — MFE Trail esistente | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 527,39588 | €48,08 | €96,16 | €1,72 | €0,05 |
| Combo Adaptive — MFE Trail esistente | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,28510 | 0,28527 | 0,31931 | 0,42622 | 0,21668 | €185,29 | €370,59 | €44,47 | €-0,22 |
| Combo Adaptive — Quality7 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1175,20470 | 1198,97807 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €0,00 | €0,00 |
| Combo Adaptive — Quality7 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03387 | 0,03387 | 0,03794 | 0,05064 | 0,02574 | €203,75 | €407,50 | €48,90 | €-0,00 |
| Combo Adaptive — Quality7 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,28527 | 0,32320 | 0,55748 | 0,28340 | €182,81 | €365,62 | €0,00 | €85,92 |
| Combo Adaptive — Trend/Transition | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive — Quality7 + Regime | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive — Long Only | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1182,39901 | 1199,50940 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,00 | €0,00 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.675,98 | €3.351,96 | €48,27 | €1,77 |
| Combo Adaptive — Long Only | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 527,39588 | €1.347,79 | €2.695,58 | €48,29 | €1,53 |
| Combo Adaptive — parziale 1R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07001 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,11 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1198,84431 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,00 | €0,00 |
| Combo Adaptive — parziale 1R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1623,18333 | 1698,82000 | 1685,26109 | 819,70758 | 1740,74186 | €659,36 | €1.318,73 | €0,00 | €61,45 |
| Combo Adaptive — parziale 1R | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,28527 | 0,32320 | 0,55748 | 0,28340 | €187,17 | €374,34 | €0,00 | €87,97 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 527,39588 | €82,46 | €164,92 | €2,95 | €0,09 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €0,00 | €92,98 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07001 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,11 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1198,84431 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,00 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1698,82000 | 1685,90652 | 825,72069 | 1810,18864 | €17,35 | €34,70 | €0,00 | €1,35 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €204,60 | €409,21 | €49,10 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,28527 | 0,32320 | 0,55748 | 0,23865 | €183,50 | €367,00 | €0,00 | €86,24 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 536,51792 | €135,42 | €270,84 | €4,85 | €0,15 |
| Combo Adaptive — target pieno 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive — target pieno 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €0,00 | €91,25 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07001 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,11 |
| Combo Adaptive — target pieno 3R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1167,82027 | 1198,84431 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,00 | €0,00 |
| Combo Adaptive — target pieno 3R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1635,09047 | 1698,82000 | 1685,90652 | 825,72069 | 1810,18864 | €17,03 | €34,05 | €0,00 | €1,33 |
| Combo Adaptive — target pieno 3R | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02044 | €200,78 | €401,56 | €48,19 | €-0,00 |
| Combo Adaptive — target pieno 3R | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,37290 | 0,28527 | 0,32320 | 0,55748 | 0,23865 | €180,07 | €360,14 | €0,00 | €84,63 |
| Combo Adaptive — target pieno 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 509,15181 | 509,44000 | 500,02977 | 257,12166 | 536,51792 | €132,89 | €265,78 | €4,76 | €0,15 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63492,10000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €8,33 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63492,10000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €2,31 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 74,57408 | 75,29200 | 76,05188 | 111,48825 | 70,87959 | €1.259,31 | €2.518,63 | €49,91 | €-24,25 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,07001 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €6,23 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,93 | €73,85 | €1,65 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1698,82000 | 1576,72439 | 825,72069 | 1751,82260 | €626,90 | €1.253,80 | €44,76 | €48,87 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1897,77000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €-0,25 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €-0,41 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1182,39901 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €0,00 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1897,77000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,16 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.637,93 | €3.275,87 | €47,17 | €1,73 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €-0,42 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1167,82027 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1655,75286 | 1698,82000 | 1602,89078 | 836,15519 | 1761,47701 | €734,74 | €1.469,49 | €46,92 | €38,22 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,07000 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €7,53 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1189,34318 | 1189,34318 | 1163,02033 | 600,61830 | 1241,98888 | €1.101,72 | €2.203,44 | €48,77 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1897,77000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €-0,08 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 59,07000 | 58,18865 | 29,81460 | 60,73912 | €1.636,69 | €3.273,37 | €47,14 | €1,73 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €36,43 | €72,87 | €1,62 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1698,82000 | 1576,72439 | 825,72069 | 1751,82260 | €618,57 | €1.237,14 | €44,16 | €48,22 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1897,77000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €-0,25 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €-0,41 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1165,32878 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,00 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1632,05865 | 1698,82000 | 1586,54904 | 824,18962 | 1768,58749 | €850,90 | €1.701,80 | €47,45 | €69,61 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,07000 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €7,83 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €-0,41 |
| Combo Adaptive — Side × Regime Guard | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive — Side × Regime Guard | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,07001 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €-4,94 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €24,08 |
| Combo Adaptive — Side × Regime Guard | ACE | SHORT | Combo Adaptive | 60m | 2,0x | 0,15317 | 0,15317 | 0,15317 | 0,22899 | 0,11641 | €207,74 | €415,49 | €0,00 | €-0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,11 | €74,22 | €1,65 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1698,82000 | 1576,72439 | 825,72069 | 1751,82260 | €630,00 | €1.260,01 | €44,98 | €49,11 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1897,77000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €-0,25 |
| Master Adaptive GB20 — Breakeven 0,5R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €-0,41 |
| Master Adaptive GB20 — 50% a 0,75R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1193,28554 | 1193,28554 | 1166,68449 | 602,60920 | 1246,48765 | €37,07 | €74,14 | €1,65 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1635,09047 | 1698,82000 | 1576,72439 | 825,72069 | 1751,82260 | €629,33 | €1.258,67 | €44,93 | €49,06 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1897,77000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €-0,25 |
| Master Adaptive GB20 — 50% a 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €-0,41 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1897,77000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €-9,61 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 63492,10000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €-0,46 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03387 | 0,03387 | 0,03794 | 0,04499 | 0,02778 | €143,50 | €430,49 | €51,66 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ACE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €143,19 | €429,58 | €0,00 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1902,79048 | 1897,77000 | 1881,47923 | 1278,04094 | 1934,75736 | €1.508,82 | €4.526,45 | €50,70 | €-11,94 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99724 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €29,34 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63492,10000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €-4,43 |
| MAIN — Side × Regime Guard | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €1,95 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 59,42488 | 59,07000 | 57,77054 | 39,91371 | 62,73356 | €20,16 | €60,47 | €1,68 | €-0,36 |
| Combo Trend — Side × Regime Guard | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07001 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-15,52 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 0,99724 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €22,48 |
| Combo Trend — Side × Regime Guard | ACE | SHORT | Combo Trend | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,09934 | €214,51 | €429,02 | €51,48 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTC | SHORT | Combo Trend | 60m | 2,0x | 62834,55058 | 63492,10000 | 63839,90339 | 93937,65311 | 60622,77440 | €105,21 | €210,42 | €3,37 | €-2,20 |
| FAST NoHigh <7,5 · SHORT only | EDEN | LONG | Momentum / breakout | 60m | 3,0x | 0,05927 | 0,05927 | 0,05215 | 0,03981 | 0,06993 | €136,56 | €409,67 | €49,16 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | ACE | SHORT | Momentum / breakout | 60m | 3,0x | 0,15317 | 0,15317 | 0,15317 | 0,20346 | 0,12560 | €135,49 | €406,48 | €0,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €0,00 |
| Bilanciata V3 · LONG only | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07001 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,22 |
| Bilanciata V3 · LONG only | SNDK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1635,09047 | 1698,82000 | 1682,47471 | 1098,23576 | 1751,82258 | €432,90 | €1.298,70 | €0,00 | €50,62 |
| Bilanciata V3 · LONG only | TUT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03149 | 0,03149 | 0,03527 | 0,04183 | 0,02393 | €120,86 | €362,58 | €43,51 | €-0,00 |
| Bilanciata V3 · LONG only | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99724 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €0,25 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 62892,88891 | 63492,10000 | 63798,54651 | 83542,72076 | 61081,57371 | €37,97 | €113,91 | €1,64 | €-1,09 |
| Bilanciata V3 · LONG only | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,36815 | 0,28527 | 0,31949 | 0,48902 | 0,27979 | €126,96 | €380,87 | €0,00 | €85,74 |
| Bilanciata V3 · LONG only | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.101,68 | €3.305,04 | €47,59 | €-1,98 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €0,52 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,68 | €403,35 | €48,40 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,07001 | 0,07049 | 0,10388 | 0,06749 | €70,07 | €140,14 | €2,02 | €-1,05 |
| Scanner Bottom5 Short Profit Lock V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €205,68 | €411,36 | €49,36 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,28527 | 0,32611 | 0,55748 | 0,28340 | €205,47 | €410,94 | €0,00 | €96,57 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63492,10000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,40 | €90,81 | €1,31 | €-0,68 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 0,99724 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €0,52 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03194 | 0,03194 | 0,03577 | 0,04775 | 0,02428 | €201,98 | €403,97 | €48,48 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06949 | 0,07001 | 0,07049 | 0,10388 | 0,06749 | €70,18 | €140,35 | €2,02 | €-1,05 |
| Scanner Bottom5 Short Mfe Trail V1 | ACE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,13497 | 0,13497 | 0,15117 | 0,20178 | 0,10258 | €205,99 | €411,99 | €49,44 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37290 | 0,28527 | 0,32611 | 0,55748 | 0,28340 | €205,79 | €411,57 | €0,00 | €96,71 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63018,79372 | 63492,10000 | 63926,26435 | 94213,09661 | 61203,85246 | €45,47 | €90,94 | €1,31 | €-0,68 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom5 Short Mfe Trail V1 | H | SHORT | 2026-08-17T13:06:22+00:00 | 0,12263 | €-6,14 | -1,28 | STOP_GAP_STRESS |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | 2026-08-17T13:06:22+00:00 | 0,00000 | €84,92 | 1,90 | TARGET |
| Scanner Bottom5 Short Profit Lock V1 | H | SHORT | 2026-08-17T13:06:22+00:00 | 0,12263 | €-6,13 | -1,28 | STOP_GAP_STRESS |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | 2026-08-17T13:06:22+00:00 | 0,00000 | €84,79 | 1,90 | TARGET |
| Bilanciata V3 · LONG only | H | SHORT | 2026-08-17T13:06:22+00:00 | 0,12263 | €-4,44 | -1,28 | STOP_GAP_STRESS |
| Bilanciata V3 · LONG only | HYPE | LONG | 2026-08-17T13:06:22+00:00 | 58,81049 | €-9,62 | -0,21 | STOP_GAP_STRESS |
| FAST NoHigh <7,5 · SHORT only | HYPE | LONG | 2026-08-17T13:06:22+00:00 | 58,81049 | €-0,34 | -0,27 | STOP_GAP_STRESS |
| Rapida V3 NoHigh — Regime Guard | HYPE | LONG | 2026-08-17T13:06:22+00:00 | 58,81049 | €-13,64 | -0,27 | STOP_GAP_STRESS |
| Rapida V3 NoHigh — Range Only | HYPE | LONG | 2026-08-17T13:06:22+00:00 | 58,81049 | €-23,41 | -0,45 | STOP_GAP_STRESS |
| Combo Adaptive — target pieno 3R | H | SHORT | 2026-08-17T13:06:22+00:00 | 0,12362 | €-51,04 | -1,08 | STOP_STRESS_SLIPPAGE |
| Combo Adaptive — target pieno 3R | HYPE | LONG | 2026-08-17T13:06:22+00:00 | 58,81049 | €0,65 | 1,59 | STOP_GAP_STRESS |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | H | SHORT | 2026-08-17T13:06:22+00:00 | 0,12362 | €-52,01 | -1,08 | STOP_STRESS_SLIPPAGE |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 373/30 | 33/30 | 0,67 | 2,04 | -0,17R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 341/30 | 20/30 | 0,59 | 1,90 | -0,22R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 213/30 | 22/30 | 0,78 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 215/30 | 22/30 | 0,75 | 1,57 | -0,13R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 289/30 | 31/30 | 0,77 | 0,62 | -0,12R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 259/30 | 11/30 | 0,68 | 0,00 | -0,16R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 121/30 | 8/30 | 0,67 | 1,02 | -0,17R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 276/30 | 17/30 | 0,59 | 4,50 | -0,23R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 418/30 | 24/30 | 0,68 | 0,64 | -0,17R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 382/30 | 7/30 | 0,59 | 0,02 | -0,22R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 289/30 | 30/30 | 0,81 | 1,02 | -0,10R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 529/30 | 55/30 | 0,81 | 1,12 | -0,09R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 121/30 | 15/30 | 0,42 | 0,99 | -0,39R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 471/30 | 44/30 | 0,68 | 1,20 | -0,17R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 475/30 | 37/30 | 0,68 | 0,76 | -0,17R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 435/30 | 23/30 | 0,59 | 1,12 | -0,22R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 268/30 | 41/30 | 0,72 | 0,72 | -0,17R | €-9,22 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 22/30 | 0,00 | 2,08 | 0,00R | €21,27 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 643/30 | 104/30 | 0,88 | 0,86 | -0,07R | €-2,66 | 8,81% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 46/30 | 0,00 | 0,60 | 0,00R | €-13,49 | 9,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 10/30 | 0,00 | 1,56 | 0,00R | €10,74 | 1,80% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 223/30 | 62/30 | 1,04 | 0,81 | 0,02R | €-4,51 | 6,62% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 403/30 | 94/30 | 0,91 | 0,96 | -0,05R | €-0,83 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 324/30 | 50/30 | 0,80 | 0,44 | -0,11R | €-12,31 | 6,83% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 172/30 | 29/30 | 0,95 | 1,05 | -0,02R | €1,12 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 433/30 | 76/30 | 0,80 | 1,03 | -0,10R | €0,54 | 6,52% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 500/30 | 112/30 | 0,84 | 1,13 | -0,08R | €2,65 | 6,52% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 657/30 | 119/30 | 0,76 | 1,16 | -0,13R | €2,81 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 70/30 | 0,00 | 1,46 | 0,00R | €9,51 | 3,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 80/30 | 0,00 | 1,09 | 0,00R | €2,16 | 5,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 33/30 | 0,00 | 1,41 | 0,00R | €10,59 | 2,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 388/30 | 122/30 | 0,81 | 1,17 | -0,10R | €3,68 | 4,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 620/30 | 135/30 | 0,72 | 0,93 | -0,15R | €-1,52 | 3,95% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 49/30 | 28/30 | 0,59 | 0,80 | -0,24R | €-5,20 | 3,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 633/30 | 143/30 | 0,79 | 0,92 | -0,11R | €-1,72 | 7,14% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 459/30 | 113/30 | 0,78 | 1,07 | -0,12R | €1,49 | 6,72% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 254/30 | 75/30 | 0,92 | 0,75 | -0,04R | €-7,52 | 6,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 257/30 | 71/30 | 0,88 | 0,81 | -0,06R | €-5,18 | 5,23% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 350/30 | 86/30 | 0,84 | 0,65 | -0,08R | €-9,06 | 10,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 34/30 | 0,00 | 1,47 | 0,00R | €9,77 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 54/30 | 0,00 | 1,23 | 0,00R | €4,72 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 528/30 | 103/30 | 0,76 | 0,87 | -0,13R | €-3,21 | 6,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 66/30 | 0,00 | 0,80 | 0,00R | €-4,77 | 8,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 99/30 | 0,00 | 0,90 | 0,00R | €-1,83 | 7,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 38/30 | 0,00 | 0,80 | 0,00R | €-4,96 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 586/30 | 117/30 | 0,74 | 0,80 | -0,14R | €-4,39 | 7,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 249/30 | 37/30 | 0,72 | 0,95 | -0,19R | €-1,26 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 181/30 | 73/30 | 1,13 | 0,78 | 0,06R | €-5,96 | 6,53% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 11/30 | 5/30 | 0,57 | 0,89 | -0,22R | €-2,34 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 14/30 | 7/30 | 0,22 | 0,84 | -0,63R | €-3,75 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 4/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 15/30 | 9/30 | 0,78 | 0,53 | -0,13R | €-16,82 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,23% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 517/30 | 75/30 | 0,97 | 0,87 | -0,02R | €-2,52 | 5,40% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 282/30 | 45/30 | 0,98 | 0,71 | -0,01R | €-7,65 | 5,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 551/30 | 89/30 | 0,97 | 0,47 | -0,01R | €-12,42 | 11,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 458/30 | 76/30 | 0,92 | 0,63 | -0,04R | €-7,62 | 6,20% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 62/30 | 22/30 | 1,22 | 0,63 | 0,10R | €-12,83 | 4,21% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 62/30 | 22/30 | 1,15 | 0,48 | 0,07R | €-18,39 | 5,41% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 149/30 | 41/30 | 0,88 | 0,63 | -0,06R | €-9,55 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 189/30 | 32/30 | 0,86 | 0,75 | -0,07R | €-6,02 | 3,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 78/30 | 0,74 | 0,69 | -0,20R | €-6,29 | 6,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 55/30 | 0,00 | 0,97 | 0,00R | €-0,54 | 6,65% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 59/30 | 0,74 | 0,50 | -0,20R | €-11,33 | 6,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 87/30 | 33/30 | 1,26 | 0,79 | 0,11R | €-6,67 | 5,09% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 320/30 | 70/30 | 1,08 | 0,56 | 0,04R | €-13,36 | 11,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 425/30 | 103/30 | 0,91 | 0,81 | -0,05R | €-4,85 | 9,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 45/30 | 0,00 | 1,36 | 0,00R | €6,24 | 2,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 12/30 | 10/30 | 0,51 | 0,62 | -0,36R | €-10,55 | 2,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 18/30 | 12/30 | 0,40 | 0,94 | -0,41R | €-1,28 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 205/30 | 63/30 | 0,82 | 1,44 | -0,12R | €10,43 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 135/30 | 31/30 | 0,78 | 1,64 | -0,13R | €13,11 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 428/30 | 70/30 | 0,89 | 0,57 | -0,06R | €-10,65 | 9,01% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 14/30 | 8/30 | 0,30 | 0,05 | -0,56R | €-38,45 | 3,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 13/30 | 7/30 | 0,28 | 0,28 | -0,63R | €-33,90 | 2,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 20/30 | 11/30 | 0,29 | 0,11 | -0,55R | €-41,03 | 4,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 12/30 | 15/30 | 0,89 | 0,35 | -0,07R | €-21,51 | 3,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 261/30 | 49/30 | 1,01 | 0,62 | 0,01R | €-13,04 | 6,90% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 44/30 | 0,00 | 0,55 | 0,00R | €-14,10 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 33/30 | 0,00 | 0,37 | 0,00R | €-26,44 | 11,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 39/30 | 0,00 | 0,53 | 0,00R | €-16,16 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 486/30 | 76/30 | 1,39 | 0,53 | 0,13R | €-10,40 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 229/30 | 46/30 | 1,03 | 0,67 | 0,02R | €-12,21 | 6,80% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 238/30 | 40/30 | 0,99 | 0,50 | -0,01R | €-19,53 | 8,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 165/30 | 45/30 | 1,02 | 0,48 | 0,01R | €-24,32 | 11,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 251/30 | 41/30 | 0,98 | 0,56 | -0,01R | €-16,26 | 7,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 539/30 | 85/30 | 0,85 | 0,64 | -0,09R | €-8,48 | 9,65% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 215/30 | 70/30 | 1,14 | 0,91 | 0,07R | €-2,71 | 8,11% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 192/30 | 54/30 | 0,49 | 1,03 | -0,29R | €0,59 | 5,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 192/30 | 54/30 | 0,49 | 1,03 | -0,29R | €0,59 | 5,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 192/30 | 54/30 | 0,49 | 1,03 | -0,29R | €0,59 | 5,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 224/30 | 74/30 | 0,69 | 0,91 | -0,17R | €-1,74 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 226/30 | 46/30 | 0,75 | 0,96 | -0,12R | €-0,81 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 203/30 | 47/30 | 0,66 | 0,94 | -0,16R | €-1,11 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 261/30 | 45/30 | 1,00 | 0,53 | -0,00R | €-15,04 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 262/30 | 45/30 | 0,99 | 0,53 | -0,00R | €-15,04 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 262/30 | 45/30 | 0,99 | 0,53 | -0,00R | €-15,04 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 308/30 | 65/30 | 1,09 | 0,74 | 0,05R | €-7,02 | 10,37% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 125/30 | 10/30 | 0,87 | 0,87 | -0,07R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 261/30 | 46/30 | 0,94 | 0,41 | -0,03R | €-19,13 | 10,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 275/30 | 60/30 | 1,17 | 0,64 | 0,07R | €-10,89 | 7,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 230/30 | 45/30 | 1,04 | 0,69 | 0,02R | €-10,90 | 7,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 286/30 | 67/30 | 1,18 | 0,59 | 0,08R | €-12,30 | 8,78% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 238/30 | 50/30 | 1,05 | 0,64 | 0,02R | €-12,11 | 7,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 326/30 | 58/30 | 1,07 | 0,34 | 0,03R | €-18,18 | 11,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 257/30 | 53/30 | 0,99 | 0,52 | -0,01R | €-14,76 | 11,00% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 243/30 | 49/30 | 0,99 | 0,52 | -0,00R | €-15,86 | 10,71% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 339/30 | 73/30 | 1,11 | 1,01 | 0,06R | €0,34 | 8,85% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 21/30 | 10/30 | 0,36 | 0,15 | -0,54R | €-37,89 | 4,47% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 2/30 | 2/30 | 1,18 | 0,65 | 0,10R | €-8,96 | 0,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 12/30 | 6/30 | 0,81 | 1,24 | -0,11R | €6,55 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 15/30 | 8/30 | 0,55 | 0,49 | -0,34R | €-15,55 | 2,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 3/30 | 3/30 | 0,63 | 0,35 | -0,26R | €-22,94 | 0,87% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 19/30 | 9/30 | 0,51 | 0,37 | -0,40R | €-26,61 | 3,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 4/30 | 4/30 | 0,00 | 0,00 | -1,06R | €-51,82 | 2,10% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07001**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.5 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63492.1 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation, volume_valid**
- High **0.07007**; close **0.07005**; wick alta **28.6%**; volume **x2.43**

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

- Regime: **RANGE_HIGH_VOL**
- Famiglia: **RANGE**
- Confidenza: **79,60%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC -1.0, breadth EMA50 67%, ADX 23.5.
- BTC trend score: **-1,00**; ADX: **23,48**; breadth sopra EMA50: **66,67%**
- Mediana alt vs BTC: **-0,54%**; dispersione: **10,60%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **79**
- Posizioni research aperte: **598**
- Trade research chiusi: **25202**
- Eventi di mercato indipendenti chiusi: **3495**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **65258**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 11 | 373 | 373 | 29,76% | 0,67 | -0,17R | €-641,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 11 | 341 | 341 | 28,74% | 0,59 | -0,22R | €-742,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 4 | 213 | 213 | 46,01% | 0,78 | -0,12R | €-253,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 4 | 215 | 215 | 32,09% | 0,75 | -0,13R | €-277,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 5 | 289 | 289 | 31,83% | 0,77 | -0,12R | €-345,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 5 | 259 | 259 | 31,66% | 0,68 | -0,16R | €-422,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 121 | 121 | 33,88% | 0,67 | -0,17R | €-207,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 1 | 276 | 276 | 26,81% | 0,59 | -0,23R | €-642,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 8 | 418 | 418 | 29,19% | 0,68 | -0,17R | €-711,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 8 | 382 | 382 | 28,01% | 0,59 | -0,22R | €-832,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 5 | 289 | 289 | 32,53% | 0,81 | -0,10R | €-285,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 9 | 529 | 529 | 39,51% | 0,81 | -0,09R | €-474,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 121 | 121 | 28,10% | 0,42 | -0,39R | €-469,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 10 | 471 | 471 | 28,87% | 0,68 | -0,17R | €-797,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 10 | 475 | 475 | 28,84% | 0,68 | -0,17R | €-798,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 10 | 435 | 435 | 27,59% | 0,59 | -0,22R | €-941,44 |
| MAIN | 19 | 268 | 268 | 25,75% | 0,72 | -0,17R | €-463,53 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 13 | 643 | 643 | 33,13% | 0,88 | -0,07R | €-422,11 |
| Bilanciata 1H V2 | 6 | 256 | 223 | 37,11% | 1,04 | 0,02R | €58,08 |
| Bilanciata 1H V3 Filtered | 9 | 403 | 403 | 34,24% | 0,91 | -0,05R | €-195,07 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 9 | 324 | 324 | 33,02% | 0,80 | -0,11R | €-340,41 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 172 | 172 | 37,79% | 0,95 | -0,02R | €-41,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 8 | 433 | 433 | 34,64% | 0,80 | -0,10R | €-437,46 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 8 | 500 | 500 | 35,80% | 0,84 | -0,08R | €-403,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 10 | 657 | 657 | 33,49% | 0,76 | -0,13R | €-836,03 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 7 | 388 | 388 | 35,05% | 0,81 | -0,10R | €-381,24 |
| SHADOW_1H_FAST_TP2_V1 | 11 | 620 | 620 | 30,32% | 0,72 | -0,15R | €-936,56 |
| Rapida 1H V2 | 0 | 57 | 49 | 36,84% | 0,59 | -0,24R | €-135,15 |
| Rapida 1H V3 Filtered | 10 | 633 | 633 | 34,12% | 0,79 | -0,11R | €-721,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 10 | 459 | 459 | 34,42% | 0,78 | -0,12R | €-534,48 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 4 | 254 | 254 | 47,64% | 0,92 | -0,04R | €-112,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 4 | 257 | 257 | 36,96% | 0,88 | -0,06R | €-153,39 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 5 | 350 | 350 | 36,29% | 0,84 | -0,08R | €-287,63 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 7 | 528 | 528 | 33,52% | 0,76 | -0,13R | €-668,31 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 10 | 586 | 586 | 33,11% | 0,74 | -0,14R | €-803,87 |
| SHADOW_4H_WIDE | 31 | 249 | 249 | 20,48% | 0,72 | -0,19R | €-475,61 |
| SHADOW_BOLLINGER_MR_1H | 2 | 181 | 181 | 48,62% | 1,13 | 0,06R | €109,76 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 11 | 11 | 54,55% | 0,57 | -0,22R | €-23,77 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 14 | 14 | 28,57% | 0,22 | -0,63R | €-88,00 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,93 |
| SHADOW_BTC_EMA_1H | 0 | 15 | 15 | 46,67% | 0,78 | -0,13R | €-19,79 |
| SHADOW_BTC_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 12 | 517 | 517 | 36,56% | 0,97 | -0,02R | €-78,72 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 282 | 282 | 36,17% | 0,98 | -0,01R | €-29,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 11 | 551 | 551 | 40,83% | 0,97 | -0,01R | €-72,21 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 12 | 458 | 458 | 39,08% | 0,92 | -0,04R | €-179,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 62 | 62 | 45,16% | 1,22 | 0,10R | €61,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 62 | 62 | 37,10% | 1,15 | 0,07R | €43,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 149 | 149 | 31,54% | 0,88 | -0,06R | €-89,34 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 189 | 189 | 34,92% | 0,86 | -0,07R | €-129,79 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 87 | 87 | 50,57% | 1,26 | 0,11R | €100,02 |
| SHADOW_COMBO_SCANNER | 8 | 320 | 320 | 35,00% | 1,08 | 0,04R | €133,99 |
| SHADOW_COMBO_TREND | 16 | 425 | 425 | 31,29% | 0,91 | -0,05R | €-223,17 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 12 | 12 | 33,33% | 0,51 | -0,36R | €-43,62 |
| SHADOW_DOGE_EMA_1H | 0 | 18 | 18 | 27,78% | 0,40 | -0,41R | €-73,66 |
| SHADOW_DONCHIAN_1H | 6 | 205 | 205 | 29,27% | 0,82 | -0,12R | €-241,31 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 6 | 135 | 135 | 31,11% | 0,78 | -0,13R | €-176,23 |
| SHADOW_EMA_TREND_1H | 17 | 428 | 428 | 30,84% | 0,89 | -0,06R | €-272,62 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 14 | 14 | 28,57% | 0,30 | -0,56R | €-77,90 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 13 | 13 | 23,08% | 0,28 | -0,63R | €-81,36 |
| SHADOW_ETH_EMA_1H | 0 | 20 | 20 | 30,00% | 0,29 | -0,55R | €-110,17 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 1 | 12 | 12 | 41,67% | 0,89 | -0,07R | €-8,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 9 | 261 | 261 | 32,95% | 1,01 | 0,01R | €19,19 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 4 | 486 | 486 | 66,46% | 1,39 | 0,13R | €619,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 9 | 229 | 229 | 33,19% | 1,03 | 0,02R | €42,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 8 | 238 | 238 | 31,09% | 0,99 | -0,01R | €-19,56 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 165 | 165 | 33,33% | 1,02 | 0,01R | €23,37 |
| SHADOW_MASTER_ADAPTIVE_V1 | 9 | 251 | 251 | 32,27% | 0,98 | -0,01R | €-35,32 |
| Forza relativa 1H V1 | 17 | 539 | 539 | 28,76% | 0,85 | -0,09R | €-461,79 |
| Forza relativa 1H V2 | 8 | 230 | 215 | 35,65% | 1,14 | 0,07R | €170,11 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 8 | 192 | 192 | 26,04% | 0,49 | -0,29R | €-558,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 8 | 192 | 192 | 26,04% | 0,49 | -0,29R | €-558,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 8 | 192 | 192 | 26,04% | 0,49 | -0,29R | €-558,20 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 224 | 224 | 29,02% | 0,69 | -0,17R | €-384,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 10 | 226 | 226 | 51,77% | 0,75 | -0,12R | €-261,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 10 | 203 | 203 | 50,74% | 0,66 | -0,16R | €-317,83 |
| SHADOW_SCANNER_TOP10_LONG | 5 | 261 | 261 | 34,87% | 1,00 | -0,00R | €-0,43 |
| SHADOW_SCANNER_TOP15_LONG | 5 | 262 | 262 | 34,73% | 0,99 | -0,00R | €-11,54 |
| SHADOW_SCANNER_TOP20_LONG | 5 | 262 | 262 | 34,73% | 0,99 | -0,00R | €-11,54 |
| SHADOW_SCANNER_TOP5_BTC | 8 | 308 | 308 | 34,42% | 1,09 | 0,05R | €155,02 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 125 | 125 | 31,20% | 0,87 | -0,07R | €-91,35 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 8 | 261 | 261 | 32,57% | 0,94 | -0,03R | €-87,52 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 275 | 275 | 45,82% | 1,17 | 0,07R | €205,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 6 | 230 | 230 | 34,35% | 1,04 | 0,02R | €47,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 4 | 286 | 286 | 45,45% | 1,18 | 0,08R | €216,75 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 6 | 238 | 238 | 34,03% | 1,05 | 0,02R | €58,80 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 5 | 326 | 326 | 43,87% | 1,07 | 0,03R | €107,59 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 8 | 257 | 257 | 31,91% | 0,99 | -0,01R | €-20,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 8 | 243 | 243 | 31,28% | 0,99 | -0,00R | €-9,85 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 339 | 339 | 36,28% | 1,11 | 0,06R | €189,01 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 21 | 21 | 23,81% | 0,36 | -0,54R | €-113,90 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,93 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 12 | 12 | 50,00% | 0,81 | -0,11R | €-12,76 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 15 | 15 | 33,33% | 0,55 | -0,34R | €-50,34 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 3 | 3 | 33,33% | 0,63 | -0,26R | €-7,86 |
| SHADOW_SOL_EMA_1H | 0 | 19 | 19 | 26,32% | 0,51 | -0,40R | €-76,60 |
| SHADOW_SOL_EMA_4H | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,50 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 36 | 36 | 22,22% | 0,48 | -0,32R | €-116,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 53 | 53 | 41,51% | 1,26 | 0,13R | €66,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 110 | 110 | 33,64% | 0,63 | -0,19R | €-212,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 2 | 9 | 9 | 22,22% | 0,18 | -0,58R | €-52,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 4 | 51 | 51 | 31,37% | 0,89 | -0,05R | €-26,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 4 | 55 | 55 | 29,09% | 0,57 | -0,26R | €-141,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 52 | 52 | 17,31% | 0,47 | -0,26R | €-137,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 35 | 35 | 20,00% | 0,30 | -0,49R | €-170,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 40 | 40 | 42,50% | 1,39 | 0,18R | €70,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 1 | 103 | 103 | 33,01% | 0,52 | -0,25R | €-259,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 2 | 8 | 8 | 12,50% | 0,15 | -0,68R | €-54,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 4 | 50 | 50 | 32,00% | 1,00 | 0,00R | €0,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 4 | 51 | 51 | 27,45% | 0,54 | -0,27R | €-140,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 49 | 49 | 16,33% | 0,31 | -0,36R | €-177,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,78 | -0,12R | €-7,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 64 | 64 | 39,06% | 0,48 | -0,33R | €-208,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 3 | 30 | 30 | 56,67% | 1,03 | 0,02R | €4,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 1 | 29 | 29 | 44,83% | 0,70 | -0,17R | €-49,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 1,08 | 0,04R | €1,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-207,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 3 | 30 | 30 | 30,00% | 0,88 | -0,05R | €-15,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 1 | 29 | 29 | 31,03% | 0,68 | -0,20R | €-58,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 51 | 51 | 37,25% | 1,00 | -0,00R | €-0,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 79 | 79 | 34,18% | 0,62 | -0,21R | €-166,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 1 | 8 | 8 | 0,00% | 0,00 | -0,96R | €-76,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 3 | 41 | 41 | 34,15% | 1,17 | 0,07R | €29,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 1 | 39 | 39 | 33,33% | 0,79 | -0,12R | €-46,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,18 | -0,48R | €-43,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 43 | 43 | 37,21% | 1,03 | 0,01R | €5,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 69 | 69 | 36,23% | 0,56 | -0,23R | €-160,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 1 | 7 | 7 | 0,00% | 0,00 | -0,95R | €-66,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 3 | 40 | 40 | 35,00% | 1,26 | 0,10R | €41,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 1 | 36 | 36 | 30,56% | 0,58 | -0,24R | €-87,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 119 | 119 | 33,61% | 0,65 | -0,18R | €-217,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,73 | -0,16R | €-83,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 104 | 104 | 32,69% | 0,66 | -0,19R | €-193,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 1 | 32 | 32 | 21,88% | 0,69 | -0,15R | €-47,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,14 | -0,67R | €-161,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 135 | 135 | 33,33% | 0,65 | -0,19R | €-256,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 4 | 48 | 48 | 25,00% | 0,71 | -0,13R | €-63,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 3 | 75 | 75 | 29,33% | 0,64 | -0,19R | €-145,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 71 | 71 | 23,94% | 0,65 | -0,17R | €-119,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,09 | -0,71R | €-171,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 126 | 126 | 32,54% | 0,57 | -0,22R | €-281,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 4 | 47 | 47 | 25,53% | 0,71 | -0,13R | €-61,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 3 | 69 | 69 | 27,54% | 0,59 | -0,22R | €-153,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 66 | 66 | 22,73% | 0,47 | -0,27R | €-176,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 52 | 52 | 38,46% | 1,07 | 0,04R | €18,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 79 | 79 | 36,71% | 0,75 | -0,14R | €-107,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 1 | 8 | 8 | 0,00% | 0,00 | -0,96R | €-76,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 3 | 41 | 41 | 34,15% | 1,17 | 0,07R | €29,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 1 | 39 | 39 | 33,33% | 0,79 | -0,12R | €-46,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 0 | 53 | 53 | 32,08% | 0,42 | -0,35R | €-184,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 66 | 66 | 45,45% | 1,02 | 0,01R | €7,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 149 | 149 | 37,58% | 0,79 | -0,10R | €-145,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 3 | 20 | 20 | 30,00% | 0,40 | -0,42R | €-83,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 3 | 65 | 65 | 47,69% | 1,41 | 0,13R | €85,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 2 | 88 | 88 | 38,64% | 0,76 | -0,11R | €-94,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 81 | 81 | 40,74% | 0,84 | -0,07R | €-56,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 48 | 48 | 37,50% | 0,47 | -0,32R | €-151,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 1 | 4 | 4 | 50,00% | 0,92 | -0,05R | €-1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 0 | 60 | 60 | 35,00% | 0,99 | -0,01R | €-4,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 1 | 131 | 131 | 32,82% | 0,63 | -0,20R | €-261,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 2 | 20 | 20 | 20,00% | 0,29 | -0,49R | €-97,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 4 | 58 | 58 | 32,76% | 1,16 | 0,07R | €38,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 3 | 75 | 75 | 29,33% | 0,64 | -0,19R | €-145,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 1 | 132 | 132 | 32,58% | 0,62 | -0,21R | €-271,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 2 | 20 | 20 | 20,00% | 0,29 | -0,49R | €-97,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 4 | 58 | 58 | 32,76% | 1,16 | 0,07R | €38,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 3 | 75 | 75 | 29,33% | 0,64 | -0,19R | €-145,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,26 | -0,48R | €-230,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 1 | 124 | 124 | 31,45% | 0,50 | -0,27R | €-332,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 2 | 16 | 16 | 12,50% | 0,29 | -0,52R | €-83,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 4 | 57 | 57 | 33,33% | 1,25 | 0,10R | €57,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 3 | 69 | 69 | 27,54% | 0,59 | -0,22R | €-153,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 65 | 65 | 21,54% | 0,39 | -0,31R | €-201,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,89 | -0,05R | €-10,79 |
| MAIN | ALT_ROTATION_UP | 3 | 39 | 39 | 17,95% | 0,31 | -0,51R | €-196,95 |
| MAIN | RANGE | 1 | 73 | 73 | 21,92% | 0,64 | -0,23R | €-165,36 |
| MAIN | RANGE_HIGH_VOL | 3 | 12 | 12 | 25,00% | 0,71 | -0,15R | €-17,66 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 4 | 35 | 35 | 25,71% | 0,65 | -0,23R | €-79,75 |
| MAIN | TREND_DOWN | 6 | 41 | 41 | 26,83% | 0,78 | -0,13R | €-51,96 |
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
| Bilanciata 1H V1 | RANGE | 1 | 169 | 169 | 39,05% | 1,07 | 0,03R | €56,92 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 4 | 30 | 30 | 16,67% | 0,31 | -0,51R | €-152,78 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 4 | 92 | 92 | 39,13% | 1,25 | 0,12R | €114,94 |
| Bilanciata 1H V1 | TREND_DOWN | 4 | 83 | 83 | 31,33% | 0,72 | -0,15R | €-125,59 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 109 | 109 | 30,28% | 0,92 | -0,04R | €-40,50 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 58 | 49 | 37,93% | 1,12 | 0,06R | €34,42 |
| Bilanciata 1H V2 | RANGE | 2 | 121 | 109 | 34,71% | 0,81 | -0,11R | €-133,59 |
| Bilanciata 1H V2 | TRANSITION | 4 | 77 | 65 | 40,26% | 1,43 | 0,20R | €157,25 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 42 | 42 | 26,19% | 0,54 | -0,30R | €-128,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 45 | 45 | 31,11% | 1,08 | 0,05R | €21,32 |
| Bilanciata 1H V3 Filtered | RANGE | 1 | 116 | 116 | 40,52% | 1,08 | 0,04R | €43,95 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 10 | 10 | 20,00% | 0,35 | -0,48R | €-47,81 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 4 | 50 | 50 | 36,00% | 1,15 | 0,07R | €35,73 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 3 | 58 | 58 | 36,21% | 0,66 | -0,20R | €-113,88 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 62 | 62 | 30,65% | 1,06 | 0,03R | €18,24 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 19,35% | 0,26 | -0,52R | €-161,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 32,56% | 1,18 | 0,10R | €42,31 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 94 | 94 | 38,30% | 0,85 | -0,08R | €-72,21 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,49 | -0,34R | €-26,98 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 4 | 42 | 42 | 35,71% | 1,16 | 0,07R | €30,04 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 3 | 59 | 59 | 35,59% | 0,64 | -0,21R | €-124,99 |
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
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 143 | 143 | 34,97% | 0,78 | -0,12R | €-166,44 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 3 | 55 | 55 | 40,00% | 1,07 | 0,03R | €15,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 4 | 76 | 76 | 30,26% | 0,61 | -0,24R | €-179,09 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 73 | 73 | 27,40% | 0,74 | -0,12R | €-84,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 18,92% | 0,33 | -0,49R | €-181,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 173 | 173 | 39,31% | 0,98 | -0,01R | €-21,26 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 3 | 57 | 57 | 42,11% | 1,20 | 0,08R | €44,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 4 | 76 | 76 | 30,26% | 0,61 | -0,24R | €-179,09 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 89 | 89 | 26,97% | 0,65 | -0,18R | €-156,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 77 | 77 | 20,78% | 0,38 | -0,43R | €-330,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 72 | 72 | 38,89% | 0,87 | -0,07R | €-51,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 195 | 195 | 36,92% | 0,82 | -0,09R | €-184,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 3 | 22 | 22 | 36,36% | 0,80 | -0,12R | €-25,57 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 3 | 80 | 80 | 41,25% | 1,24 | 0,10R | €77,89 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 3 | 98 | 98 | 29,59% | 0,60 | -0,22R | €-219,46 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 104 | 104 | 27,88% | 0,70 | -0,15R | €-160,49 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 22,73% | 0,37 | -0,46R | €-202,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 37,25% | 0,89 | -0,06R | €-29,33 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 113 | 113 | 42,48% | 1,11 | 0,05R | €59,96 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 9 | 9 | 44,44% | 0,87 | -0,07R | €-6,67 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 2 | 51 | 51 | 41,18% | 1,25 | 0,10R | €50,20 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 3 | 56 | 56 | 28,57% | 0,55 | -0,26R | €-144,73 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,60 | -0,22R | €-127,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 75 | 75 | 20,00% | 0,42 | -0,40R | €-298,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 40,54% | 1,06 | 0,03R | €24,26 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 1 | 179 | 179 | 34,64% | 0,77 | -0,12R | €-219,83 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 3 | 21 | 21 | 23,81% | 0,43 | -0,37R | €-78,66 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 4 | 74 | 74 | 37,84% | 1,33 | 0,13R | €97,99 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 3 | 91 | 91 | 28,57% | 0,60 | -0,23R | €-212,43 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 95 | 95 | 21,05% | 0,53 | -0,25R | €-237,49 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 0 | 40 | 33 | 37,50% | 0,73 | -0,14R | €-57,99 |
| Rapida 1H V2 | TRANSITION | 0 | 7 | 7 | 57,14% | 0,81 | -0,07R | €-4,61 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 74 | 74 | 20,27% | 0,37 | -0,43R | €-315,89 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 69 | 69 | 39,13% | 0,94 | -0,03R | €-22,82 |
| Rapida 1H V3 Filtered | RANGE | 1 | 174 | 174 | 37,36% | 0,82 | -0,09R | €-164,09 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 3 | 21 | 21 | 33,33% | 0,70 | -0,18R | €-38,59 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 3 | 73 | 73 | 38,36% | 1,08 | 0,04R | €26,36 |
| Rapida 1H V3 Filtered | TREND_DOWN | 3 | 86 | 86 | 29,07% | 0,61 | -0,21R | €-180,13 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 108 | 108 | 37,04% | 1,00 | 0,00R | €0,97 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-232,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 41,67% | 1,03 | 0,01R | €8,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 141 | 141 | 38,30% | 0,90 | -0,05R | €-68,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 2 | 11 | 11 | 36,36% | 0,71 | -0,17R | €-18,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 3 | 55 | 55 | 38,18% | 0,98 | -0,01R | €-5,21 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 4 | 61 | 61 | 29,51% | 0,63 | -0,22R | €-132,64 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 69 | 69 | 28,99% | 0,67 | -0,17R | €-116,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 23,08% | 0,19 | -0,65R | €-84,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 79 | 79 | 43,04% | 0,86 | -0,08R | €-63,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 3 | 31 | 31 | 58,06% | 1,29 | 0,12R | €36,25 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 1 | 32 | 32 | 43,75% | 0,84 | -0,09R | €-30,04 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 16,67% | 0,19 | -0,63R | €-75,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 81 | 81 | 39,51% | 0,94 | -0,03R | €-27,15 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 3 | 31 | 31 | 38,71% | 1,09 | 0,04R | €11,12 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 32 | 32 | 34,38% | 0,76 | -0,15R | €-46,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 5,56% | 0,10 | -0,73R | €-131,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 38,33% | 0,88 | -0,07R | €-39,77 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 98 | 98 | 40,82% | 0,93 | -0,04R | €-34,70 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,22 | -0,65R | €-51,67 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 3 | 46 | 46 | 41,30% | 1,17 | 0,07R | €32,18 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 46 | 46 | 34,78% | 0,76 | -0,14R | €-63,47 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 17,39% | 0,32 | -0,51R | €-234,33 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 176 | 176 | 38,64% | 0,87 | -0,07R | €-116,04 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 3 | 57 | 57 | 33,33% | 0,91 | -0,04R | €-22,60 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 3 | 86 | 86 | 29,07% | 0,61 | -0,21R | €-180,13 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 94 | 94 | 31,91% | 0,79 | -0,11R | €-104,22 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 73 | 73 | 20,55% | 0,38 | -0,42R | €-304,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 68 | 68 | 36,76% | 0,83 | -0,09R | €-63,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 172 | 172 | 37,21% | 0,80 | -0,10R | €-178,82 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 3 | 20 | 20 | 35,00% | 0,76 | -0,14R | €-28,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 3 | 68 | 68 | 38,24% | 1,10 | 0,04R | €29,13 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 3 | 86 | 86 | 29,07% | 0,61 | -0,21R | €-180,13 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 91 | 91 | 30,77% | 0,75 | -0,13R | €-121,78 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 1,26 | 0,13R | €18,79 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 34 | 34 | 23,53% | 0,48 | -0,41R | €-138,96 |
| SHADOW_4H_WIDE | RANGE | 6 | 65 | 65 | 15,38% | 0,60 | -0,28R | €-183,37 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 4 | 8 | 8 | 25,00% | 0,92 | -0,06R | €-5,07 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 36 | 36 | 13,89% | 0,39 | -0,45R | €-163,12 |
| SHADOW_4H_WIDE | TREND_DOWN | 8 | 39 | 39 | 28,21% | 1,14 | 0,09R | €34,81 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 38 | 38 | 23,68% | 1,04 | 0,02R | €8,48 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 0,99 | -0,00R | €-0,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 64 | 64 | 48,44% | 1,13 | 0,06R | €37,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 2 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-3,07 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 13 | 13 | 53,85% | 1,74 | 0,31R | €39,93 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
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
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
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
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,62 | -0,24R | €-109,67 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 59 | 59 | 35,59% | 0,97 | -0,01R | €-8,05 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 1 | 139 | 139 | 41,73% | 0,97 | -0,01R | €-20,15 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 4 | 19 | 19 | 26,32% | 0,66 | -0,19R | €-35,70 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 71 | 71 | 42,25% | 1,47 | 0,21R | €151,63 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 5 | 70 | 70 | 35,71% | 0,91 | -0,05R | €-32,07 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 94 | 94 | 36,17% | 1,12 | 0,05R | €48,17 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 15,38% | 0,48 | -0,33R | €-42,51 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 35,85% | 1,00 | -0,00R | €-1,04 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 67 | 67 | 47,76% | 1,21 | 0,10R | €70,23 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,57 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 2 | 38 | 38 | 47,37% | 2,09 | 0,35R | €134,72 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 2 | 42 | 42 | 35,71% | 1,10 | 0,05R | €19,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,58 | -0,25R | €-135,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 67 | 67 | 38,81% | 0,91 | -0,05R | €-30,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 138 | 138 | 41,30% | 1,11 | 0,05R | €67,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 4 | 20 | 20 | 40,00% | 0,63 | -0,19R | €-38,77 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 2 | 61 | 61 | 47,54% | 1,25 | 0,11R | €65,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 5 | 93 | 93 | 38,71% | 0,93 | -0,03R | €-23,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 96 | 96 | 50,00% | 1,33 | 0,13R | €127,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,65 | -0,22R | €-102,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 57 | 57 | 36,84% | 1,01 | 0,00R | €2,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 1 | 127 | 127 | 44,88% | 1,04 | 0,02R | €26,32 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 4 | 17 | 17 | 35,29% | 0,85 | -0,07R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 54 | 54 | 46,30% | 1,36 | 0,16R | €87,25 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 5 | 70 | 70 | 38,57% | 0,89 | -0,05R | €-36,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 73 | 73 | 36,99% | 0,73 | -0,12R | €-87,95 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 2 | 32 | 32 | 34,38% | 0,86 | -0,08R | €-25,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 2 | 32 | 32 | 34,38% | 0,88 | -0,07R | €-23,11 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 18 | 18 | 27,78% | 0,63 | -0,21R | €-38,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 38 | 38 | 39,47% | 1,17 | 0,09R | €34,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,65 | -0,18R | €-10,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 2 | 26 | 26 | 34,62% | 0,99 | -0,01R | €-1,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 27 | 27 | 25,93% | 0,63 | -0,19R | €-50,44 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 5 | 77 | 77 | 38,96% | 1,08 | 0,04R | €32,25 |
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
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -0,79R | €-23,63 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 5 | 5 | 80,00% | 4,65 | 0,83R | €41,31 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,21 | -0,55R | €-82,64 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 1,09 | 0,05R | €25,32 |
| SHADOW_COMBO_SCANNER | RANGE | 2 | 76 | 76 | 44,74% | 1,40 | 0,20R | €150,28 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,23 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 4 | 53 | 53 | 43,40% | 1,67 | 0,31R | €165,88 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 43 | 43 | 30,23% | 0,73 | -0,15R | €-65,86 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 0 | 35 | 35 | 25,71% | 0,65 | -0,21R | €-73,73 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,77 | -0,15R | €-76,54 |
| SHADOW_COMBO_TREND | RANGE | 5 | 115 | 115 | 33,91% | 0,95 | -0,03R | €-33,62 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 3 | 13 | 13 | 30,77% | 0,89 | -0,05R | €-6,77 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 60 | 60 | 36,67% | 1,36 | 0,19R | €114,33 |
| SHADOW_COMBO_TREND | TREND_DOWN | 7 | 60 | 60 | 30,00% | 0,70 | -0,17R | €-99,55 |
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
| SHADOW_DONCHIAN_1H | RANGE | 2 | 56 | 56 | 30,36% | 0,88 | -0,08R | €-45,83 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 9 | 9 | 44,44% | 1,63 | 0,28R | €25,45 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 0 | 24 | 24 | 41,67% | 1,71 | 0,34R | €82,19 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 2 | 20 | 20 | 25,00% | 0,29 | -0,51R | €-102,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 1 | 39 | 39 | 28,21% | 1,09 | 0,05R | €18,70 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,23 | -0,63R | €-107,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 21,43% | 0,16 | -0,64R | €-89,01 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 36 | 36 | 30,56% | 0,73 | -0,17R | €-60,89 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 7 | 7 | 57,14% | 3,24 | 0,65R | €45,72 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 0 | 17 | 17 | 52,94% | 2,80 | 0,66R | €111,46 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 2 | 18 | 18 | 27,78% | 0,32 | -0,51R | €-92,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 1 | 25 | 25 | 24,00% | 0,92 | -0,03R | €-8,27 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 0 | 37 | 37 | 24,32% | 0,57 | -0,27R | €-100,46 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 49 | 49 | 28,57% | 0,72 | -0,19R | €-91,58 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 115 | 115 | 34,78% | 1,04 | 0,02R | €23,33 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 4 | 14 | 14 | 35,71% | 1,31 | 0,14R | €19,49 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 58 | 58 | 36,21% | 1,25 | 0,14R | €78,65 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 7 | 62 | 62 | 30,65% | 0,69 | -0,17R | €-107,05 |
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
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 75 | 75 | 32,00% | 1,00 | 0,00R | €1,97 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 4 | 30 | 30 | 46,67% | 1,78 | 0,40R | €120,27 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 2 | 46 | 46 | 34,78% | 1,09 | 0,06R | €25,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 44,44% | 0,85 | -0,08R | €-14,12 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 2 | 138 | 138 | 65,22% | 1,37 | 0,12R | €166,37 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 72 | 72 | 75,00% | 1,91 | 0,22R | €160,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 2 | 75 | 75 | 65,33% | 1,35 | 0,12R | €90,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,63 | -0,24R | €-34,08 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 76 | 76 | 34,21% | 1,11 | 0,07R | €50,71 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 4 | 29 | 29 | 37,93% | 1,23 | 0,14R | €40,36 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 2 | 42 | 42 | 38,10% | 1,23 | 0,14R | €58,57 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 1,36 | 0,21R | €18,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 68 | 68 | 30,88% | 1,10 | 0,07R | €44,75 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 3 | 27 | 27 | 40,74% | 1,41 | 0,24R | €64,16 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 2 | 39 | 39 | 38,46% | 1,25 | 0,16R | €60,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,90R | €-71,98 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 57 | 57 | 36,84% | 1,14 | 0,09R | €51,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 4 | 22 | 22 | 50,00% | 2,31 | 0,56R | €122,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 31 | 31 | 25,81% | 0,70 | -0,22R | €-66,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,57 | -0,31R | €-43,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 71 | 71 | 33,80% | 1,11 | 0,06R | €45,44 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 4 | 29 | 29 | 41,38% | 1,42 | 0,24R | €70,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 2 | 40 | 40 | 37,50% | 1,20 | 0,12R | €48,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 19,57% | 0,44 | -0,37R | €-168,98 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 67 | 67 | 32,84% | 0,87 | -0,08R | €-53,81 |
| Forza relativa 1H V1 | RANGE | 5 | 159 | 159 | 30,82% | 0,85 | -0,08R | €-134,84 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 3 | 15 | 15 | 6,67% | 0,21 | -0,56R | €-83,80 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 3 | 70 | 70 | 37,14% | 1,40 | 0,20R | €140,40 |
| Forza relativa 1H V1 | TREND_DOWN | 6 | 69 | 69 | 28,99% | 0,83 | -0,09R | €-62,38 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 95 | 95 | 25,26% | 0,91 | -0,05R | €-45,58 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,64 | -0,21R | €-41,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 26 | 23 | 38,46% | 1,35 | 0,18R | €47,67 |
| Forza relativa 1H V2 | RANGE | 4 | 67 | 65 | 35,82% | 0,92 | -0,04R | €-29,68 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 2 | 39 | 34 | 41,03% | 1,80 | 0,36R | €140,16 |
| Forza relativa 1H V2 | TREND_DOWN | 2 | 33 | 32 | 30,30% | 0,95 | -0,02R | €-7,09 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 3 | 13 | 13 | 30,77% | 1,06 | 0,03R | €3,81 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 3 | 42 | 42 | 28,57% | 0,39 | -0,37R | €-156,37 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 3 | 13 | 13 | 30,77% | 1,06 | 0,03R | €3,81 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 3 | 42 | 42 | 28,57% | 0,39 | -0,37R | €-156,37 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 3 | 13 | 13 | 30,77% | 1,06 | 0,03R | €3,81 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 3 | 42 | 42 | 28,57% | 0,39 | -0,37R | €-156,37 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,07 | 0,03R | €4,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 71 | 71 | 29,58% | 0,65 | -0,19R | €-135,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 3 | 14 | 14 | 35,71% | 1,18 | 0,08R | €11,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 34 | 34 | 41,18% | 1,16 | 0,08R | €28,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 3 | 38 | 38 | 28,95% | 0,39 | -0,35R | €-134,57 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 23 | 23 | 4,35% | 0,16 | -0,42R | €-97,06 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 29,63% | 0,29 | -0,48R | €-128,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 63 | 63 | 55,56% | 0,69 | -0,13R | €-84,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 4 | 17 | 17 | 64,71% | 1,41 | 0,15R | €24,65 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 27 | 27 | 59,26% | 1,51 | 0,22R | €58,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 5 | 61 | 61 | 55,74% | 0,68 | -0,13R | €-80,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 19 | 19 | 42,11% | 0,65 | -0,16R | €-29,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,22 | -0,52R | €-124,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 56 | 56 | 55,36% | 0,42 | -0,25R | €-138,62 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 4 | 14 | 14 | 57,14% | 1,28 | 0,12R | €17,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 26 | 26 | 61,54% | 1,57 | 0,23R | €59,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 5 | 51 | 51 | 54,90% | 0,71 | -0,12R | €-62,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 18 | 18 | 38,89% | 0,34 | -0,31R | €-55,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 50 | 50 | 32,00% | 0,86 | -0,08R | €-38,14 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,55 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 3 | 41 | 41 | 41,46% | 1,63 | 0,24R | €97,61 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 51 | 51 | 31,37% | 0,82 | -0,10R | €-49,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,55 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 3 | 41 | 41 | 41,46% | 1,63 | 0,24R | €97,61 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 51 | 51 | 31,37% | 0,82 | -0,10R | €-49,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,55 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 3 | 41 | 41 | 41,46% | 1,63 | 0,24R | €97,61 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,23 | -0,51R | €-71,62 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 1,09 | 0,05R | €25,90 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 71 | 71 | 45,07% | 1,55 | 0,26R | €183,27 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,23 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 4 | 49 | 49 | 42,86% | 1,72 | 0,33R | €163,45 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
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
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 66 | 66 | 43,94% | 1,40 | 0,20R | €130,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 4 | 37 | 37 | 45,95% | 2,11 | 0,43R | €159,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,04 | -0,54R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 39 | 39 | 48,72% | 1,37 | 0,16R | €61,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,34 | -0,35R | €-14,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 40 | 40 | 50,00% | 1,40 | 0,16R | €62,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -0,75R | €-82,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 33 | 33 | 39,39% | 1,40 | 0,20R | €65,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 3 | 35 | 35 | 40,00% | 1,71 | 0,29R | €102,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,54 | -0,25R | €-38,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 39 | 39 | 48,72% | 1,37 | 0,16R | €61,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,34 | -0,35R | €-14,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 42 | 42 | 47,62% | 1,32 | 0,13R | €52,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,26 | -0,47R | €-61,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 33 | 33 | 39,39% | 1,40 | 0,20R | €65,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 3 | 36 | 36 | 38,89% | 1,59 | 0,26R | €91,94 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,48 | -0,30R | €-48,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 54 | 54 | 44,44% | 0,99 | -0,00R | €-1,94 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,40 | 0,16R | €119,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,33 | -0,31R | €-15,26 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 3 | 46 | 46 | 50,00% | 1,36 | 0,15R | €67,24 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 56 | 56 | 44,64% | 0,92 | -0,03R | €-18,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,51 | -0,29R | €-20,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 33,96% | 1,05 | 0,03R | €13,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 2 | 62 | 62 | 41,94% | 1,42 | 0,21R | €129,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 4 | 37 | 37 | 43,24% | 1,86 | 0,36R | €132,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 41 | 41 | 29,27% | 0,77 | -0,13R | €-54,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,60R | €-41,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 35,85% | 1,00 | -0,00R | €-1,34 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 58 | 58 | 41,38% | 1,44 | 0,23R | €131,53 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 2 | 3 | 3 | 0,00% | 0,00 | -0,72R | €-21,54 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 4 | 31 | 31 | 41,94% | 2,35 | 0,49R | €153,19 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 38 | 38 | 28,95% | 0,79 | -0,11R | €-43,01 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,35 | -0,47R | €-74,87 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 52 | 52 | 34,62% | 0,97 | -0,02R | €-9,35 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 75 | 75 | 49,33% | 1,64 | 0,27R | €205,66 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 6 | 6 | 0,00% | 0,00 | -0,89R | €-53,38 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 3 | 54 | 54 | 42,59% | 1,63 | 0,27R | €143,65 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 78 | 78 | 34,62% | 1,08 | 0,04R | €29,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,84 | -0,09R | €-1,73 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,41 | -0,47R | €-32,89 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
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
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-17T13:06:51+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **766**
- Scenari virtuali ancora attivi: **13710**
- Gruppi in attesa dell'uscita originale: **351**
- Gruppi con originale chiuso ma Shadow ancora attive: **415**
- Confronti completati: **228698**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 5457 | 5526 | +€7,73 | 51,2% | 1541 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5457 | 5526 | +€6,79 | 50,6% | 1524 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5457 | 5526 | +€4,33 | 48,5% | 1698 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 5453 | 5526 | €-0,34 | 47,3% | 1189 | 711 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5451 | 5520 | +€5,50 | 49,0% | 1539 | 123 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5448 | 5517 | +€4,12 | 49,0% | 1469 | 185 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5415 | 5484 | +€7,12 | 44,8% | 1236 | 111 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5415 | 5484 | +€5,91 | 44,8% | 1172 | 177 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5415 | 5484 | +€5,14 | 42,8% | 1359 | 98 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5408 | 5481 | €-0,13 | 42,6% | 717 | 1033 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5406 | 5475 | +€2,07 | 38,1% | 663 | 922 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5391 | 5464 | €-4,69 | 34,4% | 418 | 1451 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5383 | 5452 | +€4,89 | 44,0% | 1059 | 288 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5382 | 5451 | +€1,27 | 35,8% | 531 | 1150 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5371 | 5440 | +€3,04 | 42,3% | 939 | 506 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5362 | 5431 | +€5,24 | 35,1% | 780 | 496 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5307 | 5376 | €-4,81 | 35,2% | 933 | 1043 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5306 | 5372 | +€5,61 | 39,1% | 399 | 760 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5284 | 5353 | €-2,94 | 32,7% | 454 | 1292 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5128 | 5197 | €-8,17 | 27,5% | 418 | 1470 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-17T13:07:01+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **228698**
- Valutazioni prodotte: **19301**
- Candidature al Blocco 5: **42**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 248 | 0,555 | 0,461 | 0,442 | 68,5% | 98,3 | ELIGIBLE_FOR_MUTATION |
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

Generato: 2026-08-17T13:09:21+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 61 | 100,00% | 0,87 | €-106,99 | €-1,75 | 2,58% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 61 | 100,00% | 0,89 | €-91,22 | €-1,50 | 2,75% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 32 | 96,97% | 0,99 | €-9,97 | €-0,31 | 2,95% | EARLY_NOT_CONFIRMED |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 26 | 92,86% | 0,00 | €-285,06 | €-10,96 | 2,85% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 65 | 100,00% | 1,03 | +€37,91 | +€0,58 | 2,13% | NOT_READY_FOR_PROMOTION |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-17T13:06:22+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **119**
- Simulazioni completate nel ciclo: **11**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **561.46 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 235 | 0 | 31137.12 |
| DOWN_20 | 235 | 0 | 62274.24 |
| DOWN_30 | 235 | 0 | 93411.36 |
| DOWN_40 | 235 | 67 | 119466.67 |
| UP_10 | 189 | 0 | 14718.95 |
| UP_20 | 189 | 3 | 29449.62 |
| UP_30 | 189 | 10 | 44252.33 |
| UP_40 | 189 | 76 | 55722.93 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-17T13:05:15+00:00

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

Generato: 2026-08-17T13:09:25+00:00

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

Generato: 2026-08-17T13:09:25+00:00

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

Generato: 2026-08-17T13:09:25+00:00

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

Generato: 2026-08-17T13:09:25+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 18.3 | E | 119 | 1.17 | 0.075 | 8.02 |
| 2 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 17.6 | E | 45 | 1.60 | 0.251 | 5.48 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 16.8 | E | 70 | 1.33 | 0.145 | 5.98 |
| 4 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 15.0 | E | 123 | 1.03 | 0.015 | 16.32 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 14.9 | E | 143 | 0.91 | -0.042 | 18.56 |
| 6 | SHADOW_DONCHIAN_1H | BASELINE | 13.6 | E | 63 | 1.19 | 0.112 | 8.55 |
| 7 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 13.0 | E | 112 | 0.95 | -0.028 | 23.13 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 12.8 | E | 103 | 0.97 | -0.014 | 12.98 |
| 9 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 11.9 | E | 113 | 0.88 | -0.068 | 21.34 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 11.3 | E | 117 | 0.83 | -0.086 | 17.33 |

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

Generato: 2026-08-17T13:09:25+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **HIGH_VOLATILITY**
- Righe di performance: **640**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **302**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | shadow-donchian-1h-gb20-120r-v1 | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.695 | 0.00 |
| 2 | MAIN_SIDE_REGIME_GUARD_V1 | main-side-regime-guard-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.485 | 0.00 |
| 3 | SHADOW_BTC_ADAPTIVE_1H | shadow-btc-adaptive-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.861 | 0.00 |
| 4 | SHADOW_BTC_DONCHIAN_1H | shadow-btc-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.969 | 0.00 |
| 5 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | shadow-combo-trend-side-regime-guard-v1 | INSUFFICIENT | 77.2 | 6 | 2.29 | 0.514 | 1.28 |
| 6 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | shadow-combo-adaptive-side-regime-guard-v1 | INSUFFICIENT | 76.7 | 9 | 2.87 | 0.727 | 2.38 |
| 7 | SHADOW_ETH_ADAPTIVE_1H | shadow-eth-adaptive-1h | INSUFFICIENT | 75.7 | 1 | 99.00 | 0.286 | 0.00 |
| 8 | SHADOW_BTC_EMA_1H | shadow-btc-ema-1h | INSUFFICIENT | 75.4 | 3 | 2.58 | 0.577 | 1.10 |
| 9 | SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | shadow-combo-adaptive-runner25-v1 | OBSERVING | 74.6 | 10 | 2.19 | 0.547 | 1.28 |
| 10 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | shadow-combo-adaptive-partial-1r-v1 | OBSERVING | 74.0 | 14 | 1.93 | 0.392 | 1.33 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-17T13:09:25+00:00

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

Generato: 2026-08-17T13:06:22+00:00

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
