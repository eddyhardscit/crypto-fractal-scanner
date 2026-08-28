# Paper trading automatico KuCoin

Generato: 2026-08-28T12:14:42+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-28T12:05:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-28T12:05:32+00:00 | 2026-08-28T12:05:32+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-28T11:45:00+00:00 | 2026-08-28T11:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-28T11:00:00+00:00 | 2026-08-28T11:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-28T08:00:00+00:00 | 2026-08-28T08:00:00+00:00 | 5,7 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bilanciata V3 · LONG only | TRUMP | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | TRUMP | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC 2–3 | TRUMP | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | TRUMP | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | TRUMP | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ENA | 240m | LONG | 8,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | SOL | 240m | LONG | 6,75 | 6,00 | 0,00 | READY | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | ETH | 240m | LONG | 6,09 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 6,04 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | RISK_GATE | 5,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | HYPE | 240m | LONG | 7,29 | 6,00 | 0,00 | RISK_GATE | 5,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | BELOW_SCORE | 5,7 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +4.75; soglia ±6.00; mancano 1.25 punti. |
| Ampia 4H | ENA | 240m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| MAIN — Side × Regime Guard | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | SOL | 240m | LONG | 6,75 | 5,00 | 0,00 | READY | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Sol Ema 4H | SOL | 240m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Adaptive 4H | SOL | 240m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| MAIN — Side × Regime Guard | SOL | 240m | LONG | 6,75 | 6,00 | 0,00 | READY | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | ENA | 60m | LONG | 6,25 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | ENA | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | ENA | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | ENA | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | ENA | 60m | LONG | 6,25 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | ENA | 60m | LONG | 6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.855,77 | -1,44% | €107,43 | €3.000,00 | 3,58% | 7 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2397 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 7 | €9.855,77 | €709,52 | €2.128,57 | €195,23 | €47,66 |
| TEST | Rapida score 6–7,5 — Cost Aware | 6 | €11.335,87 | €888,53 | €2.665,58 | €226,90 | €-8,69 |
| TEST | Benchmark Donchian breakout 1H | 2 | €11.189,72 | €878,48 | €1.756,97 | €107,05 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 6 | €11.111,84 | €1.196,28 | €2.392,57 | €170,29 | €-5,05 |
| TEST | Scanner Top 5 Long 1H | 4 | €11.052,74 | €858,91 | €1.717,82 | €163,75 | €40,36 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €10.926,27 | €857,80 | €1.715,60 | €104,53 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.883,19 | €677,89 | €2.033,66 | €163,42 | €62,22 |
| TEST | Combo Adaptive — madre | 5 | €10.665,78 | €1.019,54 | €2.039,09 | €160,49 | €-2,89 |
| TEST | Rapida V1 — senza PEPE | 6 | €10.640,02 | €1.692,66 | €5.077,97 | €211,79 | €-38,06 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.584,28 | €1.218,95 | €3.656,84 | €211,70 | €-19,11 |
| TEST | Rapida 1H V3 Filtered — madre | 6 | €10.516,28 | €1.211,12 | €3.633,35 | €210,34 | €-18,98 |
| TEST | Combo Adaptive — Long Only | 4 | €10.464,51 | €2.025,96 | €4.051,91 | €155,53 | €3,24 |
| TEST | Rapida V3 NoHigh — Regime Guard | 2 | €10.394,25 | €284,00 | €852,00 | €101,41 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.359,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.345,51 | €1.043,49 | €2.086,98 | €153,94 | €-6,19 |
| TEST | Ampia 4H | 7 | €10.340,80 | €1.057,57 | €2.115,14 | €205,57 | €61,39 |
| TEST | Rapida V1 — target pieno 2R | 5 | €10.319,61 | €732,34 | €2.197,03 | €156,11 | €-0,17 |
| TEST | Sol Donchian 1H | 0 | €10.305,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.277,95 | €831,85 | €1.663,69 | €154,32 | €36,92 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.242,63 | €407,92 | €815,83 | €51,22 | €-0,16 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.222,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.211,12 | €449,62 | €899,24 | €50,98 | €15,16 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 6 | €10.205,60 | €1.784,29 | €3.568,59 | €204,36 | €0,14 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 6 | €10.199,63 | €1.783,25 | €3.566,50 | €204,24 | €0,14 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.181,65 | €2.248,48 | €4.496,97 | €203,73 | €-14,06 |
| TEST | Sol Ema 1H | 0 | €10.177,93 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 2 | €10.163,03 | €429,03 | €1.287,09 | €101,56 | €2,39 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.137,41 | €1.962,17 | €3.924,33 | €153,15 | €60,33 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 5 | €10.135,41 | €452,99 | €1.358,96 | €152,82 | €-1,49 |
| TEST | Sol Ema 4H | 1 | €10.108,43 | €439,17 | €878,34 | €50,55 | €-0,18 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 4 | €10.103,82 | €570,41 | €1.711,23 | €150,54 | €-12,30 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.056,36 | €648,94 | €1.297,88 | €50,35 | €-12,59 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.043,50 | €775,58 | €1.551,16 | €50,15 | €14,43 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.033,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.004,40 | €704,37 | €1.408,74 | €50,10 | €-13,66 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €9.998,89 | €284,10 | €852,30 | €50,06 | €-12,15 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.992,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.988,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.956,34 | €487,73 | €975,47 | €0,00 | €46,29 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.950,88 | €700,60 | €1.401,20 | €49,83 | €-13,59 |
| TEST | Sol Bollinger 4H | 1 | €9.942,95 | €478,97 | €957,94 | €49,65 | €12,88 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.942,69 | €706,71 | €1.413,42 | €99,54 | €-4,30 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.924,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 6 | €9.891,27 | €1.651,53 | €3.303,06 | €194,30 | €34,64 |
| TEST | Scanner Top20 Long | 6 | €9.891,27 | €1.651,53 | €3.303,06 | €194,30 | €34,64 |
| TEST | FAST NoHigh <7,5 · SHORT only | 5 | €9.883,20 | €441,71 | €1.325,14 | €149,01 | €-1,45 |
| TEST | Combo Scanner | 5 | €9.874,97 | €801,63 | €1.603,27 | €148,27 | €35,53 |
| TEST | Eth Adaptive 1H | 0 | €9.873,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.854,56 | €1.892,30 | €3.784,59 | €196,89 | €-4,26 |
| TEST | Sol Bollinger 1H | 0 | €9.839,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 3 | €9.822,90 | €919,99 | €2.759,98 | €147,16 | €-6,02 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €9.819,98 | €554,67 | €1.664,02 | €147,23 | €-12,02 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.817,63 | €697,82 | €1.395,64 | €98,29 | €-4,25 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.799,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €9.790,61 | €961,34 | €1.922,67 | €146,29 | €0,64 |
| TEST | Btc Ema 1H | 0 | €9.779,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 5 | €9.778,37 | €837,50 | €2.512,51 | €147,36 | €-18,17 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.758,45 | €745,95 | €2.237,86 | €195,16 | €-1,03 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.709,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.691,98 | €1.224,82 | €3.674,45 | €193,93 | €-13,32 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.682,13 | €1.706,39 | €3.412,78 | €193,45 | €-17,93 |
| TEST | Global Confluence puro 1H | 0 | €9.679,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.635,07 | €779,81 | €1.559,63 | €144,67 | €34,61 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 6 | €9.609,61 | €2.958,17 | €5.916,35 | €191,69 | €6,31 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 6 | €9.599,39 | €2.955,03 | €5.910,05 | €191,48 | €6,31 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.588,30 | €406,69 | €1.220,07 | €96,33 | €-11,65 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.584,17 | €3.588,44 | €7.176,88 | €191,71 | €52,06 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 6 | €9.562,26 | €2.943,60 | €5.887,19 | €190,74 | €6,28 |
| TEST | Top 5 + BTC — Guard | 4 | €9.538,42 | €731,29 | €1.462,57 | €143,29 | €-2,80 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.477,92 | €2.920,91 | €5.841,82 | €188,69 | €0,90 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.452,94 | €2.981,09 | €5.962,17 | €188,97 | €-15,27 |
| TEST | Bilanciata 1H V2 | 4 | €9.441,25 | €1.001,50 | €3.004,50 | €187,79 | €-4,08 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.435,60 | €2.909,31 | €5.818,62 | €188,82 | €5,74 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.421,74 | €397,72 | €1.193,17 | €93,98 | €-11,44 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 5 | €9.342,15 | €1.048,09 | €2.096,17 | €181,93 | €49,60 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.316,59 | €714,28 | €1.428,56 | €139,95 | €-2,73 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 5 | €9.313,63 | €2.721,06 | €5.442,12 | €186,43 | €5,49 |
| TEST | Bilanciata V3 · LONG only | 3 | €9.290,66 | €870,16 | €2.610,47 | €139,19 | €-5,70 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €9.286,87 | €1.555,58 | €3.111,16 | €138,80 | €-4,77 |
| TEST | Combo Trend | 5 | €9.274,85 | €1.023,97 | €2.047,95 | €139,11 | €-8,86 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 2 | €9.209,98 | €332,47 | €664,95 | €48,68 | €-2,68 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.163,35 | €865,53 | €1.731,06 | €138,62 | €-0,81 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €9.000,90 | €643,84 | €1.287,69 | €90,25 | €-4,63 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €8.918,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.851,54 | €2.301,55 | €4.603,10 | €176,94 | €-2,41 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €8.833,24 | €1.479,60 | €2.959,19 | €132,02 | €-4,54 |
| TEST | Combo Adaptive — target pieno 3R | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.855,77 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.335,87 | €1.346,38 | 151 | 151 | 53,64% | 1,46 | €8,92 | 5,23% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.189,72 | €1.189,97 | 114 | 114 | 46,49% | 1,46 | €10,44 | 6,27% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.111,84 | €1.118,65 | 119 | 119 | 53,78% | 1,53 | €9,40 | 6,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.052,74 | €1.013,44 | 149 | 149 | 47,65% | 1,36 | €6,80 | 8,85% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.926,27 | €926,51 | 82 | 82 | 45,12% | 1,55 | €11,30 | 6,27% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.883,19 | €822,88 | 37 | 37 | 54,05% | 2,16 | €22,24 | 3,82% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.665,78 | €670,22 | 157 | 157 | 46,50% | 1,26 | €4,27 | 7,91% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.640,02 | €681,34 | 226 | 226 | 46,46% | 1,16 | €3,01 | 7,45% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.584,28 | €605,70 | 196 | 196 | 50,51% | 1,19 | €3,09 | 9,50% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.516,28 | €537,56 | 240 | 240 | 45,00% | 1,12 | €2,24 | 9,48% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.464,51 | €463,70 | 129 | 129 | 47,29% | 1,17 | €3,59 | 7,78% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.394,25 | €394,76 | 84 | 84 | 48,81% | 1,24 | €4,70 | 5,24% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.359,25 | €359,25 | 50 | 45 | 50,00% | 1,31 | €7,18 | 3,89% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.345,51 | €353,22 | 120 | 120 | 47,50% | 1,15 | €2,94 | 8,68% |
| TEST | Ampia 4H | Confluenza trend | €10.340,80 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.319,61 | €321,10 | 239 | 239 | 40,17% | 1,08 | €1,34 | 6,56% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.305,79 | €305,79 | 15 | 15 | 60,00% | 2,24 | €20,39 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.277,95 | €242,06 | 132 | 132 | 44,70% | 1,09 | €1,83 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.242,63 | €243,28 | 8 | 8 | 62,50% | 3,16 | €30,41 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.222,53 | €222,53 | 63 | 63 | 50,79% | 1,16 | €3,53 | 4,50% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.211,12 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.205,60 | €207,92 | 111 | 111 | 42,34% | 1,08 | €1,87 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.199,63 | €201,94 | 115 | 115 | 42,61% | 1,08 | €1,76 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.181,65 | €198,71 | 138 | 138 | 48,55% | 1,08 | €1,44 | 10,31% |
| TEST | Sol Ema 1H | Trend following EMA | €10.177,93 | €177,93 | 17 | 17 | 47,06% | 1,41 | €10,47 | 3,33% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.163,03 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,25% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.137,41 | €79,41 | 159 | 159 | 45,28% | 1,03 | €0,50 | 8,69% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.135,41 | €137,81 | 153 | 153 | 42,48% | 1,04 | €0,90 | 7,10% |
| TEST | Sol Ema 4H | Trend following EMA | €10.108,43 | €109,13 | 9 | 9 | 44,44% | 1,51 | €12,13 | 2,27% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.103,82 | €117,25 | 165 | 165 | 43,64% | 1,03 | €0,71 | 10,60% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.056,36 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.043,50 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.033,18 | €33,18 | 18 | 18 | 44,44% | 1,07 | €1,84 | 4,59% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Btc Ema 4H | Trend following EMA | €10.004,40 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.998,89 | €11,54 | 73 | 73 | 42,47% | 1,01 | €0,16 | 4,16% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.992,60 | €-7,40 | 10 | 10 | 50,00% | 0,97 | €-0,74 | 1,89% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Doge Ema 1H | Trend following EMA | €9.988,85 | €-11,15 | 17 | 17 | 58,82% | 0,97 | €-0,66 | 2,77% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Eth Ema 4H | Trend following EMA | €9.956,34 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,88 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.942,95 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.942,69 | €-52,16 | 40 | 40 | 47,50% | 0,95 | €-1,30 | 4,21% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,84 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.891,27 | €-141,07 | 136 | 136 | 47,79% | 0,94 | €-1,04 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.891,27 | €-141,07 | 136 | 136 | 47,79% | 0,94 | €-1,04 | 10,31% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.883,20 | €-114,47 | 117 | 117 | 41,03% | 0,95 | €-0,98 | 7,10% |
| TEST | Combo Scanner | Combo Scanner | €9.874,97 | €-159,56 | 137 | 137 | 44,53% | 0,95 | €-1,16 | 11,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.873,49 | €-126,51 | 14 | 14 | 42,86% | 0,72 | €-9,04 | 3,14% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.854,56 | €-138,61 | 65 | 65 | 49,23% | 0,91 | €-2,13 | 5,38% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.839,28 | €-160,72 | 13 | 13 | 38,46% | 0,68 | €-12,36 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.822,90 | €-169,42 | 165 | 165 | 41,21% | 0,95 | €-1,03 | 9,12% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.819,98 | €-166,99 | 134 | 134 | 43,28% | 0,94 | €-1,25 | 7,10% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.817,63 | €-177,28 | 40 | 40 | 42,50% | 0,83 | €-4,43 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Ema 1H | Trend following EMA | €9.799,26 | €-200,74 | 20 | 20 | 40,00% | 0,71 | €-10,04 | 4,80% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.790,61 | €-208,87 | 119 | 112 | 42,86% | 0,94 | €-1,76 | 10,88% |
| TEST | Btc Ema 1H | Trend following EMA | €9.779,44 | €-220,56 | 14 | 14 | 28,57% | 0,55 | €-15,75 | 2,31% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.778,37 | €-201,86 | 174 | 174 | 41,95% | 0,94 | €-1,16 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.758,45 | €-239,06 | 212 | 212 | 43,40% | 0,94 | €-1,13 | 9,00% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.709,98 | €-290,02 | 14 | 14 | 28,57% | 0,52 | €-20,72 | 3,74% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.691,98 | €-292,43 | 106 | 106 | 45,28% | 0,86 | €-2,76 | 9,26% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.682,13 | €-297,89 | 83 | 83 | 39,76% | 0,85 | €-3,59 | 8,88% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.679,31 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.635,07 | €-398,57 | 124 | 124 | 43,55% | 0,84 | €-3,21 | 12,28% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.609,61 | €-392,96 | 66 | 66 | 31,82% | 0,79 | €-5,95 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.599,39 | €-403,17 | 61 | 61 | 36,07% | 0,78 | €-6,61 | 7,98% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.588,30 | €-399,22 | 94 | 94 | 40,43% | 0,84 | €-4,25 | 6,64% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.584,17 | €-463,09 | 55 | 55 | 32,73% | 0,76 | €-8,42 | 8,18% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.562,26 | €-440,29 | 63 | 63 | 34,92% | 0,78 | €-6,99 | 7,80% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.538,42 | €-457,62 | 115 | 115 | 38,26% | 0,84 | €-3,98 | 7,34% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.477,92 | €-519,47 | 70 | 70 | 37,14% | 0,75 | €-7,42 | 7,96% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.452,94 | €-527,93 | 65 | 65 | 35,38% | 0,75 | €-8,12 | 7,26% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.441,25 | €-552,71 | 111 | 101 | 44,14% | 0,77 | €-4,98 | 9,18% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.435,60 | €-566,44 | 97 | 97 | 48,45% | 0,74 | €-5,84 | 9,02% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.421,74 | €-565,77 | 98 | 98 | 44,90% | 0,80 | €-5,77 | 8,22% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.342,15 | €-705,98 | 169 | 169 | 42,01% | 0,78 | €-4,18 | 15,45% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.316,59 | €-679,55 | 132 | 132 | 39,39% | 0,78 | €-5,15 | 8,78% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.313,63 | €-688,38 | 55 | 55 | 25,45% | 0,64 | €-12,52 | 11,41% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.290,66 | €-702,07 | 119 | 119 | 41,18% | 0,70 | €-5,90 | 8,85% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.286,87 | €-706,49 | 34 | 34 | 23,53% | 0,37 | €-20,78 | 8,80% |
| TEST | Combo Trend | Combo Trend | €9.274,85 | €-714,19 | 161 | 161 | 39,13% | 0,81 | €-4,44 | 10,85% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.209,98 | €-786,94 | 76 | 76 | 35,53% | 0,67 | €-10,35 | 10,40% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.163,35 | €-834,76 | 127 | 127 | 37,80% | 0,68 | €-6,57 | 12,31% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.000,90 | €-993,70 | 93 | 93 | 35,48% | 0,63 | €-10,68 | 10,18% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.918,97 | €-1.081,03 | 48 | 48 | 35,42% | 0,46 | €-22,52 | 12,56% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.851,54 | €-1.143,10 | 60 | 60 | 26,67% | 0,56 | €-19,05 | 12,40% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.833,24 | €-1.160,44 | 80 | 80 | 31,25% | 0,51 | €-14,51 | 13,85% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,74600 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €46,99 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,41994 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-0,72 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 83,18500 | 81,67793 | 52,97621 | 90,53117 | €8,52 | €25,56 | €0,00 | €1,40 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2503,94069 | 2503,44000 | 2419,15966 | 1681,81350 | 2673,50272 | €10,53 | €31,58 | €1,07 | €-0,01 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 244,76000 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €-13,65 |
| Bilanciata 1H — LONG senza Range High Vol | TRUMP | LONG | Confluenza trend | 60m | 3,0x | 2,74355 | 2,74600 | 2,55460 | 1,84275 | 3,12145 | €234,56 | €703,68 | €48,46 | €0,63 |
| Bilanciata 1H — LONG senza Range High Vol | ENA | LONG | Confluenza trend | 60m | 3,0x | 0,16818 | 0,16698 | 0,15607 | 0,11296 | 0,19242 | €13,64 | €40,93 | €2,95 | €-0,29 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19977 | €131,74 | €395,21 | €47,43 | €0,00 |
| Bilanciata 1H V2 | TRUMP | LONG | Confluenza trend V2 | 60m | 3,0x | 2,74355 | 2,74600 | 2,55460 | 1,84275 | 3,12145 | €228,59 | €685,78 | €47,23 | €0,61 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16818 | 0,16698 | 0,15607 | 0,11296 | 0,19242 | €218,78 | €656,35 | €47,29 | €-4,70 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16848 | 0,16698 | 0,15591 | 0,11316 | 0,19363 | €219,57 | €658,70 | €49,15 | €-5,88 |
| Bilanciata 1H V3 Filtered | TRUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,74655 | 2,74600 | 2,55919 | 1,84477 | 3,12128 | €240,00 | €720,01 | €49,12 | €-0,14 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,02 | €417,05 | €50,05 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16848 | 0,16698 | 0,15871 | 0,11316 | 0,18315 | €324,69 | €974,07 | €56,53 | €-8,69 |
| Rapida V1 — no HIGH + score <7,5 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €132,75 | €398,25 | €47,79 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €22,66 | €67,97 | €3,99 | €-0,97 |
| Rapida V1 — no HIGH + score <7,5 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08608 | 0,08697 | 0,08737 | 0,11435 | 0,08416 | €16,72 | €50,16 | €0,75 | €-0,52 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €284,10 | €852,30 | €50,06 | €-12,15 |
| Rapida V1 — senza PEPE | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| Rapida V1 — senza PEPE | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 244,76000 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €-1,53 |
| Rapida V1 — senza PEPE | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| Rapida V1 — senza PEPE | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €145,28 | €435,84 | €52,30 | €0,00 |
| Rapida V1 — senza PEPE | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08608 | 0,08697 | 0,08737 | 0,11435 | 0,08416 | €1.181,49 | €3.544,46 | €52,89 | €-36,53 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| Rapida V1 — target pieno 2R | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| Rapida V1 — target pieno 2R | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16701 | 0,16698 | 0,15751 | 0,11218 | 0,18602 | €289,77 | €869,31 | €49,46 | €-0,17 |
| Rapida 1H V3 Filtered — madre | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered — madre | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 244,76000 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €-18,81 |
| Rapida 1H V3 Filtered — madre | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,42 | €25,27 | €3,03 | €0,00 |
| Rapida 1H V3 Filtered — madre | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16701 | 0,16698 | 0,15751 | 0,11218 | 0,18127 | €283,71 | €851,14 | €48,43 | €-0,17 |
| Rapida V3 — no volatilità HIGH | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €9,29 | €27,86 | €3,34 | €0,00 |
| Rapida V3 — no volatilità HIGH | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €281,15 | €843,44 | €49,54 | €-12,02 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| Rapida V3 — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 244,76000 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €-17,68 |
| Rapida V3 — Long Only | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €135,44 | €406,31 | €48,76 | €0,00 |
| Rapida V3 — Long Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €11,51 | €34,54 | €2,03 | €-0,49 |
| Rapida V3 — Long + no HIGH + score <7,5 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €134,26 | €402,77 | €48,33 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €272,43 | €817,30 | €48,00 | €-11,65 |
| Rapida V3 — senza ESPORTS | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 244,76000 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €-0,86 |
| Rapida V3 — senza ESPORTS | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| Rapida V3 — senza ESPORTS | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16701 | 0,16698 | 0,15751 | 0,11218 | 0,18127 | €285,86 | €857,57 | €48,80 | €-0,17 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,69 | €419,06 | €50,29 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €287,72 | €863,17 | €50,70 | €-12,30 |
| Rapida V3 senza ESPORTS — MFE Lock | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 244,76000 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €-18,93 |
| Rapida V3 senza ESPORTS — MFE Lock | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,48 | €25,43 | €3,05 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16701 | 0,16698 | 0,15751 | 0,11218 | 0,18127 | €285,55 | €856,64 | €48,74 | €-0,17 |
| Rapida V3 — qualità completa + profit lock | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15804 | 0,15804 | 0,13908 | 0,10615 | 0,18649 | €130,02 | €390,07 | €46,81 | €0,00 |
| Rapida V3 — qualità completa + profit lock | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €267,70 | €803,11 | €47,17 | €-11,44 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2503,44000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,14 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 83,18500 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,35 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,74600 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €66,18 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08697 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-7,27 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | BTR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,15974 | 0,15974 | 0,14057 | 0,08067 | 0,20191 | €200,93 | €401,87 | €48,22 | €0,00 |
| Forza relativa 1H V2 | TRUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,15924 | €355,39 | €710,77 | €48,95 | €0,64 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 801,10000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-0,29 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | TRUMP | LONG | Trend following EMA | 60m | 2,0x | 2,74855 | 2,74600 | 2,53490 | 1,38802 | 3,21857 | €279,38 | €558,77 | €43,43 | €-0,52 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,74600 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €45,86 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €384,03 | €768,07 | €55,34 | €-5,50 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 244,76000 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €-14,42 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | BTR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €206,82 | €413,63 | €49,64 | €0,00 |
| Scanner Top10 Long | TRUMP | LONG | Scanner Top10 Long | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €369,58 | €739,16 | €50,91 | €0,66 |
| Scanner Top10 Long | ENA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €20,79 | €41,59 | €3,00 | €-0,30 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 244,76000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €-1,88 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,74600 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €41,44 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | BTR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top15 Long | ENA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €343,65 | €687,31 | €49,52 | €-4,92 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 244,76000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €-1,88 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,74600 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €41,44 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | BTR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top20 Long | ENA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €343,65 | €687,31 | €49,52 | €-4,92 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,74600 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €42,82 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,18500 | 81,99407 | 42,56385 | 89,32457 | €30,02 | €60,05 | €1,63 | €-0,78 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €357,11 | €714,22 | €51,46 | €-5,11 |
| Top 5 + BTC — solo MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Top 5 + BTC — solo MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,74600 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €40,14 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,18500 | 81,99407 | 42,56385 | 89,32457 | €28,15 | €56,29 | €1,53 | €-0,73 |
| Top 5 + BTC — solo MFE | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €334,77 | €669,55 | €48,24 | €-4,79 |
| Top 5 + BTC — Guard | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Top 5 + BTC — Guard | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,74600 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €1,94 |
| Top 5 + BTC — Guard | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €189,80 | €379,60 | €45,55 | €0,00 |
| Top 5 + BTC — Guard | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €331,18 | €662,37 | €47,72 | €-4,74 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Top 5 + BTC — BTC≤3 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €308,12 | €616,23 | €44,40 | €-4,41 |
| Top 5 + BTC — BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74655 | 2,74600 | 2,55919 | 1,38701 | 3,15875 | €323,73 | €647,47 | €44,17 | €-0,13 |
| Top 5 + BTC — BTC 2–3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Top 5 + BTC — BTC 2–3 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €323,94 | €647,88 | €46,68 | €-4,64 |
| Top 5 + BTC — BTC 2–3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74655 | 2,74600 | 2,55919 | 1,38701 | 3,15875 | €340,36 | €680,72 | €46,44 | €-0,14 |
| Top 5 + BTC — Guard + MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Top 5 + BTC — Guard + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,74600 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €1,90 |
| Top 5 + BTC — Guard + MFE | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €185,39 | €370,78 | €44,49 | €0,00 |
| Top 5 + BTC — Guard + MFE | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €323,48 | €646,96 | €46,61 | €-4,63 |
| Top 5 + BTC — Guard + BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,74600 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €1,89 |
| Top 5 + BTC — Guard + BTC≤3 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €319,77 | €639,55 | €46,08 | €-4,58 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €313,96 | €627,93 | €45,24 | €-4,49 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74655 | 2,74600 | 2,55919 | 1,38701 | 3,15875 | €329,88 | €659,76 | €45,01 | €-0,13 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,82 | €421,64 | €50,60 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,18500 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,23 | €0,71 | €-0,34 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,31040 | €370,24 | €740,48 | €51,00 | €0,66 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,20453 | €12,60 | €25,20 | €1,82 | €-0,18 |
| Top 5 + BTC — target pieno 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,94 | €421,89 | €50,63 | €0,00 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,18500 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,25 | €0,71 | €-0,34 |
| Top 5 + BTC — target pieno 3R | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,31040 | €370,46 | €740,92 | €51,03 | €0,66 |
| Top 5 + BTC — target pieno 3R | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,20453 | €12,61 | €25,22 | €1,82 | €-0,18 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 801,10000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-4,19 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 83,18500 | 81,73954 | 42,56385 | 89,88454 | €13,36 | €26,72 | €0,81 | €-0,35 |
| Combo Trend | TRUMP | LONG | Combo Trend | 60m | 2,0x | 2,74355 | 2,74600 | 2,53360 | 1,38549 | 3,20543 | €297,16 | €594,31 | €45,48 | €0,53 |
| Combo Trend | ENA | LONG | Combo Trend | 60m | 2,0x | 0,16848 | 0,16698 | 0,15452 | 0,08508 | 0,19921 | €272,14 | €544,28 | €45,12 | €-4,86 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,74600 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €41,08 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 84,28485 | 83,18500 | 81,99407 | 42,56385 | 89,32457 | €24,57 | €49,15 | €1,34 | €-0,64 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19484 | €343,11 | €686,22 | €49,44 | €-4,91 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 244,76000 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €-0,87 |
| Combo Adaptive — madre | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,74600 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €3,28 |
| Combo Adaptive — madre | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €222,35 | €444,69 | €53,36 | €0,00 |
| Combo Adaptive — madre | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €370,32 | €740,64 | €53,36 | €-5,30 |
| Combo Adaptive — MFE Trail esistente | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 244,76000 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €-1,15 |
| Combo Adaptive — MFE Trail esistente | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,74600 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €55,41 |
| Combo Adaptive — MFE Trail esistente | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €163,28 | €326,55 | €39,19 | €0,00 |
| Combo Adaptive — MFE Trail esistente | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €324,72 | €649,45 | €46,79 | €-4,65 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 244,76000 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €-13,75 |
| Combo Adaptive — Quality7 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €351,63 | €703,25 | €48,43 | €0,63 |
| Combo Adaptive — Quality7 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €336,30 | €672,60 | €48,46 | €-4,81 |
| Combo Adaptive — Trend/Transition | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive — Trend/Transition | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €204,79 | €409,58 | €49,15 | €0,00 |
| Combo Adaptive — Trend/Transition | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €357,90 | €715,80 | €49,30 | €0,64 |
| Combo Adaptive — Trend/Transition | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €342,54 | €685,09 | €49,36 | €-4,90 |
| Combo Adaptive — Quality7 + Regime | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €356,56 | €713,12 | €49,11 | €0,64 |
| Combo Adaptive — Quality7 + Regime | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €341,26 | €682,52 | €49,17 | €-4,88 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive — Long Only | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,74600 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €8,44 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €363,37 | €726,74 | €52,36 | €-5,20 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,74600 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €60,92 |
| Combo Adaptive — parziale 1R | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive — parziale 1R | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €41,31 | €82,63 | €5,95 | €-0,59 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €361,10 | €722,20 | €49,74 | €0,65 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €345,61 | €691,22 | €49,80 | €-4,95 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 79575,88000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €-13,66 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 79575,88000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €-13,59 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 79575,88000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €14,43 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 79575,88000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €-12,59 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 105,86117 | 105,84000 | 99,76922 | 53,45989 | 121,09104 | €439,17 | €878,34 | €50,55 | €-0,18 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 105,84000 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €15,16 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 105,84000 | 112,84334 | 160,38740 | 97,27311 | €478,97 | €957,94 | €49,65 | €12,88 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,86117 | 105,84000 | 99,21540 | 53,45989 | 122,47558 | €407,92 | €815,83 | €51,22 | €-0,16 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2503,44000 | 2464,86772 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €0,00 | €46,29 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.560,29 | €3.120,58 | €46,79 | €1,41 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,23 | €382,45 | €45,89 | €0,00 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 105,84000 | 103,93146 | 53,96853 | 112,74219 | €863,53 | €1.727,06 | €47,46 | €-16,62 |
| Master Adaptive V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16698 | 0,14798 | 0,08135 | 0,18729 | €293,22 | €586,43 | €47,70 | €21,47 |
| Master Adaptive V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €12,58 | €25,16 | €1,73 | €0,02 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.565,03 | €3.130,05 | €46,93 | €1,41 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,14959 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €343,00 | €686,01 | €47,25 | €0,61 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,91738 | 105,84000 | 103,99458 | 53,99328 | 112,76299 | €858,29 | €1.716,58 | €46,93 | €-17,30 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.493,28 | €2.986,56 | €44,78 | €1,35 |
| Master Adaptive Strict3 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €184,95 | €369,91 | €44,39 | €0,00 |
| Master Adaptive Strict3 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €320,71 | €641,43 | €44,18 | €0,57 |
| Master Adaptive Strict3 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16818 | 0,16698 | 0,15607 | 0,08493 | 0,19242 | €302,60 | €605,21 | €43,60 | €-4,33 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.572,67 | €3.145,34 | €47,16 | €1,42 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16110 | 0,16110 | 0,14177 | 0,08136 | 0,19977 | €197,88 | €395,75 | €47,49 | €0,00 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 107,32546 | 105,84000 | 104,39936 | 54,19936 | 113,17765 | €18,64 | €37,29 | €1,02 | €-0,52 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.539,56 | €3.079,12 | €46,16 | €1,39 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €188,69 | €377,37 | €45,28 | €0,00 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 105,84000 | 103,93146 | 53,96853 | 112,74219 | €852,06 | €1.704,12 | €46,83 | €-16,40 |
| Master Adaptive Gb20 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16698 | 0,14798 | 0,08135 | 0,18729 | €289,32 | €578,64 | €47,07 | €21,19 |
| Master Adaptive Gb20 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,78156 | 2,74600 | 2,59415 | 1,40469 | 3,15637 | €17,24 | €34,47 | €2,32 | €-0,44 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 83,18500 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €60,78 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2614,85753 | €1.568,97 | €3.137,94 | €47,05 | €1,42 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,43928 | 105,84000 | 103,65189 | 53,75184 | 114,80148 | €920,14 | €1.840,29 | €48,19 | €-10,36 |
| Master Adaptive Runner25 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16698 | 0,15522 | 0,08370 | 0,19732 | €14,90 | €29,81 | €1,89 | €0,22 |
| Master Adaptive Runner25 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15905 | 0,15905 | 0,13997 | 0,08032 | 0,21631 | €158,41 | €316,83 | €38,02 | €0,00 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive — Side × Regime Guard | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €210,11 | €420,21 | €50,43 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,16848 | 0,16698 | 0,15591 | 0,08508 | 0,19363 | €346,85 | €693,71 | €51,76 | €-6,19 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.568,02 | €3.136,03 | €47,02 | €1,42 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €192,17 | €384,35 | €46,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 105,84000 | 103,93146 | 53,96853 | 112,74219 | €867,81 | €1.735,61 | €47,70 | €-16,70 |
| Master Adaptive GB20 — Breakeven 0,5R | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16698 | 0,14798 | 0,08135 | 0,18729 | €294,67 | €589,34 | €47,94 | €21,58 |
| Master Adaptive GB20 — Breakeven 0,5R | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €12,64 | €25,28 | €1,74 | €0,02 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.566,35 | €3.132,70 | €46,97 | €1,41 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,97 | €383,94 | €46,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 105,84000 | 103,93146 | 53,96853 | 112,74219 | €866,88 | €1.733,77 | €47,65 | €-16,68 |
| Master Adaptive GB20 — 50% a 0,75R | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16698 | 0,14798 | 0,08135 | 0,18729 | €294,36 | €588,71 | €47,89 | €21,55 |
| Master Adaptive GB20 — 50% a 0,75R | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,74600 | 2,55460 | 1,38549 | 3,12145 | €12,63 | €25,26 | €1,74 | €0,02 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2503,44000 | 2474,17356 | 1263,66673 | 2577,34181 | €1.829,31 | €3.658,61 | €41,14 | €1,65 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,20861 | €188,78 | €377,55 | €45,31 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16698 | 0,15126 | 0,08135 | 0,18729 | €63,69 | €127,37 | €7,77 | €4,66 |
| Master Adaptive GB20 — Loss Cap 0,75R | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74855 | 2,74600 | 2,60434 | 1,38802 | 3,13312 | €443,59 | €887,18 | €46,55 | €-0,82 |
| Rapida V3 NoHigh — Regime Guard | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 83,18500 | 81,08374 | 52,16065 | 90,56048 | €216,52 | €649,56 | €0,00 | €46,22 |
| MAIN — Side × Regime Guard | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,41994 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-1,33 |
| MAIN — Side × Regime Guard | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2503,44000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,80 |
| MAIN — Side × Regime Guard | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16698 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €16,52 |
| MAIN — Dynamic Asset Selector | HYPE | LONG | Confluenza trend | 240m | 3,0x | 84,46489 | 83,18500 | 79,49888 | 56,73225 | 94,39691 | €288,05 | €864,16 | €50,81 | €-13,09 |
| MAIN — Dynamic Asset Selector | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16698 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €15,49 |
| Combo Trend — Side × Regime Guard | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTR | LONG | Combo Trend | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €231,16 | €462,32 | €55,48 | €0,00 |
| Combo Trend — Side × Regime Guard | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 83,18500 | 81,73954 | 42,56385 | 89,88454 | €32,97 | €65,95 | €1,99 | €-0,86 |
| Combo Trend — Side × Regime Guard | TRUMP | LONG | Combo Trend | 60m | 2,0x | 2,74355 | 2,74600 | 2,53360 | 1,38549 | 3,20543 | €363,18 | €726,37 | €55,58 | €0,65 |
| Combo Trend — Side × Regime Guard | ENA | LONG | Combo Trend | 60m | 2,0x | 0,16818 | 0,16698 | 0,15472 | 0,08493 | 0,19780 | €338,29 | €676,57 | €54,16 | €-4,84 |
| FAST NoHigh <7,5 · SHORT only | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €129,45 | €388,34 | €46,60 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16939 | 0,16698 | 0,15944 | 0,11378 | 0,18432 | €22,09 | €66,28 | €3,89 | €-0,94 |
| FAST NoHigh <7,5 · SHORT only | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08608 | 0,08697 | 0,08737 | 0,11435 | 0,08416 | €16,30 | €48,91 | €0,73 | €-0,50 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16848 | 0,16698 | 0,15591 | 0,11316 | 0,19363 | €207,67 | €623,01 | €46,49 | €-5,56 |
| Bilanciata V3 · LONG only | TRUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,74655 | 2,74600 | 2,55919 | 1,84477 | 3,12128 | €227,00 | €681,00 | €46,46 | €-0,14 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,55 | €385,10 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €179,76 | €359,53 | €43,14 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,85 | €385,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €180,04 | €360,08 | €43,21 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida V3 NoHigh — Regime Guard | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-56,03 | -1,07 | STOP |
| Rapida V3 senza ESPORTS — Stress Guard | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-55,11 | -1,07 | STOP |
| Rapida V3 senza ESPORTS — MFE Lock | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-52,94 | -1,07 | STOP |
| Rapida V3 — senza ESPORTS | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-52,60 | -1,07 | STOP |
| Rapida V3 — no volatilità HIGH | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-52,79 | -1,07 | STOP |
| Rapida 1H V3 Filtered — madre | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-52,60 | -1,07 | STOP |
| Rapida V1 — target pieno 2R | SUI | SHORT | 2026-08-28T11:15:00+00:00 | 0,76436 | €-54,21 | -1,07 | STOP |
| Rapida V1 — senza PEPE | SUI | SHORT | 2026-08-28T11:00:00+00:00 | 0,76190 | €-0,12 | -0,07 | STOP |
| Rapida V1 — no HIGH + score <7,5 | SUI | SHORT | 2026-08-28T11:00:00+00:00 | 0,76190 | €-3,55 | -0,07 | STOP |
| FAST NoHigh <7,5 · SHORT only | SUI | SHORT | 2026-08-28T11:00:00+00:00 | 0,76190 | €-3,47 | -0,07 | STOP |
| Sol Ema 4H | SOL | LONG | 2026-08-28T10:15:00+00:00 | 105,05473 | €53,06 | 1,06 | STOP |
| Sol Bollinger 1H | SOL | SHORT | 2026-08-28T10:15:00+00:00 | 104,99124 | €70,34 | 1,44 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 572/30 | 33/30 | 0,89 | 2,04 | -0,06R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 528/30 | 20/30 | 0,85 | 1,90 | -0,08R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 240/30 | 22/30 | 0,88 | 1,74 | -0,06R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 243/30 | 22/30 | 0,83 | 1,57 | -0,08R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 493/30 | 31/30 | 0,95 | 0,62 | -0,02R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 451/30 | 11/30 | 0,93 | 0,00 | -0,03R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 130/30 | 8/30 | 0,75 | 1,02 | -0,13R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 314/30 | 17/30 | 0,68 | 4,50 | -0,18R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 484/30 | 24/30 | 0,73 | 0,64 | -0,14R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 444/30 | 7/30 | 0,64 | 0,02 | -0,19R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 493/30 | 30/30 | 0,98 | 1,02 | -0,01R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 816/30 | 55/30 | 0,91 | 1,12 | -0,04R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 151/30 | 15/30 | 0,57 | 0,99 | -0,27R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 717/30 | 44/30 | 0,82 | 1,20 | -0,09R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 721/30 | 37/30 | 0,82 | 0,76 | -0,09R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 664/30 | 23/30 | 0,76 | 1,12 | -0,12R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 347/30 | 52/30 | 0,79 | 0,87 | -0,12R | €-3,67 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 13/30 | 0,00 | 1,47 | 0,00R | €12,42 | 2,25% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 37/30 | 0,00 | 2,16 | 0,00R | €22,24 | 3,82% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 50/30 | 28/30 | 0,67 | 0,60 | -0,18R | €-2,16 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 862/30 | 121/30 | 0,94 | 0,69 | -0,03R | €-7,02 | 13,99% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 106/30 | 0,00 | 0,86 | 0,00R | €-2,76 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 280/30 | 101/30 | 1,20 | 0,77 | 0,10R | €-4,98 | 9,18% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 544/30 | 165/30 | 1,02 | 0,95 | 0,01R | €-1,03 | 9,12% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 465/30 | 119/30 | 0,97 | 0,70 | -0,02R | €-5,90 | 8,85% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 246/30 | 73/30 | 0,93 | 1,01 | -0,03R | €0,16 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 514/30 | 117/30 | 0,87 | 0,95 | -0,06R | €-0,98 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 581/30 | 153/30 | 0,90 | 1,04 | -0,05R | €0,90 | 7,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 965/30 | 226/30 | 0,85 | 1,16 | -0,08R | €3,01 | 7,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 151/30 | 0,00 | 1,46 | 0,00R | €8,92 | 5,23% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 95/30 | 0,00 | 0,72 | 0,00R | €-8,78 | 12,64% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 38/30 | 0,00 | 1,14 | 0,00R | €3,94 | 3,35% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 548/30 | 137/30 | 0,92 | 0,84 | -0,04R | €-4,26 | 12,33% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 923/30 | 239/30 | 0,84 | 1,08 | -0,08R | €1,34 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 67/30 | 45/30 | 0,89 | 1,31 | -0,06R | €7,18 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 896/30 | 240/30 | 0,87 | 1,12 | -0,07R | €2,24 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 670/30 | 136/30 | 0,93 | 0,75 | -0,03R | €-6,57 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 283/30 | 98/30 | 0,99 | 0,80 | -0,01R | €-5,77 | 8,22% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 287/30 | 94/30 | 0,96 | 0,84 | -0,02R | €-4,25 | 6,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 570/30 | 174/30 | 0,97 | 0,94 | -0,01R | €-1,16 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 41/30 | 0,00 | 1,25 | 0,00R | €6,05 | 3,97% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 84/30 | 0,00 | 1,24 | 0,00R | €4,70 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 596/30 | 134/30 | 0,80 | 0,94 | -0,10R | €-1,25 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 165/30 | 0,00 | 1,03 | 0,00R | €0,71 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 196/30 | 0,00 | 1,19 | 0,00R | €3,09 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 63/30 | 0,00 | 1,16 | 0,00R | €3,53 | 4,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 849/30 | 212/30 | 0,84 | 0,94 | -0,08R | €-1,13 | 9,00% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 327/30 | 52/30 | 0,83 | 1,24 | -0,11R | €5,39 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 293/30 | 81/30 | 1,17 | 0,55 | 0,07R | €-15,55 | 14,60% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 15/30 | 9/30 | 0,64 | 0,86 | -0,19R | €-3,49 | 1,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 2/30 | 2/30 | 2,26 | 2,39 | 0,67R | €35,09 | 0,96% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 9/30 | 6/30 | 3,40 | 4,66 | 0,60R | €34,87 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 2/30 | 2/30 | 1,56 | 1,54 | 0,31R | €14,72 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 17/30 | 10/30 | 0,32 | 0,85 | -0,54R | €-4,29 | 1,49% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 6/30 | 4/30 | 0,50 | 0,80 | -0,45R | €-8,55 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 20/30 | 14/30 | 0,75 | 0,55 | -0,15R | €-15,75 | 2,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 4/30 | 3/30 | 0,75 | 1,19 | -0,20R | €6,47 | 1,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 712/30 | 157/30 | 1,01 | 1,26 | 0,01R | €4,27 | 7,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 443/30 | 129/30 | 1,07 | 1,17 | 0,04R | €3,59 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 781/30 | 169/30 | 1,02 | 0,78 | 0,01R | €-4,18 | 15,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 653/30 | 159/30 | 0,96 | 1,03 | -0,02R | €0,50 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 83/30 | 40/30 | 1,44 | 0,95 | 0,18R | €-1,30 | 4,21% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 83/30 | 40/30 | 1,43 | 0,83 | 0,18R | €-4,43 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 227/30 | 83/30 | 0,99 | 0,85 | -0,00R | €-3,59 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 250/30 | 65/30 | 1,04 | 0,91 | 0,02R | €-2,13 | 5,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 94/30 | 0,74 | 0,53 | -0,20R | €-11,02 | 12,67% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 120/30 | 0,00 | 1,15 | 0,00R | €2,94 | 8,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 75/30 | 0,74 | 0,38 | -0,20R | €-16,04 | 12,67% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 109/30 | 48/30 | 1,23 | 0,46 | 0,10R | €-22,52 | 12,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 445/30 | 137/30 | 1,12 | 0,95 | 0,07R | €-1,16 | 11,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 588/30 | 161/30 | 1,00 | 0,81 | -0,00R | €-4,44 | 10,85% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 119/30 | 0,00 | 1,53 | 0,00R | €9,40 | 6,20% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 13/30 | 10/30 | 1,77 | 0,97 | 0,27R | €-0,74 | 1,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 17/30 | 13/30 | 0,45 | 0,79 | -0,39R | €-5,78 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 28/30 | 17/30 | 0,42 | 0,97 | -0,41R | €-0,66 | 2,77% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 313/30 | 114/30 | 0,89 | 1,46 | -0,07R | €10,44 | 6,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 243/30 | 82/30 | 0,90 | 1,55 | -0,06R | €11,30 | 6,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 596/30 | 127/30 | 1,01 | 0,68 | 0,01R | €-6,57 | 12,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 23/30 | 14/30 | 0,59 | 0,72 | -0,30R | €-9,04 | 3,14% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 15/30 | 7/30 | 1,86 | 0,22 | 0,32R | €-42,33 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 22/30 | 14/30 | 0,43 | 0,52 | -0,46R | €-20,72 | 3,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 32/30 | 20/30 | 0,54 | 0,71 | -0,31R | €-10,04 | 4,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 6/30 | 5/30 | 0,46 | 0,58 | -0,38R | €-17,74 | 1,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 14/30 | 17/30 | 0,90 | 0,41 | -0,07R | €-18,86 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 289/30 | 70/30 | 1,08 | 0,75 | 0,05R | €-7,42 | 7,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 66/30 | 0,00 | 0,79 | 0,00R | €-5,95 | 8,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 55/30 | 0,00 | 0,64 | 0,00R | €-12,52 | 11,41% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 61/30 | 0,00 | 0,78 | 0,00R | €-6,61 | 7,98% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 546/30 | 97/30 | 1,38 | 0,74 | 0,12R | €-5,84 | 9,02% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 254/30 | 65/30 | 1,06 | 0,75 | 0,04R | €-8,12 | 7,26% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 265/30 | 55/30 | 1,05 | 0,76 | 0,03R | €-8,42 | 8,18% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 183/30 | 60/30 | 1,00 | 0,56 | -0,00R | €-19,05 | 12,40% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 278/30 | 63/30 | 1,03 | 0,78 | 0,02R | €-6,99 | 7,80% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 713/30 | 105/30 | 0,93 | 0,47 | -0,04R | €-14,80 | 17,39% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 274/30 | 112/30 | 1,24 | 0,94 | 0,12R | €-1,76 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 230/30 | 70/30 | 0,52 | 0,65 | -0,27R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 230/30 | 70/30 | 0,52 | 0,65 | -0,27R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 230/30 | 70/30 | 0,52 | 0,65 | -0,27R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 262/30 | 89/30 | 0,67 | 0,64 | -0,18R | €-9,30 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 270/30 | 61/30 | 0,77 | 0,58 | -0,10R | €-12,17 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 243/30 | 62/30 | 0,69 | 0,56 | -0,14R | €-12,20 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 437/30 | 138/30 | 1,08 | 1,08 | 0,04R | €1,44 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 438/30 | 136/30 | 1,08 | 0,94 | 0,04R | €-1,04 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 438/30 | 136/30 | 1,08 | 0,94 | 0,04R | €-1,04 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 431/30 | 132/30 | 1,14 | 1,09 | 0,07R | €1,83 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 155/30 | 34/30 | 0,76 | 0,37 | -0,14R | €-20,78 | 8,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 316/30 | 80/30 | 0,89 | 0,51 | -0,06R | €-14,51 | 13,85% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 331/30 | 93/30 | 1,12 | 0,63 | 0,05R | €-10,68 | 10,18% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 279/30 | 76/30 | 0,97 | 0,67 | -0,02R | €-10,35 | 10,40% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 427/30 | 132/30 | 1,20 | 0,78 | 0,08R | €-5,15 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 351/30 | 115/30 | 1,13 | 0,84 | 0,07R | €-3,98 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 479/30 | 124/30 | 1,11 | 0,84 | 0,05R | €-3,21 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 379/30 | 115/30 | 1,07 | 1,08 | 0,04R | €1,76 | 12,06% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 356/30 | 111/30 | 1,11 | 1,08 | 0,05R | €1,87 | 11,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 476/30 | 149/30 | 1,15 | 1,36 | 0,08R | €6,80 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 32/30 | 18/30 | 0,82 | 1,07 | -0,12R | €1,84 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 9/30 | 8/30 | 2,54 | 3,16 | 0,54R | €30,41 | 1,01% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 24/30 | 13/30 | 0,79 | 0,68 | -0,12R | €-12,36 | 2,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 5/30 | 4/30 | 1,99 | 0,56 | 0,41R | €-17,33 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 26/30 | 15/30 | 1,07 | 2,24 | 0,04R | €20,39 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 7/30 | 6/30 | 1,26 | 2,73 | 0,16R | €32,74 | 1,05% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 30/30 | 17/30 | 0,99 | 1,41 | -0,01R | €10,47 | 3,33% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 10/30 | 9/30 | 0,85 | 1,51 | -0,10R | €12,13 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08697**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 29.7 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 79575.88 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, stop_within_limit**
- High **0.08697**; close **0.08692**; wick alta **23.1%**; volume **x0.13**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=463; LEGACY_RESEARCH_EVIDENCE_V3=2276; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **TREND_UP**
- Famiglia: **TREND_UP**
- Confidenza: **75,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +3.0, 67% sopra EMA50, ADX 39.5.
- BTC trend score: **3,00**; ADX: **39,52**; breadth sopra EMA50: **66,67%**
- Mediana alt vs BTC: **-0,02%**; dispersione: **6,26%**

- Aperti in questo ciclo: **5**
- Chiusi in questo ciclo: **11**
- Posizioni research aperte: **452**
- Trade research chiusi: **34497**
- Eventi di mercato indipendenti chiusi: **4636**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **89072**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 6 | 572 | 572 | 36,01% | 0,89 | -0,06R | €-315,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 6 | 528 | 528 | 35,42% | 0,85 | -0,08R | €-398,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 2 | 240 | 240 | 47,50% | 0,88 | -0,06R | €-152,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 1 | 243 | 243 | 34,57% | 0,83 | -0,08R | €-200,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 4 | 493 | 493 | 36,92% | 0,95 | -0,02R | €-116,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 4 | 451 | 451 | 37,47% | 0,93 | -0,03R | €-143,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 130 | 130 | 35,38% | 0,75 | -0,13R | €-164,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 2 | 314 | 314 | 29,94% | 0,68 | -0,18R | €-553,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 3 | 484 | 484 | 30,99% | 0,73 | -0,14R | €-678,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 3 | 444 | 444 | 29,95% | 0,64 | -0,19R | €-832,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 4 | 493 | 493 | 37,32% | 0,98 | -0,01R | €-56,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 5 | 816 | 816 | 40,69% | 0,91 | -0,04R | €-315,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 0 | 151 | 151 | 33,77% | 0,57 | -0,27R | €-404,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 6 | 717 | 717 | 33,33% | 0,82 | -0,09R | €-653,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 6 | 721 | 721 | 33,29% | 0,82 | -0,09R | €-653,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 6 | 664 | 664 | 32,83% | 0,76 | -0,12R | €-782,00 |
| MAIN | 20 | 347 | 347 | 28,82% | 0,79 | -0,12R | €-424,02 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 50 | 50 | 38,00% | 0,67 | -0,18R | €-87,69 |
| Bilanciata 1H V1 | 14 | 862 | 862 | 35,96% | 0,94 | -0,03R | €-288,65 |
| Bilanciata 1H V2 | 5 | 322 | 280 | 41,30% | 1,20 | 0,10R | €330,26 |
| Bilanciata 1H V3 Filtered | 8 | 544 | 544 | 37,68% | 1,02 | 0,01R | €64,16 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 8 | 465 | 465 | 37,42% | 0,97 | -0,02R | €-81,19 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 246 | 246 | 39,43% | 0,93 | -0,03R | €-84,43 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 5 | 514 | 514 | 35,99% | 0,87 | -0,06R | €-323,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 5 | 581 | 581 | 36,83% | 0,90 | -0,05R | €-289,28 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 8 | 965 | 965 | 36,27% | 0,85 | -0,08R | €-740,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 7 | 548 | 548 | 38,50% | 0,92 | -0,04R | €-211,38 |
| SHADOW_1H_FAST_TP2_V1 | 8 | 923 | 923 | 33,91% | 0,84 | -0,08R | €-748,39 |
| Rapida 1H V2 | 0 | 77 | 67 | 44,16% | 0,89 | -0,06R | €-45,85 |
| Rapida 1H V3 Filtered | 6 | 896 | 896 | 36,94% | 0,87 | -0,07R | €-590,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 6 | 670 | 670 | 39,25% | 0,93 | -0,03R | €-226,03 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 283 | 283 | 49,12% | 0,99 | -0,01R | €-14,92 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 1 | 287 | 287 | 38,68% | 0,96 | -0,02R | €-55,79 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 570 | 570 | 39,82% | 0,97 | -0,01R | €-80,75 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 3 | 596 | 596 | 34,73% | 0,80 | -0,10R | €-609,81 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 6 | 849 | 849 | 36,40% | 0,84 | -0,08R | €-672,03 |
| SHADOW_4H_WIDE | 31 | 327 | 327 | 23,85% | 0,83 | -0,11R | €-355,46 |
| SHADOW_BOLLINGER_MR_1H | 1 | 293 | 293 | 48,46% | 1,17 | 0,07R | €218,49 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 15 | 15 | 46,67% | 0,64 | -0,19R | €-28,10 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 2 | 2 | 50,00% | 2,26 | 0,67R | €13,50 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 9 | 9 | 77,78% | 3,40 | 0,60R | €54,38 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 17 | 17 | 29,41% | 0,32 | -0,54R | €-91,62 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 6 | 6 | 16,67% | 0,50 | -0,45R | €-26,75 |
| SHADOW_BTC_EMA_1H | 0 | 20 | 20 | 45,00% | 0,75 | -0,15R | €-30,58 |
| SHADOW_BTC_EMA_4H | 1 | 4 | 4 | 25,00% | 0,75 | -0,20R | €-8,17 |
| SHADOW_COMBO_ADAPTIVE | 10 | 712 | 712 | 38,62% | 1,01 | 0,01R | €46,43 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 443 | 443 | 39,73% | 1,07 | 0,04R | €159,30 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 9 | 781 | 781 | 41,74% | 1,02 | 0,01R | €79,93 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 10 | 653 | 653 | 40,89% | 0,96 | -0,02R | €-119,82 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 83 | 83 | 48,19% | 1,44 | 0,18R | €150,44 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 83 | 83 | 42,17% | 1,43 | 0,18R | €149,23 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 6 | 227 | 227 | 36,12% | 0,99 | -0,00R | €-8,16 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 250 | 250 | 40,00% | 1,04 | 0,02R | €41,69 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 109 | 109 | 48,62% | 1,23 | 0,10R | €108,65 |
| SHADOW_COMBO_SCANNER | 6 | 445 | 445 | 37,98% | 1,12 | 0,07R | €289,71 |
| SHADOW_COMBO_TREND | 10 | 588 | 588 | 35,37% | 1,00 | -0,00R | €-2,86 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 13 | 13 | 61,54% | 1,77 | 0,27R | €34,65 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 17 | 17 | 35,29% | 0,45 | -0,39R | €-66,91 |
| SHADOW_DOGE_EMA_1H | 0 | 28 | 28 | 28,57% | 0,42 | -0,41R | €-114,08 |
| SHADOW_DONCHIAN_1H | 6 | 313 | 313 | 33,55% | 0,89 | -0,07R | €-210,61 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 6 | 243 | 243 | 35,80% | 0,90 | -0,06R | €-145,53 |
| SHADOW_EMA_TREND_1H | 11 | 596 | 596 | 35,74% | 1,01 | 0,01R | €45,67 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 23 | 23 | 34,78% | 0,59 | -0,30R | €-67,99 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 15 | 15 | 60,00% | 1,86 | 0,32R | €47,90 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 22 | 22 | 27,27% | 0,43 | -0,46R | €-101,74 |
| SHADOW_ETH_EMA_1H | 1 | 32 | 32 | 37,50% | 0,54 | -0,31R | €-100,57 |
| SHADOW_ETH_EMA_4H | 1 | 6 | 6 | 33,33% | 0,46 | -0,38R | €-22,83 |
| SHADOW_GLOBAL_PURE | 0 | 14 | 14 | 42,86% | 0,90 | -0,07R | €-9,14 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 289 | 289 | 33,91% | 1,08 | 0,05R | €134,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 5 | 546 | 546 | 66,30% | 1,38 | 0,12R | €659,67 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 254 | 254 | 33,46% | 1,06 | 0,04R | €98,94 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 265 | 265 | 32,08% | 1,05 | 0,03R | €81,94 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 3 | 183 | 183 | 32,24% | 1,00 | -0,00R | €-3,51 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 278 | 278 | 33,09% | 1,03 | 0,02R | €60,89 |
| Forza relativa 1H V1 | 16 | 713 | 713 | 32,12% | 0,93 | -0,04R | €-274,57 |
| Forza relativa 1H V2 | 8 | 294 | 274 | 39,12% | 1,24 | 0,12R | €350,82 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 4 | 230 | 230 | 26,96% | 0,52 | -0,27R | €-627,28 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 4 | 230 | 230 | 26,96% | 0,52 | -0,27R | €-627,28 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 4 | 230 | 230 | 26,96% | 0,52 | -0,27R | €-627,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 4 | 262 | 262 | 29,39% | 0,67 | -0,18R | €-472,57 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 4 | 270 | 270 | 52,59% | 0,77 | -0,10R | €-274,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 4 | 243 | 243 | 51,44% | 0,69 | -0,14R | €-339,89 |
| SHADOW_SCANNER_TOP10_LONG | 7 | 437 | 437 | 39,36% | 1,08 | 0,04R | €168,65 |
| SHADOW_SCANNER_TOP15_LONG | 7 | 438 | 438 | 39,50% | 1,08 | 0,04R | €165,71 |
| SHADOW_SCANNER_TOP20_LONG | 7 | 438 | 438 | 39,50% | 1,08 | 0,04R | €165,71 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 431 | 431 | 37,59% | 1,14 | 0,07R | €309,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 3 | 155 | 155 | 30,32% | 0,76 | -0,14R | €-219,47 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 3 | 316 | 316 | 32,91% | 0,89 | -0,06R | €-183,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 2 | 331 | 331 | 43,81% | 1,12 | 0,05R | €170,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 2 | 279 | 279 | 34,41% | 0,97 | -0,02R | €-44,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 4 | 427 | 427 | 44,96% | 1,20 | 0,08R | €352,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 4 | 351 | 351 | 37,89% | 1,13 | 0,07R | €231,60 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 5 | 479 | 479 | 44,05% | 1,11 | 0,05R | €221,67 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 6 | 379 | 379 | 36,41% | 1,07 | 0,04R | €145,35 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 6 | 356 | 356 | 35,96% | 1,11 | 0,05R | €192,16 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 476 | 476 | 39,08% | 1,15 | 0,08R | €360,96 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 32 | 32 | 37,50% | 0,82 | -0,12R | €-39,74 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 9 | 9 | 66,67% | 2,54 | 0,54R | €48,91 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 24 | 24 | 45,83% | 0,79 | -0,12R | €-29,47 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 5 | 5 | 60,00% | 1,99 | 0,41R | €20,58 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 26 | 26 | 46,15% | 1,07 | 0,04R | €10,49 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 7 | 7 | 42,86% | 1,26 | 0,16R | €10,86 |
| SHADOW_SOL_EMA_1H | 0 | 30 | 30 | 40,00% | 0,99 | -0,01R | €-2,44 |
| SHADOW_SOL_EMA_4H | 1 | 10 | 10 | 40,00% | 0,85 | -0,10R | €-9,83 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 2 | 75 | 75 | 32,00% | 0,61 | -0,22R | €-162,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 3 | 148 | 148 | 47,30% | 1,34 | 0,15R | €217,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 118 | 118 | 33,90% | 0,63 | -0,19R | €-227,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,71 | -0,15R | €-28,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 57 | 57 | 35,09% | 1,17 | 0,07R | €41,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 55 | 55 | 20,00% | 0,46 | -0,27R | €-146,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 2 | 69 | 69 | 31,88% | 0,49 | -0,31R | €-213,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 3 | 129 | 129 | 46,51% | 1,38 | 0,16R | €201,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 111 | 111 | 33,33% | 0,54 | -0,24R | €-269,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,69 | -0,17R | €-30,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 56 | 56 | 35,71% | 1,25 | 0,10R | €57,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 53 | 53 | 20,75% | 0,35 | -0,33R | €-174,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 10 | 10 | 50,00% | 0,87 | -0,07R | €-7,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 1 | 56 | 56 | 55,36% | 1,34 | 0,15R | €86,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 68 | 68 | 39,71% | 0,51 | -0,31R | €-208,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 35 | 35 | 57,14% | 1,45 | 0,17R | €60,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 40 | 40 | 45,00% | 0,87 | -0,06R | €-24,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,98 | -0,01R | €-0,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 58 | 58 | 43,10% | 1,24 | 0,11R | €63,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 71 | 71 | 33,80% | 0,50 | -0,28R | €-201,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 35 | 35 | 34,29% | 1,25 | 0,09R | €32,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 1 | 39 | 39 | 28,21% | 0,83 | -0,07R | €-25,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 35,71% | 0,66 | -0,14R | €-40,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 3 | 175 | 175 | 41,14% | 1,04 | 0,02R | €33,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 88 | 88 | 35,23% | 0,68 | -0,17R | €-151,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 48 | 48 | 35,42% | 1,37 | 0,14R | €65,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 1 | 58 | 58 | 31,03% | 0,78 | -0,10R | €-58,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 37,04% | 0,53 | -0,21R | €-55,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 3 | 156 | 156 | 42,31% | 1,13 | 0,06R | €95,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 77 | 77 | 36,36% | 0,59 | -0,21R | €-159,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 47 | 47 | 36,17% | 1,43 | 0,15R | €72,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 1 | 54 | 54 | 31,48% | 0,59 | -0,18R | €-98,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 128 | 128 | 35,16% | 0,73 | -0,14R | €-174,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 2 | 29 | 29 | 24,14% | 0,29 | -0,53R | €-154,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 64 | 64 | 35,94% | 0,89 | -0,06R | €-38,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 112 | 112 | 33,93% | 0,71 | -0,15R | €-168,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 38 | 38 | 26,32% | 0,88 | -0,06R | €-21,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 2 | 49 | 49 | 26,53% | 0,43 | -0,35R | €-172,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 74 | 74 | 39,19% | 1,14 | 0,07R | €49,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 148 | 148 | 33,11% | 0,66 | -0,18R | €-272,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 57 | 57 | 28,07% | 0,93 | -0,03R | €-17,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 75 | 75 | 25,33% | 0,62 | -0,18R | €-138,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 2 | 47 | 47 | 25,53% | 0,36 | -0,41R | €-194,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 60 | 60 | 40,00% | 1,16 | 0,08R | €47,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 0 | 138 | 138 | 31,88% | 0,57 | -0,23R | €-312,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 56 | 56 | 28,57% | 0,89 | -0,05R | €-26,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 71 | 71 | 25,35% | 0,48 | -0,26R | €-183,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 35,71% | 0,66 | -0,14R | €-40,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 3 | 176 | 176 | 41,48% | 1,06 | 0,03R | €52,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 88 | 88 | 37,50% | 0,80 | -0,10R | €-91,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 48 | 48 | 35,42% | 1,37 | 0,14R | €65,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 1 | 58 | 58 | 31,03% | 0,78 | -0,10R | €-58,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 111 | 111 | 38,74% | 0,63 | -0,19R | €-206,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 2 | 210 | 210 | 43,33% | 1,11 | 0,04R | €93,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 164 | 164 | 37,80% | 0,83 | -0,08R | €-124,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 32 | 32 | 34,38% | 0,58 | -0,23R | €-73,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 74 | 74 | 45,95% | 1,41 | 0,13R | €95,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 86 | 86 | 41,86% | 0,85 | -0,07R | €-56,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 28,57% | 0,39 | -0,45R | €-126,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 24 | 24 | 33,33% | 0,78 | -0,14R | €-33,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 50 | 50 | 40,00% | 0,55 | -0,26R | €-128,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 9 | 9 | 55,56% | 1,56 | 0,27R | €24,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 26 | 26 | 19,23% | 0,32 | -0,48R | €-124,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 2 | 93 | 93 | 27,96% | 0,49 | -0,28R | €-264,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 3 | 186 | 186 | 40,86% | 1,08 | 0,04R | €69,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 144 | 144 | 32,64% | 0,64 | -0,19R | €-277,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 67 | 67 | 34,33% | 1,32 | 0,13R | €83,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 74 | 74 | 24,32% | 0,57 | -0,21R | €-158,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 2 | 93 | 93 | 27,96% | 0,49 | -0,28R | €-264,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 3 | 188 | 188 | 40,96% | 1,09 | 0,04R | €79,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 145 | 145 | 32,41% | 0,63 | -0,20R | €-287,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 67 | 67 | 34,33% | 1,32 | 0,13R | €83,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 74 | 74 | 24,32% | 0,57 | -0,21R | €-158,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 87 | 87 | 28,74% | 0,43 | -0,33R | €-285,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 3 | 165 | 165 | 41,82% | 1,13 | 0,06R | €103,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 0 | 136 | 136 | 30,88% | 0,50 | -0,27R | €-363,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 28 | 28 | 25,00% | 0,63 | -0,20R | €-56,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 66 | 66 | 34,85% | 1,37 | 0,14R | €92,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 70 | 70 | 24,29% | 0,41 | -0,30R | €-208,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 2 | 28 | 28 | 28,57% | 0,71 | -0,16R | €-44,58 |
| MAIN | ALT_ROTATION_UP | 9 | 82 | 82 | 30,49% | 0,65 | -0,22R | €-178,05 |
| MAIN | RANGE | 0 | 77 | 77 | 22,08% | 0,65 | -0,22R | €-165,89 |
| MAIN | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 3 | 38 | 38 | 26,32% | 0,70 | -0,19R | €-71,12 |
| MAIN | TREND_DOWN | 1 | 46 | 46 | 28,26% | 0,79 | -0,12R | €-57,38 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 4 | 40 | 40 | 30,00% | 1,01 | 0,00R | €1,45 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 22 | 22 | 45,45% | 1,09 | 0,04R | €7,83 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 91 | 91 | 26,37% | 0,52 | -0,30R | €-272,37 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 5 | 197 | 197 | 43,65% | 1,14 | 0,07R | €138,51 |
| Bilanciata 1H V1 | RANGE | 0 | 180 | 180 | 39,44% | 1,05 | 0,03R | €49,57 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 46 | 46 | 26,09% | 0,50 | -0,34R | €-156,31 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 3 | 102 | 102 | 37,25% | 1,17 | 0,08R | €84,42 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 2 | 114 | 114 | 29,82% | 0,89 | -0,06R | €-62,97 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 2 | 107 | 90 | 50,47% | 1,68 | 0,29R | €305,59 |
| Bilanciata 1H V2 | RANGE | 0 | 130 | 117 | 34,62% | 0,83 | -0,10R | €-127,97 |
| Bilanciata 1H V2 | TRANSITION | 3 | 85 | 73 | 40,00% | 1,38 | 0,18R | €152,65 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 68 | 68 | 27,94% | 0,50 | -0,32R | €-215,33 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 4 | 113 | 113 | 45,13% | 1,41 | 0,20R | €225,09 |
| Bilanciata 1H V3 Filtered | RANGE | 0 | 124 | 124 | 40,32% | 1,07 | 0,03R | €40,92 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,56 | -0,28R | €-50,80 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 55 | 55 | 34,55% | 1,07 | 0,03R | €17,93 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 66 | 66 | 31,82% | 1,11 | 0,06R | €36,83 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 57 | 57 | 24,56% | 0,32 | -0,44R | €-248,70 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 111 | 111 | 45,95% | 1,47 | 0,22R | €246,09 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 0 | 102 | 102 | 38,24% | 0,86 | -0,07R | €-75,24 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 31,25% | 0,69 | -0,19R | €-29,97 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 47 | 47 | 34,04% | 1,06 | 0,03R | €12,25 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 2 | 45 | 45 | 26,67% | 0,89 | -0,05R | €-24,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 29,41% | 0,73 | -0,13R | €-22,62 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 79 | 79 | 45,57% | 1,00 | 0,00R | €0,76 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 51 | 51 | 41,18% | 0,97 | -0,01R | €-6,96 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,70 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 29 | 29 | 44,83% | 1,30 | 0,13R | €37,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 1 | 53 | 53 | 33,96% | 0,93 | -0,03R | €-14,85 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 47 | 47 | 34,04% | 0,88 | -0,06R | €-26,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 1 | 84 | 84 | 44,05% | 1,09 | 0,04R | €35,66 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 0 | 155 | 155 | 35,48% | 0,78 | -0,11R | €-177,52 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 1 | 65 | 65 | 41,54% | 1,20 | 0,08R | €48,90 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 1 | 80 | 80 | 30,00% | 0,83 | -0,07R | €-58,47 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 65 | 65 | 30,77% | 0,70 | -0,17R | €-108,97 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 85 | 85 | 44,71% | 1,13 | 0,06R | €49,55 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 0 | 185 | 185 | 39,46% | 0,96 | -0,02R | €-32,33 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 67 | 67 | 43,28% | 1,32 | 0,12R | €78,59 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 1 | 96 | 96 | 29,17% | 0,72 | -0,14R | €-130,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 128 | 128 | 30,47% | 0,61 | -0,23R | €-294,10 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 4 | 226 | 226 | 40,71% | 0,92 | -0,04R | €-92,09 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 0 | 213 | 213 | 37,09% | 0,83 | -0,09R | €-188,26 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 40 | 40 | 37,50% | 0,86 | -0,07R | €-29,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 93 | 93 | 41,94% | 1,37 | 0,14R | €125,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 1 | 111 | 111 | 28,83% | 0,72 | -0,14R | €-158,82 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 49 | 49 | 46,94% | 1,55 | 0,20R | €97,83 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 2 | 73 | 73 | 28,77% | 0,48 | -0,34R | €-245,65 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 133 | 133 | 45,86% | 1,19 | 0,08R | €111,27 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 119 | 119 | 42,02% | 1,06 | 0,03R | €37,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 41,18% | 0,87 | -0,07R | €-11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 54 | 54 | 40,74% | 1,32 | 0,12R | €63,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 2 | 63 | 63 | 28,57% | 0,65 | -0,19R | €-118,58 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 2 | 124 | 124 | 29,84% | 0,61 | -0,22R | €-276,58 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 4 | 229 | 229 | 41,05% | 1,05 | 0,02R | €55,55 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 195 | 195 | 34,87% | 0,80 | -0,11R | €-206,82 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 39 | 39 | 28,21% | 0,64 | -0,20R | €-78,08 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 86 | 86 | 39,53% | 1,47 | 0,18R | €150,95 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 100 | 100 | 22,00% | 0,51 | -0,26R | €-257,61 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 24 | 22 | 45,83% | 0,94 | -0,03R | €-7,95 |
| Rapida 1H V2 | RANGE | 0 | 44 | 36 | 40,91% | 0,84 | -0,08R | €-36,12 |
| Rapida 1H V2 | TRANSITION | 0 | 9 | 9 | 55,56% | 0,95 | -0,02R | €-1,77 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 121 | 121 | 29,75% | 0,53 | -0,28R | €-341,14 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 3 | 205 | 205 | 43,90% | 1,11 | 0,05R | €99,48 |
| Rapida 1H V3 Filtered | RANGE | 0 | 188 | 188 | 37,23% | 0,82 | -0,09R | €-176,31 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 34 | 34 | 38,24% | 0,87 | -0,07R | €-23,20 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 82 | 82 | 37,80% | 1,13 | 0,06R | €45,13 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 113 | 113 | 37,17% | 1,00 | -0,00R | €-0,47 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 60 | 60 | 36,67% | 0,90 | -0,05R | €-32,12 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 97 | 97 | 32,99% | 0,57 | -0,26R | €-252,51 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 162 | 162 | 48,77% | 1,31 | 0,13R | €204,19 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 149 | 149 | 38,26% | 0,88 | -0,06R | €-88,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 22 | 22 | 40,91% | 0,94 | -0,03R | €-6,30 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 60 | 60 | 40,00% | 1,14 | 0,06R | €35,63 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 73 | 73 | 30,14% | 0,71 | -0,15R | €-107,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 29,41% | 0,28 | -0,53R | €-89,36 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 1 | 62 | 62 | 58,06% | 1,26 | 0,11R | €69,04 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 83 | 83 | 43,37% | 0,86 | -0,08R | €-68,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 36 | 36 | 58,33% | 1,61 | 0,21R | €77,08 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 1 | 51 | 51 | 50,98% | 1,05 | 0,02R | €11,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 18,75% | 0,28 | -0,52R | €-83,03 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 63 | 63 | 44,44% | 1,14 | 0,06R | €38,90 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 86 | 86 | 40,70% | 0,94 | -0,03R | €-25,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 36 | 36 | 41,67% | 1,41 | 0,14R | €51,95 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 1 | 52 | 52 | 34,62% | 0,97 | -0,01R | €-5,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 38 | 38 | 26,32% | 0,35 | -0,38R | €-144,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 194 | 194 | 43,30% | 1,06 | 0,03R | €52,79 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 108 | 108 | 41,67% | 0,97 | -0,01R | €-15,59 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 53 | 53 | 41,51% | 1,31 | 0,12R | €61,93 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 72 | 72 | 34,72% | 0,90 | -0,05R | €-35,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 44,74% | 1,30 | 0,13R | €50,46 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 71 | 71 | 28,17% | 0,49 | -0,32R | €-229,14 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 79 | 79 | 41,77% | 1,05 | 0,02R | €18,18 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 0 | 190 | 190 | 38,42% | 0,87 | -0,07R | €-128,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 65 | 65 | 33,85% | 0,99 | -0,01R | €-3,67 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 99 | 99 | 32,32% | 0,80 | -0,11R | €-105,65 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 120 | 120 | 30,00% | 0,53 | -0,27R | €-329,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 204 | 204 | 43,14% | 1,06 | 0,03R | €58,35 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 186 | 186 | 37,10% | 0,80 | -0,10R | €-191,04 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,92 | -0,04R | €-13,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 77 | 77 | 37,66% | 1,16 | 0,06R | €47,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 96 | 96 | 31,25% | 0,76 | -0,13R | €-123,21 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 42,50% | 1,23 | 0,10R | €40,19 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 5 | 25 | 25 | 28,00% | 1,29 | 0,16R | €39,17 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 11 | 66 | 66 | 37,88% | 1,01 | 0,01R | €4,84 |
| SHADOW_4H_WIDE | RANGE | 2 | 73 | 73 | 15,07% | 0,62 | -0,26R | €-187,47 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 39 | 39 | 15,38% | 0,45 | -0,40R | €-156,04 |
| SHADOW_4H_WIDE | TREND_DOWN | 2 | 45 | 45 | 26,67% | 0,96 | -0,03R | €-11,28 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 40 | 40 | 22,50% | 0,95 | -0,03R | €-12,13 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 3 | 19 | 19 | 21,05% | 0,75 | -0,17R | €-31,47 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 28 | 28 | 42,86% | 0,90 | -0,05R | €-13,95 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 1 | 92 | 92 | 50,00% | 1,23 | 0,09R | €82,01 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 69 | 69 | 44,93% | 0,98 | -0,01R | €-6,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 60,00% | 2,25 | 0,41R | €41,08 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 15 | 15 | 60,00% | 2,13 | 0,41R | €60,85 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 41 | 41 | 43,90% | 0,92 | -0,04R | €-15,55 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 0,99 | -0,00R | €-0,60 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 0,83 | -0,08R | €-4,03 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,42R | €24,17 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 1,54 | 0,20R | €6,15 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 0,57 | -0,29R | €-14,53 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 50,00% | 2,52 | 0,82R | €16,32 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,33 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,46 | -0,30R | €-5,95 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,41R | €24,09 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 3 | 76 | 76 | 26,32% | 0,57 | -0,26R | €-194,57 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 4 | 163 | 163 | 43,56% | 1,15 | 0,08R | €126,52 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 149 | 149 | 42,28% | 1,00 | -0,00R | €-2,37 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 32 | 32 | 37,50% | 0,88 | -0,06R | €-19,15 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 79 | 79 | 41,77% | 1,41 | 0,18R | €144,06 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 75 | 75 | 34,67% | 0,89 | -0,05R | €-37,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 98 | 98 | 36,73% | 1,11 | 0,05R | €49,89 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 18,52% | 0,49 | -0,31R | €-84,75 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 155 | 155 | 43,23% | 1,11 | 0,06R | €93,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 75 | 75 | 49,33% | 1,31 | 0,14R | €108,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 2 | 42 | 42 | 45,24% | 2,11 | 0,33R | €138,78 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 57 | 57 | 29,82% | 0,66 | -0,16R | €-89,74 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 2 | 94 | 94 | 37,23% | 0,71 | -0,14R | €-132,16 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 3 | 186 | 186 | 39,78% | 1,00 | 0,00R | €1,47 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 148 | 148 | 41,89% | 1,16 | 0,07R | €105,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 38 | 38 | 42,11% | 0,80 | -0,09R | €-32,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 2 | 69 | 69 | 47,83% | 1,31 | 0,12R | €83,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 98 | 98 | 36,73% | 0,88 | -0,05R | €-46,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 100 | 100 | 50,00% | 1,29 | 0,12R | €120,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 3 | 76 | 76 | 26,32% | 0,59 | -0,24R | €-185,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 4 | 161 | 161 | 44,10% | 1,08 | 0,04R | €65,16 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 137 | 137 | 45,26% | 1,05 | 0,02R | €33,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 30 | 30 | 43,33% | 1,03 | 0,01R | €3,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 62 | 62 | 46,77% | 1,37 | 0,16R | €96,12 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 75 | 75 | 38,67% | 0,90 | -0,05R | €-33,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 77 | 77 | 37,66% | 0,76 | -0,11R | €-85,32 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 2 | 36 | 36 | 36,11% | 0,91 | -0,05R | €-17,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 29 | 29 | 55,17% | 1,83 | 0,27R | €79,31 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,69 | 0,49R | €88,88 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 2 | 36 | 36 | 36,11% | 0,90 | -0,06R | €-20,39 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 29 | 29 | 41,38% | 1,59 | 0,20R | €57,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 55,56% | 3,14 | 0,62R | €112,49 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,04 | -0,62R | €-111,61 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 2 | 69 | 69 | 43,48% | 1,09 | 0,05R | €33,25 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 42 | 42 | 38,10% | 1,02 | 0,01R | €4,16 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 2 | 29 | 29 | 34,48% | 0,98 | -0,01R | €-3,69 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 21 | 21 | 38,10% | 1,31 | 0,09R | €19,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 3 | 93 | 93 | 39,78% | 1,04 | 0,02R | €18,42 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 106 | 106 | 35,85% | 0,83 | -0,08R | €-82,72 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 22 | 22 | 27,27% | 0,47 | -0,29R | €-64,40 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 1,93 | 0,35R | €31,68 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 32 | 32 | 50,00% | 1,38 | 0,18R | €57,26 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 7 | 7 | 71,43% | 5,11 | 0,67R | €47,21 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 28 | 28 | 14,29% | 0,16 | -0,62R | €-174,50 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 4 | 123 | 123 | 43,09% | 1,24 | 0,13R | €160,85 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 84 | 84 | 46,43% | 1,45 | 0,21R | €179,30 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 2 | 60 | 60 | 43,33% | 1,81 | 0,34R | €202,88 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 66 | 66 | 30,30% | 1,05 | 0,03R | €17,07 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 3 | 57 | 57 | 31,58% | 0,63 | -0,22R | €-125,44 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 4 | 139 | 139 | 42,45% | 1,13 | 0,07R | €96,56 |
| SHADOW_COMBO_TREND | RANGE | 0 | 128 | 128 | 35,16% | 1,04 | 0,02R | €24,85 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 23 | 23 | 34,78% | 1,15 | 0,07R | €15,88 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 66 | 66 | 36,36% | 1,32 | 0,16R | €107,41 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 67 | 67 | 29,85% | 0,70 | -0,16R | €-107,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 76 | 76 | 30,26% | 1,08 | 0,04R | €28,08 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 0,63 | -0,27R | €-8,18 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 71,29 | 0,77R | €30,62 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 25,00% | 0,07 | -0,78R | €-31,00 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,19 | -0,64R | €-25,79 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,61 | -0,25R | €-17,63 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,13 | -0,61R | €-48,91 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,61R | €-42,76 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,97 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 43 | 43 | 23,26% | 0,46 | -0,41R | €-178,25 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 3 | 79 | 79 | 36,71% | 0,77 | -0,15R | €-120,51 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 65 | 65 | 32,31% | 1,02 | 0,01R | €8,90 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 28 | 28 | 39,29% | 1,47 | 0,23R | €64,33 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 23 | 23 | 52,17% | 1,69 | 0,35R | €80,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 33 | 33 | 21,21% | 0,30 | -0,57R | €-186,73 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 3 | 71 | 71 | 39,44% | 0,84 | -0,10R | €-70,09 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 0 | 45 | 45 | 33,33% | 0,98 | -0,01R | €-6,16 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 21 | 21 | 47,62% | 2,13 | 0,45R | €93,60 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 58,82% | 2,03 | 0,44R | €75,25 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 3 | 60 | 60 | 30,00% | 0,56 | -0,27R | €-163,20 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 4 | 138 | 138 | 44,20% | 1,22 | 0,12R | €158,88 |
| SHADOW_EMA_TREND_1H | RANGE | 0 | 125 | 125 | 35,20% | 1,08 | 0,04R | €49,33 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 64 | 64 | 34,38% | 1,16 | 0,09R | €56,98 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 80 | 80 | 28,75% | 0,95 | -0,03R | €-23,01 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,65 | -0,26R | €-23,12 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,74 | -0,17R | €-8,58 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 7 | 7 | 57,14% | 2,62 | 0,50R | €34,85 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,23 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,29 | -0,66R | €-46,36 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,56 | -0,33R | €-19,66 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,98 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 50,00% | 0,89 | -0,06R | €-7,18 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 1 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,57 | -0,30R | €-8,95 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 6 | 6 | 33,33% | 0,68 | -0,24R | €-14,10 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 31,82% | 0,95 | -0,03R | €-7,14 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 2 | 39 | 39 | 35,90% | 1,10 | 0,06R | €24,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 0 | 81 | 81 | 32,10% | 1,04 | 0,02R | €18,15 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 4 | 35 | 35 | 45,71% | 1,89 | 0,42R | €146,99 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 63 | 63 | 28,57% | 0,81 | -0,13R | €-82,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 33 | 33 | 54,55% | 0,92 | -0,03R | €-11,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 91 | 91 | 73,63% | 1,86 | 0,22R | €199,25 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 149 | 149 | 66,44% | 1,46 | 0,14R | €213,68 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 3 | 80 | 80 | 72,50% | 1,79 | 0,20R | €157,17 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 115 | 115 | 61,74% | 1,05 | 0,02R | €20,99 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,95 | -0,03R | €-6,33 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 0 | 82 | 82 | 34,15% | 1,14 | 0,08R | €66,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 5 | 35 | 35 | 40,00% | 1,46 | 0,25R | €86,43 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 71 | 71 | 26,76% | 0,74 | -0,19R | €-134,46 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 37,50% | 1,39 | 0,23R | €36,29 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 42 | 42 | 30,95% | 0,88 | -0,09R | €-36,93 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 0 | 74 | 74 | 31,08% | 1,15 | 0,09R | €65,91 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 4 | 31 | 31 | 41,94% | 1,67 | 0,34R | €103,99 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 60 | 60 | 23,33% | 0,65 | -0,26R | €-156,30 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,17 | -0,72R | €-94,10 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 59 | 59 | 35,59% | 1,11 | 0,07R | €41,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 3 | 28 | 28 | 46,43% | 2,20 | 0,50R | €139,19 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 50 | 50 | 32,00% | 0,96 | -0,03R | €-12,66 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,88 | -0,08R | €-16,20 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 2 | 41 | 41 | 36,59% | 1,12 | 0,08R | €31,71 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 0 | 77 | 77 | 33,77% | 1,14 | 0,08R | €61,59 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 4 | 34 | 34 | 41,18% | 1,55 | 0,29R | €97,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 63 | 63 | 23,81% | 0,63 | -0,27R | €-171,08 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 4 | 71 | 71 | 28,17% | 0,57 | -0,26R | €-186,96 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 4 | 161 | 161 | 40,99% | 1,15 | 0,08R | €131,67 |
| Forza relativa 1H V1 | RANGE | 1 | 169 | 169 | 30,18% | 0,81 | -0,10R | €-171,44 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 28 | 28 | 28,57% | 0,53 | -0,25R | €-70,96 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 4 | 75 | 75 | 36,00% | 1,38 | 0,19R | €140,17 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 75 | 75 | 28,00% | 0,87 | -0,07R | €-51,18 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 1 | 98 | 98 | 25,51% | 0,91 | -0,05R | €-44,31 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 27,27% | 0,81 | -0,12R | €-39,63 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 33 | 32 | 39,39% | 0,73 | -0,13R | €-44,43 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 2 | 58 | 53 | 48,28% | 1,69 | 0,32R | €186,14 |
| Forza relativa 1H V2 | RANGE | 1 | 74 | 71 | 33,78% | 0,88 | -0,07R | €-50,90 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 2 | 43 | 38 | 39,53% | 1,71 | 0,33R | €140,20 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 35 | 34 | 28,57% | 0,95 | -0,02R | €-7,36 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 38 | 35 | 47,37% | 1,88 | 0,38R | €145,99 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 48 | 48 | 20,83% | 0,30 | -0,47R | €-227,81 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 0 | 61 | 61 | 22,95% | 0,33 | -0,39R | €-236,25 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 23 | 23 | 43,48% | 1,19 | 0,10R | €23,62 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 48 | 48 | 20,83% | 0,30 | -0,47R | €-227,81 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 0 | 61 | 61 | 22,95% | 0,33 | -0,39R | €-236,25 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 23 | 23 | 43,48% | 1,19 | 0,10R | €23,62 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 48 | 48 | 20,83% | 0,30 | -0,47R | €-227,81 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 0 | 61 | 61 | 22,95% | 0,33 | -0,39R | €-236,25 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 23 | 23 | 43,48% | 1,19 | 0,10R | €23,62 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 43 | 43 | 27,91% | 0,57 | -0,26R | €-110,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 46,67% | 1,70 | 0,29R | €44,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 74 | 74 | 28,38% | 0,61 | -0,21R | €-156,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,33 | 0,13R | €23,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 39 | 39 | 38,46% | 1,02 | 0,01R | €4,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 2 | 50 | 50 | 50,00% | 0,56 | -0,20R | €-102,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 45,45% | 1,12 | 0,06R | €6,29 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 0 | 66 | 66 | 53,03% | 0,64 | -0,16R | €-104,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 22 | 22 | 63,64% | 1,42 | 0,16R | €34,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 30 | 30 | 60,00% | 1,46 | 0,20R | €58,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 2 | 42 | 42 | 47,62% | 0,42 | -0,28R | €-116,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,55 | 0,22R | €28,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 0 | 59 | 59 | 52,54% | 0,38 | -0,27R | €-159,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 60,00% | 1,23 | 0,10R | €19,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 29 | 29 | 62,07% | 1,60 | 0,24R | €70,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 23 | 23 | 26,09% | 0,62 | -0,22R | €-50,45 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 4 | 161 | 161 | 42,24% | 1,07 | 0,04R | €59,43 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 2 | 46 | 46 | 39,13% | 1,65 | 0,22R | €100,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 1 | 52 | 52 | 26,92% | 0,58 | -0,21R | €-107,39 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 23 | 23 | 26,09% | 0,62 | -0,22R | €-50,39 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 164 | 164 | 43,29% | 1,08 | 0,04R | €63,67 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 2 | 46 | 46 | 39,13% | 1,65 | 0,22R | €100,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 1 | 52 | 52 | 26,92% | 0,58 | -0,21R | €-107,39 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 23 | 23 | 26,09% | 0,62 | -0,22R | €-50,39 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 164 | 164 | 43,29% | 1,08 | 0,04R | €63,67 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 2 | 46 | 46 | 39,13% | 1,65 | 0,22R | €100,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 1 | 52 | 52 | 26,92% | 0,58 | -0,21R | €-107,39 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 26 | 26 | 15,38% | 0,18 | -0,59R | €-152,37 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 4 | 123 | 123 | 43,09% | 1,24 | 0,13R | €161,44 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 79 | 79 | 46,84% | 1,60 | 0,27R | €212,29 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 2 | 55 | 55 | 41,82% | 1,82 | 0,34R | €188,19 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 65 | 65 | 29,23% | 0,99 | -0,01R | €-3,64 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,05 | -0,75R | €-89,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 1 | 52 | 52 | 34,62% | 0,77 | -0,15R | €-75,79 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 23 | 23 | 47,83% | 2,22 | 0,43R | €100,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 50 | 50 | 28,00% | 0,86 | -0,07R | €-35,92 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 10,00% | 0,05 | -0,69R | €-138,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 66 | 66 | 33,33% | 0,79 | -0,13R | €-86,04 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,46 | 0,21R | €159,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 43 | 43 | 44,19% | 2,27 | 0,43R | €184,01 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 44 | 44 | 20,45% | 0,53 | -0,26R | €-115,59 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,28 | -0,33R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 38,33% | 0,95 | -0,02R | €-14,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 44 | 44 | 47,73% | 1,36 | 0,14R | €60,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 1 | 47 | 47 | 51,06% | 1,27 | 0,11R | €54,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 0,38 | -0,38R | €-18,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,07 | -0,66R | €-104,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 34,00% | 0,92 | -0,05R | €-24,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 40 | 40 | 37,50% | 1,72 | 0,28R | €112,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 1 | 36 | 36 | 22,22% | 0,63 | -0,20R | €-73,12 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,85R | €-51,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 26 | 26 | 34,62% | 0,57 | -0,20R | €-52,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 1 | 124 | 124 | 42,74% | 1,19 | 0,08R | €104,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 46 | 46 | 45,65% | 1,28 | 0,11R | €50,09 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 52 | 52 | 48,08% | 1,25 | 0,10R | €53,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 19,05% | 0,23 | -0,52R | €-109,25 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 2 | 102 | 102 | 45,10% | 1,40 | 0,21R | €210,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 2 | 41 | 41 | 36,59% | 1,62 | 0,25R | €102,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 41 | 41 | 21,95% | 0,67 | -0,18R | €-73,37 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 32 | 32 | 34,38% | 0,47 | -0,25R | €-81,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 2 | 143 | 143 | 41,96% | 1,04 | 0,02R | €23,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 81 | 81 | 46,91% | 1,52 | 0,20R | €162,96 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,61 | -0,16R | €-26,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 2 | 51 | 51 | 49,02% | 1,45 | 0,16R | €83,62 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 1 | 64 | 64 | 48,44% | 1,26 | 0,10R | €64,14 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 21,05% | 0,24 | -0,53R | €-100,94 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 123 | 123 | 42,28% | 1,24 | 0,13R | €160,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 0 | 70 | 70 | 44,29% | 1,49 | 0,23R | €162,79 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 2 | 43 | 43 | 41,86% | 2,01 | 0,36R | €156,51 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 49 | 49 | 20,41% | 0,56 | -0,24R | €-115,89 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 16,67% | 0,08 | -0,67R | €-121,41 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 117 | 117 | 41,88% | 1,26 | 0,14R | €163,07 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 65 | 65 | 43,08% | 1,53 | 0,26R | €169,81 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 2 | 37 | 37 | 40,54% | 2,51 | 0,47R | €173,66 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 47 | 47 | 21,28% | 0,57 | -0,22R | €-104,91 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 32 | 32 | 21,88% | 0,42 | -0,37R | €-118,78 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 3 | 127 | 127 | 41,73% | 1,11 | 0,06R | €73,52 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 81 | 81 | 49,38% | 1,55 | 0,24R | €194,78 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 2 | 59 | 59 | 40,68% | 1,64 | 0,25R | €147,01 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 83 | 83 | 36,14% | 1,13 | 0,06R | €49,73 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 60,00% | 2,05 | 0,45R | €45,46 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,75 | -0,18R | €-14,00 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 100,00% | ∞ | 1,14R | €34,32 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 75,00% | 1,91 | 0,24R | €9,76 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,41 | -0,45R | €-45,27 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,60 | -0,30R | €-18,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,51 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,16 | -0,75R | €-37,55 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 50,00% | 1,36 | 0,20R | €15,94 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 66,67% | 2,69 | 0,63R | €38,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,72R | €27,23 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,20 | 0,10R | €2,07 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 66,67% | 2,76 | 0,63R | €56,57 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 1,02 | 0,01R | €1,11 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 1,81 | 0,28R | €8,45 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-28T12:08:41+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **531**
- Scenari virtuali ancora attivi: **8919**
- Gruppi in attesa dell'uscita originale: **310**
- Gruppi con originale chiuso ma Shadow ancora attive: **221**
- Confronti completati: **416259**

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

Generato: 2026-08-28T12:09:46+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **416259**
- Valutazioni prodotte: **25566**
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

# Forward Exit Challengers — verifica pulita

Generato: 2026-08-28T12:14:27+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Operativo | Identità | Gross cert. | Net cert. | Pending | Gap | Conflict | Formal review NET | PF storico | PnL storico | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,16 | +€67,59 | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,01 | +€2,56 | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,11 | +€95,26 | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,09 | +€75,72 | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | 90 | 100 | 19 | 0 | 8 | 73 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,55 | +€846,28 | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | 38 | 51 | 11 | 0 | 9 | 30 | 1 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 5,77 | +€1.682,13 | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | 154 | 147 | 22 | 0 | 6 | 117 | 2 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,65 | +€1.253,39 | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 0,00 | €0,00 | COLLECTING |

## Regole di valutazione

- Il campione operativo resta esposto per continuità storica, ma non è il campione formale.
- La soglia 50 usa esclusivamente NET_CERTIFIED_CLOSED_PAIRS.
- P0C produce FORMAL_CERTIFIED_OUTCOME; Block-3 produce SIMULATION_RUNTIME_OUTCOME.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-28T12:05:54+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **55**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **628.58 R**
- Profitto virtuale mancato: **1101.45 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 232 | 0 | 15640.62 |
| DOWN_20 | 232 | 0 | 31281.23 |
| DOWN_30 | 232 | 0 | 46921.85 |
| DOWN_40 | 232 | 65 | 60272.48 |
| UP_10 | 73 | 0 | 5402.48 |
| UP_20 | 73 | 0 | 10804.96 |
| UP_30 | 73 | 0 | 16207.44 |
| UP_40 | 73 | 29 | 19718.03 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-28T12:05:17+00:00

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

Generato: 2026-08-28T12:14:34+00:00

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

Generato: 2026-08-28T12:14:35+00:00

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

Generato: 2026-08-28T12:14:35+00:00

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

Generato: 2026-08-28T12:14:35+00:00

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
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 23.6 | E | 119 | 1.72 | 0.333 | 14.44 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 23.4 | E | 151 | 1.44 | 0.200 | 16.35 |
| 3 | SHADOW_COMBO_ADAPTIVE | BASELINE | 22.1 | E | 157 | 1.37 | 0.175 | 14.19 |
| 4 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 20.9 | E | 37 | 1.91 | 0.422 | 4.71 |
| 5 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 20.1 | E | 196 | 1.18 | 0.088 | 30.08 |
| 6 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 19.9 | E | 226 | 1.21 | 0.099 | 25.70 |
| 7 | SHADOW_1H_FAST_V3 | BASELINE | 19.2 | E | 240 | 1.15 | 0.074 | 29.54 |
| 8 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | BASELINE | 18.7 | E | 159 | 1.11 | 0.057 | 22.70 |
| 9 | SHADOW_DONCHIAN_1H | BASELINE | 18.3 | E | 114 | 1.35 | 0.201 | 17.00 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | BASELINE | 18.0 | E | 165 | 1.06 | 0.031 | 23.64 |

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

Generato: 2026-08-28T12:14:35+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BULL_TREND**
- Righe di performance: **1098**
- Strategie preferite nel regime corrente: **20**
- Strategie da evitare nel regime corrente: **3**
- Memorie contestuali: **524**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.621 | 0.00 |
| 2 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | shadow-1h-fast-v3-no-esports-mfe-lock-v1 | SPECIALIST | 75.4 | 68 | 1.80 | 0.338 | 11.23 |
| 3 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | INSUFFICIENT | 75.0 | 6 | 5.10 | 0.770 | 1.05 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.8 | 12 | 4.37 | 0.378 | 1.07 |
| 5 | SHADOW_DOGE_BOLLINGER_1H | shadow-doge-bollinger-1h | INSUFFICIENT | 74.5 | 3 | 1.98 | 0.477 | 1.47 |
| 6 | SHADOW_SOL_ADAPTIVE_1H | shadow-sol-adaptive-1h | INSUFFICIENT | 72.8 | 7 | 2.58 | 0.503 | 1.17 |
| 7 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 72.7 | 5 | 3.47 | 0.591 | 1.20 |
| 8 | SHADOW_SOL_ADAPTIVE_4H | shadow-sol-adaptive-4h | INSUFFICIENT | 70.0 | 4 | 2.56 | 0.460 | 1.04 |
| 9 | SHADOW_SOL_EMA_4H | shadow-sol-ema-4h | INSUFFICIENT | 70.0 | 4 | 2.57 | 0.469 | 1.04 |
| 10 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | COMPATIBLE | 68.2 | 42 | 1.60 | 0.327 | 7.79 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-28T12:14:35+00:00

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

Generato: 2026-08-28T12:05:54+00:00

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
