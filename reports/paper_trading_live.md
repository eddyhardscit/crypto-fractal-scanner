# Paper trading automatico KuCoin

Generato: 2026-07-29T05:25:12+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-29T05:23:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-29T05:23:25+00:00 | 2026-07-29T05:23:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-29T05:00:00+00:00 | 2026-07-29T05:00:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-29T04:00:00+00:00 | 2026-07-29T04:00:00+00:00 | 23,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-29T00:00:00+00:00 | 2026-07-29T00:00:00+00:00 | 1,39 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ZEC | 240m | SHORT | -7,70 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | COTI | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -4,84 | 6,00 | 1,16 | STALE_CANDLE | 1,39 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,58 | 6,00 | 3,42 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,39 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 2,16 | 6,00 | 3,84 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 1,94 | 6,00 | 4,06 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,61 | 6,00 | 5,39 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | BANK | 60m | SHORT | -8,25 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | SHORT | -8,25 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | HYPE | 60m | SHORT | -6,73 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | HYPE | 60m | SHORT | -6,73 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| Rapida V1 — score 6–7,5 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| Rapida score 6–7,5 — senza Trend Up | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| Rapida score 6–7,5 — Range Only | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| Rapida score 6–7,5 — Cost Aware | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.689,81 | -3,10% | €-310,19 | €3.000,00 | -10,34% | 6 | 27 | 33,33% | 0,70 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 27 | 964 | CAMPIONE INSUFFICIENTE | 30 (mancano 3) |

- Trade del Principale 4H chiusi: **27**; win rate **33,33%**; profit factor **0,70**.
- Expectancy: **€-11,65** per trade; P&L netto: **€-314,59**; max drawdown: **6,36%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.689,81 | €1.248,21 | €3.744,64 | €144,37 | €5,79 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.583,54 | €2.771,86 | €5.543,73 | €151,77 | €8,45 |
| TEST | Rapida score 6–7,5 — Cost Aware | 1 | €10.506,90 | €211,20 | €633,59 | €51,83 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 2 | €10.493,60 | €413,70 | €1.241,11 | €103,78 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 2 | €10.487,01 | €403,79 | €1.211,37 | €105,23 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.474,03 | €1.856,16 | €5.568,48 | €209,35 | €5,92 |
| TEST | Rapida V3 NoHigh — Regime Guard | 0 | €10.399,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 5 | €10.364,44 | €2.197,27 | €6.591,81 | €106,40 | €16,62 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.355,69 | €70,71 | €141,42 | €2,58 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €10.302,82 | €1.168,08 | €2.336,15 | €55,91 | €23,01 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 2 | €10.301,29 | €346,30 | €1.038,89 | €51,11 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 1 | €10.296,23 | €142,68 | €428,04 | €51,37 | €0,00 |
| TEST | Bilanciata 1H V2 | 2 | €10.279,42 | €173,21 | €519,64 | €49,92 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 3 | €10.262,58 | €1.902,44 | €3.804,89 | €153,05 | €10,43 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.241,64 | €142,81 | €428,44 | €51,41 | €-40,53 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.240,41 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 1 | €10.235,86 | €187,44 | €562,31 | €52,01 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 2 | €10.232,44 | €395,88 | €1.187,64 | €99,47 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.231,65 | €1.389,97 | €4.169,92 | €152,72 | €21,36 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €10.224,31 | €37,16 | €74,32 | €1,36 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 1 | €10.218,59 | €143,01 | €429,04 | €51,48 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 1 | €10.218,03 | €227,32 | €681,96 | €52,06 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 2 | €10.208,22 | €405,03 | €1.215,10 | €101,79 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 1 | €10.185,07 | €185,40 | €556,20 | €51,45 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 2 | €10.145,87 | €206,10 | €618,29 | €52,56 | €0,00 |
| TEST | Combo Adaptive — madre | 4 | €10.114,11 | €1.205,67 | €2.411,33 | €104,15 | €0,32 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 2 | €10.099,98 | €263,10 | €789,31 | €51,07 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.096,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 0 | €10.096,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €10.053,94 | €2.334,73 | €4.669,45 | €151,91 | €10,25 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €10.050,00 | €3.050,20 | €6.100,40 | €199,05 | €-7,89 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 1 | €10.049,44 | €184,02 | €552,07 | €51,07 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 1 | €10.030,78 | €183,89 | €551,67 | €51,03 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.009,58 | €182,35 | €547,06 | €50,60 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 3 | €9.993,85 | €2.293,91 | €4.587,82 | €150,23 | €10,39 |
| TEST | Btc Adaptive 1H | 1 | €9.993,49 | €1.158,94 | €3.476,83 | €50,07 | €-18,69 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €9.990,71 | €1.775,58 | €3.551,16 | €200,37 | €16,22 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 1 | €9.990,65 | €675,44 | €2.026,32 | €49,98 | €-4,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.989,57 | €3.097,46 | €6.194,92 | €146,85 | €-32,38 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.988,39 | €1.388,29 | €2.776,58 | €149,15 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.984,54 | €2.495,25 | €4.990,50 | €104,10 | €-3,96 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 3 | €9.974,12 | €221,90 | €665,70 | €51,17 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.958,93 | €489,81 | €979,63 | €51,01 | €-0,40 |
| TEST | Scanner Bottom15 Short | 5 | €9.958,93 | €489,81 | €979,63 | €51,01 | €-0,40 |
| TEST | Scanner Bottom20 Short | 5 | €9.958,93 | €489,81 | €979,63 | €51,01 | €-0,40 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.952,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 2 | €9.935,21 | €1.397,03 | €2.794,06 | €51,31 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.933,86 | €3.366,63 | €6.733,26 | €100,30 | €-4,81 |
| TEST | Btc Donchian 4H | 1 | €9.925,63 | €1.196,13 | €2.392,26 | €49,75 | €-24,34 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 1 | €9.925,47 | €180,82 | €542,46 | €50,18 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 4 | €9.925,46 | €1.871,48 | €5.614,43 | €149,15 | €-3,94 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.911,85 | €1.148,42 | €3.445,25 | €49,61 | €-8,40 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.892,28 | €1.147,21 | €3.441,62 | €49,56 | €-18,50 |
| TEST | Sol Ema 4H | 1 | €9.889,24 | €780,22 | €1.560,44 | €49,48 | €-5,90 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 0 | €9.870,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.864,70 | €2.278,82 | €4.557,64 | €147,95 | €9,97 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 1 | €9.843,56 | €85,15 | €170,29 | €3,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 2 | €9.838,56 | €327,41 | €982,22 | €49,25 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 1 | €9.837,77 | €70,70 | €141,40 | €2,58 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.832,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 1 | €9.826,60 | €180,15 | €540,44 | €49,99 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 1 | €9.818,04 | €194,51 | €583,53 | €49,25 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 0 | €9.807,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 1 | €9.806,54 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.799,16 | €33,54 | €67,08 | €1,22 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 1 | €9.796,05 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.771,73 | €20,87 | €41,74 | €0,76 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 1 | €9.770,35 | €37,63 | €75,26 | €1,37 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.762,69 | €1.529,14 | €3.058,29 | €48,93 | €-22,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €9.761,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 1 | €9.758,94 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Master Adaptive V1 | 1 | €9.754,92 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.724,36 | €177,16 | €531,47 | €49,16 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 6 | €9.710,32 | €502,07 | €1.004,15 | €102,28 | €0,24 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 2 | €9.698,55 | €2.043,62 | €4.087,25 | €100,09 | €-35,23 |
| TEST | Combo Scanner | 1 | €9.693,06 | €23,89 | €47,78 | €0,87 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.692,09 | €2.124,48 | €4.248,96 | €121,20 | €10,07 |
| TEST | Top 5 + BTC — Guard | 0 | €9.688,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 2 | €9.660,53 | €1.051,34 | €3.154,01 | €98,63 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €9.660,17 | €2.436,58 | €4.873,16 | €103,52 | €32,41 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.639,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.628,98 | €1.549,90 | €3.099,79 | €97,01 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 1 | €9.587,00 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.580,46 | €174,53 | €523,60 | €48,43 | €0,00 |
| TEST | Scanner Top10 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Scanner Top15 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Scanner Top20 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Combo Trend | 5 | €9.499,86 | €2.601,00 | €5.202,01 | €141,66 | €-9,74 |
| TEST | Top 5 + BTC — Guard + MFE | 0 | €9.463,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 1 | €9.450,13 | €172,16 | €516,48 | €47,77 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.408,26 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 1 | €9.333,92 | €883,78 | €1.767,56 | €48,23 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.689,81 | €-314,59 | 27 | 27 | 33,33% | 0,70 | €-11,65 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.583,54 | €577,97 | 36 | 36 | 55,56% | 1,67 | €16,05 | 3,09% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.506,90 | €507,28 | 35 | 35 | 54,29% | 1,94 | €14,49 | 1,96% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.493,60 | €494,34 | 62 | 62 | 48,39% | 1,41 | €7,97 | 2,83% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.487,01 | €487,73 | 73 | 73 | 45,21% | 1,37 | €6,68 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.474,03 | €471,30 | 60 | 60 | 41,67% | 1,37 | €7,85 | 2,49% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.399,89 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.364,44 | €351,55 | 70 | 70 | 47,14% | 1,29 | €5,02 | 3,56% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.355,69 | €355,77 | 49 | 49 | 44,90% | 1,31 | €7,26 | 4,79% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.302,82 | €281,00 | 6 | 6 | 66,67% | 5,76 | €46,83 | 1,61% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.301,29 | €301,92 | 31 | 31 | 51,61% | 2,05 | €9,74 | 2,01% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.296,23 | €296,59 | 11 | 11 | 63,64% | 2,82 | €26,96 | 1,78% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.279,42 | €279,74 | 39 | 37 | 53,85% | 1,36 | €7,17 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.262,58 | €254,67 | 30 | 30 | 56,67% | 1,73 | €8,49 | 1,58% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.241,64 | €282,54 | 10 | 10 | 50,00% | 2,29 | €28,25 | 1,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.240,41 | €241,67 | 15 | 15 | 60,00% | 4,66 | €16,11 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,86 | €236,20 | 19 | 19 | 52,63% | 1,90 | €12,43 | 2,72% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.232,44 | €233,15 | 26 | 26 | 50,00% | 1,70 | €8,97 | 1,76% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.231,65 | €212,50 | 13 | 13 | 46,15% | 1,65 | €16,35 | 2,40% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.224,31 | €224,35 | 40 | 40 | 40,00% | 1,25 | €5,61 | 3,94% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.218,59 | €218,95 | 12 | 12 | 58,33% | 1,75 | €18,25 | 2,28% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.218,03 | €218,44 | 67 | 67 | 44,78% | 1,16 | €3,26 | 3,61% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.208,22 | €208,95 | 31 | 31 | 54,84% | 1,32 | €6,74 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.185,07 | €185,40 | 71 | 71 | 45,07% | 1,14 | €2,61 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,87 | €146,24 | 42 | 42 | 47,62% | 1,20 | €3,48 | 2,91% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.114,11 | €116,12 | 36 | 36 | 44,44% | 1,22 | €3,23 | 2,58% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,98 | €100,46 | 53 | 53 | 56,60% | 1,12 | €1,90 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.096,23 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.096,10 | €96,10 | 59 | 59 | 50,85% | 1,11 | €1,63 | 2,98% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.053,94 | €47,13 | 38 | 38 | 39,47% | 1,07 | €1,24 | 2,31% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.050,00 | €60,65 | 26 | 26 | 53,85% | 1,15 | €2,33 | 2,23% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.049,44 | €49,77 | 22 | 22 | 45,45% | 1,12 | €2,26 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.030,78 | €31,11 | 102 | 102 | 38,24% | 1,02 | €0,31 | 2,94% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,91 | €10,91 | 11 | 11 | 36,36% | 1,23 | €0,99 | 0,25% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.009,58 | €9,91 | 29 | 29 | 37,93% | 1,02 | €0,34 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,18 | €2,18 | 11 | 11 | 36,36% | 1,23 | €0,20 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.993,85 | €-13,15 | 23 | 23 | 34,78% | 0,96 | €-0,57 | 2,48% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.993,49 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Ampia 4H | Confluenza trend | €9.990,71 | €-23,91 | 22 | 22 | 22,73% | 0,96 | €-1,09 | 3,68% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.990,65 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,90% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.989,57 | €26,01 | 14 | 14 | 50,00% | 1,16 | €1,86 | 1,53% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.988,39 | €-9,84 | 15 | 15 | 53,33% | 0,96 | €-0,66 | 1,38% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.984,54 | €-8,51 | 52 | 51 | 40,38% | 0,99 | €-0,16 | 5,53% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.974,12 | €-25,48 | 76 | 76 | 36,84% | 0,98 | €-0,34 | 2,58% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.958,93 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.958,93 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.958,93 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.952,81 | €-47,19 | 11 | 11 | 36,36% | 0,29 | €-4,29 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.935,21 | €-63,10 | 18 | 18 | 27,78% | 0,82 | €-3,51 | 2,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.933,86 | €-56,24 | 41 | 41 | 39,02% | 0,93 | €-1,37 | 5,48% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.925,63 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,25% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.925,47 | €-74,20 | 35 | 35 | 40,00% | 0,90 | €-2,12 | 4,40% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.925,46 | €-66,58 | 18 | 18 | 38,89% | 0,83 | €-3,70 | 1,76% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Sol Ema 1H | Trend following EMA | €9.911,85 | €-77,68 | 6 | 6 | 33,33% | 0,64 | €-12,95 | 1,88% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Btc Ema 1H | Trend following EMA | €9.892,28 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Sol Ema 4H | Trend following EMA | €9.889,24 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,35% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.870,43 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.864,70 | €-141,67 | 21 | 21 | 38,10% | 0,64 | €-6,75 | 2,44% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.843,56 | €-156,34 | 25 | 25 | 32,00% | 0,80 | €-6,25 | 4,68% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.838,56 | €-160,85 | 35 | 35 | 42,86% | 0,76 | €-4,60 | 3,08% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.837,77 | €-162,15 | 29 | 29 | 34,48% | 0,79 | €-5,59 | 4,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.832,55 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,60% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.826,60 | €-173,07 | 76 | 76 | 38,16% | 0,89 | €-2,28 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.818,04 | €-181,61 | 23 | 23 | 43,48% | 0,64 | €-7,90 | 3,23% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.807,66 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,36% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.806,54 | €-191,77 | 21 | 21 | 19,05% | 0,67 | €-9,13 | 3,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.799,16 | €-200,80 | 21 | 21 | 33,33% | 0,74 | €-9,56 | 3,64% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.796,05 | €-202,30 | 16 | 16 | 31,25% | 0,62 | €-12,64 | 2,89% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.771,73 | €-228,24 | 20 | 20 | 30,00% | 0,69 | €-11,41 | 3,98% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.770,35 | €-229,60 | 21 | 21 | 33,33% | 0,64 | €-10,93 | 4,42% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.762,69 | €-213,48 | 12 | 12 | 33,33% | 0,45 | €-17,79 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,49 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.758,94 | €-241,03 | 18 | 18 | 27,78% | 0,66 | €-13,39 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.754,92 | €-245,05 | 18 | 18 | 27,78% | 0,66 | €-13,61 | 4,07% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.724,36 | €-275,32 | 30 | 30 | 33,33% | 0,62 | €-9,18 | 4,83% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.710,32 | €-288,39 | 40 | 40 | 32,50% | 0,71 | €-7,21 | 3,97% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.698,55 | €-263,40 | 17 | 17 | 23,53% | 0,60 | €-15,49 | 4,45% |
| TEST | Combo Scanner | Combo Scanner | €9.693,06 | €-306,92 | 49 | 49 | 36,73% | 0,77 | €-6,26 | 5,08% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.692,09 | €-315,24 | 38 | 38 | 39,47% | 0,56 | €-8,30 | 3,97% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.688,64 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 3,94% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.660,53 | €-337,58 | 18 | 18 | 27,78% | 0,48 | €-18,75 | 4,32% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.660,17 | €-369,44 | 46 | 46 | 28,26% | 0,70 | €-8,03 | 7,55% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.639,39 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.628,98 | €-369,16 | 52 | 52 | 57,69% | 0,60 | €-7,10 | 4,27% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.587,00 | €-411,37 | 33 | 33 | 33,33% | 0,46 | €-12,47 | 5,00% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.580,46 | €-419,23 | 10 | 10 | 0,00% | 0,00 | €-41,92 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Combo Trend | Combo Trend | €9.499,86 | €-486,71 | 57 | 57 | 31,58% | 0,73 | €-8,54 | 7,64% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.463,31 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,43% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.450,13 | €-549,56 | 55 | 55 | 29,09% | 0,62 | €-9,99 | 6,46% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.408,26 | €-590,15 | 26 | 26 | 23,08% | 0,49 | €-22,70 | 6,12% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.333,92 | €-665,02 | 49 | 49 | 28,57% | 0,42 | €-13,57 | 6,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 73,46700 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €-0,10 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,07058 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €-8,18 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 54,56900 | 57,64134 | 73,46073 | 50,62613 | €353,42 | €1.060,27 | €44,83 | €14,07 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63620,87328 | 63962,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.153,42 | €3.460,26 | €49,83 | €-18,60 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 55,31793 | 54,56900 | 55,05561 | 73,48066 | 53,09375 | €867,03 | €2.601,09 | €0,00 | €35,22 |
| Bilanciata 1H V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,34076 | 3,34076 | 2,94410 | 2,24388 | 4,13409 | €15,79 | €47,36 | €5,62 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,38464 | 3,38464 | 2,98212 | 2,27335 | 4,18968 | €136,07 | €408,22 | €48,55 | €0,00 |
| Bilanciata 1H — SHORT Trend Down stretto | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 461,87761 | 462,79000 | 473,26988 | 613,52742 | 439,09306 | €675,44 | €2.026,32 | €49,98 | €-4,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 54,81304 | 54,56900 | 55,99251 | 72,80998 | 52,45408 | €780,21 | €2.340,62 | €50,37 | €10,42 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 461,87761 | 462,79000 | 473,26988 | 613,52742 | 439,09306 | €707,43 | €2.122,30 | €52,35 | €-4,19 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,28834 | 73,46700 | 74,34369 | 97,35134 | 71,17764 | €41,52 | €124,56 | €1,79 | €-0,30 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €191,12 | €573,36 | €53,03 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €186,12 | €558,37 | €51,65 | €0,00 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,34076 | 3,34076 | 3,03225 | 2,24388 | 3,80354 | €187,97 | €563,92 | €52,08 | €0,00 |
| Rapida V1 — senza PEPE | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €185,40 | €556,20 | €51,45 | €0,00 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | NEAR | SHORT | Momentum / breakout | 60m | 3,0x | 1,67599 | 1,67599 | 1,70517 | 2,22628 | 1,61763 | €25,97 | €77,91 | €1,36 | €-0,00 |
| Rapida V1 — target pieno 2R | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €8,60 | €25,80 | €2,39 | €0,00 |
| Rapida 1H V3 Filtered — madre | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €183,89 | €551,67 | €51,03 | €0,00 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €172,16 | €516,48 | €47,77 | €0,00 |
| Rapida V3 — senza ESPORTS | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €180,15 | €540,44 | €49,99 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €180,82 | €542,46 | €50,18 | €0,00 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 54,56900 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €55,19 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,08525 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €-0,53 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63318,66373 | 63962,80000 | 64874,97444 | 94661,40228 | 58960,99415 | €18,28 | €36,56 | €0,90 | €-0,37 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07058 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,27 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00411 | 0,00372 | 0,00361 | 0,00207 | 0,00549 | €199,76 | €399,51 | €47,94 | €-37,79 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 55,31793 | 54,56900 | 55,29611 | 82,70031 | 52,87133 | €1.199,49 | €2.398,97 | €0,00 | €32,48 |
| Forza relativa 1H V1 | BEAT | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 3,34076 | 3,34076 | 2,94410 | 1,68709 | 4,21342 | €200,74 | €401,49 | €47,67 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 461,87761 | 462,79000 | 473,26988 | 690,50702 | 436,81461 | €16,57 | €33,14 | €0,82 | €-0,07 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 461,87761 | 462,79000 | 473,26988 | 690,50702 | 436,81461 | €1.001,44 | €2.002,88 | €49,40 | €-3,96 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63620,87328 | 63962,80000 | 64638,80725 | 95113,20555 | 61076,03835 | €1.401,20 | €2.802,39 | €44,84 | €-15,06 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,56900 | 56,47572 | 82,45966 | 51,86008 | €1.103,00 | €2.206,00 | €52,74 | €23,52 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,56900 | 56,47572 | 82,45966 | 51,86008 | €1.079,15 | €2.158,31 | €51,60 | €23,01 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 55,41391 | 54,56900 | 56,77767 | 82,84380 | 52,41364 | €13,15 | €26,30 | €0,65 | €0,40 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,28834 | 73,46700 | 74,46095 | 109,56607 | 70,70859 | €32,26 | €64,53 | €1,03 | €-0,16 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63294,93848 | 63962,80000 | 64206,38559 | 94625,93303 | 61472,04425 | €1.726,79 | €3.453,57 | €49,73 | €-36,44 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 55,31793 | 54,56900 | 55,05561 | 82,70031 | 53,09375 | €1.175,62 | €2.351,23 | €0,00 | €31,83 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,28834 | 73,46700 | 74,34369 | 109,56607 | 71,17764 | €41,16 | €82,32 | €1,19 | €-0,20 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63364,29461 | 63962,80000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 54,80404 | 54,56900 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,13 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63364,29461 | 63962,80000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 54,80404 | 54,56900 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,13 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63364,29461 | 63962,80000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 54,80404 | 54,56900 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,13 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07008 | 0,07058 | 0,07120 | 0,10476 | 0,06727 | €1.529,14 | €3.058,29 | €48,93 | €-22,00 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,67989 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,00 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,80404 | 54,56900 | 56,08765 | 81,93204 | 51,98009 | €1.015,43 | €2.030,86 | €47,57 | €8,71 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07008 | 0,07058 | 0,07120 | 0,10476 | 0,06761 | €1.282,62 | €2.565,24 | €41,04 | €-18,45 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive — madre | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive — madre | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56900 | 55,95929 | 81,93204 | 52,49353 | €37,18 | €74,35 | €1,57 | €0,32 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive — Quality7 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56900 | 55,99251 | 81,94549 | 52,45408 | €1.166,31 | €2.332,62 | €50,19 | €10,39 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56900 | 55,99251 | 81,94549 | 52,45408 | €1.130,49 | €2.260,99 | €48,65 | €10,07 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56900 | 55,99251 | 81,94549 | 51,27460 | €1.151,04 | €2.302,07 | €49,54 | €10,25 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Combo Adaptive — target pieno 3R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56900 | 55,95929 | 81,93204 | 51,33828 | €1.162,02 | €2.324,05 | €48,99 | €9,97 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 63620,87328 | 63962,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.147,21 | €3.441,62 | €49,56 | €-18,50 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63318,66373 | 63962,80000 | 64635,54187 | 94661,40228 | 59631,40456 | €1.196,13 | €2.392,26 | €49,75 | €-24,34 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63620,87328 | 63962,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.158,94 | €3.476,83 | €50,07 | €-18,69 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,28834 | 73,46700 | 74,34369 | 97,35134 | 71,17764 | €1.148,42 | €3.445,25 | €49,61 | €-8,40 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 73,46700 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-5,90 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €0,00 |
| Combo Adaptive — Side × Regime Guard | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56900 | 55,95929 | 81,93204 | 52,49353 | €1.215,65 | €2.431,30 | €51,25 | €10,43 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00372 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €-35,23 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,07058 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €-8,67 |
| MAIN — Side × Regime Guard | ZEC | SHORT | Confluenza trend | 240m | 3,0x | 469,12616 | 462,79000 | 492,16341 | 623,15591 | 423,05164 | €346,80 | €1.040,39 | €51,09 | €14,05 |
| MAIN — Side × Regime Guard | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 54,56900 | 57,64134 | 73,46073 | 50,62613 | €401,28 | €1.203,85 | €50,90 | €15,98 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00411 | 0,00372 | 0,00361 | 0,00276 | 0,00509 | €142,81 | €428,44 | €51,41 | €-40,53 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTC | SHORT | Combo Trend | 60m | 2,0x | 63620,87328 | 63962,80000 | 64638,80725 | 95113,20555 | 61381,41854 | €1.578,90 | €3.157,81 | €50,52 | €-16,97 |
| Combo Trend — Side × Regime Guard | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,80404 | 54,56900 | 56,08765 | 81,93204 | 51,98009 | €1.059,16 | €2.118,31 | €49,61 | €9,08 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,34076 | 3,34076 | 3,03225 | 2,24388 | 3,80354 | €183,30 | €549,89 | €50,78 | €0,00 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 461,87761 | 462,79000 | 473,26988 | 613,52742 | 439,09306 | €664,50 | €1.993,49 | €49,17 | €-3,94 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63294,93848 | 63962,80000 | 64206,38559 | 94625,93303 | 61472,04425 | €1.647,88 | €3.295,77 | €47,46 | €-34,78 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €59,89 | €119,78 | €0,00 | €2,39 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €15,45 | €30,90 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,16732 | €187,44 | €562,31 | €52,01 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €15,38 | €46,14 | €4,27 | €0,00 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,16732 | €184,02 | €552,07 | €51,07 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | NEAR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,66900 | 1,66900 | 1,69806 | 2,21699 | 1,61088 | €52,00 | €156,00 | €2,72 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €177,16 | €531,47 | €49,16 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €182,35 | €547,06 | €50,60 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,16732 | €174,53 | €523,60 | €48,43 | €0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend — Side × Regime Guard | ZEC | SHORT | 2026-07-29T05:23:38+00:00 | 461,79570 | €2,02 | 0,95 | STOP |
| Combo Trend | ZEC | SHORT | 2026-07-29T05:23:38+00:00 | 461,94196 | €28,82 | 0,61 | STOP |
| Benchmark trend following EMA 1H | ZEC | SHORT | 2026-07-29T05:23:38+00:00 | 461,94196 | €26,77 | 0,61 | STOP |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €1,91 | 0,73 | STOP |
| Scanner Bottom20 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Scanner Bottom15 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Scanner Bottom10 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Combo Adaptive — target pieno 3R | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €38,41 | 0,78 | STOP |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €39,96 | 0,78 | STOP |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €37,16 | 0,78 | STOP |
| Combo Adaptive — parziale 1R | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,63101 | €46,70 | 0,97 | STOP |
| Combo Adaptive — madre | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €39,06 | 0,78 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 48/30 | 31/30 | 0,68 | 2,05 | -0,21R | €9,74 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 28/30 | 19/30 | 0,39 | 1,90 | -0,45R | €12,43 | 2,72% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 18/30 | 22/30 | 0,69 | 1,74 | -0,24R | €12,35 | 1,72% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 18/30 | 22/30 | 0,69 | 1,57 | -0,24R | €8,43 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 29/30 | 30/30 | 0,50 | 0,62 | -0,40R | €-9,18 | 4,83% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 12/30 | 10/30 | 0,24 | 0,00 | -0,67R | €-41,92 | 4,20% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 6/30 | 7/30 | 1,28 | 1,03 | 0,14R | €0,61 | 2,15% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 20/30 | 15/30 | 1,00 | 4,66 | 0,00R | €16,11 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 31/30 | 23/30 | 0,70 | 0,64 | -0,21R | €-7,90 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 11/30 | 7/30 | 0,30 | 0,02 | -0,53R | €-33,97 | 2,82% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 29/30 | 29/30 | 0,73 | 1,02 | -0,20R | €0,34 | 4,84% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 60/30 | 53/30 | 0,74 | 1,12 | -0,16R | €1,90 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 13/30 | 15/30 | 0,87 | 0,99 | -0,09R | €-0,32 | 2,70% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 56/30 | 42/30 | 0,59 | 1,20 | -0,27R | €3,48 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 59/30 | 35/30 | 0,61 | 0,76 | -0,25R | €-4,60 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 38/30 | 22/30 | 0,43 | 1,12 | -0,37R | €2,26 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 80/30 | 27/30 | 1,00 | 0,70 | -0,00R | €-11,65 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 10/30 | 0,00 | 2,29 | 0,00R | €28,25 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 13/30 | 0,00 | 1,65 | 0,00R | €16,35 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 12/30 | 7/30 | 0,24 | 0,12 | -0,63R | €-6,34 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 14/30 | 11/30 | 0,43 | 0,29 | -0,34R | €-4,29 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 225/30 | 70/30 | 1,01 | 1,29 | 0,00R | €5,02 | 3,56% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 18/30 | 0,00 | 0,48 | 0,00R | €-18,75 | 4,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,90% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 57/30 | 37/30 | 1,47 | 1,36 | 0,26R | €7,17 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 111/30 | 60/30 | 1,01 | 1,37 | 0,01R | €7,85 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 34/30 | 18/30 | 0,47 | 0,83 | -0,41R | €-3,70 | 1,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 28/30 | 25/30 | 1,46 | 0,99 | 0,23R | €-0,14 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 32/30 | 26/30 | 1,45 | 1,70 | 0,21R | €8,97 | 1,76% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 99/30 | 62/30 | 1,19 | 1,41 | 0,10R | €7,97 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 144/30 | 71/30 | 0,88 | 1,14 | -0,07R | €2,61 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 35/30 | 0,00 | 1,94 | 0,00R | €14,49 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 31/30 | 0,00 | 1,32 | 0,00R | €6,74 | 2,77% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 12/30 | 0,00 | 1,75 | 0,00R | €18,25 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 96/30 | 73/30 | 0,94 | 1,37 | -0,03R | €6,68 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 139/30 | 76/30 | 0,88 | 0,98 | -0,07R | €-0,34 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 15/30 | 15/30 | 0,62 | 0,93 | -0,26R | €-1,52 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 180/30 | 102/30 | 0,92 | 1,02 | -0,04R | €0,31 | 2,94% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 113/30 | 67/30 | 0,90 | 1,16 | -0,06R | €3,26 | 3,61% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 48/30 | 49/30 | 1,06 | 0,93 | 0,04R | €-1,56 | 3,21% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 48/30 | 44/30 | 1,06 | 0,86 | 0,04R | €-3,24 | 2,86% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 68/30 | 55/30 | 0,87 | 0,62 | -0,08R | €-9,99 | 6,46% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 11/30 | 0,00 | 2,82 | 0,00R | €26,96 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 20/30 | 0,00 | 3,42 | 0,00R | €19,99 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 105/30 | 62/30 | 0,98 | 0,90 | -0,01R | €-2,09 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 35/30 | 0,00 | 0,90 | 0,00R | €-2,12 | 4,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 59/30 | 0,00 | 1,11 | 0,00R | €1,63 | 2,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 20/30 | 0,00 | 1,17 | 0,00R | €3,80 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 134/30 | 76/30 | 0,80 | 0,89 | -0,12R | €-2,28 | 2,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 68/30 | 22/30 | 0,85 | 0,96 | -0,11R | €-1,09 | 3,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 69/30 | 50/30 | 1,22 | 0,82 | 0,12R | €-4,77 | 5,70% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 5/30 | 3/30 | 0,01 | 1,24 | -0,88R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 5/30 | 4/30 | 3,94 | 2,94 | 0,67R | €27,74 | 0,70% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 7/30 | 5/30 | 0,01 | 0,97 | -0,96R | €-0,63 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,25% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 6/30 | 6/30 | 0,85 | 0,59 | -0,11R | €-14,69 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 165/30 | 36/30 | 1,13 | 1,22 | 0,08R | €3,23 | 2,58% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 57/30 | 18/30 | 0,88 | 0,82 | -0,08R | €-3,51 | 2,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 135/30 | 49/30 | 1,07 | 0,42 | 0,04R | €-13,57 | 6,69% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 106/30 | 38/30 | 0,98 | 0,56 | -0,01R | €-8,30 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 11/30 | 11/30 | 0,80 | 0,71 | -0,14R | €-7,09 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 11/30 | 11/30 | 0,80 | 0,31 | -0,14R | €-18,43 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 31/30 | 23/30 | 1,31 | 0,96 | 0,17R | €-0,57 | 2,48% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 43/30 | 22/30 | 0,59 | 0,79 | -0,32R | €-4,40 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 45/30 | 38/30 | 0,74 | 1,07 | -0,20R | €1,24 | 2,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 30/30 | 0,00 | 1,73 | 0,00R | €8,49 | 1,58% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 45/30 | 21/30 | 0,74 | 0,64 | -0,20R | €-6,75 | 2,44% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 27/30 | 20/30 | 0,95 | 0,76 | -0,03R | €-8,37 | 3,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 93/30 | 49/30 | 1,36 | 0,77 | 0,21R | €-6,26 | 5,08% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 127/30 | 57/30 | 1,05 | 0,73 | 0,03R | €-8,54 | 7,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 26/30 | 0,00 | 1,15 | 0,00R | €2,33 | 2,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 4/30 | 4/30 | 0,41 | 0,41 | -0,50R | €-24,49 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 5/30 | 6/30 | 1,12 | 1,34 | 0,08R | €6,42 | 1,08% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 8/30 | 10/30 | 0,84 | 1,57 | -0,09R | €9,62 | 1,36% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 80/30 | 36/30 | 0,83 | 1,67 | -0,13R | €16,05 | 3,09% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 11/30 | 6/30 | 0,86 | 5,76 | -0,11R | €46,83 | 1,61% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 133/30 | 40/30 | 0,99 | 0,71 | -0,00R | €-7,21 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 6/30 | 6/30 | 0,34 | 0,08 | -0,61R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 2/30 | 2/30 | 1,21 | 0,28 | 0,12R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 5/30 | 5/30 | 0,42 | 0,42 | -0,52R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 6/30 | 8/30 | 0,34 | 0,16 | -0,61R | €-34,02 | 2,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-52,87 | 1,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 12/30 | 1,75 | 0,45 | 0,41R | €-17,79 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 51/30 | 21/30 | 0,85 | 0,74 | -0,10R | €-9,56 | 3,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 21/30 | 0,00 | 0,67 | 0,00R | €-9,13 | 3,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 17/30 | 0,00 | 0,60 | 0,00R | €-15,49 | 4,45% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 16/30 | 0,00 | 0,62 | 0,00R | €-12,64 | 2,89% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 51/30 | 52/30 | 0,77 | 0,60 | -0,16R | €-7,10 | 4,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 46/30 | 18/30 | 0,81 | 0,66 | -0,13R | €-13,39 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 41/30 | 20/30 | 0,75 | 0,69 | -0,19R | €-11,41 | 3,98% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 39/30 | 26/30 | 0,87 | 0,49 | -0,09R | €-22,70 | 6,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 51/30 | 18/30 | 0,77 | 0,66 | -0,16R | €-13,61 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 167/30 | 46/30 | 0,91 | 0,70 | -0,06R | €-8,03 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 65/30 | 51/30 | 1,34 | 0,99 | 0,20R | €-0,16 | 5,53% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 32/30 | 20/30 | 0,57 | 0,91 | -0,30R | €-1,97 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 32/30 | 20/30 | 0,57 | 0,91 | -0,30R | €-1,97 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 32/30 | 20/30 | 0,57 | 0,91 | -0,30R | €-1,97 | 2,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 72/30 | 41/30 | 0,99 | 0,93 | -0,01R | €-1,37 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 26/30 | 15/30 | 1,26 | 0,96 | 0,12R | €-0,66 | 1,38% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 24/30 | 14/30 | 1,14 | 1,16 | 0,07R | €1,86 | 1,53% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 24/30 | 20/30 | 1,02 | 0,34 | 0,01R | €-22,84 | 6,28% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 25/30 | 20/30 | 0,95 | 0,34 | -0,03R | €-22,84 | 6,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 25/30 | 20/30 | 0,95 | 0,34 | -0,03R | €-22,84 | 6,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 91/30 | 40/30 | 1,34 | 1,25 | 0,20R | €5,61 | 3,94% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 23/30 | 10/30 | 0,68 | 0,87 | -0,22R | €-3,13 | 2,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 47/30 | 21/30 | 0,90 | 0,64 | -0,06R | €-10,93 | 4,42% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 39/30 | 34/30 | 1,11 | 0,61 | 0,07R | €-10,61 | 3,93% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 38/30 | 19/30 | 1,10 | 0,70 | 0,07R | €-10,12 | 4,36% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 44/30 | 41/30 | 1,11 | 0,53 | 0,07R | €-13,09 | 5,43% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 43/30 | 24/30 | 1,05 | 0,59 | 0,03R | €-12,97 | 3,94% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 54/30 | 33/30 | 1,01 | 0,46 | 0,01R | €-12,47 | 5,00% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 40/30 | 29/30 | 1,05 | 0,79 | 0,03R | €-5,59 | 4,99% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 40/30 | 25/30 | 1,05 | 0,80 | 0,03R | €-6,25 | 4,68% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 105/30 | 49/30 | 1,27 | 1,31 | 0,16R | €7,26 | 4,79% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 8/30 | 7/30 | 0,57 | 0,24 | -0,36R | €-31,26 | 2,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 2/30 | 0,00 | 0,65 | -1,05R | €-8,96 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 5/30 | 5/30 | 0,88 | 0,82 | -0,06R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 6/30 | 4/30 | 0,34 | 26,39 | -0,62R | €28,48 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 2/30 | 0,00 | 0,71 | -1,06R | €-7,50 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 7/30 | 6/30 | 0,68 | 0,64 | -0,25R | €-12,95 | 1,88% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-51,84 | 1,35% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07058**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 25.2 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63962.8 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07067**; close **0.07065**; wick alta **14.3%**; volume **x1.08**

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
- Confidenza: **90,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -3.32%, 55% sotto -1%.
- BTC trend score: **-1,00**; ADX: **26,56**; breadth sopra EMA50: **25,00%**
- Mediana alt vs BTC: **-3,32%**; dispersione: **13,56%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **9**
- Posizioni research aperte: **438**
- Trade research chiusi: **5204**
- Eventi di mercato indipendenti chiusi: **1090**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **21059**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 7 | 48 | 48 | 25,00% | 0,68 | -0,21R | €-100,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 6 | 28 | 28 | 17,86% | 0,39 | -0,45R | €-127,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 1 | 18 | 18 | 27,78% | 0,69 | -0,24R | €-42,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 1 | 18 | 18 | 27,78% | 0,69 | -0,24R | €-42,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 2 | 29 | 29 | 20,69% | 0,50 | -0,40R | €-117,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 2 | 12 | 12 | 8,33% | 0,24 | -0,67R | €-80,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 1 | 6 | 6 | 33,33% | 1,28 | 0,14R | €8,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 3 | 20 | 20 | 30,00% | 1,00 | 0,00R | €0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 5 | 31 | 31 | 25,81% | 0,70 | -0,21R | €-65,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 4 | 11 | 11 | 9,09% | 0,30 | -0,53R | €-58,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 2 | 29 | 29 | 27,59% | 0,73 | -0,20R | €-57,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 7 | 60 | 60 | 36,67% | 0,74 | -0,16R | €-94,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 2 | 13 | 13 | 30,77% | 0,87 | -0,09R | €-11,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 8 | 56 | 56 | 23,21% | 0,59 | -0,27R | €-148,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 9 | 59 | 59 | 23,73% | 0,61 | -0,25R | €-149,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 7 | 38 | 38 | 18,42% | 0,43 | -0,37R | €-140,66 |
| MAIN | 19 | 80 | 80 | 33,75% | 1,00 | -0,00R | €-0,33 |
| RSI_EXTREME_LONG_15M | 0 | 12 | 12 | 25,00% | 0,24 | -0,63R | €-75,99 |
| RSI_EXTREME_SHORT_15M | 0 | 14 | 14 | 35,71% | 0,43 | -0,34R | €-47,04 |
| Bilanciata 1H V1 | 14 | 225 | 225 | 34,22% | 1,01 | 0,00R | €10,61 |
| Bilanciata 1H V2 | 5 | 64 | 57 | 43,75% | 1,47 | 0,26R | €169,36 |
| Bilanciata 1H V3 Filtered | 13 | 111 | 111 | 34,23% | 1,01 | 0,01R | €6,84 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 11 | 34 | 34 | 20,59% | 0,47 | -0,41R | €-140,11 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 28 | 28 | 50,00% | 1,46 | 0,23R | €64,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 6 | 32 | 32 | 50,00% | 1,45 | 0,21R | €67,37 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 6 | 99 | 99 | 45,45% | 1,19 | 0,10R | €101,71 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 7 | 144 | 144 | 38,19% | 0,88 | -0,07R | €-101,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 96 | 96 | 39,58% | 0,94 | -0,03R | €-32,38 |
| SHADOW_1H_FAST_TP2_V1 | 8 | 139 | 139 | 32,37% | 0,88 | -0,07R | €-103,49 |
| Rapida 1H V2 | 0 | 17 | 15 | 29,41% | 0,62 | -0,26R | €-43,50 |
| Rapida 1H V3 Filtered | 8 | 180 | 180 | 38,33% | 0,92 | -0,04R | €-80,42 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 8 | 113 | 113 | 38,05% | 0,90 | -0,06R | €-70,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 1 | 48 | 48 | 43,75% | 1,06 | 0,04R | €18,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 1 | 48 | 48 | 43,75% | 1,06 | 0,04R | €18,29 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 68 | 68 | 38,24% | 0,87 | -0,08R | €-55,56 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 5 | 105 | 105 | 40,00% | 0,98 | -0,01R | €-9,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 7 | 134 | 134 | 35,07% | 0,80 | -0,12R | €-162,51 |
| SHADOW_4H_WIDE | 25 | 68 | 68 | 23,53% | 0,85 | -0,11R | €-76,07 |
| SHADOW_BOLLINGER_MR_1H | 1 | 69 | 69 | 49,28% | 1,22 | 0,12R | €80,08 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 5 | 5 | 20,00% | 0,01 | -0,88R | €-44,14 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 5 | 5 | 80,00% | 3,94 | 0,67R | €33,34 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 7 | 7 | 14,29% | 0,01 | -0,96R | €-67,16 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 0 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,67 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 11 | 165 | 165 | 36,97% | 1,13 | 0,08R | €130,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 1 | 57 | 57 | 29,82% | 0,88 | -0,08R | €-43,76 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 12 | 135 | 135 | 37,04% | 1,07 | 0,04R | €59,23 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 11 | 106 | 106 | 33,96% | 0,98 | -0,01R | €-15,79 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 11 | 11 | 27,27% | 0,80 | -0,14R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 11 | 11 | 27,27% | 0,80 | -0,14R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 3 | 31 | 31 | 38,71% | 1,31 | 0,17R | €52,69 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 0 | 43 | 43 | 23,26% | 0,59 | -0,32R | €-137,20 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 2 | 45 | 45 | 20,00% | 0,74 | -0,20R | €-91,17 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 2 | 45 | 45 | 20,00% | 0,74 | -0,20R | €-91,17 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 27 | 27 | 40,74% | 0,95 | -0,03R | €-8,21 |
| SHADOW_COMBO_SCANNER | 2 | 93 | 93 | 37,63% | 1,36 | 0,21R | €194,14 |
| SHADOW_COMBO_TREND | 17 | 127 | 127 | 33,07% | 1,05 | 0,03R | €39,85 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 4 | 4 | 25,00% | 0,41 | -0,50R | €-19,94 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 5 | 5 | 40,00% | 1,12 | 0,08R | €4,06 |
| SHADOW_DOGE_EMA_1H | 0 | 8 | 8 | 25,00% | 0,84 | -0,09R | €-7,42 |
| SHADOW_DONCHIAN_1H | 6 | 80 | 80 | 26,25% | 0,83 | -0,13R | €-104,13 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 4 | 11 | 11 | 27,27% | 0,86 | -0,11R | €-12,04 |
| SHADOW_EMA_TREND_1H | 16 | 133 | 133 | 31,58% | 0,99 | -0,00R | €-4,47 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,67 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 5 | 5 | 20,00% | 0,42 | -0,52R | €-26,11 |
| SHADOW_ETH_EMA_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,55 |
| SHADOW_ETH_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_GLOBAL_PURE | 1 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 4 | 51 | 51 | 29,41% | 0,85 | -0,10R | €-52,79 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 3 | 51 | 51 | 27,45% | 0,77 | -0,16R | €-82,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 3 | 46 | 46 | 28,26% | 0,81 | -0,13R | €-59,10 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 4 | 41 | 41 | 19,51% | 0,75 | -0,19R | €-78,73 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 1 | 39 | 39 | 30,77% | 0,87 | -0,09R | €-34,83 |
| SHADOW_MASTER_ADAPTIVE_V1 | 3 | 51 | 51 | 27,45% | 0,77 | -0,16R | €-82,00 |
| Forza relativa 1H V1 | 19 | 167 | 167 | 29,34% | 0,91 | -0,06R | €-106,22 |
| Forza relativa 1H V2 | 7 | 70 | 65 | 38,57% | 1,34 | 0,20R | €138,59 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 11 | 32 | 32 | 25,00% | 0,57 | -0,30R | €-97,09 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 11 | 32 | 32 | 25,00% | 0,57 | -0,30R | €-97,09 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 11 | 32 | 32 | 25,00% | 0,57 | -0,30R | €-97,09 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 11 | 72 | 72 | 33,33% | 0,99 | -0,01R | €-4,79 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 11 | 26 | 26 | 57,69% | 1,26 | 0,12R | €30,43 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 11 | 24 | 24 | 54,17% | 1,14 | 0,07R | €16,08 |
| SHADOW_SCANNER_TOP10_LONG | 1 | 24 | 24 | 33,33% | 1,02 | 0,01R | €2,49 |
| SHADOW_SCANNER_TOP15_LONG | 1 | 25 | 25 | 32,00% | 0,95 | -0,03R | €-8,62 |
| SHADOW_SCANNER_TOP20_LONG | 1 | 25 | 25 | 32,00% | 0,95 | -0,03R | €-8,62 |
| SHADOW_SCANNER_TOP5_BTC | 1 | 91 | 91 | 36,26% | 1,34 | 0,20R | €181,22 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 23 | 23 | 21,74% | 0,68 | -0,22R | €-51,58 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 1 | 47 | 47 | 27,66% | 0,90 | -0,06R | €-30,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 0 | 39 | 39 | 33,33% | 1,11 | 0,07R | €27,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 0 | 38 | 38 | 31,58% | 1,10 | 0,07R | €24,81 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 0 | 44 | 44 | 34,09% | 1,11 | 0,07R | €29,02 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 0 | 43 | 43 | 30,23% | 1,05 | 0,03R | €14,03 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 1 | 54 | 54 | 31,48% | 1,01 | 0,01R | €4,51 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 4 | 40 | 40 | 25,00% | 1,05 | 0,03R | €13,35 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 4 | 40 | 40 | 25,00% | 1,05 | 0,03R | €13,35 |
| SHADOW_SCANNER_TOP5_LONG | 1 | 105 | 105 | 38,10% | 1,27 | 0,16R | €165,26 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 8 | 8 | 25,00% | 0,57 | -0,36R | €-28,58 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 5 | 5 | 60,00% | 0,88 | -0,06R | €-2,81 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,62R | €-37,09 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,47 |
| SHADOW_SOL_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,12 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 5 | 22 | 22 | 22,73% | 0,59 | -0,25R | €-54,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 1,27 | 0,17R | €20,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 5 | 5 | 20,00% | 0,63 | -0,23R | €-11,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 5 | 21 | 21 | 19,05% | 0,36 | -0,47R | €-98,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,38R | €23,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,16 | 0,11R | €10,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,16 | 0,11R | €10,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -0,79R | €-31,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -0,79R | €-31,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 1 | 4 | 4 | 25,00% | 0,96 | -0,02R | €-0,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 3 | 4 | 4 | 0,00% | 0,00 | -0,78R | €-31,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,42 | 0,23R | €22,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 4 | 4 | 4 | 0,00% | 0,00 | -0,78R | €-31,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 4 | 4 | 4 | 0,00% | 0,00 | -0,78R | €-31,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -0,79R | €-31,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 9 | 9 | 44,44% | 1,39 | 0,24R | €21,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 5 | 5 | 60,00% | 2,86 | 0,76R | €38,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 6 | 29 | 29 | 41,38% | 0,62 | -0,20R | €-58,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,38 | 0,21R | €21,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 6 | 6 | 50,00% | 1,91 | 0,47R | €28,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,17R | €1,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,30 | 0,19R | €13,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 6 | 26 | 26 | 19,23% | 0,43 | -0,31R | €-81,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 6 | 26 | 26 | 19,23% | 0,43 | -0,31R | €-81,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 6 | 26 | 26 | 19,23% | 0,38 | -0,37R | €-95,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,38R | €23,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| MAIN | ALT_ROTATION_DOWN | 6 | 7 | 7 | 28,57% | 0,97 | -0,02R | €-1,41 |
| MAIN | ALT_ROTATION_UP | 2 | 10 | 10 | 10,00% | 0,22 | -0,72R | €-72,20 |
| MAIN | RANGE | 7 | 26 | 26 | 34,62% | 1,02 | 0,01R | €3,46 |
| MAIN | RANGE_HIGH_VOL | 2 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| MAIN | TREND_UP | 1 | 19 | 19 | 36,84% | 1,12 | 0,08R | €14,71 |
| MAIN | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,94 | -0,04R | €-2,34 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,05 | -0,86R | €-34,43 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 5 | 5 | 20,00% | 0,43 | -0,34R | €-17,24 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 6 | 35 | 35 | 25,71% | 0,63 | -0,24R | €-85,32 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 1 | 21 | 21 | 38,10% | 1,12 | 0,08R | €16,39 |
| Bilanciata 1H V1 | RANGE | 2 | 54 | 54 | 42,59% | 1,41 | 0,24R | €130,11 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 6,67% | 0,13 | -0,86R | €-129,29 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 0 | 33 | 33 | 39,39% | 1,29 | 0,17R | €56,83 |
| Bilanciata 1H V1 | TREND_DOWN | 3 | 4 | 4 | 50,00% | 1,24 | 0,13R | €5,04 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| Bilanciata 1H V1 | TREND_UP | 0 | 48 | 48 | 37,50% | 1,23 | 0,14R | €66,63 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 2 | 11 | 9 | 36,36% | 1,04 | 0,02R | €2,70 |
| Bilanciata 1H V2 | RANGE | 3 | 32 | 30 | 43,75% | 1,41 | 0,23R | €74,30 |
| Bilanciata 1H V2 | TRANSITION | 0 | 21 | 18 | 47,62% | 1,88 | 0,44R | €92,35 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 28 | 28 | 28,57% | 0,75 | -0,17R | €-48,10 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 2 | 8 | 8 | 25,00% | 0,61 | -0,32R | €-25,49 |
| Bilanciata 1H V3 Filtered | RANGE | 2 | 23 | 23 | 52,17% | 2,00 | 0,51R | €116,91 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,03R | €-41,09 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 9 | 9 | 44,44% | 1,46 | 0,28R | €24,77 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 3 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 23 | 23 | 39,13% | 1,30 | 0,17R | €40,12 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 17 | 17 | 17,65% | 0,37 | -0,48R | €-81,48 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,50 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 0 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,91R | €19,09 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 3 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,25 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,72 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 16,67% | 0,36 | -0,44R | €-26,51 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 0,95 | -0,03R | €-2,21 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 6 | 6 | 83,33% | 7,11 | 1,06R | €63,32 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 5 | 5 | 40,00% | 0,89 | -0,07R | €-3,68 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 2 | 2 | 0,00% | 0,00 | -0,55R | €-10,95 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 1 | 14 | 14 | 42,86% | 1,00 | -0,00R | €-0,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 4 | 4 | 50,00% | 1,41 | 0,21R | €8,41 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 4 | 4 | 50,00% | 1,45 | 0,12R | €4,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 5 | 5 | 60,00% | 1,95 | 0,42R | €21,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 20 | 20 | 20,00% | 0,37 | -0,47R | €-93,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 15 | 15 | 46,67% | 1,16 | 0,09R | €13,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 34 | 34 | 58,82% | 2,17 | 0,45R | €153,60 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 4 | 4 | 50,00% | 1,45 | 0,12R | €4,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 21 | 21 | 33,33% | 0,66 | -0,24R | €-51,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 5 | 53 | 53 | 24,53% | 0,45 | -0,37R | €-196,43 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,86 | -0,09R | €-13,18 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 35 | 35 | 54,29% | 1,68 | 0,31R | €109,88 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,33 | -0,55R | €-27,71 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 6 | 6 | 83,33% | 6,30 | 1,01R | €60,52 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 5 | 5 | 40,00% | 0,75 | -0,11R | €-5,32 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 21 | 21 | 28,57% | 0,55 | -0,34R | €-72,31 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 33 | 33 | 24,24% | 0,44 | -0,39R | €-130,33 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,92 | -0,05R | €-8,25 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 27 | 27 | 59,26% | 2,13 | 0,45R | €121,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,43R | €28,69 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,29 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 11 | 11 | 27,27% | 0,49 | -0,40R | €-43,48 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 6 | 50 | 50 | 22,00% | 0,49 | -0,34R | €-171,54 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 41,18% | 1,23 | 0,15R | €24,85 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 30 | 30 | 46,67% | 1,61 | 0,33R | €98,09 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,37 | -0,55R | €-32,86 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 6 | 6 | 83,33% | 8,41 | 1,41R | €84,61 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 5 | 5 | 40,00% | 0,99 | -0,01R | €-0,32 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 21 | 21 | 19,05% | 0,43 | -0,50R | €-104,08 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,77 |
| Rapida 1H V2 | RANGE | 0 | 12 | 10 | 33,33% | 0,82 | -0,10R | €-12,29 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 6 | 51 | 51 | 23,53% | 0,43 | -0,38R | €-191,79 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 16 | 16 | 50,00% | 1,30 | 0,16R | €26,17 |
| Rapida 1H V3 Filtered | RANGE | 1 | 35 | 35 | 54,29% | 1,69 | 0,32R | €111,57 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,80 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 62,50% | 2,25 | 0,51R | €40,77 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -0,53R | €-21,30 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 38 | 38 | 47,37% | 1,23 | 0,13R | €49,02 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 5 | 41 | 41 | 24,39% | 0,44 | -0,40R | €-163,90 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,91 | -0,06R | €-9,61 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 30 | 30 | 56,67% | 2,03 | 0,41R | €124,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,43R | €28,69 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,37R | €-11,08 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 15 | 15 | 33,33% | 0,66 | -0,24R | €-36,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 0,82 | -0,12R | €-15,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 16 | 16 | 62,50% | 2,40 | 0,54R | €86,58 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 11 | 11 | 36,36% | 0,74 | -0,18R | €-20,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 0,82 | -0,12R | €-15,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 16 | 16 | 62,50% | 2,40 | 0,54R | €86,58 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 36,36% | 0,74 | -0,18R | €-20,19 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 12 | 12 | 0,00% | 0,00 | -0,95R | €-114,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 0,95 | -0,03R | €-4,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 20 | 20 | 60,00% | 2,17 | 0,48R | €95,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,40 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 15 | 15 | 26,67% | 0,49 | -0,40R | €-60,35 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 4 | 25 | 25 | 24,00% | 0,46 | -0,39R | €-96,66 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,11 | 0,07R | €8,74 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 35 | 35 | 54,29% | 1,69 | 0,32R | €111,57 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -0,53R | €-21,30 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 23 | 23 | 30,43% | 0,58 | -0,31R | €-71,03 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 6 | 50 | 50 | 24,00% | 0,44 | -0,36R | €-180,36 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,85 | -0,10R | €-14,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 34 | 34 | 52,94% | 1,60 | 0,28R | €96,70 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,66 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,45R | €43,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -0,53R | €-21,30 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 21 | 21 | 28,57% | 0,54 | -0,35R | €-73,72 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 5 | 6 | 6 | 33,33% | 1,83 | 0,42R | €25,20 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 4 | 4 | 0,00% | 0,00 | -1,02R | €-40,69 |
| SHADOW_4H_WIDE | RANGE | 9 | 23 | 23 | 30,43% | 1,19 | 0,13R | €30,86 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 16 | 16 | 37,50% | 1,63 | 0,40R | €64,58 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,38 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 15 | 15 | 53,33% | 0,93 | -0,04R | €-5,64 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 0,79 | -0,14R | €-11,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,67 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 16 | 16 | 56,25% | 1,67 | 0,32R | €50,98 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,75 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 5 | 31 | 31 | 29,03% | 0,78 | -0,14R | €-42,83 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 13 | 13 | 30,77% | 0,80 | -0,15R | €-18,85 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 2 | 42 | 42 | 42,86% | 1,37 | 0,22R | €94,39 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,47 | -0,44R | €-21,91 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 22 | 22 | 50,00% | 2,00 | 0,49R | €106,98 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 3 | 3 | 33,33% | 0,33 | -0,48R | €-14,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 36 | 36 | 41,67% | 1,48 | 0,26R | €95,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,33 | -0,46R | €-41,22 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,02 | 0,01R | €1,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 15 | 15 | 60,00% | 2,92 | 0,78R | €117,34 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 12 | 12 | 8,33% | 0,21 | -0,64R | €-76,92 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 6 | 34 | 34 | 38,24% | 0,86 | -0,07R | €-25,27 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 14 | 14 | 28,57% | 0,72 | -0,21R | €-29,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 2 | 30 | 30 | 50,00% | 1,83 | 0,44R | €132,86 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,47 | -0,44R | €-21,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 6 | 6 | 66,67% | 3,52 | 0,92R | €55,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -0,73R | €-21,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 28 | 28 | 39,29% | 1,39 | 0,22R | €60,29 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 5 | 31 | 31 | 29,03% | 0,79 | -0,13R | €-39,62 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 1 | 11 | 11 | 36,36% | 1,02 | 0,01R | €1,26 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 2 | 30 | 30 | 50,00% | 1,83 | 0,44R | €132,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 5 | 5 | 60,00% | 2,65 | 0,72R | €36,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 3 | 3 | 33,33% | 0,39 | -0,43R | €-12,93 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 15 | 15 | 13,33% | 0,34 | -0,52R | €-77,39 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 8 | 8 | 25,00% | 0,75 | -0,16R | €-13,19 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 8 | 8 | 25,00% | 0,75 | -0,16R | €-13,19 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 8 | 8 | 12,50% | 0,07 | -0,51R | €-40,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,22 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 13 | 13 | 69,23% | 4,32 | 1,05R | €137,01 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 4 | 4 | 25,00% | 0,63 | -0,29R | €-11,45 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 10 | 10 | 40,00% | 1,19 | 0,12R | €12,10 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 25 | 25 | 20,00% | 0,51 | -0,37R | €-93,43 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 40,00% | 2,13 | 0,62R | €61,68 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 40,00% | 2,13 | 0,62R | €61,68 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,53 | -0,24R | €-21,28 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 11 | 11 | 45,45% | 1,15 | 0,09R | €9,62 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 2 | 2 | 50,00% | 1,32 | 0,18R | €3,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 4 | 4 | 50,00% | 1,53 | 0,27R | €10,70 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 10 | 10 | 0,00% | 0,00 | -0,72R | €-72,33 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 1,02 | 0,02R | €1,43 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 19 | 19 | 57,89% | 2,89 | 0,82R | €155,76 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 15 | 15 | 46,67% | 1,60 | 0,34R | €50,68 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 27 | 27 | 40,74% | 1,60 | 0,33R | €89,86 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 7 | 21 | 21 | 33,33% | 0,99 | -0,01R | €-1,24 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 12 | 12 | 25,00% | 0,68 | -0,26R | €-30,82 |
| SHADOW_COMBO_TREND | RANGE | 3 | 33 | 33 | 39,39% | 1,33 | 0,21R | €70,59 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,89 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 17 | 17 | 47,06% | 2,04 | 0,52R | €88,27 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TREND_UP | 1 | 28 | 28 | 32,14% | 1,03 | 0,02R | €6,46 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 18,18% | 0,50 | -0,38R | €-42,23 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,15 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,40R | €-12,04 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 3 | 18 | 18 | 22,22% | 0,65 | -0,29R | €-51,62 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 12,50% | 0,32 | -0,63R | €-50,42 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 20 | 20 | 30,00% | 0,99 | -0,01R | €-2,06 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 9 | 9 | 33,33% | 1,35 | 0,21R | €18,91 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 14 | 14 | 35,71% | 1,28 | 0,19R | €26,97 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 1,11 | 0,08R | €4,78 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 3 | 8 | 8 | 12,50% | 0,33 | -0,63R | €-50,08 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 2,41R | €48,18 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 6 | 21 | 21 | 23,81% | 0,63 | -0,24R | €-51,01 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 12 | 12 | 16,67% | 0,41 | -0,53R | €-63,15 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 31 | 31 | 41,94% | 1,57 | 0,33R | €102,87 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,50 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 17 | 17 | 41,18% | 1,59 | 0,33R | €56,40 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 3 | 2 | 2 | 50,00% | 0,52 | -0,24R | €-4,83 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 33 | 33 | 30,30% | 0,98 | -0,01R | €-4,37 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,87 | -0,09R | €-9,90 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 11,11% | 0,27 | -0,59R | €-52,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-23,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 1 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,96R | €58,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 19 | 19 | 10,53% | 0,25 | -0,64R | €-121,97 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 8 | 8 | 12,50% | 0,32 | -0,52R | €-41,76 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 13 | 13 | 61,54% | 3,11 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 21 | 21 | 9,52% | 0,22 | -0,68R | €-143,21 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 8 | 8 | 12,50% | 0,32 | -0,52R | €-41,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 1 | 13 | 13 | 61,54% | 3,11 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 21 | 21 | 9,52% | 0,22 | -0,68R | €-143,39 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 2,73 | 0,63R | €18,93 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,19 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 1 | 13 | 13 | 46,15% | 2,51 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 17 | 17 | 5,88% | 0,20 | -0,71R | €-120,76 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 16 | 16 | 62,50% | 3,25 | 0,86R | €137,25 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 17 | 17 | 5,88% | 0,12 | -0,83R | €-141,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 8 | 8 | 12,50% | 0,32 | -0,52R | €-41,76 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 1 | 13 | 13 | 61,54% | 3,11 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 21 | 21 | 9,52% | 0,22 | -0,68R | €-143,21 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 8 | 30 | 30 | 16,67% | 0,38 | -0,47R | €-140,73 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 19 | 19 | 26,32% | 0,73 | -0,21R | €-40,77 |
| Forza relativa 1H V1 | RANGE | 4 | 41 | 41 | 34,15% | 1,11 | 0,07R | €29,13 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 6 | 6 | 0,00% | 0,00 | -1,02R | €-61,42 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 0 | 17 | 17 | 47,06% | 1,88 | 0,48R | €80,99 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 2 | 2 | 50,00% | 2,15 | 0,58R | €11,69 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | TREND_UP | 1 | 42 | 42 | 35,71% | 1,36 | 0,21R | €86,32 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 16 | 16 | 31,25% | 0,88 | -0,06R | €-10,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 8 | 7 | 25,00% | 0,68 | -0,25R | €-19,89 |
| Forza relativa 1H V2 | RANGE | 1 | 13 | 13 | 61,54% | 3,40 | 0,95R | €123,51 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 0 | 13 | 11 | 38,46% | 1,31 | 0,20R | €25,87 |
| Forza relativa 1H V2 | TREND_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V2 | TREND_UP | 0 | 14 | 13 | 42,86% | 1,60 | 0,35R | €49,20 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 5 | 15 | 15 | 13,33% | 0,26 | -0,53R | €-79,61 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 7 | 7 | 0,00% | 0,00 | -1,11R | €-77,56 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 3 | 3 | 3 | 66,67% | 2,37 | 0,51R | €15,22 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 5 | 15 | 15 | 13,33% | 0,26 | -0,53R | €-79,61 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 7 | 7 | 0,00% | 0,00 | -1,11R | €-77,56 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 3 | 3 | 3 | 66,67% | 2,37 | 0,51R | €15,22 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 5 | 15 | 15 | 13,33% | 0,26 | -0,53R | €-79,61 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 7 | 7 | 0,00% | 0,00 | -1,11R | €-77,56 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 3 | 3 | 3 | 66,67% | 2,37 | 0,51R | €15,22 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 3 | 17 | 17 | 35,29% | 1,09 | 0,05R | €8,64 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 21 | 21 | 33,33% | 0,88 | -0,09R | €-18,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 17 | 17 | 41,18% | 1,49 | 0,26R | €43,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 2 | 3 | 3 | 66,67% | 2,37 | 0,51R | €15,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 4 | 14 | 14 | 57,14% | 0,84 | -0,07R | €-10,20 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,96R | €9,64 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 3 | 5 | 5 | 40,00% | 0,25 | -0,50R | €-24,81 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 4 | 13 | 13 | 53,85% | 0,56 | -0,21R | €-27,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 3 | 5 | 5 | 40,00% | 0,64 | -0,24R | €-12,02 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,65 | -0,21R | €-10,67 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 16,67% | 0,36 | -0,57R | €-34,49 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,53 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,65 | -0,21R | €-10,67 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,30 | -0,65R | €-45,60 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,53 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,65 | -0,21R | €-10,67 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,30 | -0,65R | €-45,60 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,53 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 10 | 10 | 0,00% | 0,00 | -0,72R | €-72,33 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-9,09 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 19 | 19 | 57,89% | 3,31 | 0,88R | €166,71 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 13 | 13 | 46,15% | 1,79 | 0,45R | €58,04 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 26 | 26 | 38,46% | 1,47 | 0,27R | €69,15 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,03R | €-0,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,95 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 8 | 8 | 25,00% | 0,82 | -0,12R | €-9,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 0,00% | 0,00 | -0,68R | €-61,65 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 16,67% | 0,40 | -0,54R | €-32,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,41 | -0,45R | €-31,39 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,05 | -0,55R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 5 | 5 | 20,00% | 0,53 | -0,38R | €-19,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,64R | €-51,51 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 5 | 5 | 20,00% | 0,53 | -0,38R | €-19,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 20,00% | 0,24 | -0,47R | €-47,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,69 | -0,21R | €-19,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 0,00% | 0,00 | -0,69R | €-62,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,69 | -0,21R | €-19,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,21 | -0,52R | €-57,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 16,67% | 0,40 | -0,54R | €-32,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,81 | -0,11R | €-10,01 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,40 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 22,22% | 0,78 | -0,19R | €-16,96 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 11 | 11 | 54,55% | 3,52 | 1,16R | €128,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 1 | 10 | 10 | 10,00% | 0,40 | -0,45R | €-45,34 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 22,22% | 0,78 | -0,19R | €-16,96 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 11 | 11 | 54,55% | 3,52 | 1,16R | €128,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 10 | 10 | 10,00% | 0,40 | -0,45R | €-45,34 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,21 | -0,61R | €-73,57 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 11 | 11 | 27,27% | 0,69 | -0,24R | €-26,69 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 20 | 20 | 60,00% | 3,28 | 0,82R | €164,58 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,96 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 35 | 35 | 42,86% | 1,54 | 0,29R | €102,79 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,06 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,51 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,06 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,55 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-29T05:23:48+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **621**
- Scenari virtuali ancora attivi: **9210**
- Gruppi in attesa dell'uscita originale: **190**
- Gruppi con originale chiuso ma Shadow ancora attive: **431**
- Confronti completati: **107031**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3000 | 3065 | +€8,69 | 51,6% | 873 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3000 | 3065 | +€7,03 | 50,6% | 875 | 21 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3000 | 3065 | +€4,48 | 48,5% | 972 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 2993 | 3058 | +€4,97 | 49,2% | 882 | 57 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 2991 | 3056 | +€3,48 | 48,9% | 827 | 123 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 2991 | 3056 | €-1,81 | 46,9% | 637 | 459 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 2968 | 3033 | +€6,35 | 44,3% | 694 | 80 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 2968 | 3033 | +€4,46 | 43,9% | 671 | 115 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 2968 | 3033 | +€4,31 | 42,1% | 762 | 78 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 2968 | 3033 | +€2,90 | 43,3% | 586 | 192 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 2966 | 3031 | +€1,12 | 41,1% | 508 | 354 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 2962 | 3027 | €-1,72 | 32,5% | 364 | 654 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 2953 | 3018 | €-2,19 | 39,1% | 371 | 720 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 2922 | 2987 | €-4,96 | 32,8% | 169 | 917 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 2910 | 2975 | €-2,31 | 29,9% | 306 | 745 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 2891 | 2956 | +€4,81 | 33,2% | 410 | 330 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2846 | 2911 | €-6,35 | 27,9% | 255 | 786 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2836 | 2901 | +€4,22 | 36,8% | 198 | 511 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2793 | 2858 | €-6,01 | 33,6% | 520 | 557 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2716 | 2781 | €-12,03 | 22,9% | 254 | 830 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-29T05:23:57+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **107031**
- Valutazioni prodotte: **17856**
- Candidature al Blocco 5: **5**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_MBV3_GB20_R100 | 170 | 0,242 | 0,149 | 0,159 | 60,0% | 93,6 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 1640 | 0,288 | 0,149 | 0,231 | 55,7% | 88,9 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 1640 | 0,258 | 0,112 | 0,204 | 55,4% | 88,5 | ELIGIBLE_FOR_MUTATION |
| GB20_R050 | 1640 | 0,301 | 0,149 | 0,250 | 54,6% | 87,7 | VALIDATING |
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

Generato: 2026-07-29T05:25:07+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 23 | 100,00% | 0,97 | €-9,32 | €-0,41 | 1,72% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 23 | 100,00% | 0,88 | €-39,35 | €-1,71 | 1,67% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 9 | 100,00% | 0,58 | €-111,91 | €-12,43 | 1,12% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 6 | 100,00% | 0,00 | €-104,80 | €-17,47 | 1,05% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 24 | 100,00% | 0,74 | €-126,85 | €-5,29 | 2,13% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-29T05:23:38+00:00

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
| DOWN_10 | 58 | 0 | 5302.35 |
| DOWN_20 | 58 | 0 | 10604.70 |
| DOWN_30 | 58 | 1 | 15921.33 |
| DOWN_40 | 58 | 23 | 20215.91 |
| UP_10 | 135 | 0 | 12675.53 |
| UP_20 | 135 | 0 | 25351.07 |
| UP_30 | 135 | 0 | 38026.60 |
| UP_40 | 135 | 48 | 47646.00 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-29T05:23:13+00:00

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

Generato: 2026-07-29T05:25:09+00:00

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

Generato: 2026-07-29T05:25:09+00:00

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

Generato: 2026-07-29T05:25:09+00:00

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

Generato: 2026-07-29T05:25:09+00:00

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
| 1 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 17.0 | E | 62 | 1.45 | 0.181 | 5.40 |
| 2 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 16.6 | E | 71 | 1.31 | 0.124 | 3.55 |
| 3 | SHADOW_1H_FAST_V3 | BASELINE | 16.5 | E | 102 | 1.13 | 0.055 | 5.36 |
| 4 | SHADOW_COMBO_ADAPTIVE | BASELINE | 16.4 | E | 36 | 1.67 | 0.196 | 2.72 |
| 5 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 16.3 | E | 35 | 1.52 | 0.201 | 3.32 |
| 6 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 16.2 | E | 30 | 1.61 | 0.250 | 6.54 |
| 7 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 15.9 | E | 73 | 1.22 | 0.089 | 3.78 |
| 8 | SHADOW_DONCHIAN_1H | BASELINE | 15.4 | E | 36 | 1.49 | 0.274 | 8.55 |
| 9 | SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | BASELINE | 15.0 | E | 31 | 1.42 | 0.188 | 4.15 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 14.6 | E | 59 | 1.26 | 0.085 | 5.89 |

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

Generato: 2026-07-29T05:25:09+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **598**
- Strategie preferite nel regime corrente: **7**
- Strategie da evitare nel regime corrente: **3**
- Memorie contestuali: **281**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.115 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 5 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 77.2 | 17 | 2.60 | 0.490 | 2.17 |
| 6 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | OBSERVING | 77.1 | 11 | 2.84 | 0.537 | 2.17 |
| 7 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 77.0 | 10 | 2.89 | 0.391 | 1.04 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 76.1 | 7 | 2.35 | 0.426 | 1.11 |
| 9 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | OBSERVING | 73.2 | 19 | 1.91 | 0.331 | 3.16 |
| 10 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | OBSERVING | 72.7 | 23 | 1.79 | 0.351 | 2.24 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-29T05:25:09+00:00

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

Generato: 2026-07-29T05:23:38+00:00

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
