# Paper trading automatico KuCoin

Generato: 2026-07-22T18:38:50+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-22T18:38:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-22T18:38:25+00:00 | 2026-07-22T18:38:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-22T18:15:00+00:00 | 2026-07-22T18:15:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-22T17:00:00+00:00 | 2026-07-22T17:00:00+00:00 | 38,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-22T12:00:00+00:00 | 2026-07-22T12:00:00+00:00 | 2,64 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ADA | 240m | LONG | 8,19 | 6,00 | 0,00 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -8,08 | 6,00 | 0,00 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,94 | 6,00 | 0,00 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 5,28 | 6,00 | 0,72 | STALE_CANDLE | 2,64 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -5,14 | 6,00 | 0,86 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,53 | 6,00 | 1,47 | STALE_CANDLE | 2,64 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,22 | 6,00 | 1,78 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | LAB | 240m | SHORT | -3,75 | 6,00 | 2,25 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 3,13 | 6,00 | 2,87 | STALE_CANDLE | 2,64 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 2,64 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 158.5 minuti; tolleranza 60 minuti. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ADA | 60m | LONG | 6,51 | 4,50 | 0,00 | OPENED | 38,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | LAB | 60m | LONG | 5,25 | 4,50 | 0,00 | OPENED | 38,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €10 · 15x | BANK | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤70.0 in rientro. RSI 76.3→72.7; volume x3.62; shock 3.15 ATR. |
| Scalp RSI Short 75 · €50 · 15x | BANK | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤70.0 in rientro. RSI 76.3→72.7; volume x3.62; shock 3.15 ATR. |
| Scalp RSI Short 75 · prudente · 5x | BANK | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤70.0 in rientro. RSI 76.3→72.7; volume x3.62; shock 3.15 ATR. |
| Scalp RSI Short 80 · €10 · 15x | BANK | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥80.0. RSI 76.3→72.7; volume x3.62; shock 3.15 ATR. |
| Scalp RSI Short 80 · €50 · 15x | BANK | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥80.0. RSI 76.3→72.7; volume x3.62; shock 3.15 ATR. |
| Scalp RSI Short 80 · prudente · 5x | BANK | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥80.0. RSI 76.3→72.7; volume x3.62; shock 3.15 ATR. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.904,54 | -0,95% | €-95,46 | €3.000,00 | -3,18% | 4 | 17 | 29,41% | 0,73 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 17 | 351 | CAMPIONE INSUFFICIENTE | 30 (mancano 13) |

- Trade del Principale 4H chiusi: **17**; win rate **29,41%**; profit factor **0,73**.
- Expectancy: **€-8,97** per trade; P&L netto: **€-152,45**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.904,54 | €1.512,92 | €4.538,75 | €147,66 | €56,46 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.489,52 | €1.266,43 | €2.532,86 | €157,89 | €-23,05 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.403,47 | €2.729,95 | €5.459,91 | €156,45 | €-10,13 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.330,72 | €2.286,80 | €6.860,41 | €154,63 | €0,02 |
| TEST | Combo Adaptive — madre | 3 | €10.245,88 | €2.169,96 | €4.339,92 | €153,94 | €8,59 |
| TEST | Bilanciata 1H V1 | 4 | €10.196,16 | €3.306,93 | €9.920,79 | €204,41 | €-63,47 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.165,00 | €3.555,00 | €7.109,99 | €152,79 | €11,40 |
| TEST | Forza relativa 1H V2 | 4 | €10.122,20 | €2.785,02 | €5.570,05 | €151,27 | €-45,25 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.085,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.083,90 | €2.723,66 | €5.447,33 | €50,41 | €41,07 |
| TEST | Ampia 4H | 4 | €10.054,77 | €2.235,83 | €4.471,66 | €201,27 | €-32,05 |
| TEST | Btc Bollinger 4H | 1 | €10.031,72 | €1.313,84 | €2.627,69 | €50,00 | €34,51 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.021,99 | €968,56 | €1.937,11 | €50,00 | €23,41 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.014,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.011,78 | €1.105,63 | €2.211,26 | €50,00 | €10,25 |
| TEST | Btc Donchian 4H | 1 | €10.011,78 | €1.105,63 | €2.211,26 | €50,00 | €10,25 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.005,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.002,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €10.002,68 | €1.062,51 | €3.187,53 | €100,42 | €0,27 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.997,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.997,32 | €934,60 | €2.803,79 | €50,02 | €0,43 |
| TEST | Eth Ema 4H | 1 | €9.989,70 | €883,93 | €1.767,86 | €50,00 | €-8,83 |
| TEST | Rapida 1H V3 Filtered — madre | 3 | €9.989,20 | €2.120,81 | €6.362,43 | €148,99 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €9.988,15 | €1.875,09 | €3.750,19 | €100,66 | €-13,64 |
| TEST | Sol Ema 1H | 1 | €9.987,27 | €1.001,44 | €3.004,32 | €49,95 | €-2,07 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €9.987,07 | €2.827,84 | €5.655,68 | €150,04 | €-14,27 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €9.987,07 | €2.827,84 | €5.655,68 | €150,04 | €-14,27 |
| TEST | Btc Adaptive 4H | 1 | €9.985,92 | €1.047,40 | €2.094,81 | €50,00 | €-14,50 |
| TEST | Benchmark trend following EMA 1H | 2 | €9.983,72 | €1.311,90 | €2.623,80 | €99,39 | €-15,29 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.979,10 | €807,13 | €1.614,26 | €50,00 | €-20,15 |
| TEST | Sol Adaptive 1H | 1 | €9.977,98 | €1.000,51 | €3.001,52 | €49,91 | €-2,07 |
| TEST | Sol Ema 4H | 1 | €9.977,20 | €880,51 | €1.761,01 | €50,00 | €-21,98 |
| TEST | Sol Donchian 4H | 1 | €9.977,20 | €880,51 | €1.761,01 | €50,00 | €-21,98 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.973,84 | €2.339,93 | €4.679,86 | €149,52 | €12,28 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €9.963,54 | €3.363,30 | €6.726,60 | €149,56 | €3,56 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €9.959,66 | €1.277,26 | €2.554,51 | €149,85 | €-21,89 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €9.959,66 | €1.277,26 | €2.554,51 | €149,85 | €-21,89 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €9.946,44 | €2.543,53 | €5.087,05 | €149,64 | €-31,93 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.942,27 | €2.576,61 | €5.153,21 | €149,81 | €-19,89 |
| TEST | Btc Donchian 1H | 0 | €9.937,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.935,50 | €1.153,05 | €3.459,15 | €49,81 | €-24,79 |
| TEST | Rapida V1 — senza PEPE | 3 | €9.934,90 | €2.639,17 | €7.917,50 | €149,68 | €-17,31 |
| TEST | Btc Ema 1H | 0 | €9.934,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 3 | €9.933,21 | €1.942,95 | €5.828,84 | €149,35 | €-1,88 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.927,86 | €2.075,49 | €4.150,97 | €148,31 | €13,92 |
| TEST | Combo Adaptive — Quality7 | 2 | €9.916,28 | €1.968,07 | €3.936,13 | €99,06 | €20,16 |
| TEST | Combo Scanner | 2 | €9.905,14 | €1.065,42 | €2.130,85 | €99,73 | €-1,84 |
| TEST | Rapida V3 — score <7,5 | 1 | €9.898,20 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.898,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 0 | €9.897,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 2 | €9.896,82 | €1.639,80 | €4.919,40 | €99,37 | €0,15 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 2 | €9.885,15 | €897,55 | €2.692,66 | €98,91 | €-31,30 |
| TEST | Rapida V3 — no volatilità HIGH | 2 | €9.870,11 | €1.632,42 | €4.897,25 | €98,90 | €0,15 |
| TEST | Eth Ema 1H | 1 | €9.866,88 | €1.144,65 | €3.433,94 | €49,45 | €-20,52 |
| TEST | Combo Adaptive — Long Only | 2 | €9.864,16 | €1.099,22 | €2.198,44 | €98,72 | €-1,82 |
| TEST | Rapida V1 — target pieno 2R | 1 | €9.862,39 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.858,10 | €1.282,24 | €2.564,48 | €148,09 | €-21,67 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.858,02 | €1.973,66 | €3.947,32 | €99,07 | €20,17 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.858,02 | €1.973,66 | €3.947,32 | €99,07 | €20,17 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.850,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.847,79 | €1.260,81 | €2.521,62 | €147,54 | €-26,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.831,42 | €1.301,48 | €2.602,97 | €148,06 | €-39,56 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.827,35 | €2.141,01 | €4.282,03 | €147,68 | €17,95 |
| TEST | Rapida 1H V1 — madre | 3 | €9.783,73 | €2.121,86 | €6.365,57 | €146,23 | €0,00 |
| TEST | Master Adaptive V1 | 3 | €9.781,76 | €2.731,68 | €5.463,37 | €146,91 | €1,69 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.781,76 | €2.731,68 | €5.463,37 | €146,91 | €1,69 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.781,76 | €2.731,68 | €5.463,37 | €146,91 | €1,69 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.760,39 | €3.788,57 | €7.577,13 | €148,35 | €-70,51 |
| TEST | Global Confluence puro 1H | 1 | €9.759,30 | €1.527,19 | €3.054,37 | €48,87 | €-12,85 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.749,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.745,48 | €1.236,67 | €2.473,34 | €0,00 | €43,07 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.719,79 | €1.182,17 | €2.364,33 | €146,66 | €-39,11 |
| TEST | Top 5 + BTC — Guard | 3 | €9.696,83 | €1.161,08 | €2.322,16 | €146,20 | €-21,31 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.675,10 | €1.149,02 | €2.298,05 | €96,76 | €-6,13 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.672,37 | €2.208,64 | €4.417,28 | €146,39 | €-71,56 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | Madre Rapida 1H V1 originale, invariata. |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | Accetta soltanto score assoluti da 6,0 a meno di 7,5. |
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
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | Benchmark puro: ritorno verso la media dopo uscita dalle Bollinger e conferma RSI estrema. |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | Benchmark puro: trend following con prezzo, EMA20, EMA50 e filtro ADX. |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | Opera long solo sulle cinque crypto più forti della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | Opera short solo sulle cinque crypto più deboli della classifica live KuCoin, con conferma tecnica. |
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
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | Chiude il 75% a 2R e lascia il 25% verso 3R con profit lock a 1,8R. |
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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.904,54 | €-152,45 | 17 | 17 | 29,41% | 0,73 | €-8,97 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.489,52 | €513,90 | 28 | 28 | 50,00% | 1,96 | €18,35 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.403,47 | €416,52 | 20 | 20 | 50,00% | 2,23 | €20,83 | 1,74% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.330,72 | €334,16 | 28 | 28 | 46,43% | 1,48 | €11,93 | 2,20% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.245,88 | €239,35 | 20 | 20 | 45,00% | 1,71 | €11,97 | 1,31% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.196,16 | €265,27 | 30 | 30 | 50,00% | 1,47 | €8,84 | 1,81% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.165,00 | €157,56 | 17 | 17 | 47,06% | 1,40 | €9,27 | 1,98% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.122,20 | €170,79 | 22 | 21 | 36,36% | 1,28 | €7,76 | 2,76% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.085,92 | €85,92 | 9 | 9 | 44,44% | 1,40 | €9,55 | 1,12% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.083,90 | €46,36 | 19 | 19 | 42,11% | 1,14 | €2,44 | 2,06% |
| TEST | Ampia 4H | Confluenza trend | €10.054,77 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,37% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.031,72 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,27% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.021,99 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.014,00 | €14,00 | 2 | 2 | 100,00% | ∞ | €7,00 | 0,04% |
| TEST | Btc Ema 4H | Trend following EMA | €10.011,78 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.011,78 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.005,24 | €5,24 | 2 | 2 | 50,00% | 10,75 | €2,62 | 0,09% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.002,80 | €2,80 | 2 | 2 | 100,00% | ∞ | €1,40 | 0,01% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.002,68 | €4,32 | 20 | 18 | 50,00% | 1,01 | €0,22 | 2,75% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.997,37 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,55% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.997,32 | €-1,43 | 4 | 3 | 25,00% | 0,98 | €-0,36 | 0,99% |
| TEST | Eth Ema 4H | Trend following EMA | €9.989,70 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.989,20 | €-7,38 | 47 | 47 | 34,04% | 0,99 | €-0,16 | 2,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,26 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Combo Trend | Combo Trend | €9.988,15 | €3,85 | 16 | 16 | 31,25% | 1,01 | €0,24 | 2,35% |
| TEST | Sol Ema 1H | Trend following EMA | €9.987,27 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 1,10% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.987,07 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.987,07 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.985,92 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,37% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.983,72 | €0,58 | 14 | 14 | 35,71% | 1,00 | €0,04 | 2,25% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.979,10 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.977,98 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 1,12% |
| TEST | Sol Ema 4H | Trend following EMA | €9.977,20 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.977,20 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.973,84 | €-35,63 | 8 | 8 | 50,00% | 0,83 | €-4,45 | 1,41% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.963,54 | €-36,11 | 7 | 7 | 42,86% | 0,83 | €-5,16 | 1,41% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.959,66 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,21% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.959,66 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,21% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.946,44 | €-18,57 | 21 | 21 | 28,57% | 0,95 | €-0,88 | 2,70% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.942,27 | €-35,06 | 5 | 5 | 20,00% | 0,52 | €-7,01 | 1,51% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.937,58 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.935,50 | €-37,64 | 3 | 3 | 66,67% | 0,31 | €-12,55 | 1,02% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.934,90 | €-43,44 | 15 | 15 | 26,67% | 0,86 | €-2,90 | 2,10% |
| TEST | Btc Ema 1H | Trend following EMA | €9.934,39 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.933,21 | €-61,41 | 3 | 3 | 0,00% | 0,00 | €-20,47 | 1,08% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.927,86 | €-83,93 | 8 | 8 | 37,50% | 0,70 | €-10,49 | 2,18% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.916,28 | €-101,74 | 3 | 3 | 33,33% | 0,05 | €-33,91 | 1,51% |
| TEST | Combo Scanner | Combo Scanner | €9.905,14 | €-91,73 | 21 | 21 | 38,10% | 0,85 | €-4,37 | 2,48% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.898,20 | €-100,92 | 18 | 18 | 27,78% | 0,77 | €-5,61 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.898,20 | €-101,80 | 19 | 19 | 26,32% | 0,77 | €-5,36 | 2,49% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.897,06 | €-102,94 | 10 | 10 | 20,00% | 0,57 | €-10,29 | 2,11% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.896,82 | €-100,78 | 18 | 18 | 27,78% | 0,77 | €-5,60 | 2,49% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.885,15 | €-82,33 | 20 | 20 | 35,00% | 0,85 | €-4,12 | 2,83% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.870,11 | €-127,49 | 19 | 19 | 31,58% | 0,76 | €-6,71 | 2,96% |
| TEST | Eth Ema 1H | Trend following EMA | €9.866,88 | €-110,26 | 5 | 5 | 40,00% | 0,33 | €-22,05 | 1,59% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.864,16 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.862,39 | €-136,72 | 15 | 15 | 26,67% | 0,68 | €-9,11 | 2,13% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.858,10 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,51% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.858,02 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,79% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.858,02 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,79% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.850,91 | €-149,09 | 9 | 9 | 22,22% | 0,48 | €-16,57 | 2,00% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.847,79 | €-124,50 | 5 | 5 | 20,00% | 0,42 | €-24,90 | 2,79% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.831,42 | €-127,46 | 3 | 3 | 0,00% | 0,00 | €-42,49 | 1,69% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.827,35 | €-187,92 | 10 | 10 | 30,00% | 0,51 | €-18,79 | 2,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.783,73 | €-212,84 | 54 | 54 | 31,48% | 0,84 | €-3,94 | 6,14% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.781,76 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.781,76 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.781,76 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.760,39 | €-163,77 | 3 | 3 | 0,00% | 0,00 | €-54,59 | 2,60% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.759,30 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,92% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.749,89 | €-250,11 | 9 | 9 | 33,33% | 0,25 | €-27,79 | 2,84% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.745,48 | €-296,31 | 18 | 18 | 22,22% | 0,44 | €-16,46 | 4,81% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.719,79 | €-239,81 | 6 | 6 | 0,00% | 0,00 | €-39,97 | 2,87% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.696,83 | €-280,49 | 5 | 5 | 0,00% | 0,00 | €-56,10 | 3,19% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.675,10 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.672,37 | €-253,42 | 9 | 9 | 22,22% | 0,12 | €-28,16 | 3,55% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07268 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €5,56 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,15620 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €50,89 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 514,40710 | 510,80000 | 526,37866 | 683,30410 | 490,46397 | €731,22 | €2.193,66 | €51,05 | €15,38 |
| Bilanciata 1H V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,17971 | 0,17569 | 0,17590 | 0,12070 | 0,18732 | €809,54 | €2.428,61 | €51,41 | €-54,30 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1937,36740 | 1923,98000 | 1909,46931 | 1301,26510 | 1993,16358 | €1.184,41 | €3.553,24 | €51,17 | €-24,55 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00180 | 0,00177 | 0,00159 | 0,00121 | 0,00222 | €143,70 | €431,11 | €50,27 | €-7,21 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 512,43749 | 510,80000 | 523,41700 | 680,68780 | 490,47847 | €780,12 | €2.340,36 | €50,14 | €7,48 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 514,40710 | 510,80000 | 526,37866 | 683,30410 | 490,46397 | €738,63 | €2.215,89 | €51,57 | €15,54 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 58,56129 | 58,91800 | 59,74667 | 77,78891 | 56,19052 | €849,08 | €2.547,23 | €51,56 | €-15,52 |
| Rapida 1H V1 — madre | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 — madre | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 — madre | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00187 | 0,00177 | 0,00171 | 0,00126 | 0,00211 | €193,16 | €579,49 | €49,74 | €-31,30 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17580 | 0,17569 | 0,17285 | 0,11808 | 0,18022 | €988,05 | €2.964,14 | €49,69 | €-1,78 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | LAB | LONG | Momentum / breakout | 60m | 3,0x | 0,15623 | 0,15620 | 0,14118 | 0,10494 | 0,17881 | €171,84 | €515,51 | €49,67 | €-0,10 |
| Rapida V1 — senza PEPE | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 515,14695 | 510,80000 | 524,33753 | 684,28687 | 501,36109 | €935,01 | €2.805,03 | €50,04 | €23,67 |
| Rapida V1 — senza PEPE | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17815 | 0,17569 | 0,17516 | 0,11966 | 0,18263 | €990,47 | €2.971,41 | €49,81 | €-40,98 |
| Rapida V1 — target pieno 2R | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 510,87780 | 510,80000 | 519,99222 | 678,61602 | 497,20619 | €934,60 | €2.803,79 | €50,02 | €0,43 |
| Rapida 1H V3 Filtered — madre | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida V3 — score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| Rapida V3 — no volatilità HIGH | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 510,82781 | 510,80000 | 519,94133 | 678,54961 | 497,15754 | €925,01 | €2.775,03 | €49,51 | €0,15 |
| Rapida V3 — senza ESPORTS | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 510,82781 | 510,80000 | 519,94133 | 678,54961 | 497,15754 | €927,51 | €2.782,54 | €49,64 | €0,15 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07268 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-5,63 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 510,80000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-14,72 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-4,14 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1923,98000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €-7,56 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | ADA | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,17815 | 0,17569 | 0,17431 | 0,08996 | 0,18659 | €1.157,66 | €2.315,32 | €49,90 | €-31,93 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 512,43749 | 510,80000 | 523,41700 | 766,09405 | 488,28257 | €1.188,35 | €2.376,70 | €50,92 | €7,59 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00234 | €214,82 | €429,64 | €50,07 | €-20,67 |
| Forza relativa 1H V2 | ADA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17815 | 0,17569 | 0,17431 | 0,08996 | 0,18659 | €1.166,52 | €2.333,03 | €50,28 | €-32,17 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,85923 | 58,91800 | 60,10965 | 87,99454 | 55,73317 | €1.195,13 | €2.390,27 | €50,78 | €-2,39 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 510,80000 | 527,70883 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €50,83 | €13,78 |
| Benchmark Bollinger mean reversion 1H | ZEC | LONG | Bollinger mean reversion | 60m | 2,0x | 514,61290 | 510,80000 | 504,63261 | 259,87952 | 529,58334 | €1.299,75 | €2.599,50 | €50,41 | €-19,26 |
| Benchmark Bollinger mean reversion 1H | ADA | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,17949 | 0,17569 | 0,17796 | 0,26834 | 0,17474 | €1.423,91 | €2.847,83 | €0,00 | €60,33 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 58,56129 | 58,91800 | 59,87838 | 87,54912 | 55,66368 | €1.104,85 | €2.209,70 | €49,70 | €-13,46 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €-1,83 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €-1,94 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00231 | €218,50 | €437,00 | €52,44 | €-21,12 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 521,71564 | 510,80000 | 520,35622 | 779,96488 | 496,96511 | €1.029,27 | €2.058,54 | €0,00 | €43,07 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 77,51100 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €-8,21 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €-1,92 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16335 | 0,15620 | 0,14544 | 0,08249 | 0,20276 | €227,11 | €454,22 | €49,81 | €-19,89 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €-1,79 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00235 | €201,99 | €403,97 | €48,48 | €-19,52 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,51100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €-12,43 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-1,84 |
| Top 5 + BTC — BTC 2–3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,51100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €-12,43 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-1,84 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00235 | €203,02 | €406,03 | €48,72 | €-19,62 |
| Top 5 + BTC — Guard + MFE | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16335 | 0,15620 | 0,14544 | 0,08249 | 0,20276 | €222,53 | €445,06 | €48,81 | €-19,49 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €-1,82 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-19,85 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-19,85 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16335 | 0,15620 | 0,14544 | 0,08249 | 0,20276 | €225,09 | €450,17 | €49,37 | €-19,71 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-1,84 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-20,05 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-1,84 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-20,05 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07238 | 0,07268 | 0,07353 | 0,10820 | 0,06948 | €1.527,19 | €3.054,37 | €48,87 | €-12,85 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,39131 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €0,00 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 58,56129 | 58,91800 | 59,87838 | 87,54912 | 55,66368 | €1.119,67 | €2.239,34 | €50,36 | €-13,64 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €-1,84 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,17714 | 510,80000 | 525,63928 | 768,69483 | 491,25287 | €1.147,58 | €2.295,16 | €51,16 | €15,07 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15620 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €-6,48 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15620 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €-6,13 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 510,80000 | 526,97821 | 770,65289 | 492,50422 | €1.108,92 | €2.217,83 | €49,44 | €20,16 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 510,80000 | 526,97821 | 770,65289 | 492,50422 | €1.111,03 | €2.222,05 | €49,53 | €20,20 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15620 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €-6,28 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 510,80000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €20,17 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €-1,82 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €-1,82 |
| Combo Adaptive — parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,68684 | 510,80000 | 527,82154 | 770,95183 | 491,41745 | €1.042,77 | €2.085,55 | €49,08 | €19,76 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 510,80000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €20,17 |
| Combo Adaptive — 75% a 2R + runner 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 58,56129 | 58,91800 | 59,74667 | 87,54912 | 55,00513 | €1.231,85 | €2.463,69 | €49,87 | €-15,01 |
| Combo Adaptive — 75% a 2R + runner 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 510,80000 | 525,11837 | 769,45713 | 483,39306 | €1.229,27 | €2.458,54 | €49,83 | €18,57 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 510,80000 | 525,11837 | 769,45713 | 483,39306 | €1.230,32 | €2.460,64 | €49,87 | €18,58 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15620 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €-6,31 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65713,90000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €10,25 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65713,90000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €10,25 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 65713,90000 | 67855,55360 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €50,00 | €34,51 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 65713,90000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-14,50 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 77,51100 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €-2,07 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 77,51100 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-21,98 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 77,51100 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-21,98 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 77,51100 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €23,41 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 77,51100 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €-2,07 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 77,51100 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-20,15 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1935,54703 | 1923,98000 | 1907,67515 | 1300,04242 | 1991,29079 | €1.144,65 | €3.433,94 | €49,45 | €-20,52 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1923,98000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €-8,83 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1937,86750 | 1923,98000 | 1909,96220 | 1301,60100 | 1993,67808 | €1.153,05 | €3.459,15 | €49,81 | €-24,79 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-1,80 |
| Master Adaptive V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13898 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €3,49 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-1,80 |
| Master Adaptive No Alt V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13898 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €3,49 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1923,98000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-18,44 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17971 | 0,17569 | 0,17590 | 0,09075 | 0,18732 | €1.164,38 | €2.328,77 | €49,29 | €-52,06 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-1,80 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00187 | 0,00177 | 0,00166 | 0,00094 | 0,00228 | €224,01 | €448,03 | €49,44 | €-24,20 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00186 | 0,00177 | 0,00164 | 0,00094 | 0,00229 | €208,66 | €417,31 | €48,63 | €-20,07 |
| Master Adaptive Gb20 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17971 | 0,17569 | 0,17590 | 0,09075 | 0,18732 | €1.151,35 | €2.302,69 | €48,74 | €-51,48 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15620 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €-1,80 |
| Master Adaptive Runner25 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13898 | 1,12142 | 0,57459 | 1,18696 | €1.694,88 | €3.389,77 | €48,81 | €3,49 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17641 | €23,91 | 0,48 | STOP |
| Rapida V3 — qualità completa + profit lock | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-54,32 | -1,11 | STOP |
| Rapida V3 — senza ESPORTS | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-55,01 | -1,11 | STOP |
| Rapida V3 — Long + no HIGH + score <7,5 | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-54,88 | -1,11 | STOP |
| Rapida V3 — Long Only | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-55,14 | -1,11 | STOP |
| Rapida V3 — no volatilità HIGH | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-54,86 | -1,11 | STOP |
| Rapida V3 — score <7,5 | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-55,15 | -1,11 | STOP |
| Rapida 1H V3 Filtered — madre | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-55,65 | -1,11 | STOP |
| Rapida V1 — target pieno 2R | ADA | LONG | 2026-07-22T18:38:35+00:00 | 0,17664 | €-55,18 | -1,11 | STOP |
| Rapida V1 — target pieno 2R | AKE | LONG | 2026-07-22T18:38:35+00:00 | 0,00180 | €-0,98 | -0,02 | STOP |
| Rapida V1 — senza PEPE | AKE | LONG | 2026-07-22T18:38:35+00:00 | 0,00180 | €-0,97 | -0,02 | STOP |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | AKE | LONG | 2026-07-22T18:38:35+00:00 | 0,00180 | €-0,98 | -0,02 | STOP |

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
| MAIN | Principale 4H | 39/30 | 17/30 | 0,86 | 0,73 | -0,10R | €-8,97 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 2/30 | 2/30 | ∞ | 10,75 | 0,97R | €2,62 | 0,09% | COERENTE + | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 130/30 | 30/30 | 0,97 | 1,47 | -0,02R | €8,84 | 1,81% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 19/30 | 18/30 | 1,67 | 1,01 | 0,36R | €0,22 | 2,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 39/30 | 28/30 | 1,29 | 1,48 | 0,18R | €11,93 | 2,20% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 151/30 | 54/30 | 0,88 | 0,84 | -0,08R | €-3,94 | 6,14% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2/30 | 3/30 | 1,36 | 0,00 | 0,18R | €-20,47 | 1,08% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 21/30 | 20/30 | 0,65 | 0,85 | -0,25R | €-4,12 | 2,83% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 21/30 | 15/30 | 0,65 | 0,86 | -0,25R | €-2,90 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 14/30 | 19/30 | 0,98 | 0,77 | -0,02R | €-5,36 | 2,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 19/30 | 15/30 | 0,47 | 0,68 | -0,44R | €-9,11 | 2,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 2/30 | 3/30 | 0,59 | 0,98 | -0,31R | €-0,36 | 0,99% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 63/30 | 47/30 | 1,01 | 0,99 | 0,00R | €-0,16 | 2,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 20/30 | 18/30 | 0,71 | 0,77 | -0,20R | €-5,61 | 2,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 8/30 | 9/30 | 0,42 | 0,25 | -0,47R | €-27,79 | 2,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 8/30 | 9/30 | 0,42 | 0,48 | -0,47R | €-16,57 | 2,00% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 9/30 | 10/30 | 0,36 | 0,57 | -0,55R | €-10,29 | 2,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 21/30 | 19/30 | 0,66 | 0,76 | -0,24R | €-6,71 | 2,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 21/30 | 18/30 | 0,66 | 0,77 | -0,24R | €-5,60 | 2,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 38/30 | 12/30 | 0,85 | 1,27 | -0,12R | €7,39 | 2,37% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 28/30 | 19/30 | 0,99 | 1,14 | -0,01R | €2,44 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 2/30 | 0,00 | 0,78 | -1,11R | €-5,87 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,37% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,27% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 3/30 | 0,00 | 0,43 | -1,12R | €-20,81 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 4/30 | 0,57 | 0,60 | -0,36R | €-16,40 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 71/30 | 20/30 | 1,35 | 1,71 | 0,21R | €11,97 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 9/30 | 5/30 | 0,90 | 0,42 | -0,07R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 39/30 | 27/30 | 1,29 | 0,45 | 0,18R | €-11,76 | 4,11% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 16/30 | 10/30 | 0,81 | 0,51 | -0,14R | €-18,79 | 2,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-53,33 | 1,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-53,33 | 1,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 2/30 | 3/30 | 0,00 | 0,05 | -1,06R | €-33,91 | 1,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 13/30 | 8/30 | 0,54 | 0,70 | -0,38R | €-10,49 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 11/30 | 7/30 | 0,61 | 0,83 | -0,34R | €-5,16 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 11/30 | 8/30 | 0,61 | 0,83 | -0,34R | €-4,45 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 10/30 | 9/30 | 1,43 | 1,40 | 0,23R | €9,55 | 1,12% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 43/30 | 21/30 | 1,72 | 0,85 | 0,40R | €-4,37 | 2,48% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 55/30 | 16/30 | 1,17 | 1,01 | 0,12R | €0,24 | 2,35% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 1/30 | 2/30 | 0,00 | 0,46 | -1,12R | €-15,51 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 1/30 | 4/30 | 0,00 | 0,54 | -1,11R | €-12,93 | 1,27% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 32/30 | 17/30 | 1,03 | 1,40 | 0,03R | €9,27 | 1,98% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 61/30 | 14/30 | 1,13 | 1,00 | 0,09R | €0,04 | 2,25% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 2/30 | 3/30 | 1,70 | 0,31 | 0,39R | €-12,55 | 1,02% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 2/30 | 5/30 | 1,70 | 0,33 | 0,39R | €-22,05 | 1,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 7/30 | 0,00 | 0,17 | -1,10R | €-32,29 | 2,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 6/30 | 5/30 | 0,35 | 0,42 | -0,58R | €-24,90 | 2,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 5/30 | 9/30 | 0,00 | 0,12 | -1,08R | €-28,16 | 3,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 5/30 | 4/30 | 0,00 | 0,00 | -1,08R | €-54,11 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 5/30 | 4/30 | 0,00 | 0,00 | -1,08R | €-54,11 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 4/30 | 3/30 | 0,00 | 0,00 | -1,08R | €-54,59 | 2,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 5/30 | 4/30 | 0,00 | 0,00 | -1,08R | €-54,11 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 91/30 | 21/30 | 0,99 | 0,95 | -0,01R | €-0,88 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 26/30 | 21/30 | 1,48 | 1,28 | 0,29R | €7,76 | 2,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 31/30 | 18/30 | 0,59 | 0,44 | -0,29R | €-16,46 | 4,81% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 44/30 | 20/30 | 1,79 | 2,23 | 0,44R | €20,83 | 1,74% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 4/30 | 2/30 | 0,69 | 1,08 | -0,24R | €2,23 | 1,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 4/30 | 2/30 | 0,69 | 1,08 | -0,24R | €2,23 | 1,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 2/30 | 3/30 | 0,00 | 0,00 | -1,01R | €-42,49 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 5/30 | 6/30 | 0,00 | 0,00 | -1,06R | €-39,97 | 2,87% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 5/30 | 5/30 | 0,00 | 0,00 | -1,06R | €-56,10 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 7/30 | 5/30 | 0,80 | 0,52 | -0,15R | €-7,01 | 1,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 5/30 | 6/30 | 0,70 | 0,90 | -0,26R | €-2,82 | 2,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 5/30 | 6/30 | 0,70 | 0,90 | -0,26R | €-2,82 | 2,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 57/30 | 28/30 | 1,60 | 1,96 | 0,34R | €18,35 | 2,70% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 1,12% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 1/30 | 2/30 | 0,00 | 0,41 | -1,12R | €-1,31 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 2/30 | 2/30 | 1,70 | 0,83 | 0,39R | €-4,58 | 1,10% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,35% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07268**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.8 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65713.9 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.07319**; close **0.07298**; wick alta **57.1%**; volume **x0.51**

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

- Regime: **TREND_UP**
- Famiglia: **TREND_UP**
- Confidenza: **78,30%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +3.0, 83% sopra EMA50, ADX 30.6.
- BTC trend score: **3,00**; ADX: **30,62**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **0,91%**; dispersione: **7,59%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **418**
- Trade research chiusi: **1412**
- Eventi di mercato indipendenti chiusi: **452**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **5655**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 12 | 39 | 39 | 30,77% | 0,86 | -0,10R | €-39,07 |
| RSI_EXTREME_LONG_15M | 0 | 2 | 2 | 100,00% | ∞ | 0,97R | €19,43 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 14 | 130 | 130 | 33,85% | 0,97 | -0,02R | €-28,19 |
| Bilanciata 1H V2 | 7 | 22 | 19 | 45,45% | 1,67 | 0,36R | €78,64 |
| Bilanciata 1H V3 Filtered | 11 | 39 | 39 | 41,03% | 1,29 | 0,18R | €70,99 |
| Rapida 1H V1 | 9 | 151 | 151 | 38,41% | 0,88 | -0,08R | €-113,91 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 4 | 2 | 2 | 50,00% | 1,36 | 0,18R | €3,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 5 | 21 | 21 | 33,33% | 0,65 | -0,25R | €-51,49 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 7 | 21 | 21 | 33,33% | 0,65 | -0,25R | €-51,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 3 | 14 | 14 | 42,86% | 0,98 | -0,02R | €-2,13 |
| SHADOW_1H_FAST_TP2_V1 | 8 | 19 | 19 | 21,05% | 0,47 | -0,44R | €-84,54 |
| Rapida 1H V2 | 2 | 3 | 2 | 33,33% | 0,59 | -0,31R | €-9,29 |
| Rapida 1H V3 Filtered | 6 | 63 | 63 | 42,86% | 1,01 | 0,00R | €2,36 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 3 | 20 | 20 | 35,00% | 0,71 | -0,20R | €-40,16 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 8 | 8 | 25,00% | 0,42 | -0,47R | €-37,99 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 8 | 8 | 25,00% | 0,42 | -0,47R | €-37,99 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 9 | 9 | 22,22% | 0,36 | -0,55R | €-49,09 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 3 | 21 | 21 | 33,33% | 0,66 | -0,24R | €-51,09 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 4 | 21 | 21 | 33,33% | 0,66 | -0,24R | €-51,17 |
| SHADOW_4H_WIDE | 18 | 38 | 38 | 23,68% | 0,85 | -0,12R | €-45,80 |
| SHADOW_BOLLINGER_MR_1H | 2 | 28 | 28 | 42,86% | 0,99 | -0,01R | €-2,20 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 15 | 71 | 71 | 42,25% | 1,35 | 0,21R | €152,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 9 | 9 | 9 | 33,33% | 0,90 | -0,07R | €-6,61 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 14 | 39 | 39 | 41,03% | 1,29 | 0,18R | €69,70 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 11 | 16 | 16 | 31,25% | 0,81 | -0,14R | €-21,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 11 | 13 | 13 | 23,08% | 0,54 | -0,38R | €-48,90 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 11 | 11 | 11 | 18,18% | 0,61 | -0,34R | €-37,01 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 11 | 11 | 11 | 18,18% | 0,61 | -0,34R | €-37,01 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 10 | 10 | 50,00% | 1,43 | 0,23R | €22,73 |
| SHADOW_COMBO_SCANNER | 10 | 43 | 43 | 46,51% | 1,72 | 0,40R | €173,58 |
| SHADOW_COMBO_TREND | 15 | 55 | 55 | 36,36% | 1,17 | 0,12R | €64,08 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | 8 | 32 | 32 | 31,25% | 1,03 | 0,03R | €8,02 |
| SHADOW_EMA_TREND_1H | 16 | 61 | 61 | 34,43% | 1,13 | 0,09R | €53,70 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 7 | 6 | 6 | 16,67% | 0,35 | -0,58R | €-34,76 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 4 | 4 | 0,00% | 0,00 | -1,08R | €-43,07 |
| SHADOW_MASTER_ADAPTIVE_V1 | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| Forza relativa 1H V1 | 10 | 91 | 91 | 30,77% | 0,99 | -0,01R | €-8,35 |
| Forza relativa 1H V2 | 6 | 29 | 26 | 41,38% | 1,48 | 0,29R | €84,31 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 4 | 31 | 31 | 22,58% | 0,59 | -0,29R | €-91,39 |
| SHADOW_SCANNER_TOP5_BTC | 10 | 44 | 44 | 45,45% | 1,79 | 0,44R | €191,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 8 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,71 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 8 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 4 | 5 | 5 | 0,00% | 0,00 | -1,06R | €-52,85 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 4 | 5 | 5 | 0,00% | 0,00 | -1,06R | €-52,85 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 9 | 7 | 7 | 28,57% | 0,80 | -0,15R | €-10,82 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 8 | 5 | 5 | 20,00% | 0,70 | -0,26R | €-12,76 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 8 | 5 | 5 | 20,00% | 0,70 | -0,26R | €-12,76 |
| SHADOW_SCANNER_TOP5_LONG | 10 | 57 | 57 | 45,61% | 1,60 | 0,34R | €191,71 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| MAIN | RANGE | 0 | 14 | 14 | 28,57% | 0,77 | -0,17R | €-23,82 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 2 | 6 | 6 | 33,33% | 0,97 | -0,02R | €-1,10 |
| MAIN | TREND_UP | 3 | 12 | 12 | 33,33% | 0,96 | -0,03R | €-3,22 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 3 | 5 | 5 | 40,00% | 1,18 | 0,11R | €5,72 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 1 | 13 | 13 | 53,85% | 2,16 | 0,56R | €72,85 |
| Bilanciata 1H V1 | RANGE | 0 | 28 | 28 | 32,14% | 0,91 | -0,06R | €-16,44 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,38 |
| Bilanciata 1H V1 | TRANSITION | 2 | 26 | 26 | 30,77% | 0,85 | -0,11R | €-27,93 |
| Bilanciata 1H V1 | TREND_UP | 3 | 39 | 39 | 38,46% | 1,21 | 0,13R | €50,64 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 4 | 9 | 9 | 33,33% | 0,91 | -0,06R | €-5,65 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 2 | 4 | 3 | 100,00% | ∞ | 1,93R | €77,01 |
| Bilanciata 1H V2 | RANGE | 0 | 6 | 5 | 33,33% | 1,19 | 0,10R | €6,25 |
| Bilanciata 1H V2 | TRANSITION | 5 | 12 | 11 | 33,33% | 0,94 | -0,04R | €-4,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 3 | 3 | 66,67% | 3,76 | 0,93R | €27,94 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,44 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 19 | 19 | 47,37% | 1,70 | 0,38R | €72,47 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 5 | 9 | 9 | 33,33% | 0,91 | -0,06R | €-5,71 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 33,33% | 0,64 | -0,26R | €-23,06 |
| Rapida 1H V1 | ALT_ROTATION_UP | 2 | 10 | 10 | 60,00% | 2,06 | 0,45R | €44,74 |
| Rapida 1H V1 | RANGE | 0 | 35 | 35 | 40,00% | 1,04 | 0,02R | €8,01 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 23 | 23 | 43,48% | 1,20 | 0,11R | €24,41 |
| Rapida 1H V1 | TREND_UP | 1 | 45 | 45 | 42,22% | 0,99 | -0,00R | €-2,18 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 3 | 18 | 18 | 33,33% | 0,65 | -0,26R | €-45,94 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,20 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,63 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 2 | 12 | 12 | 25,00% | 0,44 | -0,45R | €-53,75 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,63 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 2 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 2 | 10 | 10 | 20,00% | 0,33 | -0,56R | €-56,45 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,93 | 0,40R | €20,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 2 | 6 | 6 | 16,67% | 0,26 | -0,65R | €-38,77 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 4 | 5 | 5 | 20,00% | 0,44 | -0,47R | €-23,25 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 1,69 | 0,38R | €7,61 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,89 |
| Rapida 1H V2 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,66 | -0,24R | €-21,76 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 2 | 3 | 3 | 100,00% | ∞ | 1,43R | €42,76 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-2,77 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 28 | 28 | 50,00% | 1,37 | 0,19R | €53,97 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 3 | 17 | 17 | 29,41% | 0,54 | -0,35R | €-59,70 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 2 | 9 | 9 | 22,22% | 0,38 | -0,51R | €-46,32 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 2 | 5 | 5 | 20,00% | 0,31 | -0,61R | €-30,25 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 2 | 5 | 5 | 20,00% | 0,31 | -0,61R | €-30,25 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 2 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,96 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 2 | 12 | 12 | 25,00% | 0,43 | -0,46R | €-54,65 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 2 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 2 | 10 | 10 | 20,00% | 0,33 | -0,57R | €-57,34 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 2 | 15 | 15 | 26,67% | 0,98 | -0,01R | €-1,81 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 10 | 10 | 40,00% | 1,81 | 0,50R | €49,91 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 50,00% | 1,24 | 0,13R | €2,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 11 | 11 | 45,45% | 1,06 | 0,04R | €4,23 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 3 | 3 | 3 | 66,67% | 3,57 | 0,91R | €27,40 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 2 | 4 | 4 | 50,00% | 1,87 | 0,44R | €17,68 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,47 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 17 | 17 | 47,06% | 1,64 | 0,36R | €60,98 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 3 | 27 | 27 | 48,15% | 1,74 | 0,40R | €108,26 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 5 | 7 | 7 | 28,57% | 0,74 | -0,19R | €-13,44 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 100,00% | ∞ | 1,89R | €37,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 5 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,46 | -0,45R | €-22,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 3 | 3 | 66,67% | 3,57 | 0,91R | €27,40 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 2 | 5 | 5 | 40,00% | 1,21 | 0,13R | €6,57 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 3 | 19 | 19 | 47,37% | 1,71 | 0,39R | €73,37 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 5 | 9 | 9 | 22,22% | 0,52 | -0,39R | €-35,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 3 | 3 | 3 | 66,67% | 3,57 | 0,91R | €27,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 100,00% | ∞ | 1,89R | €37,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 5 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,09 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,71 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 7 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,08 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 2 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,71 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 2 | 2 | 50,00% | 2,71 | 0,91R | €18,27 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 4 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,39 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 3 | 2 | 2 | 50,00% | 2,71 | 0,91R | €18,27 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 3 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 4 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,39 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 2 | 2 | 50,00% | 2,10 | 0,57R | €11,44 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 13 | 13 | 38,46% | 1,08 | 0,05R | €6,95 |
| SHADOW_COMBO_SCANNER | TREND_UP | 3 | 18 | 18 | 50,00% | 2,05 | 0,55R | €99,87 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 50,00% | 2,05 | 0,55R | €32,82 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 3 | 2 | 2 | 50,00% | 1,91 | 0,50R | €10,05 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 2 | 3 | 3 | 66,67% | 4,26 | 1,10R | €33,07 |
| SHADOW_COMBO_TREND | RANGE | 0 | 8 | 8 | 12,50% | 0,29 | -0,67R | €-53,33 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 21 | 21 | 38,10% | 1,28 | 0,18R | €37,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 4 | 7 | 7 | 28,57% | 0,82 | -0,13R | €-9,36 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 2 | 2 | 50,00% | 2,19 | 0,65R | €13,05 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 12,50% | 0,32 | -0,64R | €-51,15 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 66,67% | 4,47 | 1,25R | €37,51 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 3 | 2 | 2 | 50,00% | 1,93 | 0,51R | €10,21 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 3 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 9 | 9 | 11,11% | 0,29 | -0,59R | €-53,03 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 27 | 27 | 33,33% | 1,09 | 0,06R | €15,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 4 | 7 | 7 | 42,86% | 1,56 | 0,33R | €22,97 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,90R | €19,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 4 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,66 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 5 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 6 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 5 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 6 | 4 | 4 | 0,00% | 0,00 | -1,08R | €-43,07 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 5 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,43 |
| Forza relativa 1H V1 | RANGE | 0 | 20 | 20 | 20,00% | 0,55 | -0,36R | €-71,11 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 13 | 13 | 46,15% | 1,81 | 0,45R | €58,14 |
| Forza relativa 1H V1 | TREND_UP | 4 | 33 | 33 | 39,39% | 1,60 | 0,32R | €106,06 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 2,11R | €21,13 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,52R | €10,34 |
| Forza relativa 1H V2 | RANGE | 0 | 3 | 3 | 66,67% | 4,31 | 1,12R | €33,59 |
| Forza relativa 1H V2 | TRANSITION | 2 | 9 | 8 | 33,33% | 1,05 | 0,03R | €3,12 |
| Forza relativa 1H V2 | TREND_UP | 0 | 10 | 9 | 50,00% | 2,12 | 0,58R | €57,73 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 1,90R | €38,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 7 | 7 | 0,00% | 0,00 | -1,08R | €-75,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 1 | 12 | 12 | 33,33% | 0,98 | -0,01R | €-1,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 2,12 | 0,58R | €23,08 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 5 | 5 | 60,00% | 5,82 | 1,06R | €53,24 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 3 | 17 | 17 | 47,06% | 1,84 | 0,47R | €79,16 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 50,00% | 2,05 | 0,55R | €32,82 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,71 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 33,33% | 1,01 | 0,00R | €0,29 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,09 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,09 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,55 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 6 | 6 | 66,67% | 7,07 | 1,12R | €67,10 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,31 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 3 | 26 | 26 | 50,00% | 1,85 | 0,45R | €116,81 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 50,00% | 1,83 | 0,44R | €26,30 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-22T18:38:43+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **293**
- Scenari virtuali ancora attivi: **2668**
- Gruppi in attesa dell'uscita originale: **153**
- Gruppi con originale chiuso ma Shadow ancora attive: **140**
- Confronti completati: **9916**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 459 | 520 | +€7,95 | 47,7% | 122 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 459 | 520 | +€6,16 | 46,5% | 122 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 459 | 520 | +€4,15 | 45,8% | 123 | 10 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 459 | 520 | +€3,28 | 46,2% | 131 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 459 | 520 | +€2,18 | 45,0% | 118 | 19 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 451 | 512 | +€4,88 | 38,7% | 104 | 16 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 451 | 512 | +€3,38 | 38,1% | 96 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 451 | 512 | +€2,54 | 37,3% | 111 | 16 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 451 | 512 | +€2,00 | 38,1% | 76 | 45 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 450 | 511 | +€0,49 | 51,1% | 109 | 51 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 449 | 510 | +€1,16 | 35,7% | 51 | 82 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 442 | 503 | €-2,95 | 29,6% | 33 | 110 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 435 | 496 | €-4,97 | 25,6% | 38 | 119 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 424 | 485 | +€5,13 | 46,0% | 41 | 90 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 421 | 482 | +€2,18 | 29,0% | 48 | 46 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 420 | 481 | €-7,88 | 22,9% | 35 | 110 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 416 | 477 | €-7,70 | 26,6% | 85 | 60 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 389 | 450 | +€0,36 | 32,0% | 22 | 104 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 376 | 437 | +€3,88 | 33,2% | 20 | 53 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 376 | 436 | €-13,81 | 17,7% | 34 | 97 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-22T18:38:44+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **9916**
- Valutazioni prodotte: **3283**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 444 | 0,056 | 0,043 | -0,018 | 54,5% | 81,4 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| TP_R050 | 453 | 0,116 | 0,000 | 0,040 | 47,0% | 73,8 | VALIDATING |
| GB30_R050 | 453 | 0,157 | 0,000 | 0,085 | 47,5% | 73,8 | VALIDATING |
| GB40_R050 | 453 | 0,117 | 0,000 | 0,046 | 47,0% | 73,7 | VALIDATING |
| GB20_R050 | 453 | 0,191 | 0,000 | 0,113 | 48,8% | 73,7 | VALIDATING |
| GB20_R100 | 445 | 0,113 | 0,000 | 0,061 | 38,7% | 73,5 | VALIDATING |
| GB30_R100 | 445 | 0,087 | 0,000 | 0,036 | 38,2% | 73,5 | VALIDATING |
| GB40_R100 | 445 | 0,064 | 0,000 | 0,013 | 38,2% | 73,3 | VALIDATING |
| GB50_R100 | 443 | 0,048 | 0,000 | -0,002 | 35,9% | 72,8 | VALIDATING |
| TIME_12H | 418 | 0,121 | 0,000 | 0,049 | 47,8% | 72,8 | VALIDATING |
| TP_R100 | 445 | 0,082 | 0,000 | 0,026 | 36,9% | 69,8 | VALIDATING |
| TP_R150 | 415 | 0,069 | 0,000 | 0,011 | 28,9% | 69,4 | VALIDATING |
| TP_R200 | 370 | 0,083 | 0,000 | 0,013 | 33,8% | 69,1 | VALIDATING |
| GB50_R050 | 453 | 0,073 | 0,000 | 0,009 | 46,4% | 66,0 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TIME_24H | 383 | 0,021 | 0,000 | -0,081 | 31,1% | 44,5 | VALIDATING |
| ATR15_R100 | 436 | -0,039 | 0,000 | -0,087 | 29,4% | 33,2 | VALIDATING |
| BE_R050 | 410 | -0,087 | 0,000 | -0,162 | 29,5% | 32,1 | UNDERPERFORMING |
| ATR20_R100 | 429 | -0,086 | 0,000 | -0,141 | 24,7% | 31,0 | UNDERPERFORMING |

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

Generato: 2026-07-22T18:38:49+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 1 | 100,00% | 0,00 | €-54,51 | €-54,51 | 0,55% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 1 | 100,00% | 0,00 | €-54,51 | €-54,51 | 0,55% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-22T18:38:35+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **6**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **14.14 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 126 | 0 | 21487.81 |
| DOWN_20 | 126 | 0 | 42975.63 |
| DOWN_30 | 126 | 1 | 64482.75 |
| DOWN_40 | 126 | 38 | 79914.46 |
| UP_10 | 40 | 0 | 7254.33 |
| UP_20 | 40 | 0 | 14508.66 |
| UP_30 | 40 | 0 | 21762.99 |
| UP_40 | 40 | 13 | 27401.44 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-22T18:38:12+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **0**
- Nuovi candidati nel ciclo: **0**
- Evidenze rifiutate nel ciclo: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Regola di mutazione

Ogni candidato è una copia indipendente del genitore e cambia un solo parametro scalare. Il file principale paper_trading_config.json non viene riscritto.

## Candidati attivi

| Candidato | Genitore | Parametro | Vecchio | Nuovo | Scenario |
| --- | --- | --- | ---: | ---: | --- |
| — | — | — | — | — | — |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-22T18:38:49+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **0**
- Pronti per revisione promozione: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Confronto

| Candidato | Genitore | Stato | Coppie | Δ medio R | CI basso | PF cand. | PF gen. | DD cand. | DD gen. | Score |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| — | — | Nessun candidato attivo | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-07-22T18:38:49+00:00

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

Generato: 2026-07-22T18:38:49+00:00

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

Generato: 2026-07-22T18:38:50+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **76**
- Hall of Fame: **3**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_BALANCED | BASELINE | 14.7 | E | 30 | 1.48 | 0.178 | 3.70 |
| 2 | SHADOW_1H_FAST_V3 | BASELINE | 9.1 | E | 47 | 0.99 | -0.002 | 5.36 |
| 3 | SHADOW_1H_FAST | BASELINE | 5.6 | E | 54 | 0.84 | -0.080 | 12.39 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-22T18:38:50+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **284**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **142**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 2 | SHADOW_RSI_LONG_15X_10_RSI25 | shadow-rsi-long-15x-10-rsi25 | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.984 | 0.00 |
| 3 | SHADOW_RSI_LONG_15X_50_RSI25 | shadow-rsi-long-15x-50-rsi25 | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.984 | 0.00 |
| 4 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.524 | 0.00 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 77.8 | 18 | 2.10 | 0.333 | 1.10 |
| 6 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 7 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 69.1 | 17 | 1.87 | 0.328 | 3.09 |
| 8 | SHADOW_RSI_LONG_5X_RSI25 | shadow-rsi-long-5x-rsi25 | INSUFFICIENT | 65.0 | 2 | 10.75 | 0.262 | 0.05 |
| 9 | SHADOW_1H_FAST_V2 | shadow-1h-fast-v2 | INSUFFICIENT | 64.2 | 3 | 5.86 | 0.380 | 0.23 |
| 10 | SHADOW_1H_BALANCED_V3 | shadow-1h-balanced-v3 | OBSERVING | 63.5 | 15 | 1.69 | 0.339 | 3.15 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-22T18:38:50+00:00

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

Generato: 2026-07-22T18:38:35+00:00

> Ultimo livello di osservabilità della pipeline. Non ripara, non riavvia, non modifica strategie o posizioni e non invia ordini.

## Stato generale

- Salute: **HEALTHY**
- Pipeline completa: **SI**
- Live bloccato: **SI**
- Persistenza completa: **SI**
- Catena audit valida: **SI**
- Recovery readiness: **READY**
- Controlli: **34**
- Warning: **0**
- Critici: **0**

## Controlli non superati

| Categoria | Controllo | Stato | Severità | Dettaglio |
| --- | --- | --- | --- | --- |
| — | Tutti i controlli | PASS | INFO | Nessuna anomalia |

## Sicurezza

- Riparazioni automatiche: **0**
- Riavvii automatici: **0**
- Mutazioni/promozioni/rollback/rilasci automatici: **0**
- Modifiche live: **NO**
- Ordini reali: **0**
