# Paper trading automatico KuCoin

Generato: 2026-07-27T07:24:36+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-27T07:23:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-27T07:23:25+00:00 | 2026-07-27T07:23:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-27T07:00:00+00:00 | 2026-07-27T07:00:00+00:00 | 8,6 min | 25,0 min | OK |
| 60m | 12 | 2026-07-27T06:00:00+00:00 | 2026-07-27T06:00:00+00:00 | 23,6 min | 45,0 min | OK |
| 240m | 12 | 2026-07-27T00:00:00+00:00 | 2026-07-27T00:00:00+00:00 | 3,39 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | PEPE | 60m | LONG | 8,09 | 4,50 | 0,00 | OPENED | 23,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 23,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | PEPE | 60m | LONG | 8,09 | 4,50 | 0,00 | OPENED | 23,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 23,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | PEPE | 240m | LONG | 6,53 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,24 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | EUL | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SHIB | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,00 | 6,00 | 4,00 | STALE_CANDLE | 3,39 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,70 | 6,00 | 4,30 | STALE_CANDLE | 3,39 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,69 | 6,00 | 4,31 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 1,34 | 6,00 | 4,66 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,25 | 6,00 | 4,75 | STALE_CANDLE | 3,39 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 1,24 | 6,00 | 4,76 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | BANK | 60m | LONG | 9,75 | 5,00 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | BANK | 60m | LONG | 9,75 | 5,00 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered — madre | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — no volatilità HIGH | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — Long Only | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — senza ESPORTS | BANK | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 23,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.848,27 | -1,52% | €-151,73 | €3.000,00 | -5,06% | 4 | 22 | 31,82% | 0,80 | 4,52% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 22 | 771 | CAMPIONE INSUFFICIENTE | 30 (mancano 8) |

- Trade del Principale 4H chiusi: **22**; win rate **31,82%**; profit factor **0,80**.
- Expectancy: **€-6,82** per trade; P&L netto: **€-149,93**; max drawdown: **4,52%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.848,27 | €947,35 | €2.842,05 | €100,60 | €-0,81 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.714,68 | €3.093,73 | €6.187,46 | €55,55 | €88,46 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.684,84 | €547,89 | €1.643,66 | €159,10 | €-0,39 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.655,65 | €3.315,69 | €6.631,38 | €106,02 | €58,25 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 2 | €10.603,46 | €483,16 | €1.449,49 | €103,37 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 3 | €10.496,23 | €496,95 | €1.490,85 | €105,42 | €-0,40 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.480,83 | €232,83 | €698,50 | €54,00 | €-0,47 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 4 | €10.453,29 | €2.807,73 | €8.423,18 | €104,73 | €30,64 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.446,92 | €3.834,56 | €7.669,11 | €158,26 | €32,19 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.441,00 | €222,84 | €668,52 | €53,35 | €-0,43 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 3 | €10.432,35 | €1.533,83 | €4.601,48 | €1,77 | €59,17 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 3 | €10.398,80 | €1.091,51 | €3.274,54 | €101,01 | €-14,63 |
| TEST | Rapida V3 NoHigh — Regime Guard | 2 | €10.397,21 | €187,63 | €562,88 | €53,52 | €-0,57 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 3 | €10.374,10 | €1.693,66 | €5.080,99 | €102,63 | €0,00 |
| TEST | Bilanciata 1H V1 | 5 | €10.371,98 | €2.285,03 | €6.855,09 | €52,10 | €44,85 |
| TEST | Rapida score 6–7,5 — Range Only | 3 | €10.358,40 | €793,83 | €2.381,49 | €154,26 | €-14,56 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.344,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 4 | €10.341,18 | €1.173,24 | €3.519,73 | €53,06 | €1,73 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 3 | €10.337,30 | €1.897,39 | €5.692,17 | €51,55 | €44,23 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.322,30 | €466,49 | €1.399,48 | €50,44 | €33,91 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 2 | €10.302,95 | €475,15 | €1.425,46 | €101,57 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.296,85 | €313,60 | €940,79 | €102,49 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 3 | €10.292,98 | €3.218,92 | €9.656,77 | €153,94 | €-14,41 |
| TEST | Combo Adaptive — Side × Regime Guard | 3 | €10.277,77 | €1.680,99 | €3.361,97 | €153,21 | €-15,72 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 4 | €10.259,72 | €1.490,88 | €4.472,63 | €150,48 | €-26,46 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 5 | €10.252,90 | €398,49 | €1.195,48 | €52,45 | €0,04 |
| TEST | Rapida V1 — senza PEPE | 2 | €10.249,84 | €2.351,47 | €7.054,40 | €101,82 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 4 | €10.244,63 | €1.074,62 | €3.223,87 | €102,49 | €-1,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 3 | €10.239,21 | €373,39 | €1.120,17 | €55,57 | €-1,35 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.231,63 | €452,09 | €904,18 | €101,21 | €-0,15 |
| TEST | Combo Adaptive — madre | 4 | €10.203,22 | €2.162,62 | €4.325,23 | €204,07 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €10.200,42 | €1.358,78 | €4.076,33 | €101,14 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €10.189,27 | €2.751,42 | €5.502,84 | €103,99 | €41,53 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.183,37 | €2.775,19 | €5.550,37 | €103,49 | €42,53 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €10.173,99 | €3.041,83 | €6.083,67 | €201,84 | €-11,07 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 2 | €10.173,88 | €2.387,16 | €7.161,49 | €50,82 | €-11,28 |
| TEST | Btc Bollinger 1H | 0 | €10.168,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 4 | €10.165,27 | €1.999,59 | €3.999,19 | €150,96 | €-0,78 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 3 | €10.158,00 | €3.848,11 | €11.544,33 | €101,78 | €30,68 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 4 | €10.154,46 | €2.684,27 | €8.052,82 | €101,46 | €28,39 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 3 | €10.150,61 | €1.873,45 | €5.620,36 | €100,19 | €-20,83 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €10.128,57 | €275,53 | €826,58 | €51,72 | €-0,63 |
| TEST | Forza relativa 1H V2 | 3 | €10.123,60 | €2.339,86 | €4.679,73 | €54,70 | €51,25 |
| TEST | Rapida V1 — target pieno 2R | 5 | €10.114,87 | €2.562,28 | €7.686,85 | €151,91 | €-14,49 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €10.083,38 | €3.152,79 | €9.458,37 | €150,78 | €-14,11 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €10.073,55 | €631,90 | €1.895,69 | €99,63 | €-14,21 |
| TEST | Ampia 4H | 3 | €10.061,19 | €1.527,13 | €3.054,26 | €149,32 | €-23,16 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €10.056,13 | €3.144,27 | €9.432,80 | €150,37 | €-14,07 |
| TEST | Bilanciata V3 · LONG only | 4 | €10.053,50 | €1.239,20 | €3.717,59 | €101,37 | €0,56 |
| TEST | Combo Adaptive — Long Only | 5 | €10.049,95 | €3.469,07 | €6.938,13 | €200,34 | €-11,07 |
| TEST | Rapida 1H V1 — madre | 1 | €10.048,63 | €1.486,90 | €4.460,70 | €49,96 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 5 | €10.045,58 | €2.739,97 | €5.479,93 | €102,27 | €41,88 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 2 | €10.041,17 | €531,37 | €1.594,12 | €101,57 | €-14,40 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 4 | €10.035,40 | €3.534,16 | €7.068,31 | €150,89 | €-14,59 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €10.034,85 | €1.988,08 | €3.976,15 | €144,24 | €0,77 |
| TEST | Combo Scanner | 5 | €10.033,27 | €2.722,53 | €5.445,06 | €101,45 | €42,49 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €10.032,65 | €2.088,81 | €4.177,61 | €100,07 | €48,05 |
| TEST | Rapida 1H V2 | 3 | €10.024,86 | €4.383,00 | €13.149,00 | €150,74 | €-13,65 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 4 | €10.024,43 | €2.651,59 | €5.303,18 | €150,47 | €-10,71 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 4 | €10.024,39 | €2.463,89 | €7.391,67 | €99,91 | €42,01 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €10.014,81 | €2.664,52 | €5.329,05 | €150,82 | €-10,90 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.010,23 | €50,00 | €750,00 | €6,39 | €-0,29 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.002,05 | €10,00 | €150,00 | €1,28 | €-0,06 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 3 | €9.999,49 | €2.319,93 | €4.639,86 | €52,73 | €37,93 |
| TEST | Scanner Top15 Long | 3 | €9.999,49 | €2.319,93 | €4.639,86 | €52,73 | €37,93 |
| TEST | Scanner Top20 Long | 3 | €9.999,49 | €2.319,93 | €4.639,86 | €52,73 | €37,93 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 1 | €9.998,03 | €10,00 | €150,00 | €6,94 | €-2,18 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 2 | €9.997,68 | €967,58 | €2.902,73 | €100,00 | €-0,58 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 2 | €9.997,68 | €967,58 | €2.902,73 | €100,00 | €-0,58 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.994,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 5 | €9.992,40 | €2.058,16 | €4.116,32 | €99,26 | €57,79 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 1 | €9.990,13 | €50,00 | €750,00 | €34,68 | €-10,89 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 1 | €9.984,53 | €828,72 | €2.486,15 | €50,00 | €-13,97 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 1 | €9.973,73 | €43,15 | €215,74 | €9,98 | €-3,13 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 5 | €9.971,12 | €1.185,46 | €3.556,39 | €99,83 | €-13,95 |
| TEST | Eth Ema 4H | 1 | €9.966,84 | €1.036,30 | €2.072,59 | €49,74 | €20,96 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 3 | €9.965,75 | €1.752,07 | €5.256,22 | €149,95 | €-10,84 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.962,81 | €1.383,38 | €2.766,77 | €49,61 | €28,48 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.946,96 | €1.292,62 | €3.877,86 | €49,64 | €22,27 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.942,96 | €233,49 | €1.167,44 | €9,94 | €-0,46 |
| TEST | Sol Adaptive 4H | 1 | €9.934,40 | €761,04 | €1.522,08 | €49,74 | €-13,33 |
| TEST | Sol Donchian 4H | 1 | €9.932,98 | €830,21 | €1.660,43 | €49,74 | €-14,54 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.925,54 | €1.659,25 | €3.318,51 | €198,60 | €-44,68 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.923,54 | €1.372,84 | €2.745,68 | €149,15 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.923,49 | €5.116,26 | €10.232,53 | €144,75 | €47,54 |
| TEST | Btc Ema 1H | 0 | €9.911,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.911,28 | €862,58 | €1.725,17 | €49,74 | €-36,13 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 3 | €9.900,04 | €652,43 | €1.957,28 | €97,84 | €-13,76 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.877,72 | €1.371,54 | €2.743,08 | €99,39 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.872,42 | €1.896,14 | €3.792,28 | €49,61 | €56,62 |
| TEST | Eth Adaptive 1H | 1 | €9.871,22 | €1.140,50 | €3.421,49 | €49,27 | €19,65 |
| TEST | Top 5 + BTC — Guard | 3 | €9.858,45 | €1.913,39 | €3.826,78 | €147,07 | €-10,73 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.851,27 | €2.023,94 | €4.047,88 | €148,64 | €-10,72 |
| TEST | Master Adaptive Runner25 V1 | 4 | €9.839,62 | €2.010,14 | €4.020,28 | €148,12 | €-10,71 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.834,54 | €4.821,61 | €9.643,21 | €149,39 | €26,72 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.810,93 | €2.008,03 | €4.016,07 | €148,00 | €-10,68 |
| TEST | Master Adaptive V1 | 4 | €9.806,79 | €2.007,63 | €4.015,27 | €147,98 | €-10,67 |
| TEST | Eth Ema 1H | 1 | €9.798,96 | €1.132,15 | €3.396,44 | €48,91 | €19,51 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.793,88 | €2.297,41 | €4.594,82 | €95,65 | €45,32 |
| TEST | Global Confluence puro 1H | 0 | €9.790,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.751,48 | €2.159,38 | €4.318,77 | €98,62 | €0,00 |
| TEST | Scanner Bottom15 Short | 3 | €9.751,48 | €2.159,38 | €4.318,77 | €98,62 | €0,00 |
| TEST | Scanner Bottom20 Short | 3 | €9.751,48 | €2.159,38 | €4.318,77 | €98,62 | €0,00 |
| TEST | Forza relativa 1H V1 | 5 | €9.738,77 | €2.641,65 | €5.283,31 | €101,31 | €37,69 |
| TEST | Combo Adaptive — parziale 1R | 6 | €9.718,68 | €2.549,49 | €5.098,97 | €194,08 | €-4,70 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.705,31 | €1.786,26 | €3.572,51 | €48,61 | €0,00 |
| TEST | Combo Trend | 3 | €9.698,05 | €1.332,61 | €2.665,23 | €93,74 | €9,50 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.683,07 | €2.164,39 | €4.328,79 | €94,58 | €44,86 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.650,33 | €3.311,32 | €6.622,64 | €193,23 | €-10,26 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.608,35 | €3.742,70 | €7.485,40 | €141,82 | €39,67 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.601,01 | €2.743,97 | €5.487,93 | €192,25 | €-10,27 |

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
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.848,27 | €-149,93 | 22 | 22 | 31,82% | 0,80 | €-6,82 | 4,52% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.714,68 | €630,33 | 38 | 38 | 52,63% | 1,74 | €16,59 | 3,57% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.684,84 | €686,31 | 47 | 47 | 44,68% | 1,73 | €14,60 | 2,20% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.655,65 | €602,13 | 27 | 27 | 55,56% | 2,13 | €22,30 | 2,12% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.603,46 | €604,33 | 56 | 56 | 50,00% | 1,60 | €10,79 | 2,83% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.496,23 | €497,52 | 47 | 47 | 51,06% | 1,65 | €10,59 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.480,83 | €481,72 | 52 | 52 | 48,08% | 1,51 | €9,26 | 2,49% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.453,29 | €427,70 | 16 | 16 | 62,50% | 4,74 | €26,73 | 1,97% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.446,92 | €419,63 | 30 | 30 | 50,00% | 1,60 | €13,99 | 3,23% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.441,00 | €441,83 | 16 | 16 | 68,75% | 3,00 | €27,61 | 1,96% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.432,35 | €375,94 | 16 | 16 | 56,25% | 2,53 | €23,50 | 1,62% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.398,80 | €415,39 | 22 | 22 | 63,64% | 2,86 | €18,88 | 1,14% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.397,21 | €398,56 | 17 | 17 | 70,59% | 3,46 | €23,44 | 1,39% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.374,10 | €377,59 | 29 | 29 | 62,07% | 2,29 | €13,02 | 2,05% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.371,98 | €334,41 | 50 | 50 | 52,00% | 1,34 | €6,69 | 3,25% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.358,40 | €374,49 | 10 | 10 | 70,00% | 3,74 | €37,45 | 2,28% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.344,54 | €344,54 | 6 | 6 | 66,67% | 7,16 | €57,42 | 1,06% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.341,18 | €341,56 | 21 | 21 | 61,90% | 2,21 | €16,26 | 1,32% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.337,30 | €296,50 | 16 | 16 | 50,00% | 2,59 | €18,53 | 2,27% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.322,30 | €289,58 | 7 | 7 | 57,14% | 3,63 | €41,37 | 1,49% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.302,95 | €303,80 | 16 | 16 | 68,75% | 2,24 | €18,99 | 2,01% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.296,85 | €297,96 | 10 | 10 | 70,00% | 2,84 | €29,80 | 1,78% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.292,98 | €313,18 | 78 | 78 | 41,03% | 1,21 | €4,02 | 2,89% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.277,77 | €295,65 | 13 | 13 | 84,62% | 3,73 | €22,74 | 1,41% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.259,72 | €288,87 | 18 | 18 | 50,00% | 2,20 | €16,05 | 1,60% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.252,90 | €253,58 | 13 | 13 | 61,54% | 4,25 | €19,51 | 2,01% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.249,84 | €254,07 | 46 | 46 | 45,65% | 1,29 | €5,52 | 2,15% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.244,63 | €247,57 | 18 | 18 | 61,11% | 2,03 | €13,75 | 1,76% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,21 | €241,88 | 13 | 13 | 61,54% | 4,96 | €18,61 | 1,01% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.231,63 | €232,32 | 13 | 13 | 61,54% | 2,39 | €17,87 | 1,32% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.203,22 | €206,62 | 25 | 25 | 48,00% | 1,52 | €8,26 | 1,49% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.200,42 | €202,87 | 37 | 35 | 54,05% | 1,27 | €5,48 | 2,75% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.189,27 | €151,32 | 13 | 13 | 53,85% | 1,33 | €11,64 | 3,22% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.183,37 | €144,46 | 17 | 17 | 52,94% | 1,31 | €8,50 | 3,25% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.173,99 | €189,58 | 23 | 23 | 47,83% | 1,42 | €8,24 | 2,12% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.173,88 | €189,91 | 15 | 15 | 53,33% | 1,58 | €12,66 | 2,17% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.168,12 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,54% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.165,27 | €169,33 | 17 | 17 | 47,06% | 1,94 | €9,96 | 1,51% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €10.158,00 | €134,70 | 9 | 9 | 55,56% | 1,82 | €14,97 | 2,06% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €10.154,46 | €130,91 | 17 | 17 | 52,94% | 1,43 | €7,70 | 2,38% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.150,61 | €174,84 | 20 | 20 | 45,00% | 1,51 | €8,74 | 2,07% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €10.128,57 | €129,70 | 43 | 43 | 51,16% | 1,14 | €3,02 | 3,21% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.123,60 | €75,50 | 42 | 41 | 40,48% | 1,05 | €1,80 | 5,10% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.114,87 | €133,97 | 49 | 49 | 38,78% | 1,13 | €2,73 | 2,58% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.083,38 | €103,17 | 52 | 52 | 42,31% | 1,10 | €1,98 | 2,49% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €10.073,55 | €88,90 | 39 | 39 | 46,15% | 1,11 | €2,28 | 2,86% |
| TEST | Ampia 4H | Confluenza trend | €10.061,19 | €85,82 | 18 | 18 | 27,78% | 1,17 | €4,77 | 3,68% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.056,13 | €75,86 | 53 | 53 | 43,40% | 1,07 | €1,43 | 2,96% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €10.053,50 | €55,84 | 8 | 8 | 37,50% | 1,34 | €6,98 | 1,46% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.049,95 | €65,56 | 11 | 11 | 45,45% | 1,28 | €5,96 | 2,34% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.048,63 | €51,31 | 77 | 77 | 35,06% | 1,03 | €0,67 | 6,76% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.045,58 | €7,37 | 12 | 12 | 50,00% | 1,02 | €0,61 | 3,23% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.041,17 | €56,63 | 6 | 6 | 50,00% | 1,56 | €9,44 | 2,15% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €10.035,40 | €54,23 | 10 | 10 | 40,00% | 1,16 | €5,42 | 3,63% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.034,85 | €36,84 | 12 | 12 | 50,00% | 1,09 | €3,07 | 3,23% |
| TEST | Combo Scanner | Combo Scanner | €10.033,27 | €-5,67 | 35 | 35 | 45,71% | 0,99 | €-0,16 | 3,25% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.032,65 | €-12,51 | 6 | 6 | 33,33% | 0,93 | €-2,09 | 2,84% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.024,86 | €46,84 | 14 | 13 | 50,00% | 1,15 | €3,35 | 1,69% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €10.024,43 | €38,32 | 8 | 8 | 50,00% | 1,14 | €4,79 | 2,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €10.024,39 | €-13,19 | 14 | 14 | 57,14% | 0,96 | €-0,94 | 2,93% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €10.014,81 | €28,91 | 14 | 14 | 28,57% | 1,08 | €2,06 | 3,15% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,23 | €10,98 | 9 | 9 | 33,33% | 1,23 | €1,22 | 0,25% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,05 | €2,20 | 9 | 9 | 33,33% | 1,23 | €0,24 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.999,49 | €-35,65 | 10 | 10 | 50,00% | 0,86 | €-3,57 | 3,62% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.999,49 | €-35,65 | 10 | 10 | 50,00% | 0,86 | €-3,57 | 3,62% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.999,49 | €-35,65 | 10 | 10 | 50,00% | 0,86 | €-3,57 | 3,62% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.998,03 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,05% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.997,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,02% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.997,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,02% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.994,85 | €-5,15 | 17 | 17 | 41,18% | 0,99 | €-0,30 | 2,31% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.992,40 | €-62,83 | 12 | 12 | 50,00% | 0,81 | €-5,24 | 2,18% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.990,13 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,24% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €9.984,53 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,15% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.973,73 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,40% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.971,12 | €-12,80 | 13 | 13 | 61,54% | 0,96 | €-0,98 | 3,08% |
| TEST | Eth Ema 4H | Trend following EMA | €9.966,84 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,80% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.965,75 | €-20,25 | 11 | 11 | 45,45% | 0,94 | €-1,84 | 2,47% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.962,81 | €-90,36 | 7 | 7 | 42,86% | 0,57 | €-12,91 | 1,95% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.946,96 | €-72,68 | 4 | 4 | 25,00% | 0,56 | €-18,17 | 1,38% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.942,96 | €-55,88 | 9 | 9 | 22,22% | 0,16 | €-6,21 | 0,58% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.934,40 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,73% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.932,98 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,75% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.925,54 | €-26,77 | 27 | 27 | 40,74% | 0,96 | €-0,99 | 2,25% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.923,54 | €-74,71 | 6 | 6 | 50,00% | 0,54 | €-12,45 | 1,38% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.923,49 | €-118,31 | 39 | 39 | 38,46% | 0,88 | €-3,03 | 4,19% |
| TEST | Btc Ema 1H | Trend following EMA | €9.911,86 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Sol Ema 4H | Trend following EMA | €9.911,28 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,97% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.900,04 | €-85,02 | 43 | 43 | 37,21% | 0,91 | €-1,98 | 3,67% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.877,72 | €-119,98 | 5 | 5 | 40,00% | 0,25 | €-24,00 | 1,53% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.872,42 | €-181,92 | 7 | 7 | 28,57% | 0,18 | €-25,99 | 2,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.871,22 | €-146,11 | 5 | 5 | 40,00% | 0,11 | €-29,22 | 1,84% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.858,45 | €-128,29 | 17 | 17 | 35,29% | 0,78 | €-7,55 | 3,36% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.851,27 | €-135,12 | 15 | 15 | 40,00% | 0,78 | €-9,01 | 3,64% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.839,62 | €-146,81 | 14 | 14 | 35,71% | 0,74 | €-10,49 | 3,98% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.834,54 | €-186,71 | 21 | 21 | 38,10% | 0,62 | €-8,89 | 3,95% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.810,93 | €-175,53 | 12 | 12 | 33,33% | 0,68 | €-14,63 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.806,79 | €-179,67 | 12 | 12 | 33,33% | 0,68 | €-14,97 | 4,07% |
| TEST | Eth Ema 1H | Trend following EMA | €9.798,96 | €-218,24 | 7 | 7 | 28,57% | 0,20 | €-31,18 | 2,52% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.793,88 | €-248,68 | 26 | 26 | 42,31% | 0,67 | €-9,56 | 3,93% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.790,66 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.751,48 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.751,48 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.751,48 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.738,77 | €-295,76 | 29 | 29 | 27,59% | 0,66 | €-10,20 | 6,18% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.718,68 | €-272,77 | 20 | 20 | 40,00% | 0,54 | €-13,64 | 3,32% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.705,31 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Combo Trend | Combo Trend | €9.698,05 | €-308,91 | 39 | 39 | 33,33% | 0,78 | €-7,92 | 7,02% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.683,07 | €-359,33 | 29 | 29 | 37,93% | 0,58 | €-12,39 | 5,08% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.650,33 | €-335,44 | 48 | 48 | 58,33% | 0,61 | €-6,99 | 4,16% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.608,35 | €-426,83 | 21 | 21 | 28,57% | 0,57 | €-20,33 | 5,48% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.601,01 | €-385,36 | 30 | 30 | 30,00% | 0,50 | €-12,85 | 5,33% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €-0,81 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1943,95871 | 1969,50000 | 1952,10441 | 1305,69227 | 1999,94472 | €1.144,39 | €3.433,17 | €0,00 | €45,11 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 60,41523 | 59,96100 | 59,54525 | 40,57889 | 62,15519 | €12,00 | €36,00 | €0,52 | €-0,27 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,38 | €25,15 | €0,63 | €0,01 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €643,12 | €1.929,37 | €49,89 | €-10,84 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | SHIB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,58 | €25,73 | €1,38 | €-0,55 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1969,50000 | 1930,05275 | 1315,29231 | 2014,64922 | €8,95 | €26,84 | €0,39 | €0,15 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,70 | €35,09 | €1,52 | €-0,43 |
| Rapida V1 — score 6–7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,05376 | €8,47 | €25,40 | €0,28 | €-0,04 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| Rapida score 6–7,5 — Range Only | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €394,57 | €1.183,71 | €51,34 | €-14,56 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,64 | €34,93 | €1,52 | €-0,43 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,88 | €1.157,65 | €50,21 | €-14,24 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,11443 | 1,11105 | 1,10195 | 0,74853 | 1,13316 | €70,58 | €211,74 | €2,37 | €-0,64 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,05376 | €1.416,99 | €4.250,97 | €47,61 | €-5,95 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,60 | €31,81 | €1,45 | €-0,33 |
| Rapida V1 — target pieno 2R | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €839,51 | €2.518,54 | €50,65 | €-14,16 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V2 | XRP | LONG | Momentum / breakout V2 | 60m | 3,0x | 1,11443 | 1,11105 | 1,10195 | 0,74853 | 1,13316 | €1.498,43 | €4.495,30 | €50,35 | €-13,65 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €854,32 | €2.562,95 | €51,54 | €-14,41 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — score <7,5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,86 | €32,57 | €1,41 | €-0,40 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €834,66 | €2.503,97 | €50,36 | €-14,07 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €375,62 | €1.126,85 | €48,88 | €-13,86 |
| Rapida V3 — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €32,85 | €98,56 | €0,00 | €0,09 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,28 | €1.155,84 | €50,13 | €-14,21 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €836,92 | €2.510,76 | €50,50 | €-14,11 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €20,15 | €60,45 | €2,62 | €-0,74 |
| Rapida V3 senza ESPORTS — Long Only | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,05376 | €14,96 | €44,89 | €0,50 | €-0,06 |
| Rapida V3 senza ESPORTS — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €889,35 | €2.668,06 | €0,00 | €2,54 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,11105 | 1,10195 | 0,74853 | 1,13316 | €1.512,48 | €4.537,44 | €50,82 | €-13,77 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €874,68 | €2.624,05 | €0,00 | €2,49 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,43 | €46,28 | €2,01 | €-0,57 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,05376 | €14,94 | €44,83 | €0,50 | €-0,06 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 59,96100 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-23,16 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | ETH | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1943,95871 | 1969,50000 | 1949,69644 | 981,69915 | 2005,54333 | €1.433,90 | €2.867,80 | €0,00 | €37,68 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,97 | €29,95 | €0,75 | €0,01 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €846,05 | €1.692,10 | €0,00 | €51,25 |
| Scalp RSI Long 25 · €10 · 15x | EUL | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 1,97690 | 1,94820 | 1,88547 | 1,85499 | 2,11403 | €10,00 | €150,00 | €6,94 | €-2,18 |
| Scalp RSI Long 25 · €50 · 15x | EUL | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 1,97690 | 1,94820 | 1,88547 | 1,85499 | 2,11403 | €50,00 | €750,00 | €34,68 | €-10,89 |
| Scalp RSI Long 25 · prudente · 5x | EUL | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 1,97690 | 1,94820 | 1,88547 | 1,59140 | 2,15974 | €43,15 | €215,74 | €9,98 | €-3,13 |
| Scalp RSI Short 75 · €10 · 15x | ETH | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 1968,72618 | 1969,50000 | 1985,49557 | 2090,13096 | 1943,57208 | €10,00 | €150,00 | €1,28 | €-0,06 |
| Scalp RSI Short 75 · €50 · 15x | ETH | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 1968,72618 | 1969,50000 | 1985,49557 | 2090,13096 | 1943,57208 | €50,00 | €750,00 | €6,39 | €-0,29 |
| Scalp RSI Short 75 · prudente · 5x | ETH | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 1968,72618 | 1969,50000 | 1985,49557 | 2352,62778 | 1935,18737 | €233,49 | €1.167,44 | €9,94 | €-0,46 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 58,92678 | 59,96100 | 59,85884 | 29,75803 | 61,28385 | €1.635,95 | €3.271,90 | €0,00 | €57,42 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1958,25157 | 1969,50000 | 1926,91955 | 988,91704 | 2036,58163 | €70,73 | €141,45 | €2,26 | €0,81 |
| Benchmark Donchian breakout 1H | PEPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,82 | €33,65 | €0,93 | €0,01 |
| Benchmark Bollinger mean reversion 1H | XRP | SHORT | Bollinger mean reversion | 60m | 2,0x | 1,11399 | 1,11105 | 1,12736 | 1,66541 | 1,09394 | €1.986,03 | €3.972,07 | €47,66 | €10,47 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 60,34277 | 59,96100 | 61,06689 | 90,21245 | 59,25660 | €1.980,47 | €3.960,93 | €47,53 | €25,06 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.149,76 | €2.299,52 | €49,55 | €12,01 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | SHIB | LONG | Trend following EMA | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €389,51 | €779,03 | €49,98 | €-35,29 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €835,63 | €1.671,25 | €48,02 | €-9,39 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.011,45 | €2.022,90 | €0,00 | €41,77 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1943,95871 | 1969,50000 | 1952,10441 | 981,69915 | 1999,94472 | €1.778,37 | €3.556,74 | €0,00 | €46,73 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 60,04501 | 59,96100 | 59,18036 | 30,32273 | 61,77430 | €14,18 | €28,35 | €0,41 | €-0,04 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,24 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €0,00 | €38,18 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,24 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €0,00 | €38,18 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,24 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €0,00 | €38,18 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1969,50000 | 1950,76468 | 981,69915 | 2005,54333 | €1.658,75 | €3.317,49 | €0,00 | €43,59 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 60,04501 | 59,96100 | 59,18036 | 30,32273 | 61,94723 | €12,65 | €25,30 | €0,36 | €-0,04 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.010,86 | €2.021,73 | €52,28 | €-11,36 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — solo MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1947,14935 | 1969,50000 | 1954,15909 | 983,31042 | 2008,83504 | €1.634,22 | €3.268,43 | €0,00 | €37,52 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 60,04501 | 59,96100 | 59,18036 | 30,32273 | 61,94723 | €36,62 | €73,24 | €1,05 | €-0,10 |
| Top 5 + BTC — solo MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €951,60 | €1.903,20 | €49,21 | €-10,70 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €954,30 | €1.908,59 | €49,35 | €-10,73 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC≤3 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1969,50000 | 1950,76468 | 981,69915 | 2005,54333 | €1.593,18 | €3.186,36 | €0,00 | €41,86 |
| Top 5 + BTC — BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,64 | €33,28 | €0,83 | €0,01 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €996,29 | €1.992,58 | €0,00 | €48,05 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €407,51 | €815,02 | €45,45 | €-10,02 |
| Top 5 + BTC — Guard + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.000,26 | €2.000,52 | €0,00 | €54,88 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €911,18 | €1.822,36 | €45,43 | €0,77 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €414,63 | €829,26 | €46,24 | €-10,20 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.011,73 | €2.023,45 | €0,00 | €55,51 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1969,50000 | 1950,76468 | 981,69915 | 2027,93773 | €1.617,79 | €3.235,59 | €0,00 | €42,51 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,90 | €33,79 | €0,84 | €0,01 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Top 5 + BTC — target pieno 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1969,50000 | 1950,76468 | 981,69915 | 2027,93773 | €1.579,98 | €3.159,95 | €0,00 | €41,52 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,50 | €33,00 | €0,82 | €0,01 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €784,30 | €1.568,61 | €0,00 | €40,21 |
| Combo Trend | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €338,96 | €677,92 | €43,49 | €-30,71 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 1943,95871 | 1969,50000 | 1950,76468 | 981,69915 | 2005,54333 | €1.616,34 | €3.232,67 | €0,00 | €42,47 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,84 | €0,01 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €913,78 | €1.827,57 | €47,26 | €-10,27 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive — Quality7 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €12,84 | €25,69 | €1,30 | €-0,78 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Trend/Transition | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.044,39 | €2.088,78 | €0,00 | €57,30 |
| Combo Adaptive — Trend/Transition | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1947,28938 | 1969,50000 | 1951,73653 | 983,38114 | 2003,37131 | €32,32 | €64,64 | €0,00 | €0,74 |
| Combo Adaptive — Trend/Transition | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 60,41523 | 59,96100 | 59,54525 | 30,50969 | 62,15519 | €16,99 | €33,99 | €0,49 | €-0,26 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,87 | €2.063,74 | €0,00 | €56,62 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €-0,13 |
| Combo Adaptive — Long Only | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €972,81 | €1.945,63 | €50,31 | €-10,94 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1949,77988 | 1969,50000 | 1952,35985 | 984,63884 | 2005,93354 | €13,89 | €27,78 | €0,00 | €0,28 |
| Combo Adaptive — parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €443,37 | €886,74 | €22,93 | €-4,98 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €519,11 | €1.038,23 | €0,00 | €28,48 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €984,84 | €1.969,68 | €50,93 | €-11,07 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 76,62900 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €-36,13 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 76,62900 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €-14,54 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 76,62900 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €-13,33 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1958,25157 | 1969,50000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.132,15 | €3.396,44 | €48,91 | €19,51 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1949,77988 | 1969,50000 | 1902,99144 | 984,63884 | 2066,75096 | €1.036,30 | €2.072,59 | €49,74 | €20,96 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1958,25157 | 1969,50000 | 1933,18595 | 1315,29231 | 2008,38281 | €1.292,62 | €3.877,86 | €49,64 | €22,27 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1958,25157 | 1969,50000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.140,50 | €3.421,49 | €49,27 | €19,65 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €949,30 | €1.898,59 | €49,09 | €-10,67 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €949,70 | €1.899,39 | €49,11 | €-10,68 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1943,95871 | 1969,50000 | 1915,96571 | 981,69915 | 1999,94472 | €1.509,27 | €3.018,53 | €43,47 | €39,66 |
| Master Adaptive Strict3 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €15,76 | €31,52 | €0,79 | €0,01 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €953,60 | €1.907,20 | €49,32 | €-10,72 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €912,79 | €1.825,58 | €47,21 | €-10,26 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €952,47 | €1.904,95 | €49,26 | €-10,71 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €-4,54 |
| Combo Adaptive — Side × Regime Guard | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €994,19 | €1.988,39 | €51,41 | €-11,18 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €969,43 | €1.938,87 | €50,13 | €-10,90 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1955,19096 | 1969,50000 | 1955,19096 | 987,37143 | 2011,50046 | €13,71 | €27,42 | €0,00 | €0,20 |
| Master Adaptive GB20 — 50% a 0,75R | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €970,36 | €1.940,72 | €50,18 | €-10,91 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1970,82409 | 1969,50000 | 1949,53919 | 995,26616 | 2027,58382 | €14,30 | €28,60 | €0,31 | €-0,02 |
| Master Adaptive GB20 — Loss Cap 0,75R | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.295,75 | €2.591,50 | €50,26 | €-14,57 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,44 | €46,31 | €2,01 | €-0,57 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €326,47 | €979,41 | €50,44 | €33,91 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,70 | €29,40 | €1,89 | €-1,33 |
| Combo Trend — Side × Regime Guard | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,55 | €25,09 | €0,00 | €0,93 |
| Combo Trend — Side × Regime Guard | ETH | LONG | Combo Trend | 60m | 2,0x | 1949,77988 | 1969,50000 | 1918,58340 | 984,63884 | 2018,41213 | €12,70 | €25,41 | €0,41 | €0,26 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €25,54 | €76,62 | €3,32 | €-0,94 |
| FAST NoHigh <7,5 · SHORT only | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,05376 | €14,15 | €42,44 | €0,48 | €-0,06 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1969,50000 | 1930,05275 | 1315,29231 | 2014,64922 | €32,22 | €96,65 | €1,39 | €0,56 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €392,53 | €1.177,60 | €51,08 | €-14,48 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €1.490,87 | €4.472,61 | €0,00 | €58,76 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €13,99 | €41,96 | €0,47 | €-0,06 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €11,18 | €33,53 | €0,00 | €0,44 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,41523 | 59,96100 | 59,73858 | 40,57889 | 61,76853 | €19,28 | €57,83 | €0,65 | €-0,43 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €827,61 | €2.482,82 | €49,93 | €-13,96 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,30 | €1.170,89 | €50,79 | €-14,40 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,89 | €1.172,67 | €50,86 | €-14,42 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €58,50 | €175,50 | €0,00 | €2,31 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €850,77 | €2.552,31 | €51,33 | €-14,35 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €828,72 | €2.486,15 | €50,00 | €-13,97 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €17,30 | €51,91 | €0,58 | €-0,07 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €863,11 | €2.589,32 | €52,07 | €-14,55 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €386,01 | €1.158,04 | €50,23 | €-14,24 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €1.443,11 | €4.329,34 | €0,00 | €56,88 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €13,53 | €40,59 | €0,45 | €-0,06 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €841,62 | €2.524,86 | €50,78 | €-14,19 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €397,61 | €1.192,82 | €51,74 | €-14,67 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €1.522,40 | €4.567,21 | €0,00 | €60,01 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €21,34 | €64,03 | €0,72 | €-0,09 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €866,38 | €2.599,13 | €52,27 | €-14,61 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €1.423,15 | €4.269,44 | €0,00 | €56,10 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €14,65 | €43,94 | €0,49 | €-0,06 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €831,59 | €2.494,76 | €50,17 | €-14,02 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,11105 | 1,10195 | 0,74853 | 1,13940 | €23,07 | €69,20 | €0,78 | €-0,21 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1952,19036 | 1969,50000 | 1957,49631 | 1311,22119 | 1995,91942 | €12,06 | €36,18 | €0,00 | €0,32 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €17,07 | €51,20 | €0,57 | €-0,07 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,11105 | 1,10195 | 0,74853 | 1,13940 | €1.516,65 | €4.549,94 | €50,96 | €-13,81 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1957,58044 | 1305,69227 | 1987,50339 | €1.489,14 | €4.467,43 | €0,00 | €58,70 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €842,32 | €2.526,96 | €50,82 | €-14,20 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,87 | €32,61 | €1,41 | €-0,40 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1969,50000 | 1949,40180 | 1305,69227 | 1987,50339 | €1.512,51 | €4.537,54 | €0,00 | €59,62 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 59,96100 | 59,37250 | 40,33023 | 61,39001 | €10,44 | €31,33 | €0,35 | €-0,04 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €36,61 | €109,84 | €4,76 | €-1,35 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,43537 | 0,43528 | 0,38312 | 0,29242 | 0,56598 | €138,89 | €416,67 | €50,00 | €-0,08 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €828,69 | €2.486,06 | €50,00 | €-0,50 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,43537 | 0,43528 | 0,38312 | 0,29242 | 0,56598 | €138,89 | €416,67 | €50,00 | €-0,08 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €828,69 | €2.486,06 | €50,00 | €-0,50 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | LONG | 2026-07-27T07:23:40+00:00 | 0,00000 | €0,70 | 0,18 | STOP |
| Combo Adaptive — parziale 1R | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €36,22 | 1,64 | TARGET |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €55,52 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €57,37 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €56,92 | 1,14 | STOP_SAME_CANDLE_CONSERVATIVE |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €57,82 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €58,16 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €55,52 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €56,49 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €57,42 | 1,13 | STOP_GAP_STRESS |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | PEPE | LONG | 2026-07-27T06:53:40+00:00 | 0,00000 | €98,23 | 1,92 | TARGET |
| Scanner Top 5 Long 1H | AKE | LONG | 2026-07-27T06:38:40+00:00 | 0,00395 | €107,57 | 2,00 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 14/30 | 13/30 | 1,39 | 4,25 | 0,23R | €19,51 | 2,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 12/30 | 16/30 | 1,31 | 2,53 | 0,19R | €23,50 | 1,62% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 12/30 | 16/30 | 1,31 | 2,59 | 0,19R | €18,53 | 2,27% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 12/30 | 17/30 | 1,31 | 1,43 | 0,19R | €7,70 | 2,38% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,02% | n/a | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 4/30 | 6/30 | 1,94 | 1,56 | 0,48R | €9,44 | 2,15% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 12/30 | 13/30 | 1,85 | 4,96 | 0,45R | €18,61 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 16/30 | 14/30 | 1,45 | 0,96 | 0,26R | €-0,94 | 2,93% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,02% | n/a | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 12/30 | 16/30 | 2,58 | 4,74 | 0,69R | €26,73 | 1,97% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 13/30 | 22/30 | 2,16 | 2,86 | 0,56R | €18,88 | 1,14% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 7/30 | 9/30 | 2,37 | 1,82 | 0,63R | €14,97 | 2,06% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 13/30 | 18/30 | 1,58 | 2,20 | 0,33R | €16,05 | 1,60% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 16/30 | 13/30 | 1,45 | 0,96 | 0,26R | €-0,98 | 3,08% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,15% | n/a | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 66/30 | 22/30 | 1,03 | 0,80 | 0,02R | €-6,82 | 4,52% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 6/30 | 0,00 | 7,16 | 0,00R | €57,42 | 1,06% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 7/30 | 0,00 | 3,63 | 0,00R | €41,37 | 1,49% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 10/30 | 5/30 | 0,31 | 0,20 | -0,54R | €-4,60 | 0,40% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 12/30 | 9/30 | 0,40 | 0,16 | -0,41R | €-6,21 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 179/30 | 50/30 | 1,03 | 1,34 | 0,02R | €6,69 | 3,25% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 11/30 | 0,00 | 0,94 | 0,00R | €-1,84 | 2,47% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 49/30 | 35/30 | 1,47 | 1,27 | 0,27R | €5,48 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 83/30 | 47/30 | 1,16 | 1,73 | 0,10R | €14,60 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 8/30 | 8/30 | 1,13 | 1,34 | 0,09R | €6,98 | 1,46% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 205/30 | 77/30 | 0,91 | 1,03 | -0,06R | €0,67 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 23/30 | 20/30 | 1,97 | 1,51 | 0,40R | €8,74 | 2,07% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 22/30 | 18/30 | 1,98 | 2,03 | 0,42R | €13,75 | 1,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 86/30 | 56/30 | 1,24 | 1,60 | 0,13R | €10,79 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 88/30 | 46/30 | 1,04 | 1,29 | 0,02R | €5,52 | 2,15% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 16/30 | 0,00 | 3,00 | 0,00R | €27,61 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 16/30 | 0,00 | 2,24 | 0,00R | €18,99 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 10/30 | 0,00 | 3,74 | 0,00R | €37,45 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 64/30 | 52/30 | 1,26 | 1,51 | 0,14R | €9,26 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 83/30 | 49/30 | 1,02 | 1,13 | 0,01R | €2,73 | 2,58% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 13/30 | 13/30 | 0,70 | 1,15 | -0,21R | €3,35 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 130/30 | 78/30 | 1,15 | 1,21 | 0,08R | €4,02 | 2,89% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 74/30 | 47/30 | 1,14 | 1,65 | 0,08R | €10,59 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 42/30 | 43/30 | 1,13 | 1,14 | 0,08R | €3,02 | 3,21% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 42/30 | 39/30 | 1,13 | 1,11 | 0,08R | €2,28 | 2,86% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 51/30 | 43/30 | 1,13 | 0,91 | 0,08R | €-1,98 | 3,67% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 10/30 | 0,00 | 2,84 | 0,00R | €29,80 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 17/30 | 0,00 | 3,46 | 0,00R | €23,44 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 85/30 | 53/30 | 1,14 | 1,07 | 0,08R | €1,43 | 2,96% | COERENTE + | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 21/30 | 0,00 | 2,21 | 0,00R | €16,26 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 29/30 | 0,00 | 2,29 | 0,00R | €13,02 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 15/30 | 0,00 | 1,58 | 0,00R | €12,66 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 84/30 | 52/30 | 1,05 | 1,10 | 0,03R | €1,98 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 52/30 | 18/30 | 1,00 | 1,17 | 0,00R | €4,77 | 3,68% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 50/30 | 39/30 | 1,12 | 0,88 | 0,07R | €-3,03 | 4,19% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 4/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 3/30 | 3/30 | ∞ | ∞ | 1,37R | €56,04 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 5/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 6/30 | 0,57 | 0,59 | -0,36R | €-14,69 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 126/30 | 25/30 | 1,16 | 1,52 | 0,10R | €8,26 | 1,49% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 39/30 | 11/30 | 1,05 | 1,28 | 0,03R | €5,96 | 2,34% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 93/30 | 30/30 | 1,08 | 0,50 | 0,05R | €-12,85 | 5,33% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 67/30 | 20/30 | 0,95 | 0,54 | -0,03R | €-13,64 | 3,32% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 7/30 | 7/30 | 0,74 | 0,57 | -0,19R | €-12,91 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 7/30 | 7/30 | 0,74 | 0,18 | -0,19R | €-25,99 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 20/30 | 17/30 | 1,54 | 1,94 | 0,31R | €9,96 | 1,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 31/30 | 12/30 | 0,44 | 0,81 | -0,49R | €-5,24 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 40/30 | 23/30 | 0,58 | 1,42 | -0,37R | €8,24 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 13/30 | 0,00 | 3,73 | 0,00R | €22,74 | 1,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 40/30 | 13/30 | 0,58 | 0,76 | -0,37R | €-5,13 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 19/30 | 17/30 | 1,02 | 0,99 | 0,01R | €-0,30 | 2,31% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 76/30 | 35/30 | 1,58 | 0,99 | 0,34R | €-0,16 | 3,25% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 100/30 | 39/30 | 1,07 | 0,78 | 0,05R | €-7,92 | 7,02% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 13/30 | 0,00 | 2,39 | 0,00R | €17,87 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 3/30 | 4/30 | 0,84 | 0,98 | -0,12R | €-0,31 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 4/30 | 8/30 | 1,71 | 1,55 | 0,39R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 61/30 | 27/30 | 0,91 | 2,13 | -0,07R | €22,30 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 104/30 | 27/30 | 1,09 | 0,96 | 0,06R | €-0,99 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 5/30 | 5/30 | 0,42 | 0,11 | -0,51R | €-29,22 | 1,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 2/30 | 0,00 | 0,28 | -1,13R | €-20,26 | 0,91% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 4/30 | 4/30 | 0,56 | 0,56 | -0,37R | €-18,17 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 5/30 | 7/30 | 0,43 | 0,20 | -0,51R | €-31,18 | 2,52% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 10/30 | 1,75 | 0,37 | 0,41R | €-20,93 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 35/30 | 15/30 | 1,11 | 0,78 | 0,07R | €-9,01 | 3,64% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 14/30 | 0,00 | 1,08 | 0,00R | €2,06 | 3,15% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 10/30 | 0,00 | 1,16 | 0,00R | €5,42 | 3,63% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 8/30 | 0,00 | 1,14 | 0,00R | €4,79 | 2,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 35/30 | 48/30 | 0,99 | 0,61 | -0,01R | €-6,99 | 4,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 32/30 | 12/30 | 0,99 | 0,68 | -0,01R | €-14,63 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 27/30 | 14/30 | 1,00 | 0,74 | -0,00R | €-10,49 | 3,98% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 30/30 | 21/30 | 0,95 | 0,57 | -0,04R | €-20,33 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 35/30 | 12/30 | 0,99 | 0,68 | -0,01R | €-14,97 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 130/30 | 29/30 | 1,04 | 0,66 | 0,03R | €-10,20 | 6,18% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 48/30 | 41/30 | 1,61 | 1,05 | 0,36R | €1,80 | 5,10% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 50/30 | 29/30 | 0,80 | 0,61 | -0,14R | €-9,96 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 2/30 | 6/30 | 0,00 | 0,54 | -1,10R | €-12,45 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 2/30 | 5/30 | 0,00 | 0,25 | -1,10R | €-24,00 | 1,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 10/30 | 10/30 | 2,86 | 0,86 | 0,77R | €-3,57 | 3,62% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 10/30 | 10/30 | 2,86 | 0,86 | 0,77R | €-3,57 | 3,62% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 10/30 | 10/30 | 2,86 | 0,86 | 0,77R | €-3,57 | 3,62% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 74/30 | 30/30 | 1,56 | 1,60 | 0,33R | €13,99 | 3,23% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 14/30 | 6/30 | 1,14 | 0,93 | 0,09R | €-2,09 | 2,84% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 32/30 | 12/30 | 1,26 | 1,02 | 0,17R | €0,61 | 3,23% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 26/30 | 26/30 | 1,57 | 0,67 | 0,33R | €-9,56 | 3,93% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 26/30 | 12/30 | 1,57 | 1,09 | 0,33R | €3,07 | 3,23% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 29/30 | 29/30 | 1,29 | 0,58 | 0,19R | €-12,39 | 5,08% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 29/30 | 17/30 | 1,29 | 0,78 | 0,19R | €-7,55 | 3,36% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 36/30 | 21/30 | 1,22 | 0,62 | 0,14R | €-8,89 | 3,95% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 27/30 | 17/30 | 1,41 | 1,31 | 0,29R | €8,50 | 3,25% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 27/30 | 13/30 | 1,41 | 1,33 | 0,29R | €11,64 | 3,22% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 88/30 | 38/30 | 1,44 | 1,74 | 0,25R | €16,59 | 3,57% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 6/30 | 6/30 | 0,85 | 0,29 | -0,11R | €-27,47 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 3/30 | 4/30 | 0,60 | 0,41 | -0,30R | €-24,69 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,75% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 5/30 | 5/30 | 1,14 | 0,86 | 0,09R | €-4,58 | 1,67% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,97% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07298**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.6 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65416.7 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, volume_valid**
- High **0.073**; close **0.07298**; wick alta **6.7%**; volume **x1.91**

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
- Confidenza: **71,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +2.0, 92% sopra EMA50, ADX 19.4.
- BTC trend score: **2,00**; ADX: **19,38**; breadth sopra EMA50: **91,67%**
- Mediana alt vs BTC: **0,91%**; dispersione: **13,92%**

- Aperti in questo ciclo: **6**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **711**
- Trade research chiusi: **3539**
- Eventi di mercato indipendenti chiusi: **864**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **17499**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 6 | 14 | 14 | 42,86% | 1,39 | 0,23R | €32,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 4 | 12 | 12 | 41,67% | 1,31 | 0,19R | €22,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 4 | 12 | 12 | 41,67% | 1,31 | 0,19R | €22,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 7 | 12 | 12 | 41,67% | 1,31 | 0,19R | €23,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 3 | 4 | 4 | 50,00% | 1,94 | 0,48R | €19,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 3 | 12 | 12 | 50,00% | 1,85 | 0,45R | €53,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 8 | 16 | 16 | 43,75% | 1,45 | 0,26R | €42,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 7 | 12 | 12 | 58,33% | 2,58 | 0,69R | €82,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 8 | 13 | 13 | 53,85% | 2,16 | 0,56R | €72,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 7 | 7 | 57,14% | 2,37 | 0,63R | €44,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 8 | 13 | 13 | 46,15% | 1,58 | 0,33R | €42,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 9 | 16 | 16 | 43,75% | 1,45 | 0,26R | €42,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | 15 | 66 | 66 | 34,85% | 1,03 | 0,02R | €13,46 |
| RSI_EXTREME_LONG_15M | 1 | 10 | 10 | 30,00% | 0,31 | -0,54R | €-54,33 |
| RSI_EXTREME_SHORT_15M | 1 | 12 | 12 | 33,33% | 0,40 | -0,41R | €-49,15 |
| Bilanciata 1H V1 | 18 | 179 | 179 | 34,64% | 1,03 | 0,02R | €34,21 |
| Bilanciata 1H V2 | 9 | 56 | 49 | 42,86% | 1,47 | 0,27R | €149,88 |
| Bilanciata 1H V3 Filtered | 12 | 83 | 83 | 37,35% | 1,16 | 0,10R | €84,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 7 | 8 | 8 | 37,50% | 1,13 | 0,09R | €6,88 |
| Rapida 1H V1 | 3 | 205 | 205 | 39,02% | 0,91 | -0,06R | €-113,51 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 3 | 23 | 23 | 56,52% | 1,97 | 0,40R | €92,55 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 6 | 22 | 22 | 59,09% | 1,98 | 0,42R | €92,32 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 9 | 86 | 86 | 47,67% | 1,24 | 0,13R | €114,51 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 11 | 88 | 88 | 43,18% | 1,04 | 0,02R | €19,58 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 64 | 64 | 48,44% | 1,26 | 0,14R | €90,01 |
| SHADOW_1H_FAST_TP2_V1 | 13 | 83 | 83 | 36,14% | 1,02 | 0,01R | €11,05 |
| Rapida 1H V2 | 3 | 14 | 13 | 35,71% | 0,70 | -0,21R | €-29,31 |
| Rapida 1H V3 Filtered | 12 | 130 | 130 | 45,38% | 1,15 | 0,08R | €106,96 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 9 | 74 | 74 | 45,95% | 1,14 | 0,08R | €58,67 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 4 | 42 | 42 | 45,24% | 1,13 | 0,08R | €32,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 4 | 42 | 42 | 45,24% | 1,13 | 0,08R | €32,64 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 7 | 51 | 51 | 45,10% | 1,13 | 0,08R | €38,30 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 12 | 85 | 85 | 45,88% | 1,14 | 0,08R | €66,11 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 11 | 84 | 84 | 44,05% | 1,05 | 0,03R | €24,87 |
| SHADOW_4H_WIDE | 25 | 52 | 52 | 26,92% | 1,00 | 0,00R | €1,54 |
| SHADOW_BOLLINGER_MR_1H | 7 | 50 | 50 | 46,00% | 1,12 | 0,07R | €34,95 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,44 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 3 | 3 | 100,00% | ∞ | 1,37R | €41,00 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 5 | 5 | 0,00% | 0,00 | -1,12R | €-56,25 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 19 | 126 | 126 | 38,10% | 1,16 | 0,10R | €129,45 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 12 | 39 | 39 | 35,90% | 1,05 | 0,03R | €13,02 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 19 | 93 | 93 | 36,56% | 1,08 | 0,05R | €48,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 19 | 67 | 67 | 34,33% | 0,95 | -0,03R | €-21,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 7 | 7 | 28,57% | 0,74 | -0,19R | €-13,41 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 7 | 7 | 28,57% | 0,74 | -0,19R | €-13,41 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 6 | 20 | 20 | 45,00% | 1,54 | 0,31R | €62,69 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 8 | 31 | 31 | 19,35% | 0,44 | -0,49R | €-150,46 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 7 | 40 | 40 | 17,50% | 0,58 | -0,37R | €-147,89 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 7 | 40 | 40 | 17,50% | 0,58 | -0,37R | €-147,89 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 19 | 19 | 42,11% | 1,02 | 0,01R | €2,78 |
| SHADOW_COMBO_SCANNER | 11 | 76 | 76 | 43,42% | 1,58 | 0,34R | €255,81 |
| SHADOW_COMBO_TREND | 18 | 100 | 100 | 34,00% | 1,07 | 0,05R | €50,03 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | 11 | 61 | 61 | 27,87% | 0,91 | -0,07R | €-41,56 |
| SHADOW_EMA_TREND_1H | 19 | 104 | 104 | 33,65% | 1,09 | 0,06R | €61,00 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 5 | 5 | 20,00% | 0,42 | -0,51R | €-25,56 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 4 | 4 | 25,00% | 0,56 | -0,37R | €-14,86 |
| SHADOW_ETH_EMA_1H | 1 | 5 | 5 | 20,00% | 0,43 | -0,51R | €-25,44 |
| SHADOW_ETH_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 0 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 13 | 35 | 35 | 37,14% | 1,11 | 0,07R | €25,93 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 13 | 35 | 35 | 34,29% | 0,99 | -0,01R | €-3,28 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 12 | 32 | 32 | 34,38% | 0,99 | -0,01R | €-2,02 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 13 | 27 | 27 | 25,93% | 1,00 | -0,00R | €-0,84 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 8 | 30 | 30 | 33,33% | 0,95 | -0,04R | €-10,53 |
| SHADOW_MASTER_ADAPTIVE_V1 | 13 | 35 | 35 | 34,29% | 0,99 | -0,01R | €-3,28 |
| Forza relativa 1H V1 | 19 | 130 | 130 | 32,31% | 1,04 | 0,03R | €32,68 |
| Forza relativa 1H V2 | 8 | 53 | 48 | 43,40% | 1,61 | 0,36R | €188,42 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 6 | 50 | 50 | 28,00% | 0,80 | -0,14R | €-67,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | 7 | 10 | 10 | 60,00% | 2,86 | 0,77R | €76,85 |
| SHADOW_SCANNER_TOP15_LONG | 8 | 10 | 10 | 60,00% | 2,86 | 0,77R | €76,85 |
| SHADOW_SCANNER_TOP20_LONG | 8 | 10 | 10 | 60,00% | 2,86 | 0,77R | €76,85 |
| SHADOW_SCANNER_TOP5_BTC | 11 | 74 | 74 | 41,89% | 1,56 | 0,33R | €242,90 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 8 | 14 | 14 | 35,71% | 1,14 | 0,09R | €13,07 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 11 | 32 | 32 | 37,50% | 1,26 | 0,17R | €53,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 8 | 26 | 26 | 42,31% | 1,57 | 0,33R | €86,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 8 | 26 | 26 | 42,31% | 1,57 | 0,33R | €86,54 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 8 | 29 | 29 | 37,93% | 1,29 | 0,19R | €53,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 8 | 29 | 29 | 37,93% | 1,29 | 0,19R | €53,95 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 11 | 36 | 36 | 36,11% | 1,22 | 0,14R | €51,20 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 12 | 27 | 27 | 33,33% | 1,41 | 0,29R | €78,34 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 12 | 27 | 27 | 33,33% | 1,41 | 0,29R | €78,34 |
| SHADOW_SCANNER_TOP5_LONG | 10 | 88 | 88 | 42,05% | 1,44 | 0,25R | €220,57 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,52 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 0 | 5 | 5 | 40,00% | 1,14 | 0,09R | €4,59 |
| SHADOW_SOL_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 2 | 10 | 10 | 50,00% | 1,82 | 0,43R | €43,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 2 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 2 | 8 | 8 | 50,00% | 1,78 | 0,42R | €33,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 2 | 8 | 8 | 50,00% | 1,78 | 0,42R | €33,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 1 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 2 | 6 | 6 | 50,00% | 1,77 | 0,41R | €24,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 1 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 3 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 2 | 8 | 8 | 50,00% | 1,81 | 0,43R | €34,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 1 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 3 | 8 | 8 | 50,00% | 1,81 | 0,43R | €34,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 2 | 7 | 7 | 57,14% | 2,37 | 0,63R | €44,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 1 | 4 | 4 | 75,00% | 5,78 | 1,21R | €48,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 3 | 7 | 7 | 57,14% | 2,37 | 0,63R | €44,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 5 | 5 | 60,00% | 2,89 | 0,77R | €38,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 1 | 6 | 6 | 50,00% | 1,77 | 0,41R | €24,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 3 | 6 | 6 | 50,00% | 1,77 | 0,41R | €24,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 1 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 3 | 8 | 8 | 50,00% | 1,81 | 0,43R | €34,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 1 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,88 |
| MAIN | ALT_ROTATION_UP | 4 | 8 | 8 | 0,00% | 0,00 | -1,02R | €-81,72 |
| MAIN | RANGE | 7 | 25 | 25 | 36,00% | 1,08 | 0,06R | €13,82 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,18 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 1 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,05 | -0,86R | €-34,43 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 1 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,38 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 5 | 17 | 17 | 47,06% | 1,64 | 0,35R | €60,25 |
| Bilanciata 1H V1 | RANGE | 5 | 51 | 51 | 41,18% | 1,33 | 0,20R | €101,69 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 0 | 30 | 30 | 33,33% | 1,00 | -0,00R | €-0,05 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Bilanciata 1H V1 | TREND_UP | 3 | 43 | 43 | 39,53% | 1,31 | 0,18R | €77,80 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 5 | 8 | 6 | 50,00% | 1,82 | 0,43R | €34,69 |
| Bilanciata 1H V2 | RANGE | 4 | 28 | 26 | 39,29% | 1,25 | 0,15R | €42,71 |
| Bilanciata 1H V2 | TRANSITION | 0 | 20 | 17 | 45,00% | 1,69 | 0,36R | €72,49 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 1,04 | 0,03R | €3,17 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 5 | 5 | 5 | 40,00% | 1,25 | 0,16R | €7,84 |
| Bilanciata 1H V3 Filtered | RANGE | 5 | 20 | 20 | 50,00% | 1,83 | 0,44R | €88,50 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 21 | 21 | 42,86% | 1,53 | 0,29R | €60,84 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 5 | 3 | 3 | 66,67% | 3,79 | 0,96R | €28,83 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,25 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 1 | 21 | 21 | 23,81% | 0,43 | -0,43R | €-90,26 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 2 | 65 | 65 | 44,62% | 1,16 | 0,09R | €58,28 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,83R | €-41,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 6 | 6 | 50,00% | 1,29 | 0,15R | €9,22 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 1 | 5 | 5 | 100,00% | ∞ | 1,47R | €73,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 1 | 4 | 4 | 50,00% | 1,35 | 0,19R | €7,75 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 3 | 12 | 12 | 50,00% | 1,34 | 0,18R | €21,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 4 | 4 | 50,00% | 1,41 | 0,21R | €8,41 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 1 | 2 | 2 | 100,00% | ∞ | 1,42R | €28,35 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,40 | -0,46R | €-82,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 3 | 13 | 13 | 53,85% | 1,56 | 0,27R | €35,45 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 4 | 31 | 31 | 61,29% | 2,09 | 0,46R | €141,45 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 1 | 18 | 18 | 33,33% | 0,66 | -0,24R | €-43,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 21,05% | 0,38 | -0,49R | €-92,40 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 2 | 13 | 13 | 46,15% | 1,11 | 0,07R | €8,60 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 3 | 33 | 33 | 54,55% | 1,60 | 0,29R | €96,40 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,48R | €44,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 3 | 15 | 15 | 26,67% | 0,49 | -0,40R | €-60,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 33,33% | 0,65 | -0,25R | €-30,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 15 | 15 | 46,67% | 1,17 | 0,10R | €14,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 24 | 24 | 62,50% | 2,24 | 0,50R | €118,84 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,37 | -0,53R | €-47,60 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 15,79% | 0,36 | -0,54R | €-102,47 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 2 | 15 | 15 | 46,67% | 1,54 | 0,31R | €46,62 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 28 | 28 | 46,43% | 1,50 | 0,28R | €79,75 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,39 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,95R | €58,62 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 4 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V2 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,62 | -0,28R | €-8,35 |
| Rapida 1H V2 | RANGE | 2 | 10 | 9 | 40,00% | 0,85 | -0,10R | €-9,53 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 21 | 21 | 28,57% | 0,52 | -0,36R | €-75,39 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 2 | 14 | 14 | 57,14% | 1,76 | 0,35R | €49,03 |
| Rapida 1H V3 Filtered | RANGE | 4 | 32 | 32 | 56,25% | 1,72 | 0,34R | €108,45 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 7 | 7 | 57,14% | 1,83 | 0,38R | €26,94 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| Rapida 1H V3 Filtered | TREND_UP | 3 | 31 | 31 | 51,61% | 1,45 | 0,23R | €71,35 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,78 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 15 | 15 | 46,67% | 1,15 | 0,09R | €13,25 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 5 | 26 | 26 | 61,54% | 2,14 | 0,47R | €122,24 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 13 | 13 | 30,77% | 0,58 | -0,31R | €-40,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 2 | 11 | 11 | 45,45% | 1,11 | 0,07R | €7,21 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 14 | 14 | 64,29% | 2,60 | 0,59R | €82,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 9 | 9 | 33,33% | 0,63 | -0,27R | €-24,31 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 11 | 11 | 45,45% | 1,11 | 0,07R | €7,21 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 14 | 14 | 64,29% | 2,60 | 0,59R | €82,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 9 | 9 | 33,33% | 0,63 | -0,27R | €-24,31 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 12 | 12 | 50,00% | 1,29 | 0,16R | €18,80 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 18 | 18 | 61,11% | 2,28 | 0,51R | €91,11 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 3 | 8 | 8 | 25,00% | 0,43 | -0,48R | €-38,01 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 2 | 11 | 11 | 54,55% | 1,59 | 0,29R | €31,60 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 4 | 32 | 32 | 56,25% | 1,72 | 0,34R | €108,45 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 3 | 16 | 16 | 31,25% | 0,59 | -0,30R | €-48,70 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 2 | 13 | 13 | 46,15% | 1,10 | 0,06R | €7,91 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 3 | 31 | 31 | 54,84% | 1,62 | 0,30R | €93,59 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 3 | 14 | 14 | 28,57% | 0,52 | -0,37R | €-51,39 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 2,79R | €55,73 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_4H_WIDE | RANGE | 10 | 21 | 21 | 23,81% | 0,85 | -0,12R | €-24,87 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 14 | 14 | 42,86% | 2,03 | 0,61R | €84,85 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 2 | 6 | 6 | 16,67% | 0,27 | -0,65R | €-38,82 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 2 | 19 | 19 | 47,37% | 1,16 | 0,09R | €17,24 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 3 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,75 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 5 | 9 | 9 | 44,44% | 1,48 | 0,28R | €25,00 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 4 | 40 | 40 | 42,50% | 1,34 | 0,21R | €84,86 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 20 | 20 | 45,00% | 1,65 | 0,34R | €68,99 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 5 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 7 | 7 | 57,14% | 2,42 | 0,64R | €45,11 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 2 | 13 | 13 | 61,54% | 3,12 | 0,83R | €107,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 4 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 5 | 10 | 10 | 40,00% | 1,22 | 0,14R | €13,89 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 4 | 28 | 28 | 50,00% | 1,83 | 0,44R | €123,33 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 4 | 4 | 50,00% | 1,78 | 0,43R | €17,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 5 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 5 | 7 | 7 | 57,14% | 2,42 | 0,64R | €45,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 4 | 28 | 28 | 50,00% | 1,83 | 0,44R | €123,33 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,91 | -0,07R | €-1,99 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 5 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,63 | -0,29R | €-11,69 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,63 | -0,29R | €-11,69 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,34 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 12 | 12 | 66,67% | 3,84 | 0,98R | €117,20 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 8 | 8 | 25,00% | 0,60 | -0,32R | €-25,89 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 8 | 15 | 15 | 20,00% | 0,46 | -0,46R | €-68,71 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 11 | 11 | 45,45% | 1,15 | 0,09R | €9,62 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 1 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 2 | 7 | 7 | 42,86% | 1,55 | 0,33R | €23,06 |
| SHADOW_COMBO_SCANNER | RANGE | 2 | 17 | 17 | 58,82% | 3,00 | 0,85R | €144,23 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 15 | 15 | 46,67% | 1,60 | 0,34R | €50,68 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 5 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,57 | -0,35R | €-31,72 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 5 | 8 | 8 | 37,50% | 1,24 | 0,16R | €12,65 |
| SHADOW_COMBO_TREND | RANGE | 3 | 31 | 31 | 38,71% | 1,29 | 0,19R | €58,86 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 16 | 16 | 43,75% | 1,79 | 0,42R | €67,09 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 20,00% | 0,51 | -0,41R | €-41,36 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 9 | 9 | 22,22% | 0,65 | -0,29R | €-25,72 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 3 | 5 | 5 | 20,00% | 0,58 | -0,35R | €-17,42 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 20 | 20 | 30,00% | 0,99 | -0,01R | €-2,06 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 0 | 7 | 7 | 14,29% | 0,45 | -0,42R | €-29,27 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,57 | -0,35R | €-31,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 5 | 8 | 8 | 25,00% | 0,69 | -0,25R | €-19,68 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 29 | 29 | 41,38% | 1,54 | 0,31R | €91,14 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 17 | 17 | 41,18% | 1,59 | 0,33R | €56,40 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_EMA_TREND_1H | TREND_UP | 4 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-9,03 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 14,29% | 0,32 | -0,60R | €-41,93 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 1 | 4 | 4 | 25,00% | 0,62 | -0,30R | €-11,90 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 10 | 10 | 60,00% | 2,93 | 0,78R | €78,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,96R | €58,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 7 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 1,22 | 0,14R | €6,92 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 11 | 11 | 63,64% | 3,41 | 0,89R | €98,08 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 7 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 11 | 11 | 63,64% | 3,41 | 0,89R | €98,08 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 7 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,46 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 11 | 11 | 45,45% | 2,45 | 0,80R | €88,08 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 5 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 14 | 14 | 64,29% | 3,52 | 0,91R | €127,72 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 5 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 1,22 | 0,14R | €6,92 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 11 | 11 | 63,64% | 3,41 | 0,89R | €98,08 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 7 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 3 | 9 | 9 | 11,11% | 0,26 | -0,69R | €-61,85 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 3 | 17 | 17 | 29,41% | 0,85 | -0,11R | €-19,14 |
| Forza relativa 1H V1 | RANGE | 6 | 38 | 38 | 34,21% | 1,11 | 0,08R | €28,71 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 0 | 16 | 16 | 50,00% | 2,11 | 0,57R | €91,12 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Forza relativa 1H V1 | TREND_UP | 5 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 50,00% | 2,02 | 0,53R | €32,04 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 3 | 6 | 5 | 33,33% | 1,02 | 0,02R | €0,99 |
| Forza relativa 1H V2 | RANGE | 1 | 13 | 13 | 61,54% | 3,40 | 0,95R | €123,51 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 0 | 13 | 11 | 38,46% | 1,31 | 0,20R | €25,87 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TREND_UP | 1 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 5 | 5 | 60,00% | 2,62 | 0,71R | €35,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 20 | 20 | 30,00% | 0,75 | -0,19R | €-37,65 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 3 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,75 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 5 | 5 | 100,00% | ∞ | 1,98R | €98,91 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,75 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 5 | 5 | 100,00% | ∞ | 1,98R | €98,91 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,75 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 5 | 5 | 100,00% | ∞ | 1,98R | €98,91 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 2 | 8 | 8 | 37,50% | 1,24 | 0,16R | €12,54 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 17 | 17 | 58,82% | 3,51 | 0,91R | €155,18 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 13 | 13 | 46,15% | 1,79 | 0,45R | €58,04 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 5 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,19 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 4 | 3 | 3 | 66,67% | 3,93 | 1,09R | €32,59 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,67 | -0,27R | €-10,61 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 12 | 12 | 58,33% | 3,01 | 0,85R | €101,95 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 4 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,01 | 0,00R | €0,12 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 2 | 12 | 12 | 58,33% | 3,01 | 0,85R | €101,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 3 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,01 | 0,00R | €0,12 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 2 | 12 | 12 | 58,33% | 3,01 | 0,85R | €101,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 3 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,01 | 0,00R | €0,12 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 2 | 12 | 12 | 58,33% | 3,01 | 0,85R | €101,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 4 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,01 | 0,00R | €0,12 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 2 | 12 | 12 | 58,33% | 3,01 | 0,85R | €101,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 4 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,67 | -0,26R | €-10,54 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 2 | 12 | 12 | 58,33% | 3,01 | 0,85R | €101,95 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 5 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 7 | 7 | 28,57% | 1,09 | 0,07R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 2 | 10 | 10 | 50,00% | 2,93 | 0,98R | €98,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 5 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 7 | 7 | 28,57% | 1,09 | 0,07R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 2 | 10 | 10 | 50,00% | 2,93 | 0,98R | €98,19 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 5 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 2 | 9 | 9 | 33,33% | 0,92 | -0,06R | €-5,06 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 18 | 18 | 61,11% | 3,51 | 0,86R | €155,05 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 4 | 29 | 29 | 48,28% | 1,84 | 0,43R | €125,07 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-27T07:23:51+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **814**
- Scenari virtuali ancora attivi: **12210**
- Gruppi in attesa dell'uscita originale: **340**
- Gruppi con originale chiuso ma Shadow ancora attive: **474**
- Confronti completati: **55562**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 1914 | 1979 | +€4,18 | 47,0% | 654 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 1914 | 1979 | +€2,37 | 45,0% | 671 | 16 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 1914 | 1979 | +€0,17 | 43,7% | 681 | 38 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 1914 | 1979 | €-0,77 | 43,1% | 737 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 1912 | 1977 | €-1,25 | 43,1% | 643 | 87 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 1896 | 1961 | +€4,49 | 43,7% | 538 | 45 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 1896 | 1961 | +€1,24 | 40,4% | 606 | 43 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 1895 | 1960 | +€2,44 | 43,1% | 525 | 71 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 1879 | 1944 | +€1,10 | 42,8% | 443 | 131 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 1866 | 1931 | +€3,42 | 32,4% | 315 | 195 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 1859 | 1924 | €-0,32 | 40,6% | 366 | 249 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 1859 | 1924 | €-4,17 | 43,0% | 483 | 309 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 1855 | 1920 | €-3,48 | 32,9% | 276 | 431 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 1852 | 1917 | €-2,45 | 39,2% | 279 | 466 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 1829 | 1894 | +€5,64 | 40,0% | 165 | 301 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 1813 | 1878 | €-6,10 | 29,4% | 237 | 497 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 1779 | 1844 | €-4,08 | 35,1% | 160 | 532 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 1777 | 1842 | €-10,72 | 27,5% | 189 | 532 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 1727 | 1792 | €-13,77 | 27,3% | 423 | 352 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 1600 | 1665 | €-19,44 | 20,5% | 188 | 517 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-27T07:23:54+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **55562**
- Valutazioni prodotte: **15838**
- Candidature al Blocco 5: **1**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
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
| TP_R035 | 40 | 3,103 | 4,188 | 2,510 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB20_R100 | 40 | 3,424 | 4,831 | 2,706 | 87,5% | 87,3 | EARLY_SIGNAL |
| ATR15_R100 | 40 | 2,858 | 4,115 | 2,143 | 87,5% | 87,3 | EARLY_SIGNAL |

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

Generato: 2026-07-27T07:24:33+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 21 | 100,00% | 1,35 | +€125,64 | +€5,98 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 21 | 100,00% | 1,17 | +€60,61 | +€2,89 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 7 | 100,00% | 1,62 | +€60,25 | +€8,61 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 7 | 100,00% | 1,40 | +€39,37 | +€5,62 | 0,54% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 1 | 100,00% | 0,00 | €-50,14 | €-50,14 | 0,50% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 1 | 50,00% | 0,00 | €-46,66 | €-46,66 | 0,47% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 2 | 100,00% | 0,94 | €-0,03 | €-0,01 | 0,00% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-27T07:23:40+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **2**
- Simulazioni bloccate attive: **113**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-17.73 R**
- Profitto virtuale mancato: **256.41 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 238 | 2 | 31494.28 |
| DOWN_20 | 238 | 3 | 62928.55 |
| DOWN_30 | 238 | 3 | 94341.26 |
| DOWN_40 | 238 | 91 | 117427.93 |
| UP_10 | 99 | 2 | 13193.70 |
| UP_20 | 99 | 3 | 26327.39 |
| UP_30 | 99 | 3 | 39344.34 |
| UP_40 | 99 | 53 | 47360.89 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-27T07:23:13+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **16**
- Nuovi candidati nel ciclo: **2**
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
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-27T07:24:34+00:00

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

Generato: 2026-07-27T07:24:34+00:00

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

Generato: 2026-07-27T07:24:34+00:00

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

Generato: 2026-07-27T07:24:34+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **141**
- Hall of Fame: **20**
- Memorie genetiche: **4**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 19.1 | E | 38 | 1.82 | 0.349 | 5.96 |
| 2 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 18.3 | E | 56 | 1.62 | 0.238 | 5.40 |
| 3 | SHADOW_1H_BALANCED_V3 | BASELINE | 18.0 | E | 47 | 1.65 | 0.268 | 3.23 |
| 4 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 17.3 | E | 47 | 1.56 | 0.205 | 3.68 |
| 5 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 17.1 | E | 52 | 1.52 | 0.186 | 3.71 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 16.7 | E | 78 | 1.35 | 0.139 | 5.36 |
| 7 | SHADOW_SCANNER_TOP5_BTC | BASELINE | 16.2 | E | 30 | 1.62 | 0.288 | 5.51 |
| 8 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 15.8 | E | 46 | 1.46 | 0.183 | 3.55 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 14.1 | E | 52 | 1.30 | 0.130 | 4.74 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 13.6 | E | 53 | 1.25 | 0.117 | 5.53 |

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

Generato: 2026-07-27T07:24:34+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **493**
- Strategie preferite nel regime corrente: **8**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **236**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 82.3 | 14 | 3.24 | 0.664 | 2.17 |
| 2 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | INSUFFICIENT | 81.7 | 8 | 5.66 | 0.606 | 1.03 |
| 3 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.115 | 0.00 |
| 4 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 5 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 6 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | shadow-combo-adaptive-side-regime-guard-v1 | OBSERVING | 80.3 | 11 | 4.46 | 0.666 | 1.09 |
| 7 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 8 | EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | momentum_breakout_v3_filtered | INSUFFICIENT | 79.6 | 9 | 3.33 | 0.652 | 2.10 |
| 9 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | OBSERVING | 78.3 | 14 | 3.08 | 0.631 | 3.16 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | OBSERVING | 78.2 | 10 | 2.86 | 0.593 | 2.17 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-27T07:24:34+00:00

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

Generato: 2026-07-27T07:23:40+00:00

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
