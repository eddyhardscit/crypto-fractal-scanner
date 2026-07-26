# Paper trading automatico KuCoin

Generato: 2026-07-26T06:54:18+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-26T06:53:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-26T06:53:25+00:00 | 2026-07-26T06:53:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-26T06:30:00+00:00 | 2026-07-26T06:30:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-26T05:00:00+00:00 | 2026-07-26T05:00:00+00:00 | 53,5 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-26T00:00:00+00:00 | 2026-07-26T00:00:00+00:00 | 2,89 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ESPORTS | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | EUL | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ALLO | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SHIB | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -5,17 | 6,00 | 0,83 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 5,13 | 6,00 | 0,87 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,68 | 6,00 | 2,32 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,63 | 6,00 | 3,37 | STALE_CANDLE | 2,89 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -1,50 | 6,00 | 4,50 | STALE_CANDLE | 2,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,18 | 6,00 | 4,82 | STALE_CANDLE | 2,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 2,89 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 173.5 minuti; tolleranza 60 minuti. |
| Scalp RSI Long 25 · €10 · 15x | ESPORTS | 15m | LONG | 10,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: stop tecnico ≤5.0%. RSI 23.8→36.2; volume x9.01; shock 2.48 ATR. |
| Scalp RSI Long 25 · €50 · 15x | ESPORTS | 15m | LONG | 10,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: stop tecnico ≤5.0%. RSI 23.8→36.2; volume x9.01; shock 2.48 ATR. |
| Scalp RSI Long 25 · prudente · 5x | ESPORTS | 15m | LONG | 10,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: stop tecnico ≤5.0%. RSI 23.8→36.2; volume x9.01; shock 2.48 ATR. |
| Scalp RSI Long 20 · €10 · 15x | ESPORTS | 15m | LONG | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤20.0, stop tecnico ≤5.0%. RSI 23.8→36.2; volume x9.01; shock 2.48 ATR. |
| Scalp RSI Long 20 · €50 · 15x | ESPORTS | 15m | LONG | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤20.0, stop tecnico ≤5.0%. RSI 23.8→36.2; volume x9.01; shock 2.48 ATR. |
| Scalp RSI Long 20 · prudente · 5x | ESPORTS | 15m | LONG | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤20.0, stop tecnico ≤5.0%. RSI 23.8→36.2; volume x9.01; shock 2.48 ATR. |
| Scalp RSI Long 15 · €10 · 15x | BTC | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |
| Scalp RSI Long 20 · €10 · 15x | BTC | 15m | LONG | 7,00 | 8,00 | 1,00 | BELOW_SCORE | 8,5 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +7.00; soglia ±8.00; mancano 1.00 punti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.758,08 | -2,42% | €-241,92 | €3.000,00 | -8,06% | 4 | 20 | 30,00% | 0,68 | 4,49% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 20 | 674 | CAMPIONE INSUFFICIENTE | 30 (mancano 10) |

- Trade del Principale 4H chiusi: **20**; win rate **30,00%**; profit factor **0,68**.
- Expectancy: **€-12,00** per trade; P&L netto: **€-239,93**; max drawdown: **4,49%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.758,08 | €958,82 | €2.876,46 | €99,82 | €-0,99 |
| TEST | Scanner Top 5 Long 1H | 4 | €10.630,72 | €1.343,05 | €2.686,11 | €161,89 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.579,73 | €2.097,44 | €4.194,88 | €102,83 | €75,13 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.553,32 | €1.688,99 | €5.066,96 | €210,66 | €-1,29 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.515,73 | €1.613,73 | €4.841,20 | €207,30 | €30,51 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.445,30 | €601,72 | €1.805,16 | €105,02 | €52,97 |
| TEST | Bilanciata 1H V1 | 5 | €10.434,91 | €1.723,63 | €5.170,90 | €106,78 | €18,85 |
| TEST | Rapida V1 — score 6–7,5 | 2 | €10.422,16 | €1.133,93 | €3.401,80 | €103,79 | €-1,67 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.404,71 | €1.384,69 | €2.769,38 | €158,28 | €1,86 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.382,10 | €1.131,44 | €3.394,31 | €103,67 | €-1,66 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 5 | €10.360,27 | €982,91 | €2.948,72 | €155,78 | €48,05 |
| TEST | Rapida V3 NoHigh — Regime Guard | 5 | €10.354,40 | €1.024,71 | €3.074,12 | €207,94 | €5,09 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €10.327,22 | €477,92 | €1.433,76 | €106,02 | €-0,09 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.296,98 | €424,09 | €1.272,26 | €103,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 4 | €10.268,46 | €559,42 | €1.678,27 | €53,66 | €93,64 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.263,70 | €1.246,58 | €2.493,17 | €103,70 | €85,21 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.252,05 | €332,13 | €996,40 | €102,04 | €-22,03 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 5 | €10.249,04 | €1.021,85 | €3.065,55 | €155,96 | €39,77 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 3 | €10.234,58 | €1.262,46 | €3.787,38 | €101,24 | €50,29 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 3 | €10.225,09 | €1.251,66 | €3.754,99 | €101,22 | €50,26 |
| TEST | FAST NoHigh <7,5 · SHORT only | 4 | €10.224,35 | €2.224,62 | €6.673,87 | €152,05 | €50,59 |
| TEST | Combo Adaptive — madre | 5 | €10.221,23 | €2.175,38 | €4.350,76 | €204,61 | €18,69 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.208,32 | €2.091,35 | €6.274,04 | €204,92 | €-20,02 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 6 | €10.205,15 | €1.048,68 | €3.146,03 | €100,76 | €87,14 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €10.186,80 | €1.097,55 | €3.292,64 | €204,17 | €26,78 |
| TEST | MAIN — Dynamic Asset Selector | 3 | €10.184,32 | €996,99 | €2.990,97 | €101,25 | €-13,06 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.174,52 | €205,84 | €617,51 | €0,00 | €54,26 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.168,21 | €1.136,15 | €3.408,46 | €101,24 | €25,23 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.151,30 | €986,57 | €2.959,70 | €200,28 | €-30,30 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.136,73 | €1.717,11 | €3.434,22 | €151,60 | €30,90 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.135,81 | €2.702,71 | €8.108,12 | €202,99 | €-22,76 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 2 | €10.124,98 | €1.390,42 | €4.171,26 | €101,19 | €23,58 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.121,46 | €1.367,95 | €2.735,91 | €153,82 | €2,04 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 2 | €10.119,04 | €1.389,60 | €4.168,81 | €101,13 | €23,56 |
| TEST | Btc Bollinger 1H | 1 | €10.113,81 | €1.402,77 | €4.208,32 | €50,50 | €17,56 |
| TEST | Combo Mean Reversion | 2 | €10.103,89 | €2.224,11 | €4.448,22 | €50,00 | €38,67 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €10.092,78 | €1.368,50 | €2.737,00 | €154,42 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 6 | €10.091,58 | €2.286,31 | €4.572,63 | €202,20 | €18,78 |
| TEST | Rapida 1H V2 | 2 | €10.087,47 | €2.884,57 | €8.653,70 | €100,39 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 5 | €10.086,06 | €2.213,50 | €4.427,00 | €201,69 | €18,09 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.083,37 | €1.516,61 | €4.549,84 | €153,50 | €-10,45 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.078,27 | €2.687,60 | €8.062,81 | €201,84 | €-22,63 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 4 | €10.075,83 | €589,27 | €1.767,80 | €101,28 | €51,05 |
| TEST | Rapida V3 — qualità completa + profit lock | 4 | €10.062,07 | €592,47 | €1.777,41 | €101,05 | €50,93 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.056,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €10.018,21 | €1.302,99 | €2.605,98 | €153,07 | €-1,27 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 4 | €10.010,17 | €2.118,91 | €6.356,74 | €199,54 | €31,18 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 4 | €10.004,96 | €819,12 | €2.457,37 | €153,26 | €-4,30 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.003,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.002,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 6 | €9.992,49 | €1.133,78 | €2.267,56 | €150,54 | €50,70 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €9.992,03 | €1.340,87 | €2.681,73 | €152,01 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 5 | €9.991,37 | €1.870,62 | €5.611,85 | €152,55 | €-22,45 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.983,19 | €1.316,28 | €2.632,57 | €151,09 | €2,04 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Rapida 1H V1 — madre | 2 | €9.974,17 | €1.645,02 | €4.935,06 | €99,89 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.967,73 | €830,21 | €1.660,43 | €49,74 | €20,52 |
| TEST | Combo Adaptive — Long Only | 5 | €9.966,89 | €2.708,23 | €5.416,47 | €197,84 | €2,81 |
| TEST | Sol Adaptive 4H | 1 | €9.966,26 | €761,04 | €1.522,08 | €49,74 | €18,81 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.949,77 | €1.153,43 | €3.460,30 | €49,83 | €-14,69 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.947,84 | €862,58 | €1.725,17 | €49,74 | €0,74 |
| TEST | Combo Adaptive — target pieno 3R | 5 | €9.947,55 | €2.240,27 | €4.480,54 | €199,25 | €17,99 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.944,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.940,74 | €1.734,53 | €3.469,06 | €199,10 | €-4,59 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.931,24 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €9.929,35 | €2.647,18 | €7.941,55 | €198,85 | €-22,32 |
| TEST | Forza relativa 1H V2 | 4 | €9.928,49 | €1.929,15 | €3.858,30 | €151,90 | €-10,75 |
| TEST | Eth Donchian 1H | 0 | €9.927,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 3 | €9.919,79 | €1.247,80 | €3.743,41 | €150,05 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.917,27 | €1.927,00 | €3.854,00 | €151,25 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €9.902,52 | €2.640,03 | €7.920,08 | €198,32 | €-22,26 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.902,28 | €1.154,19 | €2.308,39 | €50,00 | €34,08 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.893,76 | €1.186,90 | €2.373,81 | €50,00 | €46,28 |
| TEST | Scanner Top10 Long | 4 | €9.889,43 | €1.809,41 | €3.618,83 | €148,96 | €-14,38 |
| TEST | Scanner Top15 Long | 4 | €9.889,43 | €1.809,41 | €3.618,83 | €148,96 | €-14,38 |
| TEST | Scanner Top20 Long | 4 | €9.889,43 | €1.809,41 | €3.618,83 | €148,96 | €-14,38 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.888,15 | €1.146,74 | €3.440,21 | €49,54 | €-18,02 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 5 | €9.886,71 | €563,00 | €1.688,99 | €151,18 | €-26,29 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 5 | €9.886,71 | €563,00 | €1.688,99 | €151,18 | €-26,29 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.865,07 | €4.009,45 | €8.018,89 | €147,66 | €-5,85 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 3 | €9.863,84 | €1.877,19 | €3.754,39 | €150,60 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Top 5 + BTC — Guard | 4 | €9.855,31 | €1.196,81 | €2.393,62 | €150,57 | €-0,26 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 4 | €9.847,36 | €2.447,58 | €4.895,16 | €151,45 | €-0,13 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.815,76 | €1.138,34 | €3.415,02 | €49,18 | €-17,89 |
| TEST | Top 5 + BTC — solo MFE | 4 | €9.810,10 | €3.909,71 | €7.819,43 | €196,28 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.790,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 4 | €9.783,96 | €590,60 | €1.771,79 | €148,74 | €2,12 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.774,25 | €1.276,66 | €2.553,32 | €148,84 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.773,79 | €2.891,19 | €5.782,38 | €194,92 | €-4,32 |
| TEST | Scanner Bottom10 Short | 2 | €9.767,33 | €1.977,42 | €3.954,85 | €49,86 | €45,75 |
| TEST | Scanner Bottom15 Short | 2 | €9.767,33 | €1.977,42 | €3.954,85 | €49,86 | €45,75 |
| TEST | Scanner Bottom20 Short | 2 | €9.767,33 | €1.977,42 | €3.954,85 | €49,86 | €45,75 |
| TEST | Master Adaptive Runner25 V1 | 4 | €9.739,57 | €1.263,03 | €2.526,06 | €148,15 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 4 | €9.739,43 | €2.092,23 | €4.184,46 | €171,15 | €8,67 |
| TEST | Master Adaptive V1 | 4 | €9.730,10 | €1.263,75 | €2.527,51 | €148,19 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.730,10 | €1.263,75 | €2.527,51 | €148,19 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.729,35 | €1.282,83 | €2.565,66 | €147,28 | €1,73 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.724,36 | €1.583,60 | €3.167,19 | €48,61 | €17,79 |
| TEST | Forza relativa 1H V1 | 4 | €9.636,56 | €1.401,14 | €2.802,28 | €150,57 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.618,63 | €1.163,71 | €2.327,41 | €145,88 | €1,71 |
| TEST | Combo Trend | 4 | €9.612,56 | €1.360,97 | €2.721,94 | €148,18 | €10,70 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.565,64 | €2.419,55 | €4.839,09 | €146,01 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.521,88 | €2.034,13 | €4.068,27 | €190,44 | €0,00 |

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
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.758,08 | €-239,93 | 20 | 20 | 30,00% | 0,68 | €-12,00 | 4,49% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.630,72 | €631,85 | 34 | 34 | 55,88% | 1,85 | €18,58 | 2,70% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.579,73 | €507,69 | 24 | 24 | 54,17% | 2,06 | €21,15 | 2,12% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.553,32 | €557,35 | 42 | 42 | 45,24% | 1,60 | €13,27 | 2,20% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.515,73 | €488,12 | 46 | 46 | 50,00% | 1,55 | €10,61 | 2,83% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.445,30 | €393,42 | 39 | 39 | 48,72% | 1,56 | €10,09 | 2,49% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.434,91 | €421,78 | 43 | 43 | 53,49% | 1,48 | €9,81 | 2,30% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.422,16 | €425,86 | 44 | 44 | 47,73% | 1,55 | €9,68 | 2,49% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.404,71 | €404,25 | 26 | 26 | 50,00% | 1,67 | €15,55 | 2,25% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.382,10 | €385,17 | 8 | 8 | 87,50% | 7,94 | €48,15 | 1,17% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.360,27 | €313,61 | 4 | 4 | 100,00% | ∞ | €78,40 | 0,53% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.354,40 | €350,77 | 9 | 9 | 77,78% | 4,20 | €38,97 | 1,39% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.327,22 | €327,55 | 11 | 11 | 72,73% | 3,40 | €29,78 | 2,01% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.296,98 | €297,12 | 9 | 9 | 66,67% | 3,17 | €33,01 | 2,28% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.268,46 | €176,42 | 4 | 4 | 75,00% | 9,37 | €44,11 | 0,70% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.263,70 | €180,37 | 6 | 6 | 83,33% | 4,24 | €30,06 | 0,82% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.252,05 | €274,29 | 8 | 8 | 75,00% | 3,50 | €34,29 | 1,78% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.249,04 | €211,69 | 8 | 8 | 75,00% | 4,78 | €26,46 | 0,95% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.234,58 | €186,22 | 4 | 4 | 75,00% | 9,84 | €46,55 | 0,69% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.225,09 | €176,67 | 4 | 4 | 75,00% | 9,39 | €44,17 | 0,68% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.224,35 | €178,42 | 8 | 8 | 75,00% | 3,44 | €22,30 | 1,39% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.221,23 | €205,57 | 24 | 24 | 45,83% | 1,52 | €8,57 | 1,49% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.208,32 | €232,10 | 18 | 18 | 55,56% | 1,97 | €12,89 | 2,05% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.205,15 | €120,53 | 3 | 3 | 66,67% | 316,11 | €40,18 | 0,46% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.186,80 | €161,62 | 10 | 10 | 60,00% | 1,73 | €16,16 | 1,32% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.184,32 | €198,64 | 2 | 2 | 100,00% | ∞ | €99,32 | 0,78% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.174,52 | €120,63 | 3 | 3 | 66,67% | 316,37 | €40,21 | 0,45% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.168,21 | €144,49 | 3 | 3 | 66,67% | 3,67 | €48,16 | 0,75% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.151,30 | €182,96 | 7 | 7 | 57,14% | 2,48 | €26,14 | 1,60% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.136,73 | €108,22 | 6 | 6 | 50,00% | 1,96 | €18,04 | 0,97% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.135,81 | €163,05 | 73 | 73 | 38,36% | 1,11 | €2,23 | 2,89% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.124,98 | €103,91 | 5 | 5 | 60,00% | 1,95 | €20,78 | 0,81% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.121,46 | €120,80 | 12 | 12 | 58,33% | 1,33 | €10,07 | 2,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €10.119,04 | €97,97 | 1 | 1 | 100,00% | ∞ | €97,97 | 0,56% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.113,81 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.103,89 | €69,11 | 15 | 15 | 40,00% | 1,18 | €4,61 | 2,31% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.092,78 | €94,17 | 10 | 10 | 60,00% | 1,26 | €9,42 | 2,33% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.091,58 | €75,71 | 20 | 20 | 45,00% | 1,17 | €3,79 | 2,12% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.087,47 | €92,66 | 12 | 11 | 50,00% | 1,36 | €7,72 | 1,69% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.086,06 | €70,79 | 14 | 14 | 50,00% | 1,40 | €5,06 | 1,51% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.083,37 | €95,99 | 33 | 31 | 51,52% | 1,13 | €2,91 | 2,75% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.078,27 | €105,35 | 41 | 41 | 41,46% | 1,12 | €2,57 | 2,10% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €10.075,83 | €25,24 | 28 | 28 | 42,86% | 1,04 | €0,90 | 2,86% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €10.062,07 | €11,61 | 29 | 29 | 51,72% | 1,02 | €0,40 | 3,21% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.056,58 | €56,58 | 13 | 13 | 30,77% | 1,24 | €4,35 | 1,92% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.018,21 | €20,89 | 8 | 8 | 50,00% | 1,07 | €2,61 | 2,30% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,98 | €10,98 | 9 | 9 | 33,33% | 1,23 | €1,22 | 0,25% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €10.010,17 | €-17,68 | 4 | 4 | 25,00% | 0,84 | €-4,42 | 1,46% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €10.004,96 | €10,73 | 6 | 6 | 50,00% | 1,05 | €1,79 | 1,60% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.003,75 | €3,75 | 2 | 2 | 100,00% | ∞ | €1,88 | 0,07% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.002,57 | €2,57 | 2 | 2 | 100,00% | ∞ | €1,28 | 0,06% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,20 | €2,20 | 9 | 9 | 33,33% | 1,23 | €0,24 | 0,05% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,43 | €1,43 | 1 | 1 | 100,00% | ∞ | €1,43 | 0,06% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,97 | €0,97 | 1 | 1 | 100,00% | ∞ | €0,97 | 0,07% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,51 | €0,51 | 2 | 2 | 100,00% | ∞ | €0,26 | 0,01% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 1 | 1 | 100,00% | ∞ | €0,29 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.992,49 | €-56,35 | 24 | 24 | 33,33% | 0,91 | €-2,35 | 2,25% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.992,03 | €-6,51 | 9 | 9 | 55,56% | 0,98 | €-0,72 | 2,26% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.991,37 | €16,81 | 44 | 44 | 34,09% | 1,02 | €0,38 | 2,58% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Combo Scanner | Combo Scanner | €9.983,19 | €-17,52 | 30 | 30 | 46,67% | 0,98 | €-0,58 | 2,66% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.974,17 | €-23,25 | 76 | 76 | 34,21% | 0,99 | €-0,31 | 6,76% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.967,73 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.966,89 | €-32,81 | 8 | 8 | 37,50% | 0,86 | €-4,10 | 2,34% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.966,26 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Ema 1H | Trend following EMA | €9.949,77 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Sol Ema 4H | Trend following EMA | €9.947,84 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,57% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.947,55 | €-67,05 | 12 | 12 | 41,67% | 0,76 | €-5,59 | 1,41% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.944,12 | €-55,88 | 9 | 9 | 22,22% | 0,16 | €-6,21 | 0,56% |
| TEST | Ampia 4H | Confluenza trend | €9.940,74 | €-53,35 | 17 | 17 | 23,53% | 0,89 | €-3,14 | 3,67% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.931,24 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.929,35 | €-43,95 | 47 | 47 | 38,30% | 0,96 | €-0,94 | 2,49% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.928,49 | €-58,57 | 40 | 39 | 37,50% | 0,96 | €-1,46 | 4,86% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.927,32 | €-72,68 | 4 | 4 | 25,00% | 0,56 | €-18,17 | 1,38% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.919,79 | €-78,30 | 7 | 7 | 42,86% | 0,72 | €-11,19 | 1,69% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.917,27 | €-80,42 | 7 | 7 | 28,57% | 0,71 | €-11,49 | 2,23% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.902,52 | €-70,86 | 48 | 48 | 39,58% | 0,94 | €-1,48 | 2,96% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.902,28 | €-129,97 | 4 | 4 | 25,00% | 0,20 | €-32,49 | 1,38% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.893,76 | €-151,10 | 4 | 4 | 25,00% | 0,05 | €-37,77 | 1,53% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.889,43 | €-94,55 | 5 | 5 | 40,00% | 0,52 | €-18,91 | 2,86% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.889,43 | €-94,55 | 5 | 5 | 40,00% | 0,52 | €-18,91 | 2,86% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.889,43 | €-94,55 | 5 | 5 | 40,00% | 0,52 | €-18,91 | 2,86% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.888,15 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.886,71 | €-85,98 | 5 | 5 | 60,00% | 0,58 | €-17,20 | 2,11% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.886,71 | €-85,98 | 5 | 5 | 60,00% | 0,58 | €-17,20 | 2,11% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.865,07 | €-123,13 | 34 | 34 | 38,24% | 0,86 | €-3,62 | 3,70% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.863,84 | €-134,27 | 5 | 5 | 40,00% | 0,51 | €-26,85 | 2,22% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.855,31 | €-143,28 | 11 | 11 | 36,36% | 0,70 | €-13,03 | 3,31% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.847,36 | €-150,25 | 6 | 6 | 33,33% | 0,47 | €-25,04 | 2,98% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Eth Ema 1H | Trend following EMA | €9.815,76 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.810,10 | €-185,85 | 16 | 16 | 37,50% | 0,52 | €-11,62 | 3,95% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.790,66 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.783,96 | €-217,48 | 33 | 33 | 33,33% | 0,75 | €-6,59 | 3,65% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.774,25 | €-224,28 | 11 | 11 | 36,36% | 0,56 | €-20,39 | 2,80% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.773,79 | €-218,42 | 41 | 41 | 60,98% | 0,69 | €-5,33 | 4,16% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.767,33 | €-276,05 | 5 | 5 | 0,00% | 0,00 | €-55,21 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.767,33 | €-276,05 | 5 | 5 | 0,00% | 0,00 | €-55,21 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.767,33 | €-276,05 | 5 | 5 | 0,00% | 0,00 | €-55,21 | 2,72% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.739,57 | €-258,98 | 10 | 10 | 30,00% | 0,44 | €-25,90 | 3,19% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.739,43 | €-266,13 | 15 | 15 | 40,00% | 0,51 | €-17,74 | 2,68% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.730,10 | €-268,44 | 8 | 8 | 25,00% | 0,42 | €-33,56 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.730,10 | €-268,44 | 8 | 8 | 25,00% | 0,42 | €-33,56 | 3,19% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.729,35 | €-271,35 | 22 | 22 | 40,91% | 0,59 | €-12,33 | 2,88% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.724,36 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.636,56 | €-362,07 | 27 | 27 | 25,93% | 0,56 | €-13,41 | 5,74% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.618,63 | €-382,31 | 25 | 25 | 36,00% | 0,50 | €-15,29 | 4,05% |
| TEST | Combo Trend | Combo Trend | €9.612,56 | €-397,02 | 35 | 35 | 28,57% | 0,71 | €-11,34 | 5,93% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.565,64 | €-431,78 | 18 | 18 | 27,78% | 0,52 | €-23,99 | 4,69% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.521,88 | €-475,61 | 29 | 29 | 27,59% | 0,39 | €-16,40 | 5,33% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 75,02500 | 75,57185 | 98,06983 | 70,34400 | €20,35 | €61,04 | €1,44 | €-0,99 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00329 | 0,00329 | 0,00290 | 0,00221 | 0,00408 | €12,36 | €37,07 | €4,45 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,34590 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €18,65 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,26 | €27,78 | €0,60 | €0,20 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €138,85 | €416,55 | €49,99 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €142,81 | €428,43 | €51,41 | €0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,36742 | 0,35951 | 0,33054 | 0,24679 | 0,44120 | €161,71 | €485,13 | €48,70 | €-10,45 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00330 | 0,00330 | 0,00293 | 0,00221 | 0,00403 | €158,25 | €474,75 | €52,90 | €0,00 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €746,35 | €2.239,05 | €51,86 | €-1,29 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,12 | €474,35 | €49,93 | €0,00 |
| Rapida V1 — score 6–7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €167,22 | €501,65 | €51,54 | €0,00 |
| Rapida V1 — score 6–7,5 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €966,72 | €2.900,15 | €52,25 | €-1,67 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €53,83 | €161,50 | €2,91 | €-0,09 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,51 | €502,54 | €51,57 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €963,92 | €2.891,76 | €52,10 | €-1,66 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €165,85 | €497,54 | €51,12 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.045,31 | €3.135,93 | €52,26 | €15,47 |
| Rapida V1 — no HIGH + score <7,5 | EUL | LONG | Momentum / breakout | 60m | 3,0x | 2,41518 | 2,49860 | 2,12536 | 1,62220 | 2,84992 | €145,14 | €435,42 | €52,25 | €15,04 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €160,87 | €482,60 | €50,80 | €0,00 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,35951 | 0,34052 | 0,25233 | 0,42842 | €175,27 | €525,81 | €49,21 | €-22,63 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00387 | €157,69 | €473,06 | €49,80 | €0,00 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,35951 | 0,34052 | 0,25233 | 0,44600 | €177,34 | €532,02 | €49,79 | €-22,89 |
| Rapida V1 — target pieno 2R | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,76 | €32,27 | €0,58 | €0,44 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,77 | €485,30 | €51,08 | €0,00 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,35951 | 0,34052 | 0,25233 | 0,42842 | €176,34 | €529,01 | €49,51 | €-22,76 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €166,71 | €500,13 | €51,38 | €0,00 |
| Rapida V3 — score <7,5 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,62756 | €144,76 | €434,29 | €0,00 | €53,02 |
| Rapida V3 — score <7,5 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €31,47 | €94,42 | €1,70 | €-0,05 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,01 | €474,02 | €49,90 | €0,00 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,35951 | 0,34052 | 0,25233 | 0,42842 | €172,41 | €517,23 | €48,41 | €-22,26 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €155,06 | €465,19 | €48,97 | €0,00 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,40774 | €180,50 | €541,50 | €49,57 | €1,51 |
| Rapida V3 — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €11,07 | €33,21 | €1,24 | €0,62 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €160,75 | €482,24 | €49,49 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,62756 | €139,59 | €418,78 | €0,00 | €51,13 |
| Rapida V3 — Long + no HIGH + score <7,5 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €42,31 | €126,93 | €2,29 | €-0,07 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,44 | €475,31 | €50,03 | €0,00 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,35951 | 0,34052 | 0,25233 | 0,42842 | €172,88 | €518,63 | €48,54 | €-22,32 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,13 | €474,39 | €49,94 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,40774 | €184,93 | €554,79 | €50,79 | €1,54 |
| Rapida V3 senza ESPORTS — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €455,27 | €1.365,80 | €50,78 | €25,33 |
| Rapida V3 senza ESPORTS — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,44 | €151,33 | €2,73 | €-0,09 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,34590 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-22,03 |
| Rapida V3 senza ESPORTS — MFE Lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35802 | 0,35951 | 0,32525 | 0,24047 | 0,40718 | €180,50 | €541,49 | €49,57 | €2,25 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00358 | €199,03 | €597,09 | €50,62 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €18,16 | €54,48 | €2,10 | €-0,24 |
| Rapida V3 senza ESPORTS — Stress Guard | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €452,89 | €1.358,67 | €50,52 | €25,19 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €937,53 | €2.812,59 | €50,67 | €-1,62 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €159,93 | €479,80 | €49,24 | €0,00 |
| Rapida V3 — qualità completa + profit lock | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,29355 | 1,49563 | 2,62756 | €139,27 | €417,82 | €0,00 | €51,01 |
| Rapida V3 — qualità completa + profit lock | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €48,11 | €144,33 | €2,60 | €-0,08 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 58,68300 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-4,59 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00328 | 0,00328 | 0,00288 | 0,00165 | 0,00438 | €207,40 | €414,80 | €49,78 | €0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00413 | €208,36 | €416,72 | €50,01 | €0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €216,28 | €432,55 | €51,91 | €0,00 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,36855 | 0,35951 | 0,33045 | 0,18612 | 0,45238 | €219,06 | €438,12 | €45,30 | €-10,75 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,34590 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €13,12 |
| Benchmark Donchian breakout 1H | SHIB | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €505,25 | €1.010,51 | €0,00 | €62,01 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64392,60000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €16,84 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.392,21 | €2.784,42 | €49,71 | €-14,86 |
| Benchmark Bollinger mean reversion 1H | SHIB | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00001 | 0,00001 | €598,48 | €1.196,96 | €49,50 | €-7,84 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,34590 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €9,24 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | SHIB | LONG | Trend following EMA | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €479,93 | €959,86 | €0,00 | €58,91 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,55 | €29,10 | €0,69 | €0,20 |
| Benchmark trend following EMA 1H | BANK | LONG | Trend following EMA | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,47485 | €205,19 | €410,38 | €49,25 | €-17,66 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €224,41 | €448,82 | €53,86 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,34590 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €17,79 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €25,83 | €51,66 | €0,00 | €3,17 |
| Scanner Top10 Long | BANK | LONG | Scanner Top10 Long | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €-17,55 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,38133 | 0,34590 | 0,35209 | 0,57009 | 0,30594 | €246,17 | €492,34 | €0,00 | €45,75 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €25,83 | €51,66 | €0,00 | €3,17 |
| Scanner Top15 Long | BANK | LONG | Scanner Top15 Long | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €-17,55 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,38133 | 0,34590 | 0,35209 | 0,57009 | 0,30594 | €246,17 | €492,34 | €0,00 | €45,75 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €25,83 | €51,66 | €0,00 | €3,17 |
| Scanner Top20 Long | BANK | LONG | Scanner Top20 Long | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €-17,55 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,38133 | 0,34590 | 0,35209 | 0,57009 | 0,30594 | €246,17 | €492,34 | €0,00 | €45,75 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €219,41 | €438,82 | €52,66 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €12,99 | €25,97 | €0,00 | €1,86 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €196,51 | €393,01 | €47,16 | €0,00 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €207,86 | €415,72 | €49,89 | €0,00 |
| Top 5 + BTC — Guard | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €29,86 | €59,71 | €2,96 | €-0,26 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,72 | €421,44 | €50,57 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €201,88 | €403,77 | €48,45 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,35802 | 0,35951 | 0,31588 | 0,18080 | 0,45073 | €205,20 | €410,40 | €48,30 | €1,71 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €211,32 | €422,63 | €50,72 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,47485 | €14,78 | €29,56 | €3,55 | €-1,27 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €204,20 | €408,41 | €49,01 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,35802 | 0,35951 | 0,31588 | 0,18080 | 0,45073 | €207,57 | €415,15 | €48,86 | €1,73 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,22 | €426,44 | €51,17 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,24 | €28,48 | €0,00 | €2,04 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,56 | €427,11 | €51,25 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00329 | 0,00329 | 0,00290 | 0,00166 | 0,00416 | €208,78 | €417,57 | €50,11 | €0,00 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,34590 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €9,25 |
| Combo Trend | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €13,64 | €27,28 | €0,00 | €2,52 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €929,20 | €1.858,39 | €47,83 | €-1,07 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64392,60000 | 64181,91722 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €0,00 | €38,67 |
| Combo Mean Reversion | AKE | SHORT | Combo Mean Reversion | 60m | 2,0x | 0,00320 | 0,00320 | 0,00356 | 0,00479 | 0,00263 | €225,46 | €450,91 | €50,00 | €-0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,36 | €420,73 | €50,49 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | SHIB | LONG | Combo Scanner | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,61 | €33,22 | €0,00 | €2,04 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,34590 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €18,51 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,76 | €25,52 | €0,55 | €0,18 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00330 | 0,00330 | 0,00293 | 0,00166 | 0,00403 | €203,95 | €407,90 | €45,45 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00405 | €209,81 | €419,62 | €50,35 | €0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,34590 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €18,24 |
| Combo Adaptive — Quality7 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,94 | €33,88 | €1,68 | €-0,15 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €19,61 | €39,22 | €0,00 | €2,81 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,34590 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €8,67 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00444 | €209,99 | €419,98 | €50,40 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,34590 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €18,26 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,33 | €38,67 | €0,90 | €0,53 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,34590 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €18,01 |
| Combo Adaptive — target pieno 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €13,86 | €27,72 | €0,64 | €-0,02 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64392,60000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €-14,69 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64392,60000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €17,56 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 75,02500 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €0,74 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,02500 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €20,52 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,02500 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €18,81 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1883,04000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €-17,89 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1883,04000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €-18,02 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €201,87 | €403,75 | €48,45 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €206,32 | €412,65 | €49,52 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | SHIB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €492,66 | €985,32 | €48,89 | €-4,32 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €205,36 | €410,73 | €49,29 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Combo Adaptive — Side × Regime Guard | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €212,78 | €425,56 | €51,07 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,37453 | 0,34590 | 0,35269 | 0,55991 | 0,29289 | €232,55 | €465,11 | €0,00 | €35,55 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €548,64 | €1.097,29 | €0,00 | €67,34 |
| Combo Adaptive — Side × Regime Guard | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €40,53 | €81,06 | €1,74 | €0,57 |
| Combo Adaptive — Side × Regime Guard | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,46584 | €212,08 | €424,15 | €50,90 | €-18,25 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00317 | 0,00317 | 0,00283 | 0,00160 | 0,00387 | €231,91 | €463,82 | €50,56 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00400 | €209,67 | €419,35 | €50,32 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00275 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | SHIB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €15,15 | €30,30 | €1,13 | €-0,13 |
| Rapida V3 NoHigh — Range Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,34590 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-22,03 |
| Rapida V3 NoHigh — Regime Guard | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,34590 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-22,19 |
| Rapida V3 NoHigh — Regime Guard | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,40774 | €188,19 | €564,57 | €51,68 | €1,57 |
| Rapida V3 NoHigh — Regime Guard | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €463,29 | €1.389,88 | €51,68 | €25,77 |
| Rapida V3 NoHigh — Regime Guard | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €39,82 | €119,46 | €2,15 | €-0,07 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| MAIN — Side × Regime Guard | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 75,02500 | 75,57185 | 98,06983 | 70,34400 | €715,11 | €2.145,34 | €50,64 | €-34,75 |
| MAIN — Side × Regime Guard | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,34200 | 0,35951 | 0,34200 | 0,22971 | 0,42408 | €140,45 | €421,36 | €0,00 | €21,58 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,34590 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €38,40 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| MAIN — Dynamic Asset Selector | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 75,02500 | 75,57185 | 98,06983 | 70,34400 | €715,22 | €2.145,66 | €50,64 | €-34,75 |
| MAIN — Dynamic Asset Selector | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,34200 | 0,35951 | 0,34200 | 0,22971 | 0,42408 | €141,21 | €423,62 | €0,00 | €21,69 |
| Combo Trend — Side × Regime Guard | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €211,52 | €423,03 | €50,76 | €0,00 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,37453 | 0,34590 | 0,35665 | 0,55991 | 0,27565 | €207,96 | €415,93 | €0,00 | €31,79 |
| Combo Trend — Side × Regime Guard | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.073,98 | €2.147,95 | €51,13 | €15,12 |
| Combo Trend — Side × Regime Guard | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,58 | €33,16 | €0,00 | €1,81 |
| Combo Trend — Side × Regime Guard | BANK | LONG | Combo Trend | 60m | 2,0x | 0,37568 | 0,35951 | 0,33059 | 0,18972 | 0,47485 | €207,08 | €414,15 | €49,70 | €-17,82 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,36948 | 0,34590 | 0,35217 | 0,49079 | 0,31961 | €185,68 | €557,05 | €0,00 | €35,55 |
| FAST NoHigh <7,5 · SHORT only | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.016,35 | €3.049,05 | €50,81 | €15,04 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00314 | 0,00314 | 0,00287 | 0,00211 | 0,00354 | €200,24 | €600,71 | €51,24 | €0,00 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00328 | 0,00328 | 0,00288 | 0,00220 | 0,00406 | €137,93 | €413,80 | €49,66 | €0,00 |
| Bilanciata V3 · LONG only | SHIB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €347,90 | €1.043,70 | €49,90 | €32,42 |
| Bilanciata V3 · LONG only | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €719,52 | €2.158,55 | €50,00 | €-1,24 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,38133 | 0,34590 | 0,35209 | 0,57009 | 0,30594 | €249,04 | €498,07 | €0,00 | €46,28 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37547 | 0,34590 | 0,34244 | 0,56133 | 0,28964 | €216,32 | €432,65 | €0,00 | €34,08 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,76116 | €141,68 | €425,05 | €0,00 | €51,89 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €947,75 | €2.843,26 | €51,22 | €-1,63 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,42415 | €182,46 | €547,38 | €50,11 | €1,52 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,43 | €49,29 | €1,83 | €0,91 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €11,33 | €33,98 | €0,61 | €-0,02 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,32936 | 0,34590 | 0,35739 | 0,43751 | 0,27332 | €190,62 | €571,87 | €48,65 | €-28,71 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37922 | 0,34590 | 0,34961 | 0,50374 | 0,31790 | €205,84 | €617,51 | €0,00 | €54,26 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,03 | €486,10 | €49,94 | €0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,76116 | €9,08 | €27,24 | €0,00 | €3,33 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,42415 | €180,97 | €542,91 | €49,70 | €1,51 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €439,61 | €1.318,84 | €50,90 | €-5,79 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,32936 | 0,34590 | 0,35739 | 0,43751 | 0,27332 | €194,87 | €584,61 | €49,74 | €-29,35 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37547 | 0,34590 | 0,34244 | 0,49876 | 0,30872 | €185,38 | €556,13 | €0,00 | €43,80 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35802 | 0,35951 | 0,32525 | 0,24047 | 0,42357 | €185,12 | €555,36 | €50,84 | €2,31 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €196,95 | €590,84 | €50,09 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €444,54 | €1.333,61 | €51,47 | €-5,85 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,54081 | 2,49860 | 2,23591 | 1,70658 | 3,15060 | €9,87 | €29,61 | €3,55 | €-0,49 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,21 | €486,64 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,42415 | €184,35 | €553,05 | €50,63 | €1,54 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €438,92 | €1.316,76 | €50,82 | €-5,78 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €33,64 | €100,92 | €1,82 | €-0,06 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00319 | 0,00319 | 0,00287 | 0,00215 | 0,00385 | €162,18 | €486,55 | €49,99 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,76116 | €143,18 | €429,55 | €0,00 | €52,44 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,42415 | €188,32 | €564,95 | €51,72 | €1,57 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €447,71 | €1.343,13 | €51,84 | €-5,89 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €41,51 | €124,54 | €2,24 | €-0,07 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,35951 | 0,32569 | 0,24080 | 0,42415 | €182,46 | €547,38 | €50,11 | €1,52 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,43 | €49,29 | €1,83 | €0,91 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €11,33 | €33,98 | €0,61 | €-0,02 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,32936 | 0,34590 | 0,35739 | 0,43751 | 0,27332 | €190,62 | €571,87 | €48,65 | €-28,71 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37360 | 0,34590 | 0,35186 | 0,49626 | 0,30717 | €186,92 | €560,77 | €0,00 | €41,57 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,76116 | €142,49 | €427,47 | €0,00 | €52,19 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €67,78 | €203,35 | €3,66 | €-0,12 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €452,62 | €1.357,87 | €50,49 | €25,18 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €936,98 | €2.810,94 | €50,64 | €-1,61 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00289 | 0,00215 | 0,00382 | €172,57 | €517,70 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,29355 | 1,49563 | 2,76116 | €141,78 | €425,33 | €0,00 | €51,93 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €948,12 | €2.844,35 | €51,24 | €-1,63 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37453 | 0,34590 | 0,35071 | 0,49749 | 0,31103 | €196,07 | €588,21 | €0,00 | €44,96 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,49860 | 2,22675 | 1,49563 | 2,76116 | €9,57 | €28,71 | €0,00 | €3,50 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35041 | 0,35951 | 0,35041 | 0,23536 | 0,41456 | €185,41 | €556,23 | €0,00 | €14,44 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €200,37 | €601,11 | €50,97 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €436,24 | €1.308,71 | €48,66 | €24,27 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,02 | €63,07 | €1,14 | €-0,04 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,03756 | €-137,21 | -2,74 | LIQUIDATION_GAP |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,03756 | €-137,22 | -2,74 | LIQUIDATION_GAP |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,03756 | €-137,21 | -2,74 | LIQUIDATION_GAP |
| Master Adaptive GB20 — Loss Cap 0,75R | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-194,90 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive GB20 — 50% a 0,75R | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-193,79 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive GB20 — Breakeven 0,5R | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-194,85 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive Runner25 V1 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-191,43 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive Expanded V1 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-192,10 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive Strict3 V1 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-187,99 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive No Alt V1 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-191,24 | -3,85 | STOP_GAP_STRESS |
| Master Adaptive V1 | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-191,24 | -3,85 | STOP_GAP_STRESS |
| Combo Adaptive — parziale 1R | ESPORTS | LONG | 2026-07-26T06:53:38+00:00 | 0,02893 | €-97,96 | -3,85 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 2/30 | 4/30 | 1,88 | 9,37 | 0,46R | €44,11 | 0,70% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 2/30 | 4/30 | 1,88 | 9,84 | 0,46R | €46,55 | 0,69% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 2/30 | 4/30 | 1,88 | 9,39 | 0,46R | €44,17 | 0,68% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 3/30 | 6/30 | 0,94 | 1,05 | -0,04R | €1,79 | 1,60% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1/30 | 3/30 | ∞ | 316,37 | 1,96R | €40,21 | 0,45% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 1/30 | 3/30 | ∞ | 316,11 | 1,96R | €40,18 | 0,46% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 4/30 | 5/30 | 0,63 | 0,58 | -0,28R | €-17,20 | 2,11% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 3/30 | 4/30 | ∞ | ∞ | 1,95R | €78,40 | 0,53% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 4/30 | 8/30 | 5,75 | 4,78 | 1,21R | €26,46 | 0,95% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 1/30 | 1/30 | ∞ | ∞ | 1,96R | €97,97 | 0,56% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 3/30 | 7/30 | 0,94 | 2,48 | -0,04R | €26,14 | 1,60% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 4/30 | 5/30 | 0,63 | 0,58 | -0,28R | €-17,20 | 2,11% | COERENTE − | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 59/30 | 20/30 | 1,06 | 0,68 | 0,04R | €-12,00 | 4,49% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 2/30 | 0,00 | ∞ | 0,00R | €99,32 | 0,78% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 3/30 | 0,00 | 3,67 | 0,00R | €48,16 | 0,75% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 10/30 | 5/30 | 0,31 | 0,20 | -0,54R | €-4,60 | 0,37% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 10/30 | 9/30 | 0,45 | 0,16 | -0,37R | €-6,21 | 0,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 171/30 | 43/30 | 1,02 | 1,48 | 0,01R | €9,81 | 2,30% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 7/30 | 0,00 | 0,72 | 0,00R | €-11,19 | 1,69% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 46/30 | 31/30 | 1,44 | 1,13 | 0,25R | €2,91 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 76/30 | 42/30 | 1,18 | 1,60 | 0,12R | €13,27 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 3/30 | 4/30 | 0,92 | 0,84 | -0,06R | €-4,42 | 1,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 202/30 | 76/30 | 0,93 | 0,99 | -0,04R | €-0,31 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 15/30 | 13/30 | 1,86 | 1,24 | 0,36R | €4,35 | 1,92% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 6/30 | 8/30 | 2,80 | 3,44 | 0,62R | €22,30 | 1,39% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 68/30 | 46/30 | 1,22 | 1,55 | 0,12R | €10,61 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 73/30 | 41/30 | 1,01 | 1,12 | 0,01R | €2,57 | 2,10% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 8/30 | 0,00 | 7,94 | 0,00R | €48,15 | 1,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 11/30 | 0,00 | 3,40 | 0,00R | €29,78 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 9/30 | 0,00 | 3,17 | 0,00R | €33,01 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 49/30 | 44/30 | 1,39 | 1,55 | 0,20R | €9,68 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 66/30 | 44/30 | 0,99 | 1,02 | -0,01R | €0,38 | 2,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 11/30 | 11/30 | 0,63 | 1,36 | -0,27R | €7,72 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 113/30 | 73/30 | 1,10 | 1,11 | 0,06R | €2,23 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 57/30 | 39/30 | 1,12 | 1,56 | 0,07R | €10,09 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 28/30 | 29/30 | 1,04 | 1,02 | 0,02R | €0,40 | 3,21% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 28/30 | 28/30 | 1,04 | 1,04 | 0,02R | €0,90 | 2,86% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 37/30 | 33/30 | 0,94 | 0,75 | -0,04R | €-6,59 | 3,65% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 8/30 | 0,00 | 3,50 | 0,00R | €34,29 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 9/30 | 0,00 | 4,20 | 0,00R | €38,97 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 68/30 | 48/30 | 1,06 | 0,94 | 0,03R | €-1,48 | 2,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 10/30 | 0,00 | 1,73 | 0,00R | €16,16 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 18/30 | 0,00 | 1,97 | 0,00R | €12,89 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 5/30 | 0,00 | 1,95 | 0,00R | €20,78 | 0,81% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 68/30 | 47/30 | 0,99 | 0,96 | -0,01R | €-0,94 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 50/30 | 17/30 | 1,06 | 0,89 | 0,04R | €-3,14 | 3,67% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 44/30 | 34/30 | 1,01 | 0,86 | 0,00R | €-3,62 | 3,70% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 3/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 4/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 5/30 | 0,57 | 0,79 | -0,36R | €-6,87 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 116/30 | 24/30 | 1,14 | 1,52 | 0,09R | €8,57 | 1,49% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 33/30 | 8/30 | 0,94 | 0,86 | -0,04R | €-4,10 | 2,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 83/30 | 29/30 | 1,04 | 0,39 | 0,03R | €-16,40 | 5,33% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 58/30 | 15/30 | 0,89 | 0,51 | -0,08R | €-17,74 | 2,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 5/30 | 5/30 | 0,46 | 0,48 | -0,46R | €-16,52 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 5/30 | 5/30 | 0,46 | 0,17 | -0,46R | €-28,67 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 17/30 | 14/30 | 1,32 | 1,40 | 0,20R | €5,06 | 1,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 28/30 | 10/30 | 0,39 | 0,92 | -0,53R | €-2,35 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 38/30 | 20/30 | 0,62 | 1,17 | -0,33R | €3,79 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 6/30 | 0,00 | 4,24 | 0,00R | €30,06 | 0,82% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 38/30 | 12/30 | 0,62 | 0,76 | -0,33R | €-5,59 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 17/30 | 15/30 | 0,98 | 1,18 | -0,01R | €4,61 | 2,31% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 69/30 | 30/30 | 1,54 | 0,98 | 0,32R | €-0,58 | 2,66% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 89/30 | 35/30 | 1,12 | 0,71 | 0,08R | €-11,34 | 5,93% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 6/30 | 0,00 | 1,96 | 0,00R | €18,04 | 0,97% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 3/30 | 4/30 | 0,84 | 0,98 | -0,12R | €-0,31 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 4/30 | 8/30 | 1,71 | 1,55 | 0,39R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 52/30 | 24/30 | 0,93 | 2,06 | -0,05R | €21,15 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 94/30 | 24/30 | 1,11 | 0,91 | 0,07R | €-2,35 | 2,25% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 5/30 | 4/30 | 0,42 | 0,16 | -0,51R | €-23,05 | 1,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 4/30 | 4/30 | 0,56 | 0,56 | -0,37R | €-18,17 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 5/30 | 6/30 | 0,43 | 0,25 | -0,51R | €-27,46 | 1,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 10/30 | 1,75 | 0,37 | 0,41R | €-20,93 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 29/30 | 11/30 | 0,99 | 0,56 | -0,01R | €-20,39 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 7/30 | 0,00 | 0,71 | 0,00R | €-11,49 | 2,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 6/30 | 0,00 | 0,47 | 0,00R | €-25,04 | 2,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 5/30 | 0,00 | 0,51 | 0,00R | €-26,85 | 2,22% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 28/30 | 41/30 | 0,76 | 0,69 | -0,18R | €-5,33 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 29/30 | 8/30 | 0,85 | 0,42 | -0,11R | €-33,56 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 22/30 | 10/30 | 0,83 | 0,44 | -0,14R | €-25,90 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 27/30 | 18/30 | 0,80 | 0,52 | -0,15R | €-23,99 | 4,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 28/30 | 8/30 | 0,76 | 0,42 | -0,18R | €-33,56 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 121/30 | 27/30 | 1,04 | 0,56 | 0,03R | €-13,41 | 5,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 44/30 | 39/30 | 1,63 | 0,96 | 0,37R | €-1,46 | 4,86% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 5/30 | 5/30 | 0,00 | 0,00 | -1,11R | €-55,21 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 5/30 | 5/30 | 0,00 | 0,00 | -1,11R | €-55,21 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 5/30 | 5/30 | 0,00 | 0,00 | -1,11R | €-55,21 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 48/30 | 29/30 | 0,85 | 0,61 | -0,10R | €-9,96 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 2/30 | 4/30 | 0,00 | 0,20 | -1,10R | €-32,49 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 2/30 | 4/30 | 0,00 | 0,05 | -1,10R | €-37,77 | 1,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 4/30 | 5/30 | 5,81 | 0,52 | 1,22R | €-18,91 | 2,86% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 4/30 | 5/30 | 5,81 | 0,52 | 1,22R | €-18,91 | 2,86% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 4/30 | 5/30 | 5,81 | 0,52 | 1,22R | €-18,91 | 2,86% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 67/30 | 26/30 | 1,53 | 1,67 | 0,31R | €15,55 | 2,25% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 12/30 | 4/30 | 1,02 | 0,47 | 0,01R | €-16,77 | 2,38% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 26/30 | 9/30 | 1,11 | 0,98 | 0,07R | €-0,72 | 2,26% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 21/30 | 22/30 | 1,32 | 0,59 | 0,20R | €-12,33 | 2,88% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 21/30 | 8/30 | 1,32 | 1,07 | 0,20R | €2,61 | 2,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 24/30 | 25/30 | 1,06 | 0,50 | 0,04R | €-15,29 | 4,05% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 24/30 | 11/30 | 1,06 | 0,70 | 0,04R | €-13,03 | 3,31% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 29/30 | 16/30 | 1,09 | 0,52 | 0,06R | €-11,62 | 3,95% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 21/30 | 12/30 | 1,13 | 1,33 | 0,10R | €10,07 | 2,33% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 21/30 | 10/30 | 1,13 | 1,26 | 0,10R | €9,42 | 2,33% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 81/30 | 34/30 | 1,41 | 1,85 | 0,24R | €18,58 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 6/30 | 6/30 | 0,85 | 0,29 | -0,11R | €-27,47 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 2/30 | 4/30 | 0,00 | 0,41 | -1,13R | €-24,69 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 5/30 | 5/30 | 1,14 | 0,86 | 0,09R | €-4,58 | 1,67% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,57% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07321**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.3 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64392.6 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07296**; close **0.07293**; wick alta **11.1%**; volume **x0.34**

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

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **81,70%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +1.91%, 64% oltre +1%.
- BTC trend score: **-1,00**; ADX: **22,48**; breadth sopra EMA50: **66,67%**
- Mediana alt vs BTC: **1,91%**; dispersione: **32,09%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **41**
- Posizioni research aperte: **664**
- Trade research chiusi: **2961**
- Eventi di mercato indipendenti chiusi: **778**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **14319**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 5 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 4 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 4 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 5 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 4 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 6 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 6 | 4 | 4 | 25,00% | 0,63 | -0,28R | €-11,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 5 | 3 | 3 | 100,00% | ∞ | 1,95R | €58,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 6 | 4 | 4 | 75,00% | 5,75 | 1,21R | €48,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 2 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 6 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 6 | 4 | 4 | 25,00% | 0,63 | -0,28R | €-11,38 |
| MAIN | 17 | 59 | 59 | 35,59% | 1,06 | 0,04R | €25,21 |
| RSI_EXTREME_LONG_15M | 0 | 10 | 10 | 30,00% | 0,31 | -0,54R | €-54,33 |
| RSI_EXTREME_SHORT_15M | 0 | 10 | 10 | 30,00% | 0,45 | -0,37R | €-37,03 |
| Bilanciata 1H V1 | 17 | 171 | 171 | 34,50% | 1,02 | 0,01R | €17,62 |
| Bilanciata 1H V2 | 7 | 52 | 46 | 42,31% | 1,44 | 0,25R | €130,57 |
| Bilanciata 1H V3 Filtered | 13 | 76 | 76 | 38,16% | 1,18 | 0,12R | €87,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 6 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,68 |
| Rapida 1H V1 | 6 | 202 | 202 | 39,60% | 0,93 | -0,04R | €-80,50 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 15 | 15 | 53,33% | 1,86 | 0,36R | €54,58 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 5 | 6 | 6 | 66,67% | 2,80 | 0,62R | €37,37 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 10 | 68 | 68 | 47,06% | 1,22 | 0,12R | €82,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 11 | 73 | 73 | 42,47% | 1,01 | 0,01R | €5,10 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 8 | 49 | 49 | 51,02% | 1,39 | 0,20R | €99,88 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 66 | 66 | 34,85% | 0,99 | -0,01R | €-5,03 |
| Rapida 1H V2 | 2 | 12 | 11 | 33,33% | 0,63 | -0,27R | €-32,65 |
| Rapida 1H V3 Filtered | 12 | 113 | 113 | 44,25% | 1,10 | 0,06R | €63,54 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 10 | 57 | 57 | 45,61% | 1,12 | 0,07R | €40,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 5 | 28 | 28 | 42,86% | 1,04 | 0,02R | €6,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 5 | 28 | 28 | 42,86% | 1,04 | 0,02R | €6,26 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 6 | 37 | 37 | 40,54% | 0,94 | -0,04R | €-13,11 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 12 | 68 | 68 | 44,12% | 1,06 | 0,03R | €22,69 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 12 | 68 | 68 | 42,65% | 0,99 | -0,01R | €-3,69 |
| SHADOW_4H_WIDE | 26 | 50 | 50 | 28,00% | 1,06 | 0,04R | €21,80 |
| SHADOW_BOLLINGER_MR_1H | 7 | 44 | 44 | 43,18% | 1,01 | 0,00R | €1,50 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 4 | 4 | 0,00% | 0,00 | -1,12R | €-45,00 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 19 | 116 | 116 | 37,93% | 1,14 | 0,09R | €105,21 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 10 | 33 | 33 | 33,33% | 0,94 | -0,04R | €-14,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 19 | 83 | 83 | 36,14% | 1,04 | 0,03R | €23,76 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 18 | 58 | 58 | 32,76% | 0,89 | -0,08R | €-46,92 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 7 | 17 | 17 | 41,18% | 1,32 | 0,20R | €33,30 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 28 | 28 | 17,86% | 0,39 | -0,53R | €-148,84 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 9 | 38 | 38 | 18,42% | 0,62 | -0,33R | €-125,67 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 9 | 38 | 38 | 18,42% | 0,62 | -0,33R | €-125,67 |
| SHADOW_COMBO_MEAN_REVERSION | 3 | 17 | 17 | 41,18% | 0,98 | -0,01R | €-1,74 |
| SHADOW_COMBO_SCANNER | 11 | 69 | 69 | 43,48% | 1,54 | 0,32R | €222,92 |
| SHADOW_COMBO_TREND | 20 | 89 | 89 | 34,83% | 1,12 | 0,08R | €70,46 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | 12 | 52 | 52 | 28,85% | 0,93 | -0,05R | €-26,63 |
| SHADOW_EMA_TREND_1H | 20 | 94 | 94 | 34,04% | 1,11 | 0,07R | €70,34 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 5 | 5 | 20,00% | 0,42 | -0,51R | €-25,56 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 4 | 4 | 25,00% | 0,56 | -0,37R | €-14,86 |
| SHADOW_ETH_EMA_1H | 0 | 5 | 5 | 20,00% | 0,43 | -0,51R | €-25,44 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 0 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 11 | 29 | 29 | 34,48% | 0,99 | -0,01R | €-2,56 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 11 | 28 | 28 | 28,57% | 0,76 | -0,18R | €-50,66 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 9 | 29 | 29 | 31,03% | 0,85 | -0,11R | €-31,62 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 11 | 22 | 22 | 22,73% | 0,83 | -0,14R | €-29,84 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 27 | 27 | 29,63% | 0,80 | -0,15R | €-40,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | 11 | 28 | 28 | 28,57% | 0,76 | -0,18R | €-50,66 |
| Forza relativa 1H V1 | 18 | 121 | 121 | 32,23% | 1,04 | 0,03R | €30,81 |
| Forza relativa 1H V2 | 7 | 48 | 44 | 43,75% | 1,63 | 0,37R | €175,89 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 4 | 5 | 5 | 0,00% | 0,00 | -1,11R | €-55,34 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 4 | 5 | 5 | 0,00% | 0,00 | -1,11R | €-55,34 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 4 | 5 | 5 | 0,00% | 0,00 | -1,11R | €-55,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 48 | 48 | 29,17% | 0,85 | -0,10R | €-45,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | 6 | 4 | 4 | 75,00% | 5,81 | 1,22R | €49,00 |
| SHADOW_SCANNER_TOP15_LONG | 6 | 4 | 4 | 75,00% | 5,81 | 1,22R | €49,00 |
| SHADOW_SCANNER_TOP20_LONG | 6 | 4 | 4 | 75,00% | 5,81 | 1,22R | €49,00 |
| SHADOW_SCANNER_TOP5_BTC | 11 | 67 | 67 | 41,79% | 1,53 | 0,31R | €210,01 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 3 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 10 | 26 | 26 | 34,62% | 1,11 | 0,07R | €19,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 8 | 21 | 21 | 38,10% | 1,32 | 0,20R | €42,02 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 8 | 21 | 21 | 38,10% | 1,32 | 0,20R | €42,02 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 8 | 24 | 24 | 33,33% | 1,06 | 0,04R | €9,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 8 | 24 | 24 | 33,33% | 1,06 | 0,04R | €9,44 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 11 | 29 | 29 | 34,48% | 1,09 | 0,06R | €18,31 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 11 | 21 | 21 | 28,57% | 1,13 | 0,10R | €20,45 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 11 | 21 | 21 | 28,57% | 1,13 | 0,10R | €20,45 |
| SHADOW_SCANNER_TOP5_LONG | 10 | 81 | 81 | 41,98% | 1,41 | 0,24R | €193,21 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,52 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 0 | 5 | 5 | 40,00% | 1,14 | 0,09R | €4,59 |
| SHADOW_SOL_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 2 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 1 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 2 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 2 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 3 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 2 | 3 | 3 | 66,67% | 3,82 | 0,96R | €28,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 2 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| MAIN | ALT_ROTATION_DOWN | 2 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | ALT_ROTATION_UP | 2 | 5 | 5 | 0,00% | 0,00 | -1,02R | €-51,22 |
| MAIN | RANGE | 9 | 23 | 23 | 34,78% | 1,03 | 0,02R | €4,31 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,18 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,31 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,38 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 2 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 7 | 48 | 48 | 39,58% | 1,25 | 0,15R | €72,73 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V1 | TRANSITION | 0 | 30 | 30 | 33,33% | 1,00 | -0,00R | €-0,05 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 6 | 26 | 24 | 34,62% | 1,02 | 0,01R | €2,97 |
| Bilanciata 1H V2 | TRANSITION | 0 | 20 | 17 | 45,00% | 1,69 | 0,36R | €72,49 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 10 | 10 | 40,00% | 1,23 | 0,14R | €14,28 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 3 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 5 | 19 | 19 | 52,63% | 2,02 | 0,52R | €98,63 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,57 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,25 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 2 | 20 | 20 | 25,00% | 0,47 | -0,39R | €-78,83 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 4 | 63 | 63 | 46,03% | 1,24 | 0,13R | €79,86 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,83R | €-41,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 4 | 4 | 100,00% | ∞ | 1,49R | €59,40 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 2 | 2 | 50,00% | 1,41 | 0,21R | €4,28 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,31 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 23,53% | 0,44 | -0,42R | €-70,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 100,00% | ∞ | 1,39R | €27,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 5 | 28 | 28 | 64,29% | 2,38 | 0,53R | €148,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,31 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 18 | 18 | 22,22% | 0,41 | -0,45R | €-80,97 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 1 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 5 | 29 | 29 | 58,62% | 1,88 | 0,39R | €113,36 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,46R | €14,56 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,48R | €44,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 0,75 | -0,17R | €-18,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 2 | 5 | 5 | 60,00% | 1,89 | 0,40R | €19,89 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 4 | 22 | 22 | 68,18% | 2,88 | 0,64R | €140,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 3 | 17 | 17 | 17,65% | 0,42 | -0,47R | €-79,61 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 2 | 6 | 6 | 50,00% | 1,70 | 0,39R | €23,59 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 6 | 23 | 23 | 43,48% | 1,39 | 0,23R | €53,72 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,95R | €19,52 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,95R | €58,62 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 2 | 9 | 8 | 44,44% | 1,01 | 0,01R | €0,69 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 2 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 5 | 28 | 28 | 60,71% | 2,06 | 0,45R | €125,42 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,46R | €14,56 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 7 | 7 | 57,14% | 1,83 | 0,38R | €26,94 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 0,48 | -0,40R | €-59,35 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 5 | 24 | 24 | 66,67% | 2,67 | 0,60R | €143,82 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 13 | 13 | 69,23% | 3,24 | 0,71R | €92,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 13 | 13 | 69,23% | 3,24 | 0,71R | €92,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 3 | 15 | 15 | 66,67% | 2,90 | 0,64R | €96,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,46R | €14,56 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 19 | 19 | 31,58% | 0,61 | -0,28R | €-52,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 5 | 28 | 28 | 60,71% | 2,06 | 0,45R | €125,42 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,46R | €14,56 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 19 | 19 | 31,58% | 0,61 | -0,28R | €-52,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 2 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 5 | 27 | 27 | 59,26% | 1,93 | 0,41R | €110,55 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,46R | €14,56 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 2,79R | €55,73 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 10 | 21 | 21 | 23,81% | 0,85 | -0,12R | €-24,87 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 14 | 14 | 42,86% | 2,03 | 0,61R | €84,85 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 2 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,27 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 5 | 16 | 16 | 37,50% | 0,78 | -0,15R | €-23,76 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
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
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 2 | 6 | 6 | 50,00% | 1,86 | 0,45R | €26,75 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 8 | 35 | 35 | 40,00% | 1,21 | 0,14R | €47,78 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 20 | 20 | 45,00% | 1,65 | 0,34R | €68,99 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 1 | 11 | 11 | 18,18% | 0,41 | -0,52R | €-56,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 3 | 11 | 11 | 54,55% | 2,34 | 0,62R | €68,08 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 2 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 8 | 23 | 23 | 47,83% | 1,68 | 0,38R | €86,26 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 4 | 4 | 50,00% | 1,78 | 0,43R | €17,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 1 | 13 | 13 | 15,38% | 0,33 | -0,61R | €-78,83 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 8 | 23 | 23 | 47,83% | 1,68 | 0,38R | €86,26 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,91 | -0,07R | €-1,99 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 4 | 10 | 10 | 60,00% | 2,88 | 0,77R | €77,46 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 7 | 7 | 28,57% | 0,73 | -0,21R | €-14,77 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 13 | 13 | 23,08% | 0,84 | -0,13R | €-17,29 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 4 | 13 | 13 | 23,08% | 0,84 | -0,13R | €-17,29 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 2 | 9 | 9 | 44,44% | 1,09 | 0,06R | €5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 2 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 3 | 15 | 15 | 53,33% | 2,39 | 0,67R | €100,50 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 15 | 15 | 46,67% | 1,60 | 0,34R | €50,68 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 5 | 7 | 7 | 28,57% | 0,81 | -0,14R | €-9,97 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 2 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 7 | 26 | 26 | 38,46% | 1,28 | 0,18R | €47,83 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 16 | 16 | 43,75% | 1,79 | 0,42R | €67,09 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 20,00% | 0,51 | -0,41R | €-41,36 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 4 | 7 | 7 | 28,57% | 0,92 | -0,06R | €-3,97 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 18 | 18 | 27,78% | 0,89 | -0,09R | €-15,90 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 8 | 8 | 25,00% | 0,67 | -0,26R | €-20,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 2 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 7 | 25 | 25 | 40,00% | 1,47 | 0,28R | €69,11 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 16 | 16 | 43,75% | 1,79 | 0,42R | €67,07 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-9,03 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 14,29% | 0,32 | -0,60R | €-41,93 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 4 | 8 | 8 | 50,00% | 1,95 | 0,48R | €38,48 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,96R | €58,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 4 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 4 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 9 | 9 | 33,33% | 1,47 | 0,31R | €28,35 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 3 | 12 | 12 | 58,33% | 2,73 | 0,73R | €87,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 4 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 4 | 8 | 8 | 12,50% | 0,30 | -0,63R | €-50,74 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 2 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 7 | 35 | 35 | 31,43% | 0,98 | -0,01R | €-4,28 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | TRANSITION | 0 | 16 | 16 | 50,00% | 2,11 | 0,57R | €91,12 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 50,00% | 2,02 | 0,53R | €32,04 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 4 | 10 | 10 | 60,00% | 3,23 | 0,91R | €90,56 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 0 | 13 | 11 | 38,46% | 1,31 | 0,20R | €25,87 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 3 | 5 | 5 | 0,00% | 0,00 | -1,11R | €-55,34 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 3 | 5 | 5 | 0,00% | 0,00 | -1,11R | €-55,34 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 3 | 5 | 5 | 0,00% | 0,00 | -1,11R | €-55,34 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 4 | 19 | 19 | 31,58% | 0,81 | -0,14R | €-26,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 1,97R | €59,18 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 1,97R | €59,18 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 1,97R | €59,18 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 2 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 3 | 15 | 15 | 53,33% | 2,80 | 0,74R | €111,45 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 13 | 13 | 46,15% | 1,79 | 0,45R | €58,04 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 3 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 3 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 3 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 3 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 3 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 3 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 8 | 8 | 37,50% | 1,76 | 0,48R | €38,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 8 | 8 | 37,50% | 1,76 | 0,48R | €38,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 3 | 16 | 16 | 56,25% | 2,87 | 0,72R | €115,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 28 | 28 | 50,00% | 1,84 | 0,45R | €125,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
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
| SHADOW_SOL_EMA_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-26T06:53:50+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **680**
- Scenari virtuali ancora attivi: **11296**
- Gruppi in attesa dell'uscita originale: **347**
- Gruppi con originale chiuso ma Shadow ancora attive: **333**
- Confronti completati: **33271**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 1420 | 1485 | +€6,53 | 49,4% | 477 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 1420 | 1485 | +€4,86 | 47,5% | 496 | 16 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 1420 | 1485 | +€2,11 | 46,5% | 525 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 1404 | 1469 | +€2,83 | 46,5% | 486 | 28 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 1391 | 1456 | +€8,67 | 45,9% | 389 | 28 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 1391 | 1456 | +€6,76 | 45,3% | 374 | 53 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 1391 | 1456 | +€6,18 | 42,4% | 443 | 26 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 1389 | 1454 | +€1,47 | 45,9% | 464 | 51 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 1360 | 1425 | +€5,19 | 44,8% | 310 | 97 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 1355 | 1420 | €-0,67 | 47,1% | 373 | 199 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 1338 | 1403 | +€7,09 | 31,9% | 214 | 149 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 1334 | 1399 | +€4,40 | 42,0% | 262 | 174 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 1309 | 1374 | +€1,33 | 43,7% | 191 | 310 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 1294 | 1359 | +€8,73 | 40,5% | 101 | 220 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 1279 | 1344 | +€0,12 | 36,6% | 171 | 270 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 1268 | 1333 | €-10,84 | 31,2% | 290 | 245 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 1259 | 1324 | €-0,39 | 37,8% | 87 | 382 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 1256 | 1321 | €-3,80 | 31,4% | 152 | 334 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 1244 | 1309 | €-8,43 | 29,1% | 111 | 374 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 1149 | 1214 | €-14,48 | 24,7% | 110 | 357 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-26T06:53:53+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **33271**
- Valutazioni prodotte: **13710**
- Candidature al Blocco 5: **1**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB50_R075 | 162 | 0,158 | 0,262 | 0,030 | 60,5% | 89,7 | ELIGIBLE_FOR_MUTATION |
| GB20_R100 | 204 | 0,272 | 0,251 | 0,160 | 60,3% | 89,6 | ELIGIBLE_FOR_MUTATION |
| TP_R250 | 113 | 0,227 | 0,148 | 0,071 | 58,4% | 87,5 | ROBUST |
| GB50_R100 | 152 | 0,182 | 0,212 | 0,056 | 61,8% | 87,0 | VALIDATING |
| GB20_R075 | 208 | 0,217 | 0,103 | 0,099 | 57,7% | 87,0 | ELIGIBLE_FOR_MUTATION |
| GB20_R050 | 38 | 3,902 | 4,831 | 3,381 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB20_R075 | 38 | 3,902 | 4,831 | 3,408 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB30_R050 | 38 | 3,879 | 4,818 | 3,340 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB30_R075 | 38 | 3,879 | 4,818 | 3,335 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB40_R050 | 38 | 3,769 | 4,678 | 3,263 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB40_R075 | 38 | 3,769 | 4,678 | 3,258 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB50_R050 | 38 | 3,651 | 4,538 | 3,100 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB50_R075 | 38 | 3,651 | 4,538 | 3,108 | 92,1% | 87,0 | EARLY_SIGNAL |
| ATR15_R050 | 38 | 3,266 | 4,115 | 2,800 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB30_R100 | 38 | 3,766 | 4,818 | 3,156 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R075 | 38 | 3,732 | 4,587 | 3,212 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB40_R100 | 38 | 3,654 | 4,678 | 3,048 | 92,1% | 86,9 | EARLY_SIGNAL |
| ATR10_R050 | 38 | 3,653 | 4,641 | 3,141 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R060 | 38 | 3,598 | 4,437 | 3,093 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB50_R100 | 38 | 3,542 | 4,538 | 2,989 | 92,1% | 86,9 | EARLY_SIGNAL |

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

Generato: 2026-07-26T06:54:14+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 20 | 100,00% | 1,28 | +€103,11 | +€5,16 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 20 | 100,00% | 1,11 | +€40,98 | +€2,05 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 5 | 100,00% | 2,52 | +€82,07 | +€16,41 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 5 | 100,00% | 2,18 | +€63,95 | +€12,79 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-26T06:53:38+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **71**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **23.59 R**
- Profitto virtuale mancato: **150.37 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 302 | 9 | 25204.96 |
| DOWN_20 | 302 | 9 | 49150.22 |
| DOWN_30 | 302 | 39 | 75234.33 |
| DOWN_40 | 302 | 147 | 91641.91 |
| UP_10 | 79 | 0 | 12810.73 |
| UP_20 | 79 | 0 | 25621.46 |
| UP_30 | 79 | 6 | 38541.22 |
| UP_40 | 79 | 34 | 45812.08 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-26T06:53:13+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **12**
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
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | SHADOW_1H_FAST_V3 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | SHADOW_1H_FAST_V3_CAP75_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-26T06:54:15+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **12**
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

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-07-26T06:54:15+00:00

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

Generato: 2026-07-26T06:54:15+00:00

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

Generato: 2026-07-26T06:54:15+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **137**
- Hall of Fame: **19**
- Memorie genetiche: **2**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 20.4 | E | 34 | 1.95 | 0.394 | 5.75 |
| 2 | SHADOW_1H_BALANCED_V3 | BASELINE | 17.3 | E | 42 | 1.61 | 0.267 | 3.23 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 16.5 | E | 44 | 1.56 | 0.193 | 3.71 |
| 4 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 16.5 | E | 46 | 1.54 | 0.211 | 5.40 |
| 5 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 16.3 | E | 39 | 1.56 | 0.203 | 3.68 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 14.4 | E | 73 | 1.21 | 0.085 | 5.36 |
| 7 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 13.1 | E | 41 | 1.29 | 0.124 | 3.55 |
| 8 | SHADOW_1H_BALANCED | BASELINE | 11.6 | E | 43 | 1.50 | 0.198 | 4.17 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 10.9 | E | 47 | 1.10 | 0.046 | 4.74 |
| 10 | SHADOW_COMBO_SCANNER | BASELINE | 10.7 | E | 30 | 1.14 | 0.082 | 4.95 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| FAMILY | momentum_breakout_v3_filtered | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |
| GLOBAL | GLOBAL | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-26T06:54:15+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **453**
- Strategie preferite nel regime corrente: **3**
- Strategie da evitare nel regime corrente: **2**
- Memorie contestuali: **218**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | momentum_breakout_v3_filtered | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.416 | 0.00 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | INSUFFICIENT | 81.2 | 7 | 8.05 | 1.092 | 1.09 |
| 3 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 4 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.986 | 0.00 |
| 5 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 6 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 7 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | momentum_breakout_v3_filtered | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.959 | 0.00 |
| 8 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 9 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | INSUFFICIENT | 80.0 | 8 | 3.52 | 0.682 | 2.17 |
| 10 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | OBSERVING | 79.9 | 19 | 2.25 | 0.463 | 2.24 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-26T06:54:15+00:00

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

Generato: 2026-07-26T06:53:38+00:00

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
