# Paper trading automatico KuCoin

Generato: 2026-09-17T13:49:15+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-17T13:31:22+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-17T13:31:22+00:00 | 2026-09-17T13:31:22+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-17T13:15:00+00:00 | 2026-09-17T13:15:00+00:00 | 1,6 min | 25,0 min | OK |
| 60m | 12 | 2026-09-17T12:00:00+00:00 | 2026-09-17T12:00:00+00:00 | 31,6 min | 45,0 min | OK |
| 240m | 12 | 2026-09-17T08:00:00+00:00 | 2026-09-17T08:00:00+00:00 | 1,53 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,53 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,13 | 6,00 | 1,87 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 3,44 | 6,00 | 2,56 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | POWER | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,79 | 6,00 | 4,21 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,53 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 0,70 | 6,00 | 5,30 | STALE_CANDLE | 1,53 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,41 | 6,00 | 5,59 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 91.6 minuti; tolleranza 60 minuti. |
| Forza relativa 1H V1 | NEAR | 60m | LONG | 5,75 | 4,00 | 0,00 | READY | 31,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | ZEC | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida V1 — score 6–7,5 | ZEC | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida score 6–7,5 — senza Trend Up | ZEC | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida score 6–7,5 — Range Only | ZEC | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida score 6–7,5 — Cost Aware | ZEC | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida V1 — no HIGH + score <7,5 | ZEC | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ZEC | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida V1 — senza PEPE | ZEC | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida V1 — target pieno 2R | ZEC | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.12%. |
| Rapida 1H V2 | ZEC | 60m | LONG | 7,75 | 5,00 | 0,00 | STRATEGY_FILTER | 31,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.614,59 | -3,85% | €-193,97 | €3.000,00 | -6,47% | 5 | 64 | 40,62% | 0,78 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 64 | 3832 | PRIME INDICAZIONI | 100 (mancano 36) |

- Trade del Principale 4H chiusi: **64**; win rate **40,62%**; profit factor **0,78**.
- Expectancy: **€-5,90** per trade; P&L netto: **€-377,40**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.614,59 | €701,55 | €2.104,66 | €192,43 | €-6,73 |
| TEST | Benchmark Donchian breakout 1H | 2 | €11.984,13 | €1.358,08 | €2.716,17 | €61,78 | €14,07 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €11.701,98 | €1.326,11 | €2.652,22 | €60,33 | €13,73 |
| TEST | Rapida score 6–7,5 — Cost Aware | 4 | €11.026,40 | €2.720,30 | €8.160,91 | €109,99 | €34,13 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.998,60 | €377,83 | €1.133,50 | €68,97 | €-1,61 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €10.979,00 | €1.846,82 | €3.693,65 | €219,09 | €27,22 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 4 | €10.781,44 | €2.592,51 | €7.777,54 | €106,77 | €10,33 |
| TEST | Rapida 1H V2 | 0 | €10.617,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.591,74 | €43,70 | €87,39 | €4,73 | €-0,41 |
| TEST | Combo Adaptive — madre | 6 | €10.478,20 | €2.615,21 | €5.230,42 | €209,33 | €28,86 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.475,92 | €1.335,77 | €4.007,30 | €156,88 | €15,82 |
| TEST | Rapida V3 NoHigh — Regime Guard | 4 | €10.469,70 | €2.113,65 | €6.340,94 | €155,42 | €-7,25 |
| TEST | Combo Adaptive — Long Only | 1 | €10.443,77 | €54,80 | €109,60 | €0,00 | €3,60 |
| TEST | Scanner Top15 Long | 1 | €10.430,69 | €440,65 | €881,31 | €0,00 | €45,05 |
| TEST | Scanner Top20 Long | 1 | €10.430,69 | €440,65 | €881,31 | €0,00 | €45,05 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.264,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.242,45 | €1.587,68 | €4.763,04 | €153,23 | €31,98 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.235,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 6 | €10.212,34 | €2.542,93 | €5.085,85 | €204,02 | €22,66 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.202,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 4 | €10.194,54 | €1.299,89 | €3.899,67 | €152,67 | €15,39 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.180,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.176,64 | €1.577,48 | €4.732,44 | €152,24 | €31,78 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.134,91 | €686,68 | €2.060,03 | €101,35 | €0,88 |
| TEST | Combo Scanner | 1 | €10.108,19 | €14,17 | €28,34 | €1,63 | €0,93 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 1 | €10.097,17 | €544,16 | €1.632,48 | €50,51 | €-4,31 |
| TEST | Combo Adaptive — parziale 1R | 4 | €10.063,48 | €1.857,43 | €3.714,86 | €200,79 | €26,59 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.061,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.013,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.012,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.002,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €9.996,17 | €2.078,70 | €6.236,11 | €104,54 | €32,98 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.993,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.988,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.985,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.983,79 | €286,89 | €573,77 | €54,81 | €-0,92 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 1 | €9.964,39 | €47,66 | €95,32 | €5,16 | €-0,45 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.961,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €9.958,30 | €35,25 | €70,50 | €3,82 | €-0,33 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.956,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.912,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.874,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 2 | €9.874,06 | €768,33 | €1.536,66 | €98,68 | €8,90 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €9.861,12 | €1.529,57 | €4.588,71 | €148,40 | €-30,46 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 4 | €9.812,00 | €1.512,90 | €4.538,71 | €146,79 | €30,51 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.783,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.779,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.775,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.761,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.676,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.663,97 | €1.568,85 | €4.706,54 | €190,38 | €15,46 |
| TEST | FAST NoHigh <7,5 · SHORT only | 4 | €9.615,51 | €1.491,47 | €4.474,42 | €144,70 | €-29,70 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.605,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 4 | €9.604,64 | €1.615,64 | €3.231,27 | €191,66 | €23,81 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €9.603,56 | €1.480,76 | €4.442,29 | €143,67 | €29,86 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.595,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.543,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 1 | €9.535,86 | €199,57 | €399,13 | €47,90 | €-43,12 |
| TEST | Scanner Bottom15 Short | 1 | €9.535,86 | €199,57 | €399,13 | €47,90 | €-43,12 |
| TEST | Scanner Bottom20 Short | 1 | €9.535,86 | €199,57 | €399,13 | €47,90 | €-43,12 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 1 | €9.469,78 | €198,18 | €396,37 | €47,56 | €-42,82 |
| TEST | Rapida V3 — Long Only | 4 | €9.466,84 | €1.459,68 | €4.379,05 | €141,63 | €29,44 |
| TEST | Eth Adaptive 1H | 0 | €9.459,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 1 | €9.455,37 | €197,88 | €395,77 | €47,49 | €-42,75 |
| TEST | Bilanciata 1H V2 | 2 | €9.436,22 | €489,51 | €1.468,52 | €94,31 | €8,50 |
| TEST | Eth Ema 1H | 0 | €9.414,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 1 | €9.407,38 | €356,44 | €712,87 | €38,61 | €-3,34 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 1 | €9.401,87 | €356,23 | €712,46 | €38,59 | €-3,34 |
| TEST | Top 5 + BTC — Guard | 1 | €9.398,76 | €17,47 | €34,94 | €0,00 | €1,79 |
| TEST | Scanner Bottom 5 Short 1H | 1 | €9.382,61 | €196,36 | €392,72 | €47,13 | €-42,43 |
| TEST | Combo Adaptive — Quality7 | 3 | €9.363,40 | €1.304,68 | €2.609,36 | €140,11 | €35,40 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €9.354,00 | €2.307,71 | €6.923,13 | €93,31 | €28,95 |
| TEST | Btc Ema 1H | 0 | €9.353,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 0 | €9.351,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 1 | €9.335,42 | €33,05 | €66,09 | €3,58 | €-0,31 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €9.315,42 | €2.298,19 | €6.894,57 | €92,93 | €28,83 |
| TEST | Combo Trend | 4 | €9.313,97 | €1.566,74 | €3.133,49 | €185,86 | €23,09 |
| TEST | Top 5 + BTC — Guard + MFE | 1 | €9.180,18 | €17,06 | €34,13 | €0,00 | €1,74 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.143,13 | €1.484,30 | €4.452,91 | €180,12 | €14,63 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 1 | €9.128,99 | €435,60 | €871,21 | €44,29 | €-3,43 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 1 | €9.119,28 | €435,14 | €870,28 | €44,25 | €-3,43 |
| TEST | Bilanciata 1H V1 | 1 | €9.109,33 | €279,62 | €838,86 | €45,44 | €-3,93 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.102,31 | €389,09 | €778,18 | €39,56 | €-3,07 |
| TEST | Master Adaptive V1 | 1 | €9.084,01 | €433,46 | €866,91 | €44,08 | €-3,41 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 3 | €9.041,70 | €117,83 | €235,66 | €8,46 | €-0,92 |
| TEST | Combo Adaptive — MFE Trail esistente | 1 | €9.034,78 | €31,44 | €62,87 | €3,41 | €-0,29 |
| TEST | Master Adaptive Expanded V1 | 0 | €8.985,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €8.980,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 1 | €8.964,16 | €427,66 | €855,33 | €43,49 | €-3,37 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €8.932,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 0 | €8.928,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €8.872,56 | €115,65 | €231,30 | €8,30 | €-0,90 |
| TEST | Rapida V3 — score <7,5 | 3 | €8.838,73 | €1.711,98 | €5.135,95 | €87,99 | €0,69 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 2 | €8.596,81 | €381,90 | €763,81 | €39,97 | €-1,77 |
| TEST | Combo Mean Reversion | 1 | €8.550,69 | €653,10 | €1.306,20 | €43,35 | €19,79 |
| TEST | Forza relativa 1H V1 | 5 | €8.546,60 | €1.515,84 | €3.031,68 | €170,83 | €-20,07 |
| TEST | Master Adaptive Strict3 V1 | 0 | €8.448,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €8.413,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €8.190,54 | €379,33 | €758,67 | €39,70 | €-1,76 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €8.185,86 | €1.220,48 | €2.440,95 | €80,96 | €21,05 |
| TEST | Top 5 + BTC — BTC≤3 | 2 | €8.159,13 | €354,78 | €709,57 | €37,04 | €-1,92 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.614,59 | €-377,40 | 64 | 64 | 40,62% | 0,78 | €-5,90 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.984,13 | €1.971,69 | 170 | 170 | 45,29% | 1,56 | €11,60 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.701,98 | €1.689,83 | 138 | 138 | 44,20% | 1,65 | €12,25 | 6,75% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.026,40 | €997,17 | 212 | 212 | 49,53% | 1,23 | €4,70 | 7,95% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.998,60 | €1.000,64 | 63 | 63 | 55,56% | 1,94 | €15,88 | 7,33% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.979,00 | €954,00 | 161 | 161 | 50,31% | 1,32 | €5,93 | 10,10% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.781,44 | €775,78 | 182 | 182 | 48,90% | 1,21 | €4,26 | 5,29% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.617,99 | €617,99 | 92 | 82 | 48,91% | 1,28 | €6,72 | 3,89% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.591,74 | €592,20 | 198 | 198 | 44,44% | 1,17 | €2,99 | 8,85% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.478,20 | €452,47 | 228 | 228 | 46,49% | 1,13 | €1,98 | 8,17% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.475,92 | €461,61 | 298 | 297 | 43,62% | 1,10 | €1,55 | 9,28% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.469,70 | €425,05 | 182 | 181 | 48,90% | 1,15 | €2,34 | 5,24% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.443,77 | €440,19 | 193 | 193 | 44,56% | 1,13 | €2,28 | 7,78% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.430,69 | €385,70 | 221 | 221 | 47,51% | 1,11 | €1,75 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.430,69 | €385,70 | 221 | 221 | 47,51% | 1,11 | €1,75 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.264,13 | €264,13 | 26 | 26 | 38,46% | 1,36 | €10,16 | 3,39% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.242,45 | €213,32 | 235 | 235 | 48,94% | 1,05 | €0,91 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.235,99 | €235,99 | 23 | 23 | 56,52% | 1,56 | €10,26 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.212,34 | €192,73 | 179 | 179 | 44,13% | 1,06 | €1,08 | 11,68% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.202,44 | €202,44 | 20 | 20 | 60,00% | 1,43 | €10,12 | 3,08% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.194,54 | €181,49 | 289 | 289 | 39,79% | 1,04 | €0,63 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.180,44 | €180,44 | 31 | 31 | 61,29% | 1,28 | €5,82 | 2,77% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.176,64 | €147,70 | 279 | 279 | 44,44% | 1,03 | €0,53 | 9,48% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.134,91 | €135,27 | 119 | 119 | 42,02% | 1,05 | €1,14 | 7,07% |
| TEST | Combo Scanner | Combo Scanner | €10.108,19 | €107,27 | 196 | 196 | 43,37% | 1,03 | €0,55 | 11,38% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.097,17 | €102,46 | 76 | 76 | 43,42% | 1,06 | €1,35 | 6,49% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.063,48 | €39,12 | 187 | 187 | 44,92% | 1,01 | €0,21 | 8,69% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.061,36 | €61,36 | 33 | 33 | 48,48% | 1,43 | €1,86 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.013,96 | €13,96 | 18 | 18 | 44,44% | 1,25 | €0,78 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.012,27 | €12,27 | 33 | 33 | 48,48% | 1,43 | €0,37 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.002,79 | €2,79 | 18 | 18 | 44,44% | 1,25 | €0,16 | 0,11% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,71 | €-2,29 | 12 | 12 | 33,33% | 0,62 | €-0,19 | 0,04% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.996,17 | €-37,29 | 207 | 206 | 44,44% | 0,99 | €-0,18 | 7,10% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.993,20 | €-6,80 | 5 | 5 | 20,00% | 0,05 | €-1,36 | 0,07% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.988,57 | €-11,43 | 12 | 12 | 33,33% | 0,62 | €-0,95 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.985,57 | €-14,43 | 22 | 22 | 36,36% | 0,31 | €-0,66 | 0,17% |
| TEST | Ampia 4H | Confluenza trend | €9.983,79 | €-14,92 | 65 | 65 | 33,85% | 0,99 | €-0,23 | 4,45% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.964,39 | €-35,11 | 205 | 205 | 44,88% | 0,99 | €-0,17 | 10,31% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.961,80 | €-38,20 | 33 | 33 | 48,48% | 0,78 | €-1,16 | 0,84% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.958,30 | €-41,33 | 164 | 164 | 44,51% | 0,99 | €-0,25 | 11,27% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.956,63 | €-43,37 | 18 | 18 | 38,89% | 0,56 | €-2,41 | 0,89% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.912,62 | €-87,38 | 29 | 29 | 44,83% | 0,89 | €-3,01 | 4,59% |
| TEST | Sol Ema 1H | Trend following EMA | €9.874,85 | €-125,15 | 31 | 31 | 38,71% | 0,87 | €-4,04 | 4,45% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.874,06 | €-133,92 | 151 | 144 | 41,06% | 0,96 | €-0,89 | 10,88% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.861,12 | €-105,66 | 224 | 224 | 41,96% | 0,97 | €-0,47 | 10,86% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.812,00 | €-215,79 | 270 | 270 | 41,48% | 0,96 | €-0,80 | 10,60% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.783,14 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,32% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.779,96 | €-220,04 | 23 | 23 | 39,13% | 0,66 | €-9,57 | 3,93% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.775,84 | €-224,16 | 20 | 20 | 40,00% | 0,67 | €-11,21 | 3,48% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.761,07 | €-238,93 | 19 | 19 | 47,37% | 0,58 | €-12,58 | 3,13% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.676,47 | €-323,53 | 23 | 23 | 34,78% | 0,61 | €-14,07 | 4,65% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.663,97 | €-348,67 | 226 | 226 | 41,15% | 0,92 | €-1,54 | 14,04% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.615,51 | €-352,10 | 187 | 187 | 40,64% | 0,89 | €-1,88 | 10,86% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.605,65 | €-394,35 | 199 | 199 | 45,73% | 0,93 | €-1,98 | 8,44% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.604,64 | €-417,23 | 163 | 163 | 40,49% | 0,85 | €-2,56 | 12,31% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.603,56 | €-423,64 | 243 | 243 | 42,39% | 0,91 | €-1,74 | 10,92% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.595,38 | €-404,62 | 201 | 201 | 43,28% | 0,92 | €-2,01 | 6,64% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.543,88 | €-456,12 | 91 | 91 | 46,15% | 0,79 | €-5,01 | 6,28% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.535,86 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.535,86 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.535,86 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.469,78 | €-487,17 | 66 | 66 | 34,85% | 0,72 | €-7,38 | 9,08% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.466,84 | €-559,98 | 273 | 273 | 41,03% | 0,90 | €-2,05 | 12,52% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.459,83 | €-540,17 | 26 | 26 | 34,62% | 0,42 | €-20,78 | 5,44% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.455,37 | €-501,64 | 67 | 67 | 34,33% | 0,71 | €-7,49 | 9,08% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.436,22 | €-571,40 | 180 | 166 | 44,44% | 0,84 | €-3,17 | 11,82% |
| TEST | Eth Ema 1H | Trend following EMA | €9.414,26 | €-585,74 | 34 | 34 | 35,29% | 0,50 | €-17,23 | 5,86% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.407,38 | €-588,86 | 176 | 176 | 41,48% | 0,85 | €-3,35 | 11,91% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.401,87 | €-594,36 | 180 | 180 | 41,67% | 0,85 | €-3,30 | 12,06% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.398,76 | €-603,03 | 168 | 168 | 36,31% | 0,83 | €-3,59 | 7,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.382,61 | €-574,73 | 94 | 94 | 34,04% | 0,75 | €-6,11 | 10,17% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.363,40 | €-670,44 | 104 | 104 | 37,50% | 0,75 | €-6,45 | 8,88% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.354,00 | €-670,79 | 210 | 210 | 43,33% | 0,88 | €-3,19 | 15,94% |
| TEST | Btc Ema 1H | Trend following EMA | €9.353,69 | €-646,31 | 28 | 28 | 25,00% | 0,36 | €-23,08 | 6,56% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.351,06 | €-648,94 | 145 | 145 | 43,45% | 0,75 | €-4,48 | 9,26% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.335,42 | €-664,23 | 156 | 156 | 43,59% | 0,79 | €-4,26 | 12,28% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.315,42 | €-709,27 | 248 | 248 | 41,94% | 0,89 | €-2,86 | 15,64% |
| TEST | Combo Trend | Combo Trend | €9.313,97 | €-707,24 | 197 | 197 | 40,61% | 0,83 | €-3,59 | 14,08% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.180,18 | €-821,56 | 185 | 185 | 37,30% | 0,79 | €-4,44 | 8,78% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.143,13 | €-868,82 | 181 | 181 | 41,44% | 0,72 | €-4,80 | 13,79% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.128,99 | €-867,06 | 123 | 123 | 30,89% | 0,74 | €-7,05 | 10,08% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.119,28 | €-876,77 | 118 | 118 | 33,05% | 0,73 | €-7,43 | 9,87% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.109,33 | €-886,24 | 212 | 212 | 40,09% | 0,77 | €-4,18 | 15,68% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.102,31 | €-894,15 | 110 | 110 | 30,91% | 0,72 | €-8,13 | 9,31% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.084,01 | €-912,06 | 120 | 120 | 32,50% | 0,73 | €-7,60 | 9,87% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.041,70 | €-957,27 | 163 | 163 | 36,20% | 0,69 | €-5,87 | 14,10% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.034,78 | €-964,89 | 240 | 240 | 40,83% | 0,77 | €-4,02 | 15,45% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €8.985,64 | €-1.014,36 | 99 | 99 | 33,33% | 0,63 | €-10,25 | 10,40% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €8.980,11 | €-1.019,89 | 66 | 66 | 28,79% | 0,49 | €-15,45 | 12,43% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €8.964,16 | €-1.031,95 | 154 | 154 | 41,56% | 0,71 | €-6,70 | 10,69% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €8.932,47 | €-1.067,53 | 161 | 161 | 38,51% | 0,74 | €-6,63 | 12,74% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €8.928,71 | €-1.071,29 | 113 | 113 | 25,66% | 0,68 | €-9,48 | 12,03% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.872,56 | €-1.126,43 | 143 | 143 | 35,66% | 0,60 | €-7,88 | 14,10% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €8.838,73 | €-1.158,88 | 266 | 266 | 39,85% | 0,81 | €-4,36 | 19,03% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €8.596,81 | €-1.400,96 | 136 | 136 | 36,76% | 0,63 | €-10,30 | 16,24% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.550,69 | €-1.468,36 | 85 | 85 | 36,47% | 0,51 | €-17,27 | 16,17% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.546,60 | €-1.431,63 | 178 | 178 | 34,27% | 0,61 | €-8,04 | 19,11% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.448,19 | €-1.551,81 | 88 | 88 | 26,14% | 0,56 | €-17,63 | 15,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.413,97 | €-1.586,03 | 126 | 126 | 30,95% | 0,61 | €-12,59 | 16,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.190,54 | €-1.807,25 | 159 | 159 | 37,74% | 0,59 | €-11,37 | 18,17% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.185,86 | €-1.833,77 | 148 | 148 | 41,89% | 0,57 | €-12,39 | 20,15% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.159,13 | €-1.838,52 | 136 | 136 | 35,29% | 0,50 | €-13,52 | 20,25% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Principale 4H | BR | LONG | Confluenza trend | 240m | 3,0x | 0,64695 | 0,65492 | 0,56932 | 0,43453 | 0,80222 | €133,65 | €400,94 | €48,11 | €4,94 |
| Principale 4H | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,86857 | 2,86100 | 2,65907 | 1,92673 | 3,28758 | €219,58 | €658,74 | €48,11 | €-1,74 |
| Principale 4H | ARB | LONG | Confluenza trend | 240m | 3,0x | 0,16607 | 0,16275 | 0,14920 | 0,11155 | 0,19981 | €157,86 | €473,57 | €48,11 | €-9,48 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1362,57246 | 1361,36000 | 1248,37180 | 915,19450 | 1590,97378 | €171,74 | €515,21 | €43,18 | €-0,46 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1367,76350 | 1361,36000 | 1293,68004 | 918,68115 | 1515,93042 | €279,62 | €838,86 | €45,44 | €-3,93 |
| Bilanciata 1H V2 | BR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,79300 | €130,95 | €392,86 | €47,14 | €9,46 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 1362,57246 | 1361,36000 | 1302,82825 | 915,19450 | 1482,06089 | €358,55 | €1.075,66 | €47,16 | €-0,96 |
| Bilanciata 1H V3 Filtered | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,68654 | 2,86100 | 2,79641 | 1,80446 | 2,90794 | €21,14 | €63,41 | €0,00 | €4,12 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1287,46996 | 906,10503 | 1472,17933 | €352,57 | €1.057,70 | €48,27 | €9,66 |
| Bilanciata 1H V3 Filtered | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,65492 | 0,56033 | 0,42768 | 0,78955 | €134,14 | €402,41 | €48,29 | €11,49 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15793 | 0,11196 | 0,18419 | €306,48 | €919,44 | €48,29 | €-21,70 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 79,97846 | 54,82165 | 84,90405 | €754,53 | €2.263,59 | €45,53 | €11,89 |
| Rapida V1 — score 6–7,5 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €436,21 | €1.308,64 | €46,45 | €11,95 |
| Rapida V1 — score 6–7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €379,23 | €1.137,68 | €46,47 | €-26,85 |
| Rapida V1 — score 6–7,5 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,80756 | 2,86100 | 2,81113 | 1,88575 | 2,94000 | €492,54 | €1.477,61 | €0,00 | €28,12 |
| Rapida V1 — score 6–7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €990,21 | €2.970,64 | €0,00 | €15,60 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €438,02 | €1.314,06 | €46,65 | €12,00 |
| Rapida score 6–7,5 — senza Trend Up | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €380,80 | €1.142,39 | €46,66 | €-26,96 |
| Rapida score 6–7,5 — senza Trend Up | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,80756 | 2,86100 | 2,81113 | 1,88575 | 2,94000 | €494,58 | €1.483,73 | €0,00 | €28,24 |
| Rapida score 6–7,5 — senza Trend Up | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €994,31 | €2.982,94 | €0,00 | €15,67 |
| Rapida score 6–7,5 — Range Only | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,86857 | 2,86100 | 2,77981 | 1,92673 | 3,00171 | €544,16 | €1.632,48 | €50,51 | €-4,31 |
| Rapida score 6–7,5 — Cost Aware | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €516,33 | €1.549,00 | €54,99 | €14,15 |
| Rapida score 6–7,5 — Cost Aware | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €448,88 | €1.346,64 | €55,01 | €-31,78 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,80756 | 2,86100 | 2,81113 | 1,88575 | 2,94000 | €583,00 | €1.749,01 | €0,00 | €33,29 |
| Rapida score 6–7,5 — Cost Aware | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €1.172,09 | €3.516,26 | €0,00 | €18,47 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €464,55 | €1.393,66 | €49,47 | €12,73 |
| Rapida V1 — no HIGH + score <7,5 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13492 | 0,13638 | 0,16175 | 0,09985 | €137,41 | €412,22 | €49,47 | €-44,53 |
| Rapida V1 — no HIGH + score <7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €403,64 | €1.210,92 | €49,46 | €-28,57 |
| Rapida V1 — no HIGH + score <7,5 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,80756 | 2,86100 | 2,81113 | 1,88575 | 2,94000 | €523,97 | €1.571,91 | €0,00 | €29,92 |
| Rapida V1 — senza PEPE | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €145,31 | €435,94 | €52,31 | €10,50 |
| Rapida V1 — senza PEPE | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €554,12 | €1.662,36 | €0,00 | €38,91 |
| Rapida V1 — senza PEPE | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €491,15 | €1.473,46 | €52,30 | €13,46 |
| Rapida V1 — senza PEPE | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13492 | 0,13638 | 0,16175 | 0,09985 | €145,18 | €435,55 | €52,27 | €-47,05 |
| Rapida V1 — target pieno 2R | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,79300 | €141,41 | €424,23 | €50,91 | €10,22 |
| Rapida V1 — target pieno 2R | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,97150 | €539,24 | €1.617,71 | €0,00 | €37,87 |
| Rapida V1 — target pieno 2R | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1444,81499 | €477,96 | €1.433,88 | €50,90 | €13,10 |
| Rapida V1 — target pieno 2R | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13492 | 0,13638 | 0,16175 | 0,09254 | €141,28 | €423,85 | €50,86 | €-45,79 |
| Rapida 1H V3 Filtered — madre | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €140,94 | €422,82 | €50,74 | €10,18 |
| Rapida 1H V3 Filtered — madre | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €537,45 | €1.612,34 | €0,00 | €37,74 |
| Rapida 1H V3 Filtered — madre | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €476,37 | €1.429,12 | €50,73 | €13,05 |
| Rapida 1H V3 Filtered — madre | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €414,35 | €1.243,04 | €50,78 | €-29,33 |
| Rapida 1H V3 Filtered — madre | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €8,37 | €25,12 | €0,00 | €0,13 |
| Rapida V3 — score <7,5 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €412,91 | €1.238,73 | €43,97 | €11,31 |
| Rapida V3 — score <7,5 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €359,21 | €1.077,64 | €44,02 | €-25,43 |
| Rapida V3 — score <7,5 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €939,86 | €2.819,58 | €0,00 | €14,81 |
| Rapida V3 — no volatilità HIGH | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1366,74329 | 1361,36000 | 1312,69659 | 917,99591 | 1447,81335 | €41,02 | €123,07 | €4,87 | €-0,48 |
| Rapida V3 — no volatilità HIGH | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €138,41 | €415,22 | €49,83 | €10,00 |
| Rapida V3 — no volatilità HIGH | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €527,78 | €1.583,35 | €0,00 | €37,06 |
| Rapida V3 — no volatilità HIGH | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €406,76 | €1.220,27 | €49,85 | €-28,80 |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €964,73 | €2.894,20 | €0,00 | €15,20 |
| Rapida V3 — Long Only | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €131,11 | €393,33 | €47,20 | €9,47 |
| Rapida V3 — Long Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €499,97 | €1.499,90 | €0,00 | €35,11 |
| Rapida V3 — Long Only | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €443,15 | €1.329,46 | €47,19 | €12,14 |
| Rapida V3 — Long Only | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €385,45 | €1.156,36 | €47,23 | €-27,29 |
| Rapida V3 — senza ESPORTS | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €133,00 | €399,01 | €47,88 | €9,61 |
| Rapida V3 — senza ESPORTS | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €507,19 | €1.521,56 | €0,00 | €35,62 |
| Rapida V3 — senza ESPORTS | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €449,55 | €1.348,66 | €47,87 | €12,32 |
| Rapida V3 — senza ESPORTS | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €391,02 | €1.173,06 | €47,92 | €-27,68 |
| Rapida V3 senza ESPORTS — Long Only | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €135,89 | €407,68 | €48,92 | €9,82 |
| Rapida V3 senza ESPORTS — Long Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €518,20 | €1.554,59 | €0,00 | €36,39 |
| Rapida V3 senza ESPORTS — Long Only | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €459,31 | €1.377,93 | €48,91 | €12,58 |
| Rapida V3 senza ESPORTS — Long Only | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €399,51 | €1.198,52 | €48,96 | €-28,28 |
| Rapida V3 senza ESPORTS — MFE Lock | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €141,85 | €425,56 | €51,07 | €10,25 |
| Rapida V3 senza ESPORTS — MFE Lock | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,79556 | 2,86100 | 2,81108 | 1,87768 | 2,92751 | €540,92 | €1.622,77 | €0,00 | €37,99 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €479,45 | €1.438,36 | €51,06 | €13,14 |
| Rapida V3 senza ESPORTS — MFE Lock | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €417,03 | €1.251,08 | €51,10 | €-29,52 |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €8,43 | €25,28 | €0,00 | €0,13 |
| Rapida V3 senza ESPORTS — Stress Guard | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1366,74329 | 1361,36000 | 1312,69659 | 917,99591 | 1447,81335 | €448,80 | €1.346,39 | €53,24 | €-5,30 |
| Rapida V3 senza ESPORTS — Stress Guard | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16731 | 0,16275 | 0,16033 | 0,11238 | 0,17779 | €427,51 | €1.282,54 | €53,53 | €-34,98 |
| Rapida V3 senza ESPORTS — Stress Guard | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,80756 | 2,86100 | 2,81113 | 1,88575 | 2,94000 | €570,06 | €1.710,18 | €0,00 | €32,55 |
| Rapida V3 senza ESPORTS — Stress Guard | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €1.146,14 | €3.438,42 | €0,00 | €18,06 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,72745 | 0,72745 | 0,78235 | 1,08754 | 0,57376 | €23,11 | €46,21 | €3,49 | €-0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08143 | 0,08122 | 0,08517 | 0,12174 | 0,07096 | €31,75 | €63,49 | €2,92 | €0,16 |
| Ampia 4H | SOL | SHORT | Confluenza trend | 240m | 2,0x | 97,48250 | 100,43300 | 102,49471 | 145,73634 | 83,44831 | €17,85 | €35,69 | €1,84 | €-1,08 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,72256 | 0,72256 | 0,74546 | 1,08022 | 0,67216 | €672,88 | €1.345,76 | €42,66 | €-0,00 |
| Forza relativa 1H V1 | BR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,80835 | €178,47 | €356,94 | €42,83 | €8,60 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1349,03975 | 1361,36000 | 1287,46996 | 681,26508 | 1484,49330 | €469,23 | €938,46 | €42,83 | €8,57 |
| Forza relativa 1H V1 | POWER | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,08962 | €173,42 | €346,84 | €41,62 | €-37,47 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 81,62032 | 82,04900 | 79,97846 | 41,21826 | 85,23242 | €21,85 | €43,70 | €0,88 | €0,23 |
| Forza relativa 1H V2 | BR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,80835 | €205,54 | €411,09 | €49,33 | €9,90 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1362,57246 | 1361,36000 | 1302,82825 | 688,09909 | 1494,00974 | €562,79 | €1.125,57 | €49,35 | €-1,00 |
| Benchmark Donchian breakout 1H | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,56868 | 59,42929 | 84,57018 | 49,41718 | €19,03 | €38,06 | €1,92 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 81,62032 | 82,04900 | 79,79603 | 41,21826 | 86,18106 | €1.339,05 | €2.678,11 | €59,86 | €14,07 |
| Donchian 1H Gb20 120R V1 | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,56868 | 59,42929 | 84,57018 | 49,41718 | €18,58 | €37,16 | €1,88 | €-0,00 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 81,62032 | 82,04900 | 79,79603 | 41,21826 | 86,18106 | €1.307,53 | €2.615,06 | €58,45 | €13,73 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,28183 | 1,30125 | 1,23929 | 0,64732 | 1,34563 | €603,45 | €1.206,90 | €40,05 | €18,29 |
| Benchmark Bollinger mean reversion 1H | NEAR | SHORT | Bollinger mean reversion | 60m | 2,0x | 2,86743 | 2,86100 | 2,96249 | 4,28680 | 2,72483 | €617,03 | €1.234,06 | €40,91 | €2,77 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 1349,03975 | 1361,36000 | 1280,62887 | 681,26508 | 1499,54369 | €472,42 | €944,85 | €47,91 | €8,63 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,79556 | 2,86100 | 2,66989 | 1,41176 | 3,07204 | €532,88 | €1.065,76 | €47,91 | €24,95 |
| Benchmark trend following EMA 1H | BR | LONG | Trend following EMA | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,80835 | €199,61 | €399,22 | €47,91 | €9,61 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,16668 | 0,16275 | 0,15696 | 0,08418 | 0,18808 | €410,73 | €821,46 | €47,94 | €-19,38 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1515,93042 | €43,70 | €87,39 | €4,73 | €-0,41 |
| Scanner Bottom 5 Short 1H | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,09254 | €196,36 | €392,72 | €47,13 | €-42,43 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1515,93042 | €47,66 | €95,32 | €5,16 | €-0,45 |
| Scanner Bottom10 Short | POWER | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-43,12 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1295,15898 | 1361,36000 | 1321,87126 | 654,05528 | 1445,14594 | €440,65 | €881,31 | €0,00 | €45,05 |
| Scanner Bottom15 Short | POWER | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-43,12 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1295,15898 | 1361,36000 | 1321,87126 | 654,05528 | 1445,14594 | €440,65 | €881,31 | €0,00 | €45,05 |
| Scanner Bottom20 Short | POWER | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-43,12 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1530,74711 | €35,25 | €70,50 | €3,82 | €-0,33 |
| Top 5 + BTC — solo MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1530,74711 | €33,05 | €66,09 | €3,58 | €-0,31 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1295,15898 | 1361,36000 | 1321,87126 | 654,05528 | 1460,14465 | €17,47 | €34,94 | €0,00 | €1,79 |
| Top 5 + BTC — BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1530,74711 | €341,89 | €683,78 | €37,04 | €-3,20 |
| Top 5 + BTC — BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,72554 | 2,86100 | 2,79943 | 1,37640 | 2,96458 | €12,89 | €25,78 | €0,00 | €1,28 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1295,15898 | 1361,36000 | 1321,87126 | 654,05528 | 1460,14465 | €17,06 | €34,13 | €0,00 | €1,74 |
| Top 5 + BTC — Guard + BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1530,74711 | €368,96 | €737,91 | €39,97 | €-3,45 |
| Top 5 + BTC — Guard + BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,68654 | 2,86100 | 2,79641 | 1,35670 | 2,93008 | €12,95 | €25,89 | €0,00 | €1,68 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1530,74711 | €366,47 | €732,95 | €39,70 | €-3,43 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,68654 | 2,86100 | 2,79641 | 1,35670 | 2,93008 | €12,86 | €25,72 | €0,00 | €1,67 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1590,01389 | €356,23 | €712,46 | €38,59 | €-3,34 |
| Top 5 + BTC — target pieno 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1590,01389 | €356,44 | €712,87 | €38,61 | €-3,34 |
| Combo Trend | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,79556 | 2,86100 | 2,66989 | 1,41176 | 3,07204 | €516,79 | €1.033,59 | €46,46 | €24,20 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1349,03975 | 1361,36000 | 1280,62887 | 681,26508 | 1499,54369 | €458,08 | €916,17 | €46,46 | €8,37 |
| Combo Trend | BR | LONG | Combo Trend | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,80835 | €193,57 | €387,13 | €46,46 | €9,32 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,16668 | 0,16275 | 0,15696 | 0,08418 | 0,18808 | €398,30 | €796,60 | €46,48 | €-18,80 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,28183 | 1,30125 | 1,23929 | 0,64732 | 1,34989 | €653,10 | €1.306,20 | €43,35 | €19,79 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 1318,09357 | 1361,36000 | 1242,45840 | 665,63725 | 1484,49092 | €14,17 | €28,34 | €1,63 | €0,93 |
| Combo Adaptive — madre | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30125 | 1,33225 | 1,92042 | 1,18918 | €35,04 | €70,07 | €2,60 | €-0,91 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1505,72053 | €14,74 | €29,48 | €1,50 | €-0,12 |
| Combo Adaptive — madre | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,86100 | 2,68245 | 1,41176 | 3,02177 | €645,80 | €1.291,60 | €52,26 | €30,23 |
| Combo Adaptive — madre | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,79300 | €217,71 | €435,43 | €52,25 | €10,49 |
| Combo Adaptive — madre | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,16275 | 0,15793 | 0,08418 | 0,18419 | €497,62 | €995,25 | €52,27 | €-23,49 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 81,62032 | 82,04900 | 79,97846 | 41,21826 | 84,90405 | €1.204,29 | €2.408,59 | €48,45 | €12,65 |
| Combo Adaptive — MFE Trail esistente | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1515,93042 | €31,44 | €62,87 | €3,41 | €-0,29 |
| Combo Adaptive — Quality7 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,86100 | 2,68245 | 1,41176 | 3,02177 | €576,49 | €1.152,98 | €46,65 | €26,99 |
| Combo Adaptive — Quality7 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,79300 | €194,35 | €388,69 | €46,64 | €9,36 |
| Combo Adaptive — Quality7 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1362,57246 | 1361,36000 | 1302,82825 | 688,09909 | 1482,06089 | €533,85 | €1.067,69 | €46,81 | €-0,95 |
| Combo Adaptive — Long Only | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1318,09357 | 1361,36000 | 1324,16060 | 665,63725 | 1469,36389 | €54,80 | €109,60 | €0,00 | €3,60 |
| Combo Adaptive — parziale 1R | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,86100 | 2,68245 | 1,41176 | 3,02177 | €620,33 | €1.240,66 | €50,20 | €29,04 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1349,03975 | 1361,36000 | 1287,46996 | 681,26508 | 1472,17933 | €549,86 | €1.099,71 | €50,19 | €10,04 |
| Combo Adaptive — parziale 1R | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,79300 | €209,11 | €418,22 | €50,19 | €10,07 |
| Combo Adaptive — parziale 1R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,16275 | 0,15793 | 0,08418 | 0,18419 | €478,13 | €956,27 | €50,22 | €-22,57 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €73,50 | €146,99 | €4,81 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30125 | 1,33225 | 1,92042 | 1,14149 | €31,43 | €62,85 | €2,33 | €-0,82 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1575,20916 | €12,91 | €25,81 | €1,31 | €-0,10 |
| Combo Adaptive — target pieno 3R | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €72,15 | €144,29 | €4,72 | €-0,00 |
| Combo Adaptive — target pieno 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30125 | 1,33225 | 1,92042 | 1,14149 | €30,84 | €61,68 | €2,29 | €-0,80 |
| Combo Adaptive — target pieno 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1575,20916 | €12,67 | €25,33 | €1,29 | €-0,10 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1505,72052 | €433,46 | €866,91 | €44,08 | €-3,41 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1505,72052 | €427,66 | €855,33 | €43,49 | €-3,37 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1575,20914 | €389,09 | €778,18 | €39,56 | €-3,07 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30125 | 1,33225 | 1,92042 | 1,18918 | €28,88 | €57,77 | €2,14 | €-0,75 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1361,36000 | 1293,68004 | 690,72057 | 1515,93042 | €18,84 | €37,68 | €2,04 | €-0,18 |
| Combo Adaptive — Side × Regime Guard | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,79300 | €212,32 | €424,65 | €50,96 | €10,23 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,80756 | 2,86100 | 2,69405 | 1,41782 | 3,03459 | €630,04 | €1.260,08 | €50,95 | €23,98 |
| Combo Adaptive — Side × Regime Guard | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,16275 | 0,15793 | 0,08418 | 0,18419 | €485,00 | €970,00 | €50,94 | €-22,89 |
| Combo Adaptive — Side × Regime Guard | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 81,62032 | 82,04900 | 79,97846 | 41,21826 | 84,90405 | €1.167,84 | €2.335,68 | €46,98 | €12,27 |
| Master Adaptive GB20 — Breakeven 0,5R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1505,72052 | €435,60 | €871,21 | €44,29 | €-3,43 |
| Master Adaptive GB20 — 50% a 0,75R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1361,36000 | 1297,25468 | 690,20536 | 1505,72052 | €435,14 | €870,28 | €44,25 | €-3,43 |
| Rapida V3 NoHigh — Range Only | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,64695 | 0,65492 | 0,56932 | 0,43453 | 0,76340 | €140,77 | €422,30 | €50,68 | €5,20 |
| Rapida V3 NoHigh — Range Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,86857 | 2,86100 | 2,77981 | 1,92673 | 3,00171 | €545,91 | €1.637,73 | €50,67 | €-4,32 |
| Rapida V3 NoHigh — Regime Guard | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1366,74329 | 1361,36000 | 1312,69659 | 917,99591 | 1447,81335 | €428,09 | €1.284,28 | €50,79 | €-5,06 |
| Rapida V3 NoHigh — Regime Guard | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,63952 | 0,65492 | 0,56278 | 0,42954 | 0,75463 | €145,30 | €435,91 | €52,31 | €10,50 |
| Rapida V3 NoHigh — Regime Guard | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €426,97 | €1.280,91 | €52,32 | €-30,23 |
| Rapida V3 NoHigh — Regime Guard | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 81,62032 | 54,82165 | 83,53583 | €1.113,28 | €3.339,84 | €0,00 | €17,54 |
| MAIN — Side × Regime Guard | SUI | SHORT | Confluenza trend | 240m | 3,0x | 0,72995 | 0,72995 | 0,77421 | 0,96962 | 0,64144 | €294,19 | €882,58 | €53,51 | €-0,00 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,29295 | 1,30125 | 1,37261 | 1,71747 | 1,13364 | €83,64 | €250,92 | €15,46 | €-1,61 |
| Combo Trend — Side × Regime Guard | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,79556 | 2,86100 | 2,66989 | 1,41176 | 3,07204 | €609,18 | €1.218,36 | €54,77 | €28,52 |
| Combo Trend — Side × Regime Guard | ZEC | LONG | Combo Trend | 60m | 2,0x | 1349,03975 | 1361,36000 | 1280,62887 | 681,26508 | 1499,54369 | €539,97 | €1.079,95 | €54,77 | €9,86 |
| Combo Trend — Side × Regime Guard | BR | LONG | Combo Trend | 60m | 2,0x | 0,63952 | 0,65492 | 0,56278 | 0,32296 | 0,80835 | €228,17 | €456,34 | €54,76 | €10,99 |
| Combo Trend — Side × Regime Guard | ARB | LONG | Combo Trend | 60m | 2,0x | 0,16668 | 0,16275 | 0,15696 | 0,08418 | 0,18808 | €469,50 | €939,00 | €54,79 | €-22,16 |
| FAST NoHigh <7,5 · SHORT only | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1349,03975 | 1361,36000 | 1301,15213 | 906,10503 | 1420,87118 | €452,98 | €1.358,95 | €48,24 | €12,41 |
| FAST NoHigh <7,5 · SHORT only | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13492 | 0,13638 | 0,16175 | 0,09985 | €133,98 | €401,95 | €48,23 | €-43,42 |
| FAST NoHigh <7,5 · SHORT only | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,16275 | 0,15987 | 0,11196 | 0,17690 | €393,59 | €1.180,76 | €48,23 | €-27,86 |
| FAST NoHigh <7,5 · SHORT only | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,80756 | 2,86100 | 2,81113 | 1,88575 | 2,94000 | €510,92 | €1.532,76 | €0,00 | €29,17 |
| Bilanciata V3 · LONG only | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,68654 | 2,86100 | 2,79641 | 1,80446 | 2,90794 | €19,99 | €59,97 | €0,00 | €3,89 |
| Bilanciata V3 · LONG only | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1349,03975 | 1361,36000 | 1287,46996 | 906,10503 | 1472,17933 | €333,56 | €1.000,69 | €45,67 | €9,14 |
| Bilanciata V3 · LONG only | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,65492 | 0,56033 | 0,42768 | 0,78955 | €126,91 | €380,72 | €45,69 | €10,87 |
| Bilanciata V3 · LONG only | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16668 | 0,16275 | 0,15793 | 0,11196 | 0,18419 | €289,96 | €869,88 | €45,68 | €-20,53 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 81,62032 | 82,04900 | 79,97846 | 54,82165 | 84,90405 | €713,88 | €2.141,64 | €43,08 | €11,25 |
| Scanner Bottom5 Short Profit Lock V1 | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,09254 | €197,88 | €395,77 | €47,49 | €-42,75 |
| Scanner Bottom5 Short Mfe Trail V1 | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13492 | 0,13638 | 0,18204 | 0,09254 | €198,18 | €396,37 | €47,56 | €-42,82 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Mean Reversion | HYPE | SHORT | 2026-09-17T13:30:00+00:00 | 82,97194 | €-46,64 | -1,08 | STOP |
| Bilanciata V3 · LONG only | BTC | SHORT | 2026-09-17T12:45:00+00:00 | 77050,57484 | €-1,21 | -1,09 | STOP |
| Eth Adaptive 1H | ETH | SHORT | 2026-09-17T12:30:00+00:00 | 2458,26312 | €-50,15 | -1,05 | STOP |
| Eth Ema 1H | ETH | SHORT | 2026-09-17T12:30:00+00:00 | 2458,26312 | €-49,91 | -1,05 | STOP |
| Btc Ema 1H | BTC | SHORT | 2026-09-17T12:30:00+00:00 | 76881,83555 | €-50,78 | -1,08 | STOP |
| Donchian 1H Gb20 120R V1 | NEAR | LONG | 2026-09-17T12:45:00+00:00 | 2,89285 | €134,44 | 2,46 | TARGET |
| Benchmark Donchian breakout 1H | NEAR | LONG | 2026-09-17T12:45:00+00:00 | 2,89285 | €137,68 | 2,46 | TARGET |
| Forza relativa 1H V1 | NEAR | LONG | 2026-09-17T12:45:00+00:00 | 2,89330 | €2,94 | 2,16 | TARGET |
| Rapida V3 — score <7,5 | NEAR | LONG | 2026-09-17T12:15:00+00:00 | 2,88925 | €61,83 | 1,45 | TARGET |
| Bilanciata 1H V3 Filtered | BTC | SHORT | 2026-09-17T12:45:00+00:00 | 77050,57484 | €-1,28 | -1,09 | STOP |
| Bilanciata 1H V1 | BTC | SHORT | 2026-09-17T12:30:00+00:00 | 76856,92874 | €-2,55 | -1,08 | STOP |
| Rapida V3 NoHigh — Regime Guard | NEAR | LONG | 2026-09-17T12:00:00+00:00 | 2,85173 | €2,54 | 1,45 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🧪 Validazione congiunta Research + Paper

I due campioni vengono letti insieme ma **non sommati**: il paper è normalmente un sottoinsieme dei segnali Research. La soglia usa gli **eventi di mercato indipendenti**.
Research è HYPOTHESIS_SCREENING_ONLY: PF e numerosità non superano un gate di causalità/parità/integrità non PASS.

Requisiti per la revisione live: almeno **30 eventi indipendenti per lato**, PF almeno **1,10**, expectancy positiva e max drawdown paper non superiore a **15,00%**.

| Profilo | Conto paper di riferimento | Research eventi | Paper eventi | PF Research | PF Paper | Exp. Research | Exp. Paper | DD Paper | Accordo | Stato |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 856/30 | 33/30 | 0,86 | 2,04 | -0,07R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 802/30 | 20/30 | 0,82 | 1,90 | -0,09R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 382/30 | 22/30 | 0,93 | 1,74 | -0,03R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 389/30 | 22/30 | 0,89 | 1,57 | -0,06R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 716/30 | 31/30 | 0,92 | 0,62 | -0,04R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 667/30 | 11/30 | 0,90 | 0,00 | -0,05R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 244/30 | 8/30 | 0,90 | 1,02 | -0,05R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 538/30 | 17/30 | 0,82 | 4,50 | -0,10R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 765/30 | 24/30 | 0,81 | 0,64 | -0,10R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 712/30 | 7/30 | 0,73 | 0,02 | -0,14R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 716/30 | 30/30 | 0,94 | 1,02 | -0,03R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 1210/30 | 55/30 | 0,86 | 1,12 | -0,06R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 305/30 | 15/30 | 0,75 | 0,99 | -0,14R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 1059/30 | 44/30 | 0,81 | 1,20 | -0,10R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 1063/30 | 37/30 | 0,81 | 0,76 | -0,09R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 993/30 | 23/30 | 0,77 | 1,12 | -0,12R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 450/30 | 64/30 | 0,80 | 0,78 | -0,12R | €-5,90 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 26/30 | 0,00 | 1,36 | 0,00R | €10,16 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 63/30 | 0,00 | 1,94 | 0,00R | €15,88 | 7,33% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 40/30 | 22/30 | 0,36 | 0,53 | -0,36R | €-2,69 | 0,73% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 57/30 | 33/30 | 0,82 | 0,78 | -0,09R | €-1,16 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 1201/30 | 212/30 | 0,88 | 0,77 | -0,07R | €-4,18 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 145/30 | 0,00 | 0,75 | 0,00R | €-4,48 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 15/30 | 0,00 | 1,01 | 0,00R | €0,14 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 414/30 | 166/30 | 1,04 | 0,84 | 0,02R | €-3,17 | 11,82% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 781/30 | 226/30 | 0,92 | 0,92 | -0,04R | €-1,54 | 14,04% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 702/30 | 181/30 | 0,87 | 0,72 | -0,07R | €-4,80 | 13,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 378/30 | 161/30 | 0,86 | 0,74 | -0,07R | €-6,63 | 12,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 799/30 | 187/30 | 0,92 | 0,89 | -0,04R | €-1,88 | 10,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 866/30 | 224/30 | 0,93 | 0,97 | -0,03R | €-0,47 | 10,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1366/30 | 297/30 | 0,85 | 1,10 | -0,08R | €1,55 | 9,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 212/30 | 0,00 | 1,23 | 0,00R | €4,70 | 7,95% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 210/30 | 0,00 | 0,88 | 0,00R | €-3,19 | 15,94% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 76/30 | 0,00 | 1,06 | 0,00R | €1,35 | 6,49% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 786/30 | 248/30 | 0,91 | 0,89 | -0,04R | €-2,86 | 15,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1321/30 | 289/30 | 0,83 | 1,04 | -0,09R | €0,63 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 107/30 | 82/30 | 1,00 | 1,28 | -0,00R | €6,72 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 1263/30 | 279/30 | 0,85 | 1,03 | -0,08R | €0,53 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 963/30 | 266/30 | 0,88 | 0,81 | -0,06R | €-4,36 | 19,03% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 433/30 | 199/30 | 1,00 | 0,93 | -0,00R | €-1,98 | 8,44% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 440/30 | 201/30 | 0,95 | 0,92 | -0,03R | €-2,01 | 6,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 811/30 | 273/30 | 0,93 | 0,90 | -0,03R | €-2,05 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 119/30 | 0,00 | 1,05 | 0,00R | €1,14 | 7,07% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 181/30 | 0,00 | 1,15 | 0,00R | €2,34 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 899/30 | 206/30 | 0,86 | 0,99 | -0,07R | €-0,18 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 270/30 | 0,00 | 0,96 | 0,00R | €-0,80 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 235/30 | 0,00 | 1,05 | 0,00R | €0,91 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 182/30 | 0,00 | 1,21 | 0,00R | €4,26 | 5,29% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 1216/30 | 243/30 | 0,83 | 0,91 | -0,09R | €-1,74 | 10,92% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 419/30 | 65/30 | 0,82 | 0,99 | -0,12R | €-0,23 | 4,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 409/30 | 148/30 | 1,08 | 0,57 | 0,03R | €-12,39 | 20,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 20/30 | 14/30 | 0,65 | 0,80 | -0,18R | €-4,65 | 2,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 4/30 | 4/30 | 0,76 | 0,77 | -0,19R | €-8,79 | 1,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 12/30 | 9/30 | 2,57 | 2,77 | 0,45R | €22,61 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 4/30 | 4/30 | 2,81 | 2,86 | 0,50R | €25,47 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 23/30 | 16/30 | 0,40 | 0,85 | -0,42R | €-3,76 | 1,98% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 9/30 | 7/30 | 0,32 | 0,41 | -0,65R | €-27,30 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 34/30 | 28/30 | 0,52 | 0,36 | -0,32R | €-23,08 | 6,56% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 6/30 | 5/30 | 0,45 | 0,58 | -0,49R | €-17,17 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 1001/30 | 228/30 | 0,93 | 1,13 | -0,04R | €1,98 | 8,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 637/30 | 193/30 | 0,95 | 1,13 | -0,02R | €2,28 | 7,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 1122/30 | 240/30 | 0,94 | 0,77 | -0,03R | €-4,02 | 15,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 942/30 | 187/30 | 0,90 | 1,01 | -0,05R | €0,21 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 102/30 | 58/30 | 1,37 | 0,95 | 0,16R | €-1,12 | 4,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 102/30 | 58/30 | 1,33 | 0,86 | 0,14R | €-3,27 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 349/30 | 104/30 | 0,88 | 0,75 | -0,06R | €-6,45 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 286/30 | 91/30 | 1,00 | 0,79 | 0,00R | €-5,01 | 6,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 163/30 | 0,74 | 0,69 | -0,20R | €-5,87 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 179/30 | 0,00 | 1,06 | 0,00R | €1,08 | 11,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 143/30 | 0,74 | 0,60 | -0,20R | €-7,88 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 160/30 | 85/30 | 1,00 | 0,51 | -0,00R | €-17,27 | 16,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 636/30 | 196/30 | 0,98 | 1,03 | -0,01R | €0,55 | 11,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 828/30 | 197/30 | 0,92 | 0,83 | -0,04R | €-3,59 | 14,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 161/30 | 0,00 | 1,32 | 0,00R | €5,93 | 10,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 22/30 | 19/30 | 1,03 | 0,58 | 0,01R | €-12,58 | 3,13% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 26/30 | 20/30 | 0,80 | 1,43 | -0,13R | €10,12 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 44/30 | 31/30 | 0,63 | 1,28 | -0,23R | €5,82 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 436/30 | 170/30 | 0,89 | 1,56 | -0,07R | €11,60 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 366/30 | 138/30 | 0,89 | 1,65 | -0,06R | €12,25 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 841/30 | 163/30 | 0,88 | 0,85 | -0,07R | €-2,56 | 12,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 35/30 | 26/30 | 0,51 | 0,42 | -0,36R | €-20,78 | 5,44% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 21/30 | 12/30 | 2,42 | 0,70 | 0,45R | €-10,99 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 31/30 | 23/30 | 0,63 | 0,61 | -0,26R | €-14,07 | 4,65% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 48/30 | 34/30 | 0,40 | 0,50 | -0,42R | €-17,23 | 5,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 8/30 | 9/30 | 0,39 | 0,41 | -0,40R | €-24,10 | 2,32% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 21/30 | 23/30 | 1,00 | 0,66 | -0,00R | €-9,57 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 430/30 | 99/30 | 1,02 | 0,63 | 0,01R | €-10,25 | 10,40% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 123/30 | 0,00 | 0,74 | 0,00R | €-7,05 | 10,08% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 113/30 | 0,00 | 0,68 | 0,00R | €-9,48 | 12,03% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 118/30 | 0,00 | 0,73 | 0,00R | €-7,43 | 9,87% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 818/30 | 154/30 | 1,24 | 0,71 | 0,08R | €-6,70 | 10,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 355/30 | 126/30 | 1,02 | 0,61 | 0,01R | €-12,59 | 16,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 396/30 | 110/30 | 1,02 | 0,72 | 0,01R | €-8,13 | 9,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 252/30 | 88/30 | 0,90 | 0,56 | -0,07R | €-17,63 | 15,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 412/30 | 120/30 | 1,00 | 0,73 | 0,00R | €-7,60 | 9,87% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 995/30 | 178/30 | 0,86 | 0,61 | -0,08R | €-8,04 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 396/30 | 144/30 | 1,02 | 0,96 | 0,01R | €-0,89 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 341/30 | 75/30 | 0,59 | 0,78 | -0,23R | €-5,61 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 341/30 | 75/30 | 0,59 | 0,78 | -0,23R | €-5,61 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 341/30 | 75/30 | 0,59 | 0,78 | -0,23R | €-5,61 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 362/30 | 94/30 | 0,69 | 0,75 | -0,17R | €-6,11 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 411/30 | 66/30 | 0,79 | 0,72 | -0,09R | €-7,38 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 369/30 | 67/30 | 0,73 | 0,71 | -0,12R | €-7,49 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 645/30 | 205/30 | 0,93 | 0,99 | -0,04R | €-0,17 | 10,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 647/30 | 221/30 | 0,93 | 1,11 | -0,04R | €1,75 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 647/30 | 221/30 | 0,93 | 1,11 | -0,04R | €1,75 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 609/30 | 164/30 | 0,98 | 0,99 | -0,01R | €-0,25 | 11,27% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 218/30 | 66/30 | 0,66 | 0,49 | -0,21R | €-15,45 | 12,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 464/30 | 136/30 | 0,78 | 0,50 | -0,13R | €-13,52 | 20,25% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 503/30 | 159/30 | 0,94 | 0,59 | -0,03R | €-11,37 | 18,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 415/30 | 136/30 | 0,83 | 0,63 | -0,10R | €-10,30 | 16,24% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 633/30 | 185/30 | 1,02 | 0,79 | 0,01R | €-4,44 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 514/30 | 168/30 | 0,97 | 0,83 | -0,02R | €-3,59 | 7,34% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 702/30 | 156/30 | 0,96 | 0,79 | -0,02R | €-4,26 | 12,28% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 556/30 | 180/30 | 0,93 | 0,85 | -0,04R | €-3,30 | 12,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 528/30 | 176/30 | 0,95 | 0,85 | -0,03R | €-3,35 | 11,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 669/30 | 198/30 | 1,00 | 1,17 | 0,00R | €2,99 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 43/30 | 29/30 | 0,79 | 0,89 | -0,14R | €-3,01 | 4,59% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 11/30 | 10/30 | 1,54 | 1,64 | 0,26R | €13,87 | 1,37% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 31/30 | 20/30 | 0,82 | 0,67 | -0,10R | €-11,21 | 3,48% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 6/30 | 5/30 | 2,48 | 0,88 | 0,51R | €-3,80 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 34/30 | 23/30 | 0,98 | 1,56 | -0,01R | €10,26 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 10/30 | 9/30 | 0,73 | 1,15 | -0,20R | €4,46 | 2,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 44/30 | 31/30 | 0,80 | 0,87 | -0,14R | €-4,04 | 4,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 12/30 | 11/30 | 0,64 | 1,02 | -0,25R | €0,50 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08122**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 34.2 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 76526.3 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, stop_within_limit**
- High **0.0813**; close **0.08113**; wick alta **81.0%**; volume **x0.92**

### Gestione

- TP1 0,07107: chiude 25% e porta lo stop residuo al pareggio costi.
- TP2 0,06961: chiude 25% e porta lo stop residuo a TP1.
- TP3 0,06400: chiude 25% e porta lo stop residuo a TP2.
- TP4 0,06000: chiude l’ultimo 25%.
- Stop iniziale dinamico: almeno 0,08060, sopra il massimo della rejection con buffer 0,2%, mai oltre 0,08120.
- Politica conservativa: se stop e target sono toccati nella stessa candela, prevale lo stop.

## 🔬 Research All Signals

CAUSALITY= AFFECTED (storico) / CLEAN solo per LEGACY_RESEARCH_CAUSAL_V3
SEMANTIC_PARITY= REQUIRES_REVIEW · EVIDENCE_TIER=RESEARCH
PROMOTION_ELIGIBLE=NO · HYPOTHESIS_SCREENING_ONLY
⚠ Historical Research result — invalid for promotion evidence
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=539; LEGACY_RESEARCH_EVIDENCE_V3=18682; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **86,10%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +2.04%, 73% oltre +1%.
- BTC trend score: **-1,00**; ADX: **28,69**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **2,04%**; dispersione: **5,69%**

- Aperti in questo ciclo: **99**
- Chiusi in questo ciclo: **181**
- Posizioni research aperte: **970**
- Trade research chiusi: **50281**
- Eventi di mercato indipendenti chiusi: **6673**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **137055**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 13 | 856 | 856 | 36,92% | 0,86 | -0,07R | €-588,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 14 | 802 | 802 | 36,41% | 0,82 | -0,09R | €-730,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 4 | 382 | 382 | 47,64% | 0,93 | -0,03R | €-130,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 4 | 389 | 389 | 37,02% | 0,89 | -0,06R | €-218,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 7 | 716 | 716 | 37,57% | 0,92 | -0,04R | €-277,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 7 | 667 | 667 | 37,78% | 0,90 | -0,05R | €-324,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 244 | 244 | 39,34% | 0,90 | -0,05R | €-116,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 8 | 538 | 538 | 36,06% | 0,82 | -0,10R | €-514,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 12 | 765 | 765 | 35,16% | 0,81 | -0,10R | €-752,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 13 | 712 | 712 | 34,13% | 0,73 | -0,14R | €-1010,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 7 | 716 | 716 | 37,85% | 0,94 | -0,03R | €-217,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 15 | 1210 | 1210 | 40,50% | 0,86 | -0,06R | €-773,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 305 | 305 | 39,67% | 0,75 | -0,14R | €-432,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 15 | 1059 | 1059 | 35,22% | 0,81 | -0,10R | €-1008,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 15 | 1063 | 1063 | 35,18% | 0,81 | -0,09R | €-1009,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 15 | 993 | 993 | 34,64% | 0,77 | -0,12R | €-1169,95 |
| MAIN | 25 | 450 | 450 | 30,44% | 0,80 | -0,12R | €-538,58 |
| RSI_EXTREME_LONG_15M | 0 | 40 | 40 | 37,50% | 0,36 | -0,36R | €-145,44 |
| RSI_EXTREME_SHORT_15M | 0 | 57 | 57 | 42,11% | 0,82 | -0,09R | €-52,44 |
| Bilanciata 1H V1 | 28 | 1201 | 1201 | 37,39% | 0,88 | -0,07R | €-796,66 |
| Bilanciata 1H V2 | 11 | 475 | 414 | 41,47% | 1,04 | 0,02R | €103,48 |
| Bilanciata 1H V3 Filtered | 17 | 781 | 781 | 38,41% | 0,92 | -0,04R | €-326,72 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 17 | 702 | 702 | 38,32% | 0,87 | -0,07R | €-472,06 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 378 | 378 | 37,57% | 0,86 | -0,07R | €-276,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 15 | 799 | 799 | 38,67% | 0,92 | -0,04R | €-323,98 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 15 | 866 | 866 | 39,03% | 0,93 | -0,03R | €-289,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 22 | 1366 | 1366 | 37,41% | 0,85 | -0,08R | €-1085,51 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 10 | 786 | 786 | 39,31% | 0,91 | -0,04R | €-342,76 |
| SHADOW_1H_FAST_TP2_V1 | 21 | 1321 | 1321 | 35,35% | 0,83 | -0,09R | €-1177,57 |
| Rapida 1H V2 | 0 | 122 | 107 | 45,90% | 1,00 | -0,00R | €-0,44 |
| Rapida 1H V3 Filtered | 15 | 1263 | 1263 | 37,53% | 0,85 | -0,08R | €-1002,15 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 12 | 963 | 963 | 39,04% | 0,88 | -0,06R | €-562,59 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 4 | 433 | 433 | 48,50% | 1,00 | -0,00R | €-8,07 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 4 | 440 | 440 | 39,32% | 0,95 | -0,03R | €-110,29 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 7 | 811 | 811 | 39,46% | 0,93 | -0,03R | €-282,38 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 11 | 899 | 899 | 37,26% | 0,86 | -0,07R | €-671,11 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 15 | 1216 | 1216 | 37,17% | 0,83 | -0,09R | €-1084,11 |
| SHADOW_4H_WIDE | 36 | 419 | 419 | 25,06% | 0,82 | -0,12R | €-485,63 |
| SHADOW_BOLLINGER_MR_1H | 2 | 409 | 409 | 48,90% | 1,08 | 0,03R | €141,92 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 20 | 20 | 50,00% | 0,65 | -0,18R | €-35,17 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 4 | 4 | 25,00% | 0,76 | -0,19R | €-7,44 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 12 | 12 | 75,00% | 2,57 | 0,45R | €53,43 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 4 | 4 | 75,00% | 2,81 | 0,50R | €19,94 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 23 | 23 | 34,78% | 0,40 | -0,42R | €-95,85 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 9 | 9 | 11,11% | 0,32 | -0,65R | €-58,49 |
| SHADOW_BTC_EMA_1H | 0 | 34 | 34 | 38,24% | 0,52 | -0,32R | €-109,09 |
| SHADOW_BTC_EMA_4H | 0 | 6 | 6 | 16,67% | 0,45 | -0,49R | €-29,19 |
| SHADOW_COMBO_ADAPTIVE | 23 | 1001 | 1001 | 39,96% | 0,93 | -0,04R | €-379,97 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 13 | 637 | 637 | 40,66% | 0,95 | -0,02R | €-157,86 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 23 | 1122 | 1122 | 40,46% | 0,94 | -0,03R | €-312,03 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 23 | 942 | 942 | 41,72% | 0,90 | -0,05R | €-493,29 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 102 | 102 | 49,02% | 1,37 | 0,16R | €159,66 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 102 | 102 | 44,12% | 1,33 | 0,14R | €140,93 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 13 | 349 | 349 | 38,97% | 0,88 | -0,06R | €-223,78 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 1 | 286 | 286 | 40,91% | 1,00 | 0,00R | €2,92 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 160 | 160 | 46,25% | 1,00 | -0,00R | €-1,64 |
| SHADOW_COMBO_SCANNER | 14 | 636 | 636 | 38,36% | 0,98 | -0,01R | €-64,74 |
| SHADOW_COMBO_TREND | 22 | 828 | 828 | 36,47% | 0,92 | -0,04R | €-365,07 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 22 | 22 | 54,55% | 1,03 | 0,01R | €2,87 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 26 | 26 | 42,31% | 0,80 | -0,13R | €-33,11 |
| SHADOW_DOGE_EMA_1H | 0 | 44 | 44 | 36,36% | 0,63 | -0,23R | €-100,13 |
| SHADOW_DONCHIAN_1H | 7 | 436 | 436 | 36,01% | 0,89 | -0,07R | €-292,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 7 | 366 | 366 | 37,98% | 0,89 | -0,06R | €-227,35 |
| SHADOW_EMA_TREND_1H | 22 | 841 | 841 | 35,67% | 0,88 | -0,07R | €-563,68 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 35 | 35 | 34,29% | 0,51 | -0,36R | €-124,30 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 21 | 21 | 66,67% | 2,42 | 0,45R | €94,65 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 31 | 31 | 35,48% | 0,63 | -0,26R | €-79,28 |
| SHADOW_ETH_EMA_1H | 0 | 48 | 48 | 33,33% | 0,40 | -0,42R | €-203,72 |
| SHADOW_ETH_EMA_4H | 0 | 8 | 8 | 37,50% | 0,39 | -0,40R | €-31,92 |
| SHADOW_GLOBAL_PURE | 0 | 21 | 21 | 47,62% | 1,00 | -0,00R | €-0,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 14 | 430 | 430 | 33,95% | 1,02 | 0,01R | €42,76 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 10 | 818 | 818 | 65,65% | 1,24 | 0,08R | €632,97 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 10 | 355 | 355 | 33,52% | 1,02 | 0,01R | €47,48 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 13 | 396 | 396 | 33,33% | 1,02 | 0,01R | €52,34 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 252 | 252 | 30,95% | 0,90 | -0,07R | €-167,98 |
| SHADOW_MASTER_ADAPTIVE_V1 | 13 | 412 | 412 | 33,74% | 1,00 | 0,00R | €12,89 |
| Forza relativa 1H V1 | 29 | 995 | 995 | 33,87% | 0,86 | -0,08R | €-793,48 |
| Forza relativa 1H V2 | 18 | 425 | 396 | 38,12% | 1,02 | 0,01R | €48,62 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 13 | 341 | 341 | 31,67% | 0,59 | -0,23R | €-793,51 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 13 | 341 | 341 | 31,67% | 0,59 | -0,23R | €-793,51 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 13 | 341 | 341 | 31,67% | 0,59 | -0,23R | €-793,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 12 | 362 | 362 | 32,32% | 0,69 | -0,17R | €-614,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 12 | 411 | 411 | 54,26% | 0,79 | -0,09R | €-380,43 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 12 | 369 | 369 | 53,39% | 0,73 | -0,12R | €-443,21 |
| SHADOW_SCANNER_TOP10_LONG | 13 | 645 | 645 | 39,22% | 0,93 | -0,04R | €-242,12 |
| SHADOW_SCANNER_TOP15_LONG | 13 | 647 | 647 | 39,26% | 0,93 | -0,04R | €-238,59 |
| SHADOW_SCANNER_TOP20_LONG | 13 | 647 | 647 | 39,26% | 0,93 | -0,04R | €-238,59 |
| SHADOW_SCANNER_TOP5_BTC | 14 | 609 | 609 | 37,77% | 0,98 | -0,01R | €-67,46 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 3 | 218 | 218 | 31,19% | 0,66 | -0,21R | €-465,45 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 13 | 464 | 464 | 34,05% | 0,78 | -0,13R | €-580,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 11 | 503 | 503 | 41,75% | 0,94 | -0,03R | €-150,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 11 | 415 | 415 | 35,42% | 0,83 | -0,10R | €-402,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 12 | 633 | 633 | 43,13% | 1,02 | 0,01R | €64,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 12 | 514 | 514 | 38,52% | 0,97 | -0,02R | €-88,02 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 14 | 702 | 702 | 42,02% | 0,96 | -0,02R | €-131,31 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 14 | 556 | 556 | 37,05% | 0,93 | -0,04R | €-209,71 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 14 | 528 | 528 | 36,93% | 0,95 | -0,03R | €-156,71 |
| SHADOW_SCANNER_TOP5_LONG | 13 | 669 | 669 | 39,16% | 1,00 | 0,00R | €12,23 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 43 | 43 | 39,53% | 0,79 | -0,14R | €-60,01 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 11 | 11 | 54,55% | 1,54 | 0,26R | €28,27 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 31 | 31 | 48,39% | 0,82 | -0,10R | €-30,88 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 6 | 6 | 66,67% | 2,48 | 0,51R | €30,82 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 34 | 34 | 47,06% | 0,98 | -0,01R | €-3,42 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 10 | 10 | 30,00% | 0,73 | -0,20R | €-20,19 |
| SHADOW_SOL_EMA_1H | 0 | 44 | 44 | 36,36% | 0,80 | -0,14R | €-59,46 |
| SHADOW_SOL_EMA_4H | 0 | 12 | 12 | 33,33% | 0,64 | -0,25R | €-30,53 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 3 | 128 | 128 | 32,03% | 0,65 | -0,19R | €-244,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 3 | 223 | 223 | 43,05% | 1,00 | 0,00R | €2,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 4 | 208 | 208 | 41,35% | 0,98 | -0,01R | €-18,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 49 | 49 | 26,53% | 0,30 | -0,45R | €-220,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 7 | 7 | 71,43% | 2,09 | 0,32R | €22,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 68 | 68 | 36,76% | 1,38 | 0,16R | €105,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 60 | 60 | 26,67% | 0,55 | -0,26R | €-153,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 68 | 68 | 20,59% | 0,43 | -0,31R | €-208,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 3 | 118 | 118 | 31,36% | 0,57 | -0,25R | €-297,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 4 | 203 | 203 | 41,38% | 0,97 | -0,01R | €-30,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 4 | 199 | 199 | 40,70% | 0,86 | -0,07R | €-136,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 25,53% | 0,28 | -0,47R | €-219,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 5,17 | 0,70R | €42,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 67 | 67 | 37,31% | 1,37 | 0,15R | €99,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 56 | 56 | 25,00% | 0,52 | -0,27R | €-151,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 64 | 64 | 23,44% | 0,45 | -0,30R | €-189,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 17 | 17 | 41,18% | 0,64 | -0,22R | €-37,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 1 | 122 | 122 | 46,72% | 0,94 | -0,03R | €-37,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 113 | 113 | 46,02% | 0,83 | -0,09R | €-105,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 42 | 42 | 64,29% | 2,20 | 0,39R | €163,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 52 | 52 | 42,31% | 0,69 | -0,16R | €-85,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 31,25% | 0,65 | -0,21R | €-33,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 1 | 125 | 125 | 37,60% | 0,83 | -0,09R | €-115,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 118 | 118 | 41,53% | 0,91 | -0,05R | €-53,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 42 | 42 | 38,10% | 1,86 | 0,26R | €109,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 52 | 52 | 26,92% | 0,64 | -0,17R | €-87,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,81 | -0,08R | €-45,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 4 | 258 | 258 | 38,76% | 0,82 | -0,09R | €-242,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 2 | 153 | 153 | 40,52% | 0,95 | -0,03R | €-39,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 72 | 72 | 30,56% | 0,72 | -0,14R | €-101,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 54 | 54 | 31,48% | 0,76 | -0,11R | €-57,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 4 | 237 | 237 | 37,97% | 0,84 | -0,09R | €-213,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 2 | 140 | 140 | 42,14% | 0,91 | -0,05R | €-63,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,59 | -0,24R | €-73,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 57 | 57 | 42,11% | 1,81 | 0,26R | €145,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 38 | 38 | 31,58% | 0,61 | -0,21R | €-81,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 66 | 66 | 31,82% | 0,62 | -0,19R | €-124,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 240 | 240 | 39,17% | 0,90 | -0,05R | €-116,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 3 | 58 | 58 | 37,93% | 0,62 | -0,24R | €-137,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 3 | 145 | 145 | 35,17% | 0,73 | -0,16R | €-236,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 210 | 210 | 40,48% | 0,97 | -0,02R | €-34,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 50 | 50 | 36,00% | 1,35 | 0,14R | €69,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 57 | 57 | 26,32% | 0,62 | -0,20R | €-116,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 3 | 99 | 99 | 33,33% | 0,60 | -0,24R | €-241,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 3 | 159 | 159 | 35,22% | 0,74 | -0,15R | €-236,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 5 | 261 | 261 | 40,23% | 0,96 | -0,02R | €-46,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 68 | 68 | 33,82% | 1,20 | 0,08R | €53,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 89 | 89 | 25,84% | 0,61 | -0,20R | €-180,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 3 | 93 | 93 | 31,18% | 0,53 | -0,30R | €-281,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 4 | 142 | 142 | 33,10% | 0,69 | -0,19R | €-274,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 5 | 247 | 247 | 39,68% | 0,87 | -0,06R | €-154,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 67 | 67 | 34,33% | 1,14 | 0,05R | €36,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 83 | 83 | 26,51% | 0,52 | -0,25R | €-209,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,81 | -0,08R | €-45,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 4 | 259 | 259 | 39,00% | 0,84 | -0,09R | €-222,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 2 | 153 | 153 | 41,83% | 1,03 | 0,01R | €19,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 72 | 72 | 30,56% | 0,72 | -0,14R | €-101,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 3 | 196 | 196 | 37,24% | 0,63 | -0,19R | €-373,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 5 | 314 | 314 | 40,76% | 0,89 | -0,05R | €-161,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 4 | 290 | 290 | 41,72% | 0,99 | -0,00R | €-12,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 67 | 67 | 38,81% | 0,48 | -0,29R | €-193,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 8 | 8 | 50,00% | 0,84 | -0,08R | €-6,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 89 | 89 | 47,19% | 1,55 | 0,17R | €151,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 92 | 92 | 38,04% | 0,78 | -0,09R | €-85,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,59 | -0,12R | €-5,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 102 | 102 | 38,24% | 0,71 | -0,14R | €-147,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 64 | 64 | 43,75% | 0,82 | -0,11R | €-67,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 2 | 68 | 68 | 33,82% | 0,65 | -0,22R | €-152,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 109 | 109 | 44,04% | 0,82 | -0,09R | €-99,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 15 | 15 | 60,00% | 1,97 | 0,42R | €63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 15 | 15 | 33,33% | 0,56 | -0,20R | €-30,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 33 | 33 | 21,21% | 0,31 | -0,50R | €-164,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 3 | 166 | 166 | 28,92% | 0,56 | -0,25R | €-418,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 5 | 274 | 274 | 38,69% | 0,85 | -0,08R | €-222,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 4 | 253 | 253 | 39,53% | 0,94 | -0,03R | €-79,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 88 | 88 | 25,00% | 0,57 | -0,23R | €-200,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 3 | 166 | 166 | 28,92% | 0,56 | -0,25R | €-418,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 5 | 276 | 276 | 38,77% | 0,85 | -0,08R | €-212,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 4 | 254 | 254 | 39,37% | 0,93 | -0,04R | €-89,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 88 | 88 | 25,00% | 0,57 | -0,23R | €-200,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 3 | 156 | 156 | 28,21% | 0,53 | -0,28R | €-438,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 5 | 251 | 251 | 38,25% | 0,86 | -0,08R | €-195,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 4 | 241 | 241 | 38,59% | 0,81 | -0,09R | €-220,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 61 | 61 | 31,15% | 0,49 | -0,29R | €-179,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,45 | 0,17R | €133,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 82 | 82 | 25,61% | 0,47 | -0,29R | €-234,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 7 | 42 | 42 | 28,57% | 0,77 | -0,14R | €-57,07 |
| MAIN | ALT_ROTATION_UP | 4 | 117 | 117 | 30,77% | 0,63 | -0,24R | €-281,61 |
| MAIN | RANGE | 4 | 105 | 105 | 29,52% | 0,82 | -0,11R | €-114,02 |
| MAIN | RANGE_HIGH_VOL | 4 | 25 | 25 | 20,00% | 0,58 | -0,24R | €-60,56 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 2 | 43 | 43 | 30,23% | 0,83 | -0,10R | €-42,41 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,96 | 0,48R | €19,39 |
| MAIN | TREND_UP | 2 | 48 | 48 | 29,17% | 0,93 | -0,04R | €-19,03 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 25 | 25 | 32,00% | 0,13 | -0,59R | €-146,37 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 100,00% | ∞ | 1,09R | €32,57 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 25 | 25 | 44,00% | 0,92 | -0,04R | €-9,44 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 12 | 12 | 41,67% | 0,85 | -0,08R | €-10,11 |
| RSI_EXTREME_SHORT_15M | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,32R | €13,24 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 7 | 157 | 157 | 30,57% | 0,57 | -0,27R | €-431,26 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 7 | 291 | 291 | 41,92% | 0,96 | -0,03R | €-74,16 |
| Bilanciata 1H V1 | RANGE | 9 | 289 | 289 | 41,87% | 1,00 | -0,00R | €-0,32 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 2 | 73 | 73 | 30,14% | 0,49 | -0,33R | €-238,79 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-2,77 |
| Bilanciata 1H V1 | TRANSITION | 0 | 117 | 117 | 37,61% | 1,08 | 0,04R | €48,40 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 89 | 89 | 31,46% | 0,75 | -0,13R | €-113,61 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 50,00% | 1,44 | 0,24R | €14,27 |
| Bilanciata 1H V1 | TREND_UP | 0 | 128 | 128 | 32,03% | 0,91 | -0,05R | €-59,38 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 5 | 164 | 139 | 46,95% | 1,24 | 0,12R | €201,90 |
| Bilanciata 1H V2 | RANGE | 6 | 214 | 191 | 38,32% | 0,83 | -0,09R | €-201,04 |
| Bilanciata 1H V2 | TRANSITION | 0 | 97 | 84 | 39,18% | 1,21 | 0,11R | €102,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 116 | 116 | 28,45% | 0,50 | -0,33R | €-377,44 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 3 | 185 | 185 | 42,16% | 1,00 | 0,00R | €4,44 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 194 | 194 | 44,33% | 1,09 | 0,05R | €88,01 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 37 | 37 | 27,03% | 0,41 | -0,37R | €-138,27 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 64 | 64 | 37,50% | 1,15 | 0,07R | €44,08 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,10 | 0,06R | €4,35 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 75 | 75 | 34,67% | 1,13 | 0,06R | €47,35 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 105 | 105 | 26,67% | 0,41 | -0,39R | €-410,81 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 183 | 183 | 42,62% | 1,02 | 0,01R | €25,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 6 | 172 | 172 | 43,60% | 0,97 | -0,02R | €-28,15 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 35 | 35 | 28,57% | 0,45 | -0,34R | €-117,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 56 | 56 | 37,50% | 1,16 | 0,07R | €38,40 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,10 | 0,06R | €4,35 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 31,48% | 0,95 | -0,02R | €-13,49 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 22,58% | 0,49 | -0,26R | €-80,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 126 | 126 | 38,89% | 0,81 | -0,10R | €-124,28 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 82 | 82 | 43,90% | 1,05 | 0,03R | €20,62 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,18 | -0,71R | €-135,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 45,95% | 1,50 | 0,20R | €74,56 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 63 | 63 | 33,33% | 0,87 | -0,06R | €-35,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 86 | 86 | 40,70% | 0,97 | -0,01R | €-12,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 2 | 173 | 173 | 40,46% | 0,88 | -0,06R | €-107,59 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 7 | 272 | 272 | 41,18% | 0,99 | -0,00R | €-11,81 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 78 | 78 | 39,74% | 1,13 | 0,05R | €41,79 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 97 | 97 | 29,90% | 0,75 | -0,12R | €-114,38 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 104 | 104 | 37,50% | 0,83 | -0,09R | €-94,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 174 | 174 | 40,80% | 0,90 | -0,05R | €-93,70 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 7 | 302 | 302 | 43,05% | 1,09 | 0,04R | €133,38 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 80 | 80 | 41,25% | 1,23 | 0,09R | €71,48 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 113 | 113 | 29,20% | 0,68 | -0,17R | €-186,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 5 | 203 | 203 | 30,54% | 0,62 | -0,22R | €-450,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 7 | 339 | 339 | 39,53% | 0,82 | -0,10R | €-330,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 6 | 342 | 342 | 41,52% | 1,00 | 0,00R | €6,92 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 75 | 75 | 38,67% | 0,66 | -0,19R | €-143,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 54,55% | 1,45 | 0,17R | €18,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 109 | 109 | 42,20% | 1,33 | 0,13R | €141,25 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 104 | 104 | 29,81% | 0,64 | -0,19R | €-202,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,66 | -0,15R | €-7,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 128 | 128 | 28,91% | 0,70 | -0,16R | €-204,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 50 | 50 | 46,00% | 1,46 | 0,17R | €87,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 119 | 119 | 32,77% | 0,61 | -0,23R | €-274,27 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 2 | 202 | 202 | 41,58% | 0,95 | -0,03R | €-54,23 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 190 | 190 | 45,79% | 1,24 | 0,11R | €210,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 40 | 40 | 35,00% | 0,41 | -0,36R | €-143,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 100,00% | ∞ | 0,89R | €62,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 61 | 61 | 42,62% | 1,60 | 0,20R | €120,86 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,34 | -0,47R | €-28,15 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 75 | 75 | 28,00% | 0,62 | -0,21R | €-159,54 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 203 | 203 | 28,57% | 0,61 | -0,23R | €-469,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 6 | 336 | 336 | 39,58% | 0,88 | -0,06R | €-216,32 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 6 | 318 | 318 | 40,25% | 0,99 | -0,01R | €-16,95 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 77 | 77 | 32,47% | 0,53 | -0,26R | €-203,44 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 50,00% | 1,49 | 0,20R | €20,16 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 104 | 104 | 39,42% | 1,35 | 0,14R | €146,34 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 98 | 98 | 29,59% | 0,67 | -0,18R | €-179,94 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,21 | -0,35R | €-17,65 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 118 | 118 | 22,88% | 0,51 | -0,27R | €-318,56 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 38 | 34 | 47,37% | 0,96 | -0,02R | €-8,67 |
| Rapida 1H V2 | RANGE | 0 | 73 | 62 | 42,47% | 0,95 | -0,03R | €-19,03 |
| Rapida 1H V2 | TRANSITION | 0 | 11 | 11 | 63,64% | 1,79 | 0,25R | €27,27 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 195 | 195 | 30,26% | 0,56 | -0,26R | €-504,90 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 5 | 306 | 306 | 40,85% | 0,89 | -0,06R | €-170,33 |
| Rapida 1H V3 Filtered | RANGE | 4 | 306 | 306 | 40,52% | 0,97 | -0,02R | €-47,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 70 | 70 | 38,57% | 0,60 | -0,23R | €-158,07 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 94 | 94 | 40,43% | 1,27 | 0,11R | €104,32 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 126 | 126 | 36,51% | 0,94 | -0,03R | €-37,80 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 61 | 61 | 36,07% | 0,87 | -0,07R | €-42,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 3 | 150 | 150 | 33,33% | 0,62 | -0,22R | €-324,13 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 2 | 242 | 242 | 44,21% | 1,01 | 0,01R | €15,06 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 240 | 240 | 42,08% | 1,05 | 0,02R | €56,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 1 | 55 | 55 | 32,73% | 0,41 | -0,38R | €-206,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 87,50% | 6,12 | 0,65R | €51,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,26 | 0,11R | €75,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 66 | 66 | 27,27% | 0,61 | -0,22R | €-144,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,45 | -0,30R | €-18,15 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 86 | 86 | 29,07% | 0,64 | -0,20R | €-171,36 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,29 | -0,52R | €-125,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 1 | 133 | 133 | 48,12% | 0,94 | -0,03R | €-43,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 131 | 131 | 47,33% | 1,04 | 0,02R | €27,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 43 | 43 | 65,12% | 2,22 | 0,36R | €154,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 63 | 63 | 47,62% | 0,91 | -0,05R | €-28,47 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 21,74% | 0,28 | -0,52R | €-120,49 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 135 | 135 | 38,52% | 0,85 | -0,08R | €-109,03 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 135 | 135 | 44,44% | 1,13 | 0,07R | €89,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 43 | 43 | 44,19% | 1,85 | 0,26R | €109,67 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 65 | 65 | 32,31% | 0,78 | -0,11R | €-69,36 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 66 | 66 | 25,76% | 0,48 | -0,27R | €-180,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 290 | 290 | 40,34% | 0,87 | -0,07R | €-200,81 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 177 | 177 | 42,94% | 1,06 | 0,03R | €48,89 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 36,36% | 0,66 | -0,20R | €-64,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 62 | 62 | 46,77% | 1,73 | 0,25R | €153,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 0,81 | -0,10R | €-49,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 47,80 | 0,48R | €14,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 85 | 85 | 34,12% | 0,83 | -0,09R | €-72,37 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 43,59% | 1,23 | 0,10R | €40,01 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 122 | 122 | 33,61% | 0,60 | -0,24R | €-294,86 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 2 | 175 | 175 | 37,14% | 0,78 | -0,13R | €-219,70 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 5 | 315 | 315 | 41,90% | 1,03 | 0,01R | €46,93 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 74 | 74 | 39,19% | 1,32 | 0,12R | €87,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 112 | 112 | 32,14% | 0,76 | -0,13R | €-142,98 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 194 | 194 | 30,41% | 0,56 | -0,25R | €-493,47 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 5 | 305 | 305 | 40,33% | 0,87 | -0,07R | €-211,45 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 304 | 304 | 40,46% | 0,96 | -0,02R | €-62,60 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 69 | 69 | 39,13% | 0,61 | -0,21R | €-147,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 89 | 89 | 40,45% | 1,31 | 0,12R | €107,09 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 109 | 109 | 31,19% | 0,73 | -0,15R | €-160,54 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 41 | 41 | 41,46% | 1,16 | 0,07R | €29,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 9 | 40 | 40 | 27,50% | 1,02 | 0,01R | €5,72 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 5 | 100 | 100 | 33,00% | 0,85 | -0,10R | €-97,49 |
| SHADOW_4H_WIDE | RANGE | 7 | 96 | 96 | 18,75% | 0,66 | -0,22R | €-214,50 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 4 | 19 | 19 | 15,79% | 0,68 | -0,21R | €-39,15 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 44 | 44 | 20,45% | 0,59 | -0,28R | €-121,03 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,37 | 0,19R | €7,47 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 46 | 46 | 28,26% | 1,22 | 0,13R | €57,78 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 2 | 20 | 20 | 25,00% | 0,80 | -0,13R | €-25,04 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 2 | 55 | 55 | 43,64% | 0,80 | -0,11R | €-60,18 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 131 | 131 | 51,15% | 1,20 | 0,08R | €108,94 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 102 | 102 | 49,02% | 0,97 | -0,02R | €-16,51 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 16 | 16 | 50,00% | 1,36 | 0,15R | €23,95 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 19 | 19 | 52,63% | 1,52 | 0,23R | €44,43 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 45 | 45 | 42,22% | 0,85 | -0,07R | €-33,39 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 45,00% | 1,00 | 0,00R | €0,09 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 50,00% | 0,93 | -0,03R | €-2,49 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 50,00% | 0,45 | -0,31R | €-24,46 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,32 | 0,69R | €13,75 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,14 | 0,07R | €3,26 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,17 | -0,47R | €-9,40 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 2,22 | 0,45R | €13,43 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,65R | €6,51 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,45 | -0,38R | €-30,72 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,41 | -0,38R | €-34,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 25,00% | 0,85 | -0,12R | €-4,85 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,38 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,27 | -0,64R | €-51,33 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,27 | -0,48R | €-24,20 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 10 | 10 | 60,00% | 1,24 | 0,11R | €10,80 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,66 | -0,18R | €-3,69 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,10 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 8 | 136 | 136 | 33,09% | 0,70 | -0,18R | €-250,79 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 7 | 240 | 240 | 42,08% | 0,97 | -0,02R | €-39,18 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 241 | 241 | 44,81% | 0,94 | -0,03R | €-73,87 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 58 | 58 | 34,48% | 0,53 | -0,26R | €-153,32 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,95 | -0,03R | €-3,06 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 92 | 92 | 42,39% | 1,23 | 0,11R | €98,46 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 76 | 76 | 35,53% | 0,95 | -0,02R | €-18,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,61 | 0,91R | €36,57 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 106 | 106 | 37,74% | 1,09 | 0,04R | €41,55 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 47 | 47 | 31,91% | 0,81 | -0,11R | €-50,70 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 8 | 230 | 230 | 41,30% | 0,92 | -0,05R | €-110,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 3 | 133 | 133 | 46,62% | 0,98 | -0,01R | €-14,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 23 | 23 | 30,43% | 0,38 | -0,37R | €-86,15 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 53 | 53 | 47,17% | 1,65 | 0,22R | €114,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 45 | 45 | 37,78% | 1,22 | 0,10R | €44,99 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,16 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 65 | 65 | 32,31% | 0,68 | -0,15R | €-98,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 7 | 164 | 164 | 35,98% | 0,74 | -0,13R | €-207,92 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 8 | 282 | 282 | 37,94% | 0,88 | -0,06R | €-173,92 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 255 | 255 | 42,35% | 1,08 | 0,04R | €91,71 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 66 | 66 | 34,85% | 0,49 | -0,26R | €-171,59 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,51 | -0,30R | €-35,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 84 | 84 | 45,24% | 1,22 | 0,09R | €71,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 100 | 100 | 38,00% | 0,96 | -0,02R | €-16,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 3,69 | 0,68R | €27,30 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 109 | 109 | 50,46% | 1,27 | 0,11R | €121,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 8 | 136 | 136 | 33,09% | 0,71 | -0,18R | €-242,19 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 7 | 238 | 238 | 42,44% | 0,93 | -0,04R | €-103,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 229 | 229 | 47,16% | 1,00 | -0,00R | €-3,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 56 | 56 | 37,50% | 0,63 | -0,20R | €-113,63 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,75 | -0,16R | €-15,75 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 75 | 75 | 46,67% | 1,21 | 0,09R | €70,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 76 | 76 | 39,47% | 0,96 | -0,02R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,07 | 0,78R | €31,07 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 85 | 85 | 38,82% | 0,78 | -0,10R | €-87,22 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,97 | -0,01R | €-6,60 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 38 | 38 | 52,63% | 1,53 | 0,20R | €77,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 57,89% | 2,69 | 0,47R | €88,74 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,88 | -0,06R | €-26,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 38 | 38 | 42,11% | 1,37 | 0,14R | €54,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 3,13 | 0,59R | €112,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 4 | 43 | 43 | 37,21% | 0,74 | -0,14R | €-59,10 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 4 | 106 | 106 | 40,57% | 0,79 | -0,13R | €-136,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 76 | 76 | 36,84% | 0,79 | -0,13R | €-96,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 3 | 14 | 14 | 42,86% | 1,01 | 0,00R | €0,68 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 39 | 39 | 41,03% | 0,90 | -0,05R | €-19,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 26 | 26 | 38,46% | 1,17 | 0,06R | €15,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 110 | 110 | 41,82% | 1,06 | 0,03R | €30,23 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 125 | 125 | 36,80% | 0,78 | -0,11R | €-133,30 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 51 | 51 | 49,02% | 1,43 | 0,21R | €105,99 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 33 | 33 | 36,36% | 0,65 | -0,17R | €-57,65 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 1,21 | 0,11R | €23,55 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 53 | 53 | 45,28% | 0,87 | -0,07R | €-37,33 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 10 | 10 | 20,00% | 0,44 | -0,38R | €-38,09 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 8 | 8 | 62,50% | 2,67 | 0,46R | €36,75 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 17 | 17 | 58,82% | 1,72 | 0,23R | €38,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 50 | 50 | 26,00% | 0,48 | -0,36R | €-178,40 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 6 | 191 | 191 | 40,31% | 0,98 | -0,01R | €-22,46 |
| SHADOW_COMBO_SCANNER | RANGE | 5 | 144 | 144 | 43,75% | 1,07 | 0,03R | €49,88 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 24 | 24 | 37,50% | 0,41 | -0,34R | €-82,14 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 72 | 72 | 43,06% | 1,49 | 0,22R | €160,17 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 45 | 45 | 31,11% | 0,82 | -0,10R | €-45,10 |
| SHADOW_COMBO_SCANNER | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 72 | 72 | 31,94% | 1,09 | 0,04R | €31,62 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 7 | 106 | 106 | 29,25% | 0,55 | -0,30R | €-312,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 4 | 212 | 212 | 41,04% | 0,96 | -0,02R | €-46,17 |
| SHADOW_COMBO_TREND | RANGE | 6 | 201 | 201 | 38,81% | 1,06 | 0,03R | €61,92 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 3 | 42 | 42 | 38,10% | 0,89 | -0,06R | €-24,55 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 76 | 76 | 36,84% | 1,15 | 0,08R | €60,00 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 68 | 68 | 30,88% | 0,76 | -0,13R | €-86,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 1,61 | 0,21R | €6,21 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 82 | 82 | 31,71% | 1,04 | 0,02R | €15,16 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,62 | -0,21R | €-12,31 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 6 | 6 | 66,67% | 3,84 | 0,56R | €33,45 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 9 | 9 | 55,56% | 0,84 | -0,08R | €-7,12 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,15 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 25,00% | 0,33 | -0,56R | €-44,78 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,14 | -0,73R | €-36,57 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,92 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,75 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,08 | -0,74R | €-81,45 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 18,18% | 0,41 | -0,51R | €-56,27 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 13 | 13 | 46,15% | 1,23 | 0,12R | €15,53 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 4 | 4 | 100,00% | ∞ | 0,81R | €32,50 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 72 | 72 | 29,17% | 0,55 | -0,31R | €-225,72 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 115 | 115 | 32,17% | 0,64 | -0,26R | €-299,78 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 108 | 108 | 41,67% | 1,14 | 0,08R | €86,09 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 16 | 16 | 50,00% | 1,82 | 0,38R | €60,21 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 33 | 33 | 39,39% | 1,29 | 0,15R | €48,35 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 22 | 22 | 27,27% | 0,43 | -0,41R | €-89,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 43 | 43 | 30,23% | 1,15 | 0,07R | €32,24 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 54,17% | 1,90 | 0,44R | €104,71 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 62 | 62 | 29,03% | 0,46 | -0,38R | €-234,20 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 107 | 107 | 33,64% | 0,67 | -0,23R | €-249,37 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 88 | 88 | 44,32% | 1,16 | 0,08R | €71,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,52 | 0,57R | €80,48 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 26 | 26 | 46,15% | 1,68 | 0,30R | €77,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 20 | 20 | 30,00% | 0,46 | -0,40R | €-79,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 29 | 29 | 27,59% | 1,04 | 0,02R | €5,27 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,36 | 0,56R | €99,93 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 7 | 113 | 113 | 28,32% | 0,50 | -0,34R | €-379,95 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 4 | 217 | 217 | 41,01% | 0,95 | -0,03R | €-61,92 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 194 | 194 | 37,63% | 1,01 | 0,00R | €8,92 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 3 | 44 | 44 | 38,64% | 1,03 | 0,02R | €6,78 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 72 | 72 | 34,72% | 1,04 | 0,02R | €17,55 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,51 | -0,34R | €-10,34 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 89 | 89 | 29,21% | 0,86 | -0,08R | €-68,04 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 27,27% | 0,48 | -0,41R | €-45,03 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 10 | 10 | 30,00% | 0,38 | -0,48R | €-48,41 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,00 | -0,71R | €-21,28 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 70,00% | 4,04 | 0,66R | €65,54 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 66,67% | 1,30 | 0,11R | €3,44 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,39 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,21 | -0,60R | €-18,01 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,64 | -0,20R | €-3,91 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 22,22% | 0,30 | -0,59R | €-53,47 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,77 | -0,15R | €-13,41 |
| SHADOW_ETH_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,20 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,67 | 0,37R | €7,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 19 | 19 | 42,11% | 0,56 | -0,25R | €-48,22 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,25 | -0,55R | €-49,78 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,43 | -0,49R | €-24,67 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,64 | -0,19R | €-7,65 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,04R | €-10,39 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,35R | €3,51 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 10 | 10 | 40,00% | 0,80 | -0,13R | €-13,34 |
| SHADOW_GLOBAL_PURE | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,59R | €15,85 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 2 | 29 | 29 | 37,93% | 1,23 | 0,14R | €41,10 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 6 | 81 | 81 | 33,33% | 0,89 | -0,08R | €-65,72 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 4 | 144 | 144 | 29,86% | 0,85 | -0,10R | €-149,95 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 46 | 46 | 47,83% | 1,97 | 0,46R | €212,56 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 50 | 50 | 38,00% | 1,29 | 0,17R | €82,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 1 | 71 | 71 | 29,58% | 0,85 | -0,11R | €-74,81 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 49 | 49 | 59,18% | 1,01 | 0,01R | €2,65 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 5 | 176 | 176 | 65,91% | 1,20 | 0,07R | €120,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 268 | 268 | 66,04% | 1,26 | 0,08R | €221,24 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 100 | 100 | 73,00% | 1,75 | 0,18R | €181,85 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 78 | 78 | 64,10% | 1,36 | 0,12R | €94,03 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 132 | 132 | 60,61% | 0,99 | -0,00R | €-5,71 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 37,04% | 1,27 | 0,16R | €41,91 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 6 | 146 | 146 | 30,82% | 0,89 | -0,08R | €-110,85 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 46 | 46 | 45,65% | 1,79 | 0,40R | €182,06 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 45 | 45 | 40,00% | 1,37 | 0,21R | €96,58 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 82 | 82 | 25,61% | 0,69 | -0,23R | €-188,38 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 24 | 24 | 45,83% | 1,84 | 0,44R | €104,54 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 6 | 85 | 85 | 30,59% | 0,79 | -0,16R | €-138,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 129 | 129 | 31,01% | 0,97 | -0,02R | €-21,82 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 41 | 41 | 43,90% | 1,70 | 0,36R | €145,68 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 40,48% | 1,42 | 0,24R | €100,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 67 | 67 | 25,37% | 0,71 | -0,21R | €-142,89 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 22,22% | 0,59 | -0,31R | €-55,21 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 4 | 100 | 100 | 31,00% | 0,86 | -0,10R | €-101,93 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 36 | 36 | 47,22% | 2,12 | 0,49R | €176,16 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,75 | -0,18R | €-106,89 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 37,04% | 1,20 | 0,12R | €32,04 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 6 | 83 | 83 | 33,73% | 0,90 | -0,07R | €-58,25 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 4 | 135 | 135 | 31,85% | 0,94 | -0,04R | €-53,96 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 45 | 45 | 44,44% | 1,71 | 0,36R | €162,62 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 43 | 43 | 39,53% | 1,35 | 0,20R | €86,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 1 | 70 | 70 | 25,71% | 0,70 | -0,22R | €-153,22 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 8 | 131 | 131 | 32,06% | 0,62 | -0,24R | €-307,86 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 5 | 239 | 239 | 38,91% | 0,92 | -0,05R | €-120,88 |
| Forza relativa 1H V1 | RANGE | 10 | 252 | 252 | 33,73% | 0,80 | -0,11R | €-280,43 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 3 | 48 | 48 | 27,08% | 0,45 | -0,35R | €-170,03 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 11 | 11 | 27,27% | 0,72 | -0,18R | €-19,83 |
| Forza relativa 1H V1 | TRANSITION | 1 | 91 | 91 | 39,56% | 1,38 | 0,18R | €168,06 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 78 | 78 | 29,49% | 0,95 | -0,02R | €-19,05 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 1 | 3 | 3 | 100,00% | ∞ | 1,66R | €49,91 |
| Forza relativa 1H V1 | TREND_UP | 0 | 108 | 108 | 27,78% | 0,92 | -0,04R | €-43,00 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 34 | 34 | 26,47% | 0,77 | -0,15R | €-50,36 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 5 | 62 | 60 | 43,55% | 0,84 | -0,08R | €-50,02 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 4 | 100 | 92 | 42,00% | 1,09 | 0,06R | €56,66 |
| Forza relativa 1H V2 | RANGE | 7 | 113 | 107 | 31,86% | 0,73 | -0,16R | €-183,75 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 8 | 7 | 25,00% | 0,66 | -0,18R | €-14,36 |
| Forza relativa 1H V2 | TRANSITION | 0 | 49 | 44 | 40,82% | 1,54 | 0,25R | €122,15 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 36 | 35 | 27,78% | 0,89 | -0,05R | €-17,72 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 40,00% | 0,92 | -0,05R | €-2,35 |
| Forza relativa 1H V2 | TREND_UP | 0 | 42 | 38 | 47,62% | 1,81 | 0,36R | €152,91 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 6 | 94 | 94 | 23,40% | 0,34 | -0,48R | €-449,04 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 4 | 103 | 103 | 37,86% | 0,71 | -0,14R | €-139,33 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 6 | 94 | 94 | 23,40% | 0,34 | -0,48R | €-449,04 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 4 | 103 | 103 | 37,86% | 0,71 | -0,14R | €-139,33 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 6 | 94 | 94 | 23,40% | 0,34 | -0,48R | €-449,04 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 4 | 103 | 103 | 37,86% | 0,71 | -0,14R | €-139,33 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 6 | 81 | 81 | 24,69% | 0,42 | -0,41R | €-331,93 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 19 | 19 | 47,37% | 1,74 | 0,29R | €54,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 116 | 116 | 37,93% | 0,88 | -0,06R | €-68,89 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 30 | 30 | 46,67% | 1,14 | 0,06R | €17,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 42 | 42 | 38,10% | 1,01 | 0,01R | €2,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 6 | 100 | 100 | 45,00% | 0,51 | -0,27R | €-267,53 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,32 | 0,15R | €20,41 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 3 | 132 | 132 | 62,88% | 0,99 | -0,00R | €-4,42 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 35 | 35 | 62,86% | 1,17 | 0,07R | €23,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 33 | 33 | 57,58% | 1,30 | 0,13R | €44,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 68 | 68 | 52,94% | 0,63 | -0,16R | €-108,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,62 | -0,21R | €-8,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 6 | 81 | 81 | 40,74% | 0,39 | -0,35R | €-285,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 52,94% | 1,61 | 0,23R | €38,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 3 | 120 | 120 | 64,17% | 0,92 | -0,03R | €-33,92 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 34 | 34 | 58,82% | 0,96 | -0,02R | €-6,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 32 | 32 | 59,38% | 1,50 | 0,21R | €67,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 57 | 57 | 50,88% | 0,60 | -0,18R | €-103,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,37 | -0,35R | €-14,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,49 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 6 | 245 | 245 | 40,00% | 0,86 | -0,08R | €-197,24 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 24 | 24 | 25,00% | 0,43 | -0,38R | €-91,58 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 6 | 249 | 249 | 40,56% | 0,87 | -0,07R | €-186,54 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 24 | 24 | 25,00% | 0,43 | -0,38R | €-91,58 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 6 | 249 | 249 | 40,56% | 0,87 | -0,07R | €-186,54 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 24 | 24 | 25,00% | 0,43 | -0,38R | €-91,58 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 46 | 46 | 28,26% | 0,55 | -0,29R | €-134,71 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 6 | 189 | 189 | 40,21% | 0,97 | -0,02R | €-31,82 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 5 | 133 | 133 | 43,61% | 1,09 | 0,04R | €59,62 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 21 | 21 | 28,57% | 0,33 | -0,44R | €-93,11 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 67 | 67 | 41,79% | 1,48 | 0,22R | €145,48 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 71 | 71 | 30,99% | 1,03 | 0,02R | €10,91 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,18 | -0,67R | €-119,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 1 | 82 | 82 | 30,49% | 0,54 | -0,34R | €-277,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 1 | 12 | 12 | 41,67% | 0,44 | -0,35R | €-41,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,27 | -0,58R | €-23,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 30 | 30 | 53,33% | 2,17 | 0,40R | €120,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 58 | 58 | 29,31% | 0,86 | -0,07R | €-42,83 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 27,50% | 0,53 | -0,30R | €-120,90 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 4 | 102 | 102 | 30,39% | 0,55 | -0,31R | €-318,11 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 6 | 129 | 129 | 42,64% | 0,99 | -0,00R | €-6,12 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 30,00% | 0,35 | -0,41R | €-82,42 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 2,10 | 0,38R | €193,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 52 | 52 | 23,08% | 0,59 | -0,24R | €-122,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 32,43% | 0,69 | -0,14R | €-50,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 4 | 101 | 101 | 34,65% | 0,63 | -0,20R | €-206,05 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 5 | 156 | 156 | 43,59% | 1,08 | 0,04R | €58,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 1,28 | 0,11R | €54,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 53 | 53 | 50,94% | 1,34 | 0,14R | €72,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 57,14% | 1,17 | 0,07R | €5,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 33,33% | 0,62 | -0,22R | €-67,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 81 | 81 | 32,10% | 0,64 | -0,25R | €-203,82 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 6 | 133 | 133 | 43,61% | 1,02 | 0,01R | €13,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 24 | 24 | 29,17% | 0,31 | -0,46R | €-110,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 46 | 46 | 39,13% | 1,52 | 0,21R | €97,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 26,83% | 0,78 | -0,12R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,42 | -0,37R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 37,78% | 0,83 | -0,08R | €-35,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 6 | 194 | 194 | 40,72% | 0,93 | -0,03R | €-63,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 157 | 157 | 43,95% | 1,10 | 0,05R | €71,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 57 | 57 | 43,86% | 1,25 | 0,09R | €51,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 60 | 60 | 50,00% | 1,33 | 0,13R | €78,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 36 | 36 | 33,33% | 0,67 | -0,20R | €-71,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 4 | 158 | 158 | 43,04% | 1,10 | 0,06R | €92,43 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 5 | 132 | 132 | 43,94% | 1,04 | 0,02R | €26,09 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 1 | 24 | 24 | 29,17% | 0,31 | -0,46R | €-110,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 51 | 51 | 39,22% | 1,34 | 0,15R | €73,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 46 | 46 | 26,09% | 0,80 | -0,10R | €-48,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 56 | 56 | 35,71% | 0,70 | -0,14R | €-78,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 8 | 225 | 225 | 39,11% | 0,82 | -0,09R | €-200,56 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 148 | 148 | 44,59% | 1,11 | 0,05R | €73,98 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,45 | -0,26R | €-78,43 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 65 | 65 | 44,62% | 1,28 | 0,10R | €67,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 58 | 58 | 44,83% | 1,01 | 0,00R | €1,84 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 73 | 73 | 49,32% | 1,28 | 0,11R | €78,63 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 39 | 39 | 33,33% | 0,67 | -0,21R | €-80,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 6 | 190 | 190 | 40,00% | 0,98 | -0,01R | €-23,04 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 5 | 124 | 124 | 41,94% | 1,02 | 0,01R | €14,43 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 30,00% | 0,35 | -0,41R | €-82,92 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 55 | 55 | 40,00% | 1,41 | 0,18R | €99,29 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 43 | 43 | 30,23% | 0,87 | -0,07R | €-31,88 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,08 | 0,55R | €10,95 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 54 | 54 | 24,07% | 0,68 | -0,17R | €-91,68 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 32,43% | 0,69 | -0,20R | €-72,22 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 7 | 180 | 180 | 38,89% | 0,94 | -0,04R | €-64,89 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 119 | 119 | 42,02% | 1,06 | 0,03R | €41,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 30,00% | 0,31 | -0,44R | €-88,35 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 49 | 49 | 38,78% | 1,59 | 0,24R | €116,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,93 | -0,04R | €-14,25 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,23 | 0,12R | €2,31 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 53 | 53 | 26,42% | 0,73 | -0,13R | €-70,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 53 | 53 | 32,08% | 0,69 | -0,18R | €-97,82 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 6 | 198 | 198 | 39,90% | 0,90 | -0,06R | €-113,04 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 141 | 141 | 44,68% | 1,06 | 0,03R | €42,81 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 26 | 26 | 23,08% | 0,38 | -0,43R | €-112,40 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 70 | 70 | 41,43% | 1,43 | 0,18R | €124,25 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 92 | 92 | 38,04% | 1,14 | 0,07R | €59,88 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,10 | -0,84R | €-75,50 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 58,33% | 1,98 | 0,44R | €53,24 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 11 | 11 | 54,55% | 1,00 | -0,00R | €-0,06 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,82 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,86 | -0,10R | €-3,05 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 3,31 | 0,60R | €23,94 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 71,43% | 1,78 | 0,24R | €17,02 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,42 | -0,40R | €-44,47 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,53 | -0,33R | €-26,28 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 11,45 | 0,62R | €12,47 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,97 | -0,01R | €-0,27 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 28,57% | 0,26 | -0,59R | €-41,10 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 44,44% | 1,33 | 0,16R | €14,69 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 10 | 10 | 70,00% | 2,18 | 0,40R | €39,82 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,62 | 0,84R | €16,82 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,60 | -0,28R | €-8,29 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,08 | -0,85R | €-76,70 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 58,33% | 1,98 | 0,44R | €53,30 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 11 | 11 | 36,36% | 0,78 | -0,16R | €-17,14 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,82 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,29 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,91 | -0,05R | €-1,98 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-17T13:34:19+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **221**
- Scenari virtuali ancora attivi: **7628**
- Gruppi in attesa dell'uscita originale: **174**
- Gruppi con originale chiuso ma Shadow ancora attive: **47**
- Confronti completati: **649871**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ATR10_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR30_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A020 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A030 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A040 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A060 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A075 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A125 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R020_BALANCED_LONG | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R040 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R075 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| CH_MBV3_GB20_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-09-17T13:41:42+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **649871**
- Valutazioni prodotte: **29803**
- Candidature al Blocco 5: **15**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
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
| ATR15_R100 | 41 | 2,788 | 4,115 | 2,074 | 85,4% | 87,5 | EARLY_SIGNAL |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

🏆 CHALLENGER CANDIDATE
Aggiornamento aggregazione UTC: 2026-09-17T13:48:57+00:00
Mother canonica simulata: stessi ingressi, osservazioni ed execution del challenger.
PnL al netto delle fee modellate, funding escluso da entrambi; FX congelato all'ingresso.
Osservazioni MARK discrete: nessuna certificazione del percorso intrabar tra quotazioni.
Ranking promozionale: INSUFFICIENT_CERTIFIED_DATA

Rapida 1H V1 — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Rapida 1H V1 — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 90 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Master Adaptive Consensus — breakeven dopo +0,2R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 38 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 154 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 0 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

AUTO_PROMOTION=DISABLED · nessun ordine · revisione umana obbligatoria.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-17T13:34:03+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **31**
- Simulazioni completate nel ciclo: **13**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **773.35 R**
- Profitto virtuale mancato: **1889.97 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 148 | 0 | 15086.89 |
| DOWN_20 | 148 | 0 | 30173.78 |
| DOWN_30 | 148 | 0 | 45260.67 |
| DOWN_40 | 148 | 83 | 53488.54 |
| UP_10 | 27 | 0 | 1144.64 |
| UP_20 | 27 | 4 | 2512.42 |
| UP_30 | 27 | 4 | 3489.71 |
| UP_40 | 27 | 13 | 4664.34 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-17T13:31:08+00:00

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

Generato: 2026-09-17T13:49:04+00:00

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

Generato: 2026-09-17T13:49:04+00:00

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

Generato: 2026-09-17T13:49:04+00:00

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

Generato: 2026-09-17T13:49:04+00:00

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
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 23.1 | E | 161 | 1.43 | 0.220 | 23.36 |
| 2 | SHADOW_DONCHIAN_1H | BASELINE | 20.9 | E | 170 | 1.28 | 0.164 | 20.49 |
| 3 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | BASELINE | 20.9 | E | 182 | 1.14 | 0.066 | 10.66 |
| 4 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 20.6 | E | 181 | 1.23 | 0.110 | 14.92 |
| 5 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 20.2 | E | 212 | 1.20 | 0.098 | 25.45 |
| 6 | SHADOW_COMBO_ADAPTIVE | BASELINE | 19.9 | E | 228 | 1.20 | 0.099 | 23.82 |
| 7 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | BASELINE | 19.8 | E | 138 | 1.29 | 0.172 | 20.49 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 18.6 | E | 235 | 1.06 | 0.033 | 30.08 |
| 9 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 18.1 | E | 179 | 1.06 | 0.036 | 25.62 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 18.0 | E | 206 | 1.05 | 0.026 | 14.78 |

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

Generato: 2026-09-17T13:49:04+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BULL_TREND**
- Righe di performance: **1122**
- Strategie preferite nel regime corrente: **9**
- Strategie da evitare nel regime corrente: **15**
- Memorie contestuali: **536**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.621 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.668 | 0.00 |
| 3 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 75.5 | 3 | 2.66 | 0.572 | 1.04 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.8 | 12 | 4.37 | 0.378 | 1.07 |
| 5 | SHADOW_SOL_ADAPTIVE_1H | shadow-sol-adaptive-1h | INSUFFICIENT | 73.2 | 9 | 2.30 | 0.480 | 1.17 |
| 6 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 73.1 | 6 | 3.16 | 0.473 | 1.20 |
| 7 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | INSUFFICIENT | 71.8 | 9 | 2.30 | 0.480 | 2.14 |
| 8 | SHADOW_SCANNER_TOP15_LONG | shadow-scanner-top15-long | COMPATIBLE | 61.2 | 106 | 1.42 | 0.201 | 11.55 |
| 9 | SHADOW_SCANNER_TOP20_LONG | shadow-scanner-top20-long | COMPATIBLE | 61.2 | 106 | 1.42 | 0.201 | 11.55 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | shadow-1h-fast-v3-no-esports-mfe-lock-v1 | COMPATIBLE | 60.8 | 79 | 1.35 | 0.180 | 15.57 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-17T13:49:05+00:00

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

Generato: 2026-09-17T13:34:03+00:00

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
