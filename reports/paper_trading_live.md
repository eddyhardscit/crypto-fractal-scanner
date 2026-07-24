# Paper trading automatico KuCoin

Generato: 2026-07-24T23:24:02+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-24T23:23:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-24T23:23:25+00:00 | 2026-07-24T23:23:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-24T23:00:00+00:00 | 2026-07-24T23:00:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-24T22:00:00+00:00 | 2026-07-24T22:00:00+00:00 | 23,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-24T16:00:00+00:00 | 2026-07-24T16:00:00+00:00 | 3,39 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -8,52 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -6,02 | 6,00 | 0,00 | STALE_CANDLE | 3,39 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -5,91 | 6,00 | 0,09 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -5,03 | 6,00 | 0,97 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,35 | 6,00 | 1,65 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,71 | 6,00 | 4,29 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -1,68 | 6,00 | 4,32 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 3,39 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,11 | 6,00 | 5,89 | STALE_CANDLE | 3,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 203.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 23,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | AKE | 60m | LONG | 6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | BEAT | 60m | LONG | 6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | BEAT | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.01%. |
| Rapida V1 — score 6–7,5 | BEAT | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.01%. |
| Rapida score 6–7,5 — senza Trend Up | BEAT | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.01%. |
| Rapida score 6–7,5 — Range Only | BEAT | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.01%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.945,16 | -0,55% | €-54,84 | €3.000,00 | -1,83% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 527 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.945,16 | €1.462,87 | €4.388,60 | €148,39 | €-0,09 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.735,93 | €1.312,86 | €2.625,71 | €159,11 | €4,19 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.496,68 | €1.374,15 | €2.748,31 | €156,73 | €4,10 |
| TEST | Bilanciata 1H V1 | 4 | €10.492,86 | €2.588,10 | €7.764,31 | €155,73 | €57,32 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.435,93 | €1.671,12 | €5.013,37 | €51,50 | €57,34 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.330,71 | €4.278,69 | €12.836,08 | €102,32 | €50,39 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.252,40 | €2.857,87 | €8.573,61 | €101,51 | €72,15 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.250,23 | €2.587,51 | €5.175,01 | €102,42 | €107,03 |
| TEST | Combo Adaptive — madre | 3 | €10.244,57 | €2.757,41 | €5.514,81 | €154,10 | €-17,28 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.217,85 | €1.281,05 | €2.562,10 | €100,06 | €77,92 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.200,71 | €1.321,51 | €2.643,02 | €151,05 | €3,98 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.199,41 | €2.843,08 | €8.529,23 | €100,98 | €71,78 |
| TEST | Forza relativa 1H V2 | 4 | €10.191,06 | €1.845,37 | €3.690,73 | €151,43 | €62,34 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.138,20 | €2.402,92 | €7.208,76 | €100,98 | €46,29 |
| TEST | Bilanciata 1H V2 | 4 | €10.129,10 | €2.109,13 | €6.327,39 | €100,71 | €43,73 |
| TEST | Doge Ema 1H | 1 | €10.129,10 | €1.143,65 | €3.430,94 | €50,74 | €-17,08 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €10.109,63 | €1.326,36 | €2.652,73 | €149,34 | €3,94 |
| TEST | Combo Scanner | 3 | €10.101,26 | €2.776,18 | €5.552,36 | €150,33 | €-17,03 |
| TEST | Btc Bollinger 1H | 1 | €10.097,93 | €1.402,77 | €4.208,32 | €50,50 | €0,92 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €10.087,66 | €2.595,88 | €7.787,65 | €99,70 | €92,33 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.087,66 | €2.595,88 | €7.787,65 | €99,70 | €92,33 |
| TEST | Rapida score 6–7,5 — Cost Aware | 4 | €10.087,66 | €2.595,88 | €7.787,65 | €99,70 | €92,33 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.081,91 | €2.389,92 | €7.169,76 | €100,42 | €46,07 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €10.081,08 | €1.341,28 | €2.682,56 | €150,45 | €3,93 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.070,64 | €4.030,03 | €8.060,05 | €96,72 | €5,75 |
| TEST | Combo Mean Reversion | 2 | €10.038,93 | €3.457,67 | €6.915,35 | €98,03 | €50,22 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 3 | €10.024,64 | €2.777,85 | €5.555,71 | €99,62 | €1,06 |
| TEST | Sol Ema 1H | 1 | €10.021,70 | €1.161,12 | €3.483,35 | €50,16 | €-8,26 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 4 | €10.013,89 | €2.651,42 | €7.954,26 | €198,31 | €24,24 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2 | €10.013,08 | €920,72 | €2.762,16 | €99,56 | €28,25 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €10.007,83 | €2.828,77 | €8.486,32 | €100,10 | €50,48 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 3 | €10.005,86 | €2.837,64 | €5.675,27 | €149,81 | €-12,91 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €10.004,79 | €1.964,72 | €3.929,45 | €149,98 | €22,77 |
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
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 3 | €9.999,67 | €3.312,86 | €9.938,59 | €100,14 | €5,63 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.998,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.996,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €9.992,90 | €1.989,63 | €3.979,25 | €150,09 | €-3,87 |
| TEST | Sol Donchian 4H | 1 | €9.992,86 | €830,21 | €1.660,43 | €49,74 | €45,79 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.989,29 | €761,04 | €1.522,08 | €49,74 | €41,97 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €9.981,79 | €326,95 | €980,86 | €49,63 | €55,94 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €9.980,86 | €2.821,82 | €8.465,46 | €99,83 | €50,42 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.980,21 | €3.291,34 | €6.582,68 | €149,71 | €-16,76 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 3 | €9.978,65 | €504,12 | €1.512,37 | €99,55 | €49,41 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 3 | €9.976,52 | €2.631,95 | €7.895,85 | €100,03 | €33,69 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.974,23 | €862,58 | €1.725,17 | €49,74 | €27,31 |
| TEST | Eth Donchian 1H | 1 | €9.972,75 | €1.299,81 | €3.899,43 | €49,91 | €-7,48 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.970,47 | €2.798,22 | €5.596,43 | €149,59 | €-16,81 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.962,59 | €1.153,43 | €3.460,30 | €49,83 | €-1,01 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 3 | €9.944,25 | €1.204,48 | €2.408,96 | €147,42 | €3,88 |
| TEST | Rapida V1 — target pieno 2R | 4 | €9.942,04 | €2.809,86 | €8.429,59 | €99,44 | €50,04 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.931,24 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €9.930,82 | €1.590,83 | €3.181,66 | €148,45 | €11,86 |
| TEST | Eth Adaptive 1H | 1 | €9.929,16 | €1.146,74 | €3.440,21 | €49,54 | €23,35 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Rapida 1H V1 — madre | 4 | €9.909,37 | €2.346,66 | €7.039,99 | €98,71 | €45,00 |
| TEST | Sol Adaptive 1H | 1 | €9.897,41 | €1.144,60 | €3.433,80 | €49,45 | €10,11 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.870,76 | €1.280,37 | €2.560,75 | €147,44 | €3,85 |
| TEST | Combo Adaptive — Long Only | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.863,04 | €2.757,78 | €5.515,56 | €0,00 | €85,37 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.862,20 | €523,94 | €1.571,81 | €98,09 | €34,38 |
| TEST | Eth Ema 1H | 1 | €9.856,47 | €1.138,34 | €3.415,02 | €49,18 | €23,18 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.845,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.841,22 | €2.764,95 | €5.529,91 | €147,91 | €-16,60 |
| TEST | Sol Bollinger 1H | 1 | €9.835,94 | €1.365,75 | €4.097,24 | €49,17 | €4,96 |
| TEST | Master Adaptive V1 | 3 | €9.827,26 | €1.279,30 | €2.558,60 | €147,22 | €3,83 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.827,26 | €1.279,30 | €2.558,60 | €147,22 | €3,83 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.826,91 | €522,06 | €1.566,18 | €97,74 | €34,26 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.824,83 | €1.279,24 | €2.558,48 | €147,21 | €3,83 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.769,31 | €1.277,01 | €2.554,02 | €98,02 | €43,66 |
| TEST | Rapida V3 — Long Only | 0 | €9.769,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 2 | €9.710,53 | €2.349,50 | €4.698,99 | €100,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.694,13 | €1.289,74 | €2.579,49 | €145,92 | €3,78 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.658,39 | €1.157,97 | €2.315,93 | €97,18 | €43,16 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.607,25 | €1.286,08 | €2.572,16 | €144,79 | €42,91 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.945,16 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.735,93 | €733,40 | 31 | 31 | 54,84% | 2,38 | €23,66 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.496,68 | €494,53 | 23 | 23 | 52,17% | 2,25 | €21,50 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.492,86 | €440,97 | 39 | 39 | 53,85% | 1,61 | €11,31 | 2,30% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.435,93 | €381,29 | 34 | 34 | 47,06% | 1,47 | €11,21 | 2,20% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.330,71 | €287,11 | 33 | 33 | 45,45% | 1,50 | €8,70 | 2,49% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.252,40 | €184,94 | 28 | 28 | 42,86% | 1,36 | €6,61 | 2,49% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.250,23 | €144,73 | 19 | 19 | 47,37% | 1,34 | €7,62 | 2,12% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.244,57 | €265,08 | 22 | 22 | 50,00% | 1,78 | €12,05 | 1,31% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.217,85 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.200,71 | €198,60 | 9 | 9 | 66,67% | 2,22 | €22,07 | 2,33% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.199,41 | €132,31 | 33 | 33 | 42,42% | 1,19 | €4,01 | 2,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.191,06 | €130,93 | 34 | 33 | 35,29% | 1,13 | €3,85 | 3,69% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.138,20 | €96,29 | 62 | 62 | 35,48% | 1,08 | €1,55 | 2,89% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.129,10 | €89,16 | 27 | 25 | 51,85% | 1,16 | €3,30 | 2,75% |
| TEST | Doge Ema 1H | Trend following EMA | €10.129,10 | €148,24 | 7 | 7 | 71,43% | 2,33 | €21,18 | 1,36% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.109,63 | €107,65 | 5 | 5 | 60,00% | 1,91 | €21,53 | 1,64% |
| TEST | Combo Scanner | Combo Scanner | €10.101,26 | €121,92 | 24 | 24 | 45,83% | 1,20 | €5,08 | 2,66% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.097,93 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.087,66 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.087,66 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.087,66 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.081,91 | €40,19 | 30 | 30 | 36,67% | 1,06 | €1,34 | 2,10% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.081,08 | €79,14 | 5 | 5 | 60,00% | 1,73 | €15,83 | 2,20% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.070,64 | €70,07 | 28 | 28 | 42,86% | 1,11 | €2,50 | 2,06% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.038,93 | €-6,74 | 14 | 14 | 35,71% | 0,98 | €-0,48 | 2,31% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.024,64 | €26,91 | 8 | 8 | 62,50% | 1,23 | €3,36 | 1,51% |
| TEST | Sol Ema 1H | Trend following EMA | €10.021,70 | €32,05 | 4 | 4 | 50,00% | 1,29 | €8,01 | 1,67% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.013,89 | €-5,57 | 3 | 3 | 66,67% | 0,92 | €-1,86 | 0,98% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.013,08 | €-13,51 | 11 | 11 | 27,27% | 0,94 | €-1,23 | 1,92% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.007,83 | €-37,40 | 34 | 34 | 32,35% | 0,95 | €-1,10 | 2,49% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.005,86 | €22,17 | 15 | 15 | 46,67% | 1,06 | €1,48 | 2,12% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Ampia 4H | Confluenza trend | €10.004,79 | €-17,59 | 14 | 14 | 21,43% | 0,96 | €-1,26 | 2,94% |
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
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.999,67 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,53% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.998,95 | €-1,05 | 1 | 1 | 0,00% | 0,00 | €-1,05 | 0,04% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.996,99 | €-3,01 | 1 | 1 | 0,00% | 0,00 | €-3,01 | 0,11% |
| TEST | Combo Trend | Combo Trend | €9.992,90 | €-0,85 | 29 | 29 | 31,03% | 1,00 | €-0,03 | 3,58% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.992,86 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.989,29 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.981,79 | €-73,56 | 1 | 1 | 0,00% | 0,00 | €-73,56 | 0,94% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.980,86 | €-64,33 | 35 | 35 | 34,29% | 0,92 | €-1,84 | 2,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.980,21 | €1,30 | 19 | 19 | 36,84% | 1,00 | €0,07 | 2,25% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.978,65 | €-69,85 | 1 | 1 | 0,00% | 0,00 | €-69,85 | 0,88% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.976,52 | €-52,42 | 10 | 9 | 40,00% | 0,79 | €-5,24 | 1,69% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Sol Ema 4H | Trend following EMA | €9.974,23 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.972,75 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.970,47 | €-9,13 | 10 | 10 | 50,00% | 0,96 | €-0,91 | 1,41% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Btc Ema 1H | Trend following EMA | €9.962,59 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.944,25 | €-57,95 | 8 | 8 | 37,50% | 0,79 | €-7,24 | 3,31% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.942,04 | €-102,79 | 30 | 30 | 26,67% | 0,84 | €-3,43 | 2,58% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.931,24 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.930,82 | €-79,13 | 24 | 24 | 25,00% | 0,82 | €-3,30 | 3,25% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.929,16 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.909,37 | €-131,36 | 70 | 70 | 32,86% | 0,92 | €-1,88 | 6,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.897,41 | €-110,64 | 5 | 5 | 40,00% | 0,38 | €-22,13 | 2,14% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.870,76 | €-131,10 | 8 | 8 | 25,00% | 0,59 | €-16,39 | 2,80% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.863,04 | €-218,20 | 23 | 23 | 34,78% | 0,62 | €-9,49 | 5,48% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.862,20 | €-171,24 | 21 | 21 | 33,33% | 0,72 | €-8,15 | 2,86% |
| TEST | Eth Ema 1H | Trend following EMA | €9.856,47 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.845,62 | €-154,38 | 9 | 9 | 33,33% | 0,44 | €-17,15 | 2,92% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.841,22 | €-138,49 | 12 | 12 | 41,67% | 0,64 | €-11,54 | 2,24% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.835,94 | €-166,62 | 3 | 3 | 0,00% | 0,00 | €-55,54 | 1,89% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.827,26 | €-174,58 | 6 | 6 | 16,67% | 0,36 | €-29,10 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.827,26 | €-174,58 | 6 | 6 | 16,67% | 0,36 | €-29,10 | 3,19% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.826,91 | €-206,41 | 21 | 21 | 42,86% | 0,68 | €-9,83 | 3,21% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.824,83 | €-177,01 | 6 | 6 | 16,67% | 0,35 | €-29,50 | 3,19% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.769,31 | €-272,77 | 15 | 15 | 33,33% | 0,42 | €-18,18 | 2,88% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.769,04 | €-230,96 | 24 | 24 | 25,00% | 0,65 | €-9,62 | 3,31% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.710,53 | €-286,96 | 14 | 14 | 35,71% | 0,25 | €-20,50 | 3,95% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.694,13 | €-308,11 | 34 | 34 | 55,88% | 0,57 | €-9,06 | 4,16% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.658,39 | €-383,47 | 18 | 18 | 27,78% | 0,34 | €-21,30 | 4,05% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.607,25 | €-434,08 | 15 | 15 | 20,00% | 0,40 | €-28,94 | 4,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06940 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €-0,09 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16400 | 0,16501 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €53,26 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,30592 | 0,30834 | 0,27494 | 0,20548 | 0,36789 | €172,71 | €518,13 | €52,47 | €4,10 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 487,33251 | 487,34000 | 497,30283 | 647,34002 | 467,39189 | €854,91 | €2.564,72 | €52,47 | €-0,04 |
| Bilanciata 1H — LONG senza Range High Vol | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,29401 | 0,30834 | 0,29401 | 0,19748 | 0,36064 | €147,07 | €441,21 | €0,00 | €21,51 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00322 | €137,92 | €413,75 | €49,65 | €28,30 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,21779 | 3,21586 | 2,97356 | 2,16128 | 3,70625 | €219,14 | €657,41 | €49,90 | €-0,39 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,29967 | 0,30834 | 0,26406 | 0,20128 | 0,37088 | €141,19 | €423,58 | €50,33 | €12,26 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 494,80102 | 487,34000 | 492,41965 | 657,26069 | 474,10997 | €802,34 | €2.407,01 | €0,00 | €36,29 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.026,91 | €3.080,73 | €50,38 | €-4,82 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 494,80102 | 487,34000 | 492,41965 | 657,26069 | 474,10997 | €819,31 | €2.457,92 | €0,00 | €37,06 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,29527 | 0,30834 | 0,29527 | 0,19832 | 0,36219 | €152,72 | €458,16 | €0,00 | €20,28 |
| Rapida 1H V1 — madre | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,30834 | 0,29671 | 0,19929 | 0,34127 | €161,18 | €483,53 | €0,00 | €18,95 |
| Rapida 1H V1 — madre | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 487,34000 | 491,28201 | 653,40929 | 479,92384 | €1.018,17 | €3.054,50 | €0,00 | €28,33 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €136,66 | €409,99 | €49,20 | €28,04 |
| Rapida 1H V1 — madre | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,47347 | €1.030,66 | €3.091,97 | €49,51 | €-30,32 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,09458 | 1,09138 | 1,10684 | 1,45397 | 1,07619 | €1.525,19 | €4.575,56 | €51,25 | €13,38 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64139,13000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.520,13 | €4.560,38 | €51,08 | €-27,82 |
| Rapida V1 — score 6–7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29864 | 0,30834 | 0,29864 | 0,20059 | 0,33812 | €194,53 | €583,58 | €0,00 | €18,96 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.038,85 | €3.116,56 | €0,00 | €45,88 |
| Rapida score 6–7,5 — senza Trend Up | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,30834 | 0,29401 | 0,19748 | 0,33288 | €189,10 | €567,29 | €0,00 | €27,65 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €0,00 | €44,62 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €-8,27 |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €28,34 |
| Rapida score 6–7,5 — Range Only | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,30834 | 0,29401 | 0,19748 | 0,33288 | €189,10 | €567,29 | €0,00 | €27,65 |
| Rapida score 6–7,5 — Range Only | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €0,00 | €44,62 |
| Rapida score 6–7,5 — Range Only | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €-8,27 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €28,34 |
| Rapida score 6–7,5 — Cost Aware | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,30834 | 0,29401 | 0,19748 | 0,33288 | €189,10 | €567,29 | €0,00 | €27,65 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €0,00 | €44,62 |
| Rapida score 6–7,5 — Cost Aware | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €-8,27 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €28,34 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64139,13000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.499,07 | €4.497,20 | €50,37 | €-27,44 |
| Rapida V1 — no HIGH + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29223 | 0,30834 | 0,29223 | 0,19628 | 0,33299 | €182,11 | €546,32 | €0,00 | €30,12 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.021,31 | €3.063,92 | €0,00 | €45,10 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00263 | 0,00278 | 0,00231 | 0,00176 | 0,00310 | €140,60 | €421,79 | €50,61 | €23,99 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €137,66 | €412,97 | €49,56 | €28,25 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,30834 | 0,29671 | 0,19929 | 0,34127 | €166,45 | €499,35 | €0,00 | €19,57 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 487,34000 | 491,28201 | 653,40929 | 479,92384 | €1.035,86 | €3.107,57 | €0,00 | €28,82 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €139,04 | €417,11 | €50,05 | €28,53 |
| Rapida V1 — senza PEPE | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,47347 | €1.048,58 | €3.145,73 | €50,37 | €-30,85 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,30834 | 0,29671 | 0,19929 | 0,35612 | €160,59 | €481,78 | €0,00 | €18,89 |
| Rapida V1 — target pieno 2R | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 74,42911 | 73,86900 | 74,04827 | 98,86667 | 72,76190 | €1.475,37 | €4.426,11 | €0,00 | €33,31 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00322 | €138,00 | €414,01 | €49,68 | €28,32 |
| Rapida V1 — target pieno 2R | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,01842 | €1.035,89 | €3.107,68 | €49,76 | €-30,47 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 491,90160 | 487,34000 | 491,28201 | 653,40929 | 479,92384 | €1.030,95 | €3.092,84 | €0,00 | €28,68 |
| Rapida 1H V2 | BANK | LONG | Momentum / breakout V2 | 60m | 3,0x | 0,30592 | 0,30834 | 0,28182 | 0,20548 | 0,34207 | €210,98 | €632,95 | €49,86 | €5,00 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,30834 | 0,29671 | 0,19929 | 0,34127 | €167,02 | €501,07 | €0,00 | €19,64 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 491,90160 | 487,34000 | 491,28201 | 653,40929 | 479,92384 | €1.041,65 | €3.124,94 | €0,00 | €28,98 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €139,81 | €419,44 | €50,33 | €28,69 |
| Rapida 1H V3 Filtered — madre | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,47347 | €1.054,44 | €3.163,31 | €50,65 | €-31,02 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63750,18741 | 64139,13000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.506,88 | €4.520,63 | €50,63 | €-27,58 |
| Rapida V3 — score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,30834 | 0,29223 | 0,19628 | 0,33299 | €183,05 | €549,16 | €0,00 | €30,28 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.026,61 | €3.079,84 | €0,00 | €45,34 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00263 | 0,00278 | 0,00231 | 0,00176 | 0,00310 | €141,33 | €423,98 | €50,88 | €24,12 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,30834 | 0,29671 | 0,19929 | 0,34127 | €162,98 | €488,93 | €0,00 | €19,17 |
| Rapida V3 — no volatilità HIGH | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,42911 | 73,86900 | 74,04827 | 98,86667 | 73,17870 | €1.480,38 | €4.441,15 | €0,00 | €33,42 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €138,54 | €415,61 | €49,87 | €28,43 |
| Rapida V3 — no volatilità HIGH | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,47347 | €1.039,92 | €3.119,76 | €49,95 | €-30,59 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,21586 | 3,07807 | 2,24009 | 3,72069 | €211,65 | €634,94 | €48,94 | €-22,70 |
| Rapida V3 — Long + no HIGH + score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,30834 | 0,29223 | 0,19628 | 0,33299 | €175,74 | €527,22 | €0,00 | €29,07 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €136,55 | €409,64 | €49,16 | €28,02 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,30834 | 0,29671 | 0,19929 | 0,34127 | €162,73 | €488,20 | €0,00 | €19,14 |
| Rapida V3 — senza ESPORTS | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,42911 | 73,86900 | 74,04827 | 98,86667 | 73,17870 | €1.484,39 | €4.453,17 | €0,00 | €33,51 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €138,91 | €416,74 | €50,01 | €28,51 |
| Rapida V3 — senza ESPORTS | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,47347 | €1.042,74 | €3.128,21 | €50,09 | €-30,68 |
| Rapida V3 senza ESPORTS — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29401 | 0,30834 | 0,29401 | 0,19748 | 0,33288 | €189,09 | €567,26 | €0,00 | €27,65 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €137,86 | €413,59 | €49,63 | €28,29 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.257,30 | €3.771,89 | €49,94 | €-8,26 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €134,14 | €402,43 | €48,29 | €27,53 |
| Rapida V3 senza ESPORTS — MFE Lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30592 | 0,30834 | 0,28182 | 0,20548 | 0,34207 | €211,77 | €635,30 | €50,04 | €5,02 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 487,33251 | 487,34000 | 495,08720 | 647,34002 | 475,70048 | €1.048,22 | €3.144,65 | €50,04 | €-0,05 |
| Rapida V3 senza ESPORTS — Stress Guard | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 487,34000 | 491,39128 | 657,02164 | 482,38187 | €1.010,32 | €3.030,97 | €0,00 | €44,62 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,47 | €3.775,42 | €49,99 | €-8,27 |
| Rapida V3 senza ESPORTS — Stress Guard | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,83863 | 57,39600 | 57,74874 | 75,50065 | 55,47347 | €1.044,07 | €3.132,20 | €50,15 | €-30,71 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,21586 | 3,07807 | 2,24009 | 3,72069 | €210,89 | €632,67 | €48,76 | €-22,62 |
| Rapida V3 — qualità completa + profit lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,30834 | 0,29902 | 0,19628 | 0,33299 | €175,11 | €525,34 | €0,00 | €28,96 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00278 | 0,00229 | 0,00175 | 0,00307 | €136,06 | €408,18 | €48,98 | €27,92 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06940 | 0,07077 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €53,25 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 487,34000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-44,59 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 57,39600 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €14,11 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,29967 | 0,30834 | 0,26406 | 0,15133 | 0,37800 | €204,97 | €409,93 | €48,71 | €11,86 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,29683 | 0,30834 | 0,26156 | 0,14990 | 0,37442 | €213,94 | €427,88 | €50,84 | €16,59 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 493,58126 | 487,34000 | 503,90129 | 737,90399 | 470,87721 | €1.207,34 | €2.414,67 | €50,49 | €30,53 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00268 | 0,00278 | 0,00236 | 0,00135 | 0,00339 | €208,76 | €417,52 | €50,10 | €15,22 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 487,34000 | 494,56354 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €103,43 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,30592 | 0,30834 | 0,27150 | 0,15449 | 0,39198 | €227,65 | €455,29 | €51,23 | €3,60 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64139,13000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €0,89 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,77975 | 73,86900 | 72,89440 | 37,25878 | 75,10779 | €2.011,27 | €4.022,55 | €48,27 | €4,87 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06906 | 0,06940 | 0,07019 | 0,10324 | 0,06656 | €1.523,03 | €3.046,06 | €50,05 | €-15,17 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,83123 | 73,86900 | 75,01253 | 110,37769 | 71,23237 | €1.561,26 | €3.122,52 | €49,96 | €-1,60 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,36789 | €264,92 | €529,85 | €53,66 | €4,19 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16400 | 0,16501 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €50,10 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 494,80102 | 487,34000 | 492,41965 | 739,72752 | 474,10997 | €1.169,31 | €2.338,62 | €0,00 | €35,26 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,37408 | €259,02 | €518,04 | €52,46 | €4,10 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,37408 | €245,39 | €490,78 | €49,70 | €3,88 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,37408 | €248,77 | €497,53 | €50,39 | €3,93 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,30834 | 0,29671 | 0,14984 | 0,37504 | €201,10 | €402,19 | €0,00 | €15,77 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00260 | 0,00278 | 0,00229 | 0,00131 | 0,00328 | €200,25 | €400,50 | €48,06 | €27,39 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,37408 | €249,47 | €498,94 | €50,53 | €3,94 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,30834 | 0,29671 | 0,14984 | 0,37504 | €203,41 | €406,81 | €0,00 | €15,95 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00260 | 0,00278 | 0,00229 | 0,00131 | 0,00328 | €202,55 | €405,10 | €48,61 | €27,71 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,39887 | €251,72 | €503,43 | €50,99 | €3,98 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,30834 | 0,28125 | 0,13147 | 0,35405 | €211,25 | €422,51 | €0,00 | €77,92 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06924 | 0,06940 | 0,07034 | 0,10351 | 0,06680 | €1.558,17 | €3.116,34 | €49,86 | €-7,37 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,30592 | 0,30834 | 0,27150 | 0,15449 | 0,38166 | €221,89 | €443,78 | €49,94 | €3,51 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64139,13000 | 63010,38428 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €47,97 | €22,78 |
| Combo Mean Reversion | HYPE | LONG | Combo Mean Reversion | 60m | 2,0x | 56,86137 | 57,39600 | 55,88587 | 28,71499 | 58,42218 | €1.459,02 | €2.918,04 | €50,06 | €27,44 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06906 | 0,06940 | 0,07008 | 0,10324 | 0,06681 | €1.710,76 | €3.421,51 | €50,60 | €-17,03 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06940 | 0,07008 | 0,10324 | 0,06701 | €1.735,03 | €3.470,05 | €51,32 | €-17,28 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06940 | 0,07008 | 0,10324 | 0,06701 | €1.690,45 | €3.380,89 | €50,00 | €-16,83 |
| Combo Adaptive — Quality7 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,29671 | 0,30834 | 0,29671 | 0,14984 | 0,36180 | €228,26 | €456,51 | €0,00 | €17,89 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06940 | 0,07008 | 0,10324 | 0,06701 | €1.666,71 | €3.333,43 | €49,30 | €-16,60 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06940 | 0,07008 | 0,10324 | 0,06599 | €1.688,60 | €3.377,21 | €49,95 | €-16,81 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,39887 | €246,85 | €493,70 | €50,00 | €3,90 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06940 | 0,07008 | 0,10324 | 0,06599 | €1.688,61 | €3.377,21 | €49,95 | €-16,81 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64139,13000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €-1,01 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64139,13000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €0,92 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,69426 | 73,86900 | 74,75546 | 97,89054 | 71,57186 | €1.161,12 | €3.483,35 | €50,16 | €-8,26 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 73,86900 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €27,31 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 73,86900 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €45,79 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 73,77975 | 73,86900 | 72,89440 | 49,55540 | 75,10779 | €1.365,75 | €4.097,24 | €49,17 | €4,96 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 74,08718 | 73,86900 | 75,15403 | 98,41247 | 71,95347 | €1.144,60 | €3.433,80 | €49,45 | €10,11 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 73,86900 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €41,97 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1860,51000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €23,18 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 1856,94854 | 1860,51000 | 1880,71748 | 2466,64664 | 1809,41065 | €1.299,81 | €3.899,43 | €49,91 | €-7,48 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1860,51000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €23,35 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06906 | 0,06940 | 0,07008 | 0,09173 | 0,06701 | €1.143,65 | €3.430,94 | €50,74 | €-17,08 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,36789 | €242,50 | €485,00 | €49,12 | €3,83 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,36789 | €242,50 | €485,00 | €49,12 | €3,83 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29671 | 0,30834 | 0,26110 | 0,14984 | 0,36792 | €199,82 | €399,64 | €47,96 | €15,67 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00260 | 0,00278 | 0,00229 | 0,00131 | 0,00322 | €199,19 | €398,38 | €47,81 | €27,25 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,36789 | €243,58 | €487,15 | €49,34 | €3,85 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,36789 | €239,22 | €478,44 | €48,45 | €3,78 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,30834 | 0,27494 | 0,15449 | 0,39887 | €242,44 | €484,88 | €49,11 | €3,83 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Top 5 + BTC — solo MFE | BANK | LONG | 2026-07-24T23:23:35+00:00 | 0,30478 | €11,50 | 0,24 | STOP |
| Global Confluence puro 1H | DOGE | SHORT | 2026-07-24T23:08:35+00:00 | 0,06943 | €-4,35 | -0,09 | STOP |
| Rapida 1H V2 | DOGE | SHORT | 2026-07-24T23:08:35+00:00 | 0,06943 | €-56,06 | -1,12 | STOP |
| Bilanciata 1H V1 | DOGE | SHORT | 2026-07-24T23:08:35+00:00 | 0,06941 | €1,76 | 0,03 | STOP |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | 2026-07-24T22:53:38+00:00 | 0,31096 | €103,04 | 2,04 | STOP_GAP_STRESS |
| Master Adaptive Runner25 V1 | BANK | LONG | 2026-07-24T22:53:38+00:00 | 0,30860 | €93,98 | 1,93 | STOP |
| Master Adaptive Gb20 V1 | AKE | LONG | 2026-07-24T22:53:38+00:00 | 0,00270 | €14,52 | 0,30 | STOP_GAP_STRESS |
| Master Adaptive Gb20 V1 | BANK | LONG | 2026-07-24T22:53:38+00:00 | 0,31096 | €10,17 | 0,21 | STOP_GAP_STRESS |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BANK | LONG | 2026-07-24T22:53:38+00:00 | 0,31096 | €93,97 | 1,89 | STOP_GAP_STRESS |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | 2026-07-24T22:53:38+00:00 | 488,16003 | €35,98 | 0,72 | STOP |
| Rapida V3 senza ESPORTS — MFE Lock | BANK | LONG | 2026-07-24T22:53:38+00:00 | 0,31096 | €32,01 | 0,64 | STOP_GAP_STRESS |
| Scanner Top 5 Long 1H | BANK | LONG | 2026-07-24T22:38:38+00:00 | 0,32275 | €105,52 | 1,99 | TARGET |

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
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 157/30 | 39/30 | 1,00 | 1,61 | -0,00R | €11,31 | 2,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-69,85 | 0,88% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 34/30 | 25/30 | 1,74 | 1,16 | 0,39R | €3,30 | 2,75% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 62/30 | 34/30 | 1,25 | 1,47 | 0,16R | €11,21 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 191/30 | 70/30 | 0,94 | 0,92 | -0,04R | €-1,88 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 13/30 | 11/30 | 1,65 | 0,94 | 0,31R | €-1,23 | 1,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 52/30 | 33/30 | 1,15 | 1,19 | 0,08R | €4,01 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 58/30 | 30/30 | 0,94 | 1,06 | -0,04R | €1,34 | 2,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 37/30 | 33/30 | 1,40 | 1,50 | 0,21R | €8,70 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 49/30 | 30/30 | 0,80 | 0,84 | -0,15R | €-3,43 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 9/30 | 9/30 | 0,31 | 0,79 | -0,61R | €-5,24 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 98/30 | 62/30 | 1,04 | 1,08 | 0,02R | €1,55 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 45/30 | 28/30 | 1,07 | 1,36 | 0,04R | €6,61 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 23/30 | 21/30 | 0,88 | 0,68 | -0,08R | €-9,83 | 3,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 23/30 | 21/30 | 0,88 | 0,72 | -0,08R | €-8,15 | 2,86% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 29/30 | 24/30 | 0,62 | 0,65 | -0,28R | €-9,62 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 53/30 | 35/30 | 0,95 | 0,92 | -0,03R | €-1,84 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-73,56 | 0,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 3/30 | 0,00 | 0,92 | 0,00R | €-1,86 | 0,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,53% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 54/30 | 34/30 | 0,92 | 0,95 | -0,05R | €-1,10 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
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
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 105/30 | 22/30 | 1,15 | 1,78 | 0,10R | €12,05 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 27/30 | 5/30 | 0,65 | 0,42 | -0,27R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 72/30 | 27/30 | 1,04 | 0,45 | 0,03R | €-11,76 | 4,11% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 48/30 | 12/30 | 0,82 | 0,64 | -0,13R | €-11,54 | 2,24% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 5/30 | 5/30 | 0,46 | 0,48 | -0,46R | €-16,52 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 5/30 | 5/30 | 0,46 | 0,17 | -0,46R | €-28,67 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 9/30 | 8/30 | 0,94 | 1,23 | -0,04R | €3,36 | 1,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 26/30 | 10/30 | 0,33 | 0,92 | -0,61R | €-2,35 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 32/30 | 15/30 | 0,51 | 1,06 | -0,44R | €1,48 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 32/30 | 10/30 | 0,51 | 0,96 | -0,44R | €-0,91 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 16/30 | 14/30 | 0,84 | 0,98 | -0,11R | €-0,48 | 2,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 62/30 | 24/30 | 1,44 | 1,20 | 0,27R | €5,08 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 78/30 | 29/30 | 1,03 | 1,00 | 0,02R | €-0,03 | 3,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 4/30 | 1,67 | 0,98 | 0,38R | €-0,31 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 7/30 | 3,40 | 2,33 | 0,89R | €21,18 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 43/30 | 19/30 | 0,89 | 1,34 | -0,09R | €7,62 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 83/30 | 19/30 | 1,03 | 1,00 | 0,02R | €0,07 | 2,25% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 4/30 | 4/30 | 0,57 | 0,16 | -0,36R | €-23,05 | 1,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 4/30 | 6/30 | 0,57 | 0,25 | -0,36R | €-27,46 | 1,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 9/30 | 3,47 | 0,44 | 0,91R | €-17,15 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 22/30 | 8/30 | 0,55 | 0,59 | -0,36R | €-16,39 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 22/30 | 34/30 | 0,42 | 0,57 | -0,50R | €-9,06 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 22/30 | 6/30 | 0,42 | 0,36 | -0,50R | €-29,10 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 17/30 | 6/30 | 0,60 | 0,35 | -0,35R | €-29,50 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 22/30 | 15/30 | 0,42 | 0,40 | -0,50R | €-28,94 | 4,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 22/30 | 6/30 | 0,42 | 0,36 | -0,50R | €-29,10 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 110/30 | 24/30 | 0,98 | 0,82 | -0,01R | €-3,30 | 3,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 38/30 | 33/30 | 1,64 | 1,13 | 0,37R | €3,85 | 3,69% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 41/30 | 23/30 | 0,96 | 0,62 | -0,03R | €-9,49 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 61/30 | 23/30 | 1,38 | 2,25 | 0,23R | €21,50 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 11/30 | 4/30 | 0,76 | 0,47 | -0,18R | €-16,77 | 2,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 20/30 | 5/30 | 0,70 | 1,73 | -0,24R | €15,83 | 2,20% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 15/30 | 15/30 | 0,78 | 0,42 | -0,16R | €-18,18 | 2,88% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 15/30 | 5/30 | 0,78 | 1,91 | -0,16R | €21,53 | 1,64% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 18/30 | 18/30 | 0,60 | 0,34 | -0,32R | €-21,30 | 4,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 18/30 | 8/30 | 0,60 | 0,79 | -0,32R | €-7,24 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 23/30 | 14/30 | 0,73 | 0,25 | -0,21R | €-20,50 | 3,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 15/30 | 9/30 | 0,70 | 2,22 | -0,26R | €22,07 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 15/30 | 8/30 | 0,70 | 1,87 | -0,26R | €17,72 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 74/30 | 31/30 | 1,30 | 2,38 | 0,18R | €23,66 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
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
- Prezzo DOGE: **0.0694**
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
| BTC sotto filtro | 64139.13 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.06952**; close **0.06936**; wick alta **17.6%**; volume **x0.57**

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
- Mediana alt vs BTC: **0,31%**; dispersione: **7,10%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **513**
- Trade research chiusi: **2444**
- Eventi di mercato indipendenti chiusi: **668**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **10305**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 14 | 50 | 50 | 32,00% | 0,91 | -0,07R | €-32,71 |
| RSI_EXTREME_LONG_15M | 0 | 9 | 9 | 33,33% | 0,37 | -0,45R | €-40,45 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 18 | 157 | 157 | 34,39% | 1,00 | -0,00R | €-4,40 |
| Bilanciata 1H V2 | 10 | 38 | 34 | 47,37% | 1,74 | 0,39R | €149,20 |
| Bilanciata 1H V3 Filtered | 15 | 62 | 62 | 40,32% | 1,25 | 0,16R | €96,64 |
| Rapida 1H V1 | 13 | 191 | 191 | 39,79% | 0,94 | -0,04R | €-70,46 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 13 | 13 | 53,85% | 1,65 | 0,31R | €40,46 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 11 | 52 | 52 | 46,15% | 1,15 | 0,08R | €43,62 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 12 | 58 | 58 | 41,38% | 0,94 | -0,04R | €-20,62 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 8 | 37 | 37 | 51,35% | 1,40 | 0,21R | €77,39 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 49 | 49 | 30,61% | 0,80 | -0,15R | €-73,10 |
| Rapida 1H V2 | 3 | 10 | 9 | 20,00% | 0,31 | -0,61R | €-61,47 |
| Rapida 1H V3 Filtered | 11 | 98 | 98 | 42,86% | 1,04 | 0,02R | €23,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 9 | 45 | 45 | 44,44% | 1,07 | 0,04R | €17,79 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 23 | 23 | 39,13% | 0,88 | -0,08R | €-17,50 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 23 | 23 | 39,13% | 0,88 | -0,08R | €-17,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 29 | 29 | 31,03% | 0,62 | -0,28R | €-80,69 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 11 | 53 | 53 | 41,51% | 0,95 | -0,03R | €-17,32 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 11 | 54 | 54 | 40,74% | 0,92 | -0,05R | €-28,84 |
| SHADOW_4H_WIDE | 22 | 43 | 43 | 27,91% | 1,05 | 0,04R | €17,19 |
| SHADOW_BOLLINGER_MR_1H | 5 | 38 | 38 | 42,11% | 0,96 | -0,03R | €-9,68 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 4 | 4 | 0,00% | 0,00 | -1,12R | €-45,00 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 18 | 105 | 105 | 38,10% | 1,15 | 0,10R | €100,72 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 27 | 27 | 25,93% | 0,65 | -0,27R | €-73,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 18 | 72 | 72 | 36,11% | 1,04 | 0,03R | €19,27 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 16 | 48 | 48 | 31,25% | 0,82 | -0,13R | €-61,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 9 | 9 | 33,33% | 0,94 | -0,04R | €-3,50 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 26 | 26 | 15,38% | 0,33 | -0,61R | €-157,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 15 | 32 | 32 | 15,62% | 0,51 | -0,44R | €-141,66 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 15 | 32 | 32 | 15,62% | 0,51 | -0,44R | €-141,66 |
| SHADOW_COMBO_MEAN_REVERSION | 3 | 16 | 16 | 37,50% | 0,84 | -0,11R | €-16,81 |
| SHADOW_COMBO_SCANNER | 8 | 62 | 62 | 41,94% | 1,44 | 0,27R | €167,09 |
| SHADOW_COMBO_TREND | 19 | 78 | 78 | 33,33% | 1,03 | 0,02R | €15,46 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 14 | 43 | 43 | 27,91% | 0,89 | -0,09R | €-36,55 |
| SHADOW_EMA_TREND_1H | 19 | 83 | 83 | 32,53% | 1,03 | 0,02R | €15,51 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,33 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 7 | 22 | 22 | 22,73% | 0,55 | -0,36R | €-80,21 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 7 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,28 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 7 | 17 | 17 | 17,65% | 0,60 | -0,35R | €-58,71 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 4 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,14 |
| SHADOW_MASTER_ADAPTIVE_V1 | 7 | 22 | 22 | 18,18% | 0,42 | -0,50R | €-109,42 |
| Forza relativa 1H V1 | 16 | 110 | 110 | 30,91% | 0,98 | -0,01R | €-14,41 |
| Forza relativa 1H V2 | 6 | 41 | 38 | 43,90% | 1,64 | 0,37R | €151,89 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 11 | 41 | 41 | 31,71% | 0,96 | -0,03R | €-10,26 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 61 | 61 | 39,34% | 1,38 | 0,23R | €143,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 11 | 11 | 27,27% | 0,76 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 6 | 20 | 20 | 25,00% | 0,70 | -0,24R | €-47,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 5 | 15 | 15 | 26,67% | 0,78 | -0,16R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 15 | 15 | 26,67% | 0,78 | -0,16R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 18 | 18 | 22,22% | 0,60 | -0,32R | €-57,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 18 | 18 | 22,22% | 0,60 | -0,32R | €-57,32 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 23 | 23 | 26,09% | 0,73 | -0,21R | €-48,45 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 15 | 15 | 20,00% | 0,70 | -0,26R | €-38,29 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 15 | 15 | 20,00% | 0,70 | -0,26R | €-38,29 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 74 | 74 | 40,54% | 1,30 | 0,18R | €135,41 |
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
| Bilanciata 1H V1 | RANGE | 9 | 39 | 39 | 38,46% | 1,20 | 0,12R | €48,20 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 1 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 2 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,61 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 8 | 14 | 12 | 42,86% | 1,55 | 0,30R | €41,34 |
| Bilanciata 1H V2 | TRANSITION | 2 | 18 | 17 | 44,44% | 1,51 | 0,29R | €52,75 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 10 | 10 | 40,00% | 1,23 | 0,14R | €14,28 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 10 | 8 | 8 | 75,00% | 5,73 | 1,20R | €96,05 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,90 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 4 | 18 | 18 | 22,22% | 0,38 | -0,51R | €-91,65 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 8 | 55 | 55 | 49,09% | 1,44 | 0,21R | €117,56 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,02R | €-40,63 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 1 | 3 | 3 | 100,00% | ∞ | 1,48R | €44,53 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 9 | 17 | 17 | 76,47% | 4,39 | 0,84R | €142,29 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 3 | 17 | 17 | 23,53% | 0,41 | -0,47R | €-80,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 8 | 19 | 19 | 63,16% | 2,30 | 0,50R | €95,87 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 0,75 | -0,17R | €-18,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 7 | 13 | 13 | 84,62% | 7,74 | 1,06R | €137,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 15 | 15 | 13,33% | 0,28 | -0,65R | €-97,70 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 8 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,78 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 3 | 7 | 6 | 28,57% | 0,49 | -0,40R | €-28,12 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 19 | 19 | 26,32% | 0,47 | -0,41R | €-77,53 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 7 | 18 | 18 | 66,67% | 2,70 | 0,60R | €107,96 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 0,48 | -0,40R | €-59,35 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 8 | 14 | 14 | 78,57% | 4,96 | 0,90R | €125,93 |
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
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 7 | 18 | 18 | 66,67% | 2,70 | 0,60R | €107,96 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 18 | 18 | 27,78% | 0,51 | -0,37R | €-66,10 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 7 | 18 | 18 | 66,67% | 2,70 | 0,60R | €107,96 |
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
| SHADOW_BOLLINGER_MR_1H | RANGE | 5 | 13 | 13 | 30,77% | 0,58 | -0,32R | €-41,26 |
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
| SHADOW_COMBO_ADAPTIVE | RANGE | 9 | 28 | 28 | 39,29% | 1,18 | 0,11R | €31,73 |
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
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 9 | 16 | 16 | 50,00% | 1,84 | 0,44R | €70,20 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 9 | 16 | 16 | 50,00% | 1,84 | 0,44R | €70,20 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 4 | 4 | 50,00% | 1,95 | 0,48R | €19,37 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 3 | 5 | 5 | 20,00% | 0,45 | -0,47R | €-23,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 8 | 9 | 9 | 22,22% | 0,80 | -0,17R | €-15,08 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 8 | 9 | 9 | 22,22% | 0,80 | -0,17R | €-15,08 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 2 | 8 | 8 | 37,50% | 0,82 | -0,12R | €-9,97 |
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
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 5 | 7 | 7 | 28,57% | 0,81 | -0,14R | €-9,97 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 8 | 19 | 19 | 31,58% | 0,95 | -0,03R | €-6,59 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 2 | 9 | 9 | 22,22% | 0,58 | -0,35R | €-31,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 6 | 5 | 5 | 20,00% | 0,58 | -0,35R | €-17,35 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 5 | 13 | 13 | 23,08% | 0,69 | -0,25R | €-32,74 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 8 | 8 | 25,00% | 0,67 | -0,26R | €-20,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 8 | 18 | 18 | 33,33% | 1,13 | 0,08R | €14,85 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,60 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 5 | 5 | 20,00% | 0,74 | -0,21R | €-10,71 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 8 | 8 | 50,00% | 1,96 | 0,49R | €38,85 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 4 | 8 | 8 | 12,50% | 0,30 | -0,63R | €-50,74 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 8 | 27 | 27 | 25,93% | 0,76 | -0,18R | €-47,94 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 1 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 60,00% | 3,13 | 0,86R | €43,16 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 2 | 6 | 6 | 66,67% | 4,31 | 1,12R | €67,19 |
| Forza relativa 1H V2 | TRANSITION | 2 | 11 | 10 | 36,36% | 1,19 | 0,13R | €14,14 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 8 | 13 | 13 | 38,46% | 1,10 | 0,07R | €8,68 |
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
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 12 | 12 | 50,00% | 2,28 | 0,55R | €66,24 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
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

Generato: 2026-07-24T23:23:43+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **391**
- Scenari virtuali ancora attivi: **3544**
- Gruppi in attesa dell'uscita originale: **203**
- Gruppi con originale chiuso ma Shadow ancora attive: **188**
- Confronti completati: **18503**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 895 | 958 | +€5,15 | 50,6% | 262 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 895 | 958 | +€2,97 | 49,6% | 267 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 895 | 958 | +€0,66 | 48,2% | 274 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 895 | 958 | €-0,02 | 48,5% | 285 | 0 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 893 | 956 | €-2,06 | 48,8% | 238 | 121 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 888 | 951 | €-0,62 | 47,0% | 266 | 27 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 879 | 942 | +€4,62 | 44,8% | 223 | 23 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 879 | 942 | +€2,89 | 43,3% | 237 | 23 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 879 | 942 | +€2,76 | 44,8% | 211 | 35 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 876 | 939 | +€1,46 | 44,4% | 186 | 59 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 874 | 937 | €-2,29 | 42,8% | 138 | 201 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 867 | 930 | +€0,66 | 41,7% | 147 | 116 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 854 | 917 | €-3,47 | 35,7% | 90 | 193 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 848 | 911 | +€3,34 | 34,2% | 117 | 92 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 847 | 910 | €-7,39 | 30,3% | 75 | 243 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 837 | 900 | €-4,76 | 36,1% | 80 | 235 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 830 | 893 | +€2,43 | 39,4% | 69 | 146 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 825 | 888 | €-12,71 | 28,6% | 184 | 146 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 819 | 882 | €-11,67 | 26,6% | 70 | 240 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 767 | 830 | €-18,06 | 21,9% | 69 | 238 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-24T23:23:46+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **18503**
- Valutazioni prodotte: **5321**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TP_R100 | 232 | 0,227 | 0,322 | 0,112 | 67,7% | 95,0 | ELIGIBLE_FOR_MUTATION |
| GB30_R100 | 232 | 0,205 | 0,322 | 0,090 | 69,4% | 94,8 | ELIGIBLE_FOR_MUTATION |
| GB20_R100 | 232 | 0,236 | 0,322 | 0,121 | 68,1% | 91,2 | VALIDATING |
| GB20_R050 | 234 | 0,205 | 0,294 | 0,105 | 67,5% | 91,2 | VALIDATING |
| GB40_R100 | 230 | 0,152 | 0,281 | 0,044 | 67,8% | 91,2 | VALIDATING |
| GB30_R050 | 234 | 0,150 | 0,262 | 0,048 | 67,5% | 91,2 | VALIDATING |
| GB50_R100 | 226 | 0,099 | 0,286 | -0,007 | 67,7% | 90,0 | VALIDATING |
| GB40_R050 | 234 | 0,093 | 0,219 | -0,010 | 65,4% | 89,5 | VALIDATING |
| GB50_R050 | 231 | 0,082 | 0,171 | -0,017 | 65,8% | 88,3 | VALIDATING |
| TP_R050 | 234 | 0,061 | 0,264 | -0,034 | 66,2% | 85,0 | VALIDATING |
| TP_R150 | 210 | 0,141 | 0,078 | 0,009 | 54,3% | 84,0 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 655 | 0,092 | 0,000 | 0,031 | 45,8% | 70,0 | VALIDATING |
| TP_R150 | 632 | 0,065 | 0,000 | 0,013 | 28,2% | 69,8 | VALIDATING |
| GB20_R100 | 641 | 0,063 | 0,000 | 0,014 | 37,1% | 69,7 | VALIDATING |
| GB30_R050 | 655 | 0,052 | 0,000 | -0,014 | 44,3% | 67,9 | VALIDATING |
| TP_R200 | 202 | 0,054 | 0,104 | -0,113 | 55,9% | 66,8 | VALIDATING |
| TP_R200 | 622 | 0,051 | 0,000 | -0,014 | 35,2% | 63,8 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TP_R100 | 641 | 0,031 | 0,000 | -0,022 | 34,9% | 58,0 | VALIDATING |

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

Generato: 2026-07-24T23:24:00+00:00

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

Generato: 2026-07-24T23:23:35+00:00

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
| DOWN_10 | 130 | 0 | 12703.79 |
| DOWN_20 | 130 | 0 | 25407.58 |
| DOWN_30 | 130 | 0 | 38111.37 |
| DOWN_40 | 130 | 47 | 48425.68 |
| UP_10 | 73 | 0 | 20410.28 |
| UP_20 | 73 | 0 | 40820.56 |
| UP_30 | 73 | 0 | 61230.85 |
| UP_40 | 73 | 48 | 71364.69 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-24T23:23:12+00:00

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

Generato: 2026-07-24T23:24:00+00:00

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

Generato: 2026-07-24T23:24:00+00:00

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

Generato: 2026-07-24T23:24:00+00:00

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

Generato: 2026-07-24T23:24:01+00:00

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
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 21.1 | E | 31 | 2.40 | 0.463 | 5.75 |
| 2 | SHADOW_1H_BALANCED | BASELINE | 17.3 | E | 39 | 1.62 | 0.226 | 4.17 |
| 3 | SHADOW_1H_BALANCED_V3 | BASELINE | 15.5 | E | 34 | 1.48 | 0.228 | 3.23 |
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

Generato: 2026-07-24T23:24:01+00:00

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
| 1 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.519 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 3 | SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | shadow-scanner-top5-btc-btc-le3-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.292 | 0.00 |
| 4 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 5 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 6 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 7 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 79.5 | 20 | 2.19 | 0.325 | 1.10 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 78.2 | 6 | 4.73 | 0.683 | 1.10 |
| 9 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 77.1 | 23 | 2.19 | 0.441 | 4.17 |
| 10 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-24T23:24:01+00:00

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

Generato: 2026-07-24T23:23:35+00:00

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
