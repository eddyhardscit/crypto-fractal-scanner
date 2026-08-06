# Paper trading automatico KuCoin

Generato: 2026-08-06T16:26:50+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-06T16:23:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-06T16:23:29+00:00 | 2026-08-06T16:23:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-06T16:00:00+00:00 | 2026-08-06T16:00:00+00:00 | 8,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-06T15:00:00+00:00 | 2026-08-06T15:00:00+00:00 | 23,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-06T12:00:00+00:00 | 2026-08-06T12:00:00+00:00 | 23,7 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ADA | 240m | LONG | 9,75 | 6,00 | 0,00 | RISK_GATE | 23,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | DOGE | 240m | SHORT | -8,30 | 6,00 | 0,00 | RISK_GATE | 23,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | BLESS | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 23,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | XRP | 240m | SHORT | -6,04 | 6,00 | 0,00 | RISK_GATE | 23,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | CYS | 240m | LONG | 5,25 | 6,00 | 0,75 | BELOW_SCORE | 23,7 min | D: n/a | W: n/a | peso 0 | Punteggio +5.25; soglia ±6.00; mancano 0.75 punti. |
| Principale 4H | ETH | 240m | LONG | 5,17 | 6,00 | 0,83 | BELOW_SCORE | 23,7 min | D: n/a | W: n/a | peso 0 | Punteggio +5.17; soglia ±6.00; mancano 0.83 punti. |
| Principale 4H | SOL | 240m | SHORT | -4,89 | 6,00 | 1,11 | BELOW_SCORE | 23,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Punteggio -4.89; soglia ±6.00; mancano 1.11 punti. |
| Principale 4H | BTC | 240m | LONG | 4,50 | 6,00 | 1,50 | BELOW_SCORE | 23,7 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +4.50; soglia ±6.00; mancano 1.50 punti. |
| Scalp RSI Short 80 · €10 · 15x | ADA | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 8,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €10 · 15x | ADA | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 8,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · €50 · 15x | ADA | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 8,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €50 · 15x | ADA | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 8,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · prudente · 5x | ADA | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 8,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · prudente · 5x | ADA | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 8,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 85 · €10 · 15x | ADA | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,7 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥85.0. RSI 84.4→69.7; volume x3.03; shock 3.95 ATR. |
| Scalp RSI Short 85 · €50 · 15x | ADA | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,7 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥85.0. RSI 84.4→69.7; volume x3.03; shock 3.95 ATR. |
| Scalp RSI Short 85 · prudente · 5x | ADA | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,7 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥85.0. RSI 84.4→69.7; volume x3.03; shock 3.95 ATR. |
| Bilanciata 1H V2 | DOGE | 60m | SHORT | -7,93 | 5,50 | 0,00 | STRATEGY_FILTER | 23,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | DOGE | 60m | SHORT | -7,93 | 4,50 | 0,00 | STRATEGY_FILTER | 23,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.03%. |
| Rapida V1 — score 6–7,5 | DOGE | 60m | SHORT | -7,93 | 6,00 | 0,00 | STRATEGY_FILTER | 23,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.03%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.753,99 | -2,46% | €5,64 | €3.000,00 | 0,19% | 2 | 31 | 35,48% | 0,74 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 31 | 1025 | PRIME INDICAZIONI | 50 (mancano 19) |

- Trade del Principale 4H chiusi: **31**; win rate **35,48%**; profit factor **0,74**.
- Expectancy: **€-8,77** per trade; P&L netto: **€-271,94**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 2 | €9.753,99 | €494,66 | €1.483,99 | €49,83 | €23,38 |
| TEST | Benchmark Donchian breakout 1H | 1 | €10.562,88 | €52,48 | €104,96 | €2,54 | €0,00 |
| TEST | Rapida score 6–7,5 — Cost Aware | 0 | €10.506,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 0 | €10.492,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €10.485,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 0 | €10.440,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 0 | €10.399,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 0 | €10.355,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 1 | €10.314,28 | €88,92 | €177,84 | €4,31 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €10.305,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.295,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 0 | €10.283,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 0 | €10.278,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.237,16 | €641,89 | €1.925,68 | €50,72 | €23,94 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 0 | €10.231,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 0 | €10.224,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.218,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €10.217,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €10.206,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 0 | €10.184,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 0 | €10.111,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.096,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 0 | €10.096,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €10.071,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 0 | €10.030,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 0 | €10.027,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 0 | €10.012,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.009,05 | €50,00 | €750,00 | €24,38 | €-0,15 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.001,81 | €10,00 | €150,00 | €4,88 | €-0,03 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.997,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.996,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €9.993,38 | €10,00 | €150,00 | €4,88 | €-0,03 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 0 | €9.985,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.983,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 0 | €9.973,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.972,61 | €1.133,51 | €2.267,02 | €101,52 | €0,96 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 0 | €9.969,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €9.966,89 | €50,00 | €750,00 | €24,38 | €-0,15 |
| TEST | Btc Adaptive 1H | 0 | €9.959,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 0 | €9.957,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom15 Short | 0 | €9.957,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom20 Short | 0 | €9.957,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.953,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.949,96 | €61,21 | €306,04 | €9,95 | €-0,06 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.945,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.940,61 | €61,15 | €305,75 | €9,94 | €-0,06 |
| TEST | Forza relativa 1H V2 | 0 | €9.934,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 0 | €9.931,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 0 | €9.924,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.898,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.895,65 | €780,22 | €1.560,44 | €49,48 | €-0,46 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 0 | €9.893,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 0 | €9.883,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 0 | €9.874,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 0 | €9.870,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.867,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.858,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 0 | €9.843,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 0 | €9.837,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.832,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 0 | €9.825,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 0 | €9.807,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 0 | €9.803,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 0 | €9.799,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 0 | €9.792,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.784,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 0 | €9.771,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 0 | €9.770,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €9.761,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.758,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.754,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 0 | €9.710,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 0 | €9.708,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 0 | €9.693,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 0 | €9.688,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 0 | €9.679,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 0 | €9.656,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.639,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €9.632,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.625,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 0 | €9.583,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top20 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 0 | €9.529,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 0 | €9.463,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 0 | €9.449,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.405,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 0 | €9.331,79 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.753,99 | €-271,94 | 31 | 31 | 35,48% | 0,74 | €-8,77 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.562,88 | €562,95 | 39 | 39 | 53,85% | 1,62 | €14,43 | 3,09% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.506,14 | €506,14 | 36 | 36 | 52,78% | 1,93 | €14,06 | 1,96% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.492,11 | €492,11 | 64 | 64 | 46,88% | 1,41 | €7,69 | 2,83% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.485,55 | €485,55 | 75 | 75 | 44,00% | 1,37 | €6,47 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.440,04 | €440,04 | 66 | 66 | 39,39% | 1,33 | €6,67 | 2,82% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.399,89 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.355,52 | €355,52 | 50 | 50 | 44,00% | 1,30 | €7,11 | 4,79% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.314,28 | €314,39 | 7 | 7 | 71,43% | 6,32 | €44,91 | 1,61% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.305,06 | €305,06 | 75 | 75 | 45,33% | 1,24 | €4,07 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.295,72 | €295,72 | 12 | 12 | 58,33% | 2,80 | €24,64 | 1,78% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.283,50 | €283,50 | 33 | 33 | 54,55% | 1,80 | €8,59 | 1,58% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.278,80 | €278,80 | 41 | 39 | 51,22% | 1,36 | €6,80 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.237,16 | €211,24 | 15 | 15 | 46,67% | 1,56 | €14,08 | 2,40% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.231,01 | €231,01 | 28 | 28 | 46,43% | 1,69 | €8,25 | 1,76% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.224,22 | €224,22 | 41 | 41 | 39,02% | 1,25 | €5,47 | 3,94% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.218,07 | €218,07 | 13 | 13 | 53,85% | 1,74 | €16,77 | 2,28% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.217,21 | €217,21 | 68 | 68 | 44,12% | 1,16 | €3,19 | 3,62% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.206,76 | €206,76 | 33 | 33 | 51,52% | 1,32 | €6,27 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.184,40 | €184,40 | 72 | 72 | 44,44% | 1,14 | €2,56 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.111,99 | €111,99 | 40 | 40 | 42,50% | 1,21 | €2,80 | 2,58% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.096,23 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.096,10 | €96,10 | 59 | 59 | 50,85% | 1,11 | €1,63 | 2,98% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.071,76 | €71,76 | 43 | 43 | 37,21% | 1,11 | €1,67 | 2,31% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.030,12 | €30,12 | 103 | 103 | 37,86% | 1,02 | €0,29 | 2,95% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.027,65 | €27,65 | 30 | 30 | 50,00% | 1,06 | €0,92 | 2,61% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.012,08 | €12,08 | 26 | 26 | 34,62% | 1,03 | €0,46 | 2,48% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.009,05 | €9,65 | 20 | 20 | 45,00% | 1,14 | €0,48 | 0,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,81 | €1,93 | 20 | 20 | 45,00% | 1,14 | €0,10 | 0,06% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.997,70 | €-2,30 | 7 | 7 | 42,86% | 0,94 | €-0,33 | 0,36% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.996,69 | €-3,31 | 7 | 7 | 28,57% | 0,24 | €-0,47 | 0,04% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.993,38 | €-6,50 | 6 | 6 | 33,33% | 0,07 | €-1,08 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,04 | €-10,96 | 13 | 13 | 30,77% | 0,26 | €-0,84 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.985,05 | €-14,95 | 19 | 19 | 42,11% | 0,95 | €-0,79 | 1,38% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.983,45 | €-16,55 | 7 | 7 | 28,57% | 0,24 | €-2,36 | 0,19% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.973,32 | €-26,68 | 79 | 79 | 35,44% | 0,98 | €-0,34 | 2,58% |
| TEST | Ampia 4H | Confluenza trend | €9.972,61 | €-27,14 | 25 | 25 | 24,00% | 0,96 | €-1,09 | 3,68% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.969,87 | €-30,13 | 20 | 20 | 40,00% | 0,86 | €-1,51 | 1,53% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.966,89 | €-32,51 | 6 | 6 | 33,33% | 0,07 | €-5,42 | 0,53% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.959,54 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 0,89% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.957,79 | €-42,21 | 25 | 25 | 40,00% | 0,91 | €-1,69 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.957,79 | €-42,21 | 25 | 25 | 40,00% | 0,91 | €-1,69 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.957,79 | €-42,21 | 25 | 25 | 40,00% | 0,91 | €-1,69 | 2,72% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.953,21 | €-46,79 | 13 | 13 | 30,77% | 0,37 | €-3,60 | 0,71% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.949,96 | €-49,80 | 6 | 6 | 33,33% | 0,07 | €-8,30 | 0,71% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.945,22 | €-54,78 | 13 | 13 | 30,77% | 0,26 | €-4,21 | 0,72% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.940,61 | €-59,14 | 20 | 20 | 45,00% | 0,44 | €-2,96 | 0,64% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.934,23 | €-65,77 | 55 | 54 | 38,18% | 0,96 | €-1,20 | 5,53% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.931,86 | €-68,14 | 20 | 20 | 25,00% | 0,81 | €-3,41 | 2,34% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.924,82 | €-75,18 | 36 | 36 | 38,89% | 0,90 | €-2,09 | 4,41% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.898,26 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,48% |
| TEST | Sol Ema 4H | Trend following EMA | €9.895,65 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,44% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.893,14 | €-106,86 | 47 | 47 | 36,17% | 0,87 | €-2,27 | 5,48% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.883,60 | €-116,40 | 24 | 24 | 37,50% | 0,71 | €-4,85 | 2,44% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.874,61 | €-125,39 | 22 | 22 | 31,82% | 0,72 | €-5,70 | 2,01% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.870,43 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Sol Ema 1H | Trend following EMA | €9.867,86 | €-132,14 | 7 | 7 | 28,57% | 0,52 | €-18,88 | 2,09% |
| TEST | Btc Ema 1H | Trend following EMA | €9.858,67 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,56% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.843,36 | €-156,64 | 26 | 26 | 30,77% | 0,80 | €-6,02 | 4,68% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.837,60 | €-162,40 | 30 | 30 | 33,33% | 0,79 | €-5,41 | 4,99% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.832,55 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,60% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.825,96 | €-174,04 | 77 | 77 | 37,66% | 0,89 | €-2,26 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.807,66 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,36% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.803,17 | €-196,83 | 22 | 22 | 18,18% | 0,66 | €-8,95 | 3,35% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.799,08 | €-200,92 | 22 | 22 | 31,82% | 0,74 | €-9,13 | 3,64% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.792,75 | €-207,25 | 17 | 17 | 29,41% | 0,62 | €-12,19 | 2,93% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.784,49 | €-215,51 | 13 | 13 | 30,77% | 0,44 | €-16,58 | 2,92% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.771,68 | €-228,32 | 21 | 21 | 28,57% | 0,68 | €-10,87 | 3,98% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.770,26 | €-229,74 | 22 | 22 | 31,82% | 0,64 | €-10,44 | 4,43% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,49 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.758,89 | €-241,11 | 19 | 19 | 26,32% | 0,66 | €-12,69 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.754,87 | €-245,13 | 19 | 19 | 26,32% | 0,66 | €-12,90 | 4,07% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.710,00 | €-290,00 | 41 | 41 | 39,02% | 0,60 | €-7,07 | 3,97% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.708,46 | €-291,54 | 46 | 46 | 30,43% | 0,71 | €-6,34 | 3,97% |
| TEST | Combo Scanner | Combo Scanner | €9.693,00 | €-307,00 | 50 | 50 | 36,00% | 0,77 | €-6,14 | 5,08% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.688,64 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 3,94% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.679,07 | €-320,93 | 19 | 19 | 21,05% | 0,55 | €-16,89 | 4,64% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.656,74 | €-343,26 | 20 | 20 | 25,00% | 0,47 | €-17,16 | 4,32% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.639,39 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.632,30 | €-367,70 | 52 | 52 | 26,92% | 0,70 | €-7,07 | 7,55% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.625,26 | €-374,74 | 54 | 54 | 55,56% | 0,59 | €-6,94 | 4,27% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.583,73 | €-416,27 | 34 | 34 | 32,35% | 0,46 | €-12,24 | 5,03% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Combo Trend | Combo Trend | €9.529,98 | €-470,02 | 62 | 62 | 30,65% | 0,74 | €-7,58 | 7,64% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.463,31 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,43% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.449,51 | €-550,49 | 56 | 56 | 28,57% | 0,62 | €-9,83 | 6,47% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.405,07 | €-594,93 | 27 | 27 | 22,22% | 0,49 | €-22,03 | 6,15% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.331,79 | €-668,21 | 50 | 50 | 28,00% | 0,42 | €-13,36 | 6,71% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,06906 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €23,38 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,04449 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €0,50 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,06906 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €0,47 |
| Scalp RSI Short 80 · €10 · 15x | ADA | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,20653 | 0,20657 | 0,21324 | 0,21926 | 0,19646 | €10,00 | €150,00 | €4,88 | €-0,03 |
| Scalp RSI Short 75 · €10 · 15x | ADA | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,20653 | 0,20657 | 0,21324 | 0,21926 | 0,19646 | €10,00 | €150,00 | €4,88 | €-0,03 |
| Scalp RSI Short 80 · €50 · 15x | ADA | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,20653 | 0,20657 | 0,21324 | 0,21926 | 0,19646 | €50,00 | €750,00 | €24,38 | €-0,15 |
| Scalp RSI Short 75 · €50 · 15x | ADA | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,20653 | 0,20657 | 0,21324 | 0,21926 | 0,19646 | €50,00 | €750,00 | €24,38 | €-0,15 |
| Scalp RSI Short 80 · prudente · 5x | ADA | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,20653 | 0,20657 | 0,21324 | 0,24680 | 0,19310 | €61,21 | €306,04 | €9,95 | €-0,06 |
| Scalp RSI Short 75 · prudente · 5x | ADA | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,20653 | 0,20657 | 0,21324 | 0,24680 | 0,19310 | €61,15 | €305,75 | €9,94 | €-0,06 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 73,21200 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-0,46 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,06906 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €23,94 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scalp RSI Short 80 · prudente · 5x | ADA | SHORT | 2026-08-06T15:53:52+00:00 | 0,20432 | €-10,80 | -1,08 | STOP |
| Scalp RSI Short 80 · €50 · 15x | ADA | SHORT | 2026-08-06T15:53:52+00:00 | 0,20432 | €-13,60 | -1,08 | STOP |
| Scalp RSI Short 80 · €10 · 15x | ADA | SHORT | 2026-08-06T15:53:52+00:00 | 0,20432 | €-2,72 | -1,08 | STOP |
| Scalp RSI Long 25 · prudente · 5x | SOL | LONG | 2026-08-06T05:24:44+00:00 | 73,52397 | €-2,50 | -0,25 | STOP_GAP_STRESS |
| Scalp RSI Long 25 · €50 · 15x | SOL | LONG | 2026-08-06T05:24:44+00:00 | 73,52397 | €-0,75 | -0,25 | STOP_GAP_STRESS |
| Scalp RSI Long 25 · €10 · 15x | SOL | LONG | 2026-08-06T05:24:44+00:00 | 73,52397 | €-0,15 | -0,25 | STOP_GAP_STRESS |
| Scalp RSI Long 20 · prudente · 5x | XRP | LONG | 2026-08-06T04:24:41+00:00 | 1,03945 | €-12,00 | -1,20 | STOP |
| Scalp RSI Long 15 · prudente · 5x | XRP | LONG | 2026-08-06T04:24:41+00:00 | 1,03945 | €-11,98 | -1,20 | STOP |
| Scalp RSI Long 20 · €50 · 15x | XRP | LONG | 2026-08-06T04:24:41+00:00 | 1,03945 | €-6,31 | -1,20 | STOP |
| Scalp RSI Long 15 · €50 · 15x | XRP | LONG | 2026-08-06T04:24:41+00:00 | 1,03945 | €-6,31 | -1,20 | STOP |
| Scalp RSI Long 20 · €10 · 15x | XRP | LONG | 2026-08-06T04:24:41+00:00 | 1,03945 | €-1,26 | -1,20 | STOP |
| Scalp RSI Long 15 · €10 · 15x | XRP | LONG | 2026-08-06T04:24:41+00:00 | 1,03945 | €-1,26 | -1,20 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 197/30 | 33/30 | 0,67 | 2,04 | -0,17R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 171/30 | 20/30 | 0,51 | 1,90 | -0,27R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 113/30 | 22/30 | 0,76 | 1,74 | -0,13R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 116/30 | 22/30 | 0,71 | 1,57 | -0,16R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 149/30 | 31/30 | 0,71 | 0,62 | -0,16R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 125/30 | 11/30 | 0,61 | 0,00 | -0,21R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 90/30 | 8/30 | 0,59 | 1,02 | -0,22R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 155/30 | 17/30 | 0,53 | 4,50 | -0,28R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 217/30 | 24/30 | 0,65 | 0,64 | -0,19R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 189/30 | 7/30 | 0,51 | 0,02 | -0,27R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 149/30 | 30/30 | 0,78 | 1,02 | -0,12R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 280/30 | 55/30 | 0,74 | 1,12 | -0,13R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 83/30 | 15/30 | 0,55 | 0,99 | -0,29R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 245/30 | 44/30 | 0,63 | 1,20 | -0,20R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 249/30 | 37/30 | 0,64 | 0,76 | -0,20R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 219/30 | 23/30 | 0,51 | 1,12 | -0,27R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 156/30 | 31/30 | 0,80 | 0,74 | -0,13R | €-8,77 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 15/30 | 0,00 | 1,56 | 0,00R | €14,08 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 22/30 | 13/30 | 0,47 | 0,37 | -0,33R | €-3,60 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 28/30 | 20/30 | 0,50 | 0,44 | -0,28R | €-2,96 | 0,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 406/30 | 75/30 | 0,93 | 1,24 | -0,04R | €4,07 | 3,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 20/30 | 0,00 | 0,47 | 0,00R | €-17,16 | 4,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 2/30 | 0,00 | 0,00 | 0,00R | €-28,31 | 1,11% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 139/30 | 39/30 | 1,08 | 1,36 | 0,04R | €6,80 | 2,75% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 243/30 | 66/30 | 0,94 | 1,33 | -0,04R | €6,67 | 2,82% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 164/30 | 22/30 | 0,75 | 0,72 | -0,14R | €-5,70 | 2,01% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 105/30 | 25/30 | 1,01 | 0,99 | 0,00R | €-0,14 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 226/30 | 28/30 | 0,87 | 1,69 | -0,07R | €8,25 | 1,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 293/30 | 64/30 | 0,93 | 1,41 | -0,04R | €7,69 | 2,83% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 382/30 | 72/30 | 0,77 | 1,14 | -0,13R | €2,56 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 36/30 | 0,00 | 1,93 | 0,00R | €14,06 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 33/30 | 0,00 | 1,32 | 0,00R | €6,27 | 2,77% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 13/30 | 0,00 | 1,74 | 0,00R | €16,77 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 227/30 | 75/30 | 0,89 | 1,37 | -0,06R | €6,47 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 355/30 | 79/30 | 0,74 | 0,98 | -0,15R | €-0,34 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 33/30 | 15/30 | 0,61 | 0,93 | -0,22R | €-1,52 | 1,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 392/30 | 103/30 | 0,81 | 1,02 | -0,11R | €0,29 | 2,95% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 277/30 | 68/30 | 0,84 | 1,16 | -0,09R | €3,19 | 3,62% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 152/30 | 49/30 | 0,99 | 0,93 | -0,01R | €-1,56 | 3,21% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 156/30 | 44/30 | 0,95 | 0,86 | -0,03R | €-3,24 | 2,86% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 203/30 | 56/30 | 0,88 | 0,62 | -0,06R | €-9,83 | 6,47% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 12/30 | 0,00 | 2,80 | 0,00R | €24,64 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 20/30 | 0,00 | 3,42 | 0,00R | €19,99 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 314/30 | 62/30 | 0,79 | 0,90 | -0,11R | €-2,09 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 36/30 | 0,00 | 0,90 | 0,00R | €-2,09 | 4,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 59/30 | 0,00 | 1,11 | 0,00R | €1,63 | 2,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 20/30 | 0,00 | 1,17 | 0,00R | €3,80 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 345/30 | 77/30 | 0,74 | 0,89 | -0,14R | €-2,26 | 2,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 138/30 | 25/30 | 0,77 | 0,96 | -0,16R | €-1,09 | 3,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 118/30 | 50/30 | 1,09 | 0,82 | 0,04R | €-4,77 | 5,70% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 7/30 | 4/30 | 0,28 | 0,63 | -0,46R | €-10,11 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 7/30 | 4/30 | 5,58 | 2,94 | 0,74R | €27,74 | 0,70% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 10/30 | 5/30 | 0,12 | 0,97 | -0,80R | €-0,63 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 3/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,48% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 10/30 | 7/30 | 0,72 | 0,48 | -0,18R | €-20,19 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 319/30 | 40/30 | 1,01 | 1,21 | 0,00R | €2,80 | 2,58% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 159/30 | 20/30 | 0,91 | 0,81 | -0,05R | €-3,41 | 2,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 322/30 | 50/30 | 1,01 | 0,42 | 0,00R | €-13,36 | 6,71% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 260/30 | 41/30 | 0,93 | 0,60 | -0,04R | €-7,07 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 28/30 | 11/30 | 0,99 | 0,71 | -0,01R | €-7,09 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 28/30 | 11/30 | 0,90 | 0,31 | -0,05R | €-18,43 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 85/30 | 26/30 | 0,88 | 1,03 | -0,06R | €0,46 | 2,48% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 93/30 | 22/30 | 0,69 | 0,79 | -0,18R | €-4,40 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 43/30 | 0,74 | 1,11 | -0,20R | €1,67 | 2,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 33/30 | 0,00 | 1,80 | 0,00R | €8,59 | 1,58% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 24/30 | 0,74 | 0,71 | -0,20R | €-4,85 | 2,44% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 58/30 | 20/30 | 1,19 | 0,76 | 0,09R | €-8,37 | 3,60% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_SCANNER | Combo Scanner | 190/30 | 50/30 | 1,23 | 0,77 | 0,12R | €-6,14 | 5,08% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 256/30 | 62/30 | 0,91 | 0,74 | -0,05R | €-7,58 | 7,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 30/30 | 0,00 | 1,06 | 0,00R | €0,92 | 2,61% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 6/30 | 4/30 | 0,84 | 0,41 | -0,09R | €-24,49 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 8/30 | 6/30 | 0,73 | 1,34 | -0,18R | €6,42 | 1,08% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 14/30 | 10/30 | 0,54 | 1,57 | -0,30R | €9,62 | 1,36% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 136/30 | 39/30 | 0,79 | 1,62 | -0,14R | €14,43 | 3,09% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 66/30 | 7/30 | 0,69 | 6,32 | -0,20R | €44,91 | 1,61% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 264/30 | 46/30 | 0,87 | 0,71 | -0,08R | €-6,34 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 9/30 | 6/30 | 0,32 | 0,08 | -0,59R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 5/30 | 2/30 | 1,25 | 0,28 | 0,12R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 8/30 | 5/30 | 0,38 | 0,42 | -0,53R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 14/30 | 8/30 | 0,34 | 0,16 | -0,52R | €-34,02 | 2,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-52,87 | 1,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 8/30 | 13/30 | 2,07 | 0,44 | 0,44R | €-16,58 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 150/30 | 22/30 | 1,05 | 0,74 | 0,03R | €-9,13 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 22/30 | 0,00 | 0,66 | 0,00R | €-8,95 | 3,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 19/30 | 0,00 | 0,55 | 0,00R | €-16,89 | 4,64% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 17/30 | 0,00 | 0,62 | 0,00R | €-12,19 | 2,93% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 279/30 | 54/30 | 1,37 | 0,59 | 0,12R | €-6,94 | 4,27% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 134/30 | 19/30 | 1,05 | 0,66 | 0,03R | €-12,69 | 4,03% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 134/30 | 21/30 | 1,00 | 0,68 | 0,00R | €-10,87 | 3,98% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 104/30 | 27/30 | 0,86 | 0,49 | -0,09R | €-22,03 | 6,15% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 145/30 | 19/30 | 1,01 | 0,66 | 0,01R | €-12,90 | 4,07% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 327/30 | 52/30 | 0,86 | 0,70 | -0,08R | €-7,07 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 140/30 | 54/30 | 1,11 | 0,96 | 0,06R | €-1,20 | 5,53% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 100/30 | 25/30 | 0,49 | 0,91 | -0,30R | €-1,69 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 100/30 | 25/30 | 0,49 | 0,91 | -0,30R | €-1,69 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 100/30 | 25/30 | 0,49 | 0,91 | -0,30R | €-1,69 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 135/30 | 47/30 | 0,78 | 0,87 | -0,12R | €-2,27 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 110/30 | 19/30 | 0,66 | 0,95 | -0,17R | €-0,79 | 1,38% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 95/30 | 20/30 | 0,66 | 0,86 | -0,16R | €-1,51 | 1,53% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 125/30 | 22/30 | 1,05 | 0,34 | 0,02R | €-20,99 | 6,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 126/30 | 22/30 | 1,03 | 0,34 | 0,02R | €-20,99 | 6,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 126/30 | 22/30 | 1,03 | 0,34 | 0,02R | €-20,99 | 6,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 183/30 | 41/30 | 1,21 | 1,25 | 0,11R | €5,47 | 3,94% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 64/30 | 10/30 | 0,82 | 0,87 | -0,10R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 137/30 | 22/30 | 0,97 | 0,64 | -0,02R | €-10,44 | 4,43% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 152/30 | 34/30 | 1,13 | 0,61 | 0,06R | €-10,61 | 3,93% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 124/30 | 19/30 | 1,04 | 0,70 | 0,02R | €-10,12 | 4,36% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 162/30 | 41/30 | 1,14 | 0,53 | 0,06R | €-13,09 | 5,43% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 131/30 | 24/30 | 1,05 | 0,59 | 0,03R | €-12,97 | 3,94% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 178/30 | 34/30 | 1,10 | 0,46 | 0,04R | €-12,24 | 5,03% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 134/30 | 30/30 | 1,04 | 0,79 | 0,02R | €-5,41 | 4,99% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 129/30 | 26/30 | 1,06 | 0,80 | 0,04R | €-6,02 | 4,68% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 205/30 | 50/30 | 1,18 | 1,30 | 0,09R | €7,11 | 4,79% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 14/30 | 7/30 | 0,34 | 0,24 | -0,57R | €-31,26 | 2,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 2/30 | 0,00 | 0,65 | -1,05R | €-8,96 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 7/30 | 5/30 | 0,99 | 0,82 | -0,01R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 9/30 | 4/30 | 0,62 | 26,39 | -0,28R | €28,48 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 2/30 | 0,00 | 0,71 | -1,06R | €-7,50 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 13/30 | 7/30 | 0,51 | 0,52 | -0,41R | €-18,88 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-51,84 | 1,44% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06906**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 26.8 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64597.7 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.06912**; close **0.06897**; wick alta **50.0%**; volume **x0.50**

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

- Regime: **ALT_ROTATION_DOWN**
- Famiglia: **ALT_ROTATION**
- Confidenza: **72,90%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -1.28%, 55% sotto -1%.
- BTC trend score: **3,00**; ADX: **21,39**; breadth sopra EMA50: **50,00%**
- Mediana alt vs BTC: **-1,28%**; dispersione: **11,40%**

- Aperti in questo ciclo: **1**
- Chiusi in questo ciclo: **30**
- Posizioni research aperte: **533**
- Trade research chiusi: **14412**
- Eventi di mercato indipendenti chiusi: **2264**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **42199**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 6 | 197 | 197 | 30,46% | 0,67 | -0,17R | €-343,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 6 | 171 | 171 | 29,24% | 0,51 | -0,27R | €-465,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 3 | 113 | 113 | 46,02% | 0,76 | -0,13R | €-146,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 3 | 116 | 116 | 32,76% | 0,71 | -0,16R | €-181,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 3 | 149 | 149 | 32,21% | 0,71 | -0,16R | €-237,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 3 | 125 | 125 | 32,80% | 0,61 | -0,21R | €-257,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 1 | 90 | 90 | 32,22% | 0,59 | -0,22R | €-201,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 4 | 155 | 155 | 27,10% | 0,53 | -0,28R | €-432,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 6 | 217 | 217 | 29,95% | 0,65 | -0,19R | €-411,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 6 | 189 | 189 | 28,57% | 0,51 | -0,27R | €-515,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 3 | 149 | 149 | 33,56% | 0,78 | -0,12R | €-178,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 6 | 280 | 280 | 38,57% | 0,74 | -0,13R | €-353,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 83 | 83 | 30,12% | 0,55 | -0,29R | €-244,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 6 | 245 | 245 | 28,98% | 0,63 | -0,20R | €-489,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 6 | 249 | 249 | 28,92% | 0,64 | -0,20R | €-490,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 6 | 219 | 219 | 27,85% | 0,51 | -0,27R | €-592,75 |
| MAIN | 19 | 156 | 156 | 28,21% | 0,80 | -0,13R | €-197,63 |
| RSI_EXTREME_LONG_15M | 0 | 22 | 22 | 36,36% | 0,47 | -0,33R | €-73,68 |
| RSI_EXTREME_SHORT_15M | 1 | 28 | 28 | 35,71% | 0,50 | -0,28R | €-79,28 |
| Bilanciata 1H V1 | 14 | 406 | 406 | 34,73% | 0,93 | -0,04R | €-160,44 |
| Bilanciata 1H V2 | 9 | 158 | 139 | 37,97% | 1,08 | 0,04R | €70,16 |
| Bilanciata 1H V3 Filtered | 10 | 243 | 243 | 35,39% | 0,94 | -0,04R | €-87,61 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 10 | 164 | 164 | 33,54% | 0,75 | -0,14R | €-232,96 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 4 | 105 | 105 | 36,19% | 1,01 | 0,00R | €4,28 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 8 | 226 | 226 | 35,40% | 0,87 | -0,07R | €-147,82 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 8 | 293 | 293 | 37,20% | 0,93 | -0,04R | €-113,48 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 7 | 382 | 382 | 34,03% | 0,77 | -0,13R | €-478,32 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 227 | 227 | 36,56% | 0,89 | -0,06R | €-137,33 |
| SHADOW_1H_FAST_TP2_V1 | 7 | 355 | 355 | 31,27% | 0,74 | -0,15R | €-517,61 |
| Rapida 1H V2 | 1 | 38 | 33 | 34,21% | 0,61 | -0,22R | €-84,34 |
| Rapida 1H V3 Filtered | 6 | 392 | 392 | 34,69% | 0,81 | -0,11R | €-414,19 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 6 | 277 | 277 | 35,02% | 0,84 | -0,09R | €-238,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 152 | 152 | 48,03% | 0,99 | -0,01R | €-7,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 156 | 156 | 37,18% | 0,95 | -0,03R | €-39,73 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 203 | 203 | 36,45% | 0,88 | -0,06R | €-131,61 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 6 | 314 | 314 | 34,39% | 0,79 | -0,11R | €-356,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 6 | 345 | 345 | 33,04% | 0,74 | -0,14R | €-496,15 |
| SHADOW_4H_WIDE | 28 | 138 | 138 | 22,46% | 0,77 | -0,16R | €-219,18 |
| SHADOW_BOLLINGER_MR_1H | 0 | 118 | 118 | 46,61% | 1,09 | 0,04R | €51,40 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 7 | 7 | 42,86% | 0,28 | -0,46R | €-32,06 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 7 | 7 | 85,71% | 5,58 | 0,74R | €51,91 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 10 | 10 | 20,00% | 0,12 | -0,80R | €-79,53 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,12 |
| SHADOW_BTC_EMA_1H | 1 | 10 | 10 | 40,00% | 0,72 | -0,18R | €-18,37 |
| SHADOW_BTC_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 10 | 319 | 319 | 37,30% | 1,01 | 0,00R | €9,88 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 159 | 159 | 35,85% | 0,91 | -0,05R | €-76,32 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 7 | 322 | 322 | 40,06% | 1,01 | 0,00R | €8,59 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 10 | 260 | 260 | 38,46% | 0,93 | -0,04R | €-100,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 28 | 28 | 35,71% | 0,99 | -0,01R | €-1,59 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 28 | 28 | 25,00% | 0,90 | -0,05R | €-13,29 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 3 | 85 | 85 | 31,76% | 0,88 | -0,06R | €-55,09 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 93 | 93 | 27,96% | 0,69 | -0,18R | €-163,91 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 58 | 58 | 48,28% | 1,19 | 0,09R | €51,00 |
| SHADOW_COMBO_SCANNER | 8 | 190 | 190 | 37,89% | 1,23 | 0,12R | €231,70 |
| SHADOW_COMBO_TREND | 14 | 256 | 256 | 32,03% | 0,91 | -0,05R | €-132,96 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 6 | 6 | 50,00% | 0,84 | -0,09R | €-5,54 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 8 | 8 | 37,50% | 0,73 | -0,18R | €-14,80 |
| SHADOW_DOGE_EMA_1H | 1 | 14 | 14 | 28,57% | 0,54 | -0,30R | €-41,58 |
| SHADOW_DONCHIAN_1H | 10 | 136 | 136 | 27,21% | 0,79 | -0,14R | €-194,32 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 10 | 66 | 66 | 28,79% | 0,69 | -0,20R | €-129,24 |
| SHADOW_EMA_TREND_1H | 14 | 264 | 264 | 31,06% | 0,87 | -0,08R | €-199,66 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 9 | 9 | 22,22% | 0,32 | -0,59R | €-52,98 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 5 | 5 | 60,00% | 1,25 | 0,12R | €5,77 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 8 | 8 | 25,00% | 0,38 | -0,53R | €-42,02 |
| SHADOW_ETH_EMA_1H | 1 | 14 | 14 | 28,57% | 0,34 | -0,52R | €-73,46 |
| SHADOW_ETH_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_GLOBAL_PURE | 1 | 8 | 8 | 62,50% | 2,07 | 0,44R | €35,30 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 10 | 150 | 150 | 34,00% | 1,05 | 0,03R | €50,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 279 | 279 | 65,23% | 1,37 | 0,12R | €344,79 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 9 | 134 | 134 | 33,58% | 1,05 | 0,03R | €38,15 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 9 | 134 | 134 | 30,60% | 1,00 | 0,00R | €1,63 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 104 | 104 | 29,81% | 0,86 | -0,09R | €-96,23 |
| SHADOW_MASTER_ADAPTIVE_V1 | 9 | 145 | 145 | 33,10% | 1,01 | 0,01R | €13,68 |
| Forza relativa 1H V1 | 18 | 327 | 327 | 30,58% | 0,86 | -0,08R | €-258,69 |
| Forza relativa 1H V2 | 10 | 148 | 140 | 35,81% | 1,11 | 0,06R | €93,55 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 5 | 100 | 100 | 29,00% | 0,49 | -0,30R | €-304,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 5 | 100 | 100 | 29,00% | 0,49 | -0,30R | €-304,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 5 | 100 | 100 | 29,00% | 0,49 | -0,30R | €-304,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 5 | 135 | 135 | 32,59% | 0,78 | -0,12R | €-163,79 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 4 | 110 | 110 | 46,36% | 0,66 | -0,17R | €-187,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 4 | 95 | 95 | 47,37% | 0,66 | -0,16R | €-156,41 |
| SHADOW_SCANNER_TOP10_LONG | 7 | 125 | 125 | 36,80% | 1,05 | 0,02R | €30,39 |
| SHADOW_SCANNER_TOP15_LONG | 7 | 126 | 126 | 36,51% | 1,03 | 0,02R | €19,28 |
| SHADOW_SCANNER_TOP20_LONG | 7 | 126 | 126 | 36,51% | 1,03 | 0,02R | €19,28 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 183 | 183 | 36,61% | 1,21 | 0,11R | €208,71 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 64 | 64 | 31,25% | 0,82 | -0,10R | €-61,68 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 7 | 137 | 137 | 33,58% | 0,97 | -0,02R | €-24,69 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 152 | 152 | 43,42% | 1,13 | 0,06R | €88,35 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 124 | 124 | 34,68% | 1,04 | 0,02R | €24,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 4 | 162 | 162 | 43,21% | 1,14 | 0,06R | €99,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 131 | 131 | 34,35% | 1,05 | 0,03R | €35,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 6 | 178 | 178 | 43,26% | 1,10 | 0,04R | €76,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 134 | 134 | 32,84% | 1,04 | 0,02R | €26,93 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 129 | 129 | 32,56% | 1,06 | 0,04R | €45,46 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 205 | 205 | 37,56% | 1,18 | 0,09R | €192,81 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 14 | 14 | 21,43% | 0,34 | -0,57R | €-80,03 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 7 | 7 | 57,14% | 0,99 | -0,01R | €-0,47 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 9 | 9 | 33,33% | 0,62 | -0,28R | €-25,17 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 0 | 13 | 13 | 23,08% | 0,51 | -0,41R | €-53,84 |
| SHADOW_SOL_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,12 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 3 | 32 | 32 | 21,88% | 0,55 | -0,27R | €-86,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 1 | 25 | 25 | 36,00% | 0,99 | -0,00R | €-0,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 79 | 79 | 36,71% | 0,69 | -0,15R | €-120,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 1 | 9 | 9 | 33,33% | 1,39 | 0,18R | €16,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 20 | 20 | 30,00% | 0,42 | -0,36R | €-71,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 26 | 26 | 23,08% | 0,68 | -0,15R | €-38,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 3 | 31 | 31 | 19,35% | 0,34 | -0,45R | €-140,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 1 | 12 | 12 | 33,33% | 0,82 | -0,09R | €-11,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 75 | 75 | 36,00% | 0,56 | -0,22R | €-165,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 1 | 9 | 9 | 33,33% | 1,27 | 0,13R | €11,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 17 | 17 | 29,41% | 0,38 | -0,37R | €-63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 23 | 23 | 21,74% | 0,46 | -0,28R | €-65,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 1 | 4 | 4 | 50,00% | 1,07 | 0,03R | €1,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 1 | 20 | 20 | 50,00% | 1,16 | 0,09R | €17,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 53 | 53 | 39,62% | 0,46 | -0,34R | €-178,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 1 | 4 | 4 | 75,00% | 4,08 | 0,78R | €31,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 11 | 11 | 45,45% | 0,46 | -0,30R | €-32,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 20 | 20 | 55,00% | 1,27 | 0,12R | €23,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 1,83 | 0,30R | €9,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 1 | 22 | 22 | 36,36% | 1,00 | -0,00R | €-0,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 55 | 55 | 30,91% | 0,41 | -0,34R | €-186,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 1 | 4 | 4 | 50,00% | 3,80 | 0,72R | €28,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 11 | 11 | 36,36% | 0,64 | -0,23R | €-25,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 20 | 20 | 30,00% | 1,04 | 0,02R | €3,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,47 | -0,28R | €-22,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 1 | 22 | 22 | 36,36% | 0,87 | -0,07R | €-15,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 1 | 64 | 64 | 32,81% | 0,61 | -0,23R | €-144,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 1 | 5 | 5 | 40,00% | 3,75 | 0,57R | €28,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,86 | -0,08R | €-11,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 30 | 30 | 30,00% | 0,67 | -0,17R | €-49,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,23 | -0,41R | €-32,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 1 | 14 | 14 | 35,71% | 0,76 | -0,12R | €-17,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 1 | 55 | 55 | 34,55% | 0,53 | -0,25R | €-139,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 1 | 5 | 5 | 40,00% | 2,78 | 0,37R | €18,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 13 | 13 | 46,15% | 0,92 | -0,05R | €-6,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 27 | 27 | 29,63% | 0,58 | -0,22R | €-58,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 1 | 88 | 88 | 31,82% | 0,57 | -0,24R | €-210,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 1 | 15 | 15 | 0,00% | 0,00 | -0,95R | €-142,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 1 | 27 | 27 | 33,33% | 0,89 | -0,06R | €-15,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 1 | 76 | 76 | 31,58% | 0,61 | -0,22R | €-167,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 1 | 7 | 7 | 14,29% | 0,37 | -0,46R | €-32,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 22 | 22 | 31,82% | 0,53 | -0,29R | €-63,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -0,35R | €-20,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 1 | 21 | 21 | 4,76% | 0,12 | -0,69R | €-145,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 28 | 28 | 32,14% | 0,88 | -0,06R | €-17,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 2 | 95 | 95 | 34,74% | 0,69 | -0,17R | €-165,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 1 | 10 | 10 | 20,00% | 0,93 | -0,03R | €-2,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 36 | 36 | 25,00% | 0,59 | -0,20R | €-70,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 1 | 21 | 21 | 4,76% | 0,06 | -0,74R | €-155,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 1 | 16 | 16 | 31,25% | 0,66 | -0,18R | €-28,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 2 | 88 | 88 | 34,09% | 0,57 | -0,24R | €-207,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 1 | 10 | 10 | 20,00% | 0,69 | -0,13R | €-12,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 21 | 21 | 38,10% | 0,81 | -0,10R | €-21,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 33 | 33 | 24,24% | 0,48 | -0,27R | €-89,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,47 | -0,28R | €-22,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 1 | 23 | 23 | 39,13% | 1,04 | 0,02R | €4,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 1 | 64 | 64 | 35,94% | 0,76 | -0,13R | €-85,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 1 | 5 | 5 | 40,00% | 3,75 | 0,57R | €28,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,86 | -0,08R | €-11,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 30 | 30 | 30,00% | 0,67 | -0,17R | €-49,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 49 | 49 | 32,65% | 0,44 | -0,33R | €-161,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 1 | 30 | 30 | 43,33% | 0,99 | -0,01R | €-2,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 2 | 109 | 109 | 37,61% | 0,83 | -0,08R | €-85,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 12 | 12 | 41,67% | 1,78 | 0,21R | €25,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 30 | 30 | 50,00% | 0,99 | -0,01R | €-1,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 43 | 43 | 41,86% | 0,68 | -0,15R | €-65,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 12 | 12 | 0,00% | 0,00 | -1,02R | €-122,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 11 | 11 | 27,27% | 0,74 | -0,18R | €-20,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 36 | 36 | 36,11% | 0,56 | -0,25R | €-90,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,76 | 0,41R | €8,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 8 | 8 | 37,50% | 0,75 | -0,10R | €-8,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 13 | 13 | 30,77% | 0,66 | -0,23R | €-30,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 15,56% | 0,31 | -0,42R | €-191,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 26 | 26 | 30,77% | 0,79 | -0,10R | €-26,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 2 | 94 | 94 | 35,11% | 0,70 | -0,17R | €-155,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 1 | 11 | 11 | 27,27% | 1,38 | 0,15R | €16,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 36 | 36 | 25,00% | 0,59 | -0,20R | €-70,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 15,56% | 0,31 | -0,42R | €-191,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 28 | 28 | 32,14% | 0,88 | -0,06R | €-17,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 2 | 95 | 95 | 34,74% | 0,69 | -0,17R | €-165,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 1 | 11 | 11 | 27,27% | 1,38 | 0,15R | €16,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 36 | 36 | 25,00% | 0,59 | -0,20R | €-70,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 15,56% | 0,25 | -0,48R | €-215,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 1 | 16 | 16 | 31,25% | 0,66 | -0,18R | €-28,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 2 | 88 | 88 | 34,09% | 0,57 | -0,24R | €-207,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 1 | 11 | 11 | 27,27% | 1,26 | 0,10R | €10,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 21 | 21 | 38,10% | 0,81 | -0,10R | €-21,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 33 | 33 | 24,24% | 0,48 | -0,27R | €-89,56 |
| MAIN | ALT_ROTATION_DOWN | 3 | 15 | 15 | 33,33% | 1,30 | 0,13R | €18,91 |
| MAIN | ALT_ROTATION_UP | 7 | 21 | 21 | 19,05% | 0,34 | -0,45R | €-95,15 |
| MAIN | RANGE | 8 | 51 | 51 | 21,57% | 0,57 | -0,31R | €-155,84 |
| MAIN | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 12 | 12 | 33,33% | 0,97 | -0,02R | €-2,55 |
| MAIN | TREND_DOWN | 0 | 15 | 15 | 26,67% | 0,72 | -0,15R | €-22,75 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 0 | 30 | 30 | 36,67% | 1,18 | 0,11R | €32,89 |
| MAIN | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,94 | -0,04R | €-2,34 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 11 | 11 | 18,18% | 0,10 | -0,77R | €-85,05 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 4 | 4 | 75,00% | 5,55 | 0,50R | €20,01 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,12 | -0,66R | €-53,17 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 7 | 7 | 42,86% | 0,93 | -0,03R | €-2,10 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 53 | 53 | 22,64% | 0,48 | -0,36R | €-189,03 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 5 | 38 | 38 | 39,47% | 1,20 | 0,11R | €41,54 |
| Bilanciata 1H V1 | RANGE | 5 | 123 | 123 | 42,28% | 1,16 | 0,09R | €109,90 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 6,67% | 0,13 | -0,86R | €-129,29 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 1 | 50 | 50 | 40,00% | 1,20 | 0,11R | €54,60 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 29 | 29 | 34,48% | 0,78 | -0,11R | €-32,03 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 1 | 81 | 81 | 32,10% | 1,02 | 0,01R | €6,91 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 3 | 32 | 27 | 43,75% | 1,39 | 0,19R | €60,96 |
| Bilanciata 1H V2 | RANGE | 4 | 90 | 81 | 36,67% | 0,90 | -0,06R | €-56,16 |
| Bilanciata 1H V2 | TRANSITION | 2 | 36 | 31 | 36,11% | 1,36 | 0,18R | €65,37 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 37 | 37 | 27,03% | 0,64 | -0,23R | €-86,21 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 3 | 18 | 18 | 38,89% | 1,43 | 0,23R | €41,51 |
| Bilanciata 1H V3 Filtered | RANGE | 1 | 85 | 85 | 42,35% | 1,09 | 0,05R | €40,31 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,03R | €-41,09 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 20 | 20 | 35,00% | 1,20 | 0,11R | €21,34 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 22 | 22 | 31,82% | 0,29 | -0,44R | €-95,77 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 40 | 40 | 35,00% | 1,28 | 0,14R | €55,68 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 3 | 26 | 26 | 19,23% | 0,31 | -0,46R | €-119,58 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 16 | 16 | 43,75% | 1,83 | 0,39R | €62,51 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 63 | 63 | 39,68% | 0,79 | -0,12R | €-75,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 12 | 12 | 33,33% | 1,30 | 0,13R | €15,65 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 23 | 23 | 30,43% | 0,27 | -0,46R | €-106,88 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 2 | 19 | 19 | 26,32% | 0,94 | -0,03R | €-5,16 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 12,50% | 0,28 | -0,47R | €-37,35 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 2 | 19 | 19 | 42,11% | 1,04 | 0,02R | €3,76 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 41 | 41 | 36,59% | 0,92 | -0,04R | €-18,41 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 7 | 7 | 71,43% | 78,14 | 1,05R | €73,34 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 28 | 28 | 28,57% | 0,82 | -0,07R | €-20,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 14 | 14 | 14,29% | 0,33 | -0,42R | €-59,27 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 2 | 30 | 30 | 36,67% | 0,84 | -0,09R | €-26,45 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 97 | 97 | 38,14% | 0,87 | -0,07R | €-65,44 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 12 | 12 | 41,67% | 1,69 | 0,25R | €29,97 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,76 | -0,13R | €-41,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 1 | 38 | 38 | 28,95% | 0,82 | -0,08R | €-29,31 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 32 | 32 | 18,75% | 0,38 | -0,44R | €-141,50 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 31 | 31 | 38,71% | 0,92 | -0,04R | €-12,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 127 | 127 | 43,31% | 1,13 | 0,06R | €79,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 14 | 14 | 50,00% | 2,37 | 0,43R | €59,66 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,76 | -0,13R | €-41,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 1 | 54 | 54 | 27,78% | 0,65 | -0,19R | €-101,52 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 73 | 73 | 20,55% | 0,38 | -0,43R | €-312,02 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 2 | 33 | 33 | 36,36% | 0,81 | -0,11R | €-34,91 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 2 | 147 | 147 | 40,14% | 0,91 | -0,05R | €-70,39 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,33 | -0,55R | €-27,71 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 20 | 20 | 50,00% | 2,63 | 0,45R | €90,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 38 | 38 | 36,84% | 0,80 | -0,11R | €-41,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 1 | 61 | 61 | 26,23% | 0,63 | -0,20R | €-124,19 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 40 | 40 | 22,50% | 0,40 | -0,43R | €-172,31 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 26 | 26 | 34,62% | 0,86 | -0,08R | €-20,81 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 89 | 89 | 47,19% | 1,34 | 0,15R | €136,85 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 12 | 12 | 41,67% | 1,39 | 0,17R | €20,21 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 22 | 22 | 27,27% | 0,59 | -0,23R | €-50,88 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 33 | 33 | 30,30% | 0,69 | -0,18R | €-59,60 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 1 | 72 | 72 | 19,44% | 0,42 | -0,39R | €-282,49 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 2 | 35 | 35 | 37,14% | 0,99 | -0,01R | €-2,17 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 3 | 129 | 129 | 38,76% | 0,92 | -0,04R | €-53,51 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,37 | -0,55R | €-32,86 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 19 | 19 | 47,37% | 2,66 | 0,48R | €90,53 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 32 | 32 | 37,50% | 0,73 | -0,16R | €-50,72 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 56 | 56 | 19,64% | 0,44 | -0,33R | €-183,85 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,58R | €-11,56 |
| Rapida 1H V2 | ALT_ROTATION_UP | 1 | 7 | 7 | 28,57% | 0,29 | -0,56R | €-39,35 |
| Rapida 1H V2 | RANGE | 0 | 29 | 24 | 37,93% | 0,78 | -0,11R | €-32,76 |
| Rapida 1H V2 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -0,61R | €-12,24 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 70 | 70 | 20,00% | 0,37 | -0,42R | €-297,27 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 33 | 33 | 39,39% | 1,00 | 0,00R | €0,16 |
| Rapida 1H V3 Filtered | RANGE | 2 | 135 | 135 | 40,00% | 0,92 | -0,04R | €-57,61 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,80 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 19 | 19 | 42,11% | 1,56 | 0,22R | €42,15 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 72 | 72 | 40,28% | 1,13 | 0,06R | €45,04 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 51 | 51 | 23,53% | 0,45 | -0,38R | €-191,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 31 | 31 | 35,48% | 0,83 | -0,09R | €-28,70 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 110 | 110 | 41,82% | 1,09 | 0,04R | €48,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 11 | 11 | 45,45% | 1,72 | 0,28R | €30,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 26 | 26 | 26,92% | 0,62 | -0,21R | €-55,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 42 | 42 | 33,33% | 0,82 | -0,09R | €-38,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 2 | 10 | 10 | 20,00% | 0,21 | -0,66R | €-65,79 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 1 | 24 | 24 | 50,00% | 0,97 | -0,02R | €-4,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 68 | 68 | 44,12% | 0,91 | -0,05R | €-35,68 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 6 | 6 | 66,67% | 5,37 | 0,80R | €47,77 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,93 | -0,04R | €-5,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 29 | 29 | 62,07% | 1,34 | 0,14R | €40,93 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 11,11% | 0,20 | -0,65R | €-58,16 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 25 | 25 | 36,00% | 0,83 | -0,10R | €-24,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 70 | 70 | 38,57% | 0,97 | -0,02R | €-11,57 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 6 | 6 | 66,67% | 5,37 | 0,80R | €47,77 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 14 | 14 | 35,71% | 0,90 | -0,06R | €-8,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 31 | 31 | 35,48% | 1,00 | -0,00R | €-0,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 16 | 16 | 6,25% | 0,12 | -0,69R | €-110,28 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 29 | 29 | 37,93% | 0,88 | -0,06R | €-18,70 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 1 | 84 | 84 | 40,48% | 0,97 | -0,01R | €-12,29 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,40 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 8 | 8 | 62,50% | 6,64 | 0,78R | €62,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 20 | 20 | 40,00% | 0,93 | -0,04R | €-7,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 41 | 41 | 31,71% | 0,76 | -0,13R | €-53,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 42 | 42 | 16,67% | 0,31 | -0,51R | €-215,72 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 1 | 30 | 30 | 36,67% | 0,89 | -0,06R | €-17,28 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 2 | 135 | 135 | 40,00% | 0,92 | -0,04R | €-57,61 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 13 | 13 | 38,46% | 1,73 | 0,24R | €31,09 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 57 | 57 | 31,58% | 0,76 | -0,13R | €-75,01 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 69 | 69 | 20,29% | 0,38 | -0,41R | €-285,84 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 1 | 32 | 32 | 34,38% | 0,78 | -0,13R | €-40,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 2 | 133 | 133 | 39,85% | 0,90 | -0,05R | €-72,34 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,66 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 14 | 14 | 42,86% | 2,06 | 0,32R | €44,91 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 55 | 55 | 30,91% | 0,74 | -0,14R | €-77,70 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 6 | 9 | 9 | 33,33% | 2,02 | 0,47R | €42,28 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 8 | 13 | 13 | 30,77% | 0,39 | -0,43R | €-55,93 |
| SHADOW_4H_WIDE | RANGE | 9 | 47 | 47 | 17,02% | 0,64 | -0,26R | €-124,53 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 1 | 13 | 13 | 23,08% | 0,69 | -0,24R | €-31,18 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 15 | 15 | 26,67% | 1,04 | 0,02R | €3,35 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 1 | 28 | 28 | 28,57% | 1,18 | 0,11R | €31,88 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,38 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 0,94 | -0,04R | €-4,41 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 49 | 49 | 46,94% | 1,04 | 0,02R | €10,21 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 8 | 8 | 62,50% | 2,18 | 0,34R | €26,82 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 24 | 24 | 41,67% | 1,08 | 0,04R | €9,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,36 | -0,43R | €-21,25 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,16 | 0,09R | €3,64 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,56 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 1 | 44 | 44 | 27,27% | 0,67 | -0,20R | €-88,64 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 5 | 27 | 27 | 33,33% | 1,07 | 0,04R | €9,99 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 1 | 105 | 105 | 46,67% | 1,15 | 0,08R | €80,49 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,47 | -0,44R | €-21,91 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 34 | 34 | 41,18% | 1,50 | 0,25R | €84,09 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 23 | 23 | 30,43% | 0,49 | -0,30R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 67 | 67 | 35,82% | 1,25 | 0,11R | €75,00 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 18,18% | 0,65 | -0,20R | €-21,48 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 23 | 23 | 34,78% | 1,08 | 0,05R | €10,37 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 56 | 56 | 50,00% | 1,27 | 0,13R | €74,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 8 | 8 | 50,00% | 5,57 | 0,61R | €49,11 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 16 | 16 | 25,00% | 0,53 | -0,31R | €-48,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 37 | 37 | 27,03% | 0,53 | -0,23R | €-86,31 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 2 | 53 | 53 | 32,08% | 0,60 | -0,23R | €-124,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 2 | 34 | 34 | 38,24% | 0,97 | -0,02R | €-5,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 1 | 101 | 101 | 44,55% | 1,31 | 0,13R | €133,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,47 | -0,44R | €-21,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 19 | 19 | 42,11% | 1,81 | 0,32R | €60,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,64 | -0,18R | €-56,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 62 | 62 | 50,00% | 1,41 | 0,17R | €104,52 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 1 | 44 | 44 | 27,27% | 0,70 | -0,18R | €-81,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 5 | 25 | 25 | 36,00% | 1,21 | 0,11R | €26,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 1 | 93 | 93 | 49,46% | 1,25 | 0,12R | €113,49 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 17 | 17 | 35,29% | 1,10 | 0,05R | €8,21 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 23 | 23 | 34,78% | 0,55 | -0,26R | €-60,33 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 46 | 46 | 34,78% | 0,71 | -0,14R | €-62,20 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 7 | 7 | 14,29% | 0,46 | -0,32R | €-22,67 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 21 | 21 | 42,86% | 1,25 | 0,10R | €21,07 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 7 | 7 | 14,29% | 0,46 | -0,32R | €-22,67 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 21 | 21 | 28,57% | 1,11 | 0,04R | €9,37 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,05 | -0,56R | €-61,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 2 | 10 | 10 | 30,00% | 0,41 | -0,37R | €-36,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 32 | 32 | 43,75% | 1,36 | 0,19R | €60,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 6 | 6 | 16,67% | 0,62 | -0,20R | €-11,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 12 | 12 | 33,33% | 0,75 | -0,15R | €-18,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 14 | 14 | 28,57% | 1,29 | 0,09R | €12,52 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 25 | 25 | 32,00% | 0,82 | -0,11R | €-26,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 4 | 60 | 60 | 28,33% | 0,73 | -0,14R | €-81,51 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 10 | 10 | 30,00% | 0,53 | -0,22R | €-21,94 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 2,76 | 0,64R | €19,22 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 26 | 26 | 46,15% | 1,20 | 0,10R | €26,23 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 2 | 2 | 50,00% | 1,32 | 0,18R | €3,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 9 | 9 | 66,67% | 1,56 | 0,21R | €18,66 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 2 | 7 | 7 | 57,14% | 1,52 | 0,23R | €16,08 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 13 | 13 | 7,69% | 0,26 | -0,47R | €-61,61 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 4 | 22 | 22 | 40,91% | 1,38 | 0,20R | €44,23 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 62 | 62 | 46,77% | 1,61 | 0,30R | €183,80 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 22 | 22 | 54,55% | 2,08 | 0,42R | €91,60 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 15 | 15 | 20,00% | 0,53 | -0,32R | €-48,63 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 44 | 44 | 34,09% | 1,19 | 0,10R | €43,39 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 1 | 34 | 34 | 26,47% | 0,69 | -0,19R | €-63,23 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 4 | 26 | 26 | 30,77% | 0,96 | -0,02R | €-5,99 |
| SHADOW_COMBO_TREND | RANGE | 2 | 83 | 83 | 37,35% | 1,03 | 0,02R | €13,99 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,79R | €-31,62 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 27 | 27 | 40,74% | 1,48 | 0,25R | €66,21 |
| SHADOW_COMBO_TREND | TREND_DOWN | 1 | 22 | 22 | 27,27% | 0,49 | -0,31R | €-68,49 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 5 | 47 | 47 | 29,79% | 1,01 | 0,01R | €2,83 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 18,18% | 0,50 | -0,38R | €-42,23 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 4 | 4 | 50,00% | 0,64 | -0,20R | €-8,06 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,00 | -0,00R | €-0,06 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -0,68R | €-34,13 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,86 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,59 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 24 | 24 | 20,83% | 0,53 | -0,38R | €-90,84 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 3 | 12 | 12 | 16,67% | 0,26 | -0,59R | €-71,27 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 43 | 43 | 27,91% | 0,86 | -0,10R | €-42,42 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 12 | 12 | 41,67% | 1,71 | 0,38R | €45,05 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 0 | 10 | 10 | 30,00% | 0,21 | -0,49R | €-49,11 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 25 | 25 | 32,00% | 1,39 | 0,20R | €50,02 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 1,11 | 0,08R | €4,78 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 2 | 14 | 14 | 14,29% | 0,23 | -0,71R | €-99,32 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 3 | 4 | 4 | 25,00% | 0,03 | -0,52R | €-20,85 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 1 | 23 | 23 | 26,09% | 0,64 | -0,25R | €-57,49 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 5 | 5 | 80,00% | 8,33 | 1,49R | €74,32 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 0 | 8 | 8 | 37,50% | 0,25 | -0,49R | €-38,82 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 3 | 11 | 11 | 27,27% | 1,73 | 0,21R | €23,05 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 2 | 35 | 35 | 25,71% | 0,63 | -0,23R | €-78,96 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 4 | 26 | 26 | 26,92% | 0,77 | -0,15R | €-38,74 |
| SHADOW_EMA_TREND_1H | RANGE | 2 | 84 | 84 | 36,90% | 1,07 | 0,04R | €34,57 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,68 | -0,20R | €-10,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 25 | 25 | 36,00% | 1,18 | 0,10R | €24,34 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 1 | 23 | 23 | 30,43% | 0,51 | -0,29R | €-66,73 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 4 | 53 | 53 | 28,30% | 0,89 | -0,06R | €-33,03 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,87 | -0,09R | €-9,90 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,26 | -0,55R | €-16,36 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,11R | €1,10 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,20 | -0,68R | €-27,16 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,31 | -0,46R | €-23,07 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,84R | €8,38 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 4 | 4 | 50,00% | 1,36 | 0,20R | €7,90 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,91R | €38,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,02R | €0,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 2 | 13 | 13 | 30,77% | 0,95 | -0,03R | €-4,03 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 1 | 14 | 14 | 28,57% | 0,75 | -0,19R | €-26,86 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 56 | 56 | 33,93% | 1,03 | 0,02R | €11,12 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 7 | 7 | 71,43% | 9,54 | 1,25R | €87,66 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 21 | 21 | 42,86% | 1,55 | 0,30R | €63,09 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 3 | 38 | 38 | 26,32% | 0,74 | -0,19R | €-70,58 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 40,00% | 0,84 | -0,09R | €-13,49 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 34 | 34 | 76,47% | 2,25 | 0,31R | €104,28 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 109 | 109 | 69,72% | 1,64 | 0,19R | €208,32 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 18 | 18 | 77,78% | 2,92 | 0,33R | €59,55 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 33 | 33 | 63,64% | 1,33 | 0,11R | €37,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 69 | 69 | 56,52% | 0,86 | -0,06R | €-41,08 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,82 | -0,12R | €-12,78 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 56 | 56 | 39,29% | 1,30 | 0,18R | €100,98 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 6 | 6 | 50,00% | 2,89 | 0,64R | €38,65 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 20 | 20 | 40,00% | 1,39 | 0,22R | €44,20 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 4 | 39 | 39 | 20,51% | 0,53 | -0,36R | €-141,65 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 6 | 6 | 50,00% | 3,37 | 0,83R | €49,90 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 17 | 17 | 17,65% | 0,43 | -0,50R | €-85,17 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 50 | 50 | 36,00% | 1,34 | 0,21R | €104,30 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 5 | 5 | 40,00% | 1,87 | 0,36R | €17,78 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 18 | 18 | 44,44% | 1,71 | 0,37R | €66,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 37 | 37 | 18,92% | 0,50 | -0,38R | €-141,53 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 0,00% | 0,00 | -1,01R | €-50,68 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 48 | 48 | 37,50% | 1,15 | 0,10R | €46,26 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 6 | 6 | 50,00% | 5,42 | 0,80R | €48,15 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 13 | 13 | 23,08% | 0,65 | -0,25R | €-32,52 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 31 | 31 | 22,58% | 0,59 | -0,31R | €-97,30 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,82 | -0,12R | €-12,78 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 1 | 16 | 16 | 31,25% | 0,84 | -0,12R | €-19,15 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 53 | 53 | 39,62% | 1,33 | 0,20R | €103,48 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 6 | 6 | 50,00% | 2,89 | 0,64R | €38,65 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 19 | 19 | 42,11% | 1,52 | 0,29R | €54,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 3 | 39 | 39 | 20,51% | 0,53 | -0,36R | €-140,71 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 3 | 42 | 42 | 21,43% | 0,52 | -0,30R | €-126,71 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 35 | 35 | 31,43% | 0,78 | -0,13R | €-46,12 |
| Forza relativa 1H V1 | RANGE | 8 | 111 | 111 | 34,23% | 0,91 | -0,05R | €-55,50 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,89R | €-62,24 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 1 | 29 | 29 | 41,38% | 1,48 | 0,22R | €64,03 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 24 | 24 | 29,17% | 0,75 | -0,15R | €-35,56 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 3 | 67 | 67 | 29,85% | 1,14 | 0,07R | €46,61 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,70 | -0,16R | €-30,75 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 2 | 19 | 17 | 36,84% | 1,12 | 0,07R | €12,74 |
| Forza relativa 1H V2 | RANGE | 3 | 48 | 47 | 37,50% | 1,12 | 0,07R | €33,05 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 1 | 19 | 17 | 36,84% | 1,27 | 0,13R | €25,42 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 13 | 12 | 30,77% | 1,03 | 0,02R | €1,95 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 4 | 23 | 22 | 47,83% | 1,85 | 0,42R | €96,67 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,86 | 0,24R | €9,72 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 3 | 28 | 28 | 32,14% | 0,46 | -0,36R | €-101,09 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 10 | 10 | 50,00% | 1,31 | 0,16R | €16,08 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 1 | 8 | 8 | 0,00% | 0,00 | -0,26R | €-21,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,86 | 0,24R | €9,72 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 3 | 28 | 28 | 32,14% | 0,46 | -0,36R | €-101,09 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 10 | 10 | 50,00% | 1,31 | 0,16R | €16,08 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 1 | 8 | 8 | 0,00% | 0,00 | -0,26R | €-21,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,86 | 0,24R | €9,72 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 3 | 28 | 28 | 32,14% | 0,46 | -0,36R | €-101,09 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 10 | 10 | 50,00% | 1,31 | 0,16R | €16,08 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 1 | 8 | 8 | 0,00% | 0,00 | -0,26R | €-21,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 5 | 5 | 60,00% | 3,63 | 0,59R | €29,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 42 | 42 | 38,10% | 0,87 | -0,08R | €-32,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,31 | 0,16R | €6,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 25 | 25 | 40,00% | 1,06 | 0,03R | €8,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,66 | -0,16R | €-22,16 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 15 | 15 | 0,00% | 0,00 | -0,48R | €-72,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 26 | 26 | 30,77% | 0,31 | -0,45R | €-117,41 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -0,56R | €-11,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 2 | 31 | 31 | 58,06% | 0,59 | -0,19R | €-57,98 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,34 | 0,17R | €6,81 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 11 | 11 | 63,64% | 2,00 | 0,38R | €42,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 24 | 24 | 41,67% | 0,58 | -0,21R | €-49,35 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 1 | 10 | 10 | 50,00% | 1,05 | 0,02R | €2,18 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 23 | 23 | 30,43% | 0,24 | -0,49R | €-113,23 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,86 | 0,24R | €9,72 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 2 | 24 | 24 | 62,50% | 0,74 | -0,10R | €-24,72 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,31 | 0,16R | €6,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 11 | 11 | 63,64% | 1,78 | 0,30R | €33,12 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,65 | -0,17R | €-30,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 1 | 9 | 9 | 44,44% | 0,18 | -0,37R | €-33,20 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 7 | 7 | 28,57% | 1,30 | 0,13R | €9,07 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 4 | 19 | 19 | 31,58% | 0,82 | -0,10R | €-19,07 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 45 | 45 | 51,11% | 1,62 | 0,27R | €122,18 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 1 | 8 | 8 | 50,00% | 4,50 | 0,47R | €37,62 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 28 | 28 | 28,57% | 0,56 | -0,20R | €-55,79 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 7 | 7 | 28,57% | 1,30 | 0,13R | €9,07 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 20 | 20 | 30,00% | 0,75 | -0,15R | €-30,18 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 45 | 45 | 51,11% | 1,62 | 0,27R | €122,18 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 1 | 8 | 8 | 50,00% | 4,50 | 0,47R | €37,62 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 28 | 28 | 28,57% | 0,56 | -0,20R | €-55,79 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 7 | 7 | 28,57% | 1,30 | 0,13R | €9,07 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 20 | 20 | 30,00% | 0,75 | -0,15R | €-30,18 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 45 | 45 | 51,11% | 1,62 | 0,27R | €122,18 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 1 | 8 | 8 | 50,00% | 4,50 | 0,47R | €37,62 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 28 | 28 | 28,57% | 0,56 | -0,20R | €-55,79 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 12 | 12 | 8,33% | 0,30 | -0,42R | €-50,60 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 3 | 23 | 23 | 39,13% | 1,26 | 0,15R | €33,71 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 59 | 59 | 45,76% | 1,70 | 0,33R | €194,57 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 19 | 19 | 52,63% | 2,06 | 0,41R | €78,06 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 15 | 15 | 20,00% | 0,53 | -0,32R | €-48,63 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 43 | 43 | 32,56% | 1,10 | 0,05R | €22,68 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -0,03R | €-0,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 2 | 14 | 14 | 28,57% | 0,69 | -0,21R | €-29,48 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 7 | 7 | 57,14% | 4,49 | 0,52R | €36,32 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 30 | 30 | 33,33% | 1,01 | 0,01R | €1,82 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 0,00% | 0,00 | -0,68R | €-61,65 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 3 | 19 | 19 | 36,84% | 1,10 | 0,06R | €10,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 54 | 54 | 44,44% | 1,53 | 0,26R | €141,33 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 8 | 8 | 75,00% | 240,08 | 0,80R | €63,75 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 15 | 15 | 20,00% | 0,53 | -0,32R | €-48,63 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 24 | 24 | 20,83% | 0,44 | -0,32R | €-77,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 11,11% | 0,05 | -0,55R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 1 | 19 | 19 | 42,11% | 1,04 | 0,02R | €3,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 1 | 68 | 68 | 47,06% | 1,45 | 0,18R | €123,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 8 | 8 | 62,50% | 83,39 | 0,92R | €73,69 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,66 | -0,19R | €-35,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 26 | 26 | 50,00% | 1,12 | 0,05R | €12,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 0,00% | 0,00 | -0,64R | €-51,51 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 14 | 14 | 35,71% | 1,05 | 0,03R | €4,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 57 | 57 | 47,37% | 1,64 | 0,30R | €172,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 7 | 7 | 57,14% | 52,24 | 0,65R | €45,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 14 | 14 | 21,43% | 0,53 | -0,34R | €-47,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 20 | 20 | 20,00% | 0,49 | -0,29R | €-58,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 2 | 13 | 13 | 30,77% | 0,62 | -0,21R | €-27,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 1 | 19 | 19 | 42,11% | 1,04 | 0,02R | €3,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 1 | 68 | 68 | 47,06% | 1,45 | 0,18R | €123,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 10 | 10 | 50,00% | 6,68 | 0,63R | €63,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,66 | -0,19R | €-35,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 30 | 30 | 46,67% | 1,10 | 0,04R | €12,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 9,09% | 0,35 | -0,37R | €-40,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 2 | 14 | 14 | 35,71% | 1,05 | 0,03R | €4,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 57 | 57 | 47,37% | 1,64 | 0,30R | €172,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 7 | 7 | 57,14% | 52,24 | 0,65R | €45,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 14 | 14 | 21,43% | 0,53 | -0,34R | €-47,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 24 | 24 | 20,83% | 0,57 | -0,25R | €-58,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 2 | 14 | 14 | 28,57% | 0,54 | -0,27R | €-37,49 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 2 | 23 | 23 | 43,48% | 0,92 | -0,04R | €-8,93 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 1 | 63 | 63 | 47,62% | 1,44 | 0,18R | €113,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 12 | 12 | 58,33% | 4,51 | 0,62R | €74,55 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 20 | 20 | 35,00% | 0,59 | -0,23R | €-46,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 35 | 35 | 48,57% | 1,20 | 0,07R | €25,40 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 20,00% | 1,04 | 0,02R | €0,83 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 23 | 23 | 34,78% | 1,23 | 0,13R | €29,55 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 51 | 51 | 43,14% | 1,56 | 0,29R | €145,37 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 7 | 7 | 71,43% | 188,08 | 0,71R | €49,89 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 15 | 15 | 20,00% | 0,54 | -0,31R | €-47,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 28 | 28 | 17,86% | 0,41 | -0,36R | €-99,94 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -0,41R | €-20,67 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 24 | 24 | 37,50% | 1,25 | 0,13R | €31,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 47 | 47 | 42,55% | 1,62 | 0,33R | €154,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 7 | 7 | 71,43% | 188,08 | 0,71R | €49,89 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 14 | 14 | 21,43% | 0,62 | -0,25R | €-35,32 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 27 | 27 | 18,52% | 0,48 | -0,31R | €-83,11 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 14 | 14 | 14,29% | 0,42 | -0,38R | €-53,84 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 3 | 24 | 24 | 33,33% | 0,92 | -0,05R | €-11,27 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 59 | 59 | 49,15% | 1,69 | 0,32R | €186,68 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,96 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 21 | 21 | 47,62% | 2,00 | 0,40R | €83,66 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 58 | 58 | 37,93% | 1,25 | 0,12R | €68,65 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,51 | -0,36R | €-21,78 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 4 | 4 | 75,00% | 3,71 | 0,76R | €30,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,67 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,55 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-06T16:24:18+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **17**
- Scenari virtuali ancora attivi: **300**
- Gruppi in attesa dell'uscita originale: **17**
- Gruppi con originale chiuso ma Shadow ancora attive: **0**
- Confronti completati: **122547**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3262 | 3328 | +€9,11 | 51,7% | 916 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3262 | 3328 | +€7,46 | 50,8% | 916 | 30 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3262 | 3328 | +€6,66 | 43,1% | 710 | 88 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3262 | 3328 | +€6,23 | 49,2% | 916 | 78 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3262 | 3328 | +€5,08 | 33,1% | 411 | 381 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3262 | 3328 | +€4,85 | 48,7% | 1019 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3262 | 3328 | +€4,82 | 42,7% | 686 | 126 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3262 | 3328 | +€4,61 | 49,1% | 858 | 138 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3262 | 3328 | +€4,49 | 41,1% | 778 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3262 | 3328 | +€4,16 | 41,7% | 601 | 215 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3262 | 3328 | +€3,79 | 35,6% | 198 | 622 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3262 | 3328 | +€2,28 | 40,0% | 519 | 371 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3262 | 3328 | €-0,33 | 31,4% | 368 | 694 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3262 | 3328 | €-1,01 | 28,8% | 311 | 827 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3262 | 3328 | €-1,06 | 39,6% | 400 | 735 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3262 | 3328 | €-1,44 | 45,6% | 670 | 492 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3262 | 3328 | €-3,74 | 33,0% | 547 | 713 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3262 | 3328 | €-4,51 | 31,8% | 187 | 1001 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3262 | 3328 | €-5,35 | 27,2% | 260 | 910 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3262 | 3328 | €-8,66 | 22,5% | 260 | 1043 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-06T16:24:30+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **122547**
- Valutazioni prodotte: **18422**
- Candidature al Blocco 5: **5**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_MBV3_GB20_R100 | 181 | 0,353 | 0,149 | 0,245 | 61,9% | 93,8 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 1851 | 0,292 | 0,149 | 0,244 | 55,9% | 89,0 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 1851 | 0,263 | 0,135 | 0,217 | 55,5% | 88,7 | ELIGIBLE_FOR_MUTATION |
| GB20_R050 | 1851 | 0,316 | 0,149 | 0,268 | 54,7% | 87,6 | VALIDATING |
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

Generato: 2026-08-06T16:26:44+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 28 | 100,00% | 1,31 | +€102,25 | +€3,65 | 1,50% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 28 | 100,00% | 1,17 | +€57,70 | +€2,06 | 1,48% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 9 | 100,00% | 0,58 | €-111,91 | €-12,43 | 1,12% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 6 | 100,00% | 0,00 | €-104,80 | €-17,47 | 1,05% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 25 | 100,00% | 0,98 | €-11,82 | €-0,47 | 2,13% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-06T16:24:01+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **0**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **196.29 R**
- Profitto virtuale mancato: **312.09 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 2 | 0 | 111.55 |
| DOWN_20 | 2 | 0 | 223.09 |
| DOWN_30 | 2 | 0 | 334.64 |
| DOWN_40 | 2 | 1 | 444.41 |
| UP_10 | 9 | 0 | 640.45 |
| UP_20 | 9 | 0 | 1280.89 |
| UP_30 | 9 | 0 | 1921.34 |
| UP_40 | 9 | 3 | 2336.25 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-06T16:23:16+00:00

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

Generato: 2026-08-06T16:26:46+00:00

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

Generato: 2026-08-06T16:26:46+00:00

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

Generato: 2026-08-06T16:26:46+00:00

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

Generato: 2026-08-06T16:26:46+00:00

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
| 1 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 16.9 | E | 64 | 1.44 | 0.175 | 5.40 |
| 2 | SHADOW_COMBO_ADAPTIVE | BASELINE | 16.7 | E | 40 | 1.70 | 0.187 | 2.72 |
| 3 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 16.6 | E | 72 | 1.31 | 0.122 | 3.55 |
| 4 | SHADOW_1H_FAST_V3 | BASELINE | 16.5 | E | 103 | 1.13 | 0.054 | 5.36 |
| 5 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 16.4 | E | 33 | 1.66 | 0.244 | 6.54 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 16.2 | E | 36 | 1.52 | 0.195 | 3.32 |
| 7 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 15.9 | E | 75 | 1.22 | 0.086 | 3.78 |
| 8 | SHADOW_DONCHIAN_1H | BASELINE | 14.9 | E | 39 | 1.45 | 0.242 | 8.55 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 14.6 | E | 59 | 1.26 | 0.085 | 5.89 |
| 10 | SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | BASELINE | 14.6 | E | 33 | 1.42 | 0.175 | 4.19 |

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

Generato: 2026-08-06T16:26:46+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **610**
- Strategie preferite nel regime corrente: **7**
- Strategie da evitare nel regime corrente: **4**
- Memorie contestuali: **287**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.115 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 5 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 77.2 | 17 | 2.60 | 0.490 | 2.17 |
| 6 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | OBSERVING | 76.1 | 12 | 2.82 | 0.491 | 2.17 |
| 7 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 76.1 | 7 | 2.35 | 0.426 | 1.11 |
| 8 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 75.4 | 28 | 1.97 | 0.234 | 1.71 |
| 9 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.5 | 12 | 2.82 | 0.322 | 1.04 |
| 10 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | OBSERVING | 72.0 | 20 | 1.91 | 0.313 | 3.16 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-06T16:26:46+00:00

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

Generato: 2026-08-06T16:24:01+00:00

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
