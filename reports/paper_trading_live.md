# Paper trading automatico KuCoin

Generato: 2026-07-21T06:53:42+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-21T06:53:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-21T06:53:25+00:00 | 2026-07-21T06:53:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-21T06:30:00+00:00 | 2026-07-21T06:30:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-21T05:00:00+00:00 | 2026-07-21T05:00:00+00:00 | 53,5 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-21T00:00:00+00:00 | 2026-07-21T00:00:00+00:00 | 2,89 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 7,01 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,94 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 6,80 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | NIGHT | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,82 | 6,00 | 1,18 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 2,89 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,43 | 6,00 | 1,57 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,18 | 6,00 | 1,82 | STALE_CANDLE | 2,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,78 | 6,00 | 2,22 | STALE_CANDLE | 2,89 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,05 | 6,00 | 5,95 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Scalp RSI Long 25 · €10 · 15x | BANK | 15m | LONG | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤25.0, stop tecnico ≤5.0%. RSI 26.6→44.8; volume x3.95; shock 1.68 ATR. |
| Scalp RSI Long 25 · €50 · 15x | BANK | 15m | LONG | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤25.0, stop tecnico ≤5.0%. RSI 26.6→44.8; volume x3.95; shock 1.68 ATR. |
| Scalp RSI Long 25 · prudente · 5x | BANK | 15m | LONG | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤25.0, stop tecnico ≤5.0%. RSI 26.6→44.8; volume x3.95; shock 1.68 ATR. |
| Scalp RSI Long 15 · €10 · 15x | BANK | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |
| Scalp RSI Long 20 · €10 · 15x | BANK | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |
| Scalp RSI Long 15 · €50 · 15x | BANK | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |
| Scalp RSI Long 20 · €50 · 15x | BANK | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |
| Scalp RSI Long 15 · prudente · 5x | BANK | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.883,62 | -1,16% | €-116,38 | €3.000,00 | -3,88% | 4 | 16 | 31,25% | 0,81 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 16 | 243 | CAMPIONE INSUFFICIENTE | 30 (mancano 14) |

- Trade del Principale 4H chiusi: **16**; win rate **31,25%**; profit factor **0,81**.
- Expectancy: **€-6,29** per trade; P&L netto: **€-100,68**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.883,62 | €1.552,19 | €4.656,58 | €197,65 | €-14,78 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.497,72 | €3.540,41 | €7.080,81 | €104,19 | €73,86 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.472,31 | €3.363,52 | €6.727,04 | €103,50 | €90,12 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.281,89 | €3.152,26 | €9.456,78 | €51,19 | €167,55 |
| TEST | Combo Adaptive — madre | 3 | €10.244,15 | €2.743,84 | €5.487,67 | €153,54 | €1,52 |
| TEST | Combo Mean Reversion | 0 | €10.195,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €10.162,61 | €1.309,65 | €2.619,30 | €100,67 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.162,20 | €2.352,79 | €4.705,59 | €101,96 | €7,61 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.150,62 | €3.909,27 | €7.818,54 | €50,00 | €156,06 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.150,62 | €3.909,27 | €7.818,54 | €50,00 | €156,06 |
| TEST | Bilanciata 1H V1 | 4 | €10.139,58 | €2.802,69 | €8.408,06 | €151,29 | €62,96 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.139,36 | €1.300,59 | €2.601,19 | €50,76 | €-11,19 |
| TEST | Ampia 4H | 4 | €10.129,20 | €1.846,89 | €3.693,78 | €200,81 | €-9,70 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €10.128,00 | €3.985,76 | €7.971,52 | €99,98 | €132,79 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €10.128,00 | €3.985,76 | €7.971,52 | €99,98 | €132,79 |
| TEST | Forza relativa 1H V1 | 4 | €10.094,80 | €2.508,00 | €5.016,01 | €151,36 | €1,50 |
| TEST | Top 5 + BTC — solo MFE | 3 | €10.074,97 | €4.191,32 | €8.382,63 | €100,30 | €42,37 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €10.057,11 | €1.639,93 | €3.279,86 | €150,82 | €1,34 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.049,58 | €3.979,16 | €11.937,49 | €99,97 | €56,74 |
| TEST | Rapida V1 — senza PEPE | 3 | €10.049,58 | €3.979,16 | €11.937,49 | €99,97 | €56,74 |
| TEST | Rapida V1 — target pieno 2R | 3 | €10.049,58 | €3.979,16 | €11.937,49 | €99,97 | €56,74 |
| TEST | Rapida V3 — score <7,5 | 3 | €10.049,58 | €3.979,16 | €11.937,49 | €99,97 | €56,74 |
| TEST | Rapida V3 — Long Only | 3 | €10.049,58 | €3.979,16 | €11.937,49 | €99,97 | €56,74 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €10.049,58 | €3.979,16 | €11.937,49 | €99,97 | €56,74 |
| TEST | Combo Adaptive — Long Only | 2 | €10.047,43 | €2.785,91 | €5.571,82 | €100,29 | €20,90 |
| TEST | Sol Donchian 1H | 1 | €10.038,20 | €1.127,14 | €3.381,43 | €0,00 | €44,75 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €10.036,73 | €3.867,98 | €11.603,95 | €149,95 | €43,70 |
| TEST | Sol Ema 1H | 1 | €10.028,76 | €1.001,44 | €3.004,32 | €49,95 | €39,76 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 2 | €10.022,51 | €2.380,74 | €7.142,21 | €99,99 | €26,79 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €10.022,51 | €2.380,74 | €7.142,21 | €99,99 | €26,79 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €10.022,51 | €2.380,74 | €7.142,21 | €99,99 | €26,79 |
| TEST | Sol Adaptive 1H | 1 | €10.019,44 | €1.000,51 | €3.001,52 | €49,91 | €39,72 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.014,01 | €1.105,63 | €2.211,26 | €50,00 | €14,79 |
| TEST | Btc Donchian 4H | 1 | €10.014,01 | €1.105,63 | €2.211,26 | €50,00 | €14,79 |
| TEST | Master Adaptive V1 | 3 | €10.012,25 | €3.945,23 | €7.890,46 | €149,97 | €16,99 |
| TEST | Master Adaptive No Alt V1 | 3 | €10.012,25 | €3.945,23 | €7.890,46 | €149,97 | €16,99 |
| TEST | Master Adaptive Expanded V1 | 3 | €10.012,25 | €3.945,23 | €7.890,46 | €149,97 | €16,99 |
| TEST | Master Adaptive Gb20 V1 | 3 | €10.012,25 | €3.945,23 | €7.890,46 | €149,97 | €16,99 |
| TEST | Master Adaptive Runner25 V1 | 3 | €10.012,25 | €3.945,23 | €7.890,46 | €149,97 | €16,99 |
| TEST | Master Adaptive Strict3 V1 | 2 | €10.011,64 | €2.777,61 | €5.555,22 | €99,99 | €14,97 |
| TEST | Combo Adaptive — Quality7 | 1 | €10.007,05 | €1.067,59 | €2.135,18 | €50,00 | €8,33 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €10.007,05 | €1.067,59 | €2.135,18 | €50,00 | €8,33 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €10.007,05 | €1.067,59 | €2.135,18 | €50,00 | €8,33 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 2 | €10.006,11 | €2.750,25 | €5.500,49 | €50,00 | €64,78 |
| TEST | Combo Adaptive — target pieno 3R | 2 | €10.006,11 | €2.750,25 | €5.500,49 | €50,00 | €64,78 |
| TEST | Rapida 1H V2 | 0 | €10.004,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.992,61 | €2.770,71 | €5.541,41 | €99,74 | €20,79 |
| TEST | Eth Adaptive 1H | 1 | €9.982,59 | €1.054,45 | €3.163,36 | €49,74 | €36,62 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 2 | €9.969,83 | €2.764,39 | €5.528,78 | €99,52 | €20,74 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.967,95 | €1.532,77 | €4.598,30 | €99,11 | €38,31 |
| TEST | Btc Adaptive 1H | 1 | €9.967,33 | €1.151,09 | €3.453,28 | €49,73 | €23,09 |
| TEST | Combo Scanner | 2 | €9.961,40 | €1.577,94 | €3.155,88 | €99,71 | €1,49 |
| TEST | Eth Donchian 1H | 1 | €9.957,48 | €1.144,51 | €3.433,53 | €0,00 | €70,72 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €9.956,52 | €3.884,98 | €11.654,94 | €148,85 | €52,49 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.950,89 | €2.212,42 | €4.424,84 | €149,11 | €25,54 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.944,75 | €1.144,78 | €3.434,35 | €0,00 | €54,43 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.914,16 | €1.287,72 | €3.863,16 | €49,45 | €25,83 |
| TEST | Eth Ema 1H | 1 | €9.905,44 | €1.012,80 | €3.038,40 | €0,00 | €62,58 |
| TEST | Rapida 1H V1 — madre | 4 | €9.897,90 | €3.037,61 | €9.112,84 | €196,10 | €-15,96 |
| TEST | Top 5 + BTC — Guard | 1 | €9.886,87 | €1.054,77 | €2.109,54 | €49,40 | €8,23 |
| TEST | Top 5 + BTC — Guard + MFE | 1 | €9.886,87 | €1.054,77 | €2.109,54 | €49,40 | €8,23 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 0 | €9.881,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.881,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 1 | €9.811,14 | €207,40 | €414,80 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.773,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.734,38 | €2.612,79 | €5.225,58 | €48,50 | €40,14 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.883,62 | €-100,68 | 16 | 16 | 31,25% | 0,81 | €-6,29 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.497,72 | €428,53 | 24 | 24 | 50,00% | 2,02 | €17,86 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.472,31 | €386,68 | 17 | 17 | 47,06% | 2,37 | €22,75 | 1,62% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.281,89 | €120,58 | 23 | 23 | 39,13% | 1,19 | €5,24 | 2,20% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.244,15 | €246,18 | 16 | 16 | 43,75% | 2,08 | €15,39 | 1,27% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.195,13 | €195,13 | 7 | 7 | 57,14% | 2,81 | €27,88 | 0,59% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.162,61 | €164,02 | 18 | 18 | 33,33% | 1,33 | €9,11 | 2,32% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.162,20 | €157,42 | 15 | 15 | 46,67% | 1,46 | €10,49 | 1,98% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.150,62 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,49% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.150,62 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,49% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.139,58 | €81,68 | 21 | 21 | 42,86% | 1,21 | €3,89 | 1,81% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.139,36 | €152,11 | 15 | 15 | 46,67% | 1,66 | €10,14 | 2,06% |
| TEST | Ampia 4H | Confluenza trend | €10.129,20 | €139,54 | 11 | 11 | 27,27% | 1,50 | €12,69 | 2,08% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.128,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.128,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.094,80 | €96,51 | 16 | 16 | 37,50% | 1,37 | €6,03 | 2,29% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €10.074,97 | €37,69 | 1 | 1 | 100,00% | ∞ | €37,69 | 0,54% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Combo Trend | Combo Trend | €10.057,11 | €57,96 | 15 | 15 | 33,33% | 1,15 | €3,86 | 2,19% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.049,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.049,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.049,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.049,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €10.049,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.049,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.047,43 | €29,88 | 2 | 2 | 50,00% | 1,45 | €14,94 | 0,50% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.038,20 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,55% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.036,73 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,15% |
| TEST | Sol Ema 1H | Trend following EMA | €10.028,76 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,98% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.022,51 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,12% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €10.022,51 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,12% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €10.022,51 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,12% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.019,44 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,99% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Ema 4H | Trend following EMA | €10.014,01 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.014,01 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €10.012,25 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €10.012,25 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €10.012,25 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €10.012,25 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €10.012,25 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €10.011,64 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,09% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.007,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,09% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €10.007,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,09% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €10.007,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,09% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €10.006,11 | €-54,84 | 1 | 1 | 0,00% | 0,00 | €-54,84 | 0,36% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €10.006,11 | €-54,84 | 1 | 1 | 0,00% | 0,00 | €-54,84 | 0,36% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.004,31 | €4,31 | 3 | 2 | 33,33% | 1,07 | €1,44 | 0,93% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
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
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,97 | €-4,03 | 4 | 4 | 25,00% | 0,18 | €-1,01 | 0,04% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.992,61 | €-24,85 | 3 | 3 | 33,33% | 0,80 | €-8,28 | 0,68% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.982,59 | €-51,89 | 2 | 2 | 50,00% | 0,05 | €-25,94 | 1,02% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.969,83 | €-47,59 | 3 | 3 | 33,33% | 0,61 | €-15,86 | 0,68% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.967,95 | €-67,37 | 16 | 14 | 43,75% | 0,84 | €-4,21 | 2,75% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.967,33 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,89% |
| TEST | Combo Scanner | Combo Scanner | €9.961,40 | €-37,94 | 18 | 18 | 38,89% | 0,92 | €-2,11 | 1,95% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.957,48 | €-110,95 | 2 | 2 | 0,00% | 0,00 | €-55,48 | 1,38% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.956,52 | €-88,97 | 37 | 37 | 35,14% | 0,89 | €-2,40 | 2,89% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.950,89 | €-72,00 | 9 | 9 | 33,33% | 0,77 | €-8,00 | 2,25% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Btc Ema 1H | Trend following EMA | €9.944,75 | €-109,08 | 2 | 2 | 0,00% | 0,00 | €-54,54 | 1,56% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.914,16 | €-110,32 | 2 | 2 | 0,00% | 0,00 | €-55,16 | 1,49% |
| TEST | Eth Ema 1H | Trend following EMA | €9.905,44 | €-155,12 | 4 | 4 | 25,00% | 0,05 | €-38,78 | 1,59% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.897,90 | €-80,68 | 47 | 47 | 34,04% | 0,93 | €-1,72 | 5,36% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.886,87 | €-120,09 | 2 | 2 | 0,00% | 0,00 | €-60,05 | 1,28% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.886,87 | €-120,09 | 2 | 2 | 0,00% | 0,00 | €-60,05 | 1,28% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.881,42 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,19% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.881,42 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,19% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.811,14 | €-188,61 | 12 | 12 | 25,00% | 0,42 | €-15,72 | 3,75% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.773,98 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,46% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.734,38 | €-302,40 | 21 | 21 | 28,57% | 0,36 | €-14,40 | 3,44% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07320 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €-6,73 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 550,99000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-8,06 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1894,43881 | 1933,46000 | 1913,83676 | 1272,43140 | 1955,82155 | €1.043,85 | €3.131,56 | €0,00 | €64,50 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,13540 | 1,13490 | 1,11905 | 0,76261 | 1,16810 | €1.172,10 | €3.516,30 | €50,63 | €-1,54 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €684,20 | €2.052,59 | €0,00 | €38,31 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1894,43881 | 1933,46000 | 1913,83676 | 1272,43140 | 1955,82155 | €1.047,36 | €3.142,08 | €0,00 | €64,72 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,11148 | 1,13490 | 1,12362 | 0,74655 | 1,14349 | €1.163,70 | €3.491,09 | €0,00 | €73,55 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17417 | 0,17630 | 0,17046 | 0,11699 | 0,18161 | €799,70 | €2.399,09 | €51,19 | €29,27 |
| Rapida 1H V1 — madre | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 — madre | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00173 | 0,00168 | 0,00154 | 0,00116 | 0,00202 | €147,41 | €442,24 | €49,70 | €-14,02 |
| Rapida 1H V1 — madre | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,15447 | €1.476,35 | €4.429,06 | €49,61 | €-1,94 |
| Rapida V1 — score 6–7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-1,95 |
| Rapida V1 — score 6–7,5 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €0,00 | €36,75 |
| Rapida V1 — score 6–7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1933,46000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €21,95 |
| Rapida V1 — no HIGH + score <7,5 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17562 | 0,17630 | 0,17242 | 0,11795 | 0,18041 | €915,08 | €2.745,23 | €50,00 | €10,71 |
| Rapida V1 — no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 62,98259 | 63,21300 | 62,26655 | 42,30331 | 64,05666 | €1.465,66 | €4.396,98 | €49,99 | €16,09 |
| Rapida V1 — senza PEPE | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-1,95 |
| Rapida V1 — senza PEPE | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €0,00 | €36,75 |
| Rapida V1 — senza PEPE | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1933,46000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €21,95 |
| Rapida V1 — target pieno 2R | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,16083 | €1.488,10 | €4.464,29 | €50,00 | €-1,95 |
| Rapida V1 — target pieno 2R | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17996 | €1.003,86 | €3.011,59 | €0,00 | €36,75 |
| Rapida V1 — target pieno 2R | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1933,46000 | 1902,44598 | 1292,28312 | 1967,09220 | €1.487,21 | €4.461,62 | €49,97 | €21,95 |
| Rapida 1H V3 Filtered — madre | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered — madre | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17851 | €997,39 | €2.992,17 | €0,00 | €36,51 |
| Rapida 1H V3 Filtered — madre | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13084 | 1,13490 | 1,11817 | 0,75954 | 1,14983 | €1.481,92 | €4.445,76 | €49,79 | €15,98 |
| Rapida V3 — score <7,5 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-1,95 |
| Rapida V3 — score <7,5 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €0,00 | €36,75 |
| Rapida V3 — score <7,5 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1933,46000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €21,95 |
| Rapida V3 — no volatilità HIGH | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13062 | 1,13490 | 1,11795 | 0,75940 | 1,14961 | €1.488,10 | €4.464,29 | €50,00 | €16,92 |
| Rapida V3 — no volatilità HIGH | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17562 | 0,17630 | 0,17242 | 0,11795 | 0,18041 | €914,75 | €2.744,25 | €49,98 | €10,70 |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 62,98259 | 63,21300 | 62,26655 | 42,30331 | 64,05666 | €1.465,14 | €4.395,41 | €49,97 | €16,08 |
| Rapida V3 — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-1,95 |
| Rapida V3 — Long Only | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €0,00 | €36,75 |
| Rapida V3 — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1933,46000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €21,95 |
| Rapida V3 — Long + no HIGH + score <7,5 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17562 | 0,17630 | 0,17242 | 0,11795 | 0,18041 | €915,08 | €2.745,23 | €50,00 | €10,71 |
| Rapida V3 — Long + no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 62,98259 | 63,21300 | 62,26655 | 42,30331 | 64,05666 | €1.465,66 | €4.396,98 | €49,99 | €16,09 |
| Rapida V3 — senza ESPORTS | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13490 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-1,95 |
| Rapida V3 — senza ESPORTS | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17630 | 0,17417 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €0,00 | €36,75 |
| Rapida V3 — senza ESPORTS | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1933,46000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €21,95 |
| Rapida V3 — qualità completa + profit lock | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17562 | 0,17630 | 0,17242 | 0,11795 | 0,18041 | €915,08 | €2.745,23 | €50,00 | €10,71 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 62,98259 | 63,21300 | 62,26655 | 42,30331 | 64,05666 | €1.465,66 | €4.396,98 | €49,99 | €16,09 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07320 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-14,96 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 550,99000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €36,45 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 63,21300 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-47,73 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €16,55 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €986,47 | €1.972,93 | €50,47 | €1,50 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17562 | 0,17630 | 0,17105 | 0,08869 | 0,18704 | €975,80 | €1.951,59 | €50,78 | €7,61 |
| Benchmark Bollinger mean reversion 1H | ADA | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,17554 | 0,17630 | 0,17897 | 0,26244 | 0,17041 | €1.300,59 | €2.601,19 | €50,76 | €-11,19 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,17417 | 0,17630 | 0,17005 | 0,08796 | 0,18326 | €1.046,69 | €2.093,39 | €49,63 | €25,54 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,11469 | 1,13490 | 1,12400 | 0,56292 | 1,14680 | €1.796,54 | €3.593,08 | €0,00 | €65,14 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.118,38 | €2.236,77 | €52,38 | €8,72 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.070,89 | €2.141,78 | €0,00 | €53,44 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 78,59100 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €36,68 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,76655 | 78,59100 | 77,76655 | 39,27211 | 80,43319 | €1.603,37 | €3.206,74 | €0,00 | €34,00 |
| Top 5 + BTC — solo MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18466 | €1.073,91 | €2.147,81 | €50,30 | €8,38 |
| Top 5 + BTC — Guard | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €8,23 |
| Top 5 + BTC — BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €6,44 |
| Top 5 + BTC — BTC≤3 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16982 | 0,17630 | 0,17429 | 0,08576 | 0,17769 | €1.187,43 | €2.374,86 | €0,00 | €90,59 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,59100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €35,76 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €6,44 |
| Top 5 + BTC — BTC 2–3 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16982 | 0,17630 | 0,17429 | 0,08576 | 0,17769 | €1.187,43 | €2.374,86 | €0,00 | €90,59 |
| Top 5 + BTC — BTC 2–3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,59100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €35,76 |
| Top 5 + BTC — Guard + MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €8,23 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €4,90 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16962 | 0,17630 | 0,17422 | 0,08566 | 0,18059 | €1.159,50 | €2.319,01 | €0,00 | €91,30 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1933,46000 | 1916,33142 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €0,00 | €59,86 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €4,90 |
| Top 5 + BTC — target pieno 3R | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16962 | 0,17630 | 0,17422 | 0,08566 | 0,18059 | €1.159,50 | €2.319,01 | €0,00 | €91,30 |
| Top 5 + BTC — target pieno 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1933,46000 | 1916,33142 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €0,00 | €59,86 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €884,51 | €1.769,01 | €50,29 | €1,34 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €978,80 | €1.957,60 | €50,08 | €1,49 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive — madre | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.001,06 | €2.002,12 | €51,22 | €1,52 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,56451 | 78,59100 | 77,65759 | 39,17008 | 80,14392 | €1.462,23 | €2.924,45 | €0,00 | €38,70 |
| Combo Adaptive — MFE Trail esistente | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €947,94 | €1.895,88 | €48,50 | €1,44 |
| Combo Adaptive — Quality7 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €8,33 |
| Combo Adaptive — Trend/Transition | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.064,94 | €2.129,87 | €49,88 | €8,31 |
| Combo Adaptive — Trend/Transition | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 62,98259 | 63,21300 | 62,06196 | 31,80621 | 64,82385 | €1.705,77 | €3.411,54 | €49,87 | €12,48 |
| Combo Adaptive — Quality7 + Regime | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €8,33 |
| Combo Adaptive — Long Only | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.070,78 | €2.141,56 | €50,15 | €8,35 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 62,98259 | 63,21300 | 62,06196 | 31,80621 | 64,82385 | €1.715,13 | €3.430,26 | €50,14 | €12,55 |
| Combo Adaptive — parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.062,51 | €2.125,02 | €49,76 | €8,29 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 62,98259 | 63,21300 | 62,06196 | 31,80621 | 64,82385 | €1.701,88 | €3.403,76 | €49,75 | €12,45 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17630 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €8,33 |
| Combo Adaptive — 75% a 2R + runner 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €4,90 |
| Combo Adaptive — 75% a 2R + runner 3R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1933,46000 | 1917,89775 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €59,88 |
| Combo Adaptive — target pieno 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €4,90 |
| Combo Adaptive — target pieno 3R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1933,46000 | 1917,89775 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €59,88 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64820,68154 | 65848,00000 | 65478,64574 | 43537,89110 | 66687,51717 | €1.144,78 | €3.434,35 | €0,00 | €54,43 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65848,00000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €14,79 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 65410,57950 | 65848,00000 | 64573,32408 | 43934,10590 | 67085,09034 | €1.287,72 | €3.863,16 | €49,45 | €25,83 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65848,00000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €14,79 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 65410,57950 | 65848,00000 | 64468,66716 | 43934,10590 | 67294,40419 | €1.151,09 | €3.453,28 | €49,73 | €23,09 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 78,59100 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €39,76 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 77,56451 | 78,59100 | 77,71982 | 52,09750 | 79,85731 | €1.127,14 | €3.381,43 | €0,00 | €44,75 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 78,59100 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €39,72 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1894,43881 | 1933,46000 | 1917,32579 | 1272,43140 | 1955,82155 | €1.012,80 | €3.038,40 | €0,00 | €62,58 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1894,43881 | 1933,46000 | 1917,32579 | 1272,43140 | 1949,00125 | €1.144,51 | €3.433,53 | €0,00 | €70,72 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1911,33219 | 1933,46000 | 1881,27848 | 1283,77812 | 1971,43961 | €1.054,45 | €3.163,36 | €49,74 | €36,62 |
| Master Adaptive V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17630 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €3,33 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 63,21300 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €11,64 |
| Master Adaptive V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €2,01 |
| Master Adaptive No Alt V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17630 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €3,33 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 63,21300 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €11,64 |
| Master Adaptive No Alt V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €2,01 |
| Master Adaptive Strict3 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17630 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €3,33 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 63,21300 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €11,64 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17630 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €3,33 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 63,21300 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €11,64 |
| Master Adaptive Expanded V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €2,01 |
| Master Adaptive Gb20 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17630 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €3,33 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 63,21300 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €11,64 |
| Master Adaptive Gb20 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €2,01 |
| Master Adaptive Runner25 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17630 | 0,17190 | 0,08889 | 0,18839 | €1.067,59 | €2.135,18 | €50,00 | €3,33 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 63,21300 | 62,07773 | 31,81429 | 65,76119 | €1.710,02 | €3.420,04 | €49,99 | €11,64 |
| Master Adaptive Runner25 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €2,01 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07298 | €-54,16 | -1,10 | STOP |
| Global Confluence puro 1H | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07309 | €-53,48 | -1,09 | STOP |
| Combo Scanner | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07298 | €-54,94 | -1,10 | STOP |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07298 | €-54,84 | -1,10 | STOP |
| Combo Adaptive — 75% a 2R + runner 3R | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07298 | €-54,84 | -1,10 | STOP |
| Combo Adaptive — Trend/Transition | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07298 | €-54,73 | -1,10 | STOP |
| Combo Adaptive — parziale 1R | DOGE | SHORT | 2026-07-21T06:08:33+00:00 | 0,07298 | €-54,73 | -1,10 | STOP |
| Scanner Top 5 Long 1H | ADA | LONG | 2026-07-21T05:53:32+00:00 | 0,17723 | €99,64 | 1,93 | TARGET |
| Top 5 + BTC — solo MFE | XRP | LONG | 2026-07-21T05:53:32+00:00 | 1,12897 | €37,69 | 0,75 | STOP |
| Top 5 + BTC — Guard | BANK | LONG | 2026-07-21T05:53:32+00:00 | 0,24010 | €-66,54 | -1,33 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — Guard + MFE | BANK | LONG | 2026-07-21T05:53:32+00:00 | 0,24010 | €-66,54 | -1,33 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | 2026-07-21T05:53:32+00:00 | 0,23845 | €-65,00 | -1,30 | STOP_STRESS_SLIPPAGE |

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
| MAIN | Principale 4H | 32/30 | 16/30 | 1,01 | 0,81 | 0,01R | €-6,29 | 4,26% | DIVERGENTE | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 5/30 | 4/30 | 0,32 | 0,30 | -0,55R | €-4,46 | 0,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 112/30 | 21/30 | 1,00 | 1,21 | 0,00R | €3,89 | 1,81% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 17/30 | 14/30 | 1,67 | 0,84 | 0,37R | €-4,21 | 2,75% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 30/30 | 23/30 | 1,43 | 1,19 | 0,25R | €5,24 | 2,20% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 127/30 | 47/30 | 0,93 | 0,93 | -0,04R | €-1,72 | 5,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,12% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 2/30 | 2/30 | 0,59 | 1,07 | -0,31R | €1,44 | 0,93% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 40/30 | 37/30 | 1,23 | 0,89 | 0,13R | €-2,40 | 2,89% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,12% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,12% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,15% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 31/30 | 11/30 | 0,95 | 1,50 | -0,04R | €12,69 | 2,08% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 22/30 | 15/30 | 0,76 | 1,66 | -0,17R | €10,14 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,16 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,19% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,11R | €-54,54 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,19% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 57/30 | 16/30 | 1,67 | 2,08 | 0,37R | €15,39 | 1,27% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 3/30 | 2/30 | 0,95 | 1,45 | -0,03R | €14,94 | 0,50% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 29/30 | 21/30 | 1,53 | 0,36 | 0,30R | €-14,40 | 3,44% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 4/30 | 3/30 | 0,61 | 0,61 | -0,30R | €-15,86 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 4/30 | 3/30 | 0,61 | 0,80 | -0,30R | €-8,28 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 3/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-54,84 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 3/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-54,84 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 8/30 | 7/30 | 2,42 | 2,81 | 0,55R | €27,88 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 36/30 | 18/30 | 1,86 | 0,92 | 0,48R | €-2,11 | 1,95% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 47/30 | 15/30 | 1,17 | 1,15 | 0,11R | €3,86 | 2,19% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 1/30 | 2/30 | 0,00 | 0,46 | -1,12R | €-15,51 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 4/30 | 0,00 | 0,54 | 0,00R | €-12,93 | 1,27% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 25/30 | 15/30 | 0,72 | 1,46 | -0,22R | €10,49 | 1,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 51/30 | 9/30 | 1,13 | 0,77 | 0,09R | €-8,00 | 2,25% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,05 | 0,39R | €-25,94 | 1,02% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,13R | €-55,48 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 2/30 | 4/30 | 1,70 | 0,05 | 0,39R | €-38,78 | 1,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 7/30 | 0,00 | 0,17 | -1,10R | €-32,29 | 2,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 70/30 | 16/30 | 1,09 | 1,37 | 0,06R | €6,03 | 2,29% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 21/30 | 18/30 | 1,62 | 1,33 | 0,36R | €9,11 | 2,32% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 22/30 | 12/30 | 0,56 | 0,42 | -0,35R | €-15,72 | 3,75% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 39/30 | 17/30 | 1,87 | 2,37 | 0,47R | €22,75 | 1,62% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 2/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,51% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 2/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,51% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-60,05 | 1,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-60,05 | 1,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €37,69 | 0,54% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 2/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,49% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 2/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,49% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 50/30 | 24/30 | 1,79 | 2,02 | 0,42R | €17,86 | 2,70% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 0,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-4,49 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 2/30 | 2/30 | 1,70 | 0,83 | 0,39R | €-4,58 | 0,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.0732**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.7 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65848 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07325**; close **0.0732**; wick alta **19.2%**; volume **x1.58**

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
- Confidenza: **81,20%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 83% sopra EMA50, ADX 23.4.
- BTC trend score: **4,00**; ADX: **23,38**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **0,86%**; dispersione: **9,63%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **309**
- Trade research chiusi: **934**
- Eventi di mercato indipendenti chiusi: **349**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **3200**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 13 | 32 | 32 | 34,38% | 1,01 | 0,01R | €2,17 |
| RSI_EXTREME_SHORT_15M | 0 | 5 | 5 | 20,00% | 0,32 | -0,55R | €-27,64 |
| Bilanciata 1H V1 | 14 | 112 | 112 | 34,82% | 1,00 | 0,00R | €3,06 |
| Bilanciata 1H V2 | 6 | 19 | 17 | 47,37% | 1,67 | 0,37R | €70,45 |
| Bilanciata 1H V3 Filtered | 9 | 30 | 30 | 43,33% | 1,43 | 0,25R | €76,23 |
| Rapida 1H V1 | 9 | 127 | 127 | 39,37% | 0,93 | -0,04R | €-54,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V2 | 0 | 3 | 2 | 33,33% | 0,59 | -0,31R | €-9,29 |
| Rapida 1H V3 Filtered | 9 | 40 | 40 | 47,50% | 1,23 | 0,13R | €50,80 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | 17 | 31 | 31 | 25,81% | 0,95 | -0,04R | €-12,70 |
| SHADOW_BOLLINGER_MR_1H | 2 | 22 | 22 | 36,36% | 0,76 | -0,17R | €-36,52 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 14 | 57 | 57 | 47,37% | 1,67 | 0,37R | €212,33 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 3 | 3 | 33,33% | 0,95 | -0,03R | €-1,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 9 | 29 | 29 | 44,83% | 1,53 | 0,30R | €87,53 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 6 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 6 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 6 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 6 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 8 | 8 | 62,50% | 2,42 | 0,55R | €44,38 |
| SHADOW_COMBO_SCANNER | 9 | 36 | 36 | 47,22% | 1,86 | 0,48R | €171,25 |
| SHADOW_COMBO_TREND | 11 | 47 | 47 | 36,17% | 1,17 | 0,11R | €53,30 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 9 | 25 | 25 | 24,00% | 0,72 | -0,22R | €-55,83 |
| SHADOW_EMA_TREND_1H | 14 | 51 | 51 | 35,29% | 1,13 | 0,09R | €43,52 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | 13 | 70 | 70 | 34,29% | 1,09 | 0,06R | €43,34 |
| Forza relativa 1H V2 | 4 | 23 | 21 | 43,48% | 1,62 | 0,36R | €83,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 5 | 22 | 22 | 22,73% | 0,56 | -0,35R | €-76,88 |
| SHADOW_SCANNER_TOP5_BTC | 8 | 39 | 39 | 46,15% | 1,87 | 0,47R | €181,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | 9 | 50 | 50 | 48,00% | 1,79 | 0,42R | €208,18 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_UP | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| MAIN | RANGE | 0 | 14 | 14 | 28,57% | 0,77 | -0,17R | €-23,82 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 4 | 4 | 4 | 25,00% | 0,65 | -0,27R | €-10,68 |
| MAIN | TREND_UP | 1 | 9 | 9 | 44,44% | 1,52 | 0,30R | €27,33 |
| MAIN | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 3 | 3 | 33,33% | 0,50 | -0,42R | €-12,61 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 2,16 | 0,56R | €72,85 |
| Bilanciata 1H V1 | RANGE | 2 | 26 | 26 | 30,77% | 0,86 | -0,10R | €-25,88 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,38 |
| Bilanciata 1H V1 | TRANSITION | 3 | 24 | 24 | 33,33% | 0,90 | -0,07R | €-17,02 |
| Bilanciata 1H V1 | TREND_UP | 3 | 31 | 31 | 41,94% | 1,42 | 0,24R | €75,22 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 5 | 8 | 8 | 37,50% | 1,10 | 0,07R | €5,26 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 4 | 3 | 100,00% | ∞ | 1,93R | €77,01 |
| Bilanciata 1H V2 | RANGE | 2 | 4 | 4 | 50,00% | 1,79 | 0,44R | €17,51 |
| Bilanciata 1H V2 | TRANSITION | 3 | 11 | 10 | 27,27% | 0,71 | -0,22R | €-24,07 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,44 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 15 | 15 | 60,00% | 2,82 | 0,76R | €113,62 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 7 | 7 | 7 | 28,57% | 0,74 | -0,20R | €-13,68 |
| Rapida 1H V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 55,56% | 1,73 | 0,34R | €30,84 |
| Rapida 1H V1 | RANGE | 0 | 35 | 35 | 40,00% | 1,04 | 0,02R | €8,01 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 23 | 23 | 43,48% | 1,20 | 0,11R | €24,41 |
| Rapida 1H V1 | TREND_UP | 2 | 34 | 34 | 47,06% | 1,21 | 0,12R | €40,17 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 6 | 15 | 15 | 33,33% | 0,65 | -0,25R | €-37,60 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 2 | 2 | 100,00% | ∞ | 1,44R | €28,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-2,77 |
| Rapida 1H V3 Filtered | TREND_UP | 2 | 18 | 18 | 61,11% | 2,19 | 0,48R | €86,20 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 6 | 14 | 14 | 28,57% | 0,52 | -0,37R | €-51,36 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 3 | 14 | 14 | 21,43% | 0,74 | -0,21R | €-29,68 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 5 | 5 | 20,00% | 0,69 | -0,25R | €-12,67 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 8 | 8 | 50,00% | 2,70 | 0,88R | €70,18 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 6 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 8 | 8 | 37,50% | 0,77 | -0,16R | €-12,56 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,21 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 3 | 9 | 9 | 33,33% | 0,90 | -0,08R | €-6,79 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 15 | 15 | 53,33% | 2,13 | 0,55R | €82,64 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 23 | 23 | 56,52% | 2,44 | 0,65R | €150,35 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 6 | 6 | 6 | 33,33% | 0,94 | -0,04R | €-2,53 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,95 | -0,03R | €-1,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 4 | 4 | 25,00% | 0,61 | -0,31R | €-12,32 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,91R | €19,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 15 | 15 | 60,00% | 2,88 | 0,77R | €115,46 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 6 | 8 | 8 | 25,00% | 0,61 | -0,31R | €-24,59 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 3 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 18 | 18 | 50,00% | 2,05 | 0,55R | €99,87 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 6 | 3 | 3 | 33,33% | 1,08 | 0,05R | €1,60 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_COMBO_TREND | RANGE | 0 | 8 | 8 | 12,50% | 0,29 | -0,67R | €-53,33 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,72 |
| SHADOW_COMBO_TREND | TREND_UP | 1 | 19 | 19 | 42,11% | 1,50 | 0,30R | €57,72 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 6 | 5 | 5 | 20,00% | 0,53 | -0,39R | €-19,53 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 12,50% | 0,32 | -0,64R | €-51,15 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 1 | 9 | 9 | 44,44% | 1,82 | 0,49R | €44,53 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_EMA_TREND_1H | RANGE | 2 | 8 | 8 | 12,50% | 0,29 | -0,66R | €-52,47 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,70 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 24 | 24 | 37,50% | 1,23 | 0,15R | €36,08 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 7 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,53 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 2 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-8,74 |
| Forza relativa 1H V1 | RANGE | 2 | 18 | 18 | 22,22% | 0,59 | -0,33R | €-60,04 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 12 | 12 | 50,00% | 2,12 | 0,57R | €68,69 |
| Forza relativa 1H V1 | TREND_UP | 5 | 21 | 21 | 47,62% | 1,91 | 0,49R | €103,80 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 2 | 7 | 7 | 14,29% | 0,35 | -0,57R | €-40,04 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 2,10R | €21,00 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 2 | 8 | 8 | 37,50% | 1,26 | 0,17R | €13,67 |
| Forza relativa 1H V2 | TREND_UP | 0 | 8 | 7 | 62,50% | 3,60 | 0,99R | €78,93 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 7 | 7 | 0,00% | 0,00 | -1,08R | €-75,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 3 | 9 | 9 | 44,44% | 1,37 | 0,23R | €20,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,12 | 0,58R | €23,08 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 4 | 4 | 75,00% | 102,98 | 1,59R | €63,66 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 17 | 17 | 47,06% | 1,84 | 0,47R | €79,16 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 6 | 3 | 3 | 33,33% | 1,08 | 0,05R | €1,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 7 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,55 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 5 | 5 | 80,00% | 125,19 | 1,55R | €77,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,31 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 24 | 24 | 50,00% | 1,85 | 0,45R | €108,60 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 5 | 4 | 4 | 50,00% | 1,88 | 0,46R | €18,33 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-21T06:53:39+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **181**
- Scenari virtuali ancora attivi: **2469**
- Gruppi in attesa dell'uscita originale: **144**
- Gruppi con originale chiuso ma Shadow ancora attive: **37**
- Confronti completati: **3008**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 119 | 156 | +€9,67 | 48,1% | 31 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 119 | 156 | +€7,80 | 44,2% | 28 | 3 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 119 | 156 | +€7,55 | 47,4% | 31 | 1 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 119 | 156 | +€5,50 | 44,9% | 27 | 3 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 119 | 156 | +€5,39 | 46,2% | 32 | 2 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 119 | 156 | +€4,79 | 48,1% | 31 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 119 | 156 | +€4,37 | 45,5% | 28 | 7 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 119 | 163 | €-0,41 | 47,2% | 32 | 11 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 117 | 154 | +€4,44 | 42,9% | 28 | 4 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 117 | 154 | +€0,83 | 32,5% | 19 | 20 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 114 | 158 | +€5,30 | 43,0% | 19 | 16 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 113 | 150 | +€3,03 | 43,3% | 21 | 6 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 112 | 148 | +€4,84 | 35,8% | 9 | 21 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 111 | 148 | +€2,03 | 41,9% | 13 | 17 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 111 | 148 | €-5,34 | 31,8% | 31 | 13 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 108 | 145 | €-5,05 | 37,2% | 7 | 25 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 108 | 145 | €-5,91 | 36,6% | 4 | 28 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 99 | 143 | +€1,11 | 36,4% | 11 | 24 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 97 | 130 | €-6,67 | 30,0% | 3 | 27 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 97 | 130 | €-6,98 | 30,0% | 2 | 28 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-21T06:53:40+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **3008**
- Valutazioni prodotte: **2359**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 113 | 0,070 | 0,033 | -0,033 | 55,8% | 80,1 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| TIME_12H | 108 | 0,168 | 0,000 | 0,055 | 46,3% | 72,4 | VALIDATING |
| GB20_R050 | 113 | 0,233 | 0,000 | 0,089 | 47,8% | 70,0 | VALIDATING |
| GB30_R050 | 113 | 0,200 | 0,000 | 0,041 | 46,9% | 70,0 | VALIDATING |
| GB40_R050 | 113 | 0,162 | 0,000 | 0,013 | 46,9% | 70,0 | VALIDATING |
| GB50_R050 | 113 | 0,158 | 0,000 | 0,020 | 46,9% | 69,9 | VALIDATING |
| GB20_R100 | 113 | 0,131 | 0,000 | 0,022 | 43,4% | 69,4 | VALIDATING |
| TP_R050 | 113 | 0,158 | 0,000 | -0,005 | 47,8% | 69,2 | VALIDATING |
| TP_R100 | 113 | 0,100 | 0,000 | -0,009 | 43,4% | 68,0 | VALIDATING |
| GB50_R100 | 105 | 0,072 | 0,000 | -0,017 | 42,9% | 66,4 | VALIDATING |
| GB40_R100 | 107 | 0,065 | 0,000 | -0,032 | 43,0% | 64,3 | VALIDATING |
| GB30_R100 | 111 | 0,071 | 0,000 | -0,042 | 42,3% | 62,9 | VALIDATING |
| TP_R200 | 106 | 0,046 | 0,000 | -0,056 | 35,8% | 60,4 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| BE_R050 | 106 | 0,014 | 0,000 | -0,122 | 39,6% | 40,7 | VALIDATING |
| TP_R150 | 111 | -0,001 | 0,000 | -0,102 | 32,4% | 39,4 | VALIDATING |
| ATR20_R100 | 102 | -0,099 | 0,000 | -0,209 | 37,3% | 38,8 | VALIDATING |
| ATR15_R100 | 102 | -0,060 | 0,000 | -0,144 | 38,2% | 38,2 | VALIDATING |
| TIME_24H | 93 | -0,020 | 0,000 | -0,144 | 34,4% | 33,1 | VALIDATING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-21T06:53:33+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **1**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **5.05 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 122 | 0 | 34566.08 |
| DOWN_20 | 122 | 0 | 69132.17 |
| DOWN_30 | 122 | 0 | 103698.25 |
| DOWN_40 | 122 | 51 | 126532.31 |
| UP_10 | 22 | 0 | 1874.83 |
| UP_20 | 22 | 0 | 3749.65 |
| UP_30 | 22 | 0 | 5624.48 |
| UP_40 | 22 | 9 | 7076.91 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-21T06:53:12+00:00

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

Generato: 2026-07-21T06:53:42+00:00

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

Generato: 2026-07-21T06:53:42+00:00

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

Generato: 2026-07-21T06:53:42+00:00

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

Generato: 2026-07-21T06:53:42+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **49**
- Hall of Fame: **2**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3 | BASELINE | 7.0 | E | 37 | 0.90 | -0.047 | 5.36 |
| 2 | SHADOW_1H_FAST | BASELINE | 6.9 | E | 47 | 0.93 | -0.034 | 9.70 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-21T06:53:42+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **182**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **91**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.524 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.374 | 0.00 |
| 3 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 4 | SHADOW_COMBO_MEAN_REVERSION | shadow-combo-mean-reversion | INSUFFICIENT | 75.5 | 5 | 4.40 | 0.709 | 1.02 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 73.3 | 15 | 2.15 | 0.334 | 1.10 |
| 6 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 72.0 | 15 | 2.06 | 0.375 | 3.09 |
| 7 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 72.0 | 17 | 1.98 | 0.365 | 4.17 |
| 8 | SHADOW_1H_FAST_V2 | shadow-1h-fast-v2 | INSUFFICIENT | 70.6 | 2 | 11.45 | 0.628 | 0.12 |
| 9 | SHADOW_RELATIVE_STRENGTH_V2 | shadow-relative-strength-v2 | OBSERVING | 58.4 | 12 | 1.70 | 0.299 | 4.12 |
| 10 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | OBSERVING | 57.9 | 11 | 1.62 | 0.243 | 2.24 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-21T06:53:42+00:00

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

Generato: 2026-07-21T06:53:33+00:00

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
