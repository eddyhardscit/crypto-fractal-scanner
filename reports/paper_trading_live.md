# Paper trading automatico KuCoin

Generato: 2026-08-27T16:14:56+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-27T16:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-27T16:05:31+00:00 | 2026-08-27T16:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-27T15:45:00+00:00 | 2026-08-27T15:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-27T15:00:00+00:00 | 2026-08-27T15:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-27T12:00:00+00:00 | 2026-08-27T12:00:00+00:00 | 5,7 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida V3 NoHigh — Regime Guard | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Loss Cap 0,75R | ENA | 60m | LONG | 9,46 | 0,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — 50% a 0,75R | ENA | 60m | LONG | 9,46 | 0,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Breakeven 0,5R | ENA | 60m | LONG | 9,46 | 0,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | ENA | 60m | LONG | 9,46 | 0,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | ENA | 60m | LONG | 9,46 | 0,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | SOL | 60m | LONG | 5,57 | 0,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | ENA | 60m | LONG | 9,46 | 0,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 4H | SOL | 240m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Btc Ema 1H | BTC | 60m | LONG | 5,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | ENA | 60m | LONG | 9,46 | 5,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ENA | 240m | LONG | 8,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | SOL | 240m | LONG | 7,25 | 6,00 | 0,00 | READY | 5,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | TAO | 240m | LONG | 7,02 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | BTR | 240m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | ETH | 240m | LONG | 6,12 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | HYPE | 240m | LONG | 9,56 | 6,00 | 0,00 | RISK_GATE | 5,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | XRP | 240m | LONG | 6,28 | 6,00 | 0,00 | RISK_GATE | 5,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | ZEC | 240m | LONG | 5,82 | 6,00 | 0,18 | BELOW_SCORE | 5,7 min | D: n/a | W: n/a | peso 0 | Punteggio +5.82; soglia ±6.00; mancano 0.18 punti. |
| Principale 4H | BTC | 240m | LONG | 5,25 | 6,00 | 0,75 | BELOW_SCORE | 5,7 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +5.25; soglia ±6.00; mancano 0.75 punti. |
| Principale 4H | PEPE | 240m | LONG | 5,07 | 6,00 | 0,93 | BELOW_SCORE | 5,7 min | D: n/a | W: n/a | peso 0 | Punteggio +5.07; soglia ±6.00; mancano 0.93 punti. |
| Bilanciata 1H — LONG senza Range High Vol | ENA | 60m | LONG | 9,46 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ENA | 60m | LONG | 9,46 | 5,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | ENA | 60m | LONG | 9,46 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Long Only | ENA | 60m | LONG | 9,46 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.810,21 | -1,90% | €61,86 | €3.000,00 | 2,06% | 6 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2332 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.810,21 | €699,00 | €2.096,99 | €196,05 | €2,08 |
| TEST | Rapida score 6–7,5 — Cost Aware | 5 | €11.348,58 | €563,84 | €1.691,51 | €170,37 | €0,05 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.270,92 | €2.707,49 | €5.414,98 | €164,76 | €108,28 |
| TEST | Combo Trend — Side × Regime Guard | 6 | €11.119,56 | €2.095,77 | €4.191,54 | €114,63 | €25,24 |
| TEST | Scanner Top 5 Long 1H | 6 | €11.028,00 | €2.333,41 | €4.666,83 | €165,64 | €42,12 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.005,56 | €2.643,75 | €5.287,49 | €160,88 | €105,73 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.822,90 | €684,42 | €2.053,25 | €215,08 | €104,84 |
| TEST | Combo Adaptive — madre | 8 | €10.732,19 | €1.959,73 | €3.919,46 | €163,62 | €46,21 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.631,36 | €1.268,73 | €3.806,18 | €212,64 | €46,83 |
| TEST | Rapida V1 — senza PEPE | 6 | €10.611,47 | €1.346,56 | €4.039,69 | €211,87 | €22,31 |
| TEST | Rapida 1H V3 Filtered — madre | 6 | €10.563,05 | €1.260,58 | €3.781,73 | €211,28 | €46,53 |
| TEST | Combo Adaptive — Long Only | 6 | €10.468,80 | €3.422,27 | €6.844,54 | €157,24 | €39,93 |
| TEST | Combo Adaptive — Side × Regime Guard | 6 | €10.407,97 | €1.019,07 | €2.038,14 | €155,21 | €-13,10 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 2 | €10.395,56 | €2.110,93 | €6.332,78 | €49,48 | €28,31 |
| TEST | Rapida V3 NoHigh — Regime Guard | 5 | €10.386,05 | €1.539,54 | €4.618,63 | €203,94 | €12,36 |
| TEST | Rapida V1 — target pieno 2R | 7 | €10.373,91 | €1.275,08 | €3.825,23 | €108,75 | €56,94 |
| TEST | Sol Donchian 1H | 1 | €10.307,36 | €736,80 | €2.210,40 | €51,45 | €17,96 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 2 | €10.284,85 | €1.156,73 | €3.470,19 | €102,77 | €17,69 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.262,43 | €1.057,57 | €2.115,14 | €205,57 | €-16,98 |
| TEST | Sol Adaptive 4H | 1 | €10.260,53 | €367,30 | €734,59 | €0,00 | €67,12 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.251,96 | €2.164,33 | €4.328,67 | €153,99 | €39,04 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.232,83 | €650,72 | €1.952,17 | €0,00 | €51,87 |
| TEST | Sol Donchian 4H | 1 | €10.223,73 | €449,62 | €899,24 | €50,98 | €27,80 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 6 | €10.205,98 | €1.285,93 | €3.857,80 | €203,76 | €17,34 |
| TEST | Scanner Top10 Long | 6 | €10.199,07 | €2.918,27 | €5.836,54 | €152,54 | €78,77 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 6 | €10.168,83 | €2.359,25 | €4.718,49 | €153,24 | €45,10 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 6 | €10.162,88 | €2.357,87 | €4.715,73 | €153,15 | €45,08 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.161,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.127,70 | €395,27 | €790,53 | €0,00 | €72,23 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €10.087,29 | €641,47 | €1.924,41 | €0,00 | €51,13 |
| TEST | Combo Adaptive — parziale 1R | 7 | €10.080,64 | €1.992,30 | €3.984,61 | €149,83 | €0,09 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €10.076,50 | €1.233,25 | €3.699,74 | €199,99 | €-18,25 |
| TEST | Btc Adaptive 4H | 1 | €10.069,37 | €648,94 | €1.297,88 | €50,35 | €0,33 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.027,94 | €775,58 | €1.551,16 | €50,15 | €-1,02 |
| TEST | Btc Ema 4H | 1 | €10.018,52 | €704,37 | €1.408,74 | €50,10 | €0,36 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.014,15 | €2.206,92 | €6.620,75 | €98,97 | €89,66 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €10.013,50 | €35,97 | €107,92 | €2,93 | €-1,07 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Btc Donchian 4H | 1 | €9.964,92 | €700,60 | €1.401,20 | €49,83 | €0,36 |
| TEST | Eth Ema 4H | 1 | €9.964,87 | €487,73 | €975,47 | €0,00 | €54,76 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 6 | €9.952,00 | €1.253,93 | €3.761,80 | €198,69 | €16,91 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.929,90 | €478,97 | €957,94 | €49,65 | €-0,19 |
| TEST | Doge Donchian 1H | 0 | €9.924,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.912,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.873,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.854,20 | €2.774,68 | €5.549,37 | €147,36 | €31,31 |
| TEST | Eth Ema 1H | 0 | €9.852,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 6 | €9.850,78 | €1.229,15 | €3.687,45 | €197,03 | €-17,96 |
| TEST | Combo Scanner | 6 | €9.849,89 | €2.081,83 | €4.163,65 | €147,95 | €37,45 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 5 | €9.832,28 | €2.148,39 | €4.296,78 | €50,80 | €56,46 |
| TEST | Btc Ema 1H | 1 | €9.830,93 | €1.138,16 | €3.414,47 | €49,17 | €-0,68 |
| TEST | Scanner Top15 Long | 8 | €9.829,54 | €2.307,79 | €4.615,59 | €147,48 | €45,25 |
| TEST | Scanner Top20 Long | 8 | €9.829,54 | €2.307,79 | €4.615,59 | €147,48 | €45,25 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.797,48 | €790,73 | €2.372,19 | €195,36 | €1,94 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.787,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.786,34 | €2.830,12 | €5.660,24 | €194,50 | €49,34 |
| TEST | Rapida V3 — Long Only | 6 | €9.769,83 | €1.192,91 | €3.578,72 | €194,15 | €44,70 |
| TEST | Sol Bollinger 1H | 0 | €9.768,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 6 | €9.719,08 | €1.622,93 | €4.868,79 | €143,48 | €87,26 |
| TEST | Eth Donchian 1H | 0 | €9.709,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.702,44 | €4.007,77 | €8.015,54 | €194,05 | €128,76 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.685,96 | €772,39 | €2.317,17 | €96,69 | €-16,41 |
| TEST | Global Confluence puro 1H | 0 | €9.679,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.628,51 | €1.805,24 | €3.610,48 | €96,68 | €57,02 |
| TEST | Top 5 + BTC — solo MFE | 6 | €9.610,71 | €2.028,96 | €4.057,91 | €144,35 | €36,60 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.574,07 | €749,55 | €2.248,64 | €95,52 | €-8,72 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 6 | €9.553,63 | €3.047,78 | €6.095,57 | €191,08 | €41,37 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 6 | €9.543,47 | €3.044,54 | €6.089,09 | €190,88 | €41,33 |
| TEST | Top 5 + BTC — Guard | 5 | €9.541,91 | €1.984,42 | €3.968,84 | €143,50 | €23,09 |
| TEST | Master Adaptive V1 | 6 | €9.506,56 | €3.032,77 | €6.065,53 | €190,14 | €41,17 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.506,47 | €2.941,55 | €5.883,10 | €190,13 | €27,13 |
| TEST | Bilanciata 1H V2 | 5 | €9.506,16 | €1.755,31 | €5.265,92 | €142,32 | €61,60 |
| TEST | Bilanciata V3 · LONG only | 4 | €9.469,13 | €2.080,34 | €6.241,03 | €93,17 | €84,57 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 6 | €9.389,19 | €3.459,59 | €6.919,18 | €187,79 | €47,86 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €9.381,20 | €2.424,72 | €4.849,44 | €92,56 | €32,56 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.380,25 | €2.992,47 | €5.984,94 | €187,62 | €40,62 |
| TEST | Combo Trend | 6 | €9.373,59 | €1.829,04 | €3.658,08 | €94,79 | €35,84 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 5 | €9.320,00 | €1.938,27 | €3.876,54 | €140,16 | €22,55 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.256,81 | €1.267,77 | €2.535,55 | €140,48 | €-0,10 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.253,99 | €1.563,67 | €3.127,35 | €49,04 | €33,96 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 6 | €9.202,07 | €1.609,46 | €3.218,91 | €183,37 | €5,80 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €9.092,72 | €1.523,94 | €3.047,88 | €45,63 | €33,36 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.949,35 | €2.281,92 | €4.563,83 | €133,76 | €3,06 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €8.922,97 | €2.306,28 | €4.612,56 | €88,04 | €30,97 |
| TEST | Combo Mean Reversion | 0 | €8.918,97 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.810,21 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.348,58 | €1.349,67 | 150 | 150 | 54,00% | 1,46 | €9,00 | 5,23% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.270,92 | €1.165,39 | 108 | 108 | 47,22% | 1,48 | €10,79 | 6,11% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.119,56 | €1.096,81 | 115 | 115 | 53,91% | 1,53 | €9,54 | 6,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.028,00 | €988,71 | 143 | 143 | 47,55% | 1,36 | €6,91 | 8,85% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.005,56 | €902,51 | 76 | 76 | 46,05% | 1,58 | €11,88 | 6,11% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.822,90 | €719,92 | 36 | 36 | 52,78% | 2,02 | €20,00 | 3,82% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.732,19 | €689,31 | 150 | 150 | 46,67% | 1,28 | €4,60 | 7,91% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.631,36 | €586,93 | 193 | 193 | 50,78% | 1,19 | €3,04 | 9,50% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.611,47 | €591,69 | 221 | 221 | 46,61% | 1,14 | €2,68 | 7,45% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.563,05 | €518,91 | 237 | 237 | 45,15% | 1,12 | €2,19 | 9,48% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.468,80 | €432,98 | 124 | 124 | 46,77% | 1,16 | €3,49 | 7,78% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.407,97 | €423,24 | 116 | 116 | 48,28% | 1,18 | €3,65 | 8,68% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.395,56 | €371,05 | 58 | 58 | 53,45% | 1,30 | €6,40 | 4,50% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.386,05 | €376,45 | 77 | 77 | 49,35% | 1,23 | €4,89 | 5,24% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.373,91 | €319,27 | 229 | 229 | 40,61% | 1,08 | €1,39 | 6,56% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.307,36 | €290,73 | 14 | 14 | 57,14% | 2,18 | €20,77 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.284,85 | €269,24 | 48 | 43 | 47,92% | 1,23 | €5,61 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Ampia 4H | Confluenza trend | €10.262,43 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.260,53 | €193,98 | 7 | 7 | 57,14% | 2,72 | €27,71 | 1,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.251,96 | €215,55 | 129 | 129 | 44,19% | 1,08 | €1,67 | 11,27% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Ema 1H | Trend following EMA | €10.232,83 | €182,13 | 15 | 15 | 46,67% | 1,47 | €12,14 | 3,33% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.223,73 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.205,98 | €190,95 | 146 | 146 | 43,84% | 1,06 | €1,31 | 7,10% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.199,07 | €123,81 | 131 | 131 | 48,09% | 1,05 | €0,95 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.168,83 | €126,56 | 107 | 107 | 42,06% | 1,05 | €1,18 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.162,88 | €120,64 | 111 | 111 | 42,34% | 1,05 | €1,09 | 12,06% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.161,45 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,04% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Ema 4H | Trend following EMA | €10.127,70 | €56,08 | 8 | 8 | 37,50% | 1,26 | €7,01 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.087,29 | €37,32 | 16 | 16 | 43,75% | 1,08 | €2,33 | 4,59% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.080,64 | €82,92 | 154 | 154 | 45,45% | 1,03 | €0,54 | 8,69% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.076,50 | €96,97 | 161 | 161 | 44,10% | 1,03 | €0,60 | 10,60% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.069,37 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.027,94 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Btc Ema 4H | Trend following EMA | €10.018,52 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.014,15 | €-71,54 | 158 | 158 | 41,77% | 0,98 | €-0,45 | 9,12% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.013,50 | €14,63 | 72 | 72 | 43,06% | 1,01 | €0,20 | 4,16% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
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
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.964,92 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.964,87 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.952,00 | €-62,65 | 110 | 110 | 42,73% | 0,97 | €-0,57 | 7,10% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.929,90 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,73% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,84 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.912,24 | €-87,76 | 39 | 39 | 46,15% | 0,91 | €-2,25 | 4,21% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.873,49 | €-126,51 | 14 | 14 | 42,86% | 0,72 | €-9,04 | 3,14% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.854,20 | €-173,78 | 62 | 62 | 48,39% | 0,89 | €-2,80 | 5,38% |
| TEST | Eth Ema 1H | Trend following EMA | €9.852,76 | €-147,24 | 19 | 19 | 42,11% | 0,77 | €-7,75 | 4,80% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.850,78 | €-129,05 | 128 | 128 | 44,53% | 0,95 | €-1,01 | 7,10% |
| TEST | Combo Scanner | Combo Scanner | €9.849,89 | €-185,03 | 134 | 134 | 44,03% | 0,94 | €-1,38 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.832,28 | €-221,51 | 115 | 109 | 41,74% | 0,93 | €-1,93 | 10,88% |
| TEST | Btc Ema 1H | Trend following EMA | €9.830,93 | €-166,34 | 13 | 13 | 30,77% | 0,61 | €-12,80 | 1,94% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.829,54 | €-212,91 | 128 | 128 | 47,66% | 0,91 | €-1,66 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.829,54 | €-212,91 | 128 | 128 | 47,66% | 0,91 | €-1,66 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.797,48 | €-202,92 | 207 | 207 | 43,96% | 0,95 | €-0,98 | 9,00% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.787,56 | €-212,44 | 39 | 39 | 41,03% | 0,79 | €-5,45 | 5,41% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.786,34 | €-259,61 | 80 | 80 | 38,75% | 0,87 | €-3,25 | 8,88% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.769,83 | €-272,72 | 171 | 171 | 41,52% | 0,92 | €-1,59 | 12,52% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.768,94 | €-231,06 | 12 | 12 | 33,33% | 0,55 | €-19,26 | 2,69% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.719,08 | €-365,19 | 100 | 100 | 45,00% | 0,83 | €-3,65 | 9,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.709,98 | €-290,02 | 14 | 14 | 28,57% | 0,52 | €-20,72 | 3,74% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.702,44 | €-421,03 | 54 | 54 | 33,33% | 0,77 | €-7,80 | 8,18% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.685,96 | €-296,24 | 90 | 90 | 41,11% | 0,88 | €-3,29 | 6,64% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.679,31 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.628,51 | €-426,34 | 62 | 62 | 37,10% | 0,79 | €-6,88 | 7,26% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.610,71 | €-423,42 | 121 | 121 | 42,98% | 0,83 | €-3,50 | 12,28% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.574,07 | €-415,86 | 94 | 94 | 45,74% | 0,85 | €-4,42 | 8,22% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.553,63 | €-484,11 | 63 | 63 | 31,75% | 0,74 | €-7,68 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.543,47 | €-494,23 | 58 | 58 | 36,21% | 0,73 | €-8,52 | 7,98% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.541,91 | €-478,79 | 110 | 110 | 38,18% | 0,83 | €-4,35 | 7,34% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.506,56 | €-530,99 | 60 | 60 | 35,00% | 0,74 | €-8,85 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.506,47 | €-517,16 | 68 | 68 | 38,24% | 0,75 | €-7,61 | 7,96% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.506,16 | €-552,21 | 107 | 98 | 42,99% | 0,76 | €-5,16 | 8,84% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.469,13 | €-611,69 | 114 | 114 | 41,23% | 0,72 | €-5,37 | 8,85% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.389,19 | €-654,55 | 52 | 52 | 25,00% | 0,65 | €-12,59 | 11,41% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.381,20 | €-648,45 | 31 | 31 | 22,58% | 0,37 | €-20,92 | 8,80% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.380,25 | €-656,80 | 95 | 95 | 48,42% | 0,70 | €-6,91 | 9,02% |
| TEST | Combo Trend | Combo Trend | €9.373,59 | €-659,26 | 156 | 156 | 39,10% | 0,82 | €-4,23 | 10,85% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.320,00 | €-700,22 | 127 | 127 | 39,37% | 0,77 | €-5,51 | 8,78% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.256,81 | €-741,47 | 125 | 125 | 38,40% | 0,71 | €-5,93 | 12,31% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.253,99 | €-778,09 | 74 | 74 | 35,14% | 0,67 | €-10,51 | 10,16% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.202,07 | €-801,82 | 164 | 164 | 42,07% | 0,75 | €-4,89 | 15,45% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.092,72 | €-938,81 | 90 | 90 | 35,56% | 0,64 | €-10,43 | 9,48% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.949,35 | €-1.051,00 | 58 | 58 | 27,59% | 0,58 | €-18,12 | 11,51% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.922,97 | €-1.105,24 | 77 | 77 | 31,17% | 0,51 | €-14,35 | 13,85% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.918,97 | €-1.081,03 | 48 | 48 | 35,42% | 0,46 | €-22,52 | 12,56% |
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
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,46775 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €0,13 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 84,90600 | 73,04357 | 52,97621 | 90,53117 | €8,52 | €25,56 | €1,89 | €1,95 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 253,92000 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €33,91 |
| Bilanciata 1H — LONG senza Range High Vol | HYPE | LONG | Confluenza trend | 60m | 3,0x | 82,20244 | 84,90600 | 83,31582 | 55,21264 | 87,03215 | €28,40 | €85,21 | €0,00 | €2,80 |
| Bilanciata 1H — LONG senza Range High Vol | SOL | LONG | Confluenza trend | 60m | 3,0x | 104,41188 | 107,30400 | 105,16184 | 70,12998 | 109,98009 | €605,05 | €1.815,14 | €0,00 | €50,28 |
| Bilanciata 1H — LONG senza Range High Vol | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,45759 | 1,46775 | 1,42127 | 0,97902 | 1,53023 | €12,87 | €38,60 | €0,96 | €0,27 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | SOL | LONG | Confluenza trend V2 | 60m | 3,0x | 104,52690 | 107,30400 | 105,21076 | 70,20724 | 109,97881 | €610,98 | €1.832,95 | €0,00 | €48,70 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 84,28485 | 84,90600 | 81,99407 | 56,61133 | 88,86642 | €581,73 | €1.745,20 | €47,43 | €12,86 |
| Bilanciata 1H V2 | BTR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19977 | €131,74 | €395,21 | €47,43 | €0,04 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16574 | 0,16571 | 0,15522 | 0,11132 | 0,18679 | €8,47 | €25,42 | €1,61 | €-0,01 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20238 | 0,20238 | 0,20803 | 0,26883 | 0,19107 | €19,31 | €57,92 | €1,62 | €-0,00 |
| Bilanciata 1H V3 Filtered | TAO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 256,45378 | 253,92000 | 247,49602 | 172,25146 | 274,36930 | €462,38 | €1.387,13 | €48,45 | €-13,70 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 82,93658 | 84,90600 | 83,56533 | 55,70574 | 87,18535 | €648,50 | €1.945,50 | €0,00 | €46,20 |
| Bilanciata 1H V3 Filtered | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 104,08581 | 107,30400 | 105,15286 | 69,91097 | 109,65903 | €616,31 | €1.848,93 | €0,00 | €57,17 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €139,02 | €417,05 | €50,05 | €0,05 |
| Rapida V1 — no HIGH + score <7,5 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20481 | 0,20481 | 0,20925 | 0,27205 | 0,19815 | €53,21 | €159,62 | €3,46 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €15,70 | €47,11 | €1,28 | €-0,47 |
| Rapida V1 — no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 84,28485 | 84,90600 | 82,50313 | 56,61133 | 86,95743 | €803,42 | €2.410,25 | €50,95 | €17,76 |
| Rapida V1 — no HIGH + score <7,5 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €132,75 | €398,25 | €47,79 | €0,04 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €35,97 | €107,92 | €2,93 | €-1,07 |
| Rapida V1 — senza PEPE | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| Rapida V1 — senza PEPE | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 253,92000 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €3,80 |
| Rapida V1 — senza PEPE | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| Rapida V1 — senza PEPE | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 84,28485 | 84,90600 | 82,50313 | 56,61133 | 86,95743 | €835,39 | €2.506,17 | €52,98 | €18,47 |
| Rapida V1 — senza PEPE | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €145,28 | €435,84 | €52,30 | €0,05 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| Rapida V1 — target pieno 2R | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| Rapida V1 — target pieno 2R | TAO | LONG | Momentum / breakout | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 270,38807 | €16,65 | €49,96 | €1,36 | €-0,49 |
| Rapida V1 — target pieno 2R | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,93658 | 84,90600 | 83,80800 | 55,70574 | 86,24118 | €804,14 | €2.412,42 | €0,00 | €57,29 |
| Rapida V1 — target pieno 2R | SOL | LONG | Momentum / breakout | 60m | 3,0x | 106,86837 | 107,30400 | 104,58411 | 71,77992 | 111,43690 | €11,71 | €35,13 | €0,75 | €0,14 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 84,28485 | 84,90600 | 82,50313 | 56,61133 | 86,95743 | €809,65 | €2.428,95 | €51,35 | €17,90 |
| Rapida 1H V2 | ENA | LONG | Momentum / breakout V2 | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €347,08 | €1.041,24 | €51,43 | €-0,21 |
| Rapida 1H V3 Filtered — madre | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered — madre | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 253,92000 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €46,72 |
| Rapida 1H V3 Filtered — madre | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €8,42 | €25,27 | €3,03 | €0,00 |
| Rapida 1H V3 Filtered — madre | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €333,17 | €999,52 | €49,37 | €-0,20 |
| Rapida V3 — no volatilità HIGH | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20238 | 0,20238 | 0,20677 | 0,26883 | 0,19578 | €27,66 | €82,98 | €1,80 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €599,45 | €1.798,35 | €48,86 | €-17,77 |
| Rapida V3 — no volatilità HIGH | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €9,29 | €27,86 | €3,34 | €0,00 |
| Rapida V3 — no volatilità HIGH | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €328,51 | €985,53 | €48,68 | €-0,20 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| Rapida V3 — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 253,92000 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €43,91 |
| Rapida V3 — Long Only | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79703,63754 | 80375,74000 | 80065,01138 | 53534,27655 | 81042,65865 | €37,44 | €112,33 | €0,00 | €0,95 |
| Rapida V3 — Long Only | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €135,44 | €406,31 | €48,76 | €0,04 |
| Rapida V3 — Long Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €329,47 | €988,42 | €48,82 | €-0,20 |
| Rapida V3 — Long + no HIGH + score <7,5 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €593,36 | €1.780,09 | €48,36 | €-17,59 |
| Rapida V3 — Long + no HIGH + score <7,5 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79703,63754 | 80375,74000 | 80065,01138 | 53534,27655 | 81042,65865 | €44,77 | €134,31 | €0,00 | €1,13 |
| Rapida V3 — Long + no HIGH + score <7,5 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €134,26 | €402,77 | €48,33 | €0,04 |
| Rapida V3 — senza ESPORTS | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 253,92000 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €2,14 |
| Rapida V3 — senza ESPORTS | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| Rapida V3 — senza ESPORTS | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €330,63 | €991,90 | €48,99 | €-0,20 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €610,51 | €1.831,53 | €49,76 | €-18,10 |
| Rapida V3 senza ESPORTS — Long Only | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €139,69 | €419,06 | €50,29 | €0,05 |
| Rapida V3 senza ESPORTS — Long Only | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €340,05 | €1.020,15 | €50,39 | €-0,20 |
| Rapida V3 senza ESPORTS — MFE Lock | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 253,92000 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €47,02 |
| Rapida V3 senza ESPORTS — MFE Lock | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €8,48 | €25,43 | €3,05 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €335,33 | €1.005,98 | €49,69 | €-0,20 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79703,63754 | 80375,74000 | 80065,01138 | 53534,27655 | 81042,65865 | €1.524,86 | €4.574,59 | €0,00 | €38,58 |
| Rapida V3 senza ESPORTS — Stress Guard | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 255,41107 | 253,92000 | 248,22303 | 171,55110 | 266,19314 | €586,06 | €1.758,19 | €49,48 | €-10,26 |
| Rapida V3 — qualità completa + profit lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €582,29 | €1.746,86 | €47,46 | €-17,26 |
| Rapida V3 — qualità completa + profit lock | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79703,63754 | 80375,74000 | 78810,95680 | 53534,27655 | 81042,65865 | €37,24 | €111,71 | €1,25 | €0,94 |
| Rapida V3 — qualità completa + profit lock | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15804 | 0,16112 | 0,13908 | 0,10615 | 0,18649 | €130,02 | €390,07 | €46,81 | €7,60 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2524,19000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,46 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 84,90600 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,95 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08902 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-20,39 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20989 | 0,20989 | 0,20756 | 0,31379 | 0,19609 | €816,97 | €1.633,95 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SOL | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 104,08581 | 107,30400 | 104,99313 | 52,56334 | 110,21635 | €913,11 | €1.826,22 | €0,00 | €56,46 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,16574 | 0,16571 | 0,15522 | 0,08370 | 0,18890 | €13,29 | €26,58 | €1,69 | €-0,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 101,66933 | 107,30400 | 105,03928 | 51,34301 | 108,62113 | €1.034,66 | €2.069,32 | €0,00 | €114,69 |
| Benchmark Donchian breakout 1H | ENA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15175 | 0,16571 | 0,15571 | 0,07663 | 0,17114 | €38,55 | €77,10 | €0,00 | €7,09 |
| Benchmark Donchian breakout 1H | TAO | LONG | Donchian breakout 20 barre | 60m | 2,0x | 256,45378 | 253,92000 | 246,50071 | 129,50916 | 281,33645 | €713,06 | €1.426,12 | €55,35 | €-14,09 |
| Benchmark Donchian breakout 1H | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45759 | 1,46775 | 1,41723 | 0,73608 | 1,55848 | €42,73 | €85,47 | €2,37 | €0,60 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 101,66933 | 107,30400 | 105,03928 | 51,34301 | 108,62113 | €1.010,30 | €2.020,60 | €0,00 | €111,98 |
| Donchian 1H Gb20 120R V1 | ENA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15175 | 0,16571 | 0,15571 | 0,07663 | 0,17114 | €37,64 | €75,28 | €0,00 | €6,93 |
| Donchian 1H Gb20 120R V1 | TAO | LONG | Donchian breakout 20 barre | 60m | 2,0x | 256,45378 | 253,92000 | 246,50071 | 129,50916 | 281,33645 | €696,27 | €1.392,55 | €54,05 | €-13,76 |
| Donchian 1H Gb20 120R V1 | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45759 | 1,46775 | 1,41723 | 0,73608 | 1,55848 | €41,73 | €83,46 | €2,31 | €0,58 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 805,66000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-0,10 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,20989 | 0,20989 | 0,21687 | 0,31379 | 0,19455 | €681,63 | €1.363,26 | €45,30 | €-0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | TAO | LONG | Scanner Top 5 Long | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €787,29 | €1.574,59 | €55,00 | €-15,56 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 109,98009 | €1.030,31 | €2.060,63 | €0,00 | €57,08 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 88,86642 | €40,93 | €81,87 | €2,23 | €0,60 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 253,92000 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €35,82 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 79703,63754 | 80375,74000 | 78555,90516 | 40250,33696 | 81999,10230 | €94,05 | €188,09 | €2,71 | €1,59 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 109,98009 | €953,59 | €1.907,17 | €0,00 | €52,83 |
| Scanner Top10 Long | BTR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €206,82 | €413,63 | €49,64 | €-12,07 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 82,90558 | 84,90600 | 83,58658 | 41,86732 | 87,09963 | €12,53 | €25,06 | €0,00 | €0,60 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 253,92000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €4,67 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 79703,63754 | 80375,74000 | 78555,90516 | 40250,33696 | 81999,10230 | €68,29 | €136,57 | €1,97 | €1,15 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 109,98009 | €918,06 | €1.836,13 | €0,00 | €50,86 |
| Scanner Top15 Long | BTR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €-11,63 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 88,86642 | €13,57 | €27,13 | €0,74 | €0,20 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 253,92000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €4,67 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 79703,63754 | 80375,74000 | 78555,90516 | 40250,33696 | 81999,10230 | €68,29 | €136,57 | €1,97 | €1,15 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 109,98009 | €918,06 | €1.836,13 | €0,00 | €50,86 |
| Scanner Top20 Long | BTR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €-11,63 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 88,86642 | €13,57 | €27,13 | €0,74 | €0,20 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €731,82 | €1.463,64 | €51,12 | €-14,46 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 110,53691 | €957,78 | €1.915,56 | €0,00 | €53,06 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 89,32457 | €30,02 | €60,05 | €1,63 | €0,44 |
| Top 5 + BTC — solo MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Top 5 + BTC — solo MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Top 5 + BTC — solo MFE | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €686,05 | €1.372,09 | €47,93 | €-13,56 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 110,53691 | €897,87 | €1.795,74 | €0,00 | €49,74 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 89,32457 | €28,15 | €56,29 | €1,53 | €0,41 |
| Top 5 + BTC — Guard | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Top 5 + BTC — Guard | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Top 5 + BTC — Guard | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €686,16 | €1.372,33 | €47,93 | €-13,56 |
| Top 5 + BTC — Guard | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,52690 | 107,30400 | 105,21076 | 52,78609 | 110,52400 | €898,15 | €1.796,31 | €0,00 | €47,72 |
| Top 5 + BTC — Guard | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20978 | €189,80 | €379,60 | €45,55 | €-11,08 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Top 5 + BTC — BTC≤3 | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €638,32 | €1.276,65 | €44,59 | €-12,61 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,52690 | 107,30400 | 105,21076 | 52,78609 | 110,52400 | €820,21 | €1.640,42 | €0,00 | €43,58 |
| Top 5 + BTC — BTC 2–3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Top 5 + BTC — BTC 2–3 | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €671,11 | €1.342,21 | €46,88 | €-13,26 |
| Top 5 + BTC — BTC 2–3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,52690 | 107,30400 | 105,21076 | 52,78609 | 110,52400 | €862,33 | €1.724,67 | €0,00 | €45,82 |
| Top 5 + BTC — Guard + MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Top 5 + BTC — Guard + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Top 5 + BTC — Guard + MFE | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €670,21 | €1.340,41 | €46,82 | €-13,24 |
| Top 5 + BTC — Guard + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,52690 | 107,30400 | 105,21076 | 52,78609 | 110,52400 | €877,27 | €1.754,53 | €0,00 | €46,61 |
| Top 5 + BTC — Guard + MFE | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20978 | €185,39 | €370,78 | €44,49 | €-10,82 |
| Top 5 + BTC — Guard + BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €664,75 | €1.329,49 | €46,44 | €-13,14 |
| Top 5 + BTC — Guard + BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,52690 | 107,30400 | 105,21076 | 52,78609 | 110,52400 | €886,23 | €1.772,45 | €0,00 | €47,09 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €653,16 | €1.306,32 | €45,63 | €-12,91 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,52690 | 107,30400 | 105,21076 | 52,78609 | 110,52400 | €870,78 | €1.741,56 | €0,00 | €46,27 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 283,32706 | €24,72 | €49,44 | €1,73 | €-0,49 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,22571 | €210,82 | €421,64 | €50,60 | €-12,30 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,08581 | 107,30400 | 105,15286 | 52,56334 | 112,44564 | €932,74 | €1.865,48 | €0,00 | €57,68 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,23 | €0,71 | €0,19 |
| Top 5 + BTC — target pieno 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 283,32706 | €24,74 | €49,47 | €1,73 | €-0,49 |
| Top 5 + BTC — target pieno 3R | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,22571 | €210,94 | €421,89 | €50,63 | €-12,31 |
| Top 5 + BTC — target pieno 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 104,08581 | 107,30400 | 105,15286 | 52,56334 | 112,44564 | €933,28 | €1.866,57 | €0,00 | €57,71 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,25 | €0,71 | €0,19 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 805,66000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-1,39 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,20238 | 0,20238 | 0,20866 | 0,30256 | 0,18856 | €29,18 | €58,37 | €1,81 | €-0,00 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 104,18883 | 107,30400 | 105,08073 | 52,61536 | 110,75800 | €803,33 | €1.606,66 | €0,00 | €48,04 |
| Combo Trend | TAO | LONG | Combo Trend | 60m | 2,0x | 256,52382 | 253,92000 | 245,99516 | 129,54453 | 279,68689 | €541,85 | €1.083,69 | €44,48 | €-11,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 84,90600 | 81,73954 | 42,56385 | 89,88454 | €13,36 | €26,72 | €0,81 | €0,20 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 276,16085 | €703,10 | €1.406,21 | €49,12 | €-13,89 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 104,41188 | 107,30400 | 105,16184 | 52,72800 | 110,53691 | €920,20 | €1.840,40 | €0,00 | €50,98 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 89,32457 | €24,57 | €49,15 | €1,34 | €0,36 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 253,92000 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €2,16 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 805,66000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-1,73 |
| Combo Adaptive — madre | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive — madre | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €40,31 | €80,63 | €2,25 | €-0,00 |
| Combo Adaptive — madre | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €222,35 | €444,69 | €53,36 | €-12,98 |
| Combo Adaptive — madre | SOL | LONG | Combo Adaptive | 60m | 2,0x | 104,08581 | 107,30400 | 105,31258 | 52,56334 | 109,65903 | €946,48 | €1.892,96 | €0,00 | €58,53 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 88,86642 | €15,78 | €31,55 | €0,86 | €0,23 |
| Combo Adaptive — MFE Trail esistente | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 253,92000 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €2,87 |
| Combo Adaptive — MFE Trail esistente | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €40,65 | €81,31 | €2,27 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €163,28 | €326,55 | €39,19 | €-9,53 |
| Combo Adaptive — MFE Trail esistente | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 88,86642 | €845,44 | €1.690,88 | €45,96 | €12,46 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 253,92000 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €34,15 |
| Combo Adaptive — Quality7 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €876,38 | €1.752,76 | €48,96 | €-0,00 |
| Combo Adaptive — Quality7 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 106,43928 | 107,30400 | 103,65189 | 53,75184 | 112,01408 | €935,28 | €1.870,56 | €48,99 | €15,20 |
| Combo Adaptive — Trend/Transition | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive — Trend/Transition | TAO | LONG | Combo Adaptive | 60m | 2,0x | 256,52382 | 253,92000 | 247,04802 | 129,54453 | 275,47542 | €664,95 | €1.329,89 | €49,13 | €-13,50 |
| Combo Adaptive — Trend/Transition | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €204,79 | €409,58 | €49,15 | €-11,95 |
| Combo Adaptive — Trend/Transition | SOL | LONG | Combo Adaptive | 60m | 2,0x | 104,08581 | 107,30400 | 105,31258 | 52,56334 | 109,65903 | €917,89 | €1.835,77 | €0,00 | €56,76 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive — Long Only | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | TAO | LONG | Combo Adaptive | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €747,11 | €1.494,22 | €52,19 | €-14,76 |
| Combo Adaptive — Long Only | SOL | LONG | Combo Adaptive | 60m | 2,0x | 104,41188 | 107,30400 | 105,32092 | 52,72800 | 109,98009 | €978,05 | €1.956,10 | €0,00 | €54,18 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,28485 | 84,90600 | 81,99407 | 42,56385 | 88,86642 | €34,53 | €69,05 | €1,88 | €0,51 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive — parziale 1R | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20989 | 0,20989 | 0,20688 | 0,31379 | 0,19734 | €18,50 | €37,00 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive — parziale 1R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €37,81 | €75,62 | €2,64 | €-0,75 |
| Combo Adaptive — parziale 1R | SOL | LONG | Combo Adaptive | 60m | 2,0x | 104,41188 | 107,30400 | 105,32092 | 52,72800 | 109,98009 | €15,14 | €30,28 | €0,00 | €0,84 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 80391,81515 | 80375,74000 | 79234,17301 | 53996,50251 | 82707,09942 | €1.138,16 | €3.414,47 | €49,17 | €-0,68 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 80375,74000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €0,36 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 80375,74000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €0,36 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 80375,74000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €-1,02 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 80375,74000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €0,33 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 104,52690 | 107,30400 | 105,52194 | 70,20724 | 109,97881 | €650,72 | €1.952,17 | €0,00 | €51,87 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 98,32066 | 107,30400 | 102,73199 | 49,65193 | 113,95442 | €395,27 | €790,53 | €0,00 | €72,23 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 106,43928 | 107,30400 | 103,96160 | 71,49172 | 111,39466 | €736,80 | €2.210,40 | €51,45 | €17,96 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 107,30400 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €27,80 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 107,30400 | 112,84334 | 160,38740 | 97,27311 | €478,97 | €957,94 | €49,65 | €-0,19 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 104,52690 | 107,30400 | 105,52194 | 70,20724 | 109,97881 | €641,47 | €1.924,41 | €0,00 | €51,13 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 98,32066 | 107,30400 | 102,73199 | 49,65193 | 115,37567 | €367,30 | €734,59 | €0,00 | €67,12 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2524,19000 | 2464,86772 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €0,00 | €54,76 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.560,29 | €3.120,58 | €46,79 | €27,29 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €23,24 | €46,49 | €1,62 | €-0,46 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,16112 | 0,13908 | 0,07981 | 0,19597 | €191,23 | €382,45 | €45,89 | €7,45 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,30400 | 103,93146 | 53,96853 | 112,74219 | €863,53 | €1.727,06 | €47,46 | €7,04 |
| Master Adaptive V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16571 | 0,15522 | 0,08370 | 0,18679 | €371,72 | €743,44 | €47,21 | €-0,15 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.565,03 | €3.130,05 | €46,93 | €27,37 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,16112 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €30,16 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,52382 | 253,92000 | 247,04802 | 129,54453 | 275,47542 | €25,45 | €50,89 | €1,88 | €-0,52 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.493,28 | €2.986,56 | €44,78 | €26,11 |
| Master Adaptive Strict3 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,52382 | 253,92000 | 247,04802 | 129,54453 | 275,47542 | €603,68 | €1.207,36 | €44,60 | €-12,26 |
| Master Adaptive Strict3 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €184,95 | €369,91 | €44,39 | €-10,79 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.572,67 | €3.145,34 | €47,16 | €27,50 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €20,64 | €41,28 | €1,44 | €-0,41 |
| Master Adaptive Expanded V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16110 | 0,16112 | 0,14177 | 0,08136 | 0,19977 | €197,88 | €395,75 | €47,49 | €0,04 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 107,32546 | 107,30400 | 104,39936 | 54,19936 | 113,17765 | €18,64 | €37,29 | €1,02 | €-0,01 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.539,56 | €3.079,12 | €46,16 | €26,92 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €22,94 | €45,87 | €1,60 | €-0,45 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,16112 | 0,13908 | 0,07981 | 0,19597 | €188,69 | €377,37 | €45,28 | €7,35 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,30400 | 103,93146 | 53,96853 | 112,74219 | €852,06 | €1.704,12 | €46,83 | €6,95 |
| Master Adaptive Gb20 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16571 | 0,15522 | 0,08370 | 0,18679 | €366,78 | €733,57 | €46,58 | €-0,15 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 84,90600 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €97,80 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2614,85753 | €1.568,97 | €3.137,94 | €47,05 | €27,44 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 283,32707 | €577,74 | €1.155,48 | €40,36 | €-11,42 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,43928 | 107,30400 | 103,65189 | 53,75184 | 114,80148 | €920,14 | €1.840,29 | €48,19 | €14,95 |
| Master Adaptive Runner25 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16571 | 0,15522 | 0,08370 | 0,19732 | €14,90 | €29,81 | €1,89 | €-0,01 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 805,66000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-1,72 |
| Combo Adaptive — Side × Regime Guard | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SOL | LONG | Combo Adaptive | 60m | 2,0x | 104,52690 | 107,30400 | 105,36635 | 52,78609 | 109,97881 | €16,54 | €33,09 | €0,00 | €0,88 |
| Combo Adaptive — Side × Regime Guard | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20579 | €210,11 | €420,21 | €50,43 | €-12,26 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.568,02 | €3.136,03 | €47,02 | €27,42 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €23,36 | €46,72 | €1,63 | €-0,46 |
| Master Adaptive GB20 — Breakeven 0,5R | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,16112 | 0,13908 | 0,07981 | 0,19597 | €192,17 | €384,35 | €46,12 | €7,49 |
| Master Adaptive GB20 — Breakeven 0,5R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,30400 | 103,93146 | 53,96853 | 112,74219 | €867,81 | €1.735,61 | €47,70 | €7,07 |
| Master Adaptive GB20 — Breakeven 0,5R | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16571 | 0,15522 | 0,08370 | 0,18679 | €373,56 | €747,13 | €47,44 | €-0,15 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.566,35 | €3.132,70 | €46,97 | €27,39 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 247,49602 | 129,50916 | 274,36930 | €23,33 | €46,67 | €1,63 | €-0,46 |
| Master Adaptive GB20 — 50% a 0,75R | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,16112 | 0,13908 | 0,07981 | 0,19597 | €191,97 | €383,94 | €46,07 | €7,48 |
| Master Adaptive GB20 — 50% a 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,30400 | 103,93146 | 53,96853 | 112,74219 | €866,88 | €1.733,77 | €47,65 | €7,07 |
| Master Adaptive GB20 — 50% a 0,75R | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16571 | 0,15522 | 0,08370 | 0,18679 | €373,17 | €746,33 | €47,39 | €-0,15 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2524,19000 | 2474,17356 | 1263,66673 | 2577,34181 | €1.829,31 | €3.658,61 | €41,14 | €31,99 |
| Master Adaptive GB20 — Loss Cap 0,75R | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 256,45378 | 253,92000 | 249,73546 | 129,50916 | 274,36930 | €36,76 | €73,52 | €1,93 | €-0,73 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,16112 | 0,13908 | 0,07981 | 0,20861 | €188,78 | €377,55 | €45,31 | €7,35 |
| Master Adaptive GB20 — Loss Cap 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,30400 | 104,66569 | 53,96853 | 112,74219 | €1.136,69 | €2.273,37 | €46,86 | €9,27 |
| Master Adaptive GB20 — Loss Cap 0,75R | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16571 | 0,15785 | 0,08370 | 0,18679 | €72,36 | €144,71 | €6,89 | €-0,03 |
| Rapida V3 NoHigh — Regime Guard | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79703,63754 | 80375,74000 | 80065,01138 | 53534,27655 | 81042,65865 | €112,95 | €338,85 | €0,00 | €2,86 |
| Rapida V3 NoHigh — Regime Guard | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 106,86837 | 107,30400 | 104,58411 | 71,77992 | 110,29476 | €794,37 | €2.383,11 | €50,94 | €9,71 |
| Rapida V3 NoHigh — Regime Guard | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16574 | 0,16571 | 0,15756 | 0,11132 | 0,17802 | €348,23 | €1.044,68 | €51,60 | €-0,21 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 84,90600 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €60,62 |
| MAIN — Side × Regime Guard | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,46775 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-0,09 |
| MAIN — Side × Regime Guard | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2524,19000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €1,06 |
| MAIN — Side × Regime Guard | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,15177 | 0,16571 | 0,13506 | 0,10194 | 0,18520 | €156,97 | €470,92 | €51,86 | €43,25 |
| Combo Trend — Side × Regime Guard | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTR | LONG | Combo Trend | 60m | 2,0x | 0,16596 | 0,16112 | 0,14605 | 0,08381 | 0,20978 | €231,16 | €462,32 | €55,48 | €-13,49 |
| Combo Trend — Side × Regime Guard | SOL | LONG | Combo Trend | 60m | 2,0x | 104,08581 | 107,30400 | 104,99313 | 52,56334 | 110,89752 | €932,48 | €1.864,96 | €0,00 | €57,66 |
| Combo Trend — Side × Regime Guard | TAO | LONG | Combo Trend | 60m | 2,0x | 257,66152 | 253,92000 | 247,23759 | 130,11907 | 280,59418 | €668,48 | €1.336,96 | €54,09 | €-19,41 |
| Combo Trend — Side × Regime Guard | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 84,90600 | 81,73954 | 42,56385 | 89,88454 | €32,97 | €65,95 | €1,99 | €0,49 |
| FAST NoHigh <7,5 · SHORT only | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20481 | 0,20481 | 0,20925 | 0,27205 | 0,19815 | €51,88 | €155,65 | €3,37 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TAO | LONG | Momentum / breakout | 60m | 3,0x | 256,45378 | 253,92000 | 249,48663 | 172,25146 | 266,90450 | €15,31 | €45,94 | €1,25 | €-0,45 |
| FAST NoHigh <7,5 · SHORT only | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 84,28485 | 84,90600 | 82,50313 | 56,61133 | 86,95743 | €783,42 | €2.350,27 | €49,68 | €17,32 |
| FAST NoHigh <7,5 · SHORT only | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16112 | 0,14177 | 0,10821 | 0,19010 | €129,45 | €388,34 | €46,60 | €0,04 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | TAO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 256,45378 | 253,92000 | 247,49602 | 172,25146 | 274,36930 | €447,77 | €1.343,31 | €46,92 | €-13,27 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 82,93658 | 84,90600 | 83,56533 | 55,70574 | 87,18535 | €613,32 | €1.839,95 | €0,00 | €43,69 |
| Bilanciata V3 · LONG only | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 104,08581 | 107,30400 | 105,15286 | 69,91097 | 109,65903 | €583,77 | €1.751,31 | €0,00 | €54,15 |
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
| Rapida V3 NoHigh — Regime Guard | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €72,50 | 1,43 | TARGET |
| Scalp RSI Short 80 · prudente · 5x | TAO | SHORT | 2026-08-27T15:15:00+00:00 | 256,46128 | €-0,88 | -0,09 | TIME_EXIT |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €67,64 | 1,43 | TARGET |
| Rapida V3 senza ESPORTS — Stress Guard | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €73,39 | 1,43 | TARGET |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €70,42 | 1,43 | TARGET |
| Rapida V3 senza ESPORTS — Long Only | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €71,03 | 1,43 | TARGET |
| Rapida V3 — senza ESPORTS | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €67,77 | 1,43 | TARGET |
| Rapida V3 — Long + no HIGH + score <7,5 | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €68,92 | 1,43 | TARGET |
| Rapida V3 — Long Only | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €67,46 | 1,43 | TARGET |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €68,99 | 1,43 | TARGET |
| Rapida 1H V3 Filtered — madre | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,39795 | €69,97 | 1,43 | TARGET |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | HYPE | LONG | 2026-08-27T15:30:00+00:00 | 85,00277 | €71,18 | 1,43 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 563/30 | 33/30 | 0,89 | 2,04 | -0,05R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 520/30 | 20/30 | 0,85 | 1,90 | -0,07R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 234/30 | 22/30 | 0,87 | 1,74 | -0,07R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 235/30 | 22/30 | 0,83 | 1,57 | -0,08R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 482/30 | 31/30 | 0,95 | 0,62 | -0,03R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 441/30 | 11/30 | 0,92 | 0,00 | -0,04R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 130/30 | 8/30 | 0,75 | 1,02 | -0,13R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 304/30 | 17/30 | 0,66 | 4,50 | -0,19R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 471/30 | 24/30 | 0,73 | 0,64 | -0,14R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 432/30 | 7/30 | 0,63 | 0,02 | -0,19R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 482/30 | 30/30 | 0,97 | 1,02 | -0,01R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 804/30 | 55/30 | 0,92 | 1,12 | -0,03R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 143/30 | 15/30 | 0,57 | 0,99 | -0,27R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 704/30 | 44/30 | 0,82 | 1,20 | -0,09R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 708/30 | 37/30 | 0,82 | 0,76 | -0,09R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 652/30 | 23/30 | 0,76 | 1,12 | -0,12R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 344/30 | 52/30 | 0,78 | 0,87 | -0,13R | €-3,67 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 13/30 | 0,00 | 1,47 | 0,00R | €12,42 | 2,04% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 36/30 | 0,00 | 2,02 | 0,00R | €20,00 | 3,82% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 50/30 | 28/30 | 0,67 | 0,60 | -0,18R | €-2,16 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 845/30 | 121/30 | 0,95 | 0,69 | -0,03R | €-7,02 | 13,99% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 100/30 | 0,00 | 0,83 | 0,00R | €-3,65 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 276/30 | 98/30 | 1,20 | 0,76 | 0,10R | €-5,16 | 8,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 534/30 | 158/30 | 1,03 | 0,98 | 0,02R | €-0,45 | 9,12% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 455/30 | 114/30 | 0,97 | 0,72 | -0,01R | €-5,37 | 8,85% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 243/30 | 72/30 | 0,92 | 1,01 | -0,04R | €0,20 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 501/30 | 110/30 | 0,89 | 0,97 | -0,05R | €-0,57 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 568/30 | 146/30 | 0,91 | 1,06 | -0,04R | €1,31 | 7,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 948/30 | 221/30 | 0,86 | 1,14 | -0,07R | €2,68 | 7,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 150/30 | 0,00 | 1,46 | 0,00R | €9,00 | 5,23% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 95/30 | 0,00 | 0,72 | 0,00R | €-8,78 | 12,64% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 38/30 | 0,00 | 1,14 | 0,00R | €3,94 | 3,35% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 542/30 | 137/30 | 0,93 | 0,84 | -0,03R | €-4,26 | 12,33% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 905/30 | 229/30 | 0,85 | 1,08 | -0,08R | €1,39 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 65/30 | 43/30 | 0,84 | 1,23 | -0,08R | €5,61 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 885/30 | 237/30 | 0,88 | 1,12 | -0,06R | €2,19 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 663/30 | 136/30 | 0,94 | 0,75 | -0,03R | €-6,57 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 278/30 | 94/30 | 1,00 | 0,85 | 0,00R | €-4,42 | 8,22% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 281/30 | 90/30 | 0,97 | 0,88 | -0,01R | €-3,29 | 6,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 561/30 | 171/30 | 0,98 | 0,92 | -0,01R | €-1,59 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 41/30 | 0,00 | 1,25 | 0,00R | €6,05 | 3,97% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 77/30 | 0,00 | 1,23 | 0,00R | €4,89 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 585/30 | 128/30 | 0,81 | 0,95 | -0,10R | €-1,01 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 161/30 | 0,00 | 1,03 | 0,00R | €0,60 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 193/30 | 0,00 | 1,19 | 0,00R | €3,04 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 58/30 | 0,00 | 1,30 | 0,00R | €6,40 | 4,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 838/30 | 207/30 | 0,85 | 0,95 | -0,08R | €-0,98 | 9,00% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 325/30 | 52/30 | 0,83 | 1,24 | -0,11R | €5,39 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 287/30 | 81/30 | 1,14 | 0,55 | 0,06R | €-15,55 | 14,60% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 15/30 | 9/30 | 0,64 | 0,86 | -0,19R | €-3,49 | 1,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 2/30 | 2/30 | 2,26 | 2,39 | 0,67R | €35,09 | 0,96% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 9/30 | 6/30 | 3,40 | 4,66 | 0,60R | €34,87 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 2/30 | 2/30 | 1,56 | 1,54 | 0,31R | €14,72 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 17/30 | 10/30 | 0,32 | 0,85 | -0,54R | €-4,29 | 1,49% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 6/30 | 4/30 | 0,50 | 0,80 | -0,45R | €-8,55 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 19/30 | 13/30 | 0,82 | 0,61 | -0,10R | €-12,80 | 1,94% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 4/30 | 3/30 | 0,75 | 1,19 | -0,20R | €6,47 | 1,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 701/30 | 150/30 | 1,02 | 1,28 | 0,01R | €4,60 | 7,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 433/30 | 124/30 | 1,09 | 1,16 | 0,05R | €3,49 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 770/30 | 164/30 | 1,04 | 0,75 | 0,02R | €-4,89 | 15,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 642/30 | 154/30 | 0,97 | 1,03 | -0,01R | €0,54 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 82/30 | 39/30 | 1,40 | 0,91 | 0,17R | €-2,25 | 4,21% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 82/30 | 39/30 | 1,40 | 0,79 | 0,17R | €-5,45 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 222/30 | 80/30 | 1,00 | 0,87 | 0,00R | €-3,25 | 8,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 246/30 | 62/30 | 1,04 | 0,89 | 0,02R | €-2,80 | 5,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 94/30 | 0,74 | 0,53 | -0,20R | €-11,02 | 12,67% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 116/30 | 0,00 | 1,18 | 0,00R | €3,65 | 8,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 75/30 | 0,74 | 0,38 | -0,20R | €-16,04 | 12,67% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 109/30 | 48/30 | 1,23 | 0,46 | 0,10R | €-22,52 | 12,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 437/30 | 134/30 | 1,15 | 0,94 | 0,08R | €-1,38 | 11,38% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 580/30 | 156/30 | 1,00 | 0,82 | 0,00R | €-4,23 | 10,85% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 115/30 | 0,00 | 1,53 | 0,00R | €9,54 | 6,20% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 13/30 | 10/30 | 1,77 | 0,97 | 0,27R | €-0,74 | 1,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 17/30 | 13/30 | 0,45 | 0,79 | -0,39R | €-5,78 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 28/30 | 17/30 | 0,42 | 0,97 | -0,41R | €-0,66 | 2,77% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 306/30 | 108/30 | 0,91 | 1,48 | -0,06R | €10,79 | 6,11% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 236/30 | 76/30 | 0,92 | 1,58 | -0,05R | €11,88 | 6,11% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 585/30 | 125/30 | 1,03 | 0,71 | 0,01R | €-5,93 | 12,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 23/30 | 14/30 | 0,59 | 0,72 | -0,30R | €-9,04 | 3,14% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 15/30 | 7/30 | 1,86 | 0,22 | 0,32R | €-42,33 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 22/30 | 14/30 | 0,43 | 0,52 | -0,46R | €-20,72 | 3,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 32/30 | 19/30 | 0,54 | 0,77 | -0,31R | €-7,75 | 4,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 6/30 | 5/30 | 0,46 | 0,58 | -0,38R | €-17,74 | 1,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 14/30 | 17/30 | 0,90 | 0,41 | -0,07R | €-18,86 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 285/30 | 68/30 | 1,08 | 0,75 | 0,05R | €-7,61 | 7,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 63/30 | 0,00 | 0,74 | 0,00R | €-7,68 | 8,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 52/30 | 0,00 | 0,65 | 0,00R | €-12,59 | 11,41% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 58/30 | 0,00 | 0,73 | 0,00R | €-8,52 | 7,98% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 534/30 | 95/30 | 1,42 | 0,70 | 0,13R | €-6,91 | 9,02% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 250/30 | 62/30 | 1,09 | 0,79 | 0,06R | €-6,88 | 7,26% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 261/30 | 54/30 | 1,06 | 0,77 | 0,04R | €-7,80 | 8,18% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 180/30 | 58/30 | 1,02 | 0,58 | 0,02R | €-18,12 | 11,51% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 274/30 | 60/30 | 1,04 | 0,74 | 0,03R | €-8,85 | 7,80% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 704/30 | 105/30 | 0,93 | 0,47 | -0,04R | €-14,80 | 17,39% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 271/30 | 109/30 | 1,23 | 0,93 | 0,11R | €-1,93 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 229/30 | 70/30 | 0,52 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 229/30 | 70/30 | 0,52 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 229/30 | 70/30 | 0,52 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 261/30 | 89/30 | 0,67 | 0,64 | -0,18R | €-9,30 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 269/30 | 61/30 | 0,78 | 0,58 | -0,10R | €-12,17 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 242/30 | 62/30 | 0,68 | 0,56 | -0,14R | €-12,20 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 422/30 | 131/30 | 1,12 | 1,05 | 0,05R | €0,95 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 422/30 | 128/30 | 1,11 | 0,91 | 0,05R | €-1,66 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 422/30 | 128/30 | 1,11 | 0,91 | 0,05R | €-1,66 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 423/30 | 129/30 | 1,16 | 1,08 | 0,08R | €1,67 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 152/30 | 31/30 | 0,77 | 0,37 | -0,14R | €-20,92 | 8,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 313/30 | 77/30 | 0,90 | 0,51 | -0,06R | €-14,35 | 13,85% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 329/30 | 90/30 | 1,14 | 0,64 | 0,06R | €-10,43 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 276/30 | 74/30 | 0,98 | 0,67 | -0,01R | €-10,51 | 10,16% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 419/30 | 127/30 | 1,23 | 0,77 | 0,09R | €-5,51 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 344/30 | 110/30 | 1,15 | 0,83 | 0,08R | €-4,35 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 469/30 | 121/30 | 1,14 | 0,83 | 0,06R | €-3,50 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 371/30 | 111/30 | 1,10 | 1,05 | 0,05R | €1,09 | 12,06% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 349/30 | 107/30 | 1,13 | 1,05 | 0,07R | €1,18 | 11,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 464/30 | 143/30 | 1,17 | 1,36 | 0,08R | €6,91 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 30/30 | 16/30 | 0,77 | 1,08 | -0,16R | €2,33 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 8/30 | 7/30 | 2,23 | 2,72 | 0,49R | €27,71 | 1,01% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 23/30 | 12/30 | 0,70 | 0,55 | -0,19R | €-19,26 | 2,69% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 5/30 | 4/30 | 1,99 | 0,56 | 0,41R | €-17,33 | 1,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 24/30 | 14/30 | 1,01 | 2,18 | 0,01R | €20,77 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 7/30 | 6/30 | 1,26 | 2,73 | 0,16R | €32,74 | 1,05% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 28/30 | 15/30 | 0,94 | 1,47 | -0,04R | €12,14 | 3,33% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 9/30 | 8/30 | 0,68 | 1,26 | -0,23R | €7,01 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08902**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 29.9 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 80375.74 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, stop_within_limit**
- High **0.08907**; close **0.08863**; wick alta **0.0%**; volume **x0.60**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=461; LEGACY_RESEARCH_EVIDENCE_V3=1664; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **90,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +3.83%, 91% oltre +1%.
- BTC trend score: **4,00**; ADX: **38,82**; breadth sopra EMA50: **100,00%**
- Mediana alt vs BTC: **3,83%**; dispersione: **4,64%**

- Aperti in questo ciclo: **62**
- Chiusi in questo ciclo: **18**
- Posizioni research aperte: **698**
- Trade research chiusi: **33883**
- Eventi di mercato indipendenti chiusi: **4556**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **87162**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 11 | 563 | 563 | 35,88% | 0,89 | -0,05R | €-300,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 11 | 520 | 520 | 35,19% | 0,85 | -0,07R | €-387,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 5 | 234 | 234 | 47,44% | 0,87 | -0,07R | €-160,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 5 | 235 | 235 | 34,04% | 0,83 | -0,08R | €-196,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 9 | 482 | 482 | 36,72% | 0,95 | -0,03R | €-120,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 9 | 441 | 441 | 37,19% | 0,92 | -0,04R | €-157,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 130 | 130 | 35,38% | 0,75 | -0,13R | €-164,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 7 | 304 | 304 | 29,28% | 0,66 | -0,19R | €-569,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 9 | 471 | 471 | 30,79% | 0,73 | -0,14R | €-661,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 9 | 432 | 432 | 29,63% | 0,63 | -0,19R | €-824,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 9 | 482 | 482 | 37,14% | 0,97 | -0,01R | €-61,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 9 | 804 | 804 | 41,17% | 0,92 | -0,03R | €-269,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 4 | 143 | 143 | 33,57% | 0,57 | -0,27R | €-387,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 12 | 704 | 704 | 33,24% | 0,82 | -0,09R | €-636,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 12 | 708 | 708 | 33,19% | 0,82 | -0,09R | €-636,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 12 | 652 | 652 | 32,67% | 0,76 | -0,12R | €-774,27 |
| MAIN | 20 | 344 | 344 | 28,49% | 0,78 | -0,13R | €-441,64 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 50 | 50 | 38,00% | 0,67 | -0,18R | €-87,69 |
| Bilanciata 1H V1 | 20 | 845 | 845 | 35,86% | 0,95 | -0,03R | €-239,39 |
| Bilanciata 1H V2 | 5 | 317 | 276 | 41,01% | 1,20 | 0,10R | €321,92 |
| Bilanciata 1H V3 Filtered | 12 | 534 | 534 | 37,64% | 1,03 | 0,02R | €80,70 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 12 | 455 | 455 | 37,36% | 0,97 | -0,01R | €-64,64 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 4 | 243 | 243 | 39,09% | 0,92 | -0,04R | €-91,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 10 | 501 | 501 | 36,33% | 0,89 | -0,05R | €-275,52 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 10 | 568 | 568 | 37,15% | 0,91 | -0,04R | €-241,19 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 15 | 948 | 948 | 36,50% | 0,86 | -0,07R | €-673,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 11 | 542 | 542 | 38,56% | 0,93 | -0,03R | €-182,73 |
| SHADOW_1H_FAST_TP2_V1 | 15 | 905 | 905 | 33,92% | 0,85 | -0,08R | €-704,51 |
| Rapida 1H V2 | 2 | 75 | 65 | 42,67% | 0,84 | -0,08R | €-63,34 |
| Rapida 1H V3 Filtered | 12 | 885 | 885 | 37,06% | 0,88 | -0,06R | €-554,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 11 | 663 | 663 | 39,37% | 0,94 | -0,03R | €-197,25 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 5 | 278 | 278 | 48,92% | 1,00 | 0,00R | €1,78 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 5 | 281 | 281 | 38,79% | 0,97 | -0,01R | €-37,75 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 9 | 561 | 561 | 39,93% | 0,98 | -0,01R | €-66,75 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 9 | 585 | 585 | 34,87% | 0,81 | -0,10R | €-574,25 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 12 | 838 | 838 | 36,52% | 0,85 | -0,08R | €-636,47 |
| SHADOW_4H_WIDE | 31 | 325 | 325 | 23,69% | 0,83 | -0,11R | €-358,14 |
| SHADOW_BOLLINGER_MR_1H | 3 | 287 | 287 | 47,74% | 1,14 | 0,06R | €176,51 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 15 | 15 | 46,67% | 0,64 | -0,19R | €-28,10 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 2 | 2 | 50,00% | 2,26 | 0,67R | €13,50 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 9 | 9 | 77,78% | 3,40 | 0,60R | €54,38 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 17 | 17 | 29,41% | 0,32 | -0,54R | €-91,62 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 6 | 6 | 16,67% | 0,50 | -0,45R | €-26,75 |
| SHADOW_BTC_EMA_1H | 1 | 19 | 19 | 47,37% | 0,82 | -0,10R | €-19,47 |
| SHADOW_BTC_EMA_4H | 1 | 4 | 4 | 25,00% | 0,75 | -0,20R | €-8,17 |
| SHADOW_COMBO_ADAPTIVE | 14 | 701 | 701 | 38,66% | 1,02 | 0,01R | €81,70 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 9 | 433 | 433 | 39,95% | 1,09 | 0,05R | €199,03 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 13 | 770 | 770 | 41,95% | 1,04 | 0,02R | €134,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 14 | 642 | 642 | 40,97% | 0,97 | -0,01R | €-82,74 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 82 | 82 | 47,56% | 1,40 | 0,17R | €137,60 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 82 | 82 | 41,46% | 1,40 | 0,17R | €138,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 8 | 222 | 222 | 36,04% | 1,00 | 0,00R | €1,35 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 246 | 246 | 39,84% | 1,04 | 0,02R | €42,66 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 109 | 109 | 48,62% | 1,23 | 0,10R | €108,65 |
| SHADOW_COMBO_SCANNER | 9 | 437 | 437 | 38,22% | 1,15 | 0,08R | €327,83 |
| SHADOW_COMBO_TREND | 13 | 580 | 580 | 35,17% | 1,00 | 0,00R | €11,04 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 13 | 13 | 61,54% | 1,77 | 0,27R | €34,65 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 17 | 17 | 35,29% | 0,45 | -0,39R | €-66,91 |
| SHADOW_DOGE_EMA_1H | 0 | 28 | 28 | 28,57% | 0,42 | -0,41R | €-114,08 |
| SHADOW_DONCHIAN_1H | 12 | 306 | 306 | 33,33% | 0,91 | -0,06R | €-180,16 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 12 | 236 | 236 | 35,59% | 0,92 | -0,05R | €-115,08 |
| SHADOW_EMA_TREND_1H | 15 | 585 | 585 | 35,73% | 1,03 | 0,01R | €80,65 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 23 | 23 | 34,78% | 0,59 | -0,30R | €-67,99 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 15 | 15 | 60,00% | 1,86 | 0,32R | €47,90 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 22 | 22 | 27,27% | 0,43 | -0,46R | €-101,74 |
| SHADOW_ETH_EMA_1H | 1 | 32 | 32 | 37,50% | 0,54 | -0,31R | €-100,57 |
| SHADOW_ETH_EMA_4H | 1 | 6 | 6 | 33,33% | 0,46 | -0,38R | €-22,83 |
| SHADOW_GLOBAL_PURE | 0 | 14 | 14 | 42,86% | 0,90 | -0,07R | €-9,14 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 285 | 285 | 34,04% | 1,08 | 0,05R | €146,26 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 5 | 534 | 534 | 66,67% | 1,42 | 0,13R | €701,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 4 | 250 | 250 | 34,00% | 1,09 | 0,06R | €140,91 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 261 | 261 | 32,18% | 1,06 | 0,04R | €94,08 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 2 | 180 | 180 | 32,78% | 1,02 | 0,02R | €27,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 274 | 274 | 33,21% | 1,04 | 0,03R | €72,53 |
| Forza relativa 1H V1 | 18 | 704 | 704 | 31,96% | 0,93 | -0,04R | €-268,51 |
| Forza relativa 1H V2 | 9 | 290 | 271 | 38,62% | 1,23 | 0,11R | €328,20 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 5 | 229 | 229 | 26,64% | 0,52 | -0,28R | €-631,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 5 | 229 | 229 | 26,64% | 0,52 | -0,28R | €-631,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 5 | 229 | 229 | 26,64% | 0,52 | -0,28R | €-631,20 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 5 | 261 | 261 | 29,12% | 0,67 | -0,18R | €-476,49 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 5 | 269 | 269 | 52,79% | 0,78 | -0,10R | €-264,03 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 5 | 242 | 242 | 51,24% | 0,68 | -0,14R | €-343,81 |
| SHADOW_SCANNER_TOP10_LONG | 14 | 422 | 422 | 39,57% | 1,12 | 0,05R | €230,99 |
| SHADOW_SCANNER_TOP15_LONG | 14 | 422 | 422 | 39,57% | 1,11 | 0,05R | €225,24 |
| SHADOW_SCANNER_TOP20_LONG | 14 | 422 | 422 | 39,57% | 1,11 | 0,05R | €225,24 |
| SHADOW_SCANNER_TOP5_BTC | 9 | 423 | 423 | 37,83% | 1,16 | 0,08R | €347,72 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 3 | 152 | 152 | 30,26% | 0,77 | -0,14R | €-208,80 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 3 | 313 | 313 | 32,91% | 0,90 | -0,06R | €-172,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 1 | 329 | 329 | 44,07% | 1,14 | 0,06R | €191,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 2 | 276 | 276 | 34,42% | 0,98 | -0,01R | €-33,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 7 | 419 | 419 | 45,58% | 1,23 | 0,09R | €391,62 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 7 | 344 | 344 | 38,08% | 1,15 | 0,08R | €259,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 9 | 469 | 469 | 44,56% | 1,14 | 0,06R | €279,03 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 9 | 371 | 371 | 36,66% | 1,10 | 0,05R | €183,97 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 9 | 349 | 349 | 36,10% | 1,13 | 0,07R | €230,29 |
| SHADOW_SCANNER_TOP5_LONG | 9 | 464 | 464 | 39,22% | 1,17 | 0,08R | €392,16 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 30 | 30 | 36,67% | 0,77 | -0,16R | €-48,56 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 8 | 8 | 62,50% | 2,23 | 0,49R | €39,21 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 23 | 23 | 43,48% | 0,70 | -0,19R | €-43,78 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 5 | 5 | 60,00% | 1,99 | 0,41R | €20,58 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 24 | 24 | 45,83% | 1,01 | 0,01R | €1,83 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 7 | 7 | 42,86% | 1,26 | 0,16R | €10,86 |
| SHADOW_SOL_EMA_1H | 1 | 28 | 28 | 39,29% | 0,94 | -0,04R | €-11,26 |
| SHADOW_SOL_EMA_4H | 1 | 9 | 9 | 33,33% | 0,68 | -0,23R | €-20,41 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 3 | 74 | 74 | 32,43% | 0,63 | -0,21R | €-152,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 8 | 140 | 140 | 47,14% | 1,37 | 0,16R | €221,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 118 | 118 | 33,90% | 0,63 | -0,19R | €-227,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,71 | -0,15R | €-28,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 57 | 57 | 35,09% | 1,17 | 0,07R | €41,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 55 | 55 | 20,00% | 0,46 | -0,27R | €-146,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 3 | 68 | 68 | 32,35% | 0,50 | -0,30R | €-203,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 7 | 123 | 123 | 46,34% | 1,42 | 0,17R | €214,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 111 | 111 | 33,33% | 0,54 | -0,24R | €-269,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,69 | -0,17R | €-30,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 56 | 56 | 35,71% | 1,25 | 0,10R | €57,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 52 | 52 | 19,23% | 0,30 | -0,36R | €-186,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 10 | 10 | 50,00% | 0,87 | -0,07R | €-7,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 5 | 50 | 50 | 56,00% | 1,35 | 0,16R | €79,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 68 | 68 | 39,71% | 0,51 | -0,31R | €-208,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 35 | 35 | 57,14% | 1,45 | 0,17R | €60,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 40 | 40 | 45,00% | 0,87 | -0,06R | €-24,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,98 | -0,01R | €-0,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 5 | 50 | 50 | 42,00% | 1,29 | 0,14R | €67,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 71 | 71 | 33,80% | 0,50 | -0,28R | €-201,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 35 | 35 | 34,29% | 1,25 | 0,09R | €32,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 39 | 39 | 28,21% | 0,83 | -0,07R | €-25,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 35,71% | 0,66 | -0,14R | €-40,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 9 | 166 | 166 | 40,36% | 1,02 | 0,01R | €17,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 88 | 88 | 35,23% | 0,68 | -0,17R | €-151,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 47 | 47 | 36,17% | 1,37 | 0,14R | €66,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 57 | 57 | 31,58% | 0,81 | -0,09R | €-48,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 37,04% | 0,53 | -0,21R | €-55,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 8 | 149 | 149 | 41,61% | 1,12 | 0,06R | €83,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 77 | 77 | 36,36% | 0,59 | -0,21R | €-159,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 46 | 46 | 36,96% | 1,43 | 0,16R | €72,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 1 | 52 | 52 | 30,77% | 0,57 | -0,19R | €-100,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 128 | 128 | 35,16% | 0,73 | -0,14R | €-174,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 2 | 29 | 29 | 24,14% | 0,29 | -0,53R | €-154,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 5 | 56 | 56 | 32,14% | 0,80 | -0,12R | €-65,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 112 | 112 | 33,93% | 0,71 | -0,15R | €-168,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 36 | 36 | 27,78% | 0,94 | -0,03R | €-10,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 3 | 48 | 48 | 27,08% | 0,45 | -0,34R | €-161,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 6 | 65 | 65 | 36,92% | 1,10 | 0,05R | €33,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 148 | 148 | 33,11% | 0,66 | -0,18R | €-272,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 55 | 55 | 29,09% | 0,97 | -0,01R | €-6,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 74 | 74 | 25,68% | 0,64 | -0,17R | €-128,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 3 | 46 | 46 | 26,09% | 0,37 | -0,40R | €-183,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 5 | 53 | 53 | 37,74% | 1,13 | 0,07R | €36,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 0 | 138 | 138 | 31,88% | 0,57 | -0,23R | €-312,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 54 | 54 | 29,63% | 0,93 | -0,03R | €-14,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 69 | 69 | 24,64% | 0,46 | -0,27R | €-185,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 35,71% | 0,66 | -0,14R | €-40,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 9 | 167 | 167 | 40,72% | 1,05 | 0,02R | €37,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 88 | 88 | 37,50% | 0,80 | -0,10R | €-91,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 47 | 47 | 36,17% | 1,37 | 0,14R | €66,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 57 | 57 | 31,58% | 0,81 | -0,09R | €-48,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 3 | 110 | 110 | 39,09% | 0,64 | -0,18R | €-195,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 6 | 203 | 203 | 44,33% | 1,12 | 0,05R | €97,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 164 | 164 | 37,80% | 0,83 | -0,08R | €-124,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 32 | 32 | 34,38% | 0,58 | -0,23R | €-73,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 71 | 71 | 47,89% | 1,55 | 0,17R | €117,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 85 | 85 | 42,35% | 0,88 | -0,05R | €-46,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 28,57% | 0,39 | -0,45R | €-126,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 3 | 18 | 18 | 27,78% | 0,71 | -0,21R | €-38,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 50 | 50 | 40,00% | 0,55 | -0,26R | €-128,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 8 | 8 | 62,50% | 2,07 | 0,44R | €35,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 1 | 25 | 25 | 20,00% | 0,34 | -0,45R | €-113,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 3 | 92 | 92 | 28,26% | 0,50 | -0,28R | €-254,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 9 | 177 | 177 | 40,11% | 1,06 | 0,03R | €54,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 144 | 144 | 32,64% | 0,64 | -0,19R | €-277,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 65 | 65 | 35,38% | 1,38 | 0,15R | €95,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 73 | 73 | 24,66% | 0,58 | -0,20R | €-148,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 3 | 92 | 92 | 28,26% | 0,50 | -0,28R | €-254,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 9 | 179 | 179 | 40,22% | 1,08 | 0,04R | €63,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 145 | 145 | 32,41% | 0,63 | -0,20R | €-287,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 65 | 65 | 35,38% | 1,38 | 0,15R | €95,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 73 | 73 | 24,66% | 0,58 | -0,20R | €-148,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 3 | 86 | 86 | 29,07% | 0,44 | -0,32R | €-275,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 8 | 158 | 158 | 41,14% | 1,12 | 0,06R | €91,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 0 | 136 | 136 | 30,88% | 0,50 | -0,27R | €-363,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 28 | 28 | 25,00% | 0,63 | -0,20R | €-56,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 64 | 64 | 35,94% | 1,43 | 0,16R | €103,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 68 | 68 | 23,53% | 0,38 | -0,31R | €-210,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 3 | 27 | 27 | 25,93% | 0,66 | -0,20R | €-52,95 |
| MAIN | ALT_ROTATION_UP | 11 | 80 | 80 | 30,00% | 0,63 | -0,23R | €-187,30 |
| MAIN | RANGE | 0 | 77 | 77 | 22,08% | 0,65 | -0,22R | €-165,89 |
| MAIN | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 2 | 38 | 38 | 26,32% | 0,70 | -0,19R | €-71,12 |
| MAIN | TREND_DOWN | 1 | 46 | 46 | 28,26% | 0,79 | -0,12R | €-57,38 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 2 | 40 | 40 | 30,00% | 1,01 | 0,00R | €1,45 |
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
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 89 | 89 | 25,84% | 0,53 | -0,29R | €-258,80 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 12 | 186 | 186 | 43,55% | 1,16 | 0,08R | €151,22 |
| Bilanciata 1H V1 | RANGE | 0 | 180 | 180 | 39,44% | 1,05 | 0,03R | €49,57 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 46 | 46 | 26,09% | 0,50 | -0,34R | €-156,31 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 1 | 101 | 101 | 36,63% | 1,15 | 0,07R | €75,40 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 1 | 111 | 111 | 30,63% | 0,94 | -0,03R | €-30,97 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 5 | 102 | 86 | 50,00% | 1,69 | 0,29R | €297,24 |
| Bilanciata 1H V2 | RANGE | 0 | 130 | 117 | 34,62% | 0,83 | -0,10R | €-127,97 |
| Bilanciata 1H V2 | TRANSITION | 0 | 85 | 73 | 40,00% | 1,38 | 0,18R | €152,65 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 67 | 67 | 28,36% | 0,51 | -0,31R | €-204,76 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 8 | 106 | 106 | 45,28% | 1,48 | 0,23R | €240,13 |
| Bilanciata 1H V3 Filtered | RANGE | 0 | 124 | 124 | 40,32% | 1,07 | 0,03R | €40,92 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,56 | -0,28R | €-50,80 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 55 | 55 | 34,55% | 1,07 | 0,03R | €17,93 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 64 | 64 | 31,25% | 1,09 | 0,04R | €27,77 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 3 | 56 | 56 | 25,00% | 0,33 | -0,43R | €-238,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 8 | 104 | 104 | 46,15% | 1,54 | 0,25R | €261,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 0 | 102 | 102 | 38,24% | 0,86 | -0,07R | €-75,24 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 31,25% | 0,69 | -0,19R | €-29,97 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 47 | 47 | 34,04% | 1,06 | 0,03R | €12,25 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 1 | 43 | 43 | 25,58% | 0,84 | -0,08R | €-33,07 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 29,41% | 0,73 | -0,13R | €-22,62 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 4 | 76 | 76 | 44,74% | 0,98 | -0,01R | €-6,02 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 51 | 51 | 41,18% | 0,97 | -0,01R | €-6,96 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,70 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 29 | 29 | 44,83% | 1,30 | 0,13R | €37,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 53 | 53 | 33,96% | 0,93 | -0,03R | €-14,85 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 3 | 46 | 46 | 34,78% | 0,92 | -0,03R | €-16,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 7 | 73 | 73 | 46,58% | 1,22 | 0,10R | €72,21 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 0 | 155 | 155 | 35,48% | 0,78 | -0,11R | €-177,52 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 65 | 65 | 41,54% | 1,20 | 0,08R | €48,90 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 79 | 79 | 30,38% | 0,83 | -0,07R | €-57,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 3 | 64 | 64 | 31,25% | 0,72 | -0,15R | €-98,23 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 7 | 74 | 74 | 47,30% | 1,26 | 0,12R | €86,10 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 0 | 185 | 185 | 39,46% | 0,96 | -0,02R | €-32,33 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 67 | 67 | 43,28% | 1,32 | 0,12R | €78,59 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 95 | 95 | 29,47% | 0,72 | -0,14R | €-129,88 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 4 | 126 | 126 | 30,95% | 0,64 | -0,21R | €-260,87 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 11 | 214 | 214 | 41,12% | 0,93 | -0,03R | €-70,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 0 | 213 | 213 | 37,09% | 0,83 | -0,09R | €-188,26 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 40 | 40 | 37,50% | 0,86 | -0,07R | €-29,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 92 | 92 | 42,39% | 1,37 | 0,14R | €125,93 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 109 | 109 | 29,36% | 0,73 | -0,14R | €-147,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 49 | 49 | 46,94% | 1,55 | 0,20R | €97,83 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 72 | 72 | 29,17% | 0,49 | -0,33R | €-234,92 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 7 | 128 | 128 | 46,09% | 1,23 | 0,10R | €129,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 119 | 119 | 42,02% | 1,06 | 0,03R | €37,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 41,18% | 0,87 | -0,07R | €-11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 54 | 54 | 40,74% | 1,32 | 0,12R | €63,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 63 | 63 | 28,57% | 0,65 | -0,19R | €-118,58 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 4 | 122 | 122 | 30,33% | 0,64 | -0,20R | €-243,36 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 10 | 217 | 217 | 41,01% | 1,06 | 0,03R | €61,57 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 195 | 195 | 34,87% | 0,80 | -0,11R | €-206,82 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 39 | 39 | 28,21% | 0,64 | -0,20R | €-78,08 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 84 | 84 | 39,29% | 1,45 | 0,17R | €144,45 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 98 | 98 | 22,45% | 0,52 | -0,25R | €-246,48 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 2 | 22 | 20 | 40,91% | 0,82 | -0,12R | €-25,45 |
| Rapida 1H V2 | RANGE | 0 | 44 | 36 | 40,91% | 0,84 | -0,08R | €-36,12 |
| Rapida 1H V2 | TRANSITION | 0 | 9 | 9 | 55,56% | 0,95 | -0,02R | €-1,77 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 120 | 120 | 30,00% | 0,53 | -0,28R | €-330,40 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 9 | 198 | 198 | 43,94% | 1,11 | 0,05R | €102,84 |
| Rapida 1H V3 Filtered | RANGE | 0 | 188 | 188 | 37,23% | 0,82 | -0,09R | €-176,31 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 34 | 34 | 38,24% | 0,87 | -0,07R | €-23,20 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 80 | 80 | 38,75% | 1,17 | 0,07R | €56,25 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 112 | 112 | 37,50% | 1,02 | 0,01R | €9,87 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 60 | 60 | 36,67% | 0,90 | -0,05R | €-32,12 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 3 | 96 | 96 | 33,33% | 0,58 | -0,25R | €-241,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 8 | 156 | 156 | 49,36% | 1,35 | 0,14R | €222,23 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 149 | 149 | 38,26% | 0,88 | -0,06R | €-88,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 22 | 22 | 40,91% | 0,94 | -0,03R | €-6,30 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 60 | 60 | 40,00% | 1,14 | 0,06R | €35,63 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 73 | 73 | 30,14% | 0,71 | -0,15R | €-107,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 29,41% | 0,28 | -0,53R | €-89,36 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 5 | 57 | 57 | 57,89% | 1,35 | 0,15R | €85,74 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 83 | 83 | 43,37% | 0,86 | -0,08R | €-68,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 36 | 36 | 58,33% | 1,61 | 0,21R | €77,08 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 51 | 51 | 50,98% | 1,05 | 0,02R | €11,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 18,75% | 0,28 | -0,52R | €-83,03 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 5 | 57 | 57 | 45,61% | 1,22 | 0,10R | €56,94 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 86 | 86 | 40,70% | 0,94 | -0,03R | €-25,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 36 | 36 | 41,67% | 1,41 | 0,14R | €51,95 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 52 | 52 | 34,62% | 0,97 | -0,01R | €-5,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 38 | 38 | 26,32% | 0,35 | -0,38R | €-144,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 9 | 187 | 187 | 43,32% | 1,06 | 0,03R | €56,16 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 108 | 108 | 41,67% | 0,97 | -0,01R | €-15,59 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 52 | 52 | 42,31% | 1,31 | 0,12R | €62,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 71 | 71 | 35,21% | 0,93 | -0,03R | €-24,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 44,74% | 1,30 | 0,13R | €50,46 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 70 | 70 | 28,57% | 0,50 | -0,31R | €-218,40 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 6 | 72 | 72 | 41,67% | 1,06 | 0,03R | €21,54 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 0 | 190 | 190 | 38,42% | 0,87 | -0,07R | €-128,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 63 | 63 | 34,92% | 1,03 | 0,01R | €7,44 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 98 | 98 | 32,65% | 0,81 | -0,10R | €-95,32 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 119 | 119 | 30,25% | 0,54 | -0,27R | €-318,97 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 9 | 197 | 197 | 43,15% | 1,07 | 0,03R | €61,72 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 186 | 186 | 37,10% | 0,80 | -0,10R | €-191,04 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,92 | -0,04R | €-13,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 75 | 75 | 38,67% | 1,20 | 0,08R | €59,01 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 95 | 95 | 31,58% | 0,77 | -0,12R | €-112,88 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 42,50% | 1,23 | 0,10R | €40,19 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 5 | 25 | 25 | 28,00% | 1,29 | 0,16R | €39,17 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 13 | 64 | 64 | 37,50% | 1,01 | 0,00R | €2,16 |
| SHADOW_4H_WIDE | RANGE | 2 | 73 | 73 | 15,07% | 0,62 | -0,26R | €-187,47 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 39 | 39 | 15,38% | 0,45 | -0,40R | €-156,04 |
| SHADOW_4H_WIDE | TREND_DOWN | 2 | 45 | 45 | 26,67% | 0,96 | -0,03R | €-11,28 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 40 | 40 | 22,50% | 0,95 | -0,03R | €-12,13 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 3 | 19 | 19 | 21,05% | 0,75 | -0,17R | €-31,47 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 27 | 27 | 40,74% | 0,80 | -0,10R | €-28,26 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 2 | 88 | 88 | 48,86% | 1,20 | 0,08R | €69,02 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 69 | 69 | 44,93% | 0,98 | -0,01R | €-6,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 60,00% | 2,25 | 0,41R | €41,08 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 15 | 15 | 60,00% | 2,13 | 0,41R | €60,85 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
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
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,41R | €24,09 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 5 | 74 | 74 | 25,68% | 0,59 | -0,25R | €-181,54 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 8 | 155 | 155 | 43,87% | 1,17 | 0,09R | €138,49 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 149 | 149 | 42,28% | 1,00 | -0,00R | €-2,37 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 32 | 32 | 37,50% | 0,88 | -0,06R | €-19,15 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 79 | 79 | 41,77% | 1,41 | 0,18R | €144,06 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 75 | 75 | 34,67% | 0,89 | -0,05R | €-37,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 97 | 97 | 37,11% | 1,14 | 0,06R | €60,16 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 26 | 26 | 19,23% | 0,54 | -0,26R | €-67,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 8 | 147 | 147 | 43,54% | 1,14 | 0,07R | €105,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 75 | 75 | 49,33% | 1,31 | 0,14R | €108,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 42 | 42 | 45,24% | 2,11 | 0,33R | €138,78 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 56 | 56 | 30,36% | 0,69 | -0,14R | €-79,48 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 4 | 92 | 92 | 36,96% | 0,73 | -0,13R | €-119,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 7 | 178 | 178 | 40,45% | 1,04 | 0,02R | €33,10 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 148 | 148 | 41,89% | 1,16 | 0,07R | €105,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 38 | 38 | 42,11% | 0,80 | -0,09R | €-32,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 69 | 69 | 47,83% | 1,31 | 0,12R | €83,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 98 | 98 | 36,73% | 0,88 | -0,05R | €-46,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 99 | 99 | 50,51% | 1,33 | 0,13R | €131,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 5 | 74 | 74 | 25,68% | 0,60 | -0,24R | €-175,19 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 8 | 153 | 153 | 44,44% | 1,10 | 0,05R | €81,60 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 137 | 137 | 45,26% | 1,05 | 0,02R | €33,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 30 | 30 | 43,33% | 1,03 | 0,01R | €3,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 62 | 62 | 46,77% | 1,37 | 0,16R | €96,12 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 75 | 75 | 38,67% | 0,90 | -0,05R | €-33,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 76 | 76 | 38,16% | 0,78 | -0,10R | €-75,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 36 | 36 | 36,11% | 0,91 | -0,05R | €-17,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,69 | 0,49R | €88,88 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 36 | 36 | 36,11% | 0,90 | -0,06R | €-20,39 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 55,56% | 3,14 | 0,62R | €112,49 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 17 | 17 | 11,76% | 0,05 | -0,59R | €-101,04 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 5 | 66 | 66 | 42,42% | 1,06 | 0,03R | €21,92 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 42 | 42 | 38,10% | 1,02 | 0,01R | €4,16 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 29 | 29 | 34,48% | 0,98 | -0,01R | €-3,69 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 93 | 93 | 39,78% | 1,04 | 0,02R | €18,42 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 102 | 102 | 35,29% | 0,83 | -0,08R | €-81,74 |
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
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 27 | 27 | 14,81% | 0,17 | -0,58R | €-157,00 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 8 | 117 | 117 | 43,59% | 1,28 | 0,15R | €171,21 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 84 | 84 | 46,43% | 1,45 | 0,21R | €179,30 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 60 | 60 | 43,33% | 1,81 | 0,34R | €202,88 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 65 | 65 | 30,77% | 1,08 | 0,04R | €27,33 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 4 | 56 | 56 | 30,36% | 0,62 | -0,23R | €-128,49 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 7 | 133 | 133 | 42,86% | 1,17 | 0,09R | €120,73 |
| SHADOW_COMBO_TREND | RANGE | 0 | 128 | 128 | 35,16% | 1,04 | 0,02R | €24,85 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 23 | 23 | 34,78% | 1,15 | 0,07R | €15,88 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 66 | 66 | 36,36% | 1,32 | 0,16R | €107,41 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 67 | 67 | 29,85% | 0,70 | -0,16R | €-107,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 1 | 75 | 75 | 29,33% | 1,06 | 0,03R | €20,85 |
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
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 42 | 42 | 23,81% | 0,47 | -0,40R | €-167,77 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 8 | 73 | 73 | 35,62% | 0,79 | -0,14R | €-100,54 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 65 | 65 | 32,31% | 1,02 | 0,01R | €8,90 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 28 | 28 | 39,29% | 1,47 | 0,23R | €64,33 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 23 | 23 | 52,17% | 1,69 | 0,35R | €80,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 2 | 32 | 32 | 21,88% | 0,31 | -0,55R | €-176,25 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 8 | 65 | 65 | 38,46% | 0,88 | -0,08R | €-50,12 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 0 | 45 | 45 | 33,33% | 0,98 | -0,01R | €-6,16 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 21 | 21 | 47,62% | 2,13 | 0,45R | €93,60 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 58,82% | 2,03 | 0,44R | €75,25 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 59 | 59 | 28,81% | 0,55 | -0,28R | €-166,25 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 8 | 131 | 131 | 45,04% | 1,27 | 0,14R | €183,34 |
| SHADOW_EMA_TREND_1H | RANGE | 0 | 125 | 125 | 35,20% | 1,08 | 0,04R | €49,33 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 64 | 64 | 34,38% | 1,16 | 0,09R | €56,98 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 77 | 77 | 28,57% | 0,98 | -0,01R | €-9,44 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 4 | 37 | 37 | 35,14% | 1,06 | 0,04R | €14,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 0 | 81 | 81 | 32,10% | 1,04 | 0,02R | €18,15 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 2 | 35 | 35 | 45,71% | 1,89 | 0,42R | €146,99 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 61 | 61 | 29,51% | 0,85 | -0,10R | €-61,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 33 | 33 | 54,55% | 0,92 | -0,03R | €-11,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 5 | 83 | 83 | 74,70% | 2,06 | 0,26R | €212,69 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 149 | 149 | 66,44% | 1,46 | 0,14R | €213,68 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 79 | 79 | 72,15% | 1,77 | 0,20R | €154,65 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 112 | 112 | 63,39% | 1,13 | 0,05R | €52,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,95 | -0,03R | €-6,33 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 0 | 82 | 82 | 34,15% | 1,14 | 0,08R | €66,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 3 | 35 | 35 | 40,00% | 1,46 | 0,25R | €86,43 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 67 | 67 | 28,36% | 0,80 | -0,14R | €-92,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 37,50% | 1,39 | 0,23R | €36,29 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 40 | 40 | 30,00% | 0,84 | -0,11R | €-45,72 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 0 | 74 | 74 | 31,08% | 1,15 | 0,09R | €65,91 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 2 | 31 | 31 | 41,94% | 1,67 | 0,34R | €103,99 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 58 | 58 | 24,14% | 0,68 | -0,23R | €-135,37 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,17 | -0,72R | €-94,10 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 59 | 59 | 35,59% | 1,11 | 0,07R | €41,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 28 | 28 | 46,43% | 2,20 | 0,50R | €139,19 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 47 | 47 | 34,04% | 1,06 | 0,04R | €18,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,88 | -0,08R | €-16,20 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 4 | 39 | 39 | 35,90% | 1,09 | 0,06R | €22,42 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 0 | 77 | 77 | 33,77% | 1,14 | 0,08R | €61,59 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 2 | 34 | 34 | 41,18% | 1,55 | 0,29R | €97,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 61 | 61 | 24,59% | 0,66 | -0,25R | €-150,15 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 6 | 69 | 69 | 26,09% | 0,53 | -0,30R | €-206,48 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 7 | 156 | 156 | 41,03% | 1,15 | 0,08R | €132,04 |
| Forza relativa 1H V1 | RANGE | 1 | 169 | 169 | 30,18% | 0,81 | -0,10R | €-171,44 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 28 | 28 | 28,57% | 0,53 | -0,25R | €-70,96 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 1 | 75 | 75 | 36,00% | 1,38 | 0,19R | €140,17 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 75 | 75 | 28,00% | 0,87 | -0,07R | €-51,18 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 97 | 97 | 25,77% | 0,93 | -0,04R | €-34,05 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 32 | 32 | 28,12% | 0,88 | -0,08R | €-24,67 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 3 | 32 | 32 | 37,50% | 0,71 | -0,15R | €-47,81 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 3 | 56 | 51 | 48,21% | 1,68 | 0,31R | €174,94 |
| Forza relativa 1H V2 | RANGE | 1 | 74 | 71 | 33,78% | 0,88 | -0,07R | €-50,90 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 0 | 43 | 38 | 39,53% | 1,71 | 0,33R | €140,20 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 35 | 34 | 28,57% | 0,95 | -0,02R | €-7,36 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 1 | 37 | 34 | 45,95% | 1,83 | 0,37R | €137,96 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 3 | 47 | 47 | 19,15% | 0,28 | -0,49R | €-231,74 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 0 | 61 | 61 | 22,95% | 0,33 | -0,39R | €-236,25 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 23 | 23 | 43,48% | 1,19 | 0,10R | €23,62 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 3 | 47 | 47 | 19,15% | 0,28 | -0,49R | €-231,74 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 0 | 61 | 61 | 22,95% | 0,33 | -0,39R | €-236,25 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 23 | 23 | 43,48% | 1,19 | 0,10R | €23,62 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 3 | 47 | 47 | 19,15% | 0,28 | -0,49R | €-231,74 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 0 | 61 | 61 | 22,95% | 0,33 | -0,39R | €-236,25 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 23 | 23 | 43,48% | 1,19 | 0,10R | €23,62 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 3 | 42 | 42 | 26,19% | 0,55 | -0,27R | €-114,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 46,67% | 1,70 | 0,29R | €44,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 74 | 74 | 28,38% | 0,61 | -0,21R | €-156,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,33 | 0,13R | €23,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 39 | 39 | 38,46% | 1,02 | 0,01R | €4,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 3 | 49 | 49 | 51,02% | 0,59 | -0,19R | €-91,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 45,45% | 1,12 | 0,06R | €6,29 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 0 | 66 | 66 | 53,03% | 0,64 | -0,16R | €-104,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 22 | 22 | 63,64% | 1,42 | 0,16R | €34,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 30 | 30 | 60,00% | 1,46 | 0,20R | €58,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 3 | 41 | 41 | 46,34% | 0,40 | -0,29R | €-120,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,55 | 0,22R | €28,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 0 | 59 | 59 | 52,54% | 0,38 | -0,27R | €-159,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 60,00% | 1,23 | 0,10R | €19,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 29 | 29 | 62,07% | 1,60 | 0,24R | €70,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 22 | 22 | 27,27% | 0,71 | -0,15R | €-32,96 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 12 | 150 | 150 | 42,00% | 1,09 | 0,05R | €72,28 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 46 | 46 | 39,13% | 1,65 | 0,22R | €100,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 1 | 49 | 49 | 28,57% | 0,66 | -0,15R | €-75,39 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 22 | 22 | 27,27% | 0,71 | -0,15R | €-32,89 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 12 | 152 | 152 | 42,76% | 1,09 | 0,05R | €73,71 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 46 | 46 | 39,13% | 1,65 | 0,22R | €100,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 1 | 49 | 49 | 28,57% | 0,66 | -0,15R | €-75,39 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 22 | 22 | 27,27% | 0,71 | -0,15R | €-32,89 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 12 | 152 | 152 | 42,76% | 1,09 | 0,05R | €73,71 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 46 | 46 | 39,13% | 1,65 | 0,22R | €100,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 1 | 49 | 49 | 28,57% | 0,66 | -0,15R | €-75,39 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 25 | 25 | 16,00% | 0,19 | -0,54R | €-134,88 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 8 | 117 | 117 | 43,59% | 1,28 | 0,15R | €171,80 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 79 | 79 | 46,84% | 1,60 | 0,27R | €212,29 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 55 | 55 | 41,82% | 1,82 | 0,34R | €188,19 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 64 | 64 | 29,69% | 1,02 | 0,01R | €6,62 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,05 | -0,75R | €-89,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 3 | 50 | 50 | 34,00% | 0,77 | -0,15R | €-75,37 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 23 | 23 | 47,83% | 2,22 | 0,43R | €100,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 49 | 49 | 28,57% | 0,89 | -0,05R | €-25,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 10,00% | 0,05 | -0,69R | €-138,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 3 | 64 | 64 | 32,81% | 0,78 | -0,13R | €-85,61 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,46 | 0,21R | €159,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 43 | 43 | 44,19% | 2,27 | 0,43R | €184,01 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 43 | 43 | 20,93% | 0,55 | -0,24R | €-105,34 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,24 | -0,62R | €-80,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,28 | -0,33R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 1 | 59 | 59 | 38,98% | 0,99 | -0,01R | €-3,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 44 | 44 | 47,73% | 1,36 | 0,14R | €60,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 46 | 46 | 52,17% | 1,34 | 0,14R | €64,25 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 0,38 | -0,38R | €-18,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,07 | -0,66R | €-104,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 48 | 48 | 33,33% | 0,92 | -0,05R | €-24,41 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 40 | 40 | 37,50% | 1,72 | 0,28R | €112,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 35 | 35 | 22,86% | 0,66 | -0,18R | €-62,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,85R | €-51,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 25 | 25 | 36,00% | 0,67 | -0,14R | €-34,78 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 5 | 118 | 118 | 44,07% | 1,22 | 0,10R | €115,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 46 | 46 | 45,65% | 1,28 | 0,11R | €50,09 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 51 | 51 | 49,02% | 1,31 | 0,13R | €64,02 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 20,00% | 0,26 | -0,46R | €-91,75 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 6 | 97 | 97 | 45,36% | 1,42 | 0,22R | €210,38 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 41 | 41 | 36,59% | 1,62 | 0,25R | €102,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 40 | 40 | 22,50% | 0,70 | -0,16R | €-63,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 31 | 31 | 35,48% | 0,53 | -0,20R | €-63,50 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 7 | 135 | 135 | 42,96% | 1,09 | 0,04R | €53,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 81 | 81 | 46,91% | 1,52 | 0,20R | €162,96 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,61 | -0,16R | €-26,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 51 | 51 | 49,02% | 1,45 | 0,16R | €83,62 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 1 | 63 | 63 | 49,21% | 1,32 | 0,12R | €74,40 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 22,22% | 0,28 | -0,46R | €-83,45 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 8 | 117 | 117 | 42,74% | 1,28 | 0,15R | €171,47 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 0 | 70 | 70 | 44,29% | 1,49 | 0,23R | €162,79 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 43 | 43 | 41,86% | 2,01 | 0,36R | €156,51 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 48 | 48 | 20,83% | 0,59 | -0,22R | €-105,63 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 17,65% | 0,09 | -0,61R | €-103,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 6 | 112 | 112 | 42,86% | 1,33 | 0,17R | €192,32 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 65 | 65 | 43,08% | 1,53 | 0,26R | €169,81 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 37 | 37 | 40,54% | 2,51 | 0,47R | €173,66 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 46 | 46 | 19,57% | 0,54 | -0,25R | €-113,52 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 31 | 31 | 22,58% | 0,46 | -0,33R | €-101,29 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 7 | 119 | 119 | 42,02% | 1,14 | 0,07R | €86,02 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 81 | 81 | 49,38% | 1,55 | 0,24R | €194,78 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 59 | 59 | 40,68% | 1,64 | 0,25R | €147,01 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 1 | 80 | 80 | 36,25% | 1,14 | 0,06R | €50,93 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 8 | 8 | 62,50% | 2,12 | 0,46R | €36,64 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,75 | -0,18R | €-14,00 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,43R | €24,29 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 100,00% | ∞ | 1,14R | €34,32 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 75,00% | 1,91 | 0,24R | €9,76 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 22,22% | 0,22 | -0,66R | €-59,58 |
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
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 6 | 6 | 50,00% | 1,22 | 0,12R | €7,28 |
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
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 1 | 7 | 7 | 71,43% | 3,21 | 0,68R | €47,75 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 1,02 | 0,01R | €1,11 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 1,15 | 0,11R | €3,17 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 1,81 | 0,28R | €8,45 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-27T16:08:50+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **720**
- Scenari virtuali ancora attivi: **12691**
- Gruppi in attesa dell'uscita originale: **360**
- Gruppi con originale chiuso ma Shadow ancora attive: **360**
- Confronti completati: **402124**

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

Generato: 2026-08-27T16:10:00+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **402124**
- Valutazioni prodotte: **25278**
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

Generato: 2026-08-27T16:14:41+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Operativo | Identità | Gross cert. | Net cert. | Pending | Gap | Conflict | Formal review NET | PF storico | PnL storico | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,16 | +€67,59 | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,01 | +€2,56 | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,11 | +€95,26 | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,09 | +€75,72 | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | 90 | 88 | 18 | 0 | 4 | 65 | 1 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,55 | +€846,28 | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | 38 | 35 | 11 | 0 | 1 | 21 | 2 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 5,77 | +€1.682,13 | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | 154 | 138 | 20 | 0 | 6 | 109 | 3 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,65 | +€1.253,39 | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 0,00 | €0,00 | COLLECTING |

## Regole di valutazione

- Il campione operativo resta esposto per continuità storica, ma non è il campione formale.
- La soglia 50 usa esclusivamente NET_CERTIFIED_CLOSED_PAIRS.
- P0C produce FORMAL_CERTIFIED_OUTCOME; Block-3 produce SIMULATION_RUNTIME_OUTCOME.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-27T16:06:02+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **51**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **629.61 R**
- Profitto virtuale mancato: **1099.26 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 280 | 0 | 27293.81 |
| DOWN_20 | 280 | 0 | 54587.63 |
| DOWN_30 | 280 | 0 | 81881.44 |
| DOWN_40 | 280 | 95 | 102203.06 |
| UP_10 | 74 | 0 | 3730.86 |
| UP_20 | 74 | 0 | 7461.72 |
| UP_30 | 74 | 1 | 11156.53 |
| UP_40 | 74 | 24 | 14367.84 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-27T16:05:18+00:00

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

Generato: 2026-08-27T16:14:48+00:00

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

Generato: 2026-08-27T16:14:48+00:00

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

Generato: 2026-08-27T16:14:48+00:00

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

Generato: 2026-08-27T16:14:48+00:00

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
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 23.7 | E | 115 | 1.76 | 0.350 | 14.44 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 23.4 | E | 150 | 1.44 | 0.202 | 16.35 |
| 3 | SHADOW_COMBO_ADAPTIVE | BASELINE | 22.6 | E | 150 | 1.41 | 0.194 | 14.19 |
| 4 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 20.2 | E | 193 | 1.18 | 0.087 | 30.08 |
| 5 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 19.9 | E | 221 | 1.20 | 0.099 | 25.70 |
| 6 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 19.5 | E | 36 | 1.80 | 0.378 | 4.71 |
| 7 | SHADOW_1H_FAST_V3 | BASELINE | 19.2 | E | 237 | 1.15 | 0.073 | 29.54 |
| 8 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | BASELINE | 19.1 | E | 154 | 1.13 | 0.071 | 22.70 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | BASELINE | 18.0 | E | 161 | 1.06 | 0.030 | 23.64 |
| 10 | SHADOW_DONCHIAN_1H | BASELINE | 17.9 | E | 108 | 1.36 | 0.206 | 17.00 |

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

Generato: 2026-08-27T16:14:49+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BULL_TREND**
- Righe di performance: **1098**
- Strategie preferite nel regime corrente: **18**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **524**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.621 | 0.00 |
| 2 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | INSUFFICIENT | 79.0 | 4 | 60.90 | 1.174 | 0.08 |
| 3 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.8 | 12 | 4.37 | 0.378 | 1.07 |
| 4 | SHADOW_DOGE_BOLLINGER_1H | shadow-doge-bollinger-1h | INSUFFICIENT | 74.5 | 3 | 1.98 | 0.477 | 1.47 |
| 5 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | shadow-1h-fast-v3-no-esports-mfe-lock-v1 | SPECIALIST | 73.8 | 67 | 1.75 | 0.321 | 11.23 |
| 6 | SHADOW_SCANNER_TOP15_LONG | shadow-scanner-top15-long | COMPATIBLE | 72.9 | 58 | 1.82 | 0.342 | 8.96 |
| 7 | SHADOW_SCANNER_TOP20_LONG | shadow-scanner-top20-long | COMPATIBLE | 72.9 | 58 | 1.82 | 0.342 | 8.96 |
| 8 | SHADOW_SOL_ADAPTIVE_1H | shadow-sol-adaptive-1h | INSUFFICIENT | 72.7 | 5 | 4.06 | 0.720 | 1.17 |
| 9 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | SPECIALIST | 71.8 | 55 | 1.72 | 0.343 | 12.54 |
| 10 | SHADOW_SOL_ADAPTIVE_4H | shadow-sol-adaptive-4h | INSUFFICIENT | 70.0 | 4 | 2.56 | 0.460 | 1.04 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-27T16:14:49+00:00

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

Generato: 2026-08-27T16:06:02+00:00

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
