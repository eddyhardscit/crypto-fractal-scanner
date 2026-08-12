# Paper trading automatico KuCoin

Generato: 2026-08-12T13:28:53+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-12T13:23:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-12T13:23:32+00:00 | 2026-08-12T13:23:32+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-12T13:00:00+00:00 | 2026-08-12T13:00:00+00:00 | 8,8 min | 25,0 min | OK |
| 60m | 12 | 2026-08-12T12:00:00+00:00 | 2026-08-12T12:00:00+00:00 | 23,8 min | 45,0 min | OK |
| 240m | 12 | 2026-08-12T08:00:00+00:00 | 2026-08-12T08:00:00+00:00 | 1,40 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | CYS | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,43 | 6,00 | 1,57 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,18 | 6,00 | 2,82 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,12 | 6,00 | 2,88 | STALE_CANDLE | 1,40 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 2,88 | 6,00 | 3,12 | STALE_CANDLE | 1,40 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,88 | 6,00 | 4,12 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,40 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | LONG | 1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | NEAR | 240m | SHORT | -1,10 | 6,00 | 4,90 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,51 | 6,00 | 5,49 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,24 | 6,00 | 5,76 | STALE_CANDLE | 1,40 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | BEAT | 60m | SHORT | -8,25 | 5,00 | 0,00 | READY | 23,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | BEAT | 60m | SHORT | -8,25 | 4,50 | 0,00 | READY | 23,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | BEAT | 60m | SHORT | -8,25 | 4,50 | 0,00 | READY | 23,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | BEAT | 60m | SHORT | -8,25 | 4,00 | 0,00 | READY | 23,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 NoHigh — Regime Guard | BEAT | 60m | SHORT | -8,25 | 4,50 | 0,00 | READY | 23,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | BEAT | 60m | SHORT | -8,25 | 5,50 | 0,00 | STRATEGY_FILTER | 23,8 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BEAT | 60m | SHORT | -8,25 | 5,00 | 0,00 | STRATEGY_FILTER | 23,8 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | CYS | 60m | LONG | 7,00 | 5,00 | 0,00 | STRATEGY_FILTER | 23,8 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.700,66 | -2,99% | €-47,69 | €3.000,00 | -1,59% | 4 | 40 | 35,00% | 0,78 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 40 | 1194 | PRIME INDICAZIONI | 50 (mancano 10) |

- Trade del Principale 4H chiusi: **40**; win rate **35,00%**; profit factor **0,78**.
- Expectancy: **€-7,08** per trade; P&L netto: **€-283,07**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.700,66 | €1.263,26 | €3.789,79 | €193,15 | €-15,14 |
| TEST | Rapida score 6–7,5 — Cost Aware | 3 | €10.519,56 | €3.309,29 | €9.927,86 | €158,82 | €-14,00 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.506,06 | €4.951,56 | €9.903,13 | €158,45 | €14,85 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.478,70 | €3.286,45 | €9.859,35 | €157,87 | €-13,88 |
| TEST | Rapida V3 NoHigh — Regime Guard | 4 | €10.393,04 | €3.357,76 | €10.073,28 | €207,12 | €-26,28 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 1 | €10.308,24 | €1.585,67 | €4.757,02 | €53,28 | €-10,95 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.307,05 | €1.709,21 | €5.127,62 | €104,16 | €-10,81 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 1 | €10.273,80 | €1.542,02 | €4.626,07 | €51,81 | €-10,65 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.258,70 | €4.834,98 | €9.669,97 | €154,72 | €14,50 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.250,69 | €889,33 | €2.667,99 | €102,34 | €-13,91 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.243,90 | €3.024,24 | €9.072,71 | €204,81 | €-10,51 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 3 | €10.220,30 | €3.732,98 | €7.465,95 | €153,40 | €-18,49 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €10.200,10 | €3.199,07 | €9.597,22 | €153,67 | €-13,51 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 4 | €10.175,67 | €5.519,69 | €11.039,39 | €153,46 | €44,68 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.092,94 | €5.141,20 | €15.423,59 | €151,23 | €42,75 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 6 | €10.064,73 | €1.968,64 | €5.905,92 | €201,25 | €2,50 |
| TEST | FAST NoHigh <7,5 · SHORT only | 1 | €10.051,73 | €1.546,22 | €4.638,65 | €51,95 | €-10,68 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €10.049,29 | €4.916,54 | €9.833,09 | €201,08 | €17,66 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.046,65 | €5.449,71 | €10.899,42 | €200,91 | €44,11 |
| TEST | Sol Donchian 1H | 1 | €10.043,68 | €1.309,61 | €3.928,82 | €50,29 | €-11,75 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.043,34 | €3.784,05 | €11.352,15 | €200,71 | €-25,94 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.039,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2 | €10.035,12 | €1.626,88 | €4.880,65 | €100,14 | €41,60 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.015,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.005,03 | €50,00 | €750,00 | €4,14 | €1,62 |
| TEST | Doge Donchian 1H | 0 | €10.004,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.001,01 | €10,00 | €150,00 | €0,83 | €0,32 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €9.994,61 | €10,00 | €150,00 | €1,41 | €0,26 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.987,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.986,17 | €1.301,67 | €3.905,01 | €49,98 | €-8,99 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €9.973,06 | €50,00 | €750,00 | €7,03 | €1,29 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.950,10 | €1.152,72 | €3.458,17 | €49,80 | €-7,96 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.937,20 | €1.413,45 | €2.826,90 | €49,75 | €-12,18 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.926,30 | €211,66 | €1.058,30 | €9,93 | €1,82 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.924,32 | €359,25 | €1.796,26 | €9,92 | €3,89 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 4 | €9.915,33 | €4.189,77 | €8.379,55 | €149,27 | €-17,98 |
| TEST | Doge Bollinger 1H | 0 | €9.906,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 0 | €9.898,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.878,92 | €1.406,00 | €2.812,00 | €49,49 | €-18,14 |
| TEST | Btc Ema 1H | 1 | €9.863,97 | €1.141,05 | €3.423,15 | €49,29 | €6,22 |
| TEST | Ampia 4H | 4 | €9.863,04 | €1.901,42 | €3.802,85 | €145,59 | €-10,32 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 1 | €9.858,39 | €1.498,86 | €4.496,57 | €50,36 | €-10,35 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.836,45 | €2.576,01 | €7.728,04 | €196,57 | €-4,38 |
| TEST | Rapida V1 — target pieno 2R | 5 | €9.818,09 | €3.742,93 | €11.228,78 | €148,65 | €45,54 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.813,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.804,28 | €1.611,83 | €4.835,48 | €98,65 | €-1,93 |
| TEST | Combo Mean Reversion | 1 | €9.797,38 | €1.968,04 | €3.936,09 | €47,23 | €-40,48 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.796,05 | €1.460,09 | €4.380,26 | €49,06 | €-13,10 |
| TEST | Scanner Bottom10 Short | 3 | €9.776,35 | €3.683,87 | €7.367,73 | €146,56 | €11,53 |
| TEST | Scanner Bottom15 Short | 3 | €9.776,35 | €3.683,87 | €7.367,73 | €146,56 | €11,53 |
| TEST | Scanner Bottom20 Short | 3 | €9.776,35 | €3.683,87 | €7.367,73 | €146,56 | €11,53 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 4 | €9.759,01 | €5.300,15 | €10.600,29 | €195,16 | €26,17 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 4 | €9.744,18 | €4.101,19 | €8.202,39 | €146,69 | €-17,36 |
| TEST | Eth Adaptive 1H | 1 | €9.739,53 | €1.127,99 | €3.383,96 | €48,73 | €-4,24 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 1 | €9.734,85 | €135,24 | €405,73 | €48,69 | €-2,41 |
| TEST | Global Confluence puro 1H | 0 | €9.730,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 2 | €9.723,21 | €2.161,16 | €6.483,48 | €100,31 | €-10,25 |
| TEST | Sol Adaptive 1H | 1 | €9.715,37 | €1.125,87 | €3.377,60 | €48,64 | €-10,10 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.709,30 | €3.672,99 | €7.345,98 | €145,56 | €11,46 |
| TEST | Master Adaptive Expanded V1 | 7 | €9.707,72 | €3.976,59 | €7.953,17 | €194,48 | €79,62 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.694,53 | €3.667,40 | €7.334,81 | €145,33 | €11,44 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.689,09 | €2.860,45 | €8.581,34 | €193,72 | €-9,94 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €9.672,41 | €5.246,70 | €10.493,40 | €193,42 | €42,47 |
| TEST | Eth Ema 1H | 1 | €9.669,00 | €1.119,82 | €3.359,45 | €48,38 | €-4,21 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €9.667,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €9.666,75 | €5.243,63 | €10.487,26 | €193,31 | €42,44 |
| TEST | Rapida 1H V3 Filtered — madre | 2 | €9.659,67 | €2.147,04 | €6.441,12 | €99,65 | €-10,18 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €9.652,82 | €799,57 | €2.398,70 | €97,85 | €21,49 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.619,93 | €3.639,18 | €7.278,36 | €144,22 | €11,35 |
| TEST | Forza relativa 1H V2 | 1 | €9.604,60 | €1.698,68 | €3.397,35 | €48,92 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €9.600,58 | €5.207,74 | €10.415,48 | €191,99 | €42,15 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 1 | €9.600,41 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 1 | €9.600,03 | €1.489,03 | €4.467,09 | €50,03 | €-10,28 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 6 | €9.563,98 | €4.527,11 | €9.054,22 | €192,46 | €45,30 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.562,14 | €4.024,58 | €8.049,15 | €143,95 | €-17,04 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 6 | €9.553,81 | €4.522,29 | €9.044,59 | €192,25 | €45,25 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.533,25 | €4.512,57 | €9.025,13 | €191,84 | €45,15 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.523,36 | €3.112,37 | €9.337,12 | €142,93 | €68,40 |
| TEST | Combo Adaptive — parziale 1R | 4 | €9.521,15 | €4.023,21 | €8.046,42 | €143,34 | €-17,27 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.520,41 | €4.445,01 | €8.890,03 | €189,24 | €44,65 |
| TEST | Master Adaptive V1 | 6 | €9.516,85 | €4.504,80 | €9.009,60 | €191,51 | €45,08 |
| TEST | Forza relativa 1H V1 | 5 | €9.500,62 | €3.578,01 | €7.156,01 | €142,74 | €73,38 |
| TEST | Top 5 + BTC — Guard | 1 | €9.483,90 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| TEST | Combo Scanner | 4 | €9.472,58 | €5.133,16 | €10.266,32 | €189,43 | €41,32 |
| TEST | Rapida V3 — senza ESPORTS | 2 | €9.463,04 | €2.103,34 | €6.310,01 | €97,62 | €-9,97 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 1 | €9.435,69 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.429,69 | €2.203,64 | €4.407,28 | €97,97 | €5,51 |
| TEST | Top 5 + BTC — solo MFE | 4 | €9.417,29 | €5.108,31 | €10.216,63 | €188,32 | €41,35 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.390,41 | €4.444,95 | €8.889,90 | €188,97 | €44,48 |
| TEST | Scanner Top10 Long | 4 | €9.372,59 | €5.084,07 | €10.168,13 | €141,35 | €41,15 |
| TEST | Scanner Top15 Long | 4 | €9.372,59 | €5.084,07 | €10.168,13 | €141,35 | €41,15 |
| TEST | Scanner Top20 Long | 4 | €9.372,59 | €5.084,07 | €10.168,13 | €141,35 | €41,15 |
| TEST | Combo Trend | 5 | €9.271,12 | €4.937,78 | €9.875,56 | €184,97 | €13,55 |
| TEST | Top 5 + BTC — Guard + MFE | 1 | €9.263,33 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 4 | €9.196,69 | €3.992,29 | €7.984,58 | €144,36 | €32,39 |
| TEST | Rapida V3 — Long Only | 2 | €9.190,53 | €761,28 | €2.283,83 | €93,16 | €20,46 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.128,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 2 | €9.040,41 | €2.312,34 | €4.624,68 | €92,99 | €-7,41 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.700,66 | €-283,07 | 40 | 40 | 35,00% | 0,78 | €-7,08 | 6,36% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.519,56 | €538,70 | 48 | 48 | 52,08% | 1,63 | €11,22 | 2,44% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.506,06 | €496,58 | 52 | 52 | 48,08% | 1,39 | €9,55 | 3,39% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.478,70 | €497,69 | 90 | 90 | 44,44% | 1,29 | €5,53 | 2,55% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.393,04 | €424,58 | 34 | 34 | 55,88% | 1,78 | €12,49 | 3,55% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.308,24 | €321,24 | 87 | 87 | 42,53% | 1,17 | €3,69 | 4,71% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.307,05 | €320,16 | 26 | 26 | 50,00% | 1,59 | €12,31 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.273,80 | €286,43 | 25 | 25 | 52,00% | 1,46 | €11,46 | 2,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.258,70 | €249,44 | 20 | 20 | 45,00% | 1,63 | €12,47 | 3,39% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.250,69 | €265,31 | 19 | 19 | 47,37% | 1,61 | €13,96 | 2,40% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.243,90 | €258,60 | 77 | 77 | 40,26% | 1,16 | €3,36 | 4,30% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.220,30 | €242,66 | 48 | 48 | 47,92% | 1,30 | €5,06 | 4,12% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.200,10 | €218,58 | 48 | 48 | 50,00% | 1,21 | €4,55 | 3,20% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.175,67 | €136,95 | 57 | 57 | 42,11% | 1,10 | €2,40 | 6,80% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.092,94 | €57,87 | 85 | 85 | 42,35% | 1,03 | €0,68 | 3,64% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.064,73 | €65,12 | 89 | 89 | 43,82% | 1,04 | €0,73 | 5,46% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.051,73 | €64,40 | 51 | 51 | 39,22% | 1,07 | €1,26 | 4,71% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.049,29 | €37,55 | 38 | 38 | 50,00% | 1,06 | €0,99 | 2,89% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.046,65 | €8,42 | 48 | 48 | 37,50% | 1,01 | €0,18 | 5,97% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.043,68 | €57,78 | 5 | 5 | 60,00% | 1,95 | €11,56 | 1,09% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.043,34 | €74,52 | 83 | 83 | 42,17% | 1,04 | €0,90 | 5,76% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Ema 1H | Trend following EMA | €10.039,73 | €39,73 | 11 | 11 | 63,64% | 1,18 | €3,61 | 1,44% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.035,12 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.015,61 | €15,61 | 8 | 8 | 50,00% | 1,43 | €1,95 | 0,36% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.005,03 | €3,85 | 23 | 23 | 43,48% | 1,04 | €0,17 | 0,33% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.004,83 | €4,83 | 8 | 8 | 62,50% | 1,03 | €0,60 | 1,30% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,01 | €0,77 | 23 | 23 | 43,48% | 1,04 | €0,03 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,41 | €-2,59 | 8 | 8 | 37,50% | 0,41 | €-0,32 | 0,04% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,56 | 11 | 11 | 27,27% | 0,38 | €-0,51 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.987,03 | €-12,97 | 8 | 8 | 37,50% | 0,41 | €-1,62 | 0,21% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.986,17 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-27,78 | 11 | 11 | 27,27% | 0,38 | €-2,53 | 0,53% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.950,10 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Btc Ema 4H | Trend following EMA | €9.937,20 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-74,88 | 11 | 11 | 27,27% | 0,10 | €-6,81 | 0,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.924,32 | €-78,49 | 23 | 23 | 43,48% | 0,39 | €-3,41 | 0,84% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.915,33 | €-62,91 | 53 | 53 | 37,74% | 0,93 | €-1,19 | 4,13% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.906,84 | €-93,16 | 5 | 5 | 40,00% | 0,44 | €-18,63 | 1,89% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.898,70 | €-101,30 | 31 | 31 | 32,26% | 0,83 | €-3,27 | 2,88% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.878,92 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Btc Ema 1H | Trend following EMA | €9.863,97 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,72% |
| TEST | Ampia 4H | Confluenza trend | €9.863,04 | €-125,24 | 34 | 34 | 23,53% | 0,86 | €-3,68 | 4,36% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.858,39 | €-129,33 | 27 | 27 | 40,74% | 0,81 | €-4,79 | 3,63% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.836,45 | €-154,78 | 55 | 51 | 43,64% | 0,87 | €-2,81 | 5,20% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.818,09 | €-222,25 | 94 | 94 | 34,04% | 0,89 | €-2,36 | 3,79% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | Sol Ema 1H | Trend following EMA | €9.813,68 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 2,63% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.804,28 | €-190,74 | 55 | 55 | 45,45% | 0,86 | €-3,47 | 4,39% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.797,38 | €-159,79 | 26 | 26 | 38,46% | 0,81 | €-6,15 | 4,44% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.796,05 | €-188,23 | 25 | 22 | 36,00% | 0,72 | €-7,53 | 3,38% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.776,35 | €-231,90 | 43 | 43 | 34,88% | 0,76 | €-5,39 | 4,67% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.776,35 | €-231,90 | 43 | 43 | 34,88% | 0,76 | €-5,39 | 4,67% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.776,35 | €-231,90 | 43 | 43 | 34,88% | 0,76 | €-5,39 | 4,67% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.759,01 | €-261,44 | 26 | 26 | 26,92% | 0,56 | €-10,06 | 3,53% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.744,18 | €-234,78 | 60 | 60 | 33,33% | 0,80 | €-3,91 | 5,15% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.739,53 | €-254,20 | 7 | 7 | 28,57% | 0,06 | €-36,31 | 2,64% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.734,85 | €-262,49 | 51 | 51 | 39,22% | 0,80 | €-5,15 | 4,70% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.730,31 | €-269,69 | 14 | 14 | 28,57% | 0,39 | €-19,26 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.723,21 | €-264,20 | 69 | 69 | 49,28% | 0,81 | €-3,83 | 6,78% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.715,37 | €-272,51 | 8 | 8 | 25,00% | 0,20 | €-34,06 | 3,53% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.709,30 | €-298,90 | 35 | 35 | 34,29% | 0,62 | €-8,54 | 4,68% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.707,72 | €-367,31 | 28 | 28 | 28,57% | 0,64 | €-13,12 | 4,45% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.694,53 | €-313,66 | 36 | 36 | 33,33% | 0,57 | €-8,71 | 4,68% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.689,09 | €-297,01 | 33 | 33 | 36,36% | 0,60 | €-9,00 | 4,02% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.672,41 | €-364,40 | 33 | 33 | 30,30% | 0,64 | €-11,04 | 6,69% |
| TEST | Eth Ema 1H | Trend following EMA | €9.669,00 | €-324,78 | 9 | 9 | 22,22% | 0,14 | €-36,09 | 3,31% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.667,19 | €-332,81 | 60 | 60 | 41,67% | 0,79 | €-5,55 | 5,92% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.666,75 | €-370,04 | 37 | 37 | 32,43% | 0,64 | €-10,00 | 6,99% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.659,67 | €-327,82 | 113 | 113 | 38,05% | 0,87 | €-2,90 | 6,75% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.652,82 | €-368,01 | 44 | 44 | 34,09% | 0,68 | €-8,36 | 7,45% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.619,93 | €-388,20 | 63 | 63 | 33,33% | 0,71 | €-6,16 | 5,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.604,60 | €-393,36 | 66 | 63 | 36,36% | 0,82 | €-5,96 | 8,06% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.600,58 | €-435,95 | 29 | 29 | 31,03% | 0,51 | €-15,03 | 6,44% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.600,41 | €-399,34 | 26 | 26 | 30,77% | 0,55 | €-15,36 | 6,38% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.600,03 | €-387,76 | 78 | 78 | 39,74% | 0,81 | €-4,97 | 5,51% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.563,98 | €-475,40 | 27 | 27 | 14,81% | 0,45 | €-17,61 | 6,51% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.562,14 | €-417,21 | 41 | 41 | 31,71% | 0,53 | €-10,18 | 5,15% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.553,81 | €-485,53 | 22 | 22 | 22,73% | 0,41 | €-22,07 | 6,10% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.533,25 | €-506,00 | 26 | 26 | 23,08% | 0,50 | €-19,46 | 5,75% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.523,36 | €-539,43 | 28 | 28 | 25,00% | 0,43 | €-19,27 | 6,39% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.521,15 | €-457,96 | 54 | 54 | 35,19% | 0,58 | €-8,48 | 4,94% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.520,41 | €-518,42 | 24 | 24 | 20,83% | 0,48 | €-21,60 | 5,87% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.516,85 | €-522,33 | 24 | 24 | 20,83% | 0,48 | €-21,76 | 5,91% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.500,62 | €-569,09 | 68 | 68 | 26,47% | 0,65 | €-8,37 | 7,87% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.483,90 | €-515,85 | 31 | 31 | 25,81% | 0,48 | €-16,64 | 5,97% |
| TEST | Combo Scanner | Combo Scanner | €9.472,58 | €-563,20 | 58 | 58 | 34,48% | 0,65 | €-9,71 | 7,59% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.463,04 | €-524,70 | 87 | 87 | 37,93% | 0,74 | €-6,03 | 6,72% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.435,69 | €-564,06 | 41 | 41 | 34,15% | 0,51 | €-13,76 | 5,64% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.429,69 | €-574,75 | 56 | 56 | 28,57% | 0,58 | €-10,26 | 6,66% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.417,29 | €-618,55 | 41 | 41 | 31,71% | 0,38 | €-15,09 | 7,03% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.390,41 | €-648,26 | 59 | 59 | 50,85% | 0,46 | €-10,99 | 7,16% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.372,59 | €-663,08 | 29 | 29 | 27,59% | 0,29 | €-22,86 | 8,29% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.372,59 | €-663,08 | 29 | 29 | 27,59% | 0,29 | €-22,86 | 8,29% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.372,59 | €-663,08 | 29 | 29 | 27,59% | 0,29 | €-22,86 | 8,29% |
| TEST | Combo Trend | Combo Trend | €9.271,12 | €-737,56 | 80 | 80 | 28,75% | 0,68 | €-9,22 | 9,62% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.263,33 | €-736,42 | 48 | 48 | 33,33% | 0,46 | €-15,34 | 7,43% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.196,69 | €-830,57 | 28 | 28 | 14,29% | 0,32 | €-29,66 | 9,72% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.190,53 | €-829,29 | 64 | 64 | 26,56% | 0,54 | €-12,96 | 9,45% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.128,10 | €-871,90 | 32 | 32 | 18,75% | 0,40 | €-27,25 | 8,91% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.040,41 | €-950,56 | 67 | 67 | 29,85% | 0,40 | €-14,19 | 9,82% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01674 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €-13,26 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | CYS | LONG | Confluenza trend | 240m | 3,0x | 1,54541 | 1,53820 | 1,35996 | 1,03800 | 1,91631 | €134,84 | €404,53 | €48,54 | €-1,89 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | SOL | LONG | Confluenza trend | 60m | 3,0x | 76,70334 | 76,47400 | 75,59881 | 51,51908 | 78,91239 | €20,30 | €60,89 | €0,88 | €-0,18 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,54541 | 1,53820 | 1,35996 | 1,03800 | 1,91631 | €134,24 | €402,71 | €48,32 | €-1,88 |
| Bilanciata 1H V1 | TUT | SHORT | Confluenza trend | 60m | 3,0x | 0,07664 | 0,07582 | 0,08584 | 0,10181 | 0,05825 | €139,76 | €419,29 | €50,31 | €4,51 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 1,65399 | 1,65600 | 1,61997 | 1,11093 | 1,72203 | €13,33 | €40,00 | €0,82 | €0,05 |
| Bilanciata 1H — LONG senza Range High Vol | SOL | LONG | Confluenza trend | 60m | 3,0x | 76,70334 | 76,47400 | 75,59881 | 51,51908 | 78,91239 | €1.099,99 | €3.299,97 | €47,52 | €-9,87 |
| Bilanciata 1H — LONG senza Range High Vol | HYPE | LONG | Confluenza trend | 60m | 3,0x | 55,31106 | 56,40900 | 55,88009 | 37,15060 | 56,90402 | €1.099,69 | €3.299,06 | €0,00 | €65,49 |
| Bilanciata 1H — LONG senza Range High Vol | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,50020 | 1,53820 | 1,32018 | 1,00763 | 1,86025 | €131,62 | €394,86 | €47,38 | €10,00 |
| Bilanciata 1H — LONG senza Range High Vol | NEAR | LONG | Confluenza trend | 60m | 3,0x | 1,65399 | 1,65600 | 1,61997 | 1,11093 | 1,72203 | €771,77 | €2.315,31 | €47,62 | €2,81 |
| Bilanciata 1H — LONG senza Range High Vol | ETH | LONG | Confluenza trend | 60m | 3,0x | 1910,13195 | 1907,74000 | 1882,62605 | 1282,97196 | 1965,14375 | €9,30 | €27,91 | €0,40 | €-0,03 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 63596,27820 | 63954,10000 | 64512,06461 | 84477,05621 | 61764,70539 | €1.127,13 | €3.381,38 | €48,69 | €-19,03 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,50020 | 1,53820 | 1,32018 | 1,00763 | 1,86025 | €136,27 | €408,82 | €49,06 | €10,36 |
| Bilanciata 1H V2 | TUT | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,07664 | 0,07582 | 0,08584 | 0,10181 | 0,05825 | €132,94 | €398,81 | €47,86 | €4,29 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.129,53 | €3.388,60 | €48,80 | €-7,80 |
| Bilanciata 1H V3 Filtered | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 76,70334 | 76,47400 | 75,59881 | 51,51908 | 78,91239 | €21,23 | €63,70 | €0,92 | €-0,19 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,53820 | 1,36172 | 1,03934 | 1,91879 | €140,87 | €422,61 | €50,71 | €-2,52 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.575,50 | €4.726,51 | €52,94 | €-10,88 |
| Rapida V1 — score 6–7,5 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.565,59 | €4.696,77 | €52,60 | €-14,04 |
| Rapida V1 — score 6–7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,53820 | 1,32018 | 1,00763 | 1,77024 | €145,36 | €436,08 | €52,33 | €11,05 |
| Rapida score 6–7,5 — senza Trend Up | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.533,61 | €4.600,84 | €51,53 | €-10,59 |
| Rapida score 6–7,5 — senza Trend Up | SOL | LONG | Momentum / breakout | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.523,96 | €4.571,89 | €51,21 | €-13,67 |
| Rapida score 6–7,5 — senza Trend Up | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,53820 | 1,32018 | 1,00763 | 1,77024 | €141,49 | €424,48 | €50,94 | €10,75 |
| Rapida score 6–7,5 — Range Only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.542,02 | €4.626,07 | €51,81 | €-10,65 |
| Rapida score 6–7,5 — Cost Aware | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.591,68 | €4.775,04 | €53,48 | €-10,99 |
| Rapida score 6–7,5 — Cost Aware | SOL | LONG | Momentum / breakout | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.571,68 | €4.715,04 | €52,81 | €-14,10 |
| Rapida score 6–7,5 — Cost Aware | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,53820 | 1,32018 | 1,00763 | 1,77024 | €145,92 | €437,77 | €52,53 | €11,09 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.585,67 | €4.757,02 | €53,28 | €-10,95 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,85717 | 56,40900 | 55,23157 | 37,51740 | 56,79557 | €1.487,57 | €4.462,70 | €49,98 | €44,09 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,54741 | 1,53820 | 1,36172 | 1,03934 | 1,82594 | €139,31 | €417,94 | €50,15 | €-2,49 |
| Rapida V1 — senza PEPE | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €682,89 | €2.048,66 | €50,88 | €0,00 |
| Rapida V1 — senza PEPE | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.518,20 | €4.554,59 | €51,01 | €-10,48 |
| Rapida V1 — senza PEPE | SOL | LONG | Momentum / breakout | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.468,43 | €4.405,28 | €49,34 | €-13,17 |
| Rapida V1 — senza PEPE | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,57311 | 56,40900 | 55,95575 | 37,32661 | 56,50674 | €1.471,68 | €4.415,05 | €0,00 | €66,41 |
| Rapida V1 — target pieno 2R | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 143,59705 | €668,73 | €2.006,20 | €49,82 | €0,00 |
| Rapida V1 — target pieno 2R | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62377,95391 | €1.482,17 | €4.446,51 | €49,80 | €-10,23 |
| Rapida V1 — target pieno 2R | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,31376 | 1,53820 | 1,32599 | 0,88241 | 1,62907 | €133,10 | €399,29 | €0,00 | €68,21 |
| Rapida V1 — target pieno 2R | SOL | LONG | Momentum / breakout | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 78,42149 | €1.442,21 | €4.326,64 | €48,46 | €-12,94 |
| Rapida V1 — target pieno 2R | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,85717 | 56,40900 | 55,23157 | 37,51740 | 57,10837 | €16,71 | €50,14 | €0,56 | €0,50 |
| Rapida 1H V2 | SOL | LONG | Momentum / breakout V2 | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.460,09 | €4.380,26 | €49,06 | €-13,10 |
| Rapida 1H V3 Filtered — madre | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €672,56 | €2.017,68 | €50,11 | €0,00 |
| Rapida 1H V3 Filtered — madre | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.474,48 | €4.423,44 | €49,54 | €-10,18 |
| Rapida V3 — score <7,5 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €685,11 | €2.055,32 | €51,04 | €0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.501,29 | €4.503,87 | €50,44 | €-10,37 |
| Rapida V3 — score <7,5 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.458,14 | €4.374,42 | €48,99 | €-13,08 |
| Rapida V3 — score <7,5 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,53820 | 1,36172 | 1,03934 | 1,82594 | €139,51 | €418,54 | €50,22 | €-2,49 |
| Rapida V3 — no volatilità HIGH | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.489,03 | €4.467,09 | €50,03 | €-10,28 |
| Rapida V3 — Long Only | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €633,63 | €1.900,88 | €47,21 | €0,00 |
| Rapida V3 — Long Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,53820 | 1,28497 | 0,98076 | 1,72303 | €127,65 | €382,94 | €45,95 | €20,46 |
| Rapida V3 — Long + no HIGH + score <7,5 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,53820 | 1,36172 | 1,03934 | 1,82594 | €135,24 | €405,73 | €48,69 | €-2,41 |
| Rapida V3 — senza ESPORTS | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €658,87 | €1.976,61 | €49,09 | €0,00 |
| Rapida V3 — senza ESPORTS | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.444,46 | €4.333,39 | €48,53 | €-9,97 |
| Rapida V3 senza ESPORTS — Long Only | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €665,50 | €1.996,50 | €49,58 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,53820 | 1,28497 | 0,98076 | 1,72303 | €134,07 | €402,21 | €48,26 | €21,49 |
| Rapida V3 senza ESPORTS — MFE Lock | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €676,98 | €2.030,95 | €50,44 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.484,18 | €4.452,53 | €49,87 | €-10,25 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.498,86 | €4.496,57 | €50,36 | €-10,35 |
| Rapida V3 — qualità completa + profit lock | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 76,46529 | 76,47400 | 75,60888 | 51,35919 | 77,74991 | €1.475,52 | €4.426,55 | €49,58 | €0,50 |
| Rapida V3 — qualità completa + profit lock | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,53820 | 1,36172 | 1,03934 | 1,82594 | €136,31 | €408,93 | €49,07 | €-2,43 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,01674 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €-10,32 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,31376 | 1,53820 | 1,31376 | 0,66345 | 1,66060 | €196,52 | €393,04 | €0,00 | €67,14 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,65099 | 1,65600 | 1,61510 | 0,83375 | 1,72995 | €958,49 | €1.916,97 | €41,67 | €5,82 |
| Forza relativa 1H V1 | TUT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,07665 | 0,07582 | 0,08585 | 0,11460 | 0,05642 | €19,11 | €38,22 | €4,59 | €0,42 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Scalp RSI Short 80 · €10 · 15x | ETH | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 1911,02772 | 1907,74000 | 1928,95006 | 2028,87443 | 1884,14420 | €10,00 | €150,00 | €1,41 | €0,26 |
| Scalp RSI Short 75 · €10 · 15x | BTC | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 64092,87886 | 63954,10000 | 64446,89075 | 68045,27306 | 63561,86103 | €10,00 | €150,00 | €0,83 | €0,32 |
| Scalp RSI Short 80 · €50 · 15x | ETH | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 1911,02772 | 1907,74000 | 1928,95006 | 2028,87443 | 1884,14420 | €50,00 | €750,00 | €7,03 | €1,29 |
| Scalp RSI Short 75 · €50 · 15x | BTC | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 64092,87886 | 63954,10000 | 64446,89075 | 68045,27306 | 63561,86103 | €50,00 | €750,00 | €4,14 | €1,62 |
| Scalp RSI Short 80 · prudente · 5x | ETH | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 1911,02772 | 1907,74000 | 1928,95006 | 2283,67812 | 1875,18303 | €211,66 | €1.058,30 | €9,93 | €1,82 |
| Scalp RSI Short 75 · prudente · 5x | BTC | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 64092,87886 | 63954,10000 | 64446,89075 | 76590,99024 | 63384,85508 | €359,25 | €1.796,26 | €9,92 | €3,89 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 63954,10000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.676,44 | €3.352,88 | €53,65 | €-7,72 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 76,70334 | 76,47400 | 75,47608 | 38,73519 | 79,77147 | €1.637,31 | €3.274,63 | €52,39 | €-9,79 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 55,85717 | 56,40900 | 54,96345 | 28,20787 | 58,09146 | €1.637,81 | €3.275,62 | €52,41 | €32,36 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 63954,10000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.636,97 | €3.273,94 | €52,38 | €-7,54 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 76,70334 | 76,47400 | 75,47608 | 38,73519 | 79,77147 | €1.598,77 | €3.197,53 | €51,16 | €-9,56 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 55,85717 | 56,40900 | 54,96345 | 28,20787 | 58,09146 | €1.599,25 | €3.198,50 | €51,18 | €31,60 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 63954,10000 | 65095,57044 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €48,54 | €5,51 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.767,91 | €3.535,81 | €50,92 | €-10,57 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 55,57311 | 56,40900 | 55,88021 | 28,06442 | 57,17362 | €1.736,95 | €3.473,89 | €0,00 | €52,25 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72203 | €1.234,24 | €2.468,49 | €50,77 | €3,00 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63954,10000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €49,45 | €6,24 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07687 | 0,07582 | 0,08610 | 0,11493 | 0,05842 | €186,59 | €373,17 | €44,78 | €5,12 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.628,38 | €3.256,76 | €46,90 | €-9,74 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 55,57311 | 56,40900 | 55,88021 | 28,06442 | 57,17362 | €1.599,86 | €3.199,73 | €0,00 | €48,13 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72203 | €1.136,83 | €2.273,67 | €46,77 | €2,76 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 63954,10000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €6,28 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,07687 | 0,07582 | 0,08610 | 0,11493 | 0,05842 | €191,59 | €383,18 | €45,98 | €5,25 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.628,38 | €3.256,76 | €46,90 | €-9,74 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 55,57311 | 56,40900 | 55,88021 | 28,06442 | 57,17362 | €1.599,86 | €3.199,73 | €0,00 | €48,13 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72203 | €1.136,83 | €2.273,67 | €46,77 | €2,76 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 63954,10000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €6,28 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,07687 | 0,07582 | 0,08610 | 0,11493 | 0,05842 | €191,59 | €383,18 | €45,98 | €5,25 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.628,38 | €3.256,76 | €46,90 | €-9,74 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 55,57311 | 56,40900 | 55,88021 | 28,06442 | 57,17362 | €1.599,86 | €3.199,73 | €0,00 | €48,13 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72203 | €1.136,83 | €2.273,67 | €46,77 | €2,76 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 63954,10000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €6,28 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,07687 | 0,07582 | 0,08610 | 0,11493 | 0,05842 | €191,59 | €383,18 | €45,98 | €5,25 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 79,13330 | €1.745,49 | €3.490,98 | €50,27 | €-10,44 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,33367 | €1.714,92 | €3.429,85 | €49,39 | €51,59 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72884 | €1.218,59 | €2.437,19 | €50,13 | €2,96 |
| Top 5 + BTC — solo MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 79,13330 | €1.636,15 | €3.272,29 | €47,12 | €-9,78 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,33367 | €1.607,49 | €3.214,99 | €46,30 | €48,36 |
| Top 5 + BTC — solo MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72884 | €1.142,26 | €2.284,51 | €46,99 | €2,77 |
| Top 5 + BTC — Guard | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Top 5 + BTC — BTC≤3 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 79,13330 | €1.667,99 | €3.335,98 | €48,04 | €-9,97 |
| Top 5 + BTC — BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,33367 | €1.638,78 | €3.277,56 | €47,20 | €49,30 |
| Top 5 + BTC — BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72884 | €1.164,49 | €2.328,98 | €47,90 | €2,83 |
| Top 5 + BTC — Guard + MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 80,01692 | €1.679,49 | €3.358,97 | €48,37 | €-10,04 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,97387 | €1.650,08 | €3.300,15 | €47,52 | €49,64 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,75605 | €1.172,51 | €2.345,03 | €48,23 | €2,85 |
| Top 5 + BTC — target pieno 3R | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Top 5 + BTC — target pieno 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 80,01692 | €1.680,47 | €3.360,94 | €48,40 | €-10,05 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,97387 | €1.651,04 | €3.302,08 | €47,55 | €49,67 |
| Top 5 + BTC — target pieno 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,75605 | €1.173,20 | €2.346,40 | €48,26 | €2,85 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63807,23600 | 63954,10000 | 64828,15178 | 95391,81782 | 61561,22129 | €1.485,14 | €2.970,29 | €47,52 | €-6,84 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 76,70334 | 76,47400 | 75,47608 | 38,73519 | 79,40330 | €1.318,50 | €2.637,00 | €42,19 | €-7,88 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 55,85717 | 56,40900 | 54,96345 | 28,20787 | 57,82334 | €1.430,77 | €2.861,55 | €45,78 | €28,27 |
| Combo Mean Reversion | HYPE | SHORT | Combo Mean Reversion | 60m | 2,0x | 55,83483 | 56,40900 | 56,50485 | 83,47307 | 54,76280 | €1.968,04 | €3.936,09 | €47,23 | €-40,48 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 79,13330 | €1.645,80 | €3.291,60 | €47,40 | €-9,84 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,33367 | €1.607,82 | €3.215,65 | €46,31 | €48,37 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72884 | €1.148,88 | €2.297,76 | €47,26 | €2,79 |
| Combo Adaptive — madre | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive — madre | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive — madre | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63954,10000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.768,38 | €3.536,76 | €50,93 | €-8,14 |
| Combo Adaptive — madre | SOL | LONG | Combo Adaptive | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.646,09 | €3.292,19 | €47,41 | €-9,84 |
| Combo Adaptive — MFE Trail esistente | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive — MFE Trail esistente | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63954,10000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.608,91 | €3.217,82 | €46,34 | €-7,41 |
| Combo Adaptive — Long Only | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | SOL | LONG | Combo Adaptive | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.690,68 | €3.381,36 | €48,69 | €-10,11 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,85717 | 56,40900 | 55,05283 | 28,20787 | 57,46586 | €1.692,37 | €3.384,75 | €48,74 | €33,44 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 1,65399 | 1,65600 | 1,61997 | 0,83527 | 1,72203 | €1.168,43 | €2.336,87 | €48,07 | €2,84 |
| Combo Adaptive — parziale 1R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive — parziale 1R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive — parziale 1R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63954,10000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.698,08 | €3.396,15 | €48,90 | €-7,82 |
| Combo Adaptive — parziale 1R | SOL | LONG | Combo Adaptive | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.580,65 | €3.161,31 | €45,52 | €-9,45 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63954,10000 | 64726,06020 | 95391,81782 | 61050,76340 | €1.736,70 | €3.473,39 | €50,02 | €-7,99 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SOL | LONG | Combo Adaptive | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 80,01692 | €1.566,12 | €3.132,24 | €45,10 | €-9,37 |
| Combo Adaptive — target pieno 3R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive — target pieno 3R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63954,10000 | 64726,06020 | 95391,81782 | 61050,76340 | €1.704,25 | €3.408,50 | €49,08 | €-7,85 |
| Combo Adaptive — target pieno 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive — target pieno 3R | SOL | LONG | Combo Adaptive | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 80,01692 | €1.536,86 | €3.073,72 | €44,26 | €-9,19 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 63954,10000 | 64993,05773 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €49,29 | €6,22 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63954,10000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €-12,18 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63807,23600 | 63954,10000 | 64623,96862 | 84757,27849 | 62173,77076 | €1.301,67 | €3.905,01 | €49,98 | €-8,99 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63954,10000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €-18,14 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63807,23600 | 63954,10000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.152,72 | €3.458,17 | €49,80 | €-7,96 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 76,70334 | 76,47400 | 75,72153 | 51,51908 | 78,66694 | €1.309,61 | €3.928,82 | €50,29 | €-11,75 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 76,70334 | 76,47400 | 75,59881 | 51,51908 | 78,91239 | €1.125,87 | €3.377,60 | €48,64 | €-10,10 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1910,13195 | 1907,74000 | 1882,62605 | 1282,97196 | 1965,14375 | €1.119,82 | €3.359,45 | €48,38 | €-4,21 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1910,13195 | 1907,74000 | 1882,62605 | 1282,97196 | 1965,14375 | €1.127,99 | €3.383,96 | €48,73 | €-4,24 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07373 | €1.664,53 | €3.329,06 | €47,94 | €-20,18 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 78,66749 | €1.638,36 | €3.276,72 | €47,18 | €0,37 |
| Master Adaptive V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,62907 | €188,60 | €377,20 | €45,26 | €64,44 |
| Master Adaptive V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,65699 | 1,65600 | 1,62026 | 0,83678 | 1,73045 | €37,11 | €74,22 | €1,65 | €-0,04 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,40900 | 55,05283 | 28,20787 | 57,46586 | €24,51 | €49,02 | €0,71 | €0,48 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07373 | €1.665,22 | €3.330,43 | €47,96 | €-20,18 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 78,66749 | €1.639,04 | €3.278,07 | €47,20 | €0,37 |
| Master Adaptive No Alt V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,62907 | €188,68 | €377,35 | €45,28 | €64,47 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 78,66749 | €1.696,58 | €3.393,17 | €48,86 | €0,39 |
| Master Adaptive Expanded V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,62907 | €200,29 | €400,58 | €48,07 | €68,43 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,65600 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €10,18 |
| Master Adaptive Expanded V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07373 | €12,83 | €25,67 | €0,37 | €-0,16 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,57311 | 56,40900 | 54,77286 | 28,06442 | 57,17362 | €34,16 | €68,32 | €0,98 | €1,03 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1915,77308 | 1907,74000 | 1888,18595 | 967,46540 | 1970,94734 | €29,73 | €59,45 | €0,86 | €-0,25 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07373 | €1.642,41 | €3.284,83 | €47,30 | €-19,91 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 78,66749 | €1.616,59 | €3.233,19 | €46,56 | €0,37 |
| Master Adaptive Gb20 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,62907 | €186,09 | €372,19 | €44,66 | €63,58 |
| Master Adaptive Gb20 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,65699 | 1,65600 | 1,62026 | 0,83678 | 1,73045 | €36,62 | €73,23 | €1,62 | €-0,04 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,40900 | 55,05283 | 28,20787 | 57,46586 | €24,18 | €48,37 | €0,70 | €0,48 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07476 | €1.667,40 | €3.334,80 | €48,02 | €-20,21 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 79,76859 | €1.641,18 | €3.282,37 | €47,27 | €0,37 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,78672 | €188,92 | €377,85 | €45,34 | €64,55 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,65699 | 1,65600 | 1,62026 | 0,83678 | 1,76718 | €37,17 | €74,35 | €1,65 | €-0,04 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,40900 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €0,49 |
| Combo Adaptive — Side × Regime Guard | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63954,10000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.842,32 | €3.684,64 | €53,06 | €-8,48 |
| Combo Adaptive — Side × Regime Guard | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive — Side × Regime Guard | SOL | LONG | Combo Adaptive | 60m | 2,0x | 76,70334 | 76,47400 | 75,59881 | 38,73519 | 78,91239 | €1.673,37 | €3.346,75 | €48,19 | €-10,01 |
| Master Adaptive GB20 — Breakeven 0,5R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07373 | €1.672,77 | €3.345,55 | €48,18 | €-20,28 |
| Master Adaptive GB20 — Breakeven 0,5R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 78,66749 | €1.646,47 | €3.292,95 | €47,42 | €0,38 |
| Master Adaptive GB20 — Breakeven 0,5R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,62907 | €189,53 | €379,07 | €45,49 | €64,76 |
| Master Adaptive GB20 — Breakeven 0,5R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,65699 | 1,65600 | 1,62026 | 0,83678 | 1,73045 | €37,29 | €74,59 | €1,65 | €-0,04 |
| Master Adaptive GB20 — Breakeven 0,5R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,40900 | 55,05283 | 28,20787 | 57,46586 | €24,63 | €49,26 | €0,71 | €0,49 |
| Master Adaptive GB20 — 50% a 0,75R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07166 | 0,07123 | 0,07063 | 0,03619 | 0,07373 | €1.670,99 | €3.341,99 | €48,12 | €-20,25 |
| Master Adaptive GB20 — 50% a 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,46529 | 76,47400 | 75,36419 | 38,61497 | 78,66749 | €1.644,72 | €3.289,45 | €47,37 | €0,37 |
| Master Adaptive GB20 — 50% a 0,75R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,53820 | 1,15611 | 0,66345 | 1,62907 | €189,33 | €378,66 | €45,44 | €64,69 |
| Master Adaptive GB20 — 50% a 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,65699 | 1,65600 | 1,62026 | 0,83678 | 1,73045 | €37,25 | €74,51 | €1,65 | €-0,04 |
| Master Adaptive GB20 — 50% a 0,75R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,40900 | 55,05283 | 28,20787 | 57,46586 | €24,61 | €49,21 | €0,71 | €0,49 |
| Master Adaptive GB20 — Loss Cap 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,41728 | 76,47400 | 75,59197 | 38,59073 | 78,61810 | €1.869,62 | €3.739,25 | €40,38 | €2,78 |
| Master Adaptive GB20 — Loss Cap 0,75R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,46019 | 1,53820 | 1,28497 | 0,73740 | 1,92745 | €192,15 | €384,31 | €46,12 | €20,53 |
| Master Adaptive GB20 — Loss Cap 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,65699 | 1,65600 | 1,62945 | 0,83678 | 1,73045 | €1.386,85 | €2.773,69 | €46,11 | €-1,66 |
| Master Adaptive GB20 — Loss Cap 0,75R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,40900 | 55,25391 | 28,20787 | 57,46586 | €543,67 | €1.087,34 | €11,74 | €10,74 |
| Rapida V3 NoHigh — Range Only | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.566,03 | €4.698,09 | €52,62 | €-10,81 |
| Rapida V3 NoHigh — Range Only | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €143,18 | €429,53 | €51,54 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.581,87 | €4.745,62 | €53,15 | €-10,92 |
| Rapida V3 NoHigh — Regime Guard | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €144,63 | €433,88 | €52,07 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 76,70334 | 76,47400 | 75,84426 | 51,51908 | 77,99195 | €1.486,99 | €4.460,97 | €49,96 | €-13,34 |
| Rapida V3 NoHigh — Regime Guard | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54541 | 1,53820 | 1,35996 | 1,03800 | 1,82358 | €144,27 | €432,81 | €51,94 | €-2,02 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01674 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €-13,91 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Combo Trend — Side × Regime Guard | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend — Side × Regime Guard | SOL | LONG | Combo Trend | 60m | 2,0x | 76,70334 | 76,47400 | 75,47608 | 38,73519 | 79,40330 | €1.567,67 | €3.135,35 | €50,17 | €-9,37 |
| Combo Trend — Side × Regime Guard | HYPE | LONG | Combo Trend | 60m | 2,0x | 55,85717 | 56,40900 | 54,96345 | 28,20787 | 57,82334 | €1.567,38 | €3.134,75 | €50,16 | €30,97 |
| Combo Trend — Side × Regime Guard | ETH | LONG | Combo Trend | 60m | 2,0x | 1910,13195 | 1907,74000 | 1879,56984 | 964,61663 | 1977,36859 | €1.571,14 | €3.142,28 | €50,28 | €-3,93 |
| FAST NoHigh <7,5 · SHORT only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63954,10000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.546,22 | €4.638,65 | €51,95 | €-10,68 |
| Bilanciata V3 · LONG only | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 63954,10000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.068,36 | €3.205,08 | €46,15 | €-7,38 |
| Bilanciata V3 · LONG only | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 76,70334 | 76,47400 | 75,59881 | 51,51908 | 78,91239 | €20,08 | €60,25 | €0,87 | €-0,18 |
| Bilanciata V3 · LONG only | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,53820 | 1,36172 | 1,03934 | 1,91879 | €133,24 | €399,72 | €47,97 | €-2,38 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63954,10000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €49,84 | €6,28 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07687 | 0,07582 | 0,08610 | 0,11493 | 0,05842 | €188,03 | €376,07 | €45,13 | €5,16 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63954,10000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €49,91 | €6,29 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07687 | 0,07582 | 0,08610 | 0,11493 | 0,05842 | €188,32 | €376,64 | €45,20 | €5,16 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive GB20 — Loss Cap 0,75R | DOGE | LONG | 2026-08-12T13:24:12+00:00 | 0,07124 | €-46,14 | -1,14 | STOP |
| Rapida V3 senza ESPORTS — Stress Guard | SOL | LONG | 2026-08-12T13:09:00+00:00 | 76,45000 | €-6,34 | -0,13 | STOP |
| Rapida V3 senza ESPORTS — Long Only | SOL | LONG | 2026-08-12T13:09:00+00:00 | 76,45000 | €-6,29 | -0,13 | STOP |
| Rapida V3 — Long Only | SOL | LONG | 2026-08-12T13:09:00+00:00 | 76,45000 | €-5,99 | -0,13 | STOP |
| Rapida V3 — Long + no HIGH + score <7,5 | SOL | LONG | 2026-08-12T13:09:00+00:00 | 76,45000 | €-6,30 | -0,13 | STOP |
| Btc Bollinger 1H | BTC | LONG | 2026-08-12T12:54:09+00:00 | 63990,53505 | €27,44 | 0,54 | STOP |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | 2026-08-12T12:54:09+00:00 | 64013,32751 | €26,51 | 0,57 | STOP |
| Bilanciata 1H V1 | BTC | SHORT | 2026-08-12T12:54:09+00:00 | 64472,16750 | €-55,88 | -1,09 | STOP |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | 2026-08-12T11:39:15+00:00 | 487,15032 | €-53,07 | -1,08 | STOP |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | 2026-08-12T11:39:15+00:00 | 487,15032 | €-53,15 | -1,08 | STOP |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | 2026-08-12T11:39:15+00:00 | 487,15032 | €-52,66 | -1,08 | STOP |
| Scanner Bottom20 Short | ZEC | SHORT | 2026-08-12T11:39:15+00:00 | 487,15032 | €-53,52 | -1,08 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 300/30 | 33/30 | 0,70 | 2,04 | -0,16R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 271/30 | 20/30 | 0,58 | 1,90 | -0,23R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 169/30 | 22/30 | 0,78 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 172/30 | 22/30 | 0,77 | 1,57 | -0,12R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 232/30 | 31/30 | 0,77 | 0,62 | -0,12R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 205/30 | 11/30 | 0,69 | 0,00 | -0,16R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 108/30 | 8/30 | 0,58 | 1,02 | -0,23R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 211/30 | 17/30 | 0,52 | 4,50 | -0,29R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 319/30 | 24/30 | 0,68 | 0,64 | -0,17R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 288/30 | 7/30 | 0,57 | 0,02 | -0,23R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 232/30 | 30/30 | 0,81 | 1,02 | -0,10R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 418/30 | 55/30 | 0,81 | 1,12 | -0,09R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 108/30 | 15/30 | 0,44 | 0,99 | -0,38R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 371/30 | 44/30 | 0,69 | 1,20 | -0,16R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 375/30 | 37/30 | 0,69 | 0,76 | -0,16R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 340/30 | 23/30 | 0,58 | 1,12 | -0,22R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 215/30 | 40/30 | 0,68 | 0,78 | -0,20R | €-7,08 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 19/30 | 0,00 | 1,61 | 0,00R | €13,96 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 23/30 | 14/30 | 0,47 | 0,61 | -0,32R | €-2,07 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 36/30 | 23/30 | 0,44 | 0,39 | -0,33R | €-3,41 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 536/30 | 89/30 | 0,90 | 1,04 | -0,06R | €0,73 | 5,46% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 28/30 | 0,00 | 0,43 | 0,00R | €-19,27 | 6,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 2/30 | 0,00 | 0,00 | 0,00R | €-28,31 | 1,11% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 190/30 | 51/30 | 1,05 | 0,87 | 0,03R | €-2,81 | 5,20% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 331/30 | 77/30 | 0,91 | 1,16 | -0,05R | €3,36 | 4,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 252/30 | 33/30 | 0,78 | 0,60 | -0,12R | €-9,00 | 4,02% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 167/30 | 25/30 | 0,97 | 0,99 | -0,01R | €-0,14 | 2,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 340/30 | 51/30 | 0,82 | 1,07 | -0,09R | €1,26 | 4,71% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 407/30 | 87/30 | 0,87 | 1,17 | -0,07R | €3,69 | 4,71% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 538/30 | 85/30 | 0,79 | 1,03 | -0,11R | €0,68 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 48/30 | 0,00 | 1,63 | 0,00R | €11,22 | 2,44% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 48/30 | 0,00 | 1,21 | 0,00R | €4,55 | 3,20% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 25/30 | 0,00 | 1,46 | 0,00R | €11,46 | 2,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 318/30 | 90/30 | 0,87 | 1,29 | -0,07R | €5,53 | 2,55% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 502/30 | 94/30 | 0,74 | 0,89 | -0,14R | €-2,36 | 3,79% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 42/30 | 22/30 | 0,54 | 0,72 | -0,28R | €-7,53 | 3,38% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 526/30 | 113/30 | 0,82 | 0,87 | -0,10R | €-2,90 | 6,75% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 384/30 | 83/30 | 0,81 | 1,04 | -0,10R | €0,90 | 5,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 210/30 | 55/30 | 0,94 | 0,86 | -0,03R | €-3,47 | 4,39% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 214/30 | 51/30 | 0,93 | 0,80 | -0,04R | €-5,15 | 4,70% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 290/30 | 64/30 | 0,87 | 0,54 | -0,07R | €-12,96 | 9,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 26/30 | 0,00 | 1,59 | 0,00R | €12,31 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 34/30 | 0,00 | 1,78 | 0,00R | €12,49 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 422/30 | 78/30 | 0,79 | 0,81 | -0,11R | €-4,97 | 5,51% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 44/30 | 0,00 | 0,68 | 0,00R | €-8,36 | 7,45% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 69/30 | 0,00 | 0,81 | 0,00R | €-3,83 | 6,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 27/30 | 0,00 | 0,81 | 0,00R | €-4,79 | 3,63% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 479/30 | 87/30 | 0,77 | 0,74 | -0,12R | €-6,03 | 6,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 198/30 | 34/30 | 0,67 | 0,86 | -0,23R | €-3,68 | 4,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 161/30 | 60/30 | 1,10 | 0,79 | 0,05R | €-5,55 | 5,92% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 9/30 | 4/30 | 0,59 | 0,63 | -0,20R | €-10,11 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 7/30 | 5/30 | 5,58 | 3,42 | 0,74R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 13/30 | 5/30 | 0,24 | 0,97 | -0,59R | €-0,63 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 4/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 13/30 | 7/30 | 0,78 | 0,48 | -0,13R | €-20,19 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,23% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 434/30 | 53/30 | 0,96 | 0,93 | -0,02R | €-1,19 | 4,13% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 232/30 | 26/30 | 0,92 | 0,56 | -0,04R | €-10,06 | 3,53% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 449/30 | 67/30 | 0,96 | 0,40 | -0,02R | €-14,19 | 9,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 375/30 | 54/30 | 0,90 | 0,58 | -0,05R | €-8,48 | 4,94% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 43/30 | 11/30 | 1,55 | 0,71 | 0,22R | €-7,09 | 1,95% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 43/30 | 11/30 | 1,43 | 0,31 | 0,17R | €-18,43 | 2,32% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 119/30 | 31/30 | 0,90 | 0,83 | -0,05R | €-3,27 | 2,88% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 157/30 | 22/30 | 0,83 | 0,79 | -0,09R | €-4,40 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 60/30 | 0,74 | 0,80 | -0,20R | €-3,91 | 5,15% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 48/30 | 0,00 | 1,30 | 0,00R | €5,06 | 4,12% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 41/30 | 0,74 | 0,53 | -0,20R | €-10,18 | 5,15% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 79/30 | 26/30 | 1,24 | 0,81 | 0,11R | €-6,15 | 4,44% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_SCANNER | Combo Scanner | 266/30 | 58/30 | 1,09 | 0,65 | 0,05R | €-9,71 | 7,59% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 359/30 | 80/30 | 0,88 | 0,68 | -0,07R | €-9,22 | 9,62% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 38/30 | 0,00 | 1,06 | 0,00R | €0,99 | 2,89% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 7/30 | 5/30 | 1,03 | 0,44 | 0,02R | €-18,63 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 10/30 | 8/30 | 0,69 | 1,03 | -0,21R | €0,60 | 1,30% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 16/30 | 11/30 | 0,43 | 1,18 | -0,40R | €3,61 | 1,44% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 179/30 | 52/30 | 0,78 | 1,39 | -0,14R | €9,55 | 3,39% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 109/30 | 20/30 | 0,71 | 1,63 | -0,17R | €12,47 | 3,39% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 364/30 | 56/30 | 0,85 | 0,58 | -0,09R | €-10,26 | 6,66% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 13/30 | 7/30 | 0,33 | 0,06 | -0,51R | €-36,31 | 2,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 12/30 | 6/30 | 0,31 | 0,34 | -0,58R | €-30,47 | 2,06% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 18/30 | 9/30 | 0,34 | 0,14 | -0,49R | €-36,09 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 10/30 | 14/30 | 1,24 | 0,39 | 0,13R | €-19,26 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 210/30 | 28/30 | 0,99 | 0,64 | -0,01R | €-13,12 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 27/30 | 0,00 | 0,45 | 0,00R | €-17,61 | 6,51% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 28/30 | 0,00 | 0,32 | 0,00R | €-29,66 | 9,72% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 22/30 | 0,00 | 0,41 | 0,00R | €-22,07 | 6,10% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 391/30 | 59/30 | 1,35 | 0,46 | 0,12R | €-10,99 | 7,16% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 184/30 | 24/30 | 0,98 | 0,48 | -0,01R | €-21,60 | 5,87% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 191/30 | 26/30 | 0,95 | 0,50 | -0,03R | €-19,46 | 5,75% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 133/30 | 32/30 | 0,95 | 0,40 | -0,03R | €-27,25 | 8,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 204/30 | 24/30 | 0,94 | 0,48 | -0,04R | €-21,76 | 5,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 452/30 | 68/30 | 0,83 | 0,65 | -0,10R | €-8,37 | 7,87% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 181/30 | 63/30 | 1,13 | 0,82 | 0,07R | €-5,96 | 8,06% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 148/30 | 43/30 | 0,50 | 0,76 | -0,29R | €-5,39 | 4,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 148/30 | 43/30 | 0,50 | 0,76 | -0,29R | €-5,39 | 4,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 148/30 | 43/30 | 0,50 | 0,76 | -0,29R | €-5,39 | 4,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 182/30 | 63/30 | 0,73 | 0,71 | -0,15R | €-6,16 | 5,83% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 167/30 | 35/30 | 0,72 | 0,62 | -0,13R | €-8,54 | 4,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 147/30 | 36/30 | 0,63 | 0,57 | -0,18R | €-8,71 | 4,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 202/30 | 29/30 | 0,97 | 0,29 | -0,02R | €-22,86 | 8,29% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 203/30 | 29/30 | 0,96 | 0,29 | -0,02R | €-22,86 | 8,29% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 203/30 | 29/30 | 0,96 | 0,29 | -0,02R | €-22,86 | 8,29% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 257/30 | 48/30 | 1,10 | 1,01 | 0,05R | €0,18 | 5,97% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 124/30 | 10/30 | 0,87 | 0,87 | -0,07R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 211/30 | 29/30 | 0,91 | 0,51 | -0,05R | €-15,03 | 6,44% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 219/30 | 41/30 | 1,16 | 0,51 | 0,07R | €-13,76 | 5,64% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 185/30 | 26/30 | 1,01 | 0,55 | 0,01R | €-15,36 | 6,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 229/30 | 48/30 | 1,17 | 0,46 | 0,07R | €-15,34 | 7,43% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 192/30 | 31/30 | 1,02 | 0,48 | 0,01R | €-16,64 | 5,97% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 262/30 | 41/30 | 1,06 | 0,38 | 0,03R | €-15,09 | 7,03% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 207/30 | 37/30 | 0,96 | 0,64 | -0,02R | €-10,00 | 6,99% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 197/30 | 33/30 | 0,97 | 0,64 | -0,02R | €-11,04 | 6,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 281/30 | 57/30 | 1,10 | 1,10 | 0,05R | €2,40 | 6,80% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 19/30 | 8/30 | 0,41 | 0,20 | -0,48R | €-34,06 | 3,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 2/30 | 2/30 | 1,18 | 0,65 | 0,10R | €-8,96 | 0,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 11/30 | 5/30 | 0,61 | 0,82 | -0,24R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 12/30 | 5/30 | 0,68 | 1,95 | -0,24R | €11,56 | 1,09% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 2/30 | 2/30 | 1,29 | 0,71 | 0,15R | €-7,50 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 18/30 | 8/30 | 0,54 | 0,43 | -0,36R | €-23,29 | 2,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,05R | €-51,41 | 1,57% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07123**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 28.9 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63954.1 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07166**; close **0.0713**; wick alta **4.2%**; volume **x5.13**

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

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **87,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +1.77%, 82% oltre +1%.
- BTC trend score: **1,00**; ADX: **27,49**; breadth sopra EMA50: **66,67%**
- Mediana alt vs BTC: **1,77%**; dispersione: **8,72%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **23**
- Posizioni research aperte: **406**
- Trade research chiusi: **20531**
- Eventi di mercato indipendenti chiusi: **2953**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **53818**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 2 | 300 | 300 | 30,33% | 0,70 | -0,16R | €-468,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 2 | 271 | 271 | 29,15% | 0,58 | -0,23R | €-609,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 3 | 169 | 169 | 45,56% | 0,78 | -0,12R | €-204,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 2 | 172 | 172 | 33,14% | 0,77 | -0,12R | €-198,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 2 | 232 | 232 | 31,90% | 0,77 | -0,12R | €-281,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 2 | 205 | 205 | 32,20% | 0,69 | -0,16R | €-324,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 108 | 108 | 31,48% | 0,58 | -0,23R | €-249,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 3 | 211 | 211 | 26,54% | 0,52 | -0,29R | €-609,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 3 | 319 | 319 | 29,47% | 0,68 | -0,17R | €-544,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 3 | 288 | 288 | 28,12% | 0,57 | -0,23R | €-672,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 2 | 232 | 232 | 32,76% | 0,81 | -0,10R | €-222,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 2 | 418 | 418 | 40,43% | 0,81 | -0,09R | €-376,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 108 | 108 | 26,85% | 0,44 | -0,38R | €-414,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 2 | 371 | 371 | 29,38% | 0,69 | -0,16R | €-602,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 2 | 375 | 375 | 29,33% | 0,69 | -0,16R | €-602,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 2 | 340 | 340 | 27,94% | 0,58 | -0,22R | €-753,74 |
| MAIN | 11 | 215 | 215 | 25,12% | 0,68 | -0,20R | €-421,52 |
| RSI_EXTREME_LONG_15M | 0 | 23 | 23 | 39,13% | 0,47 | -0,32R | €-73,08 |
| RSI_EXTREME_SHORT_15M | 3 | 36 | 36 | 33,33% | 0,44 | -0,33R | €-119,37 |
| Bilanciata 1H V1 | 14 | 536 | 536 | 33,77% | 0,90 | -0,06R | €-299,37 |
| Bilanciata 1H V2 | 7 | 217 | 190 | 36,87% | 1,05 | 0,03R | €55,60 |
| Bilanciata 1H V3 Filtered | 9 | 331 | 331 | 33,84% | 0,91 | -0,05R | €-169,31 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 9 | 252 | 252 | 32,14% | 0,78 | -0,12R | €-314,66 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 3 | 167 | 167 | 37,72% | 0,97 | -0,01R | €-23,09 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 7 | 340 | 340 | 34,71% | 0,82 | -0,09R | €-303,93 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 7 | 407 | 407 | 36,12% | 0,87 | -0,07R | €-269,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 5 | 538 | 538 | 34,20% | 0,79 | -0,11R | €-616,53 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 3 | 318 | 318 | 35,85% | 0,87 | -0,07R | €-220,80 |
| SHADOW_1H_FAST_TP2_V1 | 6 | 502 | 502 | 30,88% | 0,74 | -0,14R | €-709,23 |
| Rapida 1H V2 | 1 | 50 | 42 | 32,00% | 0,54 | -0,28R | €-139,96 |
| Rapida 1H V3 Filtered | 2 | 526 | 526 | 34,98% | 0,82 | -0,10R | €-507,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 2 | 384 | 384 | 34,90% | 0,81 | -0,10R | €-383,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 210 | 210 | 47,62% | 0,94 | -0,03R | €-60,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 214 | 214 | 37,85% | 0,93 | -0,04R | €-76,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 290 | 290 | 36,55% | 0,87 | -0,07R | €-202,14 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 3 | 422 | 422 | 34,12% | 0,79 | -0,11R | €-482,56 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 2 | 479 | 479 | 33,82% | 0,77 | -0,12R | €-589,61 |
| SHADOW_4H_WIDE | 24 | 198 | 198 | 19,70% | 0,67 | -0,23R | €-458,12 |
| SHADOW_BOLLINGER_MR_1H | 1 | 161 | 161 | 47,20% | 1,10 | 0,05R | €73,11 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 9 | 9 | 55,56% | 0,59 | -0,20R | €-18,05 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 7 | 7 | 85,71% | 5,58 | 0,74R | €51,91 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 13 | 13 | 30,77% | 0,24 | -0,59R | €-76,75 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,93 |
| SHADOW_BTC_EMA_1H | 1 | 13 | 13 | 46,15% | 0,78 | -0,13R | €-17,00 |
| SHADOW_BTC_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 10 | 434 | 434 | 36,64% | 0,96 | -0,02R | €-89,05 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 232 | 232 | 35,34% | 0,92 | -0,04R | €-96,84 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 9 | 449 | 449 | 40,76% | 0,96 | -0,02R | €-76,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 10 | 375 | 375 | 38,67% | 0,90 | -0,05R | €-193,98 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 43 | 43 | 48,84% | 1,55 | 0,22R | €92,56 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 43 | 43 | 37,21% | 1,43 | 0,17R | €72,42 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 0 | 119 | 119 | 31,93% | 0,90 | -0,05R | €-57,83 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 2 | 157 | 157 | 34,39% | 0,83 | -0,09R | €-138,48 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 79 | 79 | 49,37% | 1,24 | 0,11R | €85,71 |
| SHADOW_COMBO_SCANNER | 7 | 266 | 266 | 35,34% | 1,09 | 0,05R | €136,04 |
| SHADOW_COMBO_TREND | 11 | 359 | 359 | 30,64% | 0,88 | -0,07R | €-240,73 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 7 | 7 | 57,14% | 1,03 | 0,02R | €1,06 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 10 | 10 | 40,00% | 0,69 | -0,21R | €-21,12 |
| SHADOW_DOGE_EMA_1H | 0 | 16 | 16 | 25,00% | 0,43 | -0,40R | €-63,80 |
| SHADOW_DONCHIAN_1H | 6 | 179 | 179 | 28,49% | 0,78 | -0,14R | €-251,58 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 6 | 109 | 109 | 30,28% | 0,71 | -0,17R | €-186,50 |
| SHADOW_EMA_TREND_1H | 8 | 364 | 364 | 29,67% | 0,85 | -0,09R | €-310,05 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 13 | 13 | 30,77% | 0,33 | -0,51R | €-66,79 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 12 | 12 | 25,00% | 0,31 | -0,58R | €-70,11 |
| SHADOW_ETH_EMA_1H | 1 | 18 | 18 | 33,33% | 0,34 | -0,49R | €-87,95 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 0 | 10 | 10 | 50,00% | 1,24 | 0,13R | €13,30 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 9 | 210 | 210 | 32,38% | 0,99 | -0,01R | €-10,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 391 | 391 | 65,73% | 1,35 | 0,12R | €456,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 7 | 184 | 184 | 32,07% | 0,98 | -0,01R | €-19,80 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 9 | 191 | 191 | 29,84% | 0,95 | -0,03R | €-58,39 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 3 | 133 | 133 | 31,58% | 0,95 | -0,03R | €-45,77 |
| SHADOW_MASTER_ADAPTIVE_V1 | 9 | 204 | 204 | 31,37% | 0,94 | -0,04R | €-76,64 |
| Forza relativa 1H V1 | 11 | 452 | 452 | 28,76% | 0,83 | -0,10R | €-435,16 |
| Forza relativa 1H V2 | 3 | 195 | 181 | 35,90% | 1,13 | 0,07R | €139,98 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 5 | 148 | 148 | 27,03% | 0,50 | -0,29R | €-422,06 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 5 | 148 | 148 | 27,03% | 0,50 | -0,29R | €-422,06 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 5 | 148 | 148 | 27,03% | 0,50 | -0,29R | €-422,06 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 5 | 182 | 182 | 30,22% | 0,73 | -0,15R | €-270,66 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 4 | 167 | 167 | 49,70% | 0,72 | -0,13R | €-220,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 5 | 147 | 147 | 48,30% | 0,63 | -0,18R | €-260,78 |
| SHADOW_SCANNER_TOP10_LONG | 8 | 202 | 202 | 34,65% | 0,97 | -0,02R | €-31,36 |
| SHADOW_SCANNER_TOP15_LONG | 8 | 203 | 203 | 34,48% | 0,96 | -0,02R | €-42,47 |
| SHADOW_SCANNER_TOP20_LONG | 8 | 203 | 203 | 34,48% | 0,96 | -0,02R | €-42,47 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 257 | 257 | 34,63% | 1,10 | 0,05R | €135,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 1 | 124 | 124 | 31,45% | 0,87 | -0,07R | €-90,72 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 6 | 211 | 211 | 32,23% | 0,91 | -0,05R | €-107,41 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 1 | 219 | 219 | 44,75% | 1,16 | 0,07R | €158,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 2 | 185 | 185 | 33,51% | 1,01 | 0,01R | €12,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 2 | 229 | 229 | 44,54% | 1,17 | 0,07R | €169,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 3 | 192 | 192 | 33,33% | 1,02 | 0,01R | €23,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 6 | 262 | 262 | 42,75% | 1,06 | 0,03R | €71,48 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 207 | 207 | 31,40% | 0,96 | -0,02R | €-47,32 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 197 | 197 | 30,96% | 0,97 | -0,02R | €-31,14 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 281 | 281 | 36,30% | 1,10 | 0,05R | €146,97 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 19 | 19 | 26,32% | 0,41 | -0,48R | €-91,68 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,93 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 11 | 11 | 45,45% | 0,61 | -0,24R | €-26,43 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 12 | 12 | 33,33% | 0,68 | -0,24R | €-28,92 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 2 | 2 | 50,00% | 1,29 | 0,15R | €3,02 |
| SHADOW_SOL_EMA_1H | 0 | 18 | 18 | 27,78% | 0,54 | -0,36R | €-65,49 |
| SHADOW_SOL_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,62 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 36 | 36 | 22,22% | 0,48 | -0,32R | €-116,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 1 | 45 | 45 | 42,22% | 1,30 | 0,13R | €60,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 102 | 102 | 34,31% | 0,67 | -0,17R | €-168,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,22 | -0,53R | €-42,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 31 | 31 | 35,48% | 1,17 | 0,09R | €26,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 20 | 20 | 30,00% | 0,42 | -0,36R | €-71,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 51 | 51 | 17,65% | 0,47 | -0,27R | €-136,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 35 | 35 | 20,00% | 0,30 | -0,49R | €-170,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 1 | 32 | 32 | 43,75% | 1,38 | 0,15R | €48,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 97 | 97 | 32,99% | 0,51 | -0,25R | €-242,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,17 | -0,64R | €-44,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 30 | 30 | 36,67% | 1,33 | 0,16R | €48,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 17 | 17 | 29,41% | 0,38 | -0,37R | €-63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 48 | 48 | 16,67% | 0,31 | -0,37R | €-177,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,78 | -0,12R | €-7,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 1 | 40 | 40 | 57,50% | 1,40 | 0,17R | €68,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 60 | 60 | 38,33% | 0,45 | -0,35R | €-207,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 14 | 14 | 50,00% | 1,19 | 0,10R | €13,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 11 | 11 | 45,45% | 0,46 | -0,30R | €-32,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 37 | 37 | 43,24% | 0,85 | -0,08R | €-28,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 1,08 | 0,04R | €1,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 1 | 42 | 42 | 42,86% | 1,33 | 0,15R | €61,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 63 | 63 | 30,16% | 0,41 | -0,35R | €-218,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 14 | 14 | 35,71% | 1,30 | 0,14R | €18,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 11 | 11 | 36,36% | 0,64 | -0,23R | €-25,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 1 | 36 | 36 | 25,00% | 0,82 | -0,07R | €-26,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 1 | 46 | 46 | 39,13% | 1,09 | 0,05R | €21,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 75 | 75 | 32,00% | 0,58 | -0,24R | €-181,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 20 | 20 | 35,00% | 1,46 | 0,19R | €38,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,86 | -0,08R | €-11,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 1 | 54 | 54 | 29,63% | 0,81 | -0,09R | €-49,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,18 | -0,48R | €-43,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 1 | 38 | 38 | 39,47% | 1,13 | 0,06R | €22,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 66 | 66 | 33,33% | 0,47 | -0,29R | €-190,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,92R | €-55,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 19 | 19 | 36,84% | 1,81 | 0,31R | €58,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 13 | 13 | 46,15% | 0,92 | -0,05R | €-6,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 1 | 49 | 49 | 28,57% | 0,56 | -0,21R | €-101,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 106 | 106 | 31,13% | 0,56 | -0,24R | €-258,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 1 | 47 | 47 | 31,91% | 0,77 | -0,13R | €-61,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 94 | 94 | 30,85% | 0,59 | -0,23R | €-215,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 15 | 15 | 13,33% | 0,35 | -0,49R | €-73,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 22 | 22 | 31,82% | 0,53 | -0,29R | €-63,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,14 | -0,67R | €-161,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 53 | 53 | 35,85% | 1,04 | 0,02R | €8,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 123 | 123 | 32,52% | 0,65 | -0,19R | €-229,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 22 | 22 | 22,73% | 0,70 | -0,16R | €-34,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 70 | 70 | 24,29% | 0,66 | -0,17R | €-118,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,09 | -0,71R | €-171,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 1 | 41 | 41 | 36,59% | 1,01 | 0,00R | €1,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 116 | 116 | 31,03% | 0,54 | -0,24R | €-281,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 21 | 21 | 23,81% | 0,77 | -0,11R | €-23,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 21 | 21 | 38,10% | 0,81 | -0,10R | €-21,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 65 | 65 | 23,08% | 0,47 | -0,27R | €-175,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 1 | 47 | 47 | 40,43% | 1,18 | 0,09R | €40,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 75 | 75 | 34,67% | 0,71 | -0,16R | €-121,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 20 | 20 | 35,00% | 1,46 | 0,19R | €38,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,86 | -0,08R | €-11,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 1 | 54 | 54 | 29,63% | 0,81 | -0,09R | €-49,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 0 | 53 | 53 | 32,08% | 0,42 | -0,35R | €-184,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 1 | 57 | 57 | 47,37% | 1,01 | 0,00R | €1,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 138 | 138 | 37,68% | 0,82 | -0,08R | €-112,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 18 | 18 | 33,33% | 0,47 | -0,34R | €-61,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 35 | 35 | 48,57% | 1,33 | 0,12R | €41,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 30 | 30 | 50,00% | 0,99 | -0,01R | €-1,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 80 | 80 | 41,25% | 0,85 | -0,07R | €-56,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 15 | 15 | 26,67% | 0,68 | -0,24R | €-35,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 1 | 43 | 43 | 34,88% | 0,45 | -0,34R | €-144,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,76 | 0,41R | €8,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 8 | 8 | 37,50% | 0,75 | -0,10R | €-8,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 51 | 51 | 35,29% | 1,00 | -0,00R | €-0,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 120 | 120 | 32,50% | 0,65 | -0,19R | €-228,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,35 | -0,42R | €-76,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 32 | 32 | 37,50% | 1,50 | 0,21R | €67,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 69 | 69 | 23,19% | 0,60 | -0,20R | €-138,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 53 | 53 | 35,85% | 1,04 | 0,02R | €8,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 121 | 121 | 32,23% | 0,64 | -0,20R | €-238,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,35 | -0,42R | €-76,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 32 | 32 | 37,50% | 1,50 | 0,21R | €67,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 69 | 69 | 23,19% | 0,60 | -0,20R | €-138,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,26 | -0,48R | €-230,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 1 | 41 | 41 | 36,59% | 1,01 | 0,00R | €1,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 0 | 115 | 115 | 30,43% | 0,47 | -0,28R | €-325,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,36 | -0,44R | €-61,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 31 | 31 | 38,71% | 1,76 | 0,31R | €94,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 21 | 21 | 38,10% | 0,81 | -0,10R | €-21,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 64 | 64 | 21,88% | 0,39 | -0,31R | €-200,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,89 | -0,05R | €-10,79 |
| MAIN | ALT_ROTATION_UP | 4 | 35 | 35 | 20,00% | 0,37 | -0,44R | €-155,32 |
| MAIN | RANGE | 4 | 67 | 67 | 19,40% | 0,55 | -0,30R | €-200,10 |
| MAIN | RANGE_HIGH_VOL | 0 | 10 | 10 | 30,00% | 1,06 | 0,03R | €2,61 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 21 | 21 | 23,81% | 0,52 | -0,35R | €-74,24 |
| MAIN | TREND_DOWN | 0 | 15 | 15 | 26,67% | 0,72 | -0,15R | €-22,75 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 2 | 37 | 37 | 29,73% | 0,96 | -0,02R | €-8,04 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,42 | 0,25R | €17,52 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 12 | 12 | 25,00% | 0,11 | -0,70R | €-84,45 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 4 | 4 | 75,00% | 5,55 | 0,50R | €20,01 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 3 | 10 | 10 | 30,00% | 0,22 | -0,48R | €-48,02 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 21,43% | 0,44 | -0,39R | €-221,17 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 7 | 68 | 68 | 36,76% | 1,06 | 0,03R | €23,51 |
| Bilanciata 1H V1 | RANGE | 3 | 157 | 157 | 38,85% | 1,05 | 0,03R | €44,69 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 27 | 27 | 18,52% | 0,35 | -0,49R | €-131,16 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,24 | 0,13R | €91,68 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 29 | 29 | 34,48% | 0,78 | -0,11R | €-32,03 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 3 | 106 | 106 | 31,13% | 0,93 | -0,04R | €-39,42 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 5 | 48 | 42 | 37,50% | 1,10 | 0,05R | €25,84 |
| Bilanciata 1H V2 | RANGE | 2 | 114 | 102 | 34,21% | 0,81 | -0,11R | €-130,25 |
| Bilanciata 1H V2 | TRANSITION | 0 | 55 | 46 | 41,82% | 1,60 | 0,29R | €160,00 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 42 | 42 | 26,19% | 0,54 | -0,30R | €-128,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 2 | 38 | 38 | 31,58% | 1,17 | 0,09R | €35,03 |
| Bilanciata 1H V3 Filtered | RANGE | 3 | 105 | 105 | 40,00% | 1,06 | 0,03R | €31,58 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 7 | 7 | 28,57% | 0,50 | -0,37R | €-26,19 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 37 | 37 | 35,14% | 1,09 | 0,05R | €19,63 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 22 | 22 | 31,82% | 0,29 | -0,44R | €-95,77 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 60 | 60 | 31,67% | 1,06 | 0,03R | €19,01 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 19,35% | 0,26 | -0,52R | €-161,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 36 | 36 | 33,33% | 1,31 | 0,16R | €56,03 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 3 | 83 | 83 | 37,35% | 0,81 | -0,10R | €-84,57 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 5 | 5 | 40,00% | 0,83 | -0,11R | €-5,36 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 29 | 29 | 34,48% | 1,09 | 0,05R | €13,94 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 23 | 23 | 30,43% | 0,27 | -0,46R | €-106,88 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 2 | 39 | 39 | 25,64% | 0,78 | -0,11R | €-41,83 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,25 | -0,50R | €-54,74 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 2 | 40 | 40 | 50,00% | 1,44 | 0,17R | €66,26 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 41 | 41 | 36,59% | 0,92 | -0,04R | €-18,41 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 1 | 48 | 48 | 31,25% | 0,80 | -0,08R | €-37,28 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 15,79% | 0,25 | -0,52R | €-99,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 2 | 54 | 54 | 46,30% | 1,16 | 0,07R | €38,30 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 3 | 132 | 132 | 35,61% | 0,82 | -0,09R | €-122,76 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 29 | 29 | 31,03% | 0,74 | -0,13R | €-39,11 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,76 | -0,13R | €-41,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 2 | 71 | 71 | 28,17% | 0,74 | -0,12R | €-83,53 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 18,92% | 0,33 | -0,49R | €-181,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 55 | 55 | 47,27% | 1,22 | 0,09R | €52,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 3 | 162 | 162 | 40,12% | 1,03 | 0,01R | €22,43 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 31 | 31 | 35,48% | 0,94 | -0,03R | €-9,42 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,76 | -0,13R | €-41,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 2 | 87 | 87 | 27,59% | 0,65 | -0,18R | €-155,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 77 | 77 | 20,78% | 0,38 | -0,43R | €-330,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 2 | 62 | 62 | 40,32% | 0,93 | -0,04R | €-22,31 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 185 | 185 | 36,76% | 0,83 | -0,09R | €-173,37 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 20 | 20 | 40,00% | 0,96 | -0,02R | €-4,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 1,30 | 0,13R | €56,90 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 38 | 38 | 36,84% | 0,80 | -0,11R | €-41,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 2 | 102 | 102 | 28,43% | 0,70 | -0,16R | €-159,27 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 22,73% | 0,37 | -0,46R | €-202,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 2 | 44 | 44 | 38,64% | 0,98 | -0,01R | €-4,67 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 105 | 105 | 43,81% | 1,22 | 0,10R | €109,12 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 50,00% | 1,08 | 0,04R | €3,46 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 32 | 32 | 40,62% | 1,24 | 0,10R | €32,03 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 22 | 22 | 27,27% | 0,59 | -0,23R | €-50,88 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 58 | 58 | 27,59% | 0,60 | -0,22R | €-126,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 75 | 75 | 20,00% | 0,42 | -0,40R | €-298,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 3 | 62 | 62 | 40,32% | 1,07 | 0,04R | €22,96 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 1 | 167 | 167 | 34,73% | 0,79 | -0,11R | €-185,06 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,51 | -0,30R | €-57,10 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 43 | 43 | 41,86% | 1,63 | 0,25R | €107,35 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 32 | 32 | 37,50% | 0,73 | -0,16R | €-50,72 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 2 | 93 | 93 | 21,51% | 0,53 | -0,25R | €-236,27 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 1 | 9 | 8 | 22,22% | 0,21 | -0,68R | €-61,12 |
| Rapida 1H V2 | RANGE | 0 | 38 | 31 | 34,21% | 0,66 | -0,19R | €-73,08 |
| Rapida 1H V2 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,53 | -0,19R | €-5,76 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 74 | 74 | 20,27% | 0,37 | -0,43R | €-315,89 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 60 | 60 | 40,00% | 0,99 | -0,01R | €-4,11 |
| Rapida 1H V3 Filtered | RANGE | 0 | 163 | 163 | 37,42% | 0,85 | -0,08R | €-131,74 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 19 | 19 | 36,84% | 0,84 | -0,09R | €-17,03 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 41 | 41 | 41,46% | 1,20 | 0,09R | €38,69 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 107 | 107 | 37,38% | 1,00 | 0,00R | €1,78 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-232,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 52 | 52 | 42,31% | 1,07 | 0,03R | €17,48 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 133 | 133 | 39,10% | 0,97 | -0,01R | €-19,15 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,84 | -0,08R | €-8,44 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 33 | 33 | 39,39% | 1,00 | 0,00R | €0,59 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 26 | 26 | 26,92% | 0,62 | -0,21R | €-55,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 68 | 68 | 29,41% | 0,67 | -0,17R | €-115,95 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 23,08% | 0,19 | -0,65R | €-84,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 1 | 45 | 45 | 57,78% | 1,26 | 0,11R | €49,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 75 | 75 | 42,67% | 0,87 | -0,08R | €-58,02 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 15 | 15 | 53,33% | 1,49 | 0,20R | €30,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,93 | -0,04R | €-5,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 1 | 47 | 47 | 51,06% | 0,97 | -0,01R | €-6,79 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 16,67% | 0,19 | -0,63R | €-75,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 46 | 46 | 43,48% | 1,11 | 0,05R | €22,08 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 78 | 78 | 38,46% | 0,92 | -0,04R | €-33,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 15 | 15 | 46,67% | 1,45 | 0,19R | €28,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 14 | 14 | 35,71% | 0,90 | -0,06R | €-8,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 1 | 48 | 48 | 33,33% | 0,88 | -0,05R | €-24,39 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 5,56% | 0,10 | -0,73R | €-131,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 55 | 55 | 40,00% | 0,95 | -0,02R | €-12,83 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 94 | 94 | 39,36% | 0,91 | -0,05R | €-44,28 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,27 | -0,57R | €-40,24 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 23 | 23 | 43,48% | 1,31 | 0,14R | €32,01 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 20 | 20 | 40,00% | 0,93 | -0,04R | €-7,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 67 | 67 | 34,33% | 0,87 | -0,06R | €-43,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 17,39% | 0,32 | -0,51R | €-234,33 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 1 | 57 | 57 | 38,60% | 0,93 | -0,04R | €-21,54 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 164 | 164 | 38,41% | 0,89 | -0,06R | €-90,63 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 25 | 25 | 32,00% | 0,91 | -0,04R | €-10,27 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 93 | 93 | 32,26% | 0,79 | -0,11R | €-103,40 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 73 | 73 | 20,55% | 0,38 | -0,42R | €-304,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 1 | 59 | 59 | 37,29% | 0,85 | -0,08R | €-45,23 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 161 | 161 | 37,27% | 0,83 | -0,09R | €-146,48 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 38,89% | 0,93 | -0,04R | €-6,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 36 | 36 | 41,67% | 1,27 | 0,12R | €41,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 90 | 90 | 31,11% | 0,75 | -0,13R | €-120,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 1,26 | 0,13R | €18,79 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 7 | 28 | 28 | 21,43% | 0,41 | -0,47R | €-132,84 |
| SHADOW_4H_WIDE | RANGE | 8 | 59 | 59 | 15,25% | 0,56 | -0,34R | €-199,25 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 7 | 7 | 28,57% | 1,10 | 0,07R | €5,07 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 1 | 22 | 22 | 13,64% | 0,40 | -0,47R | €-103,38 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 16 | 16 | 31,25% | 1,22 | 0,13R | €20,05 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 37 | 37 | 21,62% | 0,91 | -0,05R | €-19,38 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 20 | 20 | 50,00% | 1,11 | 0,05R | €10,60 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 59 | 59 | 45,76% | 1,05 | 0,03R | €15,18 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 1 | 4 | 4 | 50,00% | 1,39 | 0,21R | €8,27 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 10 | 10 | 60,00% | 2,81 | 0,57R | €56,63 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 8 | 8 | 62,50% | 2,18 | 0,34R | €26,82 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 1 | 5 | 5 | 40,00% | 0,36 | -0,43R | €-21,25 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 4 | 4 | 50,00% | 1,16 | 0,09R | €3,64 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,56 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,62 | -0,24R | €-109,67 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 4 | 54 | 54 | 37,04% | 1,11 | 0,05R | €29,40 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 3 | 131 | 131 | 41,98% | 0,98 | -0,01R | €-15,46 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 16 | 16 | 31,25% | 0,83 | -0,09R | €-14,08 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 53 | 53 | 41,51% | 1,41 | 0,21R | €113,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 23 | 23 | 30,43% | 0,49 | -0,30R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 92 | 92 | 36,96% | 1,12 | 0,05R | €48,94 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 15,38% | 0,48 | -0,33R | €-42,51 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 48 | 48 | 37,50% | 1,15 | 0,08R | €36,41 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 66 | 66 | 46,97% | 1,15 | 0,08R | €50,37 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 23 | 23 | 47,83% | 2,29 | 0,46R | €106,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 16 | 16 | 25,00% | 0,53 | -0,31R | €-48,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 1 | 53 | 53 | 28,30% | 0,61 | -0,19R | €-101,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,58 | -0,25R | €-135,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 4 | 60 | 60 | 41,67% | 1,02 | 0,01R | €6,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 2 | 130 | 130 | 40,77% | 1,12 | 0,05R | €67,57 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 17 | 17 | 47,06% | 0,79 | -0,10R | €-17,15 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 40 | 40 | 42,50% | 1,18 | 0,09R | €34,19 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,64 | -0,18R | €-56,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 94 | 94 | 51,06% | 1,33 | 0,14R | €128,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,65 | -0,22R | €-102,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 4 | 52 | 52 | 38,46% | 1,14 | 0,07R | €37,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 3 | 119 | 119 | 45,38% | 1,06 | 0,03R | €33,62 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 42,86% | 1,15 | 0,07R | €9,49 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 36 | 36 | 38,89% | 1,17 | 0,09R | €31,92 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 23 | 23 | 34,78% | 0,55 | -0,26R | €-60,33 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 71 | 71 | 38,03% | 0,74 | -0,12R | €-87,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 13 | 13 | 30,77% | 1,08 | 0,05R | €5,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 13 | 13 | 30,77% | 1,08 | 0,05R | €5,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 23,53% | 0,44 | -0,34R | €-57,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 38 | 38 | 39,47% | 1,17 | 0,09R | €34,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,65 | -0,18R | €-10,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 12 | 12 | 33,33% | 1,27 | 0,14R | €16,81 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 12 | 12 | 33,33% | 0,75 | -0,15R | €-18,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 47 | 47 | 38,30% | 1,09 | 0,05R | €22,80 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 97 | 97 | 35,05% | 0,80 | -0,10R | €-92,96 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 1 | 4 | 4 | 75,00% | 4,11 | 0,85R | €33,98 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 31 | 31 | 48,39% | 1,28 | 0,14R | €42,43 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,79R | €-23,63 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 4 | 4 | 75,00% | 4,12 | 0,88R | €35,34 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 9 | 9 | 66,67% | 1,56 | 0,21R | €18,66 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,21 | -0,55R | €-82,64 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 3 | 47 | 47 | 38,30% | 1,21 | 0,12R | €54,29 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 72 | 72 | 44,44% | 1,40 | 0,20R | €141,83 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,76 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 38 | 38 | 47,37% | 1,73 | 0,34R | €129,44 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,52 | -0,31R | €-49,15 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 61 | 61 | 31,15% | 1,02 | 0,01R | €6,58 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 0 | 35 | 35 | 25,71% | 0,65 | -0,21R | €-73,73 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 4 | 47 | 47 | 31,91% | 0,87 | -0,08R | €-38,00 |
| SHADOW_COMBO_TREND | RANGE | 3 | 109 | 109 | 32,11% | 0,89 | -0,06R | €-66,37 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 2 | 11 | 11 | 27,27% | 0,91 | -0,05R | €-5,01 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 46 | 46 | 36,96% | 1,22 | 0,13R | €57,58 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 23 | 23 | 26,09% | 0,49 | -0,30R | €-68,62 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 70 | 70 | 30,00% | 1,03 | 0,01R | €10,31 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-52,46 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 60,00% | 0,94 | -0,03R | €-1,46 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,81 | -0,11R | €-6,38 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -0,75R | €-45,24 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,86 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,59 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 27 | 27 | 22,22% | 0,51 | -0,37R | €-98,95 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 2 | 19 | 19 | 15,79% | 0,17 | -0,69R | €-131,83 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 53 | 53 | 28,30% | 0,77 | -0,16R | €-83,92 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,43 | 0,22R | €17,31 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 0 | 17 | 17 | 41,18% | 1,67 | 0,33R | €56,40 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 0 | 10 | 10 | 30,00% | 0,21 | -0,49R | €-49,11 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 37 | 37 | 29,73% | 1,09 | 0,05R | €19,00 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,23 | -0,63R | €-107,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 2 | 11 | 11 | 18,18% | 0,03 | -0,74R | €-81,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 0 | 33 | 33 | 27,27% | 0,53 | -0,30R | €-98,98 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 6 | 6 | 50,00% | 2,84 | 0,63R | €37,58 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 0 | 10 | 10 | 60,00% | 3,77 | 0,86R | €85,66 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 0 | 8 | 8 | 37,50% | 0,25 | -0,49R | €-38,82 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 3 | 23 | 23 | 26,09% | 0,92 | -0,03R | €-7,97 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 0 | 37 | 37 | 24,32% | 0,57 | -0,27R | €-100,46 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 2 | 46 | 46 | 30,43% | 0,80 | -0,13R | €-59,75 |
| SHADOW_EMA_TREND_1H | RANGE | 3 | 108 | 108 | 31,48% | 0,92 | -0,04R | €-47,39 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 2 | 12 | 12 | 33,33% | 1,40 | 0,18R | €21,25 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 45 | 45 | 35,56% | 1,14 | 0,08R | €37,57 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 24 | 24 | 29,17% | 0,51 | -0,28R | €-66,86 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 74 | 74 | 28,38% | 0,95 | -0,03R | €-20,43 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-53,00 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,15 | -0,63R | €-18,84 |
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
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,12 | -0,65R | €-19,52 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,84R | €8,38 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 4 | 4 | 50,00% | 1,36 | 0,20R | €7,90 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,02R | €0,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,69 | -0,22R | €-35,19 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 3 | 28 | 28 | 32,14% | 0,90 | -0,07R | €-20,48 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 6 | 68 | 68 | 30,88% | 0,95 | -0,03R | €-23,07 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 16 | 16 | 50,00% | 2,19 | 0,53R | €85,35 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 22 | 22 | 40,91% | 1,55 | 0,28R | €62,57 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 44,44% | 0,85 | -0,08R | €-14,12 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 3 | 66 | 66 | 77,27% | 2,24 | 0,29R | €193,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 2 | 132 | 132 | 65,91% | 1,43 | 0,14R | €181,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 34 | 34 | 67,65% | 1,36 | 0,11R | €36,89 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 33 | 33 | 63,64% | 1,33 | 0,11R | €37,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 107 | 107 | 62,62% | 1,08 | 0,03R | €31,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,64 | -0,26R | €-33,81 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 6 | 68 | 68 | 33,82% | 1,09 | 0,05R | €36,78 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 15 | 15 | 33,33% | 1,07 | 0,04R | €6,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 20 | 20 | 40,00% | 1,39 | 0,22R | €44,20 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 1,36 | 0,21R | €18,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 31 | 31 | 25,81% | 0,68 | -0,25R | €-78,29 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 6 | 62 | 62 | 30,65% | 1,10 | 0,06R | €39,60 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 13 | 13 | 38,46% | 1,42 | 0,23R | €30,22 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 18 | 18 | 44,44% | 1,71 | 0,37R | €66,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 0,00% | 0,00 | -1,02R | €-71,71 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 54 | 54 | 35,19% | 1,07 | 0,04R | €23,94 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 12 | 12 | 41,67% | 1,89 | 0,39R | €46,35 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 13 | 13 | 23,08% | 0,65 | -0,25R | €-32,52 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,57 | -0,31R | €-43,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 3 | 30 | 30 | 33,33% | 0,94 | -0,04R | €-12,77 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 6 | 65 | 65 | 33,85% | 1,10 | 0,06R | €39,29 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 15 | 15 | 40,00% | 1,44 | 0,24R | €36,39 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 19 | 19 | 42,11% | 1,52 | 0,29R | €54,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 19,57% | 0,44 | -0,37R | €-168,98 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 2 | 58 | 58 | 32,76% | 0,88 | -0,07R | €-40,64 |
| Forza relativa 1H V1 | RANGE | 5 | 148 | 148 | 31,08% | 0,85 | -0,08R | €-121,60 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 13 | 13 | 7,69% | 0,26 | -0,48R | €-62,75 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 0 | 51 | 51 | 39,22% | 1,35 | 0,18R | €92,51 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 26 | 26 | 26,92% | 0,75 | -0,14R | €-36,21 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 3 | 92 | 92 | 26,09% | 0,91 | -0,05R | €-44,68 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,64 | -0,21R | €-41,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 26 | 23 | 38,46% | 1,35 | 0,18R | €47,67 |
| Forza relativa 1H V2 | RANGE | 2 | 64 | 62 | 34,38% | 0,91 | -0,05R | €-32,96 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 0 | 28 | 24 | 42,86% | 1,83 | 0,37R | €103,63 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 13 | 12 | 30,77% | 1,03 | 0,02R | €1,95 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 1 | 35 | 32 | 45,71% | 1,70 | 0,33R | €116,73 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 2 | 7 | 7 | 28,57% | 0,49 | -0,31R | €-21,66 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 2 | 51 | 51 | 25,49% | 0,36 | -0,37R | €-188,84 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 15 | 15 | 46,67% | 1,08 | 0,05R | €6,96 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 1 | 15 | 15 | 6,67% | 0,29 | -0,30R | €-45,71 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 2 | 7 | 7 | 28,57% | 0,49 | -0,31R | €-21,66 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 51 | 51 | 25,49% | 0,36 | -0,37R | €-188,84 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 15 | 15 | 46,67% | 1,08 | 0,05R | €6,96 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 1 | 15 | 15 | 6,67% | 0,29 | -0,30R | €-45,71 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 2 | 7 | 7 | 28,57% | 0,49 | -0,31R | €-21,66 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 51 | 51 | 25,49% | 0,36 | -0,37R | €-188,84 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 15 | 15 | 46,67% | 1,08 | 0,05R | €6,96 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 1 | 15 | 15 | 6,67% | 0,29 | -0,30R | €-45,71 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 2 | 8 | 8 | 37,50% | 0,96 | -0,02R | €-1,79 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 64 | 64 | 31,25% | 0,69 | -0,17R | €-108,81 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 1,42 | 0,16R | €21,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 30 | 30 | 40,00% | 1,00 | -0,00R | €-0,64 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,66 | -0,16R | €-22,16 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 22 | 22 | 4,55% | 0,16 | -0,44R | €-96,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 29,63% | 0,29 | -0,48R | €-128,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 5 | 5 | 20,00% | 0,30 | -0,44R | €-22,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 2 | 56 | 56 | 57,14% | 0,73 | -0,11R | €-64,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 68,75% | 1,69 | 0,22R | €34,79 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 18 | 18 | 61,11% | 1,52 | 0,22R | €38,86 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 24 | 24 | 41,67% | 0,58 | -0,21R | €-49,35 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 1 | 18 | 18 | 44,44% | 0,65 | -0,16R | €-29,35 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,22 | -0,52R | €-124,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 0,67 | -0,18R | €-10,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 2 | 49 | 49 | 57,14% | 0,47 | -0,22R | €-109,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 61,54% | 1,54 | 0,21R | €27,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 17 | 17 | 58,82% | 1,59 | 0,26R | €43,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,65 | -0,17R | €-30,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 1 | 17 | 17 | 41,18% | 0,34 | -0,33R | €-55,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 4 | 45 | 45 | 33,33% | 1,01 | 0,00R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 55 | 55 | 47,27% | 1,39 | 0,18R | €96,26 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 2 | 46 | 46 | 28,26% | 0,58 | -0,21R | €-94,48 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 46 | 46 | 32,61% | 0,96 | -0,02R | €-9,24 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 55 | 55 | 47,27% | 1,39 | 0,18R | €96,26 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 2 | 46 | 46 | 28,26% | 0,58 | -0,21R | €-94,48 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 46 | 46 | 32,61% | 0,96 | -0,02R | €-9,24 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 55 | 55 | 47,27% | 1,39 | 0,18R | €96,26 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 2 | 46 | 46 | 28,26% | 0,58 | -0,21R | €-94,48 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,23 | -0,51R | €-71,62 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 3 | 47 | 47 | 38,30% | 1,22 | 0,12R | €54,88 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 69 | 69 | 43,48% | 1,46 | 0,22R | €152,59 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,76 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 34 | 34 | 47,06% | 1,82 | 0,37R | €127,02 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,52 | -0,31R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 60 | 60 | 30,00% | 0,96 | -0,02R | €-14,13 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,64R | €-31,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 46 | 46 | 28,26% | 0,81 | -0,10R | €-46,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 0,00% | 0,00 | -0,77R | €-92,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 3 | 44 | 44 | 38,64% | 1,15 | 0,08R | €34,01 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 64 | 64 | 42,19% | 1,31 | 0,16R | €99,36 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 22 | 22 | 54,55% | 2,71 | 0,56R | €122,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,52 | -0,31R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 40 | 40 | 20,00% | 0,46 | -0,32R | €-126,23 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,04 | -0,54R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 51,35% | 1,46 | 0,19R | €71,70 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 78 | 78 | 44,87% | 1,34 | 0,14R | €107,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,35 | -0,46R | €-13,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 22 | 22 | 50,00% | 1,79 | 0,30R | €65,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,66 | -0,19R | €-35,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -0,75R | €-82,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 32 | 32 | 40,62% | 1,49 | 0,24R | €75,85 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 67 | 67 | 44,78% | 1,41 | 0,19R | €130,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 20 | 20 | 45,00% | 2,15 | 0,42R | €83,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 14 | 14 | 21,43% | 0,53 | -0,34R | €-47,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,54 | -0,25R | €-38,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 51,35% | 1,46 | 0,19R | €71,70 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 78 | 78 | 44,87% | 1,34 | 0,14R | €107,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,35 | -0,46R | €-13,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 24 | 24 | 45,83% | 1,59 | 0,23R | €55,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,66 | -0,19R | €-35,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 49 | 49 | 48,98% | 1,25 | 0,11R | €52,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,26 | -0,47R | €-61,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 32 | 32 | 40,62% | 1,49 | 0,24R | €75,85 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 67 | 67 | 44,78% | 1,41 | 0,19R | €130,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 21 | 21 | 42,86% | 1,89 | 0,35R | €73,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 14 | 14 | 21,43% | 0,53 | -0,34R | €-47,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 38 | 38 | 21,05% | 0,59 | -0,22R | €-84,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,48 | -0,30R | €-48,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 3 | 48 | 48 | 45,83% | 1,10 | 0,05R | €21,94 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 73 | 73 | 45,21% | 1,32 | 0,13R | €97,47 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,35 | -0,46R | €-13,67 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 28 | 28 | 46,43% | 1,48 | 0,20R | €55,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 21 | 21 | 33,33% | 0,58 | -0,23R | €-47,25 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 59 | 59 | 49,15% | 1,26 | 0,10R | €61,85 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,51 | -0,29R | €-20,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 48 | 48 | 35,42% | 1,16 | 0,09R | €42,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 60 | 60 | 40,00% | 1,32 | 0,17R | €99,60 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 22 | 22 | 50,00% | 2,20 | 0,45R | €98,34 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,54 | -0,30R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 44 | 44 | 20,45% | 0,51 | -0,28R | €-125,08 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,60R | €-41,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 48 | 48 | 37,50% | 1,11 | 0,06R | €27,64 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 56 | 56 | 39,29% | 1,36 | 0,19R | €108,67 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 18 | 18 | 50,00% | 3,26 | 0,65R | €117,37 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 15 | 15 | 20,00% | 0,61 | -0,24R | €-35,84 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 43 | 43 | 20,93% | 0,54 | -0,26R | €-112,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,35 | -0,47R | €-74,87 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 3 | 48 | 48 | 35,42% | 1,08 | 0,04R | €19,55 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,78 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-41,89 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 37 | 37 | 45,95% | 1,78 | 0,35R | €129,86 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 76 | 76 | 35,53% | 1,08 | 0,04R | €29,95 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,41 | -0,47R | €-32,89 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,86 | 0,38R | €19,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-12T13:24:49+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **412**
- Scenari virtuali ancora attivi: **9265**
- Gruppi in attesa dell'uscita originale: **256**
- Gruppi con originale chiuso ma Shadow ancora attive: **156**
- Confronti completati: **163864**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 4109 | 4175 | +€8,48 | 50,3% | 1069 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 4109 | 4175 | +€7,53 | 49,3% | 1057 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 4109 | 4175 | +€6,20 | 47,6% | 1068 | 114 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 4109 | 4175 | +€4,90 | 47,8% | 1005 | 166 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 4109 | 4175 | +€4,83 | 47,7% | 1184 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 4105 | 4171 | +€6,74 | 42,6% | 838 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 4105 | 4171 | +€5,14 | 42,1% | 794 | 165 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 4105 | 4171 | +€4,91 | 40,9% | 913 | 94 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 4105 | 4171 | +€4,29 | 41,3% | 701 | 260 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 4104 | 4170 | +€2,66 | 40,1% | 601 | 429 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 4097 | 4163 | +€1,09 | 33,2% | 414 | 780 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 4095 | 4161 | €-0,29 | 30,4% | 327 | 974 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 4091 | 4157 | €-4,88 | 27,4% | 276 | 1119 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 4084 | 4150 | €-0,22 | 46,0% | 809 | 575 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 4083 | 4149 | €-0,69 | 39,5% | 462 | 863 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 4072 | 4138 | €-3,71 | 32,7% | 604 | 887 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 4063 | 4129 | €-8,46 | 23,2% | 276 | 1253 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 4060 | 4126 | +€5,29 | 32,7% | 486 | 423 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 4031 | 4097 | +€4,42 | 35,5% | 236 | 677 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 4029 | 4095 | €-5,27 | 31,1% | 209 | 1171 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-12T13:24:58+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **163864**
- Valutazioni prodotte: **18737**
- Candidature al Blocco 5: **34**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 98 | 0,465 | 0,212 | 0,345 | 61,2% | 94,8 | VALIDATING |
| GB20_R040 | 2697 | 0,279 | 0,117 | 0,242 | 54,9% | 88,0 | VALIDATING |
| GB30_R040 | 2697 | 0,265 | 0,092 | 0,229 | 54,3% | 87,5 | VALIDATING |
| GB20_R050 | 40 | 3,608 | 4,831 | 2,939 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB30_R050 | 40 | 3,583 | 4,818 | 2,878 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB20_R075 | 40 | 3,537 | 4,831 | 2,811 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB30_R075 | 40 | 3,515 | 4,818 | 2,779 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB40_R050 | 40 | 3,477 | 4,678 | 2,797 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB40_R075 | 40 | 3,411 | 4,678 | 2,753 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB50_R050 | 40 | 3,362 | 4,538 | 2,736 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB50_R075 | 40 | 3,299 | 4,538 | 2,515 | 87,5% | 87,3 | EARLY_SIGNAL |
| ATR15_R050 | 40 | 2,983 | 4,115 | 2,345 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB30_R100 | 40 | 3,407 | 4,818 | 2,653 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R075 | 40 | 3,375 | 4,587 | 2,659 | 87,5% | 87,3 | EARLY_SIGNAL |
| ATR10_R050 | 40 | 3,350 | 4,641 | 2,660 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB40_R100 | 40 | 3,301 | 4,678 | 2,615 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R060 | 40 | 3,248 | 4,437 | 2,550 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R050 | 40 | 3,238 | 4,337 | 2,594 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB50_R100 | 40 | 3,195 | 4,538 | 2,461 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R040 | 40 | 3,148 | 4,238 | 2,598 | 87,5% | 87,3 | EARLY_SIGNAL |

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

Generato: 2026-08-12T13:28:36+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 44 | 100,00% | 0,95 | €-30,95 | €-0,70 | 1,83% | EARLY_NOT_CONFIRMED |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 44 | 100,00% | 0,99 | €-5,92 | €-0,13 | 1,91% | EARLY_NOT_CONFIRMED |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 16 | 100,00% | 0,72 | €-135,52 | €-8,47 | 2,18% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 11 | 100,00% | 0,00 | €-162,51 | €-14,77 | 1,63% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 35 | 100,00% | 0,82 | €-133,25 | €-3,81 | 2,13% | EARLY_NOT_CONFIRMED |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-12T13:24:12+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **91**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **349.42 R**
- Profitto virtuale mancato: **439.74 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 180 | 0 | 35767.27 |
| DOWN_20 | 180 | 0 | 71534.54 |
| DOWN_30 | 180 | 0 | 107301.80 |
| DOWN_40 | 180 | 56 | 136222.96 |
| UP_10 | 77 | 4 | 21309.27 |
| UP_20 | 77 | 6 | 42498.54 |
| UP_30 | 77 | 6 | 63402.35 |
| UP_40 | 77 | 36 | 76758.03 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-12T13:23:18+00:00

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

Generato: 2026-08-12T13:28:42+00:00

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

Generato: 2026-08-12T13:28:42+00:00

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

Generato: 2026-08-12T13:28:42+00:00

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

Generato: 2026-08-12T13:28:42+00:00

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
| 1 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 15.8 | E | 48 | 1.39 | 0.160 | 4.24 |
| 2 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 15.0 | E | 34 | 1.50 | 0.217 | 7.64 |
| 3 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 14.6 | E | 85 | 1.14 | 0.063 | 7.82 |
| 4 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 13.4 | E | 90 | 1.03 | 0.015 | 9.81 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 13.0 | E | 113 | 0.95 | -0.021 | 13.25 |
| 6 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 12.9 | E | 38 | 1.27 | 0.116 | 5.48 |
| 7 | SHADOW_DONCHIAN_1H | BASELINE | 12.7 | E | 52 | 1.20 | 0.117 | 8.55 |
| 8 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 12.4 | E | 48 | 1.22 | 0.107 | 8.12 |
| 9 | SHADOW_1H_BALANCED_V3 | BASELINE | 12.2 | E | 77 | 1.07 | 0.038 | 9.68 |
| 10 | SHADOW_COMBO_ADAPTIVE | BASELINE | 10.6 | E | 53 | 1.09 | 0.035 | 6.68 |

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

Generato: 2026-08-12T13:28:42+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **628**
- Strategie preferite nel regime corrente: **3**
- Strategie da evitare nel regime corrente: **19**
- Memorie contestuali: **296**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.6 | 4 | 99.00 | 0.972 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 76.1 | 7 | 2.35 | 0.426 | 1.11 |
| 5 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.5 | 12 | 2.82 | 0.322 | 1.04 |
| 6 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 70.0 | 8 | 2.44 | 0.587 | 2.16 |
| 7 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | COMPATIBLE | 69.6 | 30 | 1.67 | 0.260 | 3.43 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | COMPATIBLE | 59.1 | 31 | 1.45 | 0.214 | 7.64 |
| 9 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 56.3 | 5 | 1.40 | 0.091 | 1.14 |
| 10 | SHADOW_1H_FAST | shadow-1h-fast | COMPATIBLE | 55.1 | 61 | 1.27 | 0.113 | 6.50 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-12T13:28:43+00:00

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

Generato: 2026-08-12T13:24:12+00:00

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
