# Paper trading automatico KuCoin

Generato: 2026-07-29T05:15:12+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-29T05:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-29T05:08:25+00:00 | 2026-07-29T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-29T04:45:00+00:00 | 2026-07-29T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-29T04:00:00+00:00 | 2026-07-29T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-29T00:00:00+00:00 | 2026-07-29T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ZEC | 240m | SHORT | -7,70 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | COTI | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -4,84 | 6,00 | 1,16 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,58 | 6,00 | 3,42 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 2,16 | 6,00 | 3,84 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 1,94 | 6,00 | 4,06 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,61 | 6,00 | 5,39 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | BANK | 60m | SHORT | -8,25 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | SHORT | -8,25 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | HYPE | 60m | SHORT | -6,73 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | HYPE | 60m | SHORT | -6,73 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 Range Only V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.689,08 | -3,11% | €-310,92 | €3.000,00 | -10,36% | 6 | 27 | 33,33% | 0,70 | 6,36% |

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
| PRINCIPALE | Principale 4H | 6 | €9.689,08 | €1.248,21 | €3.744,64 | €144,37 | €5,05 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.584,01 | €2.771,86 | €5.543,73 | €151,77 | €8,92 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 1 | €10.506,90 | €211,20 | €633,59 | €51,83 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 2 | €10.493,60 | €413,70 | €1.241,11 | €103,78 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 2 | €10.487,01 | €403,79 | €1.211,37 | €105,23 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.477,46 | €1.856,16 | €5.568,48 | €209,35 | €9,35 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.399,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 5 | €10.365,00 | €2.197,27 | €6.591,81 | €106,40 | €17,18 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.355,69 | €70,71 | €141,42 | €2,58 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €10.303,06 | €1.168,08 | €2.336,15 | €55,91 | €23,24 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 2 | €10.301,29 | €346,30 | €1.038,89 | €51,11 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 1 | €10.296,23 | €142,68 | €428,04 | €51,37 | €0,00 |
| TEST | Bilanciata 1H V2 | 2 | €10.279,42 | €173,21 | €519,64 | €49,92 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 3 | €10.262,84 | €1.902,44 | €3.804,89 | €153,05 | €10,69 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.253,49 | €142,81 | €428,44 | €51,41 | €-28,67 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.240,41 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 1 | €10.235,86 | €187,44 | €562,31 | €52,01 | €0,00 |
| TEST | Main Side Regime Guard V1 | 4 | €10.232,50 | €1.389,97 | €4.169,92 | €152,72 | €22,21 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 2 | €10.232,44 | €395,88 | €1.187,64 | €99,47 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €10.224,31 | €37,16 | €74,32 | €1,36 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.218,59 | €143,01 | €429,04 | €51,48 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 1 | €10.218,03 | €227,32 | €681,96 | €52,06 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 2 | €10.208,22 | €405,03 | €1.215,10 | €101,79 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 1 | €10.185,07 | €185,40 | €556,20 | €51,45 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 2 | €10.145,87 | €206,10 | €618,29 | €52,56 | €0,00 |
| TEST | Combo Adaptive | 4 | €10.114,12 | €1.205,67 | €2.411,33 | €104,15 | €0,33 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 2 | €10.099,98 | €263,10 | €789,31 | €51,07 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.096,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 0 | €10.096,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 5 | €10.054,19 | €2.334,73 | €4.669,45 | €151,91 | €10,50 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.050,48 | €3.091,48 | €6.182,96 | €199,05 | €-5,34 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 1 | €10.049,44 | €184,02 | €552,07 | €51,07 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 1 | €10.030,78 | €183,89 | €551,67 | €51,03 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.009,58 | €182,35 | €547,06 | €50,60 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.001,83 | €1.775,58 | €3.551,16 | €200,37 | €27,35 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.994,10 | €2.293,91 | €4.587,82 | €150,23 | €10,64 |
| TEST | Btc Adaptive 1H | 1 | €9.993,77 | €1.158,94 | €3.476,83 | €50,07 | €-18,41 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 1 | €9.993,76 | €675,44 | €2.026,32 | €49,98 | €-0,89 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.990,06 | €3.097,46 | €6.194,92 | €146,85 | €-31,88 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.988,39 | €1.388,29 | €2.776,58 | €149,15 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.987,62 | €2.495,25 | €4.990,50 | €104,10 | €-0,88 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 3 | €9.974,12 | €221,90 | €665,70 | €51,17 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.958,94 | €489,81 | €979,63 | €51,01 | €-0,39 |
| TEST | Scanner Bottom15 Short | 5 | €9.958,94 | €489,81 | €979,63 | €51,01 | €-0,39 |
| TEST | Scanner Bottom20 Short | 5 | €9.958,94 | €489,81 | €979,63 | €51,01 | €-0,39 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.952,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.935,21 | €1.397,03 | €2.794,06 | €51,31 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.934,33 | €3.366,63 | €6.733,26 | €100,30 | €-4,33 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.928,52 | €1.871,48 | €5.614,43 | €149,15 | €-0,87 |
| TEST | Btc Donchian 4H | 1 | €9.925,82 | €1.196,13 | €2.392,26 | €49,75 | €-24,14 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 1 | €9.925,47 | €180,82 | €542,46 | €50,18 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.909,36 | €1.148,42 | €3.445,25 | €49,61 | €-10,89 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.892,55 | €1.147,21 | €3.441,62 | €49,56 | €-18,22 |
| TEST | Sol Ema 4H | 1 | €9.888,11 | €780,22 | €1.560,44 | €49,48 | €-7,03 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.870,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.864,96 | €2.278,82 | €4.557,64 | €147,95 | €10,22 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 1 | €9.843,56 | €85,15 | €170,29 | €3,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 2 | €9.838,56 | €327,41 | €982,22 | €49,25 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 1 | €9.837,77 | €70,70 | €141,40 | €2,58 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.832,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 1 | €9.826,60 | €180,15 | €540,44 | €49,99 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 1 | €9.818,04 | €194,51 | €583,53 | €49,25 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 0 | €9.807,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.806,54 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.799,16 | €33,54 | €67,08 | €1,22 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.796,05 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.771,73 | €20,87 | €41,74 | €0,76 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €9.770,35 | €37,63 | €75,26 | €1,37 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €9.761,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.760,94 | €1.529,14 | €3.058,29 | €48,93 | €-23,74 |
| TEST | Master Adaptive No Alt V1 | 1 | €9.758,94 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Master Adaptive V1 | 1 | €9.754,92 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.724,36 | €177,16 | €531,47 | €49,16 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.710,78 | €1.344,77 | €2.689,54 | €102,28 | €28,48 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 2 | €9.710,17 | €2.043,62 | €4.087,25 | €100,09 | €-23,61 |
| TEST | Combo Scanner | 1 | €9.693,06 | €23,89 | €47,78 | €0,87 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.692,34 | €2.124,48 | €4.248,96 | €121,20 | €10,31 |
| TEST | Scanner Top5 Btc Guard V1 | 0 | €9.688,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 2 | €9.660,53 | €1.051,34 | €3.154,01 | €98,63 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €9.660,48 | €2.436,58 | €4.873,16 | €103,52 | €32,72 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 0 | €9.639,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.628,98 | €1.549,90 | €3.099,79 | €97,01 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 1 | €9.587,00 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.580,46 | €174,53 | €523,60 | €48,43 | €0,00 |
| TEST | Scanner Top10 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Scanner Top15 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Scanner Top20 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Combo Trend | 6 | €9.499,16 | €3.508,09 | €7.016,18 | €141,66 | €19,46 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 0 | €9.463,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €9.450,13 | €172,16 | €516,48 | €47,77 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.408,26 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 1 | €9.333,92 | €883,78 | €1.767,56 | €48,23 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.689,08 | €-314,59 | 27 | 27 | 33,33% | 0,70 | €-11,65 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.584,01 | €577,97 | 36 | 36 | 55,56% | 1,67 | €16,05 | 3,09% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.506,90 | €507,28 | 35 | 35 | 54,29% | 1,94 | €14,49 | 1,96% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.493,60 | €494,34 | 62 | 62 | 48,39% | 1,41 | €7,97 | 2,83% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.487,01 | €487,73 | 73 | 73 | 45,21% | 1,37 | €6,68 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.477,46 | €471,30 | 60 | 60 | 41,67% | 1,37 | €7,85 | 2,49% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.399,89 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.365,00 | €351,55 | 70 | 70 | 47,14% | 1,29 | €5,02 | 3,56% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.355,69 | €355,77 | 49 | 49 | 44,90% | 1,31 | €7,26 | 4,79% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.303,06 | €281,00 | 6 | 6 | 66,67% | 5,76 | €46,83 | 1,61% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.301,29 | €301,92 | 31 | 31 | 51,61% | 2,05 | €9,74 | 2,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.296,23 | €296,59 | 11 | 11 | 63,64% | 2,82 | €26,96 | 1,78% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.279,42 | €279,74 | 39 | 37 | 53,85% | 1,36 | €7,17 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.262,84 | €254,67 | 30 | 30 | 56,67% | 1,73 | €8,49 | 1,58% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.253,49 | €282,54 | 10 | 10 | 50,00% | 2,29 | €28,25 | 1,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.240,41 | €241,67 | 15 | 15 | 60,00% | 4,66 | €16,11 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,86 | €236,20 | 19 | 19 | 52,63% | 1,90 | €12,43 | 2,72% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.232,50 | €212,50 | 13 | 13 | 46,15% | 1,65 | €16,35 | 2,40% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.232,44 | €233,15 | 26 | 26 | 50,00% | 1,70 | €8,97 | 1,76% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.224,31 | €224,35 | 40 | 40 | 40,00% | 1,25 | €5,61 | 3,94% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.218,59 | €218,95 | 12 | 12 | 58,33% | 1,75 | €18,25 | 2,28% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.218,03 | €218,44 | 67 | 67 | 44,78% | 1,16 | €3,26 | 3,61% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.208,22 | €208,95 | 31 | 31 | 54,84% | 1,32 | €6,74 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.185,07 | €185,40 | 71 | 71 | 45,07% | 1,14 | €2,61 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,87 | €146,24 | 42 | 42 | 47,62% | 1,20 | €3,48 | 2,91% |
| TEST | Combo Adaptive | Combo Adaptive | €10.114,12 | €116,12 | 36 | 36 | 44,44% | 1,22 | €3,23 | 2,58% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,98 | €100,46 | 53 | 53 | 56,60% | 1,12 | €1,90 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.096,23 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.096,10 | €96,10 | 59 | 59 | 50,85% | 1,11 | €1,63 | 2,98% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.054,19 | €47,13 | 38 | 38 | 39,47% | 1,07 | €1,24 | 2,31% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.050,48 | €58,63 | 25 | 25 | 52,00% | 1,15 | €2,35 | 2,23% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.049,44 | €49,77 | 22 | 22 | 45,45% | 1,12 | €2,26 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.030,78 | €31,11 | 102 | 102 | 38,24% | 1,02 | €0,31 | 2,94% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,91 | €10,91 | 11 | 11 | 36,36% | 1,23 | €0,99 | 0,25% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.009,58 | €9,91 | 29 | 29 | 37,93% | 1,02 | €0,34 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,18 | €2,18 | 11 | 11 | 36,36% | 1,23 | €0,20 | 0,05% |
| TEST | Ampia 4H | Confluenza trend | €10.001,83 | €-23,91 | 22 | 22 | 22,73% | 0,96 | €-1,09 | 3,68% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.994,10 | €-13,15 | 23 | 23 | 34,78% | 0,96 | €-0,57 | 2,48% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.993,77 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.993,76 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,90% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.990,06 | €26,01 | 14 | 14 | 50,00% | 1,16 | €1,86 | 1,53% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.988,39 | €-9,84 | 15 | 15 | 53,33% | 0,96 | €-0,66 | 1,38% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.987,62 | €-8,51 | 52 | 51 | 40,38% | 0,99 | €-0,16 | 5,53% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.974,12 | €-25,48 | 76 | 76 | 36,84% | 0,98 | €-0,34 | 2,58% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.958,94 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.958,94 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.958,94 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.952,81 | €-47,19 | 11 | 11 | 36,36% | 0,29 | €-4,29 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.935,21 | €-63,10 | 18 | 18 | 27,78% | 0,82 | €-3,51 | 2,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.934,33 | €-56,24 | 41 | 41 | 39,02% | 0,93 | €-1,37 | 5,48% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.928,52 | €-66,58 | 18 | 18 | 38,89% | 0,83 | €-3,70 | 1,76% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.925,82 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,25% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.925,47 | €-74,20 | 35 | 35 | 40,00% | 0,90 | €-2,12 | 4,40% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Sol Ema 1H | Trend following EMA | €9.909,36 | €-77,68 | 6 | 6 | 33,33% | 0,64 | €-12,95 | 1,88% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Btc Ema 1H | Trend following EMA | €9.892,55 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Sol Ema 4H | Trend following EMA | €9.888,11 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,35% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.870,43 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.864,96 | €-141,67 | 21 | 21 | 38,10% | 0,64 | €-6,75 | 2,44% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.843,56 | €-156,34 | 25 | 25 | 32,00% | 0,80 | €-6,25 | 4,68% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.838,56 | €-160,85 | 35 | 35 | 42,86% | 0,76 | €-4,60 | 3,08% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.837,77 | €-162,15 | 29 | 29 | 34,48% | 0,79 | €-5,59 | 4,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.832,55 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,60% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.826,60 | €-173,07 | 76 | 76 | 38,16% | 0,89 | €-2,28 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.818,04 | €-181,61 | 23 | 23 | 43,48% | 0,64 | €-7,90 | 3,23% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.807,66 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,36% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.806,54 | €-191,77 | 21 | 21 | 19,05% | 0,67 | €-9,13 | 3,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.799,16 | €-200,80 | 21 | 21 | 33,33% | 0,74 | €-9,56 | 3,64% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.796,05 | €-202,30 | 16 | 16 | 31,25% | 0,62 | €-12,64 | 2,89% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.771,73 | €-228,24 | 20 | 20 | 30,00% | 0,69 | €-11,41 | 3,98% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.770,35 | €-229,60 | 21 | 21 | 33,33% | 0,64 | €-10,93 | 4,42% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,49 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.760,94 | €-213,48 | 12 | 12 | 33,33% | 0,45 | €-17,79 | 2,92% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.758,94 | €-241,03 | 18 | 18 | 27,78% | 0,66 | €-13,39 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.754,92 | €-245,05 | 18 | 18 | 27,78% | 0,66 | €-13,61 | 4,07% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.724,36 | €-275,32 | 30 | 30 | 33,33% | 0,62 | €-9,18 | 4,83% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.710,78 | €-315,16 | 39 | 39 | 30,77% | 0,68 | €-8,08 | 3,97% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.710,17 | €-263,40 | 17 | 17 | 23,53% | 0,60 | €-15,49 | 4,36% |
| TEST | Combo Scanner | Combo Scanner | €9.693,06 | €-306,92 | 49 | 49 | 36,73% | 0,77 | €-6,26 | 5,08% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.692,34 | €-315,24 | 38 | 38 | 39,47% | 0,56 | €-8,30 | 3,97% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.688,64 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 3,94% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.660,53 | €-337,58 | 18 | 18 | 27,78% | 0,48 | €-18,75 | 4,32% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.660,48 | €-369,44 | 46 | 46 | 28,26% | 0,70 | €-8,03 | 7,55% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.639,39 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.628,98 | €-369,16 | 52 | 52 | 57,69% | 0,60 | €-7,10 | 4,27% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.587,00 | €-411,37 | 33 | 33 | 33,33% | 0,46 | €-12,47 | 5,00% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.580,46 | €-419,23 | 10 | 10 | 0,00% | 0,00 | €-41,92 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Combo Trend | Combo Trend | €9.499,16 | €-515,52 | 56 | 56 | 30,36% | 0,71 | €-9,21 | 7,64% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.463,31 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,43% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.450,13 | €-549,56 | 55 | 55 | 29,09% | 0,62 | €-9,99 | 6,46% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.408,26 | €-590,15 | 26 | 26 | 23,08% | 0,49 | €-22,70 | 6,12% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.333,92 | €-665,02 | 49 | 49 | 28,57% | 0,42 | €-13,57 | 6,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 73,52000 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €-0,12 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,07062 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €-9,01 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 54,56300 | 57,64134 | 73,46073 | 50,62613 | €353,42 | €1.060,27 | €44,83 | €14,19 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63620,87328 | 63957,69000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.153,42 | €3.460,26 | €49,83 | €-18,32 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 55,31793 | 54,56300 | 55,05561 | 73,48066 | 53,09375 | €867,03 | €2.601,09 | €0,00 | €35,50 |
| Bilanciata 1H V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,34076 | 3,34076 | 2,94410 | 2,24388 | 4,13409 | €15,79 | €47,36 | €5,62 | €0,00 |
| 1H Balanced Long No Rhv V1 | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| 1H Balanced Long No Rhv V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,38464 | 3,38464 | 2,98212 | 2,27335 | 4,18968 | €136,07 | €408,22 | €48,55 | €0,00 |
| 1H Balanced Short Trend Down Strict V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 461,87761 | 462,08000 | 473,26988 | 613,52742 | 439,09306 | €675,44 | €2.026,32 | €49,98 | €-0,89 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 54,81304 | 54,56300 | 55,99251 | 72,80998 | 52,45408 | €780,21 | €2.340,62 | €50,37 | €10,68 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 461,87761 | 462,08000 | 473,26988 | 613,52742 | 439,09306 | €707,43 | €2.122,30 | €52,35 | €-0,93 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,28834 | 73,52000 | 74,34369 | 97,35134 | 71,17764 | €41,52 | €124,56 | €1,79 | €-0,39 |
| 1H Fast Score 6 75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €191,12 | €573,36 | €53,03 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €186,12 | €558,37 | €51,65 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,34076 | 3,34076 | 3,03225 | 2,24388 | 3,80354 | €187,97 | €563,92 | €52,08 | €0,00 |
| 1H Fast No Pepe V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €185,40 | €556,20 | €51,45 | €0,00 |
| 1H Fast Tp2 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| 1H Fast Tp2 V1 | NEAR | SHORT | Momentum / breakout | 60m | 3,0x | 1,67599 | 1,67599 | 1,70517 | 2,22628 | 1,61763 | €25,97 | €77,91 | €1,36 | €-0,00 |
| 1H Fast Tp2 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €8,60 | €25,80 | €2,39 | €0,00 |
| Rapida 1H V3 Filtered | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €183,89 | €551,67 | €51,03 | €0,00 |
| 1H Fast V3 Cap75 V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| 1H Fast V3 Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €172,16 | €516,48 | €47,77 | €0,00 |
| 1H Fast V3 No Esports V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €180,15 | €540,44 | €49,99 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €180,82 | €542,46 | €50,18 | €0,00 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 54,56300 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €55,28 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,08535 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €-0,53 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63318,66373 | 63957,69000 | 64874,97444 | 94661,40228 | 58960,99415 | €18,28 | €36,56 | €0,90 | €-0,37 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07062 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,29 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00411 | 0,00383 | 0,00361 | 0,00207 | 0,00549 | €199,76 | €399,51 | €47,94 | €-26,74 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 55,31793 | 54,56300 | 55,29611 | 82,70031 | 52,87133 | €1.199,49 | €2.398,97 | €0,00 | €32,74 |
| Forza relativa 1H V1 | BEAT | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 3,34076 | 3,34076 | 2,94410 | 1,68709 | 4,21342 | €200,74 | €401,49 | €47,67 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 461,87761 | 462,08000 | 473,26988 | 690,50702 | 436,81461 | €16,57 | €33,14 | €0,82 | €-0,01 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 461,87761 | 462,08000 | 473,26988 | 690,50702 | 436,81461 | €1.001,44 | €2.002,88 | €49,40 | €-0,88 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63620,87328 | 63957,69000 | 64638,80725 | 95113,20555 | 61076,03835 | €1.401,20 | €2.802,39 | €44,84 | €-14,84 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,56300 | 56,47572 | 82,45966 | 51,86008 | €1.103,00 | €2.206,00 | €52,74 | €23,76 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,56300 | 56,47572 | 82,45966 | 51,86008 | €1.079,15 | €2.158,31 | €51,60 | €23,24 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 55,41391 | 54,56300 | 56,77767 | 82,84380 | 52,41364 | €13,15 | €26,30 | €0,65 | €0,40 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 469,96599 | 462,08000 | 461,84959 | 702,59915 | 442,94188 | €842,70 | €1.685,39 | €0,00 | €28,28 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,28834 | 73,52000 | 74,46095 | 109,56607 | 70,70859 | €32,26 | €64,53 | €1,03 | €-0,20 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63294,93848 | 63957,69000 | 64206,38559 | 94625,93303 | 61472,04425 | €1.726,79 | €3.453,57 | €49,73 | €-36,16 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 55,31793 | 54,56300 | 55,05561 | 82,70031 | 53,09375 | €1.175,62 | €2.351,23 | €0,00 | €32,09 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,28834 | 73,52000 | 74,34369 | 109,56607 | 71,17764 | €41,16 | €82,32 | €1,19 | €-0,26 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63364,29461 | 63957,69000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,14 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63364,29461 | 63957,69000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,14 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63364,29461 | 63957,69000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,14 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07008 | 0,07062 | 0,07120 | 0,10476 | 0,06727 | €1.529,14 | €3.058,29 | €48,93 | €-23,74 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,67989 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,00 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 469,96599 | 462,08000 | 461,84959 | 702,59915 | 442,94188 | €907,09 | €1.814,17 | €0,00 | €30,44 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,80404 | 54,56300 | 56,08765 | 81,93204 | 51,98009 | €1.015,43 | €2.030,86 | €47,57 | €8,93 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07008 | 0,07062 | 0,07120 | 0,10476 | 0,06761 | €1.282,62 | €2.565,24 | €41,04 | €-19,91 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Adaptive | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €37,18 | €74,35 | €1,57 | €0,33 |
| Combo Adaptive Mfe Trail | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive Quality7 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive Quality7 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive Quality7 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56300 | 55,99251 | 81,94549 | 52,45408 | €1.166,31 | €2.332,62 | €50,19 | €10,64 |
| Combo Adaptive Long Only V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive Long Only V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,00 |
| Combo Adaptive Partial 1R V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive Partial 1R V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56300 | 55,99251 | 81,94549 | 52,45408 | €1.130,49 | €2.260,99 | €48,65 | €10,31 |
| Combo Adaptive Runner25 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive Runner25 V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive Runner25 V1 | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Combo Adaptive Runner25 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56300 | 55,99251 | 81,94549 | 51,27460 | €1.151,04 | €2.302,07 | €49,54 | €10,50 |
| Combo Adaptive Tp3 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive Tp3 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Combo Adaptive Tp3 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 51,33828 | €1.162,02 | €2.324,05 | €48,99 | €10,22 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 63620,87328 | 63957,69000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.147,21 | €3.441,62 | €49,56 | €-18,22 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63318,66373 | 63957,69000 | 64635,54187 | 94661,40228 | 59631,40456 | €1.196,13 | €2.392,26 | €49,75 | €-24,14 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63620,87328 | 63957,69000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.158,94 | €3.476,83 | €50,07 | €-18,41 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,28834 | 73,52000 | 74,34369 | 97,35134 | 71,17764 | €1.148,42 | €3.445,25 | €49,61 | €-10,89 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 73,52000 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-7,03 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €1.215,65 | €2.431,30 | €51,25 | €10,69 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00383 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €-23,61 |
| 1H Fast V3 Nohigh Range Only V1 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,07062 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €-9,53 |
| Main Side Regime Guard V1 | ZEC | SHORT | Confluenza trend | 240m | 3,0x | 469,12616 | 462,08000 | 492,16341 | 623,15591 | 423,05164 | €346,80 | €1.040,39 | €51,09 | €15,63 |
| Main Side Regime Guard V1 | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 54,56300 | 57,64134 | 73,46073 | 50,62613 | €401,28 | €1.203,85 | €50,90 | €16,11 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00411 | 0,00383 | 0,00361 | 0,00276 | 0,00509 | €142,81 | €428,44 | €51,41 | €-28,67 |
| Combo Trend Side Regime Guard V1 | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTC | SHORT | Combo Trend | 60m | 2,0x | 63620,87328 | 63957,69000 | 64638,80725 | 95113,20555 | 61381,41854 | €1.578,90 | €3.157,81 | €50,52 | €-16,72 |
| Combo Trend Side Regime Guard V1 | ZEC | SHORT | Combo Trend | 60m | 2,0x | 473,90520 | 462,08000 | 461,70335 | 708,48827 | 447,10337 | €41,28 | €82,56 | €0,00 | €2,06 |
| Combo Trend Side Regime Guard V1 | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,80404 | 54,56300 | 56,08765 | 81,93204 | 51,98009 | €1.059,16 | €2.118,31 | €49,61 | €9,32 |
| 1H Fast Nohigh Cap75 Short Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,34076 | 3,34076 | 3,03225 | 2,24388 | 3,80354 | €183,30 | €549,89 | €50,78 | €0,00 |
| 1H Balanced V3 Long Only V1 | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| 1H Balanced V3 Long Only V1 | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 461,87761 | 462,08000 | 473,26988 | 613,52742 | 439,09306 | €664,50 | €1.993,49 | €49,17 | €-0,87 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63294,93848 | 63957,69000 | 64206,38559 | 94625,93303 | 61472,04425 | €1.647,88 | €3.295,77 | €47,46 | €-34,51 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €59,89 | €119,78 | €0,00 | €2,63 |
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
| Scanner Bottom 5 Short 1H | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €1,91 | 0,73 | STOP |
| Scanner Bottom20 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Scanner Bottom15 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Scanner Bottom10 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Combo Adaptive Tp3 V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €38,41 | 0,78 | STOP |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €39,96 | 0,78 | STOP |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €37,16 | 0,78 | STOP |
| Combo Adaptive Partial 1R V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,63101 | €46,70 | 0,97 | STOP |
| Combo Adaptive | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €39,06 | 0,78 | STOP |
| 1H Fast V3 No Esports V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,51046 | €4,53 | 0,09 | STOP |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,51046 | €4,62 | 0,09 | STOP |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,51046 | €4,65 | 0,09 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
