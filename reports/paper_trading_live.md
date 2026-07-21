# Paper trading automatico KuCoin

Generato: 2026-07-21T05:14:52+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-21T05:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-21T05:08:24+00:00 | 2026-07-21T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-21T04:45:00+00:00 | 2026-07-21T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-21T04:00:00+00:00 | 2026-07-21T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-21T00:00:00+00:00 | 2026-07-21T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | ADA | 60m | LONG | 6,24 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ETH | 60m | LONG | 6,07 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ADA | 60m | LONG | 6,24 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | ADA | 60m | LONG | 6,24 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ACE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 7,01 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,94 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 6,80 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,82 | 6,00 | 1,18 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,43 | 6,00 | 1,57 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,18 | 6,00 | 1,82 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,78 | 6,00 | 2,22 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,05 | 6,00 | 5,95 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | XRP | 60m | LONG | 7,50 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | XRP | 60m | LONG | 7,50 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.884,55 | -1,15% | €-115,45 | €3.000,00 | -3,85% | 4 | 16 | 31,25% | 0,81 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 16 | 235 | CAMPIONE INSUFFICIENTE | 30 (mancano 14) |

- Trade del Principale 4H chiusi: **16**; win rate **31,25%**; profit factor **0,81**.
- Expectancy: **€-6,29** per trade; P&L netto: **€-100,68**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.884,55 | €1.552,19 | €4.656,58 | €197,65 | €-13,85 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.453,88 | €3.363,52 | €6.727,04 | €103,50 | €71,48 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.448,28 | €3.644,27 | €7.288,54 | €155,12 | €124,18 |
| TEST | Combo Adaptive | 3 | €10.240,79 | €2.743,84 | €5.487,67 | €153,54 | €-1,84 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.236,65 | €3.152,26 | €9.456,78 | €51,19 | €122,30 |
| TEST | Combo Mean Reversion | 0 | €10.195,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.193,67 | €1.522,73 | €3.045,46 | €151,81 | €-33,79 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.191,93 | €1.589,62 | €3.179,25 | €102,21 | €-26,07 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €10.152,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €10.131,56 | €1.846,89 | €3.693,78 | €200,81 | €-7,34 |
| TEST | Bilanciata 1H V1 | 4 | €10.124,13 | €2.802,69 | €8.408,06 | €151,29 | €47,52 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.100,56 | €3.909,27 | €7.818,54 | €149,97 | €105,25 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.100,56 | €3.909,27 | €7.818,54 | €149,97 | €105,25 |
| TEST | Forza relativa 1H V1 | 4 | €10.091,49 | €2.508,00 | €5.016,01 | €151,36 | €-1,81 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €10.078,16 | €3.985,76 | €7.971,52 | €149,97 | €82,94 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €10.078,16 | €3.985,76 | €7.971,52 | €149,97 | €82,94 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €10.074,45 | €4.852,44 | €9.704,89 | €99,98 | €80,68 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €10.054,14 | €1.639,93 | €3.279,86 | €150,82 | €-1,63 |
| TEST | Sol Donchian 1H | 1 | €10.022,50 | €1.127,14 | €3.381,43 | €49,98 | €29,06 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.014,82 | €1.001,44 | €3.004,32 | €49,95 | €25,82 |
| TEST | Combo Adaptive Long Only V1 | 2 | €10.011,18 | €1.376,57 | €2.753,14 | €100,00 | €13,31 |
| TEST | Sol Adaptive 1H | 1 | €10.005,50 | €1.000,51 | €3.001,52 | €49,91 | €25,79 |
| TEST | Rapida 1H V2 | 0 | €10.004,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.002,28 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| TEST | Btc Donchian 4H | 1 | €10.002,28 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.993,05 | €4.484,54 | €8.969,08 | €99,95 | €-1,57 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.993,05 | €4.484,54 | €8.969,08 | €99,95 | €-1,57 |
| TEST | 1H Fast Score 6 75 V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast No Pepe V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast Tp2 V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast V3 Cap75 V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast V3 Long Only V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast V3 No Esports V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.966,28 | €1.054,45 | €3.163,36 | €49,74 | €20,32 |
| TEST | Combo Scanner | 3 | €9.965,83 | €3.315,37 | €6.630,74 | €149,74 | €-46,94 |
| TEST | Bilanciata 1H V2 | 4 | €9.964,64 | €1.532,77 | €4.598,30 | €99,11 | €34,80 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.964,13 | €3.107,23 | €6.214,47 | €149,84 | €-31,66 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.963,18 | €2.523,11 | €5.046,23 | €124,84 | €-58,90 |
| TEST | Btc Adaptive 1H | 1 | €9.949,01 | €1.151,09 | €3.453,28 | €49,73 | €4,77 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 2 | €9.939,80 | €416,21 | €832,42 | €99,89 | €-59,70 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 2 | €9.939,80 | €416,21 | €832,42 | €99,89 | €-59,70 |
| TEST | Eth Donchian 1H | 1 | €9.939,63 | €1.144,51 | €3.433,53 | €0,00 | €52,87 |
| TEST | Scanner Top5 Btc Guard V1 | 2 | €9.935,58 | €416,12 | €832,24 | €99,87 | €-63,68 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 2 | €9.935,58 | €416,12 | €832,24 | €99,87 | €-63,68 |
| TEST | Rapida 1H V3 Filtered | 4 | €9.929,58 | €3.872,62 | €11.617,85 | €148,72 | €93,36 |
| TEST | Btc Ema 1H | 1 | €9.926,36 | €1.144,78 | €3.434,35 | €49,45 | €36,04 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.924,93 | €2.212,42 | €4.424,84 | €149,11 | €-0,42 |
| TEST | Rapida 1H V1 | 4 | €9.917,55 | €3.037,61 | €9.112,84 | €196,10 | €3,69 |
| TEST | Btc Donchian 1H | 1 | €9.893,66 | €1.287,72 | €3.863,16 | €49,45 | €5,34 |
| TEST | Eth Ema 1H | 1 | €9.889,64 | €1.012,80 | €3.038,40 | €0,00 | €46,79 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.818,74 | €1.920,13 | €3.840,25 | €49,33 | €-44,50 |
| TEST | Global Confluence puro 1H | 1 | €9.785,72 | €1.535,54 | €3.071,08 | €49,14 | €-39,90 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.717,63 | €2.612,79 | €5.225,58 | €48,50 | €23,39 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.884,55 | €-100,68 | 16 | 16 | 31,25% | 0,81 | €-6,29 | 4,26% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.453,88 | €386,68 | 17 | 17 | 47,06% | 2,37 | €22,75 | 1,62% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.448,28 | €328,90 | 23 | 23 | 47,83% | 1,78 | €14,30 | 2,70% |
| TEST | Combo Adaptive | Combo Adaptive | €10.240,79 | €246,18 | 16 | 16 | 43,75% | 2,08 | €15,39 | 1,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.236,65 | €120,58 | 23 | 23 | 39,13% | 1,19 | €5,24 | 2,20% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.195,13 | €195,13 | 7 | 7 | 57,14% | 2,81 | €27,88 | 0,59% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.193,67 | €229,40 | 17 | 17 | 35,29% | 1,54 | €13,49 | 2,32% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.191,93 | €221,19 | 14 | 14 | 50,00% | 1,80 | €15,80 | 1,98% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.152,11 | €152,11 | 15 | 15 | 46,67% | 1,66 | €10,14 | 2,06% |
| TEST | Ampia 4H | Confluenza trend | €10.131,56 | €139,54 | 11 | 11 | 27,27% | 1,50 | €12,69 | 2,08% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.124,13 | €81,68 | 21 | 21 | 42,86% | 1,21 | €3,89 | 1,81% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.100,56 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,49% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.100,56 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,49% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.091,49 | €96,51 | 16 | 16 | 37,50% | 1,37 | €6,03 | 2,29% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.078,16 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €10.078,16 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €10.074,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,54% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Combo Trend | Combo Trend | €10.054,14 | €57,96 | 15 | 15 | 33,33% | 1,15 | €3,86 | 2,19% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.022,50 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,55% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Sol Ema 1H | Trend following EMA | €10.014,82 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,98% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.011,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,50% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.005,50 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,99% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.004,31 | €4,31 | 3 | 2 | 33,33% | 1,07 | €1,44 | 0,93% |
| TEST | Btc Ema 4H | Trend following EMA | €10.002,28 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.002,28 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,97 | €-4,03 | 4 | 4 | 25,00% | 0,18 | €-1,01 | 0,04% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.993,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,33% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.993,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,33% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.966,28 | €-51,89 | 2 | 2 | 50,00% | 0,05 | €-25,94 | 1,02% |
| TEST | Combo Scanner | Combo Scanner | €9.965,83 | €17,00 | 17 | 17 | 41,18% | 1,04 | €1,00 | 1,88% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.964,64 | €-67,37 | 16 | 14 | 43,75% | 0,84 | €-4,21 | 2,75% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.964,13 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.963,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.949,01 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,89% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.939,80 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,60% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.939,80 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,60% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.939,63 | €-110,95 | 2 | 2 | 0,00% | 0,00 | €-55,48 | 1,38% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.935,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,71% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.935,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,71% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.929,58 | €-156,37 | 36 | 36 | 33,33% | 0,81 | €-4,34 | 2,89% |
| TEST | Btc Ema 1H | Trend following EMA | €9.926,36 | €-109,08 | 2 | 2 | 0,00% | 0,00 | €-54,54 | 1,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.924,93 | €-72,00 | 9 | 9 | 33,33% | 0,77 | €-8,00 | 2,25% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.917,55 | €-80,68 | 47 | 47 | 34,04% | 0,93 | €-1,72 | 4,86% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.893,66 | €-110,32 | 2 | 2 | 0,00% | 0,00 | €-55,16 | 1,49% |
| TEST | Eth Ema 1H | Trend following EMA | €9.889,64 | €-155,12 | 4 | 4 | 25,00% | 0,05 | €-38,78 | 1,59% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.818,74 | €-134,45 | 11 | 11 | 27,27% | 0,50 | €-12,22 | 3,67% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.785,72 | €-172,54 | 6 | 6 | 33,33% | 0,21 | €-28,76 | 2,35% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.717,63 | €-302,40 | 21 | 21 | 28,57% | 0,36 | €-14,40 | 3,44% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07286 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €1,31 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 546,51000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-15,16 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1894,43881 | 1923,61000 | 1905,59197 | 1272,43140 | 1955,82155 | €1.043,85 | €3.131,56 | €0,00 | €48,22 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,13540 | 1,13517 | 1,11905 | 0,76261 | 1,16810 | €1.172,10 | €3.516,30 | €50,63 | €-0,70 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €684,20 | €2.052,59 | €0,00 | €34,80 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1894,43881 | 1923,61000 | 1905,59197 | 1272,43140 | 1955,82155 | €1.047,36 | €3.142,08 | €0,00 | €48,38 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,11148 | 1,13517 | 1,11148 | 0,74655 | 1,14349 | €1.163,70 | €3.491,09 | €0,00 | €74,40 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17046 | 0,11699 | 0,18161 | €799,70 | €2.399,09 | €51,19 | €-0,48 |
| Rapida 1H V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00173 | 0,00175 | 0,00154 | 0,00116 | 0,00202 | €147,41 | €442,24 | €49,70 | €4,58 |
| Rapida 1H V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.476,35 | €4.429,06 | €49,61 | €-0,89 |
| 1H Fast Score 6 75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast Score 6 75 V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast Score 6 75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast Tp2 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,16083 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast Tp2 V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17996 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1967,09220 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11148 | 1,13517 | 1,12495 | 0,74655 | 1,13016 | €1.469,55 | €4.408,66 | €0,00 | €93,96 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €997,39 | €2.992,17 | €49,66 | €-0,60 |
| 1H Fast V3 Cap75 V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast V3 Cap75 V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast V3 Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast V3 Long Only V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast V3 No Esports V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast V3 No Esports V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07286 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-8,86 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 546,51000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €30,74 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 62,91800 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-44,08 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €14,85 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €986,47 | €1.972,93 | €50,47 | €-1,81 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,27910 | 0,25697 | 0,24560 | 0,14094 | 0,35278 | €213,08 | €426,17 | €51,14 | €-33,79 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,27375 | 0,25697 | 0,24090 | 0,13825 | 0,35588 | €212,62 | €425,25 | €51,03 | €-26,07 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,17417 | 0,17414 | 0,17005 | 0,08796 | 0,18326 | €1.046,69 | €2.093,39 | €49,63 | €-0,42 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,11469 | 1,13517 | 1,09864 | 0,56292 | 1,14680 | €1.796,54 | €3.593,08 | €51,74 | €66,01 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,17009 | 0,17414 | 0,16650 | 0,08590 | 0,17727 | €1.222,25 | €2.444,49 | €51,57 | €58,18 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06985 | €1.712,73 | €3.425,45 | €49,33 | €-44,50 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.070,89 | €2.141,78 | €0,00 | €49,76 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 78,23100 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €21,71 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,76655 | 78,23100 | 76,55444 | 39,27211 | 80,43319 | €1.603,37 | €3.206,74 | €49,98 | €19,15 |
| Scanner Top5 Btc Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,11539 | 1,13517 | 1,11539 | 0,56327 | 1,15073 | €1.735,04 | €3.470,07 | €0,00 | €61,53 |
| Scanner Top5 Btc Guard V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,36043 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,79 | €415,58 | €49,87 | €-22,50 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €2,86 |
| Scanner Top5 Btc Btc Le3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16982 | 0,17414 | 0,16625 | 0,08576 | 0,17769 | €1.187,43 | €2.374,86 | €49,99 | €60,39 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,23100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €19,70 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €2,86 |
| Scanner Top5 Btc Btc 2 3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16982 | 0,17414 | 0,16625 | 0,08576 | 0,17769 | €1.187,43 | €2.374,86 | €49,99 | €60,39 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,23100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €19,70 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,36043 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,79 | €415,58 | €49,87 | €-22,50 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28216 | 0,25697 | 0,24830 | 0,14249 | 0,35665 | €208,33 | €416,67 | €50,00 | €-37,19 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,88 | €415,75 | €49,89 | €-22,51 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28216 | 0,25697 | 0,24830 | 0,14249 | 0,35665 | €208,33 | €416,67 | €50,00 | €-37,19 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,88 | €415,75 | €49,89 | €-22,51 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Scanner Top5 Btc Runner25 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16962 | 0,17414 | 0,16597 | 0,08566 | 0,18059 | €1.159,50 | €2.319,01 | €49,99 | €61,77 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1923,61000 | 1872,70756 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €49,98 | €42,05 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Scanner Top5 Btc Tp3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16962 | 0,17414 | 0,16597 | 0,08566 | 0,18059 | €1.159,50 | €2.319,01 | €49,99 | €61,77 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1923,61000 | 1872,70756 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €49,98 | €42,05 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07193 | 0,07286 | 0,07308 | 0,10753 | 0,06905 | €1.535,54 | €3.071,08 | €49,14 | €-39,90 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €884,51 | €1.769,01 | €50,29 | €-1,63 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €978,80 | €1.957,60 | €50,08 | €-1,80 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06965 | €1.737,43 | €3.474,87 | €50,04 | €-45,14 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.001,06 | €2.002,12 | €51,22 | €-1,84 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,56451 | 78,23100 | 77,65759 | 39,17008 | 80,14392 | €1.462,23 | €2.924,45 | €0,00 | €25,13 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €947,94 | €1.895,88 | €48,50 | €-1,74 |
| Combo Adaptive Regime V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,35358 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Combo Adaptive Regime V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17017 | 0,17414 | 0,16653 | 0,08594 | 0,17746 | €1.168,24 | €2.336,48 | €50,00 | €54,48 |
| Combo Adaptive Regime V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06985 | €1.730,66 | €3.461,32 | €49,84 | €-44,97 |
| Combo Adaptive Long Only V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,35358 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Combo Adaptive Long Only V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17017 | 0,17414 | 0,16653 | 0,08594 | 0,17746 | €1.168,24 | €2.336,48 | €50,00 | €54,48 |
| Combo Adaptive Partial 1R V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,35358 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Combo Adaptive Partial 1R V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17017 | 0,17414 | 0,16653 | 0,08594 | 0,17746 | €584,12 | €1.168,24 | €25,00 | €27,24 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06985 | €1.730,66 | €3.461,32 | €49,84 | €-44,97 |
| Combo Adaptive Runner25 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Combo Adaptive Runner25 V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1923,61000 | 1903,18396 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €42,07 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06882 | €1.734,29 | €3.468,58 | €49,95 | €-45,06 |
| Combo Adaptive Tp3 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Combo Adaptive Tp3 V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1923,61000 | 1903,18396 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €42,07 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06882 | €1.734,29 | €3.468,58 | €49,95 | €-45,06 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64820,68154 | 65501,00000 | 63887,26373 | 43537,89110 | 66687,51717 | €1.144,78 | €3.434,35 | €49,45 | €36,04 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65501,00000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 65410,57950 | 65501,00000 | 64573,32408 | 43934,10590 | 67085,09034 | €1.287,72 | €3.863,16 | €49,45 | €5,34 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65501,00000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 65410,57950 | 65501,00000 | 64468,66716 | 43934,10590 | 67294,40419 | €1.151,09 | €3.453,28 | €49,73 | €4,77 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 78,23100 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €25,82 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 77,56451 | 78,23100 | 76,41811 | 52,09750 | 79,85731 | €1.127,14 | €3.381,43 | €49,98 | €29,06 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 78,23100 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €25,79 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1894,43881 | 1923,61000 | 1909,06598 | 1272,43140 | 1955,82155 | €1.012,80 | €3.038,40 | €0,00 | €46,79 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1894,43881 | 1923,61000 | 1909,06598 | 1272,43140 | 1949,00125 | €1.144,51 | €3.433,53 | €0,00 | €52,87 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1911,33219 | 1923,61000 | 1881,27848 | 1283,77812 | 1971,43961 | €1.054,45 | €3.163,36 | €49,74 | €20,32 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25216 | €-53,23 | -1,07 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25330 | €-53,88 | -1,09 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V1 | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25330 | €-55,00 | -1,09 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V3 Filtered | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25239 | €-55,20 | -1,07 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V1 | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25357 | €2,87 | 0,06 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V1 | DOGE | SHORT | 2026-07-21T03:23:31+00:00 | 0,07275 | €-56,25 | -1,13 | STOP |
| Benchmark Bollinger mean reversion 1H | BANK | SHORT | 2026-07-21T01:23:31+00:00 | 0,29357 | €-5,46 | -0,11 | STOP_STRESS_SLIPPAGE |
| Scanner Top 5 Long 1H | PEPE | LONG | 2026-07-20T22:53:31+00:00 | 0,00000 | €5,97 | 0,12 | STOP |
| Rapida 1H V1 | GRAM | SHORT | 2026-07-20T22:38:32+00:00 | 1,49330 | €-4,09 | -0,08 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V3 Filtered | ETH | LONG | 2026-07-20T19:23:30+00:00 | 1894,05992 | €-5,50 | -0,11 | STOP |
| Rapida 1H V1 | ETH | LONG | 2026-07-20T19:23:30+00:00 | 1894,05992 | €-5,58 | -0,11 | STOP |
| Benchmark Donchian breakout 1H | ETH | LONG | 2026-07-20T19:08:30+00:00 | 1897,10014 | €44,88 | 0,88 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
