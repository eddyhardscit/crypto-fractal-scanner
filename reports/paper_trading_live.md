# Paper trading automatico KuCoin

Generato: 2026-08-01T15:12:28+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-01T15:08:27+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-01T15:08:27+00:00 | 2026-08-01T15:08:27+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-01T14:45:00+00:00 | 2026-08-01T14:45:00+00:00 | 8,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-01T14:00:00+00:00 | 2026-08-01T14:00:00+00:00 | 8,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-01T08:00:00+00:00 | 2026-08-01T08:00:00+00:00 | 3,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | 1000RATS | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | GIGGLE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 7,70 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,03 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -6,15 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | KOMA | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -5,54 | 6,00 | 0,46 | STALE_CANDLE | 3,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -5,25 | 6,00 | 0,75 | STALE_CANDLE | 3,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,81 | 6,00 | 1,19 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,18 | 6,00 | 1,82 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -1,88 | 6,00 | 4,12 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | BANK | 60m | SHORT | -7,75 | 5,50 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | SHORT | -7,75 | 5,00 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | ADA | 60m | LONG | 6,63 | 5,50 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | ADA | 60m | LONG | 6,63 | 4,50 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.37%. |
| Rapida V1 — score 6–7,5 | ADA | 60m | LONG | 6,63 | 6,00 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.37%. |
| Rapida score 6–7,5 — senza Trend Up | ADA | 60m | LONG | 6,63 | 6,00 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.37%. |
| Rapida score 6–7,5 — Range Only | ADA | 60m | LONG | 6,63 | 6,00 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.37%. |
| Rapida score 6–7,5 — Cost Aware | ADA | 60m | LONG | 6,63 | 6,00 | 0,00 | STRATEGY_FILTER | 8,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.37%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.741,83 | -2,58% | €-6,52 | €3.000,00 | -0,22% | 5 | 28 | 32,14% | 0,70 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 28 | 999 | CAMPIONE INSUFFICIENTE | 30 (mancano 2) |

- Trade del Principale 4H chiusi: **28**; win rate **32,14%**; profit factor **0,70**.
- Expectancy: **€-11,24** per trade; P&L netto: **€-314,61**; max drawdown: **6,36%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.741,83 | €1.111,96 | €3.335,87 | €99,53 | €56,52 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.563,40 | €267,67 | €535,34 | €54,19 | €0,00 |
| TEST | Rapida score 6–7,5 — Cost Aware | 0 | €10.506,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 0 | €10.492,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €10.485,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 0 | €10.440,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 0 | €10.399,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 0 | €10.355,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 1 | €10.314,28 | €88,92 | €177,84 | €4,31 | €0,00 |
| TEST | Bilanciata 1H V1 | 2 | €10.305,19 | €35,29 | €105,87 | €5,62 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.295,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 0 | €10.283,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 0 | €10.278,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.273,29 | €1.389,97 | €4.169,92 | €101,81 | €60,37 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Combo Adaptive — madre | 1 | €10.112,06 | €28,25 | €56,50 | €1,30 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.096,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 0 | €10.096,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 1 | €10.071,83 | €28,88 | €57,76 | €1,33 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 0 | €10.030,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 2 | €10.028,64 | €412,14 | €824,28 | €98,91 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 0 | €10.012,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.011,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.987,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 1 | €9.985,09 | €15,45 | €30,90 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.976,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 0 | €9.973,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.971,52 | €1.133,51 | €2.267,02 | €101,52 | €-0,04 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 1 | €9.969,91 | €18,15 | €36,30 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.959,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 1 | €9.957,83 | €17,73 | €35,46 | €0,77 | €0,00 |
| TEST | Scanner Bottom15 Short | 1 | €9.957,83 | €17,73 | €35,46 | €0,77 | €0,00 |
| TEST | Scanner Bottom20 Short | 1 | €9.957,83 | €17,73 | €35,46 | €0,77 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.953,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.948,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 0 | €9.934,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 0 | €9.931,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 0 | €9.924,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.900,92 | €780,22 | €1.560,44 | €49,48 | €5,17 |
| TEST | Btc Donchian 4H | 0 | €9.898,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 1 | €9.893,19 | €17,87 | €35,75 | €0,78 | €0,00 |
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
| TEST | Benchmark trend following EMA 1H | 1 | €9.708,51 | €22,55 | €45,10 | €0,00 | €0,00 |
| TEST | Combo Scanner | 0 | €9.693,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 0 | €9.688,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 0 | €9.679,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 1 | €9.657,23 | €136,07 | €408,22 | €48,55 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.639,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.625,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 2 | €9.623,77 | €313,66 | €627,32 | €52,59 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 0 | €9.583,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top20 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 2 | €9.530,20 | €93,60 | €187,20 | €2,80 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.741,83 | €-314,61 | 28 | 28 | 32,14% | 0,70 | €-11,24 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.563,40 | €564,30 | 38 | 38 | 55,26% | 1,62 | €14,85 | 3,09% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.506,14 | €506,14 | 36 | 36 | 52,78% | 1,93 | €14,06 | 1,96% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.492,11 | €492,11 | 64 | 64 | 46,88% | 1,41 | €7,69 | 2,83% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.485,55 | €485,55 | 75 | 75 | 44,00% | 1,37 | €6,47 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.440,04 | €440,04 | 66 | 66 | 39,39% | 1,33 | €6,67 | 2,82% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.399,89 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.355,52 | €355,52 | 50 | 50 | 44,00% | 1,30 | €7,11 | 4,79% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.314,28 | €314,39 | 7 | 7 | 71,43% | 6,32 | €44,91 | 1,61% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.305,19 | €305,25 | 73 | 73 | 46,58% | 1,24 | €4,18 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.295,72 | €295,72 | 12 | 12 | 58,33% | 2,80 | €24,64 | 1,78% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.283,50 | €283,50 | 33 | 33 | 54,55% | 1,80 | €8,59 | 1,58% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.278,80 | €278,80 | 41 | 39 | 51,22% | 1,36 | €6,80 | 2,75% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.273,29 | €212,50 | 13 | 13 | 46,15% | 1,65 | €16,35 | 2,40% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
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
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.112,06 | €112,10 | 39 | 39 | 43,59% | 1,21 | €2,87 | 2,58% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.096,23 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.096,10 | €96,10 | 59 | 59 | 50,85% | 1,11 | €1,63 | 2,98% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.071,83 | €71,86 | 42 | 42 | 38,10% | 1,11 | €1,71 | 2,31% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.030,12 | €30,12 | 103 | 103 | 37,86% | 1,02 | €0,29 | 2,95% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.028,64 | €29,13 | 28 | 28 | 53,57% | 1,06 | €1,04 | 2,61% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.012,08 | €12,08 | 26 | 26 | 34,62% | 1,03 | €0,46 | 2,48% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.011,51 | €11,51 | 12 | 12 | 41,67% | 1,24 | €0,96 | 0,25% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,30 | €2,30 | 12 | 12 | 41,67% | 1,24 | €0,19 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,54 | €-2,46 | 3 | 3 | 0,00% | 0,00 | €-0,82 | 0,03% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,70 | €-10,30 | 8 | 8 | 25,00% | 0,21 | €-1,29 | 0,14% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.987,70 | €-12,30 | 3 | 3 | 0,00% | 0,00 | €-4,10 | 0,17% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.985,09 | €-14,89 | 18 | 18 | 44,44% | 0,95 | €-0,83 | 1,38% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.976,03 | €-23,97 | 3 | 3 | 0,00% | 0,00 | €-7,99 | 0,32% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.973,32 | €-26,68 | 79 | 79 | 35,44% | 0,98 | €-0,34 | 2,58% |
| TEST | Ampia 4H | Confluenza trend | €9.971,52 | €-27,14 | 25 | 25 | 24,00% | 0,96 | €-1,09 | 3,68% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.969,91 | €-30,07 | 19 | 19 | 42,11% | 0,86 | €-1,58 | 1,53% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.959,54 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 0,89% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.957,83 | €-42,14 | 24 | 24 | 41,67% | 0,91 | €-1,76 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.957,83 | €-42,14 | 24 | 24 | 41,67% | 0,91 | €-1,76 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.957,83 | €-42,14 | 24 | 24 | 41,67% | 0,91 | €-1,76 | 2,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.953,74 | €-46,26 | 12 | 12 | 41,67% | 0,30 | €-3,86 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,48 | €-51,52 | 8 | 8 | 25,00% | 0,21 | €-6,44 | 0,68% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.948,06 | €-51,94 | 8 | 8 | 12,50% | 0,10 | €-6,49 | 0,66% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.934,23 | €-65,77 | 55 | 54 | 38,18% | 0,96 | €-1,20 | 5,53% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.931,86 | €-68,14 | 20 | 20 | 25,00% | 0,81 | €-3,41 | 2,34% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.924,82 | €-75,18 | 36 | 36 | 38,89% | 0,90 | €-2,09 | 4,41% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Sol Ema 4H | Trend following EMA | €9.900,92 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,44% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.898,26 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,48% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.893,19 | €-106,79 | 46 | 46 | 36,96% | 0,87 | €-2,32 | 5,48% |
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
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.708,51 | €-291,46 | 45 | 45 | 31,11% | 0,71 | €-6,48 | 3,97% |
| TEST | Combo Scanner | Combo Scanner | €9.693,00 | €-307,00 | 50 | 50 | 36,00% | 0,77 | €-6,14 | 5,08% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.688,64 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 3,94% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.679,07 | €-320,93 | 19 | 19 | 21,05% | 0,55 | €-16,89 | 4,64% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.657,23 | €-342,52 | 19 | 19 | 26,32% | 0,47 | €-18,03 | 4,32% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.639,39 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.625,26 | €-374,74 | 54 | 54 | 55,56% | 0,59 | €-6,94 | 4,27% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.623,77 | €-375,86 | 50 | 50 | 26,00% | 0,69 | €-7,52 | 7,55% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.583,73 | €-416,27 | 34 | 34 | 32,35% | 0,46 | €-12,24 | 5,03% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Combo Trend | Combo Trend | €9.530,20 | €-469,68 | 60 | 60 | 31,67% | 0,74 | €-7,83 | 7,64% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.463,31 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,43% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.449,51 | €-550,49 | 56 | 56 | 28,57% | 0,62 | €-9,83 | 6,47% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.405,07 | €-594,93 | 27 | 27 | 22,22% | 0,49 | €-22,03 | 6,15% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.331,79 | €-668,21 | 50 | 50 | 28,00% | 0,42 | €-13,36 | 6,71% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 72,94800 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €0,09 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,07006 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €2,62 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 52,49600 | 53,24153 | 73,46073 | 50,62613 | €353,42 | €1.060,27 | €0,00 | €53,81 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,34076 | 3,34076 | 2,94410 | 2,24388 | 4,13409 | €15,79 | €47,36 | €5,62 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,38464 | 3,38464 | 2,98212 | 2,27335 | 4,18968 | €136,07 | €408,22 | €48,55 | €0,00 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,06502 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €-0,02 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07006 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,02 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | BEAT | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 3,34076 | 3,34076 | 2,94410 | 1,68709 | 4,21342 | €200,74 | €401,49 | €47,67 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,67989 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,00 |
| Combo Adaptive — madre | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 72,94800 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €5,17 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,07006 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €2,49 |
| MAIN — Side × Regime Guard | ZEC | SHORT | Confluenza trend | 240m | 3,0x | 469,12616 | 470,58000 | 492,16341 | 623,15591 | 423,05164 | €346,80 | €1.040,39 | €51,09 | €-3,22 |
| MAIN — Side × Regime Guard | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 52,49600 | 53,24153 | 73,46073 | 50,62613 | €401,28 | €1.203,85 | €0,00 | €61,10 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €15,45 | €30,90 | €0,00 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend | ALLO | SHORT | 2026-08-01T15:08:42+00:00 | 0,35393 | €-1,31 | -0,03 | TIME_EXIT_NO_CANDLES |
| Benchmark trend following EMA 1H | XMR | LONG | 2026-08-01T15:08:42+00:00 | 366,85987 | €-0,06 | -0,09 | TIME_EXIT_NO_CANDLES |
| Benchmark trend following EMA 1H | ALLO | SHORT | 2026-08-01T15:08:42+00:00 | 0,35393 | €-1,31 | -0,03 | TIME_EXIT_NO_CANDLES |
| Forza relativa 1H V2 | XMR | LONG | 2026-08-01T15:08:42+00:00 | 366,85987 | €-5,20 | -0,10 | TIME_EXIT_NO_CANDLES |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | 2026-08-01T13:38:40+00:00 | 0,00001 | €-1,86 | -0,04 | TIME_EXIT_NO_CANDLES |
| Combo Adaptive — Long Only | SHIB | LONG | 2026-08-01T13:38:40+00:00 | 0,00001 | €-0,05 | -0,04 | TIME_EXIT_NO_CANDLES |
| Forza relativa 1H V2 | WLD | SHORT | 2026-08-01T10:38:41+00:00 | 0,34370 | €-0,17 | -0,07 | TIME_EXIT_NO_CANDLES |
| Forza relativa 1H V1 | WLD | SHORT | 2026-08-01T10:38:41+00:00 | 0,34370 | €-0,05 | -0,07 | TIME_EXIT_NO_CANDLES |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | 2026-08-01T07:38:40+00:00 | 0,35271 | €-0,85 | -0,02 | TIME_EXIT_NO_CANDLES |
| Scalp RSI Short 75 · prudente · 5x | ZEC | SHORT | 2026-08-01T06:23:46+00:00 | 464,08888 | €0,93 | 0,09 | STOP |
| Scalp RSI Short 75 · €50 · 15x | ZEC | SHORT | 2026-08-01T06:23:46+00:00 | 463,90817 | €0,60 | 0,18 | STOP |
| Scalp RSI Short 75 · €10 · 15x | ZEC | SHORT | 2026-08-01T06:23:46+00:00 | 463,90817 | €0,12 | 0,18 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 108/30 | 33/30 | 0,85 | 2,04 | -0,08R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 84/30 | 20/30 | 0,59 | 1,90 | -0,23R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 45/30 | 22/30 | 0,89 | 1,74 | -0,07R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 45/30 | 22/30 | 0,94 | 1,57 | -0,03R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 61/30 | 31/30 | 0,79 | 0,62 | -0,13R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 42/30 | 11/30 | 0,64 | 0,00 | -0,20R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 31/30 | 8/30 | 1,25 | 1,02 | 0,10R | €0,42 | 2,15% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 77/30 | 17/30 | 0,60 | 4,50 | -0,25R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 103/30 | 24/30 | 0,76 | 0,64 | -0,14R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 79/30 | 7/30 | 0,54 | 0,02 | -0,27R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 61/30 | 30/30 | 0,95 | 1,02 | -0,03R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 147/30 | 55/30 | 0,84 | 1,12 | -0,08R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 36/30 | 15/30 | 0,46 | 0,99 | -0,38R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 131/30 | 44/30 | 0,70 | 1,20 | -0,17R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 135/30 | 37/30 | 0,71 | 0,76 | -0,16R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 109/30 | 23/30 | 0,54 | 1,12 | -0,26R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 115/30 | 28/30 | 0,85 | 0,70 | -0,10R | €-11,24 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 13/30 | 0,00 | 1,65 | 0,00R | €16,35 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 13/30 | 8/30 | 0,23 | 0,10 | -0,62R | €-6,49 | 0,66% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 16/30 | 12/30 | 0,49 | 0,30 | -0,26R | €-3,86 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 300/30 | 73/30 | 0,91 | 1,24 | -0,05R | €4,18 | 3,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 19/30 | 0,00 | 0,47 | 0,00R | €-18,03 | 4,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 2/30 | 0,00 | 0,00 | 0,00R | €-28,31 | 1,11% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 88/30 | 39/30 | 1,23 | 1,36 | 0,12R | €6,80 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 168/30 | 66/30 | 0,95 | 1,33 | -0,03R | €6,67 | 2,82% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 89/30 | 22/30 | 0,64 | 0,72 | -0,22R | €-5,70 | 2,01% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 40/30 | 25/30 | 1,44 | 0,99 | 0,21R | €-0,14 | 2,27% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 111/30 | 28/30 | 1,04 | 1,69 | 0,02R | €8,25 | 1,76% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 178/30 | 64/30 | 1,06 | 1,41 | 0,03R | €7,69 | 2,83% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 239/30 | 72/30 | 0,81 | 1,14 | -0,11R | €2,56 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 36/30 | 0,00 | 1,93 | 0,00R | €14,06 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 33/30 | 0,00 | 1,32 | 0,00R | €6,27 | 2,77% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 13/30 | 0,00 | 1,74 | 0,00R | €16,77 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 154/30 | 75/30 | 0,98 | 1,37 | -0,01R | €6,47 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 226/30 | 79/30 | 0,81 | 0,98 | -0,11R | €-0,34 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 18/30 | 15/30 | 0,78 | 0,93 | -0,14R | €-1,52 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 267/30 | 103/30 | 0,89 | 1,02 | -0,06R | €0,29 | 2,95% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 182/30 | 68/30 | 0,96 | 1,16 | -0,02R | €3,19 | 3,62% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 81/30 | 49/30 | 1,12 | 0,93 | 0,06R | €-1,56 | 3,21% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 81/30 | 44/30 | 1,15 | 0,86 | 0,08R | €-3,24 | 2,86% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 108/30 | 56/30 | 1,00 | 0,62 | 0,00R | €-9,83 | 6,47% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 12/30 | 0,00 | 2,80 | 0,00R | €24,64 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 20/30 | 0,00 | 3,42 | 0,00R | €19,99 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 189/30 | 62/30 | 0,90 | 0,90 | -0,06R | €-2,09 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 36/30 | 0,00 | 0,90 | 0,00R | €-2,09 | 4,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 59/30 | 0,00 | 1,11 | 0,00R | €1,63 | 2,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 20/30 | 0,00 | 1,17 | 0,00R | €3,80 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 220/30 | 77/30 | 0,80 | 0,89 | -0,11R | €-2,26 | 2,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 100/30 | 25/30 | 0,80 | 0,96 | -0,14R | €-1,09 | 3,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 82/30 | 50/30 | 1,42 | 0,82 | 0,19R | €-4,77 | 5,70% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 6/30 | 4/30 | 0,16 | 0,63 | -0,62R | €-10,11 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 6/30 | 4/30 | 5,15 | 2,94 | 0,78R | €27,74 | 0,70% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 8/30 | 5/30 | 0,16 | 0,97 | -0,71R | €-0,63 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,48% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 7/30 | 7/30 | 1,01 | 0,48 | 0,00R | €-20,19 | 1,56% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 228/30 | 39/30 | 1,06 | 1,21 | 0,03R | €2,87 | 2,58% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 85/30 | 20/30 | 0,94 | 0,81 | -0,04R | €-3,41 | 2,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 213/30 | 50/30 | 1,00 | 0,42 | -0,00R | €-13,36 | 6,71% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 169/30 | 41/30 | 0,95 | 0,60 | -0,03R | €-7,07 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 15/30 | 11/30 | 0,77 | 0,71 | -0,13R | €-7,09 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 15/30 | 11/30 | 0,70 | 0,31 | -0,17R | €-18,43 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 52/30 | 26/30 | 0,97 | 1,03 | -0,02R | €0,46 | 2,48% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 61/30 | 22/30 | 0,62 | 0,79 | -0,25R | €-4,40 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 42/30 | 0,74 | 1,11 | -0,20R | €1,71 | 2,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 33/30 | 0,00 | 1,80 | 0,00R | €8,59 | 1,58% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 24/30 | 0,74 | 0,71 | -0,20R | €-4,85 | 2,44% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 39/30 | 20/30 | 1,15 | 0,76 | 0,08R | €-8,37 | 3,60% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_SCANNER | Combo Scanner | 122/30 | 50/30 | 1,30 | 0,77 | 0,17R | €-6,14 | 5,08% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 183/30 | 60/30 | 0,93 | 0,74 | -0,04R | €-7,83 | 7,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 28/30 | 0,00 | 1,06 | 0,00R | €1,04 | 2,61% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 4/30 | 4/30 | 0,41 | 0,41 | -0,50R | €-24,49 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 7/30 | 6/30 | 0,67 | 1,34 | -0,26R | €6,42 | 1,08% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 12/30 | 10/30 | 0,55 | 1,57 | -0,29R | €9,62 | 1,36% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 98/30 | 38/30 | 0,73 | 1,62 | -0,21R | €14,85 | 3,09% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 31/30 | 7/30 | 0,51 | 6,32 | -0,37R | €44,91 | 1,61% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 189/30 | 45/30 | 0,90 | 0,71 | -0,06R | €-6,48 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 8/30 | 6/30 | 0,37 | 0,08 | -0,52R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 3/30 | 2/30 | 2,41 | 0,28 | 0,53R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 6/30 | 5/30 | 0,57 | 0,42 | -0,33R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 9/30 | 8/30 | 0,32 | 0,16 | -0,59R | €-34,02 | 2,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-52,87 | 1,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 5/30 | 13/30 | 2,85 | 0,44 | 0,81R | €-16,58 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 91/30 | 22/30 | 0,91 | 0,74 | -0,06R | €-9,13 | 3,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 22/30 | 0,00 | 0,66 | 0,00R | €-8,95 | 3,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 19/30 | 0,00 | 0,55 | 0,00R | €-16,89 | 4,64% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 17/30 | 0,00 | 0,62 | 0,00R | €-12,19 | 2,93% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 131/30 | 54/30 | 1,12 | 0,59 | 0,05R | €-6,94 | 4,27% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 82/30 | 19/30 | 0,85 | 0,66 | -0,10R | €-12,69 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 78/30 | 21/30 | 0,87 | 0,68 | -0,10R | €-10,87 | 3,98% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 60/30 | 27/30 | 0,86 | 0,49 | -0,10R | €-22,03 | 6,15% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 88/30 | 19/30 | 0,86 | 0,66 | -0,10R | €-12,90 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 237/30 | 50/30 | 0,86 | 0,69 | -0,09R | €-7,52 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 98/30 | 54/30 | 1,17 | 0,96 | 0,09R | €-1,20 | 5,53% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 73/30 | 24/30 | 0,44 | 0,91 | -0,37R | €-1,76 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 73/30 | 24/30 | 0,44 | 0,91 | -0,37R | €-1,76 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 73/30 | 24/30 | 0,44 | 0,91 | -0,37R | €-1,76 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 109/30 | 46/30 | 0,82 | 0,87 | -0,11R | €-2,32 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 75/30 | 18/30 | 0,75 | 0,95 | -0,12R | €-0,83 | 1,38% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 64/30 | 19/30 | 0,72 | 0,86 | -0,14R | €-1,58 | 1,53% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 52/30 | 22/30 | 0,97 | 0,34 | -0,02R | €-20,99 | 6,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 53/30 | 22/30 | 0,94 | 0,34 | -0,04R | €-20,99 | 6,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 53/30 | 22/30 | 0,94 | 0,34 | -0,04R | €-20,99 | 6,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 117/30 | 41/30 | 1,27 | 1,25 | 0,15R | €5,47 | 3,94% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 28/30 | 10/30 | 0,73 | 0,87 | -0,17R | €-3,13 | 2,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 73/30 | 22/30 | 0,93 | 0,64 | -0,04R | €-10,44 | 4,43% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 70/30 | 34/30 | 1,29 | 0,61 | 0,14R | €-10,61 | 3,93% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 63/30 | 19/30 | 1,13 | 0,70 | 0,07R | €-10,12 | 4,36% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 75/30 | 41/30 | 1,27 | 0,53 | 0,13R | €-13,09 | 5,43% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 68/30 | 24/30 | 1,09 | 0,59 | 0,05R | €-12,97 | 3,94% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 87/30 | 34/30 | 1,16 | 0,46 | 0,08R | €-12,24 | 5,03% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 69/30 | 30/30 | 1,01 | 0,79 | 0,01R | €-5,41 | 4,99% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 67/30 | 26/30 | 1,04 | 0,80 | 0,03R | €-6,02 | 4,68% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 133/30 | 50/30 | 1,20 | 1,30 | 0,12R | €7,11 | 4,79% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 12/30 | 7/30 | 0,34 | 0,24 | -0,61R | €-31,26 | 2,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 2/30 | 0,00 | 0,65 | -1,05R | €-8,96 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 5/30 | 5/30 | 0,88 | 0,82 | -0,06R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 7/30 | 4/30 | 0,28 | 26,39 | -0,69R | €28,48 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 2/30 | 0,00 | 0,71 | -1,06R | €-7,50 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 10/30 | 7/30 | 0,43 | 0,52 | -0,51R | €-18,88 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-51,84 | 1,44% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07006**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 27.4 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63091 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07011**; close **0.07011**; wick alta **0.0%**; volume **x0.39**

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

- Regime: **TREND_DOWN**
- Famiglia: **TREND_DOWN**
- Confidenza: **64,30%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC ribassista confermato dalla breadth: score -2.0, 42% sopra EMA50, ADX 26.5.
- BTC trend score: **-2,00**; ADX: **26,54**; breadth sopra EMA50: **41,67%**
- Mediana alt vs BTC: **-0,42%**; dispersione: **10,10%**

- Aperti in questo ciclo: **14**
- Chiusi in questo ciclo: **4**
- Posizioni research aperte: **589**
- Trade research chiusi: **8647**
- Eventi di mercato indipendenti chiusi: **1524**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **29463**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 5 | 108 | 108 | 31,48% | 0,85 | -0,08R | €-85,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 4 | 84 | 84 | 29,76% | 0,59 | -0,23R | €-193,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 2 | 45 | 45 | 44,44% | 0,89 | -0,07R | €-29,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 3 | 45 | 45 | 37,78% | 0,94 | -0,03R | €-15,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 3 | 61 | 61 | 32,79% | 0,79 | -0,13R | €-76,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 3 | 42 | 42 | 33,33% | 0,64 | -0,20R | €-83,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 31 | 31 | 35,48% | 1,25 | 0,10R | €31,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 4 | 77 | 77 | 23,38% | 0,60 | -0,25R | €-193,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 7 | 103 | 103 | 29,13% | 0,76 | -0,14R | €-140,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 5 | 79 | 79 | 26,58% | 0,54 | -0,27R | €-210,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 3 | 61 | 61 | 36,07% | 0,95 | -0,03R | €-16,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 8 | 147 | 147 | 40,14% | 0,84 | -0,08R | €-115,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 36 | 36 | 22,22% | 0,46 | -0,38R | €-137,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 7 | 131 | 131 | 27,48% | 0,70 | -0,17R | €-219,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 7 | 135 | 135 | 27,41% | 0,71 | -0,16R | €-219,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 5 | 109 | 109 | 25,69% | 0,54 | -0,26R | €-287,75 |
| MAIN | 21 | 115 | 115 | 29,57% | 0,85 | -0,10R | €-112,20 |
| RSI_EXTREME_LONG_15M | 0 | 13 | 13 | 23,08% | 0,23 | -0,62R | €-80,39 |
| RSI_EXTREME_SHORT_15M | 0 | 16 | 16 | 37,50% | 0,49 | -0,26R | €-42,33 |
| Bilanciata 1H V1 | 18 | 300 | 300 | 33,00% | 0,91 | -0,05R | €-161,39 |
| Bilanciata 1H V2 | 7 | 99 | 88 | 39,39% | 1,23 | 0,12R | €121,27 |
| Bilanciata 1H V3 Filtered | 13 | 168 | 168 | 35,12% | 0,95 | -0,03R | €-52,46 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 13 | 89 | 89 | 31,46% | 0,64 | -0,22R | €-197,81 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 40 | 40 | 50,00% | 1,44 | 0,21R | €85,50 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 7 | 111 | 111 | 40,54% | 1,04 | 0,02R | €23,12 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 7 | 178 | 178 | 41,57% | 1,06 | 0,03R | €57,46 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 10 | 239 | 239 | 35,56% | 0,81 | -0,11R | €-258,51 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 154 | 154 | 38,96% | 0,98 | -0,01R | €-13,61 |
| SHADOW_1H_FAST_TP2_V1 | 9 | 226 | 226 | 30,97% | 0,81 | -0,11R | €-258,09 |
| Rapida 1H V2 | 2 | 20 | 18 | 35,00% | 0,78 | -0,14R | €-27,35 |
| Rapida 1H V3 Filtered | 8 | 267 | 267 | 36,70% | 0,89 | -0,06R | €-164,46 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 5 | 182 | 182 | 38,46% | 0,96 | -0,02R | €-35,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 81 | 81 | 46,91% | 1,12 | 0,06R | €52,36 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 81 | 81 | 44,44% | 1,15 | 0,08R | €66,13 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 108 | 108 | 40,74% | 1,00 | 0,00R | €2,90 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 8 | 189 | 189 | 37,04% | 0,90 | -0,06R | €-107,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 8 | 220 | 220 | 34,55% | 0,80 | -0,11R | €-246,42 |
| SHADOW_4H_WIDE | 28 | 100 | 100 | 23,00% | 0,80 | -0,14R | €-142,42 |
| SHADOW_BOLLINGER_MR_1H | 3 | 82 | 82 | 52,44% | 1,42 | 0,19R | €158,50 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 6 | 6 | 33,33% | 0,16 | -0,62R | €-37,17 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 6 | 6 | 83,33% | 5,15 | 0,78R | €47,01 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 8 | 8 | 25,00% | 0,16 | -0,71R | €-57,03 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,48 |
| SHADOW_BTC_EMA_1H | 1 | 7 | 7 | 42,86% | 1,01 | 0,00R | €0,31 |
| SHADOW_BTC_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 11 | 228 | 228 | 36,84% | 1,06 | 0,03R | €77,27 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 5 | 85 | 85 | 34,12% | 0,94 | -0,04R | €-32,63 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 12 | 213 | 213 | 38,03% | 1,00 | -0,00R | €-1,45 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 11 | 169 | 169 | 37,28% | 0,95 | -0,03R | €-44,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 15 | 15 | 26,67% | 0,77 | -0,13R | €-19,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 15 | 15 | 20,00% | 0,70 | -0,17R | €-25,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 3 | 52 | 52 | 30,77% | 0,97 | -0,02R | €-8,03 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 61 | 61 | 26,23% | 0,62 | -0,25R | €-154,67 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 4 | 39 | 39 | 46,15% | 1,15 | 0,08R | €29,60 |
| SHADOW_COMBO_SCANNER | 7 | 122 | 122 | 37,70% | 1,30 | 0,17R | €208,61 |
| SHADOW_COMBO_TREND | 17 | 183 | 183 | 31,15% | 0,93 | -0,04R | €-79,03 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 4 | 4 | 25,00% | 0,41 | -0,50R | €-19,94 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 7 | 7 | 28,57% | 0,67 | -0,26R | €-18,29 |
| SHADOW_DOGE_EMA_1H | 1 | 12 | 12 | 25,00% | 0,55 | -0,29R | €-34,99 |
| SHADOW_DONCHIAN_1H | 11 | 98 | 98 | 25,51% | 0,73 | -0,21R | €-202,25 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 8 | 31 | 31 | 25,81% | 0,51 | -0,37R | €-114,28 |
| SHADOW_EMA_TREND_1H | 18 | 189 | 189 | 30,16% | 0,90 | -0,06R | €-120,96 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 8 | 8 | 25,00% | 0,37 | -0,52R | €-41,87 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 3 | 3 | 66,67% | 2,41 | 0,53R | €16,00 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 6 | 6 | 33,33% | 0,57 | -0,33R | €-19,52 |
| SHADOW_ETH_EMA_1H | 1 | 9 | 9 | 22,22% | 0,32 | -0,59R | €-52,91 |
| SHADOW_ETH_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_GLOBAL_PURE | 1 | 5 | 5 | 60,00% | 2,85 | 0,81R | €40,34 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 7 | 91 | 91 | 30,77% | 0,91 | -0,06R | €-56,98 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 131 | 131 | 54,20% | 1,12 | 0,05R | €68,40 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 82 | 82 | 29,27% | 0,85 | -0,10R | €-80,80 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 78 | 78 | 25,64% | 0,87 | -0,10R | €-74,54 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 60 | 60 | 30,00% | 0,86 | -0,10R | €-59,91 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 88 | 88 | 29,55% | 0,86 | -0,10R | €-83,83 |
| Forza relativa 1H V1 | 18 | 237 | 237 | 28,69% | 0,86 | -0,09R | €-213,72 |
| Forza relativa 1H V2 | 9 | 104 | 98 | 36,54% | 1,17 | 0,09R | €97,93 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 11 | 73 | 73 | 24,66% | 0,44 | -0,37R | €-267,14 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 11 | 73 | 73 | 24,66% | 0,44 | -0,37R | €-267,14 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 11 | 73 | 73 | 24,66% | 0,44 | -0,37R | €-267,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 10 | 109 | 109 | 31,19% | 0,82 | -0,11R | €-115,32 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 10 | 75 | 75 | 49,33% | 0,75 | -0,12R | €-90,81 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 10 | 64 | 64 | 48,44% | 0,72 | -0,14R | €-88,12 |
| SHADOW_SCANNER_TOP10_LONG | 6 | 52 | 52 | 34,62% | 0,97 | -0,02R | €-9,62 |
| SHADOW_SCANNER_TOP15_LONG | 6 | 53 | 53 | 33,96% | 0,94 | -0,04R | €-20,73 |
| SHADOW_SCANNER_TOP20_LONG | 6 | 53 | 53 | 33,96% | 0,94 | -0,04R | €-20,73 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 117 | 117 | 35,90% | 1,27 | 0,15R | €181,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 28 | 28 | 25,00% | 0,73 | -0,17R | €-48,53 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 7 | 73 | 73 | 30,14% | 0,93 | -0,04R | €-30,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 6 | 70 | 70 | 41,43% | 1,29 | 0,14R | €97,61 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 63 | 63 | 34,92% | 1,13 | 0,07R | €47,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 6 | 75 | 75 | 41,33% | 1,27 | 0,13R | €99,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 68 | 68 | 33,82% | 1,09 | 0,05R | €36,26 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 87 | 87 | 39,08% | 1,16 | 0,08R | €71,92 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 69 | 69 | 27,54% | 1,01 | 0,01R | €4,86 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 67 | 67 | 28,36% | 1,04 | 0,03R | €17,52 |
| SHADOW_SCANNER_TOP5_LONG | 6 | 133 | 133 | 37,59% | 1,20 | 0,12R | €153,15 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 12 | 12 | 16,67% | 0,34 | -0,61R | €-72,70 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 5 | 5 | 60,00% | 0,88 | -0,06R | €-2,81 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 7 | 7 | 14,29% | 0,28 | -0,69R | €-48,17 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 10 | 10 | 20,00% | 0,43 | -0,51R | €-50,51 |
| SHADOW_SOL_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,12 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 30 | 30 | 23,33% | 0,58 | -0,25R | €-75,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,12 | 0,08R | €10,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 29 | 29 | 44,83% | 1,58 | 0,23R | €68,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 7 | 7 | 28,57% | 1,23 | 0,10R | €7,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 3 | 16 | 16 | 31,25% | 0,53 | -0,27R | €-43,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 2 | 7 | 7 | 28,57% | 0,70 | -0,14R | €-9,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 29 | 29 | 20,69% | 0,35 | -0,45R | €-129,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 1 | 23 | 23 | 47,83% | 1,60 | 0,23R | €51,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 7 | 7 | 28,57% | 0,91 | -0,04R | €-2,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 1 | 15 | 15 | 33,33% | 0,48 | -0,29R | €-42,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 2 | 5 | 5 | 20,00% | 0,10 | -0,56R | €-28,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,01 | 0,01R | €0,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 15 | 15 | 40,00% | 0,69 | -0,20R | €-29,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,11R | €22,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 1 | 10 | 10 | 50,00% | 0,56 | -0,23R | €-22,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 5 | 5 | 40,00% | 0,68 | -0,21R | €-10,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,01 | 0,01R | €0,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 15 | 15 | 33,33% | 0,75 | -0,14R | €-21,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 1 | 10 | 10 | 40,00% | 0,75 | -0,15R | €-15,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 2 | 5 | 5 | 40,00% | 0,71 | -0,19R | €-9,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,63 | -0,24R | €-11,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,87 | -0,09R | €-8,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 16 | 16 | 31,25% | 0,67 | -0,20R | €-31,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 3 | 3 | 33,33% | 74,50 | 0,65R | €19,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 1 | 13 | 13 | 46,15% | 0,98 | -0,01R | €-1,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 2 | 9 | 9 | 33,33% | 0,67 | -0,23R | €-20,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,31 | -0,44R | €-21,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 11 | 11 | 36,36% | 0,73 | -0,13R | €-14,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 3 | 3 | 33,33% | 18,17 | 0,15R | €4,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 1 | 12 | 12 | 50,00% | 1,07 | 0,03R | €4,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 2 | 7 | 7 | 28,57% | 0,54 | -0,34R | €-24,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 29 | 29 | 34,48% | 1,19 | 0,08R | €22,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 15 | 15 | 0,00% | 0,00 | -0,95R | €-142,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,20 | 0,12R | €12,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 23 | 23 | 34,78% | 1,30 | 0,14R | €32,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 4 | 4 | 0,00% | 0,00 | -0,78R | €-31,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 4 | 18 | 18 | 27,78% | 0,44 | -0,36R | €-64,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 4 | 4 | 0,00% | 0,00 | -0,26R | €-10,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,13 | -0,78R | €-132,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 31 | 31 | 38,71% | 1,23 | 0,11R | €34,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 8 | 8 | 12,50% | 0,63 | -0,15R | €-11,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 4 | 19 | 19 | 36,84% | 0,71 | -0,16R | €-30,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 2 | 13 | 13 | 23,08% | 0,58 | -0,24R | €-31,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,06 | -0,84R | €-143,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 24 | 24 | 41,67% | 1,40 | 0,16R | €38,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 8 | 8 | 12,50% | 0,15 | -0,34R | €-26,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 2 | 18 | 18 | 38,89% | 0,74 | -0,14R | €-24,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 2 | 11 | 11 | 18,18% | 0,38 | -0,41R | €-44,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,63 | -0,24R | €-11,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,17 | 0,11R | €11,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 16 | 16 | 43,75% | 1,38 | 0,18R | €28,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 3 | 3 | 33,33% | 74,50 | 0,65R | €19,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 1 | 13 | 13 | 46,15% | 0,98 | -0,01R | €-1,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 2 | 9 | 9 | 33,33% | 0,67 | -0,23R | €-20,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 0 | 44 | 44 | 31,82% | 0,44 | -0,34R | €-149,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 2 | 11 | 11 | 36,36% | 1,38 | 0,19R | €21,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 36 | 36 | 50,00% | 1,50 | 0,19R | €67,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 1 | 9 | 9 | 44,44% | 1,61 | 0,21R | €19,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 4 | 25 | 25 | 52,00% | 1,02 | 0,01R | €1,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 15 | 15 | 40,00% | 0,83 | -0,09R | €-14,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -1,02R | €-111,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,30 | 0,19R | €13,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 8 | 8 | 37,50% | 1,13 | 0,06R | €4,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 3 | 5 | 5 | 20,00% | 0,12 | -0,39R | €-19,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 41 | 41 | 17,07% | 0,33 | -0,44R | €-178,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 10 | 10 | 30,00% | 0,87 | -0,08R | €-8,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 30 | 30 | 40,00% | 1,32 | 0,15R | €45,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 9 | 9 | 22,22% | 1,22 | 0,08R | €7,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 4 | 19 | 19 | 36,84% | 0,71 | -0,16R | €-30,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 2 | 13 | 13 | 23,08% | 0,58 | -0,24R | €-31,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 41 | 41 | 17,07% | 0,33 | -0,44R | €-178,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 31 | 31 | 38,71% | 1,23 | 0,11R | €34,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 9 | 9 | 22,22% | 1,22 | 0,08R | €7,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 4 | 19 | 19 | 36,84% | 0,71 | -0,16R | €-30,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 2 | 13 | 13 | 23,08% | 0,58 | -0,24R | €-31,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 41 | 41 | 17,07% | 0,27 | -0,49R | €-202,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 1 | 24 | 24 | 41,67% | 1,40 | 0,16R | €38,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 9 | 9 | 22,22% | 0,91 | -0,03R | €-2,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 2 | 18 | 18 | 38,89% | 0,74 | -0,14R | €-24,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 2 | 11 | 11 | 18,18% | 0,38 | -0,41R | €-44,62 |
| MAIN | ALT_ROTATION_DOWN | 5 | 10 | 10 | 30,00% | 1,14 | 0,07R | €7,17 |
| MAIN | ALT_ROTATION_UP | 2 | 13 | 13 | 15,38% | 0,23 | -0,61R | €-79,14 |
| MAIN | RANGE | 8 | 36 | 36 | 27,78% | 0,81 | -0,13R | €-47,89 |
| MAIN | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 10 | 10 | 40,00% | 1,29 | 0,18R | €17,72 |
| MAIN | TREND_DOWN | 2 | 11 | 11 | 27,27% | 0,78 | -0,10R | €-11,10 |
| MAIN | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| MAIN | TREND_UP | 2 | 24 | 24 | 33,33% | 0,96 | -0,02R | €-5,95 |
| MAIN | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,94 | -0,04R | €-2,34 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,44R | €-4,40 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,19 | -0,50R | €-29,72 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 5 | 5 | 20,00% | 0,43 | -0,34R | €-17,24 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 49 | 49 | 22,45% | 0,43 | -0,42R | €-207,22 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 2 | 24 | 24 | 37,50% | 1,17 | 0,11R | €25,99 |
| Bilanciata 1H V1 | RANGE | 1 | 78 | 78 | 43,59% | 1,36 | 0,20R | €154,23 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 6,67% | 0,13 | -0,86R | €-129,29 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 2 | 41 | 41 | 36,59% | 1,15 | 0,09R | €36,50 |
| Bilanciata 1H V1 | TREND_DOWN | 7 | 20 | 20 | 30,00% | 0,80 | -0,11R | €-22,75 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 1 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| Bilanciata 1H V1 | TREND_UP | 3 | 57 | 57 | 33,33% | 1,07 | 0,04R | €24,06 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 4 | 18 | 15 | 33,33% | 0,94 | -0,04R | €-6,69 |
| Bilanciata 1H V2 | RANGE | 1 | 52 | 47 | 42,31% | 1,21 | 0,11R | €59,21 |
| Bilanciata 1H V2 | TRANSITION | 2 | 29 | 26 | 37,93% | 1,46 | 0,24R | €68,75 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 34 | 34 | 29,41% | 0,64 | -0,25R | €-84,46 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 1,05 | 0,03R | €3,82 |
| Bilanciata 1H V3 Filtered | RANGE | 1 | 45 | 45 | 48,89% | 1,58 | 0,29R | €129,41 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,03R | €-41,09 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 2 | 14 | 14 | 35,71% | 1,17 | 0,10R | €14,11 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 6 | 15 | 15 | 26,67% | 0,35 | -0,41R | €-60,82 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 100,00% | ∞ | 0,69R | €6,87 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 27 | 27 | 37,04% | 1,20 | 0,11R | €29,83 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 3 | 23 | 23 | 21,74% | 0,32 | -0,51R | €-117,84 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,46 | 0,23R | €24,82 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 23 | 23 | 47,83% | 1,11 | 0,06R | €13,25 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 2 | 6 | 6 | 33,33% | 1,28 | 0,14R | €8,42 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 6 | 16 | 16 | 25,00% | 0,31 | -0,45R | €-71,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 100,00% | ∞ | 0,69R | €6,87 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 16,67% | 0,02 | -0,52R | €-31,00 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 16,67% | 0,36 | -0,44R | €-26,51 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 0,95 | -0,03R | €-2,21 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 12 | 12 | 50,00% | 1,63 | 0,28R | €33,88 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 1 | 4 | 4 | 100,00% | ∞ | 1,49R | €59,42 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 1 | 9 | 9 | 55,56% | 1,40 | 0,19R | €17,50 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,19 | -0,58R | €-63,30 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 16 | 16 | 37,50% | 0,89 | -0,07R | €-10,55 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 0 | 36 | 36 | 41,67% | 1,04 | 0,02R | €6,53 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 1 | 6 | 6 | 33,33% | 0,95 | -0,02R | €-1,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 4 | 25 | 25 | 40,00% | 0,98 | -0,01R | €-2,87 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 2 | 14 | 14 | 57,14% | 1,93 | 0,36R | €50,63 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 29 | 29 | 17,24% | 0,33 | -0,50R | €-145,52 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 41,18% | 1,04 | 0,02R | €3,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 0 | 66 | 66 | 50,00% | 1,53 | 0,23R | €151,72 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 8 | 8 | 50,00% | 1,90 | 0,35R | €28,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 4 | 25 | 25 | 40,00% | 0,98 | -0,01R | €-2,87 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 2 | 30 | 30 | 40,00% | 0,88 | -0,07R | €-21,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 68 | 68 | 20,59% | 0,36 | -0,46R | €-314,48 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 1 | 16 | 16 | 37,50% | 0,78 | -0,15R | €-23,32 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 0 | 68 | 68 | 45,59% | 1,30 | 0,14R | €95,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,33 | -0,55R | €-27,71 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 14 | 14 | 50,00% | 2,37 | 0,42R | €58,76 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 6 | 30 | 30 | 40,00% | 0,84 | -0,09R | €-27,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 2 | 33 | 33 | 33,33% | 0,70 | -0,19R | €-63,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 39 | 39 | 23,08% | 0,42 | -0,41R | €-161,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 19 | 19 | 36,84% | 0,84 | -0,10R | €-18,58 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 49 | 49 | 53,06% | 1,88 | 0,35R | €169,76 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 8 | 8 | 50,00% | 1,87 | 0,34R | €27,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 3 | 18 | 18 | 27,78% | 0,65 | -0,18R | €-32,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 16 | 16 | 43,75% | 0,93 | -0,04R | €-6,81 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 67 | 67 | 19,40% | 0,39 | -0,43R | €-289,95 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 1 | 18 | 18 | 38,89% | 1,12 | 0,08R | €14,71 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 60 | 60 | 43,33% | 1,41 | 0,21R | €124,68 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,37 | -0,55R | €-32,86 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 14 | 14 | 42,86% | 2,69 | 0,52R | €72,85 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 5 | 25 | 25 | 40,00% | 0,78 | -0,12R | €-31,22 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 3 | 30 | 30 | 20,00% | 0,47 | -0,38R | €-113,77 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,58R | €-11,56 |
| Rapida 1H V2 | ALT_ROTATION_UP | 1 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,77 |
| Rapida 1H V2 | RANGE | 0 | 15 | 13 | 40,00% | 1,05 | 0,03R | €3,85 |
| Rapida 1H V2 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 66 | 66 | 21,21% | 0,38 | -0,43R | €-284,87 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 17 | 17 | 47,06% | 1,16 | 0,09R | €16,04 |
| Rapida 1H V3 Filtered | RANGE | 0 | 64 | 64 | 46,88% | 1,45 | 0,20R | €127,16 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,80 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 16 | 16 | 43,75% | 1,61 | 0,24R | €38,98 |
| Rapida 1H V3 Filtered | TREND_DOWN | 5 | 28 | 28 | 32,14% | 0,70 | -0,17R | €-46,95 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 47 | 47 | 48,94% | 1,33 | 0,17R | €80,21 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 49 | 49 | 24,49% | 0,47 | -0,37R | €-180,93 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 19 | 19 | 36,84% | 0,83 | -0,10R | €-19,93 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 57 | 57 | 50,88% | 1,75 | 0,29R | €162,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 1 | 8 | 8 | 50,00% | 1,87 | 0,34R | €27,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 3 | 22 | 22 | 27,27% | 0,67 | -0,17R | €-37,65 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 21 | 21 | 47,62% | 1,13 | 0,07R | €15,33 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,24 | -0,68R | €-47,32 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 35,71% | 0,73 | -0,18R | €-25,78 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 29 | 29 | 51,72% | 1,35 | 0,17R | €50,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 1 | 3 | 3 | 100,00% | ∞ | 1,49R | €44,60 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 1 | 13 | 13 | 46,15% | 1,06 | 0,03R | €4,52 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 14 | 14 | 50,00% | 1,14 | 0,08R | €10,86 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,24 | -0,68R | €-47,32 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 35,71% | 0,73 | -0,18R | €-25,78 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 29 | 29 | 48,28% | 1,52 | 0,23R | €65,95 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 1 | 3 | 3 | 100,00% | ∞ | 1,49R | €44,60 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 13 | 13 | 38,46% | 1,03 | 0,02R | €2,02 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 1 | 14 | 14 | 50,00% | 1,15 | 0,08R | €11,80 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,13 | -0,76R | €-99,31 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 15 | 15 | 40,00% | 0,85 | -0,09R | €-14,19 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 33 | 33 | 48,48% | 1,51 | 0,23R | €74,88 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,40 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 5 | 5 | 80,00% | 445,80 | 1,19R | €59,31 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 19 | 19 | 42,11% | 1,03 | 0,01R | €2,72 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 18 | 18 | 38,89% | 0,76 | -0,16R | €-28,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 38 | 38 | 18,42% | 0,32 | -0,54R | €-203,31 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 1 | 14 | 14 | 42,86% | 0,98 | -0,01R | €-1,40 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 0 | 64 | 64 | 46,88% | 1,45 | 0,20R | €127,16 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 10 | 10 | 40,00% | 1,89 | 0,28R | €27,91 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 5 | 28 | 28 | 32,14% | 0,70 | -0,17R | €-46,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 32 | 32 | 37,50% | 0,80 | -0,12R | €-39,84 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 65 | 65 | 21,54% | 0,39 | -0,42R | €-273,44 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 1 | 16 | 16 | 37,50% | 0,77 | -0,16R | €-25,08 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 62 | 62 | 46,77% | 1,40 | 0,18R | €112,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,66 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 11 | 11 | 45,45% | 2,32 | 0,38R | €41,74 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 5 | 28 | 28 | 32,14% | 0,70 | -0,17R | €-46,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 30 | 30 | 36,67% | 0,78 | -0,14R | €-42,54 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 4 | 8 | 8 | 25,00% | 1,35 | 0,18R | €14,42 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 7 | 7 | 28,57% | 0,09 | -0,66R | €-46,21 |
| SHADOW_4H_WIDE | RANGE | 9 | 34 | 34 | 23,53% | 0,91 | -0,07R | €-22,80 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 10 | 10 | 20,00% | 0,68 | -0,26R | €-25,64 |
| SHADOW_4H_WIDE | TREND_DOWN | 4 | 9 | 9 | 33,33% | 1,65 | 0,30R | €26,68 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 21 | 21 | 28,57% | 1,17 | 0,11R | €23,91 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,38 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 16 | 16 | 50,00% | 0,92 | -0,04R | €-6,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 0,79 | -0,14R | €-11,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 29 | 29 | 51,72% | 1,53 | 0,22R | €64,78 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 3 | 5 | 5 | 80,00% | 273,20 | 0,88R | €44,11 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 16 | 16 | 56,25% | 1,67 | 0,32R | €50,98 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,21 | -0,66R | €-26,36 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,30 | -0,59R | €-23,62 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 3 | 3 | 66,67% | 2,33 | 0,49R | €14,75 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 2 | 40 | 40 | 27,50% | 0,60 | -0,27R | €-106,83 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 16 | 16 | 31,25% | 0,91 | -0,06R | €-9,25 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 61 | 61 | 47,54% | 1,46 | 0,24R | €144,09 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,47 | -0,44R | €-21,91 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 29 | 29 | 41,38% | 1,47 | 0,26R | €74,58 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 5 | 17 | 17 | 29,41% | 0,66 | -0,19R | €-32,15 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 46 | 46 | 39,13% | 1,39 | 0,19R | €89,19 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,33 | -0,46R | €-41,22 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,13 | 0,08R | €10,99 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 22 | 22 | 54,55% | 1,99 | 0,46R | €101,92 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 2 | 3 | 3 | 66,67% | 298,00 | 1,32R | €39,60 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 2 | 13 | 13 | 30,77% | 0,75 | -0,14R | €-17,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 1 | 17 | 17 | 23,53% | 0,39 | -0,42R | €-72,25 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 2 | 48 | 48 | 31,25% | 0,53 | -0,29R | €-140,73 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 17 | 17 | 29,41% | 0,90 | -0,06R | €-10,36 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 52 | 52 | 50,00% | 1,81 | 0,33R | €173,68 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,47 | -0,44R | €-21,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 12 | 12 | 50,00% | 2,01 | 0,45R | €53,73 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 7 | 24 | 24 | 29,17% | 0,57 | -0,23R | €-54,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 39 | 39 | 46,15% | 1,40 | 0,20R | €79,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 2 | 40 | 40 | 27,50% | 0,63 | -0,25R | €-99,48 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 1 | 14 | 14 | 35,71% | 1,13 | 0,08R | €10,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 49 | 49 | 53,06% | 1,86 | 0,37R | €182,67 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 12 | 12 | 33,33% | 0,98 | -0,01R | €-1,24 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 5 | 17 | 17 | 35,29% | 0,71 | -0,16R | €-26,81 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 1 | 25 | 25 | 32,00% | 0,56 | -0,26R | €-64,87 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 5 | 5 | 20,00% | 0,61 | -0,25R | €-12,40 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 10 | 10 | 30,00% | 0,86 | -0,07R | €-7,30 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 5 | 5 | 20,00% | 0,61 | -0,25R | €-12,40 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 10 | 10 | 20,00% | 0,75 | -0,13R | €-13,45 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 10,00% | 0,05 | -0,61R | €-61,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,22 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 19 | 19 | 52,63% | 2,70 | 0,66R | €124,71 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,53 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 2 | 10 | 10 | 30,00% | 0,56 | -0,27R | €-27,27 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 6 | 6 | 16,67% | 0,63 | -0,20R | €-11,72 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 2 | 18 | 18 | 33,33% | 0,88 | -0,08R | €-14,24 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 1 | 35 | 35 | 25,71% | 0,60 | -0,24R | €-84,56 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,53 | -0,24R | €-21,28 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 19 | 19 | 42,11% | 1,14 | 0,08R | €15,35 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 2 | 2 | 50,00% | 1,32 | 0,18R | €3,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 4 | 4 | 4 | 100,00% | ∞ | 0,80R | €32,07 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 4 | 4 | 50,00% | 1,53 | 0,27R | €10,70 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -0,76R | €-83,34 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,18 | 0,12R | €13,16 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 29 | 29 | 55,17% | 2,31 | 0,61R | €175,49 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 18 | 18 | 50,00% | 1,88 | 0,41R | €74,41 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 3 | 12 | 12 | 25,00% | 0,75 | -0,15R | €-18,23 |
| SHADOW_COMBO_SCANNER | TREND_UP | 3 | 29 | 29 | 37,93% | 1,40 | 0,24R | €68,21 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 1 | 31 | 31 | 25,81% | 0,58 | -0,27R | €-84,20 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 14 | 14 | 28,57% | 0,82 | -0,14R | €-19,09 |
| SHADOW_COMBO_TREND | RANGE | 2 | 48 | 48 | 39,58% | 1,23 | 0,14R | €64,97 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,89 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 24 | 24 | 41,67% | 1,55 | 0,29R | €69,34 |
| SHADOW_COMBO_TREND | TREND_DOWN | 7 | 14 | 14 | 21,43% | 0,65 | -0,21R | €-29,07 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 36 | 36 | 27,78% | 0,98 | -0,01R | €-3,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 18,18% | 0,50 | -0,38R | €-42,23 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,68R | €-34,13 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 6 | 6 | 50,00% | 1,31 | 0,17R | €10,25 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 23 | 23 | 21,74% | 0,53 | -0,39R | €-89,85 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 12,50% | 0,32 | -0,63R | €-50,42 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 25 | 25 | 24,00% | 0,73 | -0,22R | €-53,80 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 10 | 10 | 40,00% | 1,80 | 0,43R | €42,92 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 3 | 7 | 7 | 28,57% | 0,17 | -0,60R | €-42,19 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 15 | 15 | 33,33% | 1,28 | 0,18R | €26,84 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 1,11 | 0,08R | €4,78 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 14 | 14 | 14,29% | 0,23 | -0,71R | €-99,32 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 6 | 6 | 16,67% | 0,13 | -0,75R | €-44,86 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 3 | 3 | 100,00% | ∞ | 2,41R | €72,19 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 2 | 6 | 6 | 33,33% | 0,21 | -0,53R | €-32,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 1 | 32 | 32 | 25,00% | 0,53 | -0,31R | €-99,93 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 14 | 14 | 21,43% | 0,56 | -0,37R | €-51,42 |
| SHADOW_EMA_TREND_1H | RANGE | 3 | 46 | 46 | 41,30% | 1,42 | 0,22R | €103,30 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,50 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 22 | 22 | 36,36% | 1,22 | 0,12R | €27,47 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 8 | 16 | 16 | 25,00% | 0,63 | -0,22R | €-34,73 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 42 | 42 | 26,19% | 0,90 | -0,06R | €-25,26 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,87 | -0,09R | €-9,90 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 2 | 2 | 50,00% | 0,53 | -0,26R | €-5,25 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 0,59 | -0,23R | €-4,66 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,26 | -0,55R | €-16,36 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,91R | €38,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,81 | -0,13R | €-13,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-13,28 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 1 | 25 | 25 | 36,00% | 1,15 | 0,09R | €22,85 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 5 | 5 | 80,00% | 7,76 | 1,37R | €68,47 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 4 | 17 | 17 | 41,18% | 1,49 | 0,27R | €45,22 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 1 | 25 | 25 | 12,00% | 0,28 | -0,63R | €-156,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,39 | -0,42R | €-37,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 12 | 12 | 58,33% | 1,44 | 0,19R | €23,10 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 38 | 38 | 65,79% | 2,12 | 0,36R | €138,55 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 9 | 9 | 88,89% | 6,32 | 0,60R | €53,94 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 2 | 30 | 30 | 63,33% | 1,38 | 0,13R | €39,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 32 | 32 | 31,25% | 0,36 | -0,43R | €-138,30 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,63 | -0,25R | €-22,52 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 1 | 26 | 26 | 42,31% | 1,51 | 0,28R | €73,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 3 | 3 | 66,67% | 3,92 | 0,99R | €29,60 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 3 | 17 | 17 | 35,29% | 1,16 | 0,10R | €16,20 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 25 | 25 | 8,00% | 0,18 | -0,75R | €-186,53 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 4,72 | 1,02R | €40,67 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 12,50% | 0,30 | -0,65R | €-51,96 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 1 | 26 | 26 | 34,62% | 1,46 | 0,29R | €75,19 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 1 | 2 | 2 | 50,00% | 1,91 | 0,46R | €9,23 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 3 | 15 | 15 | 40,00% | 1,44 | 0,24R | €36,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 22 | 22 | 4,55% | 0,15 | -0,79R | €-174,04 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 23 | 23 | 47,83% | 1,78 | 0,41R | €95,28 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 2 | 2 | 2 | 100,00% | ∞ | 1,99R | €39,73 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 2 | 11 | 11 | 27,27% | 0,83 | -0,11R | €-12,26 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 2 | 19 | 19 | 10,53% | 0,23 | -0,69R | €-131,99 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,63 | -0,25R | €-22,52 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,54 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 1 | 26 | 26 | 42,31% | 1,51 | 0,28R | €73,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 3 | 3 | 66,67% | 3,92 | 0,99R | €29,60 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 3 | 16 | 16 | 37,50% | 1,28 | 0,16R | €26,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 1 | 25 | 25 | 8,00% | 0,18 | -0,75R | €-186,35 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 2 | 38 | 38 | 21,05% | 0,43 | -0,39R | €-147,11 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 21 | 21 | 28,57% | 0,82 | -0,14R | €-29,04 |
| Forza relativa 1H V1 | RANGE | 4 | 67 | 67 | 31,34% | 0,97 | -0,02R | €-12,40 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 6 | 6 | 0,00% | 0,00 | -1,02R | €-61,42 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 1 | 24 | 24 | 37,50% | 1,31 | 0,17R | €41,56 |
| Forza relativa 1H V1 | TREND_DOWN | 6 | 19 | 19 | 36,84% | 1,18 | 0,09R | €16,34 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 100,00% | ∞ | 0,63R | €6,33 |
| Forza relativa 1H V1 | TREND_UP | 2 | 51 | 51 | 29,41% | 1,15 | 0,09R | €43,44 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 27,78% | 0,70 | -0,17R | €-30,61 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 10 | 9 | 30,00% | 0,89 | -0,08R | €-8,16 |
| Forza relativa 1H V2 | RANGE | 2 | 25 | 25 | 48,00% | 1,80 | 0,37R | €91,48 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 1 | 17 | 15 | 35,29% | 1,18 | 0,10R | €17,08 |
| Forza relativa 1H V2 | TREND_DOWN | 2 | 11 | 10 | 36,36% | 1,44 | 0,21R | €22,74 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 2 | 17 | 16 | 41,18% | 1,50 | 0,30R | €50,80 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 27 | 27 | 14,81% | 0,17 | -0,66R | €-179,29 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 19 | 19 | 31,58% | 0,46 | -0,35R | €-65,64 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 7 | 7 | 42,86% | 1,39 | 0,23R | €15,86 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 5 | 9 | 9 | 33,33% | 0,59 | -0,25R | €-22,13 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -0,21R | €-10,67 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 27 | 27 | 14,81% | 0,17 | -0,66R | €-179,29 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 19 | 19 | 31,58% | 0,46 | -0,35R | €-65,64 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 7 | 7 | 42,86% | 1,39 | 0,23R | €15,86 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 5 | 9 | 9 | 33,33% | 0,59 | -0,25R | €-22,13 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -0,21R | €-10,67 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 27 | 27 | 14,81% | 0,17 | -0,66R | €-179,29 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 19 | 19 | 31,58% | 0,46 | -0,35R | €-65,64 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 7 | 7 | 42,86% | 1,39 | 0,23R | €15,86 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 5 | 9 | 9 | 33,33% | 0,59 | -0,25R | €-22,13 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -0,21R | €-10,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 23 | 23 | 26,09% | 0,66 | -0,24R | €-54,62 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 33 | 33 | 39,39% | 1,02 | 0,01R | €3,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,31 | 0,16R | €6,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 22 | 22 | 36,36% | 1,06 | 0,04R | €8,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 4 | 8 | 8 | 37,50% | 0,75 | -0,14R | €-11,02 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 12 | 12 | 0,00% | 0,00 | -0,51R | €-61,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 2 | 24 | 24 | 33,33% | 0,31 | -0,48R | €-115,86 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 0 | 16 | 16 | 75,00% | 1,50 | 0,13R | €21,43 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,34 | 0,17R | €6,81 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 7 | 7 | 71,43% | 3,37 | 0,69R | €48,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 7 | 15 | 15 | 33,33% | 0,27 | -0,42R | €-63,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 1 | 6 | 6 | 66,67% | 1,73 | 0,25R | €14,80 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 2 | 21 | 21 | 33,33% | 0,24 | -0,53R | €-111,69 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 0 | 13 | 13 | 76,92% | 1,99 | 0,24R | €31,09 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,31 | 0,16R | €6,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 7 | 7 | 71,43% | 3,17 | 0,63R | €44,02 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 5 | 11 | 11 | 27,27% | 0,41 | -0,35R | €-38,85 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 1 | 5 | 5 | 60,00% | 0,28 | -0,29R | €-14,67 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,65 | -0,21R | €-10,67 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,61 | -0,31R | €-24,75 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 14 | 14 | 64,29% | 2,77 | 0,65R | €91,64 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 2 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 2 | 13 | 13 | 23,08% | 0,73 | -0,17R | €-22,57 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 2 | 8 | 8 | 25,00% | 0,32 | -0,53R | €-42,73 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,65 | -0,21R | €-10,67 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 9 | 9 | 22,22% | 0,52 | -0,40R | €-35,87 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 14 | 14 | 64,29% | 2,77 | 0,65R | €91,64 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 2 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 2 | 13 | 13 | 23,08% | 0,73 | -0,17R | €-22,57 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 2 | 8 | 8 | 25,00% | 0,32 | -0,53R | €-42,73 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,65 | -0,21R | €-10,67 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 9 | 9 | 22,22% | 0,52 | -0,40R | €-35,87 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 14 | 14 | 64,29% | 2,77 | 0,65R | €91,64 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 2 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 2 | 13 | 13 | 23,08% | 0,73 | -0,17R | €-22,57 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 2 | 8 | 8 | 25,00% | 0,32 | -0,53R | €-42,73 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 10 | 10 | 0,00% | 0,00 | -0,72R | €-72,33 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 1,03 | 0,02R | €2,64 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 28 | 28 | 53,57% | 2,47 | 0,65R | €181,90 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 15 | 15 | 46,67% | 1,83 | 0,41R | €60,87 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 3 | 12 | 12 | 25,00% | 0,75 | -0,15R | €-18,23 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 3 | 28 | 28 | 35,71% | 1,28 | 0,17R | €47,50 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,03R | €-0,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,95 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 5 | 5 | 60,00% | 4,55 | 0,73R | €36,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 3 | 11 | 11 | 27,27% | 0,87 | -0,09R | €-9,38 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 0,00% | 0,00 | -0,68R | €-61,65 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,68 | -0,26R | €-20,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 23 | 23 | 52,17% | 2,14 | 0,56R | €128,66 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 4 | 4 | 75,00% | 350,23 | 1,16R | €46,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 3 | 12 | 12 | 25,00% | 0,75 | -0,15R | €-18,23 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 3 | 9 | 9 | 11,11% | 0,29 | -0,59R | €-53,04 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,05 | -0,55R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 1 | 6 | 6 | 33,33% | 1,33 | 0,18R | €10,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 25 | 25 | 48,00% | 2,07 | 0,44R | €110,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 4 | 4 | 100,00% | ∞ | 1,65R | €65,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 2 | 14 | 14 | 50,00% | 1,09 | 0,04R | €5,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 1 | 8 | 8 | 37,50% | 0,89 | -0,07R | €-5,75 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,64R | €-51,51 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 1,02 | 0,01R | €0,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 24 | 24 | 54,17% | 2,23 | 0,58R | €138,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 2 | 4 | 4 | 75,00% | 350,23 | 1,16R | €46,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 2 | 11 | 11 | 27,27% | 0,76 | -0,16R | €-17,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 1 | 6 | 6 | 16,67% | 0,42 | -0,50R | €-29,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 20,00% | 0,24 | -0,47R | €-47,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 1 | 6 | 6 | 33,33% | 1,33 | 0,18R | €10,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 25 | 25 | 48,00% | 2,07 | 0,44R | €110,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 4 | 4 | 100,00% | ∞ | 1,65R | €65,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 2 | 14 | 14 | 50,00% | 1,09 | 0,04R | €5,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 12 | 12 | 33,33% | 0,92 | -0,05R | €-5,85 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 0,00% | 0,00 | -0,69R | €-62,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 1,02 | 0,01R | €0,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 24 | 24 | 54,17% | 2,23 | 0,58R | €138,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 2 | 4 | 4 | 75,00% | 350,23 | 1,16R | €46,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 2 | 11 | 11 | 27,27% | 0,76 | -0,16R | €-17,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 10 | 10 | 20,00% | 0,59 | -0,30R | €-29,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,21 | -0,52R | €-57,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,80 | -0,13R | €-10,44 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 24 | 24 | 50,00% | 2,09 | 0,47R | €111,68 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 4 | 4 | 100,00% | ∞ | 1,65R | €65,86 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 4 | 15 | 15 | 46,67% | 1,08 | 0,03R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 14 | 14 | 35,71% | 1,01 | 0,00R | €0,47 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,40 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 12 | 12 | 25,00% | 0,96 | -0,03R | €-3,50 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 0 | 21 | 21 | 47,62% | 2,38 | 0,67R | €141,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 3 | 3 | 66,67% | 246,23 | 1,09R | €32,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 3 | 12 | 12 | 25,00% | 0,77 | -0,14R | €-16,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 13 | 13 | 7,69% | 0,28 | -0,59R | €-77,12 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 12 | 12 | 25,00% | 1,03 | 0,02R | €2,50 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 20 | 20 | 50,00% | 2,48 | 0,68R | €136,41 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 3 | 3 | 66,67% | 246,23 | 1,09R | €32,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 3 | 11 | 11 | 27,27% | 0,92 | -0,04R | €-4,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 13 | 13 | 7,69% | 0,28 | -0,59R | €-77,12 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,21 | -0,61R | €-73,57 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,82 | -0,13R | €-16,96 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 28 | 28 | 57,14% | 2,48 | 0,60R | €167,59 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,96 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 2 | 15 | 15 | 46,67% | 1,90 | 0,44R | €65,78 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 2 | 13 | 13 | 23,08% | 0,73 | -0,17R | €-22,57 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 39 | 39 | 41,03% | 1,31 | 0,18R | €70,60 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,55 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-01T15:09:10+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **276**
- Scenari virtuali ancora attivi: **4261**
- Gruppi in attesa dell'uscita originale: **35**
- Gruppi con originale chiuso ma Shadow ancora attive: **241**
- Confronti completati: **114793**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_12H | 3172 | 3238 | €-1,19 | 39,5% | 395 | 729 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3172 | 3238 | €-1,51 | 45,8% | 663 | 484 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3172 | 3238 | €-4,69 | 31,7% | 183 | 989 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 3153 | 3219 | +€8,89 | 51,8% | 890 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3153 | 3219 | +€7,25 | 50,9% | 892 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3153 | 3219 | +€4,89 | 48,8% | 989 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3152 | 3218 | +€5,22 | 49,4% | 901 | 63 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3150 | 3216 | +€3,73 | 49,1% | 847 | 129 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3127 | 3193 | +€6,34 | 43,3% | 696 | 88 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3127 | 3193 | +€4,50 | 42,9% | 673 | 123 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3127 | 3193 | +€4,39 | 41,2% | 762 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3126 | 3192 | +€2,95 | 42,2% | 588 | 200 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3123 | 3189 | +€1,20 | 40,2% | 509 | 362 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3114 | 3180 | +€4,85 | 32,9% | 410 | 375 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3113 | 3179 | €-1,63 | 31,5% | 365 | 671 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3110 | 3176 | €-2,19 | 28,7% | 308 | 804 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3095 | 3161 | €-6,72 | 27,0% | 257 | 878 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3088 | 3154 | +€3,68 | 35,6% | 198 | 593 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3005 | 3071 | €-6,91 | 32,7% | 543 | 625 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2977 | 3043 | €-12,54 | 21,6% | 256 | 953 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-01T15:09:24+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **114793**
- Valutazioni prodotte: **18263**
- Candidature al Blocco 5: **5**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_MBV3_GB20_R100 | 170 | 0,242 | 0,149 | 0,159 | 60,0% | 93,6 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 1759 | 0,296 | 0,149 | 0,244 | 56,5% | 89,7 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 1759 | 0,265 | 0,140 | 0,219 | 56,2% | 89,4 | ELIGIBLE_FOR_MUTATION |
| GB20_R050 | 1745 | 0,307 | 0,149 | 0,259 | 55,1% | 88,3 | ELIGIBLE_FOR_MUTATION |
| GB40_R040 | 1758 | 0,228 | 0,124 | 0,180 | 54,6% | 87,9 | VALIDATING |
| GB30_R050 | 1745 | 0,271 | 0,146 | 0,221 | 54,3% | 87,5 | VALIDATING |
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

Generato: 2026-08-01T15:12:20+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 26 | 100,00% | 1,03 | +€11,18 | +€0,43 | 1,52% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 26 | 100,00% | 0,93 | €-21,85 | €-0,84 | 1,50% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 9 | 100,00% | 0,58 | €-111,91 | €-12,43 | 1,12% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 6 | 100,00% | 0,00 | €-104,80 | €-17,47 | 1,05% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 24 | 96,00% | 0,74 | €-126,85 | €-5,29 | 2,13% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-01T15:08:42+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **1**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **196.28 R**
- Profitto virtuale mancato: **312.09 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 8 | 0 | 566.47 |
| DOWN_20 | 8 | 0 | 1132.94 |
| DOWN_30 | 8 | 0 | 1699.41 |
| DOWN_40 | 8 | 4 | 2182.79 |
| UP_10 | 31 | 0 | 1266.84 |
| UP_20 | 31 | 0 | 2533.68 |
| UP_30 | 31 | 0 | 3800.51 |
| UP_40 | 31 | 8 | 4615.78 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-01T15:08:14+00:00

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

Generato: 2026-08-01T15:12:22+00:00

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

Generato: 2026-08-01T15:12:22+00:00

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

Generato: 2026-08-01T15:12:22+00:00

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

Generato: 2026-08-01T15:12:22+00:00

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
| 2 | SHADOW_COMBO_ADAPTIVE | BASELINE | 16.9 | E | 39 | 1.71 | 0.194 | 2.72 |
| 3 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 16.6 | E | 72 | 1.31 | 0.122 | 3.55 |
| 4 | SHADOW_1H_FAST_V3 | BASELINE | 16.5 | E | 103 | 1.13 | 0.054 | 5.36 |
| 5 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 16.4 | E | 33 | 1.66 | 0.244 | 6.54 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 16.2 | E | 36 | 1.52 | 0.195 | 3.32 |
| 7 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 15.9 | E | 75 | 1.22 | 0.086 | 3.78 |
| 8 | SHADOW_DONCHIAN_1H | BASELINE | 15.1 | E | 38 | 1.45 | 0.249 | 8.55 |
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

Generato: 2026-08-01T15:12:22+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **606**
- Strategie preferite nel regime corrente: **7**
- Strategie da evitare nel regime corrente: **4**
- Memorie contestuali: **285**
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
| 10 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | OBSERVING | 72.7 | 23 | 1.79 | 0.351 | 2.24 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-01T15:12:23+00:00

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

Generato: 2026-08-01T15:08:42+00:00

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
