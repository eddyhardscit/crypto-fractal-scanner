# Paper trading automatico KuCoin

Generato: 2026-07-24T21:53:58+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-24T21:53:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-24T21:53:25+00:00 | 2026-07-24T21:53:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-24T21:30:00+00:00 | 2026-07-24T21:30:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-24T20:00:00+00:00 | 2026-07-24T20:00:00+00:00 | 53,5 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-24T16:00:00+00:00 | 2026-07-24T16:00:00+00:00 | 1,89 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -8,52 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -6,02 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -5,91 | 6,00 | 0,09 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -5,03 | 6,00 | 0,97 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | RIF | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,35 | 6,00 | 1,65 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,71 | 6,00 | 4,29 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -1,68 | 6,00 | 4,32 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 1,89 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,11 | 6,00 | 5,89 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | DOGE | 240m | SHORT | -8,52 | 5,00 | 0,00 | STALE_CANDLE | 1,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | AKE | 240m | LONG | 8,25 | 5,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | BANK | 240m | LONG | 7,75 | 5,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | BANK | 60m | LONG | 7,00 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H — LONG senza Range High Vol | BANK | 60m | LONG | 7,00 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H — SHORT Trend Down stretto | BANK | 60m | LONG | 7,00 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V2 | BANK | 60m | LONG | 7,00 | 5,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V3 Filtered | BANK | 60m | LONG | 7,00 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.954,00 | -0,46% | €-46,00 | €3.000,00 | -1,53% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 517 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.954,00 | €1.462,87 | €4.388,60 | €148,39 | €8,75 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.685,79 | €1.269,32 | €2.538,64 | €105,45 | €59,56 |
| TEST | Bilanciata 1H V1 | 4 | €10.475,62 | €2.717,92 | €8.153,75 | €50,78 | €144,79 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.437,33 | €1.331,37 | €2.662,75 | €104,27 | €58,17 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.406,48 | €1.671,12 | €5.013,37 | €154,81 | €27,90 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.300,18 | €4.278,69 | €12.836,08 | €205,17 | €20,32 |
| TEST | Combo Adaptive — madre | 3 | €10.264,17 | €2.757,41 | €5.514,81 | €154,10 | €2,32 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.239,56 | €2.359,86 | €4.719,72 | €51,18 | €96,29 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.201,14 | €2.857,87 | €8.573,61 | €203,39 | €21,34 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.196,77 | €1.281,05 | €2.562,10 | €100,06 | €56,83 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.150,27 | €1.280,09 | €2.560,17 | €100,06 | €56,57 |
| TEST | Doge Ema 1H | 1 | €10.148,47 | €1.143,65 | €3.430,94 | €50,74 | €2,29 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.148,42 | €2.843,08 | €8.529,23 | €202,34 | €21,23 |
| TEST | Forza relativa 1H V2 | 3 | €10.148,22 | €1.636,61 | €3.273,22 | €101,33 | €19,25 |
| TEST | Combo Scanner | 3 | €10.120,59 | €2.776,18 | €5.552,36 | €150,33 | €2,29 |
| TEST | Rapida 1H V3 Filtered — madre | 3 | €10.120,20 | €1.348,49 | €4.045,46 | €151,23 | €26,39 |
| TEST | Bilanciata 1H V2 | 4 | €10.109,47 | €2.109,13 | €6.327,39 | €151,03 | €24,11 |
| TEST | Btc Bollinger 1H | 1 | €10.096,18 | €1.402,77 | €4.208,32 | €50,50 | €-1,25 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 3 | €10.063,96 | €1.341,34 | €4.024,03 | €150,49 | €26,24 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.060,89 | €4.030,03 | €8.060,05 | €96,72 | €-4,35 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €10.052,47 | €1.285,16 | €2.570,32 | €98,81 | €56,03 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €10.043,85 | €2.595,88 | €7.787,65 | €199,70 | €48,52 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.043,85 | €2.595,88 | €7.787,65 | €199,70 | €48,52 |
| TEST | Rapida score 6–7,5 — Cost Aware | 4 | €10.043,85 | €2.595,88 | €7.787,65 | €199,70 | €48,52 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 2 | €10.030,41 | €2.268,80 | €6.806,39 | €99,99 | €34,49 |
| TEST | Sol Ema 1H | 1 | €10.028,65 | €1.161,12 | €3.483,35 | €50,16 | €-1,31 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €10.024,09 | €1.300,19 | €2.600,39 | €100,07 | €55,87 |
| TEST | Combo Adaptive — Quality7 | 3 | €10.023,75 | €2.777,85 | €5.555,71 | €149,70 | €0,17 |
| TEST | Ampia 4H | 4 | €10.018,81 | €1.964,72 | €3.929,45 | €149,98 | €36,79 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €10.011,57 | €1.998,65 | €3.997,31 | €47,97 | €20,70 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €10.010,81 | €1.786,04 | €5.358,11 | €98,88 | €51,58 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €10.003,63 | €3.291,34 | €6.582,68 | €149,71 | €6,66 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.998,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.996,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.996,07 | €830,21 | €1.660,43 | €49,74 | €49,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.992,24 | €761,04 | €1.522,08 | €49,74 | €44,92 |
| TEST | Rapida 1H V2 | 3 | €9.989,77 | €3.914,85 | €11.744,55 | €150,58 | €-6,82 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.989,55 | €2.798,22 | €5.596,43 | €149,59 | €2,26 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €9.983,74 | €1.781,90 | €5.345,70 | €98,82 | €51,43 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 3 | €9.982,75 | €2.797,77 | €5.595,53 | €99,81 | €57,94 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.978,73 | €1.299,81 | €3.899,43 | €49,91 | €-1,47 |
| TEST | Combo Trend | 3 | €9.978,41 | €1.973,32 | €3.946,65 | €100,16 | €89,51 |
| TEST | Sol Ema 4H | 1 | €9.977,61 | €862,58 | €1.725,17 | €49,74 | €30,68 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 4 | €9.969,96 | €2.590,77 | €7.772,30 | €198,23 | €48,19 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.964,37 | €1.153,43 | €3.460,30 | €49,83 | €0,78 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 3 | €9.945,14 | €1.773,97 | €5.321,90 | €97,91 | €51,28 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 2 | €9.943,08 | €284,99 | €854,96 | €99,65 | €13,44 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €9.939,86 | €326,95 | €980,86 | €99,63 | €14,01 |
| TEST | Eth Adaptive 1H | 1 | €9.934,41 | €1.146,74 | €3.440,21 | €49,54 | €28,60 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.931,24 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 3 | €9.924,96 | €1.126,74 | €3.380,23 | €149,11 | €13,91 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €9.913,05 | €1.590,83 | €3.181,66 | €148,45 | €-5,91 |
| TEST | Sol Adaptive 1H | 1 | €9.904,22 | €1.144,60 | €3.433,80 | €49,45 | €16,93 |
| TEST | Rapida 1H V1 — madre | 3 | €9.892,04 | €1.316,01 | €3.948,02 | €147,19 | €25,82 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 3 | €9.888,02 | €1.163,95 | €2.327,90 | €97,72 | €55,11 |
| TEST | Global Confluence puro 1H | 1 | €9.866,09 | €1.539,06 | €3.078,12 | €0,00 | €18,01 |
| TEST | Combo Adaptive — Long Only | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.864,46 | €2.757,78 | €5.515,56 | €48,90 | €86,78 |
| TEST | Eth Ema 1H | 1 | €9.861,69 | €1.138,34 | €3.415,02 | €49,18 | €28,39 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.860,04 | €2.764,95 | €5.529,91 | €147,91 | €2,23 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.844,77 | €523,94 | €1.571,81 | €147,13 | €16,95 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.832,02 | €1.240,15 | €2.480,31 | €146,90 | €62,02 |
| TEST | Sol Bollinger 1H | 1 | €9.827,72 | €1.365,75 | €4.097,24 | €49,17 | €-3,21 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.809,53 | €522,06 | €1.566,18 | €146,60 | €16,88 |
| TEST | Master Adaptive V1 | 3 | €9.793,14 | €1.239,48 | €2.478,96 | €146,74 | €66,31 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.793,14 | €1.239,48 | €2.478,96 | €146,74 | €66,31 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.793,14 | €1.239,48 | €2.478,96 | €146,74 | €66,31 |
| TEST | Rapida V3 — Long Only | 0 | €9.769,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.734,98 | €1.277,01 | €2.554,02 | €146,84 | €9,32 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.696,74 | €2.570,57 | €5.141,13 | €148,49 | €-2,03 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.666,60 | €1.252,24 | €2.504,47 | €145,88 | €0,92 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.624,45 | €1.157,97 | €2.315,93 | €145,45 | €9,22 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.573,51 | €1.286,08 | €2.572,16 | €144,79 | €9,17 |

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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.954,00 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.685,79 | €627,89 | 30 | 30 | 53,33% | 2,18 | €20,93 | 2,70% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.475,62 | €336,34 | 37 | 37 | 51,35% | 1,46 | €9,09 | 2,30% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.437,33 | €381,10 | 22 | 22 | 50,00% | 1,96 | €17,32 | 2,01% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.406,48 | €381,29 | 34 | 34 | 47,06% | 1,47 | €11,21 | 2,20% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.300,18 | €287,11 | 33 | 33 | 45,45% | 1,50 | €8,70 | 2,49% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.264,17 | €265,08 | 22 | 22 | 50,00% | 1,78 | €12,05 | 1,31% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.239,56 | €144,73 | 19 | 19 | 47,37% | 1,34 | €7,62 | 2,12% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.201,14 | €184,94 | 28 | 28 | 42,86% | 1,36 | €6,61 | 2,49% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.196,77 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.150,27 | €95,56 | 8 | 8 | 62,50% | 1,59 | €11,95 | 2,33% |
| TEST | Doge Ema 1H | Trend following EMA | €10.148,47 | €148,24 | 7 | 7 | 71,43% | 2,33 | €21,18 | 1,36% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.148,42 | €132,31 | 33 | 33 | 42,42% | 1,19 | €4,01 | 2,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.148,22 | €130,93 | 34 | 33 | 35,29% | 1,13 | €3,85 | 3,69% |
| TEST | Combo Scanner | Combo Scanner | €10.120,59 | €121,92 | 24 | 24 | 45,83% | 1,20 | €5,08 | 2,66% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.120,20 | €96,29 | 62 | 62 | 35,48% | 1,08 | €1,55 | 2,89% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.109,47 | €89,16 | 27 | 25 | 51,85% | 1,16 | €3,30 | 2,75% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.096,18 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.063,96 | €40,19 | 30 | 30 | 36,67% | 1,06 | €1,34 | 2,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.060,89 | €70,07 | 28 | 28 | 42,86% | 1,11 | €2,50 | 2,06% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.052,47 | €-1,60 | 4 | 4 | 50,00% | 0,99 | €-0,40 | 1,64% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.043,85 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.043,85 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.043,85 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.030,41 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,23% |
| TEST | Sol Ema 1H | Trend following EMA | €10.028,65 | €32,05 | 4 | 4 | 50,00% | 1,29 | €8,01 | 1,67% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.024,09 | €-29,80 | 4 | 4 | 50,00% | 0,73 | €-7,45 | 2,20% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.023,75 | €26,91 | 8 | 8 | 62,50% | 1,23 | €3,36 | 1,51% |
| TEST | Ampia 4H | Confluenza trend | €10.018,81 | €-17,59 | 14 | 14 | 21,43% | 0,96 | €-1,26 | 2,94% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.011,57 | €-6,74 | 14 | 14 | 35,71% | 0,98 | €-0,48 | 2,31% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.010,81 | €-37,40 | 34 | 34 | 32,35% | 0,95 | €-1,10 | 2,49% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.003,63 | €1,30 | 19 | 19 | 36,84% | 1,00 | €0,07 | 2,25% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,79 | €-0,21 | 1 | 1 | 0,00% | 0,00 | €-0,21 | 0,01% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.998,95 | €-1,05 | 1 | 1 | 0,00% | 0,00 | €-1,05 | 0,04% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.996,99 | €-3,01 | 1 | 1 | 0,00% | 0,00 | €-3,01 | 0,11% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.996,07 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.992,24 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.989,77 | €3,64 | 9 | 8 | 44,44% | 1,02 | €0,40 | 1,69% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.989,55 | €-9,13 | 10 | 10 | 50,00% | 0,96 | €-0,91 | 1,41% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.983,74 | €-64,33 | 35 | 35 | 34,29% | 0,92 | €-1,84 | 2,96% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.982,75 | €-71,80 | 14 | 14 | 42,86% | 0,82 | €-5,13 | 2,12% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.978,73 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Combo Trend | Combo Trend | €9.978,41 | €-108,68 | 28 | 28 | 28,57% | 0,88 | €-3,88 | 3,58% |
| TEST | Sol Ema 4H | Trend following EMA | €9.977,61 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.969,96 | €-73,56 | 1 | 1 | 0,00% | 0,00 | €-73,56 | 0,98% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Btc Ema 1H | Trend following EMA | €9.964,37 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.945,14 | €-102,79 | 30 | 30 | 26,67% | 0,84 | €-3,43 | 2,58% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.943,08 | €-69,85 | 1 | 1 | 0,00% | 0,00 | €-69,85 | 0,88% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.939,86 | €-73,56 | 1 | 1 | 0,00% | 0,00 | €-73,56 | 0,94% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.934,41 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.931,24 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.924,96 | €-86,92 | 10 | 10 | 20,00% | 0,63 | €-8,69 | 1,92% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.913,05 | €-79,13 | 24 | 24 | 25,00% | 0,82 | €-3,30 | 3,25% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.904,22 | €-110,64 | 5 | 5 | 40,00% | 0,38 | €-22,13 | 2,14% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.892,04 | €-131,36 | 70 | 70 | 32,86% | 0,92 | €-1,88 | 6,76% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.888,02 | €-165,42 | 7 | 7 | 28,57% | 0,41 | €-23,63 | 3,31% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.866,09 | €-150,03 | 8 | 8 | 37,50% | 0,45 | €-18,75 | 2,92% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.864,46 | €-218,20 | 23 | 23 | 34,78% | 0,62 | €-9,49 | 5,48% |
| TEST | Eth Ema 1H | Trend following EMA | €9.861,69 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.860,04 | €-138,49 | 12 | 12 | 41,67% | 0,64 | €-11,54 | 2,24% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.844,77 | €-171,24 | 21 | 21 | 33,33% | 0,72 | €-8,15 | 2,86% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.832,02 | €-227,96 | 7 | 7 | 14,29% | 0,29 | €-32,57 | 2,80% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.827,72 | €-166,62 | 3 | 3 | 0,00% | 0,00 | €-55,54 | 1,89% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.809,53 | €-206,41 | 21 | 21 | 42,86% | 0,68 | €-9,83 | 3,21% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.793,14 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.793,14 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.793,14 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.769,04 | €-230,96 | 24 | 24 | 25,00% | 0,65 | €-9,62 | 3,31% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.734,98 | €-272,77 | 15 | 15 | 33,33% | 0,42 | €-18,18 | 2,88% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.696,74 | €-298,46 | 13 | 13 | 30,77% | 0,22 | €-22,96 | 3,95% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.666,60 | €-332,80 | 32 | 32 | 53,12% | 0,53 | €-10,40 | 4,16% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.624,45 | €-383,47 | 18 | 18 | 27,78% | 0,34 | €-21,30 | 4,05% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.573,51 | €-434,08 | 15 | 15 | 20,00% | 0,40 | €-28,94 | 4,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06901 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €8,75 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06953 | 0,06901 | 0,06939 | 0,09235 | 0,06717 | €1.013,54 | €3.040,62 | €0,00 | €22,57 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16338 | 0,16501 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €64,16 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,26033 | 0,29535 | 0,27587 | 0,17486 | 0,32281 | €143,89 | €431,67 | €0,00 | €58,06 |
| Bilanciata 1H — LONG senza Range High Vol | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,29401 | 0,29535 | 0,26069 | 0,19748 | 0,36064 | €147,07 | €441,21 | €50,00 | €2,01 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00322 | €137,92 | €413,75 | €49,65 | €11,43 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,29967 | 0,29535 | 0,26406 | 0,20128 | 0,37088 | €141,19 | €423,58 | €50,33 | €-6,11 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 494,80102 | 489,21000 | 505,14655 | 657,26069 | 474,10997 | €802,34 | €2.407,01 | €50,33 | €27,20 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.026,91 | €3.080,73 | €50,38 | €3,02 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 494,80102 | 489,21000 | 505,14655 | 657,26069 | 474,10997 | €819,31 | €2.457,92 | €51,39 | €27,77 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,29527 | 0,29535 | 0,26181 | 0,19832 | 0,36219 | €152,72 | €458,16 | €51,92 | €0,13 |
| Rapida 1H V1 — madre | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29535 | 0,26700 | 0,19929 | 0,34127 | €161,18 | €483,53 | €48,41 | €-2,22 |
| Rapida 1H V1 — madre | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 489,21000 | 499,88678 | 653,40929 | 479,92384 | €1.018,17 | €3.054,50 | €49,58 | €16,71 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €136,66 | €409,99 | €49,20 | €11,32 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,09458 | 1,09025 | 1,10684 | 1,45397 | 1,07619 | €1.525,19 | €4.575,56 | €51,25 | €18,10 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64106,00000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.520,13 | €4.560,38 | €51,08 | €-25,45 |
| Rapida V1 — score 6–7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29864 | 0,29535 | 0,27232 | 0,20059 | 0,33812 | €194,53 | €583,58 | €51,44 | €-6,43 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.038,85 | €3.116,56 | €51,41 | €34,09 |
| Rapida score 6–7,5 — senza Trend Up | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,29535 | 0,26810 | 0,19748 | 0,33288 | €189,10 | €567,29 | €50,00 | €2,59 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €50,00 | €33,16 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €1,33 |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €11,44 |
| Rapida score 6–7,5 — Range Only | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,29535 | 0,26810 | 0,19748 | 0,33288 | €189,10 | €567,29 | €50,00 | €2,59 |
| Rapida score 6–7,5 — Range Only | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €50,00 | €33,16 |
| Rapida score 6–7,5 — Range Only | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €1,33 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €11,44 |
| Rapida score 6–7,5 — Cost Aware | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,29535 | 0,26810 | 0,19748 | 0,33288 | €189,10 | €567,29 | €50,00 | €2,59 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €50,00 | €33,16 |
| Rapida score 6–7,5 — Cost Aware | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €1,33 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €11,44 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64106,00000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.499,07 | €4.497,20 | €50,37 | €-25,10 |
| Rapida V1 — no HIGH + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29223 | 0,29535 | 0,26505 | 0,19628 | 0,33299 | €182,11 | €546,32 | €50,81 | €5,84 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.021,31 | €3.063,92 | €50,54 | €33,52 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00263 | 0,00267 | 0,00231 | 0,00176 | 0,00310 | €140,60 | €421,79 | €50,61 | €6,97 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29416 | 0,29535 | 0,27057 | 0,19758 | 0,32954 | €206,02 | €618,07 | €49,56 | €2,50 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €137,66 | €412,97 | €49,56 | €11,41 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29535 | 0,26700 | 0,19929 | 0,34127 | €166,45 | €499,35 | €49,99 | €-2,29 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 489,21000 | 499,88678 | 653,40929 | 479,92384 | €1.035,86 | €3.107,57 | €50,45 | €17,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €139,04 | €417,11 | €50,05 | €11,52 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29535 | 0,26700 | 0,19929 | 0,35612 | €160,59 | €481,78 | €48,23 | €-2,21 |
| Rapida V1 — target pieno 2R | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 74,42911 | 73,72200 | 74,04827 | 98,86667 | 72,76190 | €1.475,37 | €4.426,11 | €0,00 | €42,05 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00322 | €138,00 | €414,01 | €49,68 | €11,43 |
| Rapida 1H V2 | DOGE | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,06865 | 0,06901 | 0,06942 | 0,09119 | 0,06749 | €1.493,88 | €4.481,64 | €50,19 | €-23,75 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 491,90160 | 489,21000 | 499,88678 | 653,40929 | 479,92384 | €1.030,95 | €3.092,84 | €50,21 | €16,92 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29535 | 0,26700 | 0,19929 | 0,34127 | €167,02 | €501,07 | €50,17 | €-2,30 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 491,90160 | 489,21000 | 499,88678 | 653,40929 | 479,92384 | €1.041,65 | €3.124,94 | €50,73 | €17,10 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €139,81 | €419,44 | €50,33 | €11,58 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63750,18741 | 64106,00000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.506,88 | €4.520,63 | €50,63 | €-25,23 |
| Rapida V3 — score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,29535 | 0,26505 | 0,19628 | 0,33299 | €183,05 | €549,16 | €51,07 | €5,87 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.026,61 | €3.079,84 | €50,81 | €33,69 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00263 | 0,00267 | 0,00231 | 0,00176 | 0,00310 | €141,33 | €423,98 | €50,88 | €7,01 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29535 | 0,26700 | 0,19929 | 0,34127 | €162,98 | €488,93 | €48,95 | €-2,24 |
| Rapida V3 — no volatilità HIGH | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,42911 | 73,72200 | 74,04827 | 98,86667 | 73,17870 | €1.480,38 | €4.441,15 | €0,00 | €42,19 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €138,54 | €415,61 | €49,87 | €11,48 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,33512 | 3,07807 | 2,24009 | 3,72069 | €211,65 | €634,94 | €48,94 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,29535 | 0,26505 | 0,19628 | 0,33299 | €175,74 | €527,22 | €49,03 | €5,63 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €136,55 | €409,64 | €49,16 | €11,31 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29535 | 0,26700 | 0,19929 | 0,34127 | €162,73 | €488,20 | €48,88 | €-2,24 |
| Rapida V3 — senza ESPORTS | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,42911 | 73,72200 | 74,04827 | 98,86667 | 73,17870 | €1.484,39 | €4.453,17 | €0,00 | €42,31 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €138,91 | €416,74 | €50,01 | €11,51 |
| Rapida V3 senza ESPORTS — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29401 | 0,29535 | 0,26810 | 0,19748 | 0,33288 | €189,09 | €567,26 | €50,00 | €2,59 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €137,86 | €413,59 | €49,63 | €11,42 |
| Rapida V3 senza ESPORTS — MFE Lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29401 | 0,29535 | 0,26810 | 0,19748 | 0,33288 | €189,09 | €567,26 | €50,00 | €2,59 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.010,24 | €3.030,72 | €50,00 | €33,16 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.257,30 | €3.771,89 | €49,94 | €1,33 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €134,14 | €402,43 | €48,29 | €11,11 |
| Rapida V3 senza ESPORTS — Stress Guard | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 489,21000 | 502,78051 | 657,02164 | 482,38187 | €1.010,32 | €3.030,97 | €50,00 | €33,16 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,47 | €3.775,42 | €49,99 | €1,33 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,33512 | 3,07807 | 2,24009 | 3,72069 | €210,89 | €632,67 | €48,76 | €0,00 |
| Rapida V3 — qualità completa + profit lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,29535 | 0,26505 | 0,19628 | 0,33299 | €175,11 | €525,34 | €48,86 | €5,61 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00267 | 0,00229 | 0,00175 | 0,00307 | €136,06 | €408,18 | €48,98 | €11,27 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06901 | 0,07077 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €60,25 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 489,21000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-42,21 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 57,07700 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €18,75 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,29967 | 0,29535 | 0,26406 | 0,15133 | 0,37800 | €204,97 | €409,93 | €48,71 | €-5,91 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,29683 | 0,29535 | 0,26156 | 0,14990 | 0,37442 | €213,94 | €427,88 | €50,84 | €-2,13 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 493,58126 | 489,21000 | 503,90129 | 737,90399 | 470,87721 | €1.207,34 | €2.414,67 | €50,49 | €21,38 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 489,21000 | 499,33014 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €96,29 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64106,00000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €-1,20 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,77975 | 73,72200 | 72,89440 | 37,25878 | 75,10779 | €2.011,27 | €4.022,55 | €48,27 | €-3,15 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06906 | 0,06901 | 0,07019 | 0,10324 | 0,06656 | €1.523,03 | €3.046,06 | €50,05 | €2,04 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,83123 | 73,72200 | 75,01253 | 110,37769 | 71,23237 | €1.561,26 | €3.122,52 | €49,96 | €4,62 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,32281 | €221,39 | €442,77 | €0,00 | €59,56 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16338 | 0,16501 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €60,35 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 494,80102 | 489,21000 | 505,14655 | 739,72752 | 474,10997 | €1.169,31 | €2.338,62 | €48,90 | €26,43 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,32906 | €216,24 | €432,48 | €0,00 | €58,17 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29535 | 0,26417 | 0,14984 | 0,36831 | €221,07 | €442,14 | €48,50 | €-2,03 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,32906 | €204,86 | €409,72 | €0,00 | €55,11 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,32906 | €207,68 | €415,35 | €0,00 | €55,87 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29535 | 0,26110 | 0,14984 | 0,37504 | €201,10 | €402,19 | €48,26 | €-1,84 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00260 | 0,00267 | 0,00229 | 0,00131 | 0,00328 | €200,25 | €400,50 | €48,06 | €11,06 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,32906 | €208,27 | €416,53 | €0,00 | €56,03 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29535 | 0,26110 | 0,14984 | 0,37504 | €203,41 | €406,81 | €48,82 | €-1,86 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00260 | 0,00267 | 0,00229 | 0,00131 | 0,00328 | €202,55 | €405,10 | €48,61 | €11,19 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,35405 | €210,29 | €420,58 | €0,00 | €56,57 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29535 | 0,27587 | 0,13147 | 0,35405 | €211,25 | €422,51 | €0,00 | €56,83 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06942 | 0,06901 | 0,06942 | 0,10378 | 0,06664 | €1.539,06 | €3.078,12 | €0,00 | €18,01 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,24758 | 0,29535 | 0,26731 | 0,12503 | 0,31294 | €205,58 | €411,17 | €0,00 | €79,34 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06924 | 0,06901 | 0,07034 | 0,10351 | 0,06680 | €1.558,17 | €3.116,34 | €49,86 | €10,18 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64106,00000 | 63010,38428 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €47,97 | €20,70 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06906 | 0,06901 | 0,07008 | 0,10324 | 0,06681 | €1.710,76 | €3.421,51 | €50,60 | €2,29 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06901 | 0,07008 | 0,10324 | 0,06701 | €1.735,03 | €3.470,05 | €51,32 | €2,32 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06901 | 0,07008 | 0,10324 | 0,06701 | €1.690,45 | €3.380,89 | €50,00 | €2,26 |
| Combo Adaptive — Quality7 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,29671 | 0,29535 | 0,26417 | 0,14984 | 0,36180 | €228,26 | €456,51 | €50,07 | €-2,09 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06901 | 0,07008 | 0,10324 | 0,06701 | €1.666,71 | €3.333,43 | €49,30 | €2,23 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26033 | 0,29535 | 0,27790 | 0,13147 | 0,35405 | €206,98 | €413,96 | €0,00 | €55,68 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06901 | 0,07008 | 0,10324 | 0,06599 | €1.688,60 | €3.377,21 | €49,95 | €2,26 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06901 | 0,07008 | 0,10324 | 0,06599 | €1.688,61 | €3.377,21 | €49,95 | €2,26 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64106,00000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €0,78 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64106,00000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €-1,25 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,69426 | 73,72200 | 74,75546 | 97,89054 | 71,57186 | €1.161,12 | €3.483,35 | €50,16 | €-1,31 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 73,72200 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €30,68 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 73,72200 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €49,00 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 73,77975 | 73,72200 | 72,89440 | 49,55540 | 75,10779 | €1.365,75 | €4.097,24 | €49,17 | €-3,21 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 74,08718 | 73,72200 | 75,15403 | 98,41247 | 71,95347 | €1.144,60 | €3.433,80 | €49,45 | €16,93 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 73,72200 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €44,92 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1857,65000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €28,39 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 1856,94854 | 1857,65000 | 1880,71748 | 2466,64664 | 1809,41065 | €1.299,81 | €3.899,43 | €49,91 | €-1,47 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1857,65000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €28,60 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06906 | 0,06901 | 0,07008 | 0,09173 | 0,06701 | €1.143,65 | €3.430,94 | €50,74 | €2,29 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29535 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €66,31 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29535 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €66,31 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29671 | 0,29535 | 0,26110 | 0,14984 | 0,36792 | €199,82 | €399,64 | €47,96 | €-1,83 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00260 | 0,00267 | 0,00229 | 0,00131 | 0,00322 | €199,19 | €398,38 | €47,81 | €11,00 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25627 | 0,29535 | 0,22552 | 0,12942 | 0,31778 | €203,36 | €406,71 | €48,81 | €62,02 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30297 | 0,29535 | 0,26661 | 0,15300 | 0,37568 | €202,48 | €404,95 | €48,59 | €-10,19 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00260 | 0,00267 | 0,00229 | 0,00131 | 0,00322 | €201,13 | €402,25 | €48,27 | €11,11 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29535 | 0,22337 | 0,12818 | 0,34521 | €202,68 | €405,37 | €48,64 | €66,31 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sol Ema 1H | SOL | SHORT | 2026-07-24T21:23:40+00:00 | 73,49070 | €94,71 | 1,91 | TARGET |
| Rapida V3 — senza ESPORTS | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,45 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,42 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida V3 — score <7,5 | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,45 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,46 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida V1 — target pieno 2R | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,45 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida V1 — senza PEPE | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,45 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,41 | -0,07 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V1 — madre | ONDO | LONG | 2026-07-24T21:08:39+00:00 | 0,39900 | €-3,43 | -0,07 | TIME_EXIT_NO_CANDLES |
| Benchmark trend following EMA 1H | PEPE | SHORT | 2026-07-24T19:53:35+00:00 | 0,00000 | €55,63 | 1,12 | STOP |
| Top 5 + BTC — solo MFE | AKE | LONG | 2026-07-24T19:23:38+00:00 | 0,00250 | €-68,23 | -1,40 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — Guard + MFE | AKE | LONG | 2026-07-24T19:23:38+00:00 | 0,00250 | €-67,61 | -1,40 | STOP_STRESS_SLIPPAGE |

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
| MAIN | Principale 4H | 50/30 | 18/30 | 0,91 | 0,91 | -0,07R | €-2,94 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 9/30 | 5/30 | 0,37 | 0,20 | -0,45R | €-4,60 | 0,37% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 156/30 | 37/30 | 1,01 | 1,46 | 0,00R | €9,09 | 2,30% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-69,85 | 0,88% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 33/30 | 25/30 | 1,65 | 1,16 | 0,35R | €3,30 | 2,75% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 62/30 | 34/30 | 1,25 | 1,47 | 0,16R | €11,21 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 187/30 | 70/30 | 0,93 | 0,92 | -0,04R | €-1,88 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 12/30 | 10/30 | 1,41 | 0,63 | 0,21R | €-8,69 | 1,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 49/30 | 33/30 | 1,09 | 1,19 | 0,05R | €4,01 | 2,83% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 54/30 | 30/30 | 0,92 | 1,06 | -0,05R | €1,34 | 2,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 36/30 | 33/30 | 1,33 | 1,50 | 0,18R | €8,70 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 46/30 | 30/30 | 0,71 | 0,84 | -0,22R | €-3,43 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 8/30 | 8/30 | 0,35 | 1,02 | -0,56R | €0,40 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 96/30 | 62/30 | 1,04 | 1,08 | 0,02R | €1,55 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 44/30 | 28/30 | 1,01 | 1,36 | 0,01R | €6,61 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 23/30 | 21/30 | 0,88 | 0,68 | -0,08R | €-9,83 | 3,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 23/30 | 21/30 | 0,88 | 0,72 | -0,08R | €-8,15 | 2,86% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 29/30 | 24/30 | 0,62 | 0,65 | -0,28R | €-9,62 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 51/30 | 35/30 | 0,94 | 0,92 | -0,04R | €-1,84 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-73,56 | 0,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-73,56 | 0,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 52/30 | 34/30 | 0,90 | 0,95 | -0,06R | €-1,10 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 43/30 | 14/30 | 1,05 | 0,96 | 0,04R | €-1,26 | 2,94% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 38/30 | 28/30 | 0,96 | 1,11 | -0,03R | €2,50 | 2,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 3/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 4/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 5/30 | 0,57 | 0,79 | -0,36R | €-6,87 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 103/30 | 22/30 | 1,14 | 1,78 | 0,09R | €12,05 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 27/30 | 5/30 | 0,65 | 0,42 | -0,27R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 70/30 | 27/30 | 1,02 | 0,45 | 0,02R | €-11,76 | 4,11% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 46/30 | 12/30 | 0,79 | 0,64 | -0,15R | €-11,54 | 2,24% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 5/30 | 5/30 | 0,46 | 0,48 | -0,46R | €-16,52 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 5/30 | 5/30 | 0,46 | 0,17 | -0,46R | €-28,67 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 8/30 | 8/30 | 0,63 | 1,23 | -0,29R | €3,36 | 1,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 26/30 | 10/30 | 0,33 | 0,92 | -0,61R | €-2,35 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 30/30 | 14/30 | 0,42 | 0,82 | -0,54R | €-5,13 | 2,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 30/30 | 10/30 | 0,42 | 0,96 | -0,54R | €-0,91 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 16/30 | 14/30 | 0,84 | 0,98 | -0,11R | €-0,48 | 2,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 62/30 | 24/30 | 1,44 | 1,20 | 0,27R | €5,08 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 76/30 | 28/30 | 1,01 | 0,88 | 0,01R | €-3,88 | 3,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 4/30 | 1,67 | 0,98 | 0,38R | €-0,31 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 7/30 | 3,40 | 2,33 | 0,89R | €21,18 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 42/30 | 19/30 | 0,92 | 1,34 | -0,06R | €7,62 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 82/30 | 19/30 | 0,99 | 1,00 | -0,01R | €0,07 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 4/30 | 4/30 | 0,57 | 0,16 | -0,36R | €-23,05 | 1,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 4/30 | 6/30 | 0,57 | 0,25 | -0,36R | €-27,46 | 1,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 8/30 | 3,47 | 0,45 | 0,91R | €-18,75 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 22/30 | 7/30 | 0,55 | 0,29 | -0,36R | €-32,57 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 22/30 | 32/30 | 0,42 | 0,53 | -0,50R | €-10,40 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 22/30 | 5/30 | 0,42 | 0,00 | -0,50R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 16/30 | 5/30 | 0,40 | 0,00 | -0,55R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 22/30 | 15/30 | 0,42 | 0,40 | -0,50R | €-28,94 | 4,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 22/30 | 5/30 | 0,42 | 0,00 | -0,50R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 109/30 | 24/30 | 0,99 | 0,82 | -0,00R | €-3,30 | 3,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 37/30 | 33/30 | 1,55 | 1,13 | 0,33R | €3,85 | 3,69% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 40/30 | 23/30 | 1,00 | 0,62 | -0,00R | €-9,49 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 61/30 | 22/30 | 1,38 | 1,96 | 0,23R | €17,32 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 11/30 | 4/30 | 0,76 | 0,47 | -0,18R | €-16,77 | 2,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 20/30 | 4/30 | 0,70 | 0,73 | -0,24R | €-7,45 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 15/30 | 15/30 | 0,78 | 0,42 | -0,16R | €-18,18 | 2,88% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 15/30 | 4/30 | 0,78 | 0,99 | -0,16R | €-0,40 | 1,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 18/30 | 18/30 | 0,60 | 0,34 | -0,32R | €-21,30 | 4,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 18/30 | 7/30 | 0,60 | 0,41 | -0,32R | €-23,63 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 23/30 | 13/30 | 0,73 | 0,22 | -0,21R | €-22,96 | 3,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 14/30 | 8/30 | 0,46 | 1,59 | -0,49R | €11,95 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 14/30 | 8/30 | 0,46 | 1,87 | -0,49R | €17,72 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 74/30 | 30/30 | 1,30 | 2,18 | 0,18R | €20,93 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 4/30 | 5/30 | 0,57 | 0,38 | -0,36R | €-22,13 | 2,14% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 2/30 | 3/30 | 0,00 | 0,00 | -1,13R | €-55,54 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 3/30 | 4/30 | 0,86 | 1,29 | -0,11R | €8,01 | 1,67% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06901**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.0 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64106 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.06906**; close **0.06898**; wick alta **38.5%**; volume **x0.13**

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

- Regime: **RANGE**
- Famiglia: **RANGE**
- Confidenza: **80,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 25%, ADX 20.4.
- BTC trend score: **1,00**; ADX: **20,43**; breadth sopra EMA50: **25,00%**
- Mediana alt vs BTC: **-0,12%**; dispersione: **6,21%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **521**
- Trade research chiusi: **2395**
- Eventi di mercato indipendenti chiusi: **658**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **10054**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 14 | 50 | 50 | 32,00% | 0,91 | -0,07R | €-32,71 |
| RSI_EXTREME_LONG_15M | 0 | 9 | 9 | 33,33% | 0,37 | -0,45R | €-40,45 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 19 | 156 | 156 | 34,62% | 1,01 | 0,00R | €5,74 |
| Bilanciata 1H V2 | 10 | 37 | 33 | 45,95% | 1,65 | 0,35R | €130,05 |
| Bilanciata 1H V3 Filtered | 14 | 62 | 62 | 40,32% | 1,25 | 0,16R | €96,64 |
| Rapida 1H V1 | 15 | 187 | 187 | 39,57% | 0,93 | -0,04R | €-76,91 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 3 | 12 | 12 | 50,00% | 1,41 | 0,21R | €25,66 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 13 | 49 | 49 | 44,90% | 1,09 | 0,05R | €25,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 14 | 54 | 54 | 40,74% | 0,92 | -0,05R | €-27,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 8 | 36 | 36 | 50,00% | 1,33 | 0,18R | €63,38 |
| SHADOW_1H_FAST_TP2_V1 | 15 | 46 | 46 | 28,26% | 0,71 | -0,22R | €-100,93 |
| Rapida 1H V2 | 3 | 9 | 8 | 22,22% | 0,35 | -0,56R | €-50,04 |
| Rapida 1H V3 Filtered | 11 | 96 | 96 | 42,71% | 1,04 | 0,02R | €20,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 9 | 44 | 44 | 43,18% | 1,01 | 0,01R | €3,79 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 23 | 23 | 39,13% | 0,88 | -0,08R | €-17,50 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 23 | 23 | 39,13% | 0,88 | -0,08R | €-17,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 29 | 29 | 31,03% | 0,62 | -0,28R | €-80,69 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 11 | 51 | 51 | 41,18% | 0,94 | -0,04R | €-19,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 11 | 52 | 52 | 40,38% | 0,90 | -0,06R | €-31,42 |
| SHADOW_4H_WIDE | 22 | 43 | 43 | 27,91% | 1,05 | 0,04R | €17,19 |
| SHADOW_BOLLINGER_MR_1H | 4 | 38 | 38 | 42,11% | 0,96 | -0,03R | €-9,68 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 4 | 4 | 0,00% | 0,00 | -1,12R | €-45,00 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 18 | 103 | 103 | 37,86% | 1,14 | 0,09R | €91,96 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 27 | 27 | 25,93% | 0,65 | -0,27R | €-73,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 18 | 70 | 70 | 35,71% | 1,02 | 0,02R | €10,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 16 | 46 | 46 | 30,43% | 0,79 | -0,15R | €-70,30 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 8 | 8 | 25,00% | 0,63 | -0,29R | €-23,37 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 26 | 26 | 15,38% | 0,33 | -0,61R | €-157,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 17 | 30 | 30 | 13,33% | 0,42 | -0,54R | €-161,39 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 17 | 30 | 30 | 13,33% | 0,42 | -0,54R | €-161,39 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 16 | 16 | 37,50% | 0,84 | -0,11R | €-16,81 |
| SHADOW_COMBO_SCANNER | 8 | 62 | 62 | 41,94% | 1,44 | 0,27R | €167,09 |
| SHADOW_COMBO_TREND | 20 | 76 | 76 | 32,89% | 1,01 | 0,01R | €4,22 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 14 | 42 | 42 | 28,57% | 0,92 | -0,06R | €-26,42 |
| SHADOW_EMA_TREND_1H | 19 | 82 | 82 | 31,71% | 0,99 | -0,01R | €-5,87 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,33 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 22 | 22 | 22,73% | 0,55 | -0,36R | €-80,21 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,28 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 7 | 16 | 16 | 12,50% | 0,40 | -0,55R | €-88,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 4 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,14 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,42 |
| Forza relativa 1H V1 | 16 | 109 | 109 | 31,19% | 0,99 | -0,00R | €-4,27 |
| Forza relativa 1H V2 | 6 | 40 | 37 | 42,50% | 1,55 | 0,33R | €130,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 12 | 40 | 40 | 32,50% | 1,00 | -0,00R | €-0,13 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 61 | 61 | 39,34% | 1,38 | 0,23R | €143,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 11 | 11 | 27,27% | 0,76 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 6 | 20 | 20 | 25,00% | 0,70 | -0,24R | €-47,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 5 | 15 | 15 | 26,67% | 0,78 | -0,16R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 15 | 15 | 26,67% | 0,78 | -0,16R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 18 | 18 | 22,22% | 0,60 | -0,32R | €-57,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 18 | 18 | 22,22% | 0,60 | -0,32R | €-57,32 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 23 | 23 | 26,09% | 0,73 | -0,21R | €-48,45 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 74 | 74 | 40,54% | 1,30 | 0,18R | €135,41 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,30 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 2 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | ALT_ROTATION_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,02R | €-51,22 |
| MAIN | RANGE | 7 | 15 | 15 | 26,67% | 0,70 | -0,23R | €-33,95 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 1 | 7 | 7 | 42,86% | 1,45 | 0,26R | €18,34 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,18 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 7 | 7 | 14,29% | 0,07 | -0,86R | €-59,88 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,27 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 10 | 38 | 38 | 39,47% | 1,25 | 0,15R | €58,33 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 1 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 2 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,61 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 7 | 14 | 12 | 42,86% | 1,55 | 0,30R | €41,34 |
| Bilanciata 1H V2 | TRANSITION | 3 | 17 | 16 | 41,18% | 1,32 | 0,20R | €33,60 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 10 | 10 | 40,00% | 1,23 | 0,14R | €14,28 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 9 | 8 | 8 | 75,00% | 5,73 | 1,20R | €96,05 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,90 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 4 | 18 | 18 | 22,22% | 0,38 | -0,51R | €-91,65 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 10 | 51 | 51 | 49,02% | 1,46 | 0,22R | €111,11 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,02R | €-40,63 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 2 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,73 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 11 | 14 | 14 | 78,57% | 4,91 | 0,89R | €124,41 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 3 | 17 | 17 | 23,53% | 0,41 | -0,47R | €-80,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 10 | 15 | 15 | 66,67% | 2,71 | 0,60R | €89,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 0,75 | -0,17R | €-18,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 7 | 12 | 12 | 83,33% | 7,05 | 1,03R | €123,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 15 | 15 | 13,33% | 0,28 | -0,65R | €-97,70 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 8 | 12 | 12 | 50,00% | 1,83 | 0,44R | €52,33 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 1,98R | €19,82 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 3 | 6 | 5 | 33,33% | 0,62 | -0,28R | €-16,69 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 19 | 19 | 26,32% | 0,47 | -0,41R | €-77,53 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 7 | 16 | 16 | 68,75% | 3,02 | 0,66R | €105,38 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 0,48 | -0,40R | €-59,35 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 8 | 13 | 13 | 76,92% | 4,52 | 0,86R | €111,93 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 3 | 8 | 8 | 75,00% | 4,36 | 0,86R | €68,57 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 3 | 8 | 8 | 75,00% | 4,36 | 0,86R | €68,57 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 10 | 10 | 60,00% | 2,18 | 0,48R | €48,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 18 | 18 | 27,78% | 0,51 | -0,37R | €-66,10 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 7 | 16 | 16 | 68,75% | 3,02 | 0,66R | €105,38 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 18 | 18 | 27,78% | 0,51 | -0,37R | €-66,10 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 7 | 16 | 16 | 68,75% | 3,02 | 0,66R | €105,38 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 3 | 1 | 1 | 100,00% | ∞ | 2,79R | €27,87 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 7 | 16 | 16 | 25,00% | 0,90 | -0,07R | €-11,95 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 13 | 13 | 46,15% | 2,32 | 0,73R | €95,17 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 4 | 13 | 13 | 30,77% | 0,58 | -0,32R | €-41,26 |
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
| SHADOW_COMBO_ADAPTIVE | RANGE | 9 | 26 | 26 | 38,46% | 1,13 | 0,09R | €22,98 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 19 | 19 | 42,11% | 1,46 | 0,26R | €49,12 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 2 | 10 | 10 | 20,00% | 0,46 | -0,47R | €-46,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 2 | 7 | 7 | 42,86% | 1,47 | 0,27R | €19,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 9 | 14 | 14 | 50,00% | 1,83 | 0,44R | €61,45 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 9 | 14 | 14 | 50,00% | 1,83 | 0,44R | €61,45 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,50 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 3 | 5 | 5 | 20,00% | 0,45 | -0,47R | €-23,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 10 | 7 | 7 | 14,29% | 0,45 | -0,50R | €-34,82 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 10 | 7 | 7 | 14,29% | 0,45 | -0,50R | €-34,82 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 1 | 8 | 8 | 37,50% | 0,82 | -0,12R | €-9,97 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 3 | 10 | 10 | 50,00% | 2,10 | 0,56R | €56,36 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 14 | 14 | 42,86% | 1,34 | 0,21R | €28,81 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 6 | 6 | 6 | 16,67% | 0,40 | -0,52R | €-31,35 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 8 | 18 | 18 | 33,33% | 1,03 | 0,02R | €3,54 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 2 | 9 | 9 | 22,22% | 0,58 | -0,35R | €-31,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 6 | 5 | 5 | 20,00% | 0,58 | -0,35R | €-17,35 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 5 | 12 | 12 | 25,00% | 0,76 | -0,19R | €-22,61 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 5 | 7 | 7 | 14,29% | 0,34 | -0,60R | €-41,90 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 7 | 18 | 18 | 33,33% | 1,13 | 0,08R | €14,85 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,60 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 2 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 2 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,57 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 8 | 8 | 50,00% | 1,96 | 0,49R | €38,85 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 2 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 4 | 8 | 8 | 12,50% | 0,30 | -0,63R | €-50,74 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 8 | 26 | 26 | 26,92% | 0,80 | -0,15R | €-37,81 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 1 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 60,00% | 3,13 | 0,86R | €43,16 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 1 | 6 | 6 | 66,67% | 4,31 | 1,12R | €67,19 |
| Forza relativa 1H V2 | TRANSITION | 3 | 10 | 9 | 30,00% | 0,90 | -0,07R | €-7,01 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 9 | 12 | 12 | 41,67% | 1,25 | 0,16R | €18,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 11 | 11 | 45,45% | 2,09 | 0,51R | €56,38 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 12 | 12 | 41,67% | 1,49 | 0,30R | €36,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 6 | 6 | 33,33% | 1,08 | 0,05R | €3,14 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 2 | 6 | 6 | 33,33% | 1,08 | 0,05R | €3,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 2 | 6 | 6 | 33,33% | 1,08 | 0,05R | €3,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 2 | 6 | 6 | 33,33% | 1,08 | 0,05R | €3,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 2 | 6 | 6 | 33,33% | 1,08 | 0,05R | €3,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 2 | 6 | 6 | 33,33% | 1,08 | 0,05R | €3,14 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 12 | 12 | 50,00% | 2,28 | 0,55R | €66,24 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 28 | 28 | 50,00% | 1,84 | 0,45R | €125,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,35 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
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
| SHADOW_SOL_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-24T21:53:44+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **389**
- Scenari virtuali ancora attivi: **3531**
- Gruppi in attesa dell'uscita originale: **195**
- Gruppi con originale chiuso ma Shadow ancora attive: **194**
- Confronti completati: **18115**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 874 | 937 | €-1,08 | 49,5% | 224 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 873 | 936 | +€6,11 | 51,1% | 247 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 873 | 936 | +€3,98 | 50,0% | 252 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 873 | 936 | +€1,69 | 48,7% | 259 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 873 | 936 | +€0,99 | 49,0% | 269 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 867 | 930 | +€0,48 | 47,4% | 251 | 27 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 859 | 922 | +€5,40 | 45,2% | 209 | 23 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 859 | 922 | +€3,58 | 45,2% | 197 | 35 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 859 | 922 | +€3,56 | 43,7% | 223 | 23 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 858 | 921 | €-1,68 | 43,3% | 125 | 201 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 856 | 919 | +€2,26 | 44,9% | 172 | 59 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 848 | 911 | +€1,50 | 42,2% | 133 | 116 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 847 | 910 | €-3,17 | 35,7% | 86 | 193 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 829 | 892 | €-6,99 | 30,2% | 70 | 238 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 828 | 891 | +€3,47 | 34,5% | 104 | 92 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 828 | 891 | €-4,43 | 36,3% | 76 | 233 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 809 | 872 | €-11,45 | 29,0% | 170 | 146 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 801 | 864 | €-11,32 | 27,2% | 65 | 235 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 792 | 855 | +€0,35 | 38,1% | 63 | 146 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 749 | 812 | €-17,83 | 22,4% | 64 | 233 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-24T21:53:45+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **18115**
- Valutazioni prodotte: **5256**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TP_R100 | 217 | 0,281 | 0,358 | 0,169 | 70,5% | 95,0 | ELIGIBLE_FOR_MUTATION |
| GB20_R100 | 217 | 0,293 | 0,386 | 0,174 | 71,0% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB30_R100 | 217 | 0,266 | 0,386 | 0,154 | 72,4% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB20_R050 | 217 | 0,268 | 0,334 | 0,171 | 70,0% | 94,9 | VALIDATING |
| GB40_R100 | 215 | 0,213 | 0,322 | 0,098 | 71,2% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB30_R050 | 217 | 0,215 | 0,286 | 0,110 | 70,0% | 94,9 | VALIDATING |
| GB40_R050 | 217 | 0,159 | 0,241 | 0,056 | 68,2% | 91,0 | VALIDATING |
| GB50_R100 | 212 | 0,158 | 0,322 | 0,048 | 70,8% | 91,0 | VALIDATING |
| GB50_R050 | 215 | 0,155 | 0,233 | 0,059 | 68,4% | 90,9 | VALIDATING |
| TP_R150 | 196 | 0,160 | 0,125 | 0,027 | 56,6% | 90,2 | ELIGIBLE_FOR_MUTATION |
| TP_R050 | 217 | 0,127 | 0,279 | 0,034 | 69,1% | 89,9 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 650 | 0,102 | 0,000 | 0,039 | 46,0% | 70,0 | VALIDATING |
| TP_R150 | 626 | 0,065 | 0,000 | 0,015 | 28,1% | 69,8 | VALIDATING |
| GB20_R100 | 636 | 0,069 | 0,000 | 0,023 | 37,3% | 69,7 | VALIDATING |
| GB30_R050 | 650 | 0,062 | 0,000 | -0,005 | 44,5% | 69,3 | VALIDATING |
| GB30_R100 | 636 | 0,031 | 0,000 | -0,021 | 36,9% | 61,9 | VALIDATING |
| TP_R100 | 636 | 0,036 | 0,000 | -0,018 | 35,1% | 60,2 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TIME_12H | 653 | 0,033 | 0,000 | -0,038 | 43,0% | 55,6 | VALIDATING |

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

Generato: 2026-07-24T21:53:56+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 14 | 100,00% | 1,10 | +€32,14 | +€2,30 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 14 | 100,00% | 0,96 | €-13,01 | €-0,93 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 3 | 100,00% | 1,26 | +€13,93 | +€4,64 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 3 | 100,00% | 1,08 | +€4,49 | +€1,50 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-24T21:53:36+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **37**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-21.28 R**
- Profitto virtuale mancato: **77.89 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 127 | 0 | 12206.99 |
| DOWN_20 | 127 | 0 | 24413.99 |
| DOWN_30 | 127 | 0 | 36620.98 |
| DOWN_40 | 127 | 46 | 46449.79 |
| UP_10 | 68 | 0 | 19013.57 |
| UP_20 | 68 | 0 | 38027.14 |
| UP_30 | 68 | 0 | 57040.71 |
| UP_40 | 68 | 42 | 66914.19 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-24T21:53:13+00:00

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

Generato: 2026-07-24T21:53:57+00:00

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

Generato: 2026-07-24T21:53:57+00:00

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

Generato: 2026-07-24T21:53:57+00:00

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

Generato: 2026-07-24T21:53:57+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **95**
- Hall of Fame: **13**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 20.2 | E | 30 | 2.21 | 0.412 | 5.75 |
| 2 | SHADOW_1H_BALANCED_V3 | BASELINE | 15.5 | E | 34 | 1.48 | 0.228 | 3.23 |
| 3 | SHADOW_1H_BALANCED | BASELINE | 15.5 | E | 37 | 1.48 | 0.184 | 4.17 |
| 4 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.6 | E | 33 | 1.50 | 0.176 | 3.71 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 11.6 | E | 62 | 1.08 | 0.032 | 5.36 |
| 6 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 10.7 | E | 33 | 1.19 | 0.080 | 5.40 |
| 7 | SHADOW_RELATIVE_STRENGTH_V2 | BASELINE | 9.4 | E | 34 | 1.15 | 0.086 | 6.62 |
| 8 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 9.0 | E | 30 | 1.07 | 0.028 | 3.55 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 8.0 | E | 34 | 0.96 | -0.019 | 3.68 |
| 10 | SHADOW_1H_FAST | BASELINE | 7.9 | E | 70 | 0.92 | -0.037 | 13.48 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-24T21:53:57+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **334**
- Strategie preferite nel regime corrente: **1**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **167**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 2 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.186 | 0.00 |
| 3 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 4 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 5 | SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | shadow-scanner-top5-btc-btc-le3-v1 | INSUFFICIENT | 80.3 | 1 | 99.00 | 0.398 | 0.00 |
| 6 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 7 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 79.5 | 20 | 2.19 | 0.325 | 1.10 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 78.2 | 6 | 4.73 | 0.683 | 1.10 |
| 9 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 10 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | INSUFFICIENT | 75.4 | 3 | 2.57 | 0.576 | 1.10 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-24T21:53:57+00:00

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

Generato: 2026-07-24T21:53:36+00:00

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
