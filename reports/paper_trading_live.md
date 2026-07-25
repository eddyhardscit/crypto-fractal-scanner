# Paper trading automatico KuCoin

Generato: 2026-07-25T14:54:03+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-25T14:53:27+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-25T14:53:27+00:00 | 2026-07-25T14:53:27+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-25T14:30:00+00:00 | 2026-07-25T14:30:00+00:00 | 8,6 min | 25,0 min | OK |
| 60m | 12 | 2026-07-25T13:00:00+00:00 | 2026-07-25T13:00:00+00:00 | 53,6 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-25T08:00:00+00:00 | 2026-07-25T08:00:00+00:00 | 2,89 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -8,47 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XMR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -7,39 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,29 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -5,16 | 6,00 | 0,84 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ALLO | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,49 | 6,00 | 1,51 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -3,75 | 6,00 | 2,25 | STALE_CANDLE | 2,89 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,63 | 6,00 | 2,37 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,10 | 6,00 | 5,90 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Ampia 4H | DOGE | 240m | SHORT | -8,47 | 5,00 | 0,00 | STALE_CANDLE | 2,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| MAIN — Side × Regime Guard | DOGE | 240m | SHORT | -8,47 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| MAIN — Dynamic Asset Selector | DOGE | 240m | SHORT | -8,47 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | ALLO | 60m | SHORT | -8,25 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.6 minuti; tolleranza 45 minuti. |
| Bilanciata 1H — LONG senza Range High Vol | ALLO | 60m | SHORT | -8,25 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.6 minuti; tolleranza 45 minuti. |
| Bilanciata 1H — SHORT Trend Down stretto | ALLO | 60m | SHORT | -8,25 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.6 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V2 | ALLO | 60m | SHORT | -8,25 | 5,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.6 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V3 Filtered | ALLO | 60m | SHORT | -8,25 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.6 minuti; tolleranza 45 minuti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.923,10 | -0,77% | €-76,90 | €3.000,00 | -2,56% | 5 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 568 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.923,10 | €1.483,21 | €4.449,64 | €149,83 | €-22,39 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.827,06 | €1.607,98 | €3.215,95 | €161,89 | €95,76 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.585,52 | €1.630,72 | €3.261,45 | €158,28 | €93,33 |
| TEST | Bilanciata 1H V1 | 5 | €10.567,78 | €2.600,46 | €7.801,37 | €55,23 | €133,73 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.546,83 | €2.155,01 | €6.465,04 | €158,51 | €70,94 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.424,56 | €4.172,32 | €12.516,95 | €154,32 | €-6,27 |
| TEST | Forza relativa 1H V2 | 5 | €10.420,54 | €1.900,58 | €3.801,16 | €54,51 | €182,18 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.349,09 | €2.991,37 | €5.982,74 | €154,30 | €81,80 |
| TEST | Rapida V3 — score <7,5 | 3 | €10.332,34 | €2.889,52 | €8.668,56 | €154,42 | €-12,04 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.322,99 | €1.276,03 | €3.828,10 | €102,71 | €37,18 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €10.303,20 | €1.579,75 | €3.159,50 | €154,42 | €164,23 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.297,20 | €3.646,41 | €10.939,24 | €206,68 | €41,02 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.287,32 | €1.605,43 | €3.210,87 | €153,82 | €91,02 |
| TEST | Rapida V3 NoHigh — Regime Guard | 4 | €10.286,11 | €2.586,99 | €7.760,97 | €151,92 | €71,65 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 3 | €10.278,94 | €2.874,56 | €8.623,69 | €153,62 | €-11,98 |
| TEST | Bilanciata 1H V2 | 4 | €10.273,09 | €1.496,10 | €4.488,29 | €104,80 | €88,17 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €10.262,82 | €1.532,61 | €4.597,82 | €154,25 | €37,22 |
| TEST | Rapida score 6–7,5 — Range Only | 3 | €10.262,82 | €1.532,61 | €4.597,82 | €154,25 | €37,22 |
| TEST | Combo Adaptive — Side × Regime Guard | 4 | €10.253,66 | €3.488,24 | €6.976,47 | €101,99 | €158,50 |
| TEST | Rapida V3 NoHigh — Range Only | 3 | €10.244,92 | €2.322,33 | €6.966,98 | €151,92 | €29,98 |
| TEST | Rapida V1 — senza PEPE | 5 | €10.239,99 | €3.626,15 | €10.878,46 | €205,53 | €40,79 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.229,03 | €3.048,50 | €9.145,49 | €153,20 | €72,07 |
| TEST | Combo Adaptive — madre | 4 | €10.214,13 | €2.174,27 | €4.348,54 | €203,99 | €8,61 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €10.194,91 | €1.537,68 | €3.075,36 | €149,53 | €89,56 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €10.186,66 | €3.442,97 | €6.885,95 | €152,60 | €81,59 |
| TEST | Top 5 + BTC — BTC≤3 | 5 | €10.166,42 | €1.589,63 | €3.179,26 | €152,01 | €89,65 |
| TEST | MAIN — Dynamic Asset Selector | 3 | €10.166,10 | €994,67 | €2.984,00 | €151,25 | €68,59 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.139,24 | €1.631,86 | €4.895,57 | €201,88 | €42,88 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 4 | €10.130,61 | €2.124,92 | €4.249,84 | €50,12 | €106,82 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 4 | €10.118,31 | €2.756,36 | €5.512,72 | €200,32 | €208,57 |
| TEST | Combo Scanner | 5 | €10.102,87 | €1.618,01 | €3.236,02 | €201,52 | €39,41 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 1 | €10.099,79 | €1.088,47 | €3.265,42 | €50,22 | €16,23 |
| TEST | Btc Bollinger 1H | 1 | €10.098,40 | €1.402,77 | €4.208,32 | €50,50 | €2,05 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 2 | €10.087,47 | €2.884,57 | €8.653,70 | €100,39 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €10.084,50 | €3.572,40 | €10.717,20 | €202,40 | €36,96 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 4 | €10.083,01 | €1.998,12 | €3.996,25 | €150,47 | €69,58 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.074,89 | €4.030,03 | €8.060,05 | €96,72 | €10,65 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 3 | €10.071,65 | €640,10 | €1.920,30 | €99,87 | €84,92 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €10.070,39 | €1.394,87 | €4.184,62 | €150,05 | €113,18 |
| TEST | Scanner Top10 Long | 3 | €10.065,73 | €1.881,58 | €3.763,17 | €150,02 | €67,99 |
| TEST | Scanner Top15 Long | 3 | €10.065,73 | €1.881,58 | €3.763,17 | €150,02 | €67,99 |
| TEST | Scanner Top20 Long | 3 | €10.065,73 | €1.881,58 | €3.763,17 | €150,02 | €67,99 |
| TEST | Rapida 1H V1 — madre | 3 | €10.065,65 | €2.729,05 | €8.187,16 | €149,90 | €39,21 |
| TEST | Rapida V1 — target pieno 2R | 4 | €10.061,03 | €2.790,86 | €8.372,57 | €102,17 | €98,93 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €10.057,24 | €3.562,74 | €10.688,23 | €201,85 | €36,86 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.056,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 4 | €10.043,46 | €2.254,45 | €4.508,91 | €149,90 | €75,57 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €10.039,57 | €2.308,99 | €4.617,98 | €150,20 | €75,75 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 4 | €10.028,13 | €1.412,34 | €2.824,69 | €147,61 | €88,09 |
| TEST | Combo Mean Reversion | 3 | €10.020,94 | €3.683,13 | €7.366,26 | €97,96 | €33,23 |
| TEST | Sol Ema 1H | 1 | €10.018,45 | €1.161,12 | €3.483,35 | €50,16 | €-11,57 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 4 | €10.013,18 | €2.198,41 | €4.396,82 | €150,27 | €16,43 |
| TEST | Ampia 4H | 4 | €10.011,64 | €1.840,70 | €3.681,39 | €150,03 | €80,14 |
| TEST | Bilanciata V3 · LONG only | 2 | €10.009,32 | €2.070,97 | €6.212,91 | €99,99 | €13,04 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 1 | €10.008,26 | €146,81 | €440,42 | €50,00 | €8,52 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 1 | €9.998,52 | €822,35 | €2.467,06 | €50,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.993,64 | €4.432,13 | €8.864,26 | €199,90 | €-1,05 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.993,64 | €4.432,13 | €8.864,26 | €199,90 | €-1,05 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.991,34 | €830,21 | €1.660,43 | €49,74 | €44,26 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.987,90 | €761,04 | €1.522,08 | €49,74 | €40,57 |
| TEST | Forza relativa 1H V1 | 5 | €9.983,66 | €1.605,80 | €3.211,59 | €100,56 | €65,37 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.972,63 | €862,58 | €1.725,17 | €49,74 | €25,70 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.966,15 | €2.030,07 | €4.060,14 | €149,47 | €22,71 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.962,24 | €1.153,43 | €3.460,30 | €49,83 | €-1,93 |
| TEST | Eth Donchian 1H | 1 | €9.959,02 | €1.299,81 | €3.899,43 | €49,91 | €-21,51 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.954,43 | €1.540,87 | €3.081,73 | €198,77 | €87,91 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.943,71 | €6.552,10 | €13.104,20 | €198,36 | €5,07 |
| TEST | Scanner Bottom15 Short | 4 | €9.943,71 | €6.552,10 | €13.104,20 | €198,36 | €5,07 |
| TEST | Scanner Bottom20 Short | 4 | €9.943,71 | €6.552,10 | €13.104,20 | €198,36 | €5,07 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.940,84 | €2.237,74 | €4.475,49 | €198,53 | €8,37 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.931,24 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Combo Adaptive — Long Only | 4 | €9.919,61 | €1.602,29 | €3.204,58 | €197,30 | €54,50 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.919,20 | €407,36 | €1.222,09 | €98,99 | €19,82 |
| TEST | Eth Adaptive 1H | 1 | €9.917,03 | €1.146,74 | €3.440,21 | €49,54 | €11,08 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.910,33 | €1.506,26 | €3.012,51 | €197,30 | €87,25 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.910,33 | €1.506,26 | €3.012,51 | €197,30 | €87,25 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.907,88 | €1.505,47 | €3.010,95 | €197,25 | €87,23 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.895,99 | €405,09 | €1.215,26 | €98,45 | €19,72 |
| TEST | Sol Adaptive 1H | 1 | €9.894,14 | €1.144,60 | €3.433,80 | €49,45 | €6,87 |
| TEST | Rapida V3 — Long Only | 3 | €9.890,72 | €654,23 | €1.962,70 | €97,94 | €62,78 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.857,45 | €1.323,25 | €2.646,50 | €98,42 | €82,02 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.844,43 | €1.138,34 | €3.415,02 | €49,18 | €11,00 |
| TEST | Sol Bollinger 1H | 1 | €9.839,81 | €1.365,75 | €4.097,24 | €49,17 | €8,84 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.813,51 | €4.615,62 | €9.231,25 | €147,38 | €-1,61 |
| TEST | Combo Adaptive — parziale 1R | 4 | €9.811,97 | €2.207,08 | €4.414,15 | €195,95 | €8,27 |
| TEST | Global Confluence puro 1H | 1 | €9.795,97 | €1.538,38 | €3.076,76 | €49,23 | €-47,67 |
| TEST | Top 5 + BTC — solo MFE | 4 | €9.790,25 | €2.782,08 | €5.564,16 | €146,29 | €80,31 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.758,09 | €2.619,37 | €5.238,74 | €193,97 | €100,31 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.745,53 | €1.203,68 | €2.407,37 | €97,58 | €81,09 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.737,06 | €1.252,56 | €2.505,12 | €145,96 | €13,50 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.679,96 | €2.032,81 | €4.065,61 | €144,99 | €0,00 |

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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.923,10 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.827,06 | €733,40 | 31 | 31 | 54,84% | 2,38 | €23,66 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.585,52 | €494,53 | 23 | 23 | 52,17% | 2,25 | €21,50 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.567,78 | €440,97 | 39 | 39 | 53,85% | 1,61 | €11,31 | 2,30% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.546,83 | €480,19 | 36 | 36 | 47,22% | 1,59 | €13,34 | 2,20% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.424,56 | €435,46 | 36 | 36 | 47,22% | 1,75 | €12,10 | 2,49% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.420,54 | €241,08 | 35 | 34 | 37,14% | 1,25 | €6,89 | 3,69% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.349,09 | €270,73 | 20 | 20 | 50,00% | 1,64 | €13,54 | 2,12% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.332,34 | €348,09 | 32 | 32 | 46,88% | 1,61 | €10,88 | 2,49% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.322,99 | €287,78 | 4 | 4 | 100,00% | ∞ | €71,95 | 0,53% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.303,20 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.297,20 | €262,42 | 67 | 67 | 37,31% | 1,20 | €3,92 | 2,89% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.287,32 | €198,60 | 9 | 9 | 66,67% | 2,22 | €22,07 | 2,33% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.286,11 | €218,63 | 3 | 3 | 100,00% | ∞ | €72,88 | 0,96% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.278,94 | €294,61 | 37 | 37 | 45,95% | 1,39 | €7,96 | 2,83% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.273,09 | €188,30 | 30 | 28 | 53,33% | 1,34 | €6,28 | 2,75% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.262,82 | €228,02 | 5 | 5 | 80,00% | 4,82 | €45,60 | 1,04% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.262,82 | €228,02 | 5 | 5 | 80,00% | 4,82 | €45,60 | 1,04% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.253,66 | €99,46 | 1 | 1 | 100,00% | ∞ | €99,46 | 0,31% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.244,92 | €218,63 | 3 | 3 | 100,00% | ∞ | €72,88 | 0,96% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.239,99 | €205,40 | 35 | 35 | 40,00% | 1,30 | €5,87 | 2,10% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.229,03 | €162,12 | 8 | 8 | 62,50% | 3,00 | €20,26 | 0,98% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.214,13 | €208,06 | 23 | 23 | 47,83% | 1,53 | €9,05 | 1,44% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.194,91 | €107,65 | 5 | 5 | 60,00% | 1,91 | €21,53 | 1,64% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.186,66 | €109,33 | 1 | 1 | 100,00% | ∞ | €109,33 | 0,24% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.166,42 | €79,14 | 5 | 5 | 60,00% | 1,73 | €15,83 | 2,20% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.166,10 | €99,34 | 1 | 1 | 100,00% | ∞ | €99,34 | 0,27% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.139,24 | €99,34 | 1 | 1 | 100,00% | ∞ | €99,34 | 0,31% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €10.130,61 | €26,45 | 2 | 2 | 50,00% | 1,36 | €13,23 | 0,43% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €10.118,31 | €-86,93 | 1 | 1 | 0,00% | 0,00 | €-86,93 | 0,61% |
| TEST | Combo Scanner | Combo Scanner | €10.102,87 | €65,69 | 25 | 25 | 44,00% | 1,10 | €2,63 | 2,66% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.099,79 | €85,19 | 3 | 3 | 66,67% | 2,56 | €28,40 | 0,67% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.098,40 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.087,47 | €92,66 | 12 | 11 | 50,00% | 1,36 | €7,72 | 1,69% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.084,50 | €53,64 | 41 | 41 | 36,59% | 1,06 | €1,31 | 2,49% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €10.083,01 | €-4,53 | 2 | 2 | 50,00% | 0,94 | €-2,27 | 0,43% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.074,89 | €70,07 | 28 | 28 | 42,86% | 1,11 | €2,50 | 2,06% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.071,65 | €-12,13 | 4 | 4 | 50,00% | 0,92 | €-3,03 | 0,94% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €10.070,39 | €-39,64 | 3 | 3 | 33,33% | 0,71 | €-13,21 | 0,88% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.065,73 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.065,73 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.065,73 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,16% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.065,65 | €31,03 | 75 | 75 | 34,67% | 1,02 | €0,41 | 6,76% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.061,03 | €-32,91 | 36 | 36 | 30,56% | 0,96 | €-0,91 | 2,58% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.057,24 | €26,47 | 42 | 42 | 38,10% | 1,03 | €0,63 | 2,96% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.056,58 | €56,58 | 13 | 13 | 30,77% | 1,24 | €4,35 | 1,92% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.043,46 | €-29,28 | 10 | 10 | 50,00% | 0,83 | €-2,93 | 1,51% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.039,57 | €-33,32 | 16 | 16 | 43,75% | 0,93 | €-2,08 | 2,12% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €10.028,13 | €-57,95 | 8 | 8 | 37,50% | 0,79 | €-7,24 | 3,31% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.020,94 | €-6,74 | 14 | 14 | 35,71% | 0,98 | €-0,48 | 2,31% |
| TEST | Sol Ema 1H | Trend following EMA | €10.018,45 | €32,05 | 4 | 4 | 50,00% | 1,29 | €8,01 | 1,67% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Combo Trend | Combo Trend | €10.013,18 | €-0,85 | 29 | 29 | 31,03% | 1,00 | €-0,03 | 3,58% |
| TEST | Ampia 4H | Confluenza trend | €10.011,64 | €-70,51 | 15 | 15 | 20,00% | 0,86 | €-4,70 | 2,97% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €10.009,32 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,17% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.008,26 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,07% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.998,52 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,34% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.993,64 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,21% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.993,64 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,21% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.991,34 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.987,90 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.983,66 | €-79,13 | 24 | 24 | 25,00% | 0,82 | €-3,30 | 3,25% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Sol Ema 4H | Trend following EMA | €9.972,63 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.966,15 | €-53,77 | 20 | 20 | 35,00% | 0,89 | €-2,69 | 2,25% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Btc Ema 1H | Trend following EMA | €9.962,24 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.959,02 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.954,43 | €-131,10 | 8 | 8 | 25,00% | 0,59 | €-16,39 | 2,80% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.943,71 | €-53,50 | 1 | 1 | 0,00% | 0,00 | €-53,50 | 0,93% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.943,71 | €-53,50 | 1 | 1 | 0,00% | 0,00 | €-53,50 | 0,93% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.943,71 | €-53,50 | 1 | 1 | 0,00% | 0,00 | €-53,50 | 0,93% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.940,84 | €-64,63 | 11 | 11 | 45,45% | 0,76 | €-5,88 | 1,41% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.931,24 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.919,61 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.919,20 | €-99,88 | 24 | 24 | 37,50% | 0,85 | €-4,16 | 2,86% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.917,03 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.910,33 | €-174,58 | 6 | 6 | 16,67% | 0,36 | €-29,10 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.910,33 | €-174,58 | 6 | 6 | 16,67% | 0,36 | €-29,10 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.907,88 | €-177,01 | 6 | 6 | 16,67% | 0,35 | €-29,50 | 3,19% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.895,99 | €-122,99 | 25 | 25 | 48,00% | 0,83 | €-4,92 | 3,21% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.894,14 | €-110,64 | 5 | 5 | 40,00% | 0,38 | €-22,13 | 2,14% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.890,72 | €-170,88 | 27 | 27 | 29,63% | 0,77 | €-6,33 | 3,65% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.857,45 | €-222,86 | 18 | 18 | 33,33% | 0,53 | €-12,38 | 2,88% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Eth Ema 1H | Trend following EMA | €9.844,43 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.839,81 | €-166,62 | 3 | 3 | 0,00% | 0,00 | €-55,54 | 1,89% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.813,51 | €-177,20 | 26 | 26 | 34,62% | 0,72 | €-6,82 | 5,48% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.811,97 | €-193,27 | 13 | 13 | 38,46% | 0,56 | €-14,87 | 2,24% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.795,97 | €-154,38 | 9 | 9 | 33,33% | 0,44 | €-17,15 | 2,92% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.790,25 | €-286,96 | 14 | 14 | 35,71% | 0,25 | €-20,50 | 3,95% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.758,09 | €-338,51 | 16 | 16 | 25,00% | 0,53 | €-21,16 | 4,69% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.745,53 | €-334,13 | 21 | 21 | 28,57% | 0,43 | €-15,91 | 4,05% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.737,06 | €-274,94 | 38 | 38 | 57,89% | 0,61 | €-7,24 | 4,16% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.679,96 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,07038 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €-22,30 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 73,93900 | 75,57185 | 98,06983 | 70,34400 | €20,35 | €61,04 | €1,44 | €-0,09 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,30592 | 0,34746 | 0,32009 | 0,20548 | 0,36789 | €172,71 | €518,13 | €0,00 | €70,35 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 487,33251 | 475,42000 | 481,21745 | 647,34002 | 467,39189 | €854,91 | €2.564,72 | €0,00 | €62,69 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00329 | 0,00335 | 0,00290 | 0,00221 | 0,00408 | €12,36 | €37,07 | €4,45 | €0,68 |
| Bilanciata 1H — LONG senza Range High Vol | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,29401 | 0,34746 | 0,31684 | 0,19748 | 0,36064 | €147,07 | €441,21 | €0,00 | €80,21 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00320 | 0,00335 | 0,00282 | 0,00215 | 0,00397 | €138,85 | €416,55 | €49,99 | €20,24 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 368,43000 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €12,73 |
| Bilanciata 1H — SHORT Trend Down stretto | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,35678 | 0,34987 | 0,39728 | 0,47392 | 0,27577 | €146,81 | €440,42 | €50,00 | €8,52 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,29967 | 0,34746 | 0,31535 | 0,20128 | 0,37088 | €141,19 | €423,58 | €0,00 | €67,55 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00320 | 0,00335 | 0,00282 | 0,00215 | 0,00397 | €142,81 | €428,43 | €51,41 | €20,62 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,29527 | 0,34746 | 0,31684 | 0,19832 | 0,36219 | €152,72 | €458,16 | €0,00 | €80,98 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,73625 | 73,93900 | 74,79805 | 97,94632 | 71,61265 | €1.217,91 | €3.653,72 | €52,61 | €-10,05 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Rapida 1H V1 — madre | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.084,03 | €3.252,10 | €50,01 | €16,16 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €158,12 | €474,35 | €49,93 | €23,04 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,09458 | 1,09315 | 1,10684 | 1,45397 | 1,07619 | €1.525,19 | €4.575,56 | €51,25 | €5,98 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64156,30000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.520,13 | €4.560,38 | €51,08 | €-29,05 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.127,01 | €3.381,02 | €51,99 | €16,80 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.108,52 | €3.325,56 | €51,14 | €16,53 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00335 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €20,69 |
| Rapida score 6–7,5 — Range Only | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.108,52 | €3.325,56 | €51,14 | €16,53 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00335 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €20,69 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.108,52 | €3.325,56 | €51,14 | €16,53 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00335 | 0,00289 | 0,00216 | 0,00372 | €167,51 | €502,54 | €51,57 | €20,65 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64156,30000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.499,07 | €4.497,20 | €50,37 | €-28,65 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.118,06 | €3.354,19 | €51,58 | €16,67 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.102,88 | €3.308,63 | €50,88 | €16,44 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €160,87 | €482,60 | €50,80 | €23,44 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,33818 | 0,34746 | 0,31735 | 0,22714 | 0,36943 | €10,94 | €32,82 | €2,02 | €0,90 |
| Rapida V1 — target pieno 2R | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 486,53267 | 475,42000 | 479,70450 | 646,27757 | 472,09408 | €1.108,33 | €3.325,00 | €0,00 | €75,94 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00387 | €157,69 | €473,06 | €49,80 | €22,98 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.109,04 | €3.327,12 | €51,17 | €16,53 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €161,77 | €485,30 | €51,08 | €23,58 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33818 | 0,34746 | 0,31735 | 0,22714 | 0,36943 | €11,00 | €33,01 | €2,03 | €0,91 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63750,18741 | 64156,30000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.506,88 | €4.520,63 | €50,63 | €-28,80 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.123,87 | €3.371,61 | €51,85 | €16,76 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — no volatilità HIGH | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 477,32452 | 475,42000 | 484,66491 | 634,04607 | 466,31393 | €1.084,87 | €3.254,60 | €50,05 | €12,99 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €158,01 | €474,02 | €49,90 | €23,03 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33818 | 0,34746 | 0,31735 | 0,22714 | 0,36943 | €10,26 | €30,78 | €1,90 | €0,84 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €155,06 | €465,19 | €48,97 | €22,60 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33014 | 0,34746 | 0,33014 | 0,22174 | 0,36194 | €255,21 | €765,63 | €0,00 | €40,18 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00335 | 0,00289 | 0,00216 | 0,00372 | €160,75 | €482,24 | €49,49 | €19,82 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 477,32452 | 475,42000 | 484,66491 | 634,04607 | 466,31393 | €1.087,81 | €3.263,42 | €50,19 | €13,02 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €158,44 | €475,31 | €50,03 | €23,09 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33818 | 0,34746 | 0,31735 | 0,22714 | 0,36943 | €10,29 | €30,86 | €1,90 | €0,85 |
| Rapida V3 senza ESPORTS — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,31922 | 0,34746 | 0,32620 | 0,21441 | 0,35341 | €233,19 | €699,57 | €0,00 | €61,88 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €158,13 | €474,39 | €49,94 | €23,05 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 477,32452 | 475,42000 | 484,66491 | 634,04607 | 466,31393 | €1.102,50 | €3.307,50 | €50,86 | €13,20 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00287 | 0,00215 | 0,00369 | €163,79 | €491,38 | €50,85 | €24,06 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33259 | 0,34746 | 0,33259 | 0,22339 | 0,36462 | €259,50 | €778,50 | €0,00 | €34,82 |
| Rapida V3 senza ESPORTS — Stress Guard | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 477,79442 | 475,42000 | 485,14204 | 634,67026 | 466,77299 | €1.088,47 | €3.265,42 | €50,22 | €16,23 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00335 | 0,00289 | 0,00216 | 0,00372 | €159,93 | €479,80 | €49,24 | €19,72 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07038 | 0,07077 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €35,66 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 57,46100 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €13,17 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | BANK | LONG | Confluenza trend | 240m | 2,0x | 0,32319 | 0,34746 | 0,28441 | 0,16321 | 0,43179 | €208,50 | €417,00 | €50,04 | €31,31 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,29967 | 0,34746 | 0,31306 | 0,15133 | 0,37800 | €204,97 | €409,93 | €0,00 | €65,37 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,29683 | 0,34746 | 0,31306 | 0,14990 | 0,37442 | €213,94 | €427,88 | €0,00 | €72,98 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 493,58126 | 475,42000 | 481,93327 | 737,90399 | 470,87721 | €1.207,34 | €2.414,67 | €0,00 | €88,85 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00320 | 0,00335 | 0,00282 | 0,00162 | 0,00405 | €216,28 | €432,55 | €51,91 | €20,35 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,30592 | 0,34746 | 0,31618 | 0,15449 | 0,39198 | €227,65 | €455,29 | €0,00 | €61,82 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 477,79442 | 475,42000 | 488,29102 | 714,30266 | 451,55293 | €1.171,54 | €2.343,07 | €51,47 | €11,64 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,34987 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €8,33 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64156,30000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €1,97 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,77975 | 73,93900 | 72,89440 | 37,25878 | 75,10779 | €2.011,27 | €4.022,55 | €48,27 | €8,68 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,83123 | 73,93900 | 75,01253 | 110,37769 | 71,23237 | €1.561,26 | €3.122,52 | €49,96 | €-4,56 |
| Benchmark trend following EMA 1H | BANK | LONG | Trend following EMA | 60m | 2,0x | 0,33026 | 0,34746 | 0,29883 | 0,16678 | 0,39939 | €261,76 | €523,52 | €49,81 | €27,27 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,30592 | 0,34746 | 0,32009 | 0,15449 | 0,36789 | €264,92 | €529,85 | €0,00 | €71,94 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €224,41 | €448,82 | €53,86 | €23,16 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,66 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 475,37491 | 475,42000 | 484,51563 | 710,68548 | 457,09345 | €1.295,12 | €2.590,24 | €49,81 | €-0,25 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,73625 | 73,93900 | 74,79805 | 110,23569 | 71,61265 | €1.729,03 | €3.458,05 | €49,80 | €-9,51 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,27577 | €210,41 | €420,83 | €47,78 | €8,15 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €21,50 |
| Scanner Top10 Long | BANK | LONG | Scanner Top10 Long | 60m | 2,0x | 0,32906 | 0,34746 | 0,30181 | 0,16617 | 0,38355 | €301,89 | €603,79 | €50,00 | €33,77 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €12,71 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 478,57427 | 475,42000 | 487,11688 | 715,46853 | 461,48903 | €1.400,23 | €2.800,46 | €49,99 | €18,46 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.735,32 | €3.470,65 | €49,98 | €-13,72 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 73,94621 | 73,93900 | 75,01103 | 110,54958 | 71,81656 | €1.685,29 | €3.370,58 | €48,54 | €0,33 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €21,50 |
| Scanner Top15 Long | BANK | LONG | Scanner Top15 Long | 60m | 2,0x | 0,32906 | 0,34746 | 0,30181 | 0,16617 | 0,38355 | €301,89 | €603,79 | €50,00 | €33,77 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €12,71 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 478,57427 | 475,42000 | 487,11688 | 715,46853 | 461,48903 | €1.400,23 | €2.800,46 | €49,99 | €18,46 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.735,32 | €3.470,65 | €49,98 | €-13,72 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 73,94621 | 73,93900 | 75,01103 | 110,54958 | 71,81656 | €1.685,29 | €3.370,58 | €48,54 | €0,33 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €21,50 |
| Scanner Top20 Long | BANK | LONG | Scanner Top20 Long | 60m | 2,0x | 0,32906 | 0,34746 | 0,30181 | 0,16617 | 0,38355 | €301,89 | €603,79 | €50,00 | €33,77 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €12,71 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 478,57427 | 475,42000 | 487,11688 | 715,46853 | 461,48903 | €1.400,23 | €2.800,46 | €49,99 | €18,46 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.735,32 | €3.470,65 | €49,98 | €-13,72 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 73,94621 | 73,93900 | 75,01103 | 110,54958 | 71,81656 | €1.685,29 | €3.370,58 | €48,54 | €0,33 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,34746 | 0,32009 | 0,15449 | 0,37408 | €259,02 | €518,04 | €0,00 | €70,34 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00403 | €219,41 | €438,82 | €52,66 | €22,64 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,34 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30858 | 0,34746 | 0,33343 | 0,15583 | 0,37734 | €239,71 | €479,42 | €0,00 | €60,40 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00403 | €192,87 | €385,75 | €46,29 | €19,91 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,34746 | 0,32009 | 0,15449 | 0,37408 | €245,39 | €490,78 | €0,00 | €66,64 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00403 | €207,86 | €415,72 | €49,89 | €21,45 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,34746 | 0,32009 | 0,15449 | 0,37408 | €248,77 | €497,53 | €0,00 | €67,56 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00403 | €210,72 | €421,44 | €50,57 | €21,75 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,35 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30707 | 0,34746 | 0,33283 | 0,15507 | 0,37334 | €245,18 | €490,36 | €0,00 | €64,50 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00335 | 0,00284 | 0,00163 | 0,00407 | €201,88 | €403,77 | €48,45 | €16,59 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,34746 | 0,32009 | 0,15449 | 0,37408 | €249,47 | €498,94 | €0,00 | €67,75 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00403 | €211,32 | €422,63 | €50,72 | €21,81 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30707 | 0,34746 | 0,33283 | 0,15507 | 0,37334 | €248,00 | €495,99 | €0,00 | €65,24 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00335 | 0,00284 | 0,00163 | 0,00407 | €204,20 | €408,41 | €49,01 | €16,78 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,34746 | 0,32009 | 0,15449 | 0,39887 | €251,72 | €503,43 | €0,00 | €68,36 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00434 | €213,22 | €426,44 | €51,17 | €22,01 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,66 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,34746 | 0,31497 | 0,13147 | 0,35405 | €211,25 | €422,51 | €0,00 | €141,41 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00434 | €213,56 | €427,11 | €51,25 | €22,04 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,79 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06931 | 0,07038 | 0,07042 | 0,10361 | 0,06653 | €1.538,38 | €3.076,76 | €49,23 | €-47,67 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06924 | 0,07038 | 0,07034 | 0,10351 | 0,06680 | €1.558,17 | €3.116,34 | €49,86 | €-51,49 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,30592 | 0,34746 | 0,31814 | 0,15449 | 0,38166 | €221,89 | €443,78 | €0,00 | €60,26 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00329 | 0,00335 | 0,00290 | 0,00166 | 0,00416 | €208,78 | €417,57 | €50,11 | €7,66 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64156,30000 | 63010,38428 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €47,97 | €23,86 |
| Combo Mean Reversion | HYPE | LONG | Combo Mean Reversion | 60m | 2,0x | 56,86137 | 57,46100 | 56,98790 | 28,71499 | 58,42218 | €1.459,02 | €2.918,04 | €0,00 | €30,77 |
| Combo Mean Reversion | AKE | SHORT | Combo Mean Reversion | 60m | 2,0x | 0,00320 | 0,00335 | 0,00356 | 0,00479 | 0,00263 | €225,46 | €450,91 | €50,00 | €-21,40 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00403 | €210,36 | €420,73 | €50,49 | €21,71 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,22 |
| Combo Scanner | BANK | LONG | Combo Scanner | 60m | 2,0x | 0,33818 | 0,34746 | 0,31139 | 0,17078 | 0,39710 | €318,33 | €636,67 | €50,43 | €17,48 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,27577 | €222,29 | €444,58 | €50,47 | €8,61 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30707 | 0,34746 | 0,32285 | 0,15507 | 0,36731 | €254,82 | €509,63 | €0,00 | €67,03 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,27577 | €220,50 | €441,00 | €50,07 | €8,54 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,32906 | 0,34746 | 0,30181 | 0,16617 | 0,38355 | €297,85 | €595,70 | €49,33 | €33,32 |
| Combo Adaptive — Long Only | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €205,22 | €410,44 | €49,25 | €21,18 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,27577 | €213,53 | €427,07 | €48,48 | €8,27 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30592 | 0,34746 | 0,32205 | 0,15449 | 0,39887 | €246,85 | €493,70 | €0,00 | €67,04 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 478,57427 | 475,42000 | 487,11688 | 715,46853 | 452,94641 | €23,06 | €46,12 | €0,82 | €0,30 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,23526 | €217,23 | €434,45 | €49,32 | €8,41 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,23526 | €216,34 | €432,67 | €49,12 | €8,37 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64156,30000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €-1,93 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64156,30000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €2,05 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,69426 | 73,93900 | 74,75546 | 97,89054 | 71,57186 | €1.161,12 | €3.483,35 | €50,16 | €-11,57 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 73,93900 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €25,70 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 73,93900 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €44,26 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 73,77975 | 73,93900 | 72,89440 | 49,55540 | 75,10779 | €1.365,75 | €4.097,24 | €49,17 | €8,84 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 74,08718 | 73,93900 | 75,15403 | 98,41247 | 71,95347 | €1.144,60 | €3.433,80 | €49,45 | €6,87 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 73,93900 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €40,57 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1867,19000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €11,00 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 1856,94854 | 1867,19000 | 1880,71748 | 2466,64664 | 1809,41065 | €1.299,81 | €3.899,43 | €49,91 | €-21,51 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1867,19000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €11,08 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,34746 | 0,27494 | 0,15449 | 0,36789 | €242,50 | €485,00 | €49,12 | €65,86 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €21,20 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,20 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,34746 | 0,27494 | 0,15449 | 0,36789 | €242,50 | €485,00 | €49,12 | €65,86 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €21,20 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,20 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29671 | 0,34746 | 0,26110 | 0,14984 | 0,36792 | €199,82 | €399,64 | €47,96 | €68,36 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00335 | 0,00282 | 0,00162 | 0,00397 | €201,87 | €403,75 | €48,45 | €19,61 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €12,34 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,34746 | 0,27494 | 0,15449 | 0,36789 | €243,58 | €487,15 | €49,34 | €66,15 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00396 | €206,32 | €412,65 | €49,52 | €21,29 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,31 |
| Master Adaptive Expanded V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07011 | 0,07038 | 0,06910 | 0,03541 | 0,07213 | €20,63 | €41,26 | €0,59 | €0,16 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00325 | 0,00335 | 0,00286 | 0,00164 | 0,00403 | €202,04 | €404,08 | €48,49 | €13,50 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,34746 | 0,27494 | 0,15449 | 0,39887 | €242,44 | €484,88 | €49,11 | €65,84 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00335 | 0,00281 | 0,00161 | 0,00434 | €205,36 | €410,73 | €49,29 | €21,19 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,19 |
| Combo Adaptive — Side × Regime Guard | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30139 | 0,34746 | 0,32164 | 0,15220 | 0,36342 | €242,95 | €485,90 | €0,00 | €74,27 |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 487,66245 | 475,42000 | 480,44436 | 729,05536 | 468,37744 | €1.264,26 | €2.528,53 | €0,00 | €63,48 |
| Combo Adaptive — Side × Regime Guard | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00320 | 0,00335 | 0,00282 | 0,00162 | 0,00397 | €212,78 | €425,56 | €51,07 | €20,02 |
| Combo Adaptive — Side × Regime Guard | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 73,95421 | 73,93900 | 75,01915 | 110,56154 | 71,82433 | €1.768,24 | €3.536,48 | €50,93 | €0,73 |
| Master Adaptive GB20 — Breakeven 0,5R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30139 | 0,34746 | 0,30139 | 0,15220 | 0,36342 | €242,95 | €485,90 | €0,00 | €74,27 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00335 | 0,00320 | 0,00162 | 0,00397 | €209,82 | €419,64 | €0,00 | €19,74 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 366,72991 | 185,19860 | 380,10713 | €1.380,83 | €2.761,66 | €0,00 | €12,80 |
| Master Adaptive GB20 — 50% a 0,75R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30139 | 0,34746 | 0,30139 | 0,15220 | 0,36342 | €121,48 | €242,95 | €0,00 | €37,14 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00335 | 0,00282 | 0,00162 | 0,00397 | €209,13 | €418,26 | €50,19 | €19,68 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €12,76 |
| Master Adaptive GB20 — Loss Cap 0,75R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30139 | 0,34746 | 0,27813 | 0,15220 | 0,36342 | €323,93 | €647,87 | €50,00 | €99,03 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00335 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €92,52 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 368,43000 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €17,02 |
| Rapida V3 NoHigh — Range Only | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,47950 | 57,46100 | 58,38711 | 76,35194 | 56,11809 | €1.055,48 | €3.166,43 | €50,00 | €1,02 |
| Rapida V3 NoHigh — Range Only | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 476,20474 | 475,42000 | 483,52791 | 632,55863 | 465,21998 | €1.105,63 | €3.316,90 | €51,01 | €5,47 |
| Rapida V3 NoHigh — Range Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €23,50 |
| Rapida V3 NoHigh — Regime Guard | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,47950 | 57,46100 | 58,38711 | 76,35194 | 56,11809 | €1.055,48 | €3.166,43 | €50,00 | €1,02 |
| Rapida V3 NoHigh — Regime Guard | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 476,20474 | 475,42000 | 483,52791 | 632,55863 | 465,21998 | €1.105,63 | €3.316,90 | €51,01 | €5,47 |
| Rapida V3 NoHigh — Regime Guard | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00335 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €23,50 |
| Rapida V3 NoHigh — Regime Guard | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33014 | 0,34746 | 0,33014 | 0,22174 | 0,36194 | €264,66 | €793,99 | €0,00 | €41,66 |
| MAIN — Side × Regime Guard | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,30730 | 0,34746 | 0,27043 | 0,20640 | 0,38105 | €138,88 | €416,65 | €50,00 | €54,45 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00335 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €17,33 |
| MAIN — Side × Regime Guard | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06945 | 0,07038 | 0,07129 | 0,09225 | 0,06577 | €637,30 | €1.911,89 | €50,64 | €-25,71 |
| MAIN — Side × Regime Guard | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 73,93900 | 75,57185 | 98,06983 | 70,34400 | €715,11 | €2.145,34 | €50,64 | €-3,19 |
| MAIN — Dynamic Asset Selector | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,30730 | 0,34746 | 0,27043 | 0,20640 | 0,38105 | €138,88 | €416,65 | €50,00 | €54,45 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00335 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €17,33 |
| MAIN — Dynamic Asset Selector | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 73,93900 | 75,57185 | 98,06983 | 70,34400 | €715,22 | €2.145,66 | €50,64 | €-3,19 |
| Combo Trend — Side × Regime Guard | BANK | LONG | Combo Trend | 60m | 2,0x | 0,30089 | 0,34746 | 0,31884 | 0,15195 | 0,37359 | €227,64 | €455,28 | €0,00 | €70,47 |
| Combo Trend — Side × Regime Guard | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00320 | 0,00335 | 0,00282 | 0,00162 | 0,00405 | €211,52 | €423,03 | €50,76 | €19,90 |
| Combo Trend — Side × Regime Guard | ZEC | SHORT | Combo Trend | 60m | 2,0x | 474,93499 | 475,42000 | 483,49367 | 710,02782 | 456,10591 | €1.412,87 | €2.825,73 | €50,92 | €-2,89 |
| Combo Trend — Side × Regime Guard | SOL | SHORT | Combo Trend | 60m | 2,0x | 73,80224 | 73,93900 | 74,98307 | 110,33434 | 71,20440 | €1.590,95 | €3.181,90 | €50,91 | €-5,90 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| Bilanciata V3 · LONG only | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,94621 | 73,93900 | 75,01103 | 98,22521 | 71,81656 | €1.157,41 | €3.472,22 | €50,00 | €0,34 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 368,43000 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €12,71 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,27577 | €220,21 | €440,42 | €50,00 | €8,52 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 474,93499 | 475,42000 | 482,63780 | 710,02782 | 459,52938 | €1.541,01 | €3.082,01 | €49,99 | €-3,15 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,80224 | 73,93900 | 74,86499 | 110,33434 | 71,67673 | €1.733,04 | €3.466,09 | €49,91 | €-6,42 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35678 | 0,34987 | 0,39728 | 0,53338 | 0,27577 | €220,21 | €440,42 | €50,00 | €8,52 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 474,93499 | 475,42000 | 482,63780 | 710,02782 | 459,52938 | €1.541,01 | €3.082,01 | €49,99 | €-3,15 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,80224 | 73,93900 | 74,86499 | 110,33434 | 71,67673 | €1.733,04 | €3.466,09 | €49,91 | €-6,42 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Gb20 V1 | BANK | LONG | 2026-07-25T14:53:38+00:00 | 0,33658 | €6,32 | 0,13 | STOP_GAP_STRESS |
| Benchmark trend following EMA 1H | DOGE | SHORT | 2026-07-25T14:53:38+00:00 | 0,07023 | €-55,07 | -1,10 | STOP |
| Rapida V1 — target pieno 2R | BANK | LONG | 2026-07-25T14:53:38+00:00 | 0,34866 | €95,01 | 1,98 | TARGET |
| Doge Ema 1H | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-56,38 | -1,11 | STOP |
| Combo Scanner | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-56,22 | -1,11 | STOP |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-55,50 | -1,11 | STOP |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-55,50 | -1,11 | STOP |
| Combo Adaptive — Quality7 | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-55,56 | -1,11 | STOP |
| Combo Adaptive — parziale 1R | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-54,78 | -1,11 | STOP |
| Combo Adaptive — madre | DOGE | SHORT | 2026-07-25T14:31:05+00:00 | 0,07012 | €-57,02 | -1,11 | STOP |
| Rapida 1H V2 | BANK | LONG | 2026-07-25T14:31:05+00:00 | 0,34200 | €73,74 | 1,48 | TARGET |
| Rapida V3 — score <7,5 | PEPE | SHORT | 2026-07-25T13:38:37+00:00 | 0,00000 | €-60,35 | -1,16 | STOP |

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
| MAIN | Principale 4H | 54/30 | 18/30 | 1,05 | 0,91 | 0,03R | €-2,94 | 4,26% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €99,34 | 0,27% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €99,34 | 0,31% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 10/30 | 5/30 | 0,31 | 0,20 | -0,54R | €-4,60 | 0,37% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 161/30 | 39/30 | 1,02 | 1,61 | 0,02R | €11,31 | 2,30% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 3/30 | 0,00 | 0,71 | 0,00R | €-13,21 | 0,88% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,07% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 38/30 | 28/30 | 1,75 | 1,34 | 0,39R | €6,28 | 2,75% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 66/30 | 36/30 | 1,31 | 1,59 | 0,19R | €13,34 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 198/30 | 75/30 | 0,95 | 1,02 | -0,03R | €0,41 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 15/30 | 13/30 | 1,86 | 1,24 | 0,36R | €4,35 | 1,92% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,34% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 60/30 | 37/30 | 1,20 | 1,39 | 0,11R | €7,96 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 63/30 | 35/30 | 0,96 | 1,30 | -0,02R | €5,87 | 2,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 4/30 | 0,00 | ∞ | 0,00R | €71,95 | 0,53% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 5/30 | 0,00 | 4,82 | 0,00R | €45,60 | 1,04% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 5/30 | 0,00 | 4,82 | 0,00R | €45,60 | 1,04% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 44/30 | 36/30 | 1,45 | 1,75 | 0,23R | €12,10 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 55/30 | 36/30 | 0,90 | 0,96 | -0,07R | €-0,91 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 10/30 | 11/30 | 0,46 | 1,36 | -0,43R | €7,72 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 104/30 | 67/30 | 1,05 | 1,20 | 0,03R | €3,92 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 52/30 | 32/30 | 1,14 | 1,61 | 0,08R | €10,88 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 26/30 | 25/30 | 1,01 | 0,83 | 0,01R | €-4,92 | 3,21% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 26/30 | 24/30 | 1,01 | 0,85 | 0,01R | €-4,16 | 2,86% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 31/30 | 27/30 | 0,66 | 0,77 | -0,25R | €-6,33 | 3,65% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 3/30 | 0,00 | ∞ | 0,00R | €72,88 | 0,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 3/30 | 0,00 | ∞ | 0,00R | €72,88 | 0,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 59/30 | 42/30 | 0,98 | 1,03 | -0,01R | €0,63 | 2,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 4/30 | 0,00 | 0,92 | 0,00R | €-3,03 | 0,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 8/30 | 0,00 | 3,00 | 0,00R | €20,26 | 0,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 3/30 | 0,00 | 2,56 | 0,00R | €28,40 | 0,67% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 60/30 | 41/30 | 0,95 | 1,06 | -0,03R | €1,31 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 48/30 | 15/30 | 1,12 | 0,86 | 0,09R | €-4,70 | 2,97% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 38/30 | 28/30 | 0,96 | 1,11 | -0,03R | €2,50 | 2,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 3/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 4/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 5/30 | 0,57 | 0,79 | -0,36R | €-6,87 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 107/30 | 23/30 | 1,16 | 1,53 | 0,10R | €9,05 | 1,44% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 29/30 | 5/30 | 0,71 | 0,42 | -0,22R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 74/30 | 27/30 | 1,06 | 0,45 | 0,04R | €-11,76 | 4,11% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 50/30 | 13/30 | 0,86 | 0,56 | -0,10R | €-14,87 | 2,24% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 5/30 | 5/30 | 0,46 | 0,48 | -0,46R | €-16,52 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 5/30 | 5/30 | 0,46 | 0,17 | -0,46R | €-28,67 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 11/30 | 10/30 | 1,09 | 0,83 | 0,06R | €-2,93 | 1,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 26/30 | 10/30 | 0,33 | 0,92 | -0,61R | €-2,35 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 35/30 | 16/30 | 0,69 | 0,93 | -0,26R | €-2,08 | 2,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €99,46 | 0,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 35/30 | 11/30 | 0,69 | 0,76 | -0,26R | €-5,88 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 16/30 | 14/30 | 0,84 | 0,98 | -0,11R | €-0,48 | 2,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 64/30 | 25/30 | 1,46 | 1,10 | 0,28R | €2,63 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 82/30 | 29/30 | 1,08 | 1,00 | 0,06R | €-0,03 | 3,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €109,33 | 0,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 4/30 | 1,67 | 0,98 | 0,38R | €-0,31 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 8/30 | 3,40 | 1,55 | 0,89R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 44/30 | 20/30 | 0,96 | 1,64 | -0,03R | €13,54 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 87/30 | 20/30 | 1,08 | 0,89 | 0,05R | €-2,69 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 4/30 | 4/30 | 0,57 | 0,16 | -0,36R | €-23,05 | 1,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 4/30 | 6/30 | 0,57 | 0,25 | -0,36R | €-27,46 | 1,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 9/30 | 3,47 | 0,44 | 0,91R | €-17,15 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 24/30 | 8/30 | 0,63 | 0,59 | -0,29R | €-16,39 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 2/30 | 0,00 | 1,36 | 0,00R | €13,23 | 0,43% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-86,93 | 0,61% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 2/30 | 0,00 | 0,94 | 0,00R | €-2,27 | 0,43% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 24/30 | 38/30 | 0,50 | 0,61 | -0,42R | €-7,24 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 24/30 | 6/30 | 0,50 | 0,36 | -0,41R | €-29,10 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 18/30 | 6/30 | 0,57 | 0,35 | -0,38R | €-29,50 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 24/30 | 16/30 | 0,50 | 0,53 | -0,41R | €-21,16 | 4,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 24/30 | 6/30 | 0,50 | 0,36 | -0,42R | €-29,10 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 113/30 | 24/30 | 1,02 | 0,82 | 0,02R | €-3,30 | 3,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 40/30 | 34/30 | 1,66 | 1,25 | 0,38R | €6,89 | 3,69% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-53,50 | 0,93% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-53,50 | 0,93% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-53,50 | 0,93% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 43/30 | 26/30 | 1,03 | 0,72 | 0,02R | €-6,82 | 5,48% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,21% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,21% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 63/30 | 23/30 | 1,40 | 2,25 | 0,25R | €21,50 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 11/30 | 4/30 | 0,76 | 0,47 | -0,18R | €-16,77 | 2,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 22/30 | 5/30 | 0,78 | 1,73 | -0,16R | €15,83 | 2,20% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 17/30 | 18/30 | 0,89 | 0,53 | -0,08R | €-12,38 | 2,88% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 17/30 | 5/30 | 0,89 | 1,91 | -0,08R | €21,53 | 1,64% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 20/30 | 21/30 | 0,71 | 0,43 | -0,23R | €-15,91 | 4,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 20/30 | 8/30 | 0,71 | 0,79 | -0,23R | €-7,24 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 25/30 | 14/30 | 0,80 | 0,25 | -0,15R | €-20,50 | 3,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 17/30 | 9/30 | 0,86 | 2,22 | -0,11R | €22,07 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 17/30 | 8/30 | 0,86 | 1,87 | -0,11R | €17,72 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 76/30 | 31/30 | 1,31 | 2,38 | 0,19R | €23,66 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 5/30 | 5/30 | 1,14 | 0,38 | 0,09R | €-22,13 | 2,14% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 2/30 | 3/30 | 0,00 | 0,00 | -1,13R | €-55,54 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 4/30 | 4/30 | 1,71 | 1,29 | 0,39R | €8,01 | 1,67% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07038**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.1 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64156.3 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07021**; close **0.07021**; wick alta **0.0%**; volume **x1.26**

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
- Confidenza: **65,50%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC ribassista confermato dalla breadth: score -2.0, 33% sopra EMA50, ADX 23.1.
- BTC trend score: **-2,00**; ADX: **23,14**; breadth sopra EMA50: **33,33%**
- Mediana alt vs BTC: **-0,16%**; dispersione: **12,42%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **588**
- Trade research chiusi: **2601**
- Eventi di mercato indipendenti chiusi: **697**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **12147**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 15 | 54 | 54 | 35,19% | 1,05 | 0,03R | €16,54 |
| RSI_EXTREME_LONG_15M | 0 | 10 | 10 | 30,00% | 0,31 | -0,54R | €-54,33 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 20 | 161 | 161 | 34,78% | 1,02 | 0,02R | €24,53 |
| Bilanciata 1H V2 | 12 | 43 | 38 | 46,51% | 1,75 | 0,39R | €166,85 |
| Bilanciata 1H V3 Filtered | 17 | 66 | 66 | 40,91% | 1,31 | 0,19R | €125,56 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V1 | 10 | 198 | 198 | 39,90% | 0,95 | -0,03R | €-61,41 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 15 | 15 | 53,33% | 1,86 | 0,36R | €54,58 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 9 | 60 | 60 | 46,67% | 1,20 | 0,11R | €67,52 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 12 | 63 | 63 | 41,27% | 0,96 | -0,02R | €-13,72 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 44 | 44 | 52,27% | 1,45 | 0,23R | €102,04 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 55 | 55 | 32,73% | 0,90 | -0,07R | €-38,12 |
| Rapida 1H V2 | 3 | 11 | 10 | 27,27% | 0,46 | -0,43R | €-47,45 |
| Rapida 1H V3 Filtered | 11 | 104 | 104 | 43,27% | 1,05 | 0,03R | €33,32 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 8 | 52 | 52 | 46,15% | 1,14 | 0,08R | €42,45 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 26 | 26 | 42,31% | 1,01 | 0,01R | €1,99 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 26 | 26 | 42,31% | 1,01 | 0,01R | €1,99 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 31 | 31 | 32,26% | 0,66 | -0,25R | €-76,03 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 11 | 59 | 59 | 42,37% | 0,98 | -0,01R | €-7,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 11 | 60 | 60 | 41,67% | 0,95 | -0,03R | €-19,04 |
| SHADOW_4H_WIDE | 22 | 48 | 48 | 29,17% | 1,12 | 0,09R | €42,25 |
| SHADOW_BOLLINGER_MR_1H | 7 | 38 | 38 | 42,11% | 0,96 | -0,03R | €-9,68 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 4 | 4 | 0,00% | 0,00 | -1,12R | €-45,00 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 21 | 107 | 107 | 38,32% | 1,16 | 0,10R | €110,43 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 29 | 29 | 27,59% | 0,71 | -0,22R | €-63,89 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 21 | 74 | 74 | 36,49% | 1,06 | 0,04R | €28,97 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 19 | 50 | 50 | 32,00% | 0,86 | -0,10R | €-51,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 8 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,19 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 26 | 26 | 15,38% | 0,33 | -0,61R | €-157,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 12 | 35 | 35 | 20,00% | 0,69 | -0,26R | €-92,64 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 12 | 35 | 35 | 20,00% | 0,69 | -0,26R | €-92,64 |
| SHADOW_COMBO_MEAN_REVERSION | 4 | 16 | 16 | 37,50% | 0,84 | -0,11R | €-16,81 |
| SHADOW_COMBO_SCANNER | 9 | 64 | 64 | 42,19% | 1,46 | 0,28R | €178,80 |
| SHADOW_COMBO_TREND | 20 | 82 | 82 | 34,15% | 1,08 | 0,06R | €47,30 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 15 | 44 | 44 | 29,55% | 0,96 | -0,03R | €-12,17 |
| SHADOW_EMA_TREND_1H | 20 | 87 | 87 | 33,33% | 1,08 | 0,05R | €47,35 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,33 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 9 | 24 | 24 | 25,00% | 0,63 | -0,29R | €-70,51 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 8 | 24 | 24 | 20,83% | 0,50 | -0,42R | €-99,72 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 8 | 24 | 24 | 20,83% | 0,50 | -0,41R | €-99,57 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 8 | 18 | 18 | 16,67% | 0,57 | -0,38R | €-68,88 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 24 | 24 | 20,83% | 0,50 | -0,41R | €-99,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | 8 | 24 | 24 | 20,83% | 0,50 | -0,42R | €-99,72 |
| Forza relativa 1H V1 | 19 | 113 | 113 | 31,86% | 1,02 | 0,02R | €18,57 |
| Forza relativa 1H V2 | 7 | 43 | 40 | 44,19% | 1,66 | 0,38R | €163,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 9 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 9 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 9 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 12 | 43 | 43 | 32,56% | 1,03 | 0,02R | €8,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | 8 | 63 | 63 | 39,68% | 1,40 | 0,25R | €154,95 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 11 | 11 | 27,27% | 0,76 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 7 | 22 | 22 | 27,27% | 0,78 | -0,16R | €-35,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 5 | 17 | 17 | 29,41% | 0,89 | -0,08R | €-13,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 17 | 17 | 29,41% | 0,89 | -0,08R | €-13,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 20 | 20 | 25,00% | 0,71 | -0,23R | €-45,62 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 20 | 20 | 25,00% | 0,71 | -0,23R | €-45,62 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 8 | 25 | 25 | 28,00% | 0,80 | -0,15R | €-36,75 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 8 | 17 | 17 | 23,53% | 0,86 | -0,11R | €-18,58 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 8 | 17 | 17 | 23,53% | 0,86 | -0,11R | €-18,58 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 76 | 76 | 40,79% | 1,31 | 0,19R | €145,12 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 5 | 5 | 40,00% | 1,14 | 0,09R | €4,59 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,70 |
| SHADOW_SOL_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 2 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | ALT_ROTATION_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,02R | €-51,22 |
| MAIN | RANGE | 9 | 18 | 18 | 33,33% | 0,96 | -0,02R | €-4,35 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,18 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,27 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 10 | 42 | 42 | 40,48% | 1,31 | 0,18R | €77,26 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 1 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 12 | 12 | 25,00% | 0,68 | -0,23R | €-27,74 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 11 | 18 | 16 | 44,44% | 1,61 | 0,33R | €59,13 |
| Bilanciata 1H V2 | TRANSITION | 1 | 19 | 17 | 42,11% | 1,50 | 0,28R | €52,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 10 | 10 | 40,00% | 1,23 | 0,14R | €14,28 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 12 | 11 | 11 | 72,73% | 5,11 | 1,14R | €125,09 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 1 | 13 | 13 | 23,08% | 0,60 | -0,30R | €-39,03 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 2 | 20 | 20 | 25,00% | 0,47 | -0,39R | €-78,83 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 7 | 60 | 60 | 48,33% | 1,38 | 0,19R | €113,79 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,83R | €-41,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 4 | 4 | 100,00% | ∞ | 1,49R | €59,40 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 23,53% | 0,44 | -0,42R | €-70,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 7 | 24 | 24 | 70,83% | 3,24 | 0,70R | €166,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 18 | 18 | 22,22% | 0,41 | -0,45R | €-80,97 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 7 | 23 | 23 | 60,87% | 2,09 | 0,45R | €103,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 0,75 | -0,17R | €-18,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 5 | 20 | 20 | 75,00% | 4,06 | 0,81R | €162,01 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 3 | 17 | 17 | 17,65% | 0,42 | -0,47R | €-79,61 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 8 | 18 | 18 | 50,00% | 1,82 | 0,43R | €78,10 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,78 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 3 | 8 | 7 | 37,50% | 0,74 | -0,18R | €-14,11 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 6 | 23 | 23 | 60,87% | 2,08 | 0,45R | €104,19 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 0,48 | -0,40R | €-59,35 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 6 | 21 | 21 | 71,43% | 3,34 | 0,72R | €150,59 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 11 | 11 | 72,73% | 3,88 | 0,80R | €88,06 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 11 | 11 | 72,73% | 3,88 | 0,80R | €88,06 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,04 | 0,44R | €52,89 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 19 | 19 | 31,58% | 0,61 | -0,28R | €-52,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 6 | 23 | 23 | 60,87% | 2,08 | 0,45R | €104,19 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 19 | 19 | 31,58% | 0,61 | -0,28R | €-52,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 6 | 23 | 23 | 60,87% | 2,08 | 0,45R | €104,19 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 2,79R | €55,73 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 8 | 19 | 19 | 26,32% | 0,97 | -0,02R | €-4,43 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 14 | 14 | 42,86% | 2,03 | 0,61R | €84,85 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 7 | 13 | 13 | 30,77% | 0,58 | -0,32R | €-41,26 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,86 | 0,45R | €26,75 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 10 | 30 | 30 | 40,00% | 1,22 | 0,14R | €41,44 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 19 | 19 | 42,11% | 1,46 | 0,26R | €49,12 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 2 | 10 | 10 | 20,00% | 0,46 | -0,47R | €-46,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 2 | 9 | 9 | 44,44% | 1,57 | 0,32R | €28,71 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 10 | 18 | 18 | 50,00% | 1,85 | 0,44R | €79,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 10 | 18 | 18 | 50,00% | 1,85 | 0,44R | €79,91 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 5 | 6 | 6 | 50,00% | 1,95 | 0,48R | €29,06 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 3 | 5 | 5 | 20,00% | 0,45 | -0,47R | €-23,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 4 | 6 | 6 | 33,33% | 1,34 | 0,25R | €14,94 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 6 | 11 | 11 | 27,27% | 1,06 | 0,04R | €4,62 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 4 | 6 | 6 | 33,33% | 1,34 | 0,25R | €14,94 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 6 | 11 | 11 | 27,27% | 1,06 | 0,04R | €4,62 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 3 | 8 | 8 | 37,50% | 0,82 | -0,12R | €-9,97 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 3 | 12 | 12 | 50,00% | 2,11 | 0,57R | €68,06 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 14 | 14 | 42,86% | 1,34 | 0,21R | €28,81 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 5 | 7 | 7 | 28,57% | 0,81 | -0,14R | €-9,97 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 8 | 22 | 22 | 36,36% | 1,18 | 0,12R | €26,25 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 15 | 15 | 40,00% | 1,53 | 0,30R | €45,22 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 2 | 9 | 9 | 22,22% | 0,58 | -0,35R | €-31,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 5 | 6 | 6 | 33,33% | 1,17 | 0,12R | €7,03 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 6 | 13 | 13 | 23,08% | 0,69 | -0,25R | €-32,74 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 8 | 8 | 25,00% | 0,67 | -0,26R | €-20,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 8 | 21 | 21 | 38,10% | 1,38 | 0,23R | €47,69 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 15 | 15 | 40,00% | 1,53 | 0,30R | €45,21 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 2 | 9 | 9 | 33,33% | 1,02 | 0,01R | €1,10 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,40R | €24,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 14,29% | 0,32 | -0,60R | €-41,93 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 6 | 6 | 33,33% | 0,98 | -0,01R | €-0,89 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 7 | 7 | 42,86% | 1,47 | 0,27R | €18,98 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 7 | 7 | 42,86% | 1,47 | 0,27R | €18,98 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 6 | 6 | 16,67% | 0,59 | -0,35R | €-20,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 10 | 10 | 50,00% | 1,96 | 0,49R | €48,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 7 | 7 | 42,86% | 1,47 | 0,27R | €18,98 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 4 | 8 | 8 | 12,50% | 0,30 | -0,63R | €-50,74 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 9 | 30 | 30 | 30,00% | 0,93 | -0,05R | €-14,96 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 1 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 60,00% | 3,13 | 0,86R | €43,16 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 3 | 8 | 8 | 62,50% | 3,58 | 0,99R | €78,83 |
| Forza relativa 1H V2 | TRANSITION | 2 | 11 | 10 | 36,36% | 1,19 | 0,13R | €14,14 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 8 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 8 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 8 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 9 | 14 | 14 | 42,86% | 1,33 | 0,20R | €28,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 13 | 13 | 46,15% | 2,10 | 0,52R | €68,08 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 12 | 12 | 41,67% | 1,49 | 0,30R | €36,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 8 | 8 | 37,50% | 1,29 | 0,19R | €14,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 2 | 8 | 8 | 37,50% | 1,29 | 0,19R | €14,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 2 | 8 | 8 | 37,50% | 1,29 | 0,19R | €14,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 2 | 8 | 8 | 37,50% | 1,29 | 0,19R | €14,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 2 | 8 | 8 | 37,50% | 1,29 | 0,19R | €14,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 2 | 8 | 8 | 37,50% | 1,29 | 0,19R | €14,84 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 5 | 5 | 20,00% | 0,74 | -0,22R | €-10,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 5 | 5 | 20,00% | 0,74 | -0,22R | €-10,76 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 14 | 14 | 50,00% | 2,23 | 0,54R | €75,95 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 28 | 28 | 50,00% | 1,84 | 0,45R | €125,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,35 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-25T14:53:47+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **575**
- Scenari virtuali ancora attivi: **5748**
- Gruppi in attesa dell'uscita originale: **309**
- Gruppi con originale chiuso ma Shadow ancora attive: **266**
- Confronti completati: **20841**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 1034 | 1098 | €-3,93 | 47,1% | 305 | 127 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 1033 | 1097 | +€2,91 | 49,0% | 336 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 1033 | 1097 | +€1,02 | 47,9% | 343 | 9 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 1033 | 1097 | €-1,17 | 46,6% | 339 | 24 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 1033 | 1097 | €-1,53 | 47,2% | 359 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 1026 | 1090 | €-2,46 | 46,0% | 326 | 40 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 1022 | 1086 | €-1,10 | 44,6% | 155 | 227 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 1014 | 1078 | +€3,84 | 43,7% | 282 | 25 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 1014 | 1078 | +€1,86 | 41,3% | 310 | 23 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 1013 | 1077 | +€2,04 | 44,0% | 264 | 39 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 1010 | 1074 | +€0,68 | 43,4% | 225 | 78 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 999 | 1063 | €-0,57 | 40,2% | 182 | 149 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 977 | 1041 | +€3,92 | 33,0% | 131 | 94 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 951 | 1015 | +€4,23 | 42,0% | 72 | 154 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 934 | 998 | €-2,51 | 36,9% | 81 | 258 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 916 | 980 | €-13,45 | 29,0% | 214 | 156 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 913 | 977 | €-3,45 | 34,8% | 92 | 204 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 900 | 964 | €-7,12 | 29,9% | 77 | 249 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 884 | 948 | €-10,99 | 26,7% | 71 | 253 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 821 | 885 | €-17,09 | 21,9% | 70 | 246 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-25T14:53:49+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **20841**
- Valutazioni prodotte: **5852**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TP_R200 | 316 | 0,187 | 0,243 | 0,080 | 58,9% | 92,2 | ELIGIBLE_FOR_MUTATION |
| GB30_R100 | 362 | 0,104 | 0,149 | 0,019 | 57,7% | 87,5 | VALIDATING |
| GB20_R100 | 363 | 0,133 | 0,078 | 0,049 | 55,9% | 85,8 | VALIDATING |
| TP_R100 | 363 | 0,099 | 0,053 | 0,012 | 52,3% | 82,3 | VALIDATING |
| GB40_R100 | 360 | 0,058 | 0,149 | -0,024 | 55,8% | 78,2 | VALIDATING |
| GB20_R050 | 367 | 0,043 | 0,147 | -0,052 | 56,1% | 77,2 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 660 | 0,092 | 0,000 | 0,028 | 46,1% | 70,0 | VALIDATING |
| TP_R150 | 633 | 0,063 | 0,000 | 0,012 | 28,1% | 69,8 | VALIDATING |
| GB20_R100 | 645 | 0,065 | 0,000 | 0,015 | 37,4% | 69,8 | VALIDATING |
| GB30_R050 | 660 | 0,051 | 0,000 | -0,016 | 44,5% | 67,7 | VALIDATING |
| TP_R150 | 338 | 0,150 | 0,000 | 0,068 | 42,9% | 65,9 | VALIDATING |
| TP_R200 | 629 | 0,040 | 0,000 | -0,028 | 34,8% | 60,0 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TP_R100 | 645 | 0,033 | 0,000 | -0,022 | 35,2% | 58,7 | VALIDATING |
| GB30_R050 | 367 | 0,009 | 0,135 | -0,086 | 55,3% | 56,3 | VALIDATING |
| GB30_R100 | 645 | 0,026 | 0,000 | -0,029 | 37,1% | 55,2 | VALIDATING |
| GB50_R100 | 351 | -0,008 | 0,053 | -0,083 | 53,0% | 51,5 | VALIDATING |
| TP_R050 | 660 | 0,013 | 0,000 | -0,054 | 43,5% | 51,5 | VALIDATING |
| TP_R050 | 367 | -0,045 | 0,104 | -0,136 | 55,3% | 50,6 | VALIDATING |

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

Generato: 2026-07-25T14:54:02+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 19 | 100,00% | 1,24 | +€85,35 | +€4,49 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 19 | 100,00% | 1,07 | +€26,01 | +€1,37 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 3 | 100,00% | 1,26 | +€13,93 | +€4,64 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 3 | 100,00% | 1,08 | +€4,49 | +€1,50 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-25T14:53:38+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **17**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-86.30 R**
- Profitto virtuale mancato: **142.92 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 193 | 0 | 17295.49 |
| DOWN_20 | 193 | 0 | 34590.97 |
| DOWN_30 | 193 | 0 | 51886.46 |
| DOWN_40 | 193 | 47 | 66330.01 |
| UP_10 | 119 | 0 | 29644.05 |
| UP_20 | 119 | 0 | 59288.10 |
| UP_30 | 119 | 0 | 88932.16 |
| UP_40 | 119 | 58 | 106815.66 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-25T14:53:13+00:00

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

Generato: 2026-07-25T14:54:02+00:00

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

Generato: 2026-07-25T14:54:02+00:00

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

Generato: 2026-07-25T14:54:02+00:00

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

Generato: 2026-07-25T14:54:02+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **111**
- Hall of Fame: **15**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 21.1 | E | 31 | 2.40 | 0.463 | 5.75 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 17.4 | E | 36 | 1.75 | 0.241 | 3.71 |
| 3 | SHADOW_1H_BALANCED | BASELINE | 17.3 | E | 39 | 1.62 | 0.226 | 4.17 |
| 4 | SHADOW_1H_BALANCED_V3 | BASELINE | 16.9 | E | 36 | 1.60 | 0.268 | 3.23 |
| 5 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 15.8 | E | 32 | 1.61 | 0.219 | 3.68 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 13.6 | E | 67 | 1.20 | 0.079 | 5.36 |
| 7 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 13.6 | E | 37 | 1.38 | 0.159 | 5.40 |
| 8 | SHADOW_1H_BALANCED_V2 | BASELINE | 13.5 | E | 30 | 1.34 | 0.127 | 4.17 |
| 9 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 12.3 | E | 35 | 1.30 | 0.118 | 3.55 |
| 10 | SHADOW_RELATIVE_STRENGTH_V2 | BASELINE | 11.1 | E | 35 | 1.27 | 0.147 | 6.62 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-25T14:54:02+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **366**
- Strategie preferite nel regime corrente: **3**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **183**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | INSUFFICIENT | 81.6 | 4 | 99.00 | 1.441 | 0.00 |
| 2 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.519 | 0.00 |
| 3 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.457 | 0.00 |
| 4 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.457 | 0.00 |
| 5 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 6 | SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | shadow-scanner-top5-btc-btc-le3-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.292 | 0.00 |
| 7 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 8 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 9 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.987 | 0.00 |
| 10 | MAIN_SIDE_REGIME_GUARD_V1 | main-side-regime-guard-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.987 | 0.00 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-25T14:54:02+00:00

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

Generato: 2026-07-25T14:53:38+00:00

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
