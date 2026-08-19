# Paper trading automatico KuCoin

Generato: 2026-08-19T04:09:06+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-19T04:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-19T04:05:28+00:00 | 2026-08-19T04:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-19T03:45:00+00:00 | 2026-08-19T03:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-19T03:00:00+00:00 | 2026-08-19T03:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-19T00:00:00+00:00 | 2026-08-19T00:00:00+00:00 | 5,6 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive GB20 — Loss Cap 0,75R | SOL | 60m | LONG | 3,47 | 0,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — 50% a 0,75R | SOL | 60m | LONG | 3,47 | 0,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Breakeven 0,5R | SOL | 60m | LONG | 3,47 | 0,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | SOL | 60m | LONG | 3,47 | 0,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | SOL | 60m | LONG | 3,47 | 0,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | SOL | 60m | LONG | 3,47 | 0,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ACE | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ACE | 240m | LONG | 7,75 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | SOXL | 240m | SHORT | -6,75 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | ETH | 240m | LONG | 4,99 | 6,00 | 1,01 | BELOW_SCORE | 5,6 min | D: n/a | W: n/a | peso 0 | Punteggio +4.99; soglia ±6.00; mancano 1.01 punti. |
| Principale 4H | DOGE | 240m | SHORT | -4,95 | 6,00 | 1,05 | BELOW_SCORE | 5,6 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Punteggio -4.95; soglia ±6.00; mancano 1.05 punti. |
| Principale 4H | SOL | 240m | LONG | 4,92 | 6,00 | 1,08 | BELOW_SCORE | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Punteggio +4.92; soglia ±6.00; mancano 1.08 punti. |
| Principale 4H | SKHYNIX | 240m | SHORT | -4,90 | 6,00 | 1,10 | BELOW_SCORE | 5,6 min | D: n/a | W: n/a | peso 0 | Punteggio -4.90; soglia ±6.00; mancano 1.10 punti. |
| Ampia 4H | ACE | 240m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| MAIN — Side × Regime Guard | ACE | 240m | LONG | 7,75 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| MAIN — Dynamic Asset Selector | ACE | 240m | LONG | 7,75 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Ampia 4H | SOXL | 240m | SHORT | -6,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V1 | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | SKHYNIX | 60m | SHORT | -6,14 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — target pieno 2R | SKHYNIX | 60m | SHORT | -6,14 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom 5 Short 1H | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom10 Short | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom15 Short | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom20 Short | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom5 Short Profit Lock V1 | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom5 Short Mfe Trail V1 | SKHYNIX | 60m | SHORT | -6,14 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — no HIGH + score <7,5 | ACE | 60m | LONG | 5,75 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.644,21 | -3,56% | €-104,14 | €3.000,00 | -3,47% | 6 | 42 | 33,33% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 42 | 1602 | PRIME INDICAZIONI | 50 (mancano 8) |

- Trade del Principale 4H chiusi: **42**; win rate **33,33%**; profit factor **0,72**.
- Expectancy: **€-9,04** per trade; P&L netto: **€-379,65**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.644,21 | €1.281,99 | €3.845,96 | €192,75 | €22,64 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.670,85 | €3.807,11 | €7.614,22 | €55,33 | €71,87 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.419,62 | €3.717,48 | €7.434,96 | €54,03 | €70,18 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.415,99 | €1.752,90 | €5.258,70 | €103,53 | €69,67 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.375,15 | €3.144,71 | €9.434,12 | €105,66 | €-54,54 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.347,47 | €1.934,28 | €5.802,85 | €207,05 | €13,45 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.332,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.270,51 | €4.336,32 | €13.008,97 | €205,10 | €12,22 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 1 | €10.239,14 | €1.508,82 | €4.526,45 | €50,70 | €17,89 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.229,96 | €142,09 | €426,26 | €51,15 | €-0,09 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 6 | €10.224,66 | €1.641,80 | €4.925,41 | €204,02 | €29,14 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 6 | €10.142,73 | €2.871,87 | €8.615,60 | €202,91 | €-21,46 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 2 | €10.126,47 | €3.135,06 | €6.270,11 | €100,32 | €-2,58 |
| TEST | Btc Bollinger 4H | 1 | €10.108,03 | €1.575,64 | €3.151,29 | €50,42 | €25,76 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 1 | €10.090,88 | €1.170,75 | €3.512,25 | €50,58 | €-19,03 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.086,10 | €2.265,49 | €4.530,99 | €153,17 | €-48,52 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €10.039,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €9.997,44 | €4.221,03 | €12.663,09 | €199,65 | €11,89 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.991,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 6 | €9.970,23 | €1.600,95 | €4.802,84 | €198,95 | €28,42 |
| TEST | Ampia 4H | 6 | €9.968,38 | €1.633,87 | €3.267,74 | €199,26 | €17,39 |
| TEST | Btc Adaptive 1H | 1 | €9.960,08 | €1.156,05 | €3.468,16 | €49,94 | €-26,14 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.942,05 | €1.298,67 | €3.896,00 | €49,87 | €-29,37 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.925,83 | €1.295,52 | €2.591,05 | €49,75 | €-22,21 |
| TEST | Sol Donchian 4H | 1 | €9.920,56 | €1.200,73 | €2.401,46 | €49,66 | €-9,00 |
| TEST | Sol Adaptive 4H | 1 | €9.918,81 | €1.100,38 | €2.200,75 | €49,64 | €-8,25 |
| TEST | Rapida V3 — score <7,5 | 5 | €9.918,78 | €4.213,05 | €12.639,15 | €198,08 | €10,70 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.884,82 | €4.158,00 | €8.316,00 | €148,97 | €-8,78 |
| TEST | Scanner Bottom15 Short | 5 | €9.884,82 | €4.158,00 | €8.316,00 | €148,97 | €-8,78 |
| TEST | Scanner Bottom20 Short | 5 | €9.884,82 | €4.158,00 | €8.316,00 | €148,97 | €-8,78 |
| TEST | Sol Donchian 1H | 0 | €9.875,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.873,96 | €1.406,22 | €2.812,44 | €49,50 | €-24,11 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.838,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2 | €9.834,12 | €1.651,13 | €4.953,38 | €99,18 | €-33,75 |
| TEST | Btc Ema 1H | 1 | €9.820,74 | €1.139,88 | €3.419,65 | €49,24 | €-25,78 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 5 | €9.816,33 | €4.129,16 | €8.258,32 | €147,94 | €-8,72 |
| TEST | Combo Adaptive — Side × Regime Guard | 0 | €9.815,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.806,61 | €1.396,63 | €2.793,26 | €49,16 | €-23,95 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.803,58 | €3.594,66 | €7.189,31 | €147,40 | €-0,24 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 5 | €9.801,40 | €4.122,88 | €8.245,76 | €147,72 | €-8,70 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.800,95 | €2.975,26 | €8.925,78 | €146,27 | €-10,56 |
| TEST | Sol Ema 4H | 1 | €9.782,24 | €1.183,99 | €2.367,98 | €48,96 | €-8,87 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 1 | €9.776,04 | €1.460,07 | €4.380,22 | €49,06 | €-33,02 |
| TEST | Eth Donchian 1H | 0 | €9.762,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.753,03 | €1.129,69 | €3.389,07 | €48,80 | €-5,12 |
| TEST | Top 5 + BTC — BTC 2–3 | 1 | €9.746,18 | €209,35 | €418,71 | €49,71 | €-22,37 |
| TEST | Scanner Bottom 5 Short 1H | 5 | €9.725,97 | €4.091,15 | €8.182,31 | €146,58 | €-8,64 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 4 | €9.720,37 | €638,67 | €1.277,34 | €98,62 | €-0,24 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 4 | €9.685,62 | €1.669,55 | €3.339,10 | €145,28 | €-16,11 |
| TEST | Global Confluence puro 1H | 1 | €9.683,09 | €1.512,09 | €3.024,18 | €48,39 | €3,28 |
| TEST | Combo Mean Reversion | 1 | €9.647,37 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.621,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.603,04 | €1.800,65 | €3.601,29 | €96,04 | €80,33 |
| TEST | Combo Adaptive — Quality7 + Regime | 4 | €9.598,11 | €630,64 | €1.261,28 | €97,38 | €-0,24 |
| TEST | Rapida V1 — target pieno 2R | 5 | €9.592,44 | €2.484,74 | €7.454,23 | €192,60 | €-77,98 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €9.586,54 | €1.242,77 | €3.728,32 | €189,39 | €-11,02 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €9.583,74 | €1.263,91 | €3.791,72 | €144,26 | €13,87 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.574,73 | €867,39 | €2.602,16 | €145,64 | €14,89 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.564,42 | €202,90 | €405,81 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.551,58 | €1.105,17 | €3.315,52 | €47,74 | €4,97 |
| TEST | Rapida 1H V3 Filtered — madre | 6 | €9.523,89 | €1.234,65 | €3.703,96 | €188,15 | €-10,95 |
| TEST | Combo Adaptive — Quality7 | 2 | €9.511,58 | €713,02 | €1.426,04 | €95,14 | €-3,44 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.470,94 | €2.055,65 | €4.111,31 | €143,26 | €-25,23 |
| TEST | Combo Adaptive — Long Only | 3 | €9.466,52 | €1.682,60 | €3.365,20 | €96,98 | €-20,54 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.462,68 | €1.628,58 | €4.885,73 | €93,27 | €-32,38 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €9.450,60 | €3.280,71 | €6.561,42 | €142,78 | €-25,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 1 | €9.434,25 | €173,57 | €520,72 | €48,08 | €-27,82 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.371,91 | €3.028,31 | €9.084,94 | €140,07 | €14,26 |
| TEST | Top 5 + BTC — Guard | 3 | €9.356,00 | €2.030,71 | €4.061,41 | €141,53 | €-24,92 |
| TEST | Rapida V3 — senza ESPORTS | 6 | €9.344,13 | €1.063,87 | €3.191,61 | €145,45 | €-10,64 |
| TEST | Combo Trend | 8 | €9.333,33 | €1.717,94 | €3.435,88 | €95,95 | €50,15 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 4 | €9.323,01 | €3.486,57 | €6.973,15 | €141,63 | €39,23 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.314,29 | €5.050,54 | €10.101,09 | €186,34 | €-12,99 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 4 | €9.313,09 | €3.482,87 | €6.965,73 | €141,48 | €39,18 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.308,45 | €2.020,38 | €4.040,77 | €140,81 | €-24,80 |
| TEST | Combo Adaptive — parziale 1R | 4 | €9.300,58 | €1.603,18 | €3.206,36 | €139,51 | €-15,47 |
| TEST | Bilanciata 1H V1 | 5 | €9.288,60 | €1.758,39 | €5.275,16 | €138,02 | €-34,32 |
| TEST | Master Adaptive V1 | 4 | €9.277,07 | €3.469,39 | €6.938,79 | €140,94 | €39,03 |
| TEST | Scanner Top10 Long | 5 | €9.273,61 | €2.093,81 | €4.187,61 | €141,25 | €-44,49 |
| TEST | Scanner Top15 Long | 5 | €9.273,61 | €2.093,81 | €4.187,61 | €141,25 | €-44,49 |
| TEST | Scanner Top20 Long | 5 | €9.273,61 | €2.093,81 | €4.187,61 | €141,25 | €-44,49 |
| TEST | Bilanciata V3 · LONG only | 6 | €9.270,13 | €2.814,12 | €8.442,36 | €138,35 | €-9,99 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.251,88 | €3.631,57 | €7.263,13 | €185,74 | €-94,14 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.236,87 | €3.507,78 | €7.015,55 | €185,45 | €-21,77 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.155,74 | €495,86 | €1.487,59 | €138,93 | €-22,99 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.153,81 | €3.423,30 | €6.846,60 | €139,06 | €38,51 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.138,41 | €1.983,48 | €3.966,96 | €138,23 | €-24,35 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 4 | €9.130,14 | €1.578,01 | €3.156,02 | €137,15 | €-15,14 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €9.110,37 | €3.197,62 | €6.395,23 | €93,03 | €51,12 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €9.105,04 | €3.195,74 | €6.391,49 | €92,97 | €51,09 |
| TEST | Benchmark trend following EMA 1H | 10 | €9.093,73 | €1.989,35 | €3.978,69 | €88,35 | €-22,00 |
| TEST | Combo Scanner | 2 | €9.062,32 | €1.743,97 | €3.487,94 | €90,40 | €-24,04 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €9.031,00 | €3.135,05 | €6.270,09 | €136,44 | €-23,89 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 5 | €8.993,53 | €5.713,47 | €11.426,93 | €176,81 | €50,02 |
| TEST | Rapida V3 — Long Only | 1 | €8.982,44 | €165,26 | €495,78 | €45,78 | €-26,49 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €8.959,57 | €1.548,53 | €3.097,06 | €134,58 | €-14,86 |
| TEST | Forza relativa 1H V1 | 7 | €8.936,40 | €3.845,95 | €7.691,90 | €177,65 | €-38,81 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.935,15 | €3.207,55 | €6.415,10 | €136,45 | €-48,94 |
| TEST | Top 5 + BTC — solo MFE | 3 | €8.858,57 | €3.075,19 | €6.150,38 | €133,84 | €-23,43 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €8.623,24 | €1.479,89 | €2.959,77 | €129,39 | €-14,43 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.644,21 | €-379,65 | 42 | 42 | 33,33% | 0,72 | €-9,04 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.670,85 | €601,37 | 64 | 64 | 46,88% | 1,39 | €9,40 | 3,63% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.419,62 | €351,77 | 32 | 32 | 43,75% | 1,51 | €10,99 | 3,63% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.415,99 | €349,47 | 33 | 33 | 51,52% | 1,41 | €10,59 | 2,31% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.375,15 | €435,24 | 74 | 74 | 48,65% | 1,26 | €5,88 | 3,66% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.347,47 | €334,47 | 24 | 24 | 45,83% | 1,59 | €13,94 | 2,40% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.332,02 | €332,02 | 34 | 34 | 47,06% | 1,47 | €9,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.270,51 | €198,40 | 127 | 126 | 43,31% | 1,07 | €1,56 | 4,89% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.239,14 | €224,39 | 56 | 56 | 44,64% | 1,19 | €4,01 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.229,96 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.224,66 | €198,71 | 116 | 116 | 43,97% | 1,08 | €1,71 | 6,52% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.142,73 | €169,37 | 131 | 131 | 44,27% | 1,07 | €1,29 | 3,64% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.126,47 | €125,02 | 50 | 50 | 48,00% | 1,13 | €2,50 | 2,94% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.108,03 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.090,88 | €111,00 | 12 | 12 | 41,67% | 1,57 | €9,25 | 1,80% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.086,10 | €137,46 | 81 | 81 | 41,98% | 1,07 | €1,70 | 8,85% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.039,30 | €39,30 | 6 | 6 | 50,00% | 1,24 | €6,55 | 1,89% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.997,44 | €-72,76 | 85 | 84 | 45,88% | 0,97 | €-0,86 | 5,23% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,28 | €-8,72 | 13 | 13 | 61,54% | 0,97 | €-0,67 | 2,10% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.970,23 | €-55,08 | 80 | 80 | 42,50% | 0,97 | €-0,69 | 6,52% |
| TEST | Ampia 4H | Confluenza trend | €9.968,38 | €-49,84 | 38 | 38 | 23,68% | 0,95 | €-1,31 | 4,45% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.960,08 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.942,05 | €-26,23 | 7 | 7 | 57,14% | 0,84 | €-3,75 | 1,49% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.925,83 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,93% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.920,56 | €-68,81 | 3 | 3 | 33,33% | 0,35 | €-22,94 | 1,05% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.918,81 | €-71,45 | 3 | 3 | 33,33% | 0,32 | €-23,82 | 1,00% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.918,78 | €-84,48 | 121 | 121 | 39,67% | 0,97 | €-0,70 | 6,72% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.884,82 | €-102,53 | 63 | 63 | 34,92% | 0,93 | €-1,63 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.884,82 | €-102,53 | 63 | 63 | 34,92% | 0,93 | €-1,63 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.884,82 | €-102,53 | 63 | 63 | 34,92% | 0,93 | €-1,63 | 5,27% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.875,62 | €-124,38 | 8 | 8 | 37,50% | 0,49 | €-15,55 | 2,74% |
| TEST | Btc Ema 4H | Trend following EMA | €9.873,96 | €-100,21 | 2 | 2 | 0,00% | 0,00 | €-50,11 | 1,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.838,66 | €-161,34 | 31 | 28 | 38,71% | 0,80 | €-5,20 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.834,12 | €-129,14 | 30 | 30 | 36,67% | 0,84 | €-4,30 | 3,56% |
| TEST | Btc Ema 1H | Trend following EMA | €9.820,74 | €-151,42 | 9 | 9 | 33,33% | 0,53 | €-16,82 | 1,90% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.816,33 | €-171,11 | 54 | 54 | 35,19% | 0,86 | €-3,17 | 5,27% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.815,48 | €-184,52 | 62 | 62 | 40,32% | 0,86 | €-2,98 | 7,99% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.806,61 | €-167,74 | 3 | 3 | 0,00% | 0,00 | €-55,91 | 2,39% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.803,58 | €-192,61 | 32 | 32 | 40,62% | 0,75 | €-6,02 | 3,91% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.801,40 | €-186,06 | 55 | 55 | 34,55% | 0,84 | €-3,38 | 5,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.800,95 | €-183,24 | 103 | 103 | 36,89% | 0,92 | €-1,78 | 8,39% |
| TEST | Sol Ema 4H | Trend following EMA | €9.782,24 | €-207,28 | 4 | 4 | 0,00% | 0,00 | €-51,82 | 2,27% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.776,04 | €-188,30 | 38 | 38 | 44,74% | 0,80 | €-4,96 | 4,50% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.762,69 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Sol Ema 1H | Trend following EMA | €9.753,03 | €-239,48 | 9 | 9 | 22,22% | 0,37 | €-26,61 | 3,33% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.746,18 | €-231,87 | 12 | 12 | 25,00% | 0,47 | €-19,32 | 4,00% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.725,97 | €-261,58 | 82 | 82 | 34,15% | 0,85 | €-3,19 | 6,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.720,37 | €-282,28 | 22 | 22 | 36,36% | 0,63 | €-12,83 | 4,21% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.685,62 | €-296,35 | 85 | 85 | 37,65% | 0,83 | €-3,49 | 6,28% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.683,09 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,56% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.647,37 | €-352,36 | 35 | 35 | 40,00% | 0,70 | €-10,07 | 5,48% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.621,05 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,47% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.603,04 | €-475,43 | 80 | 76 | 38,75% | 0,82 | €-5,94 | 8,11% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.598,11 | €-404,51 | 22 | 22 | 27,27% | 0,48 | €-18,39 | 5,41% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.592,44 | €-381,45 | 144 | 143 | 35,42% | 0,88 | €-2,65 | 5,68% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.586,54 | €-406,60 | 109 | 108 | 44,95% | 0,81 | €-3,73 | 7,87% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.583,74 | €-427,86 | 106 | 106 | 42,45% | 0,84 | €-4,04 | 6,10% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.574,73 | €-439,36 | 71 | 64 | 40,85% | 0,75 | €-6,19 | 7,55% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.564,42 | €-435,33 | 73 | 73 | 42,47% | 0,78 | €-5,96 | 6,55% |
| TEST | Eth Ema 1H | Trend following EMA | €9.551,58 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,80% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.523,89 | €-469,29 | 153 | 152 | 37,91% | 0,86 | €-3,07 | 7,84% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.511,58 | €-484,87 | 46 | 46 | 30,43% | 0,64 | €-10,54 | 7,10% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.470,94 | €-500,92 | 53 | 53 | 37,74% | 0,71 | €-9,45 | 7,74% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.466,52 | €-510,92 | 54 | 54 | 37,04% | 0,65 | €-9,46 | 6,08% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.462,68 | €-502,00 | 73 | 73 | 39,73% | 0,76 | €-6,88 | 6,37% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.450,60 | €-520,14 | 72 | 72 | 36,11% | 0,73 | €-7,22 | 11,27% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.434,25 | €-538,45 | 72 | 72 | 34,72% | 0,72 | €-7,48 | 9,13% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.371,91 | €-699,70 | 78 | 77 | 43,59% | 0,71 | €-8,97 | 7,61% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.356,00 | €-616,20 | 58 | 58 | 34,48% | 0,66 | €-10,62 | 7,34% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.344,13 | €-698,69 | 127 | 126 | 37,80% | 0,76 | €-5,50 | 7,67% |
| TEST | Combo Trend | Combo Trend | €9.333,33 | €-714,56 | 115 | 115 | 33,91% | 0,77 | €-6,21 | 9,82% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.323,01 | €-713,06 | 49 | 49 | 24,49% | 0,54 | €-14,55 | 8,39% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.314,29 | €-666,82 | 49 | 49 | 30,61% | 0,63 | €-13,61 | 7,12% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.313,09 | €-722,93 | 44 | 44 | 29,55% | 0,52 | €-16,43 | 7,98% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.308,45 | €-663,90 | 68 | 68 | 38,24% | 0,66 | €-9,76 | 7,02% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.300,58 | €-682,11 | 86 | 86 | 36,05% | 0,63 | €-7,93 | 7,07% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.288,60 | €-674,90 | 116 | 116 | 37,93% | 0,73 | €-5,82 | 12,69% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.277,07 | €-758,82 | 46 | 46 | 28,26% | 0,55 | €-16,50 | 7,80% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.273,61 | €-679,26 | 53 | 53 | 33,96% | 0,56 | €-12,82 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.273,61 | €-679,26 | 53 | 53 | 33,96% | 0,56 | €-12,82 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.273,61 | €-679,26 | 53 | 53 | 33,96% | 0,56 | €-12,82 | 10,31% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.270,13 | €-714,91 | 59 | 59 | 32,20% | 0,48 | €-12,12 | 8,12% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.251,88 | €-649,45 | 53 | 53 | 32,08% | 0,64 | €-12,25 | 7,75% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.236,87 | €-739,76 | 44 | 44 | 25,00% | 0,55 | €-16,81 | 8,18% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.155,74 | €-823,44 | 52 | 52 | 30,77% | 0,53 | €-15,84 | 9,26% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.153,81 | €-881,60 | 81 | 81 | 46,91% | 0,53 | €-10,88 | 9,02% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.138,41 | €-834,43 | 75 | 75 | 37,33% | 0,61 | €-11,13 | 8,78% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.130,14 | €-852,92 | 90 | 90 | 32,22% | 0,58 | €-9,48 | 11,05% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.110,37 | €-937,64 | 56 | 56 | 30,36% | 0,48 | €-16,74 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.105,04 | €-942,94 | 60 | 60 | 31,67% | 0,47 | €-15,72 | 12,06% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.093,73 | €-881,51 | 81 | 81 | 29,63% | 0,55 | €-10,88 | 9,84% |
| TEST | Combo Scanner | Combo Scanner | €9.062,32 | €-911,23 | 78 | 78 | 34,62% | 0,61 | €-11,68 | 11,38% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.031,00 | €-941,04 | 53 | 53 | 32,08% | 0,43 | €-17,76 | 11,72% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €8.993,53 | €-1.049,90 | 35 | 35 | 17,14% | 0,33 | €-30,00 | 11,40% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €8.982,44 | €-991,57 | 92 | 92 | 29,35% | 0,61 | €-10,78 | 11,09% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.959,57 | €-1.023,80 | 71 | 71 | 30,99% | 0,42 | €-14,42 | 11,05% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.936,40 | €-1.020,35 | 97 | 97 | 28,87% | 0,58 | €-10,52 | 12,58% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.935,15 | €-1.011,64 | 48 | 48 | 27,08% | 0,54 | €-21,08 | 11,51% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €8.858,57 | €-1.114,00 | 65 | 65 | 32,31% | 0,37 | €-17,14 | 12,28% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €8.623,24 | €-1.360,58 | 97 | 97 | 30,93% | 0,42 | €-14,03 | 13,79% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99958 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €23,01 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,07006 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,23 |
| Principale 4H | SOL | LONG | Confluenza trend | 240m | 3,0x | 77,23844 | 76,94900 | 75,78654 | 51,87849 | 80,14224 | €11,96 | €35,87 | €0,67 | €-0,13 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,93 | €104,79 | €1,51 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06998 | 0,07006 | 0,07099 | 0,09295 | 0,06796 | €1.095,91 | €3.287,73 | €47,34 | €-3,85 |
| Bilanciata 1H V1 | ACE | LONG | Confluenza trend | 60m | 3,0x | 0,23434 | 0,21500 | 0,20982 | 0,15740 | 0,28337 | €142,14 | €426,43 | €44,61 | €-35,19 |
| Bilanciata 1H V1 | SOXL | SHORT | Confluenza trend | 60m | 3,0x | 127,38352 | 126,81000 | 132,78383 | 169,20778 | 116,58291 | €350,35 | €1.051,05 | €44,56 | €4,73 |
| Bilanciata 1H — LONG senza Range High Vol | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BTC | LONG | Confluenza trend | 60m | 3,0x | 64764,77036 | 64276,60000 | 63832,15767 | 43500,33743 | 66629,99575 | €87,47 | €262,41 | €3,78 | €-1,98 |
| Bilanciata 1H — LONG senza Range High Vol | ACE | LONG | Confluenza trend | 60m | 3,0x | 0,22764 | 0,21500 | 0,20039 | 0,15290 | 0,28213 | €126,17 | €378,51 | €45,31 | €-21,01 |
| Bilanciata 1H — SHORT Trend Down stretto | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 0,99958 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €-19,03 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ACE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,21513 | 0,21500 | 0,18931 | 0,14449 | 0,26676 | €132,78 | €398,34 | €47,80 | €-0,24 |
| Bilanciata 1H V2 | SNDK | SHORT | Confluenza trend V2 | 60m | 3,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2137,41315 | 1493,65499 | €444,17 | €1.332,50 | €47,80 | €15,13 |
| Bilanciata 1H V2 | SUI | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,65261 | 0,65261 | 0,66201 | 0,86688 | 0,63381 | €26,68 | €80,03 | €1,15 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07006 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,27 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99958 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €-0,09 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.164,76 | €3.494,29 | €50,32 | €-0,00 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 64764,77036 | 64276,60000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.042,91 | €3.128,72 | €45,05 | €-23,58 |
| Bilanciata 1H V3 Filtered | SKHYNIX | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1120,69460 | 1447,61199 | 1027,99798 | €565,93 | €1.697,79 | €48,14 | €13,38 |
| Rapida V1 — score 6–7,5 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.575,03 | €4.725,08 | €52,92 | €-0,00 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99958 | 1,00671 | 1,32244 | 0,97884 | €1.521,02 | €4.563,07 | €51,11 | €-18,42 |
| Rapida V1 — score 6–7,5 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €489,70 | €1.469,11 | €51,42 | €12,90 |
| Rapida V1 — score 6–7,5 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €750,57 | €2.251,70 | €49,66 | €17,74 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.533,15 | €4.599,45 | €51,51 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99958 | 1,00671 | 1,32244 | 0,97884 | €1.480,58 | €4.441,75 | €49,75 | €-17,93 |
| Rapida score 6–7,5 — senza Trend Up | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €476,68 | €1.430,05 | €50,05 | €12,56 |
| Rapida score 6–7,5 — senza Trend Up | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €730,61 | €2.191,84 | €48,33 | €17,27 |
| Rapida score 6–7,5 — Range Only | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| Rapida score 6–7,5 — Range Only | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €492,83 | €1.478,49 | €51,74 | €12,98 |
| Rapida score 6–7,5 — Range Only | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1105,10654 | 1081,21000 | 1099,51029 | 1467,94985 | 1072,37322 | €873,85 | €2.621,54 | €0,00 | €56,69 |
| Rapida score 6–7,5 — Cost Aware | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99958 | 1,00671 | 1,32244 | 0,97884 | €1.578,12 | €4.734,36 | €53,02 | €-19,11 |
| Rapida score 6–7,5 — Cost Aware | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.566,58 | €4.699,75 | €52,64 | €-35,42 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €63,61 | €190,84 | €2,14 | €-1,44 |
| Rapida V1 — no HIGH + score <7,5 | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1609,09396 | 1590,82000 | 1653,98690 | 2137,41315 | 1541,75456 | €12,94 | €38,82 | €1,08 | €0,44 |
| Rapida V1 — no HIGH + score <7,5 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €485,34 | €1.456,02 | €50,96 | €12,78 |
| Rapida V1 — no HIGH + score <7,5 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €734,40 | €2.203,21 | €48,59 | €17,36 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.488,39 | €4.465,16 | €50,01 | €-33,66 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ACE | LONG | Momentum / breakout | 60m | 3,0x | 0,21504 | 0,21500 | 0,19338 | 0,14444 | 0,24753 | €162,74 | €488,22 | €49,17 | €-0,10 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| Rapida V1 — senza PEPE | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| Rapida V1 — senza PEPE | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.477,62 | €4.432,85 | €49,65 | €-33,41 |
| Rapida V1 — senza PEPE | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1609,09396 | 1590,82000 | 1653,98690 | 2137,41315 | 1541,75456 | €15,88 | €47,64 | €1,33 | €0,54 |
| Rapida V1 — senza PEPE | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €483,03 | €1.449,09 | €50,71 | €12,72 |
| Rapida V1 — senza PEPE | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1080,56127 | 1081,21000 | 1104,16618 | 1435,34556 | 1045,15392 | €730,26 | €2.190,78 | €47,86 | €-1,32 |
| Rapida V1 — target pieno 2R | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €115,44 | €346,32 | €3,88 | €-0,00 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| Rapida V1 — target pieno 2R | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 66215,50122 | €1.432,32 | €4.296,97 | €48,13 | €-32,39 |
| Rapida V1 — target pieno 2R | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1591,30464 | 1590,82000 | 1632,05331 | 2113,78300 | 1509,80731 | €632,00 | €1.896,01 | €48,55 | €0,58 |
| Rapida V1 — target pieno 2R | ACE | LONG | Momentum / breakout | 60m | 3,0x | 0,23824 | 0,21500 | 0,21637 | 0,16002 | 0,28199 | €157,73 | €473,20 | €43,44 | €-46,17 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,35 | €73,04 | €0,82 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €154,24 | €462,73 | €40,02 | €0,00 |
| Rapida 1H V3 Filtered — madre | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,21500 | 0,20616 | 0,15256 | 0,25859 | €174,86 | €524,57 | €48,44 | €-28,03 |
| Rapida 1H V3 Filtered — madre | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €722,64 | €2.167,91 | €47,81 | €17,08 |
| Rapida V3 — score <7,5 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.494,66 | €4.483,99 | €50,22 | €-0,00 |
| Rapida V3 — score <7,5 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99556 | 0,99958 | 1,00671 | 1,32244 | 0,97884 | €1.491,98 | €4.475,94 | €50,13 | €-18,07 |
| Rapida V3 — score <7,5 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06970 | 0,07006 | 0,07048 | 0,09258 | 0,06853 | €37,09 | €111,27 | €1,25 | €-0,58 |
| Rapida V3 — score <7,5 | SOXL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €458,42 | €1.375,27 | €48,13 | €12,07 |
| Rapida V3 — score <7,5 | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €730,89 | €2.192,68 | €48,35 | €17,27 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| Rapida V3 — no volatilità HIGH | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| Rapida V3 — no volatilità HIGH | SNDK | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1591,30464 | 1590,82000 | 1632,05331 | 2113,78300 | 1530,18165 | €13,22 | €39,65 | €1,02 | €0,01 |
| Rapida V3 — no volatilità HIGH | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21613 | 0,21500 | 0,22003 | 0,14517 | 0,24484 | €181,72 | €545,15 | €0,00 | €-2,85 |
| Rapida V3 — no volatilità HIGH | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €707,08 | €2.121,25 | €46,78 | €16,71 |
| Rapida V3 — Long Only | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,21500 | 0,20616 | 0,15256 | 0,25859 | €165,26 | €495,78 | €45,78 | €-26,49 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.431,94 | €4.295,82 | €48,11 | €-32,38 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,35 | €55,04 | €0,62 | €-0,00 |
| Rapida V3 — senza ESPORTS | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| Rapida V3 — senza ESPORTS | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,21500 | 0,20616 | 0,15256 | 0,25859 | €170,95 | €512,85 | €47,35 | €-27,40 |
| Rapida V3 — senza ESPORTS | SNDK | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1591,30464 | 1590,82000 | 1632,05331 | 2113,78300 | 1530,18165 | €11,72 | €35,16 | €0,90 | €0,01 |
| Rapida V3 — senza ESPORTS | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €708,97 | €2.126,90 | €46,90 | €16,76 |
| Rapida V3 senza ESPORTS — Long Only | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,21500 | 0,20616 | 0,15256 | 0,25859 | €173,57 | €520,72 | €48,08 | €-27,82 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,51 | €73,52 | €0,82 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €155,26 | €465,77 | €40,28 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,21500 | 0,20616 | 0,15256 | 0,25859 | €176,01 | €528,02 | €48,75 | €-28,21 |
| Rapida V3 senza ESPORTS — MFE Lock | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €727,39 | €2.182,17 | €48,12 | €17,19 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.460,07 | €4.380,22 | €49,06 | €-33,02 |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1910,31000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €46,36 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| Rapida V3 — qualità completa + profit lock | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.419,52 | €4.258,55 | €47,70 | €-32,10 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 0,99958 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €17,92 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,07006 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,53 |
| Ampia 4H | BTW | LONG | Confluenza trend | 240m | 2,0x | 0,32695 | 0,32695 | 0,28771 | 0,16511 | 0,43680 | €207,21 | €414,42 | €49,73 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,65521 | 0,65521 | 0,67955 | 0,97953 | 0,58704 | €31,61 | €63,21 | €2,35 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,49 | €-0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,99556 | 0,99958 | 1,00990 | 1,48836 | 0,96402 | €1.577,31 | €3.154,62 | €45,43 | €-12,74 |
| Forza relativa 1H V1 | SKHYNIX | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1154,93662 | 1081,21000 | 1103,81605 | 1726,63025 | 1076,23129 | €31,44 | €62,88 | €0,00 | €4,01 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,65491 | 0,65491 | 0,66473 | 0,97909 | 0,63329 | €1.513,47 | €3.026,93 | €45,42 | €-0,00 |
| Forza relativa 1H V1 | SNDK | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1625,29424 | 1590,82000 | 1683,24365 | 2429,81489 | 1497,80552 | €31,35 | €62,71 | €2,24 | €1,33 |
| Forza relativa 1H V1 | ACE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,23434 | 0,21500 | 0,20982 | 0,11834 | 0,28828 | €215,46 | €430,92 | €45,08 | €-35,56 |
| Forza relativa 1H V1 | SOXL | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 127,38352 | 126,81000 | 132,78383 | 190,43837 | 115,50285 | €460,04 | €920,07 | €39,01 | €4,14 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1149,28002 | 1081,21000 | 1102,62450 | 1718,17363 | 1074,31996 | €816,29 | €1.632,59 | €0,00 | €96,70 |
| Forza relativa 1H V2 | ACE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,22714 | 0,21500 | 0,20017 | 0,11470 | 0,28646 | €202,95 | €405,90 | €48,19 | €-21,69 |
| Forza relativa 1H V2 | SNDK | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1482,11107 | €20,14 | €40,27 | €1,44 | €0,46 |
| Forza relativa 1H V2 | SUI | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,65001 | 0,65001 | 0,65937 | 0,97176 | 0,62942 | €20,45 | €40,91 | €0,59 | €-0,00 |
| Forza relativa 1H V2 | SOXL | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 127,38352 | 126,81000 | 132,78383 | 190,43837 | 115,50285 | €540,44 | €1.080,88 | €45,82 | €4,87 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €0,00 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07006 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-26,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1154,93662 | 1081,21000 | 1105,66779 | 1726,63025 | 1055,56120 | €773,75 | €1.547,50 | €0,00 | €98,79 |
| Benchmark Donchian breakout 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 64764,77036 | 64276,60000 | 63728,53404 | 32706,20903 | 67355,36118 | €59,87 | €119,74 | €1,92 | €-0,90 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €0,00 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07006 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-25,40 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1154,93662 | 1081,21000 | 1105,66779 | 1726,63025 | 1055,56120 | €755,53 | €1.511,07 | €0,00 | €96,46 |
| Donchian 1H Gb20 120R V1 | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 64764,77036 | 64276,60000 | 63728,53404 | 32706,20903 | 67355,36118 | €58,46 | €116,93 | €1,87 | €-0,88 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07006 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,05 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 0,99958 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €-0,01 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 1911,30218 | 1910,31000 | 1880,72135 | 965,20760 | 1978,58002 | €44,44 | €88,89 | €1,42 | €-0,05 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SKHYNIX | SHORT | Trend following EMA | 60m | 2,0x | 1149,28002 | 1081,21000 | 1102,62450 | 1718,17363 | 1065,99106 | €59,36 | €118,73 | €0,00 | €7,03 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €21,92 | €43,84 | €0,72 | €-0,00 |
| Benchmark trend following EMA 1H | SNDK | SHORT | Trend following EMA | 60m | 2,0x | 1609,09396 | 1590,82000 | 1673,22674 | 2405,59548 | 1468,00188 | €13,00 | €26,01 | €1,04 | €0,30 |
| Benchmark trend following EMA 1H | SOXL | SHORT | Trend following EMA | 60m | 2,0x | 127,93319 | 126,81000 | 134,32945 | 191,26013 | 113,86143 | €389,91 | €779,82 | €38,99 | €6,85 |
| Benchmark trend following EMA 1H | ACE | LONG | Trend following EMA | 60m | 2,0x | 0,23824 | 0,21500 | 0,20965 | 0,12031 | 0,30114 | €185,38 | €370,75 | €44,49 | €-36,17 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | BTC | LONG | Scanner Top 5 Long | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.762,47 | €3.524,93 | €50,76 | €-26,57 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1914,76288 | 1910,31000 | 1887,19029 | 966,95525 | 1969,90805 | €57,06 | €114,13 | €1,64 | €-0,27 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,28489 | €28,12 | €56,23 | €0,81 | €-0,08 |
| Scanner Top 5 Long 1H | ACE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28044 | €213,82 | €427,63 | €50,99 | €-21,60 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,07006 | 0,07070 | 0,10420 | 0,06769 | €1.674,47 | €3.348,95 | €48,22 | €-17,39 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.627,25 | €3.254,49 | €48,28 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,39 | €58,78 | €2,11 | €0,67 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €559,10 | €1.118,20 | €47,97 | €8,08 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 1911,30218 | 1910,31000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,04 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €-24,41 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,28489 | €55,73 | €111,47 | €1,61 | €-0,17 |
| Scanner Top10 Long | ACE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-19,87 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06970 | 0,07006 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-17,67 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,76 | €59,51 | €2,13 | €0,68 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €568,25 | €1.136,50 | €48,76 | €8,22 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 1911,30218 | 1910,31000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,04 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €-24,41 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,28489 | €55,73 | €111,47 | €1,61 | €-0,17 |
| Scanner Top15 Long | ACE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-19,87 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06970 | 0,07006 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-17,67 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,76 | €59,51 | €2,13 | €0,68 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €568,25 | €1.136,50 | €48,76 | €8,22 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 1911,30218 | 1910,31000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,04 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €-24,41 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,28489 | €55,73 | €111,47 | €1,61 | €-0,17 |
| Scanner Top20 Long | ACE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-19,87 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06970 | 0,07006 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-17,67 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,76 | €59,51 | €2,13 | €0,68 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €568,25 | €1.136,50 | €48,76 | €8,22 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.610,50 | €3.221,00 | €46,38 | €-4,87 |
| Scanner Top 5 + forza BTC 1H | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €199,35 | €398,70 | €47,54 | €-20,14 |
| Top 5 + BTC — solo MFE | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.509,61 | €3.019,22 | €43,48 | €-4,56 |
| Top 5 + BTC — solo MFE | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €186,86 | €373,72 | €44,57 | €-18,87 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Top 5 + BTC — Guard | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.636,11 | €3.272,21 | €47,12 | €-4,94 |
| Top 5 + BTC — Guard | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €197,83 | €395,66 | €47,18 | €-19,98 |
| Top 5 + BTC — BTC≤3 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.538,99 | €3.077,99 | €44,32 | €-4,65 |
| Top 5 + BTC — BTC≤3 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €190,50 | €381,00 | €45,43 | €-19,24 |
| Top 5 + BTC — BTC 2–3 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22714 | 0,21500 | 0,20017 | 0,11470 | 0,28646 | €209,35 | €418,71 | €49,71 | €-22,37 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.598,05 | €3.196,11 | €46,02 | €-4,83 |
| Top 5 + BTC — Guard + MFE | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €193,23 | €386,45 | €46,08 | €-19,52 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.656,20 | €3.312,41 | €47,70 | €-5,00 |
| Top 5 + BTC — Guard + BTC≤3 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €200,26 | €400,52 | €47,76 | €-20,23 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.627,79 | €3.255,58 | €46,88 | €-4,92 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €196,82 | €393,65 | €46,94 | €-19,88 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18671 | 0,21500 | 0,21397 | 0,09429 | 0,25393 | €184,53 | €369,05 | €0,00 | €55,91 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 80,39464 | €1.595,98 | €3.191,96 | €45,96 | €-4,82 |
| Top 5 + BTC — target pieno 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Top 5 + BTC — target pieno 3R | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18671 | 0,21500 | 0,21397 | 0,09429 | 0,25393 | €184,63 | €369,27 | €0,00 | €55,95 |
| Top 5 + BTC — target pieno 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 80,39464 | €1.596,91 | €3.193,82 | €45,99 | €-4,82 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07006 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €3,28 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07006 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,06 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €118,87 | €237,73 | €3,80 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | SKHYNIX | SHORT | Combo Trend | 60m | 2,0x | 1149,28002 | 1081,21000 | 1102,62450 | 1718,17363 | 1065,99106 | €678,02 | €1.356,03 | €0,00 | €80,32 |
| Combo Trend | BTC | LONG | Combo Trend | 60m | 2,0x | 64764,77036 | 64276,60000 | 63728,53404 | 32706,20903 | 67044,49028 | €47,89 | €95,77 | €1,53 | €-0,72 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €29,12 | €58,23 | €0,96 | €-0,00 |
| Combo Trend | SOXL | SHORT | Combo Trend | 60m | 2,0x | 127,93319 | 126,81000 | 134,32945 | 191,26013 | 113,86143 | €431,24 | €862,49 | €43,12 | €7,57 |
| Combo Trend | ACE | LONG | Combo Trend | 60m | 2,0x | 0,23824 | 0,21500 | 0,20965 | 0,12031 | 0,30114 | €190,01 | €380,02 | €45,60 | €-37,07 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 77,06541 | 76,94900 | 75,95567 | 38,91803 | 79,50684 | €1.552,40 | €3.104,81 | €44,71 | €-4,69 |
| Combo Scanner | ACE | LONG | Combo Scanner | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28584 | €191,56 | €383,13 | €45,69 | €-19,35 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07006 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,07 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €569,18 | €1.138,35 | €48,84 | €8,23 |
| Combo Adaptive — madre | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,21500 | 0,20982 | 0,11834 | 0,28337 | €233,37 | €466,74 | €48,83 | €-38,52 |
| Combo Adaptive — madre | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1081,21000 | 1120,89130 | 1630,17096 | 1029,46346 | €835,77 | €1.671,55 | €46,72 | €14,11 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,07006 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,17 |
| Combo Adaptive — MFE Trail esistente | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €506,73 | €1.013,47 | €43,48 | €7,33 |
| Combo Adaptive — MFE Trail esistente | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,21500 | 0,20982 | 0,11834 | 0,28337 | €207,77 | €415,53 | €43,47 | €-34,29 |
| Combo Adaptive — MFE Trail esistente | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1081,21000 | 1120,89130 | 1630,17096 | 1029,46346 | €752,68 | €1.505,36 | €42,07 | €12,71 |
| Combo Adaptive — Quality7 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,22714 | 0,21500 | 0,20017 | 0,11470 | 0,28107 | €200,38 | €400,75 | €47,58 | €-21,41 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 129,07251 | 126,81000 | 135,06094 | 192,96340 | 117,09566 | €512,64 | €1.025,28 | €47,57 | €17,97 |
| Combo Adaptive — Trend/Transition | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive — Trend/Transition | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €204,28 | €408,56 | €49,03 | €-0,24 |
| Combo Adaptive — Trend/Transition | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,65421 | 0,65421 | 0,66363 | 0,97804 | 0,63537 | €1.699,46 | €3.398,92 | €48,94 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive — Quality7 + Regime | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €199,96 | €399,91 | €47,99 | €-0,24 |
| Combo Adaptive — Long Only | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive — Long Only | BTC | LONG | Combo Adaptive | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €18,79 | €37,57 | €0,54 | €-0,28 |
| Combo Adaptive — Long Only | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28044 | €200,54 | €401,09 | €47,83 | €-20,26 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07006 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,06 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €546,55 | €1.093,10 | €46,90 | €7,90 |
| Combo Adaptive — parziale 1R | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,21500 | 0,20982 | 0,11834 | 0,28337 | €224,09 | €448,18 | €46,89 | €-36,99 |
| Combo Adaptive — parziale 1R | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1081,21000 | 1120,89130 | 1630,17096 | 1029,46346 | €802,55 | €1.605,09 | €44,86 | €13,55 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €202,50 | €405,01 | €48,60 | €-0,24 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07006 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,07 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 111,29360 | €536,52 | €1.073,03 | €46,03 | €7,76 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,21500 | 0,20982 | 0,11834 | 0,30789 | €219,98 | €439,95 | €46,03 | €-36,31 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1081,21000 | 1120,89130 | 1630,17096 | 998,98752 | €790,61 | €1.581,23 | €44,19 | €13,35 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07006 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,07 |
| Combo Adaptive — target pieno 3R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 111,29360 | €526,49 | €1.052,99 | €45,17 | €7,61 |
| Combo Adaptive — target pieno 3R | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,21500 | 0,20982 | 0,11834 | 0,30789 | €215,87 | €431,74 | €45,17 | €-35,63 |
| Combo Adaptive — target pieno 3R | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1081,21000 | 1120,89130 | 1630,17096 | 998,98752 | €775,84 | €1.551,69 | €43,37 | €13,10 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64764,77036 | 64276,60000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.139,88 | €3.419,65 | €49,24 | €-25,78 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 64832,38388 | 64276,60000 | 63691,33393 | 32740,35386 | 67685,00877 | €1.406,22 | €2.812,44 | €49,50 | €-24,11 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 64764,77036 | 64276,60000 | 63935,78130 | 43500,33743 | 66422,74849 | €1.298,67 | €3.896,00 | €49,87 | €-29,37 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 64832,38388 | 64276,60000 | 63691,33393 | 32740,35386 | 68027,32376 | €1.396,63 | €2.793,26 | €49,16 | €-23,95 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 64806,45612 | 64276,60000 | 65843,35941 | 96885,65189 | 62940,03018 | €1.575,64 | €3.151,29 | €50,42 | €25,76 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 64764,77036 | 64276,60000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.156,05 | €3.468,16 | €49,94 | €-26,14 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 64832,38388 | 64276,60000 | 63587,60211 | 32740,35386 | 67944,33831 | €1.295,52 | €2.591,05 | €49,75 | €-22,21 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,06541 | 76,94900 | 75,95567 | 51,76227 | 79,28489 | €1.129,69 | €3.389,07 | €48,80 | €-5,12 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 77,23844 | 76,94900 | 75,64136 | 39,00541 | 81,23117 | €1.183,99 | €2.367,98 | €48,96 | €-8,87 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 77,23844 | 76,94900 | 75,64136 | 39,00541 | 81,71030 | €1.200,73 | €2.401,46 | €49,66 | €-9,00 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 77,23844 | 76,94900 | 75,49616 | 39,00541 | 81,59414 | €1.100,38 | €2.200,75 | €49,64 | €-8,25 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1907,45141 | 1910,31000 | 1879,98411 | 1281,17153 | 1962,38601 | €1.105,17 | €3.315,52 | €47,74 | €4,97 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1910,31000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €0,37 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €39,54 |
| Master Adaptive V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €194,21 | €388,43 | €46,61 | €-0,23 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,94900 | 75,85610 | 38,86702 | 79,18096 | €1.611,05 | €3.222,10 | €46,40 | €-0,64 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1910,31000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,41 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 58,44100 | 58,18865 | 29,81460 | 60,73912 | €1.637,93 | €3.275,87 | €47,17 | €-33,17 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €40,00 |
| Master Adaptive No Alt V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22644 | 0,21500 | 0,19943 | 0,11435 | 0,28044 | €194,09 | €388,18 | €46,29 | €-19,60 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,94900 | 75,85610 | 38,86702 | 79,18096 | €1.548,55 | €3.097,10 | €44,60 | €-0,62 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 58,44100 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €-22,77 |
| Master Adaptive Strict3 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.579,70 | €3.159,40 | €45,50 | €-23,81 |
| Master Adaptive Strict3 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22714 | 0,21500 | 0,20017 | 0,11470 | 0,28107 | €22,04 | €44,08 | €5,23 | €-2,36 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1910,31000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €0,12 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 58,44100 | 58,18865 | 29,81460 | 60,73912 | €1.636,69 | €3.273,37 | €47,14 | €-33,14 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 64764,77036 | 64276,60000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.591,99 | €3.183,97 | €45,85 | €-24,00 |
| Master Adaptive Expanded V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23824 | 0,21500 | 0,21012 | 0,12031 | 0,29449 | €190,24 | €380,49 | €44,91 | €-37,12 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1910,31000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €0,37 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €39,01 |
| Master Adaptive Gb20 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €191,63 | €383,27 | €45,99 | €-0,23 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,94900 | 75,85610 | 38,86702 | 79,18096 | €1.589,64 | €3.179,29 | €45,78 | €-0,64 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 58,44100 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €-23,70 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €39,12 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23824 | 0,21500 | 0,21012 | 0,12031 | 0,32261 | €190,60 | €381,19 | €45,00 | €-37,19 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1910,31000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €0,38 |
| Master Adaptive GB20 — Breakeven 0,5R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €39,73 |
| Master Adaptive GB20 — Breakeven 0,5R | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €195,18 | €390,35 | €46,84 | €-0,23 |
| Master Adaptive GB20 — Breakeven 0,5R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,94900 | 75,85610 | 38,86702 | 79,18096 | €1.619,03 | €3.238,05 | €46,63 | €-0,65 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1910,31000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €0,38 |
| Master Adaptive GB20 — 50% a 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €39,69 |
| Master Adaptive GB20 — 50% a 0,75R | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,21500 | 0,18931 | 0,10864 | 0,26676 | €194,97 | €389,94 | €46,79 | €-0,23 |
| Master Adaptive GB20 — 50% a 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,94900 | 75,85610 | 38,86702 | 79,18096 | €1.617,31 | €3.234,61 | €46,58 | €-0,65 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1910,31000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €14,40 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64276,60000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €44,51 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22714 | 0,21500 | 0,20691 | 0,11470 | 0,28107 | €76,44 | €152,88 | €13,61 | €-8,17 |
| Master Adaptive GB20 — Loss Cap 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,94900 | 76,13317 | 38,86702 | 79,18096 | €1.799,28 | €3.598,56 | €38,86 | €-0,72 |
| Rapida V3 NoHigh — Regime Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1902,79048 | 1910,31000 | 1881,47923 | 1278,04094 | 1934,75736 | €1.508,82 | €4.526,45 | €50,70 | €17,89 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99958 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €24,15 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 59,42488 | 58,44100 | 57,77054 | 39,91371 | 62,73356 | €20,16 | €60,47 | €1,68 | €-1,00 |
| MAIN — Side × Regime Guard | SOL | LONG | Confluenza trend | 240m | 3,0x | 77,23844 | 76,94900 | 75,78654 | 51,87849 | 80,14224 | €862,59 | €2.587,77 | €48,64 | €-9,70 |
| MAIN — Dynamic Asset Selector | ACE | LONG | Confluenza trend | 240m | 3,0x | 0,21504 | 0,21500 | 0,18924 | 0,14444 | 0,26665 | €142,09 | €426,26 | €51,15 | €-0,09 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07006 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-17,77 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 0,99958 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €15,19 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64276,60000 | 64039,40494 | 43500,33743 | 65852,81851 | €62,03 | €186,09 | €2,08 | €-1,40 |
| FAST NoHigh <7,5 · SHORT only | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1609,09396 | 1590,82000 | 1653,98690 | 2137,41315 | 1541,75456 | €12,62 | €37,86 | €1,06 | €0,43 |
| FAST NoHigh <7,5 · SHORT only | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,81000 | 132,41057 | 169,93793 | 121,21713 | €473,26 | €1.419,79 | €49,69 | €12,47 |
| FAST NoHigh <7,5 · SHORT only | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1081,21000 | 1113,82819 | 1447,61199 | 1053,74704 | €716,13 | €2.148,39 | €47,38 | €16,93 |
| Bilanciata V3 · LONG only | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07006 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,25 |
| Bilanciata V3 · LONG only | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99958 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €-0,08 |
| Bilanciata V3 · LONG only | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.101,68 | €3.305,04 | €47,59 | €-0,00 |
| Bilanciata V3 · LONG only | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | BTC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 64764,77036 | 64276,60000 | 63832,15767 | 43500,33743 | 66629,99575 | €986,42 | €2.959,27 | €42,61 | €-22,31 |
| Bilanciata V3 · LONG only | SKHYNIX | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 1089,79573 | 1081,21000 | 1120,69460 | 1447,61199 | 1027,99798 | €535,28 | €1.605,84 | €45,53 | €12,65 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,07006 | 0,07070 | 0,10420 | 0,06769 | €1.687,46 | €3.374,92 | €48,60 | €-17,52 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.639,87 | €3.279,73 | €48,65 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,62 | €59,23 | €2,12 | €0,67 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €563,44 | €1.126,87 | €48,34 | €8,15 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,07006 | 0,07070 | 0,10420 | 0,06769 | €1.690,03 | €3.380,06 | €48,67 | €-17,55 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.642,36 | €3.284,73 | €48,72 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1609,09396 | 1590,82000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,66 | €59,32 | €2,13 | €0,67 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 127,73331 | 126,81000 | 133,21322 | 190,96130 | 116,77350 | €564,29 | €1.128,59 | €48,42 | €8,16 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-76,60 | -1,51 | STOP_GAP_STRESS |
| Top 5 + BTC — target pieno 3R | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,88 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — 75% a 2,2R + runner 3R | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,85 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — solo MFE | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-57,10 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — Guard | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-60,01 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — Guard + MFE | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,61 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — Guard + BTC≤3 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-60,75 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — Guard + BTC≤3 + MFE | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-59,71 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — BTC≤3 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,21 | -1,27 | STOP_GAP_STRESS |
| Top 5 + BTC — BTC 2–3 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-123,11 | -2,48 | STOP_GAP_STRESS |
| Scanner Top 5 + forza BTC 1H | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-60,91 | -1,27 | STOP_GAP_STRESS |
| Scanner Top20 Long | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-86,04 | -1,85 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 390/30 | 33/30 | 0,70 | 2,04 | -0,15R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 357/30 | 20/30 | 0,62 | 1,90 | -0,20R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 216/30 | 22/30 | 0,77 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 218/30 | 22/30 | 0,74 | 1,57 | -0,13R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 302/30 | 31/30 | 0,79 | 0,62 | -0,11R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 272/30 | 11/30 | 0,70 | 0,00 | -0,15R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 121/30 | 8/30 | 0,67 | 1,02 | -0,17R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 276/30 | 17/30 | 0,59 | 4,50 | -0,23R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 430/30 | 24/30 | 0,69 | 0,64 | -0,16R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 393/30 | 7/30 | 0,59 | 0,02 | -0,21R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 302/30 | 30/30 | 0,83 | 1,02 | -0,09R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 548/30 | 55/30 | 0,83 | 1,12 | -0,08R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 121/30 | 15/30 | 0,42 | 0,99 | -0,39R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 491/30 | 44/30 | 0,70 | 1,20 | -0,15R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 495/30 | 37/30 | 0,70 | 0,76 | -0,15R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 454/30 | 23/30 | 0,61 | 1,12 | -0,20R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 281/30 | 42/30 | 0,70 | 0,72 | -0,18R | €-9,04 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 24/30 | 0,00 | 1,59 | 0,00R | €13,94 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 661/30 | 116/30 | 0,88 | 0,73 | -0,07R | €-5,82 | 12,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 52/30 | 0,00 | 0,53 | 0,00R | €-15,84 | 9,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 12/30 | 0,00 | 1,57 | 0,00R | €9,25 | 1,80% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 229/30 | 64/30 | 1,03 | 0,75 | 0,01R | €-6,19 | 7,55% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 415/30 | 103/30 | 0,91 | 0,92 | -0,05R | €-1,78 | 8,39% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 336/30 | 59/30 | 0,81 | 0,48 | -0,10R | €-12,12 | 8,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 173/30 | 30/30 | 0,93 | 0,84 | -0,03R | €-4,30 | 3,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 444/30 | 80/30 | 0,80 | 0,97 | -0,10R | €-0,69 | 6,52% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 511/30 | 116/30 | 0,84 | 1,08 | -0,08R | €1,71 | 6,52% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 682/30 | 131/30 | 0,78 | 1,07 | -0,12R | €1,29 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 74/30 | 0,00 | 1,26 | 0,00R | €5,88 | 3,66% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 84/30 | 0,00 | 0,97 | 0,00R | €-0,86 | 5,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 33/30 | 0,00 | 1,41 | 0,00R | €10,59 | 2,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 402/30 | 126/30 | 0,84 | 1,07 | -0,08R | €1,56 | 4,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 645/30 | 143/30 | 0,73 | 0,88 | -0,14R | €-2,65 | 5,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 49/30 | 28/30 | 0,59 | 0,80 | -0,24R | €-5,20 | 3,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 653/30 | 152/30 | 0,80 | 0,86 | -0,10R | €-3,07 | 7,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 476/30 | 121/30 | 0,80 | 0,97 | -0,10R | €-0,70 | 6,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 257/30 | 77/30 | 0,91 | 0,71 | -0,05R | €-8,97 | 7,61% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 260/30 | 73/30 | 0,87 | 0,76 | -0,06R | €-6,88 | 6,37% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 363/30 | 92/30 | 0,86 | 0,61 | -0,07R | €-10,78 | 11,09% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 34/30 | 0,00 | 1,47 | 0,00R | €9,77 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 56/30 | 0,00 | 1,19 | 0,00R | €4,01 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 539/30 | 106/30 | 0,76 | 0,84 | -0,13R | €-4,04 | 6,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 72/30 | 0,00 | 0,72 | 0,00R | €-7,48 | 9,13% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 108/30 | 0,00 | 0,81 | 0,00R | €-3,73 | 7,87% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 38/30 | 0,00 | 0,80 | 0,00R | €-4,96 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 606/30 | 126/30 | 0,76 | 0,76 | -0,12R | €-5,50 | 7,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 265/30 | 38/30 | 0,68 | 0,95 | -0,22R | €-1,31 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 182/30 | 73/30 | 1,14 | 0,78 | 0,06R | €-5,96 | 6,55% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 11/30 | 5/30 | 0,57 | 0,89 | -0,22R | €-2,34 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 14/30 | 7/30 | 0,22 | 0,84 | -0,63R | €-3,75 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 5/30 | 3/30 | 0,00 | 0,00 | -1,08R | €-55,91 | 2,39% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 15/30 | 9/30 | 0,78 | 0,53 | -0,13R | €-16,82 | 1,90% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 3/30 | 2/30 | 0,00 | 0,00 | -1,08R | €-50,11 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 535/30 | 85/30 | 0,97 | 0,83 | -0,01R | €-3,49 | 6,28% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 297/30 | 54/30 | 0,97 | 0,65 | -0,02R | €-9,46 | 6,08% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 578/30 | 97/30 | 0,98 | 0,42 | -0,01R | €-14,03 | 13,79% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 476/30 | 86/30 | 0,93 | 0,63 | -0,03R | €-7,93 | 7,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 63/30 | 22/30 | 1,25 | 0,63 | 0,11R | €-12,83 | 4,21% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 63/30 | 22/30 | 1,17 | 0,48 | 0,08R | €-18,39 | 5,41% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 152/30 | 46/30 | 0,88 | 0,64 | -0,06R | €-10,54 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 192/30 | 32/30 | 0,87 | 0,75 | -0,06R | €-6,02 | 3,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 90/30 | 0,74 | 0,58 | -0,20R | €-9,48 | 11,05% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 62/30 | 0,00 | 0,86 | 0,00R | €-2,98 | 7,99% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 71/30 | 0,74 | 0,42 | -0,20R | €-14,42 | 11,05% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 89/30 | 35/30 | 1,20 | 0,70 | 0,09R | €-10,07 | 5,48% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 336/30 | 78/30 | 1,08 | 0,61 | 0,04R | €-11,68 | 11,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 444/30 | 115/30 | 0,92 | 0,77 | -0,05R | €-6,21 | 9,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 50/30 | 0,00 | 1,13 | 0,00R | €2,50 | 2,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 12/30 | 10/30 | 0,51 | 0,62 | -0,36R | €-10,55 | 2,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 18/30 | 13/30 | 0,40 | 0,97 | -0,41R | €-0,67 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 210/30 | 64/30 | 0,83 | 1,39 | -0,11R | €9,40 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 140/30 | 32/30 | 0,80 | 1,51 | -0,11R | €10,99 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 448/30 | 81/30 | 0,89 | 0,55 | -0,06R | €-10,88 | 9,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 14/30 | 8/30 | 0,30 | 0,05 | -0,56R | €-38,45 | 3,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 13/30 | 7/30 | 0,28 | 0,28 | -0,63R | €-33,90 | 2,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 20/30 | 11/30 | 0,29 | 0,11 | -0,55R | €-41,03 | 4,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 12/30 | 15/30 | 0,89 | 0,35 | -0,07R | €-21,51 | 3,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 264/30 | 53/30 | 1,00 | 0,64 | 0,00R | €-12,25 | 7,75% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 49/30 | 0,00 | 0,54 | 0,00R | €-14,55 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 35/30 | 0,00 | 0,33 | 0,00R | €-30,00 | 11,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 44/30 | 0,00 | 0,52 | 0,00R | €-16,43 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 492/30 | 81/30 | 1,40 | 0,53 | 0,13R | €-10,88 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 232/30 | 49/30 | 1,02 | 0,63 | 0,01R | €-13,61 | 7,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 242/30 | 44/30 | 0,97 | 0,55 | -0,02R | €-16,81 | 8,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 167/30 | 48/30 | 1,01 | 0,54 | 0,01R | €-21,08 | 11,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 254/30 | 46/30 | 0,97 | 0,55 | -0,02R | €-16,50 | 7,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 559/30 | 97/30 | 0,87 | 0,58 | -0,07R | €-10,52 | 12,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 223/30 | 76/30 | 1,16 | 0,82 | 0,08R | €-5,94 | 8,11% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 197/30 | 63/30 | 0,50 | 0,93 | -0,28R | €-1,63 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 197/30 | 63/30 | 0,50 | 0,93 | -0,28R | €-1,63 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 197/30 | 63/30 | 0,50 | 0,93 | -0,28R | €-1,63 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 230/30 | 82/30 | 0,69 | 0,85 | -0,17R | €-3,19 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 236/30 | 54/30 | 0,77 | 0,86 | -0,11R | €-3,17 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 213/30 | 55/30 | 0,66 | 0,84 | -0,15R | €-3,38 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 274/30 | 53/30 | 0,98 | 0,56 | -0,01R | €-12,82 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 275/30 | 53/30 | 0,97 | 0,56 | -0,01R | €-12,82 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 275/30 | 53/30 | 0,97 | 0,56 | -0,01R | €-12,82 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 324/30 | 72/30 | 1,10 | 0,73 | 0,05R | €-7,22 | 11,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 127/30 | 12/30 | 0,85 | 0,47 | -0,09R | €-19,32 | 4,00% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 277/30 | 53/30 | 0,95 | 0,43 | -0,03R | €-17,76 | 11,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 292/30 | 68/30 | 1,17 | 0,66 | 0,07R | €-9,76 | 7,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 242/30 | 53/30 | 1,04 | 0,71 | 0,02R | €-9,45 | 7,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 303/30 | 75/30 | 1,17 | 0,61 | 0,07R | €-11,13 | 8,78% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 250/30 | 58/30 | 1,05 | 0,66 | 0,02R | €-10,62 | 7,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 345/30 | 65/30 | 1,07 | 0,37 | 0,03R | €-17,14 | 12,28% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 273/30 | 60/30 | 0,99 | 0,47 | -0,00R | €-15,72 | 12,06% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 259/30 | 56/30 | 0,98 | 0,48 | -0,01R | €-16,74 | 11,78% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 352/30 | 81/30 | 1,09 | 1,07 | 0,05R | €1,70 | 8,85% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 21/30 | 10/30 | 0,36 | 0,15 | -0,54R | €-37,89 | 4,47% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 3/30 | 3/30 | 0,58 | 0,32 | -0,30R | €-23,82 | 1,00% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 12/30 | 6/30 | 0,81 | 1,24 | -0,11R | €6,55 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 15/30 | 8/30 | 0,55 | 0,49 | -0,34R | €-15,55 | 2,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 3/30 | 3/30 | 0,63 | 0,35 | -0,26R | €-22,94 | 1,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 19/30 | 9/30 | 0,51 | 0,37 | -0,40R | €-26,61 | 3,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 4/30 | 4/30 | 0,00 | 0,00 | -1,06R | €-51,82 | 2,27% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07006**
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
| BTC sotto filtro | 64276.6 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07009**; close **0.07009**; wick alta **0.0%**; volume **x0.07**

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
- Confidenza: **73,80%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -1.39%, 55% sotto -1%.
- BTC trend score: **1,00**; ADX: **24,40**; breadth sopra EMA50: **50,00%**
- Mediana alt vs BTC: **-1,39%**; dispersione: **14,90%**

- Aperti in questo ciclo: **10**
- Chiusi in questo ciclo: **26**
- Posizioni research aperte: **643**
- Trade research chiusi: **26076**
- Eventi di mercato indipendenti chiusi: **3605**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **67965**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 12 | 390 | 390 | 29,74% | 0,70 | -0,15R | €-597,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 12 | 357 | 357 | 28,85% | 0,62 | -0,20R | €-716,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 3 | 216 | 216 | 45,37% | 0,77 | -0,12R | €-264,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 3 | 218 | 218 | 31,65% | 0,74 | -0,13R | €-288,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 4 | 302 | 302 | 32,12% | 0,79 | -0,11R | €-320,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 4 | 272 | 272 | 31,99% | 0,70 | -0,15R | €-402,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 121 | 121 | 33,88% | 0,67 | -0,17R | €-207,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 1 | 276 | 276 | 26,81% | 0,59 | -0,23R | €-642,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 8 | 430 | 430 | 29,30% | 0,69 | -0,16R | €-705,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 8 | 393 | 393 | 28,24% | 0,59 | -0,21R | €-839,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 4 | 302 | 302 | 32,78% | 0,83 | -0,09R | €-261,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 12 | 548 | 548 | 39,96% | 0,83 | -0,08R | €-416,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 2 | 121 | 121 | 28,10% | 0,42 | -0,39R | €-469,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 12 | 491 | 491 | 29,33% | 0,70 | -0,15R | €-752,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 12 | 495 | 495 | 29,29% | 0,70 | -0,15R | €-752,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 12 | 454 | 454 | 28,19% | 0,61 | -0,20R | €-914,38 |
| MAIN | 17 | 281 | 281 | 25,27% | 0,70 | -0,18R | €-509,66 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 17 | 661 | 661 | 33,13% | 0,88 | -0,07R | €-442,71 |
| Bilanciata 1H V2 | 8 | 263 | 229 | 36,88% | 1,03 | 0,01R | €38,85 |
| Bilanciata 1H V3 Filtered | 14 | 415 | 415 | 34,22% | 0,91 | -0,05R | €-202,70 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 14 | 336 | 336 | 33,04% | 0,81 | -0,10R | €-348,04 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 173 | 173 | 37,57% | 0,93 | -0,03R | €-52,07 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 8 | 444 | 444 | 34,23% | 0,80 | -0,10R | €-441,43 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 8 | 511 | 511 | 35,42% | 0,84 | -0,08R | €-407,09 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 11 | 682 | 682 | 33,72% | 0,78 | -0,12R | €-795,73 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 9 | 402 | 402 | 35,07% | 0,84 | -0,08R | €-335,92 |
| SHADOW_1H_FAST_TP2_V1 | 12 | 645 | 645 | 30,54% | 0,73 | -0,14R | €-910,26 |
| Rapida 1H V2 | 0 | 57 | 49 | 36,84% | 0,59 | -0,24R | €-135,15 |
| Rapida 1H V3 Filtered | 12 | 653 | 653 | 34,46% | 0,80 | -0,10R | €-674,08 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 11 | 476 | 476 | 34,45% | 0,80 | -0,10R | €-496,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 257 | 257 | 47,08% | 0,91 | -0,05R | €-122,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 260 | 260 | 36,54% | 0,87 | -0,06R | €-163,86 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 363 | 363 | 36,64% | 0,86 | -0,07R | €-250,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 8 | 539 | 539 | 33,40% | 0,76 | -0,13R | €-679,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 12 | 606 | 606 | 33,50% | 0,76 | -0,12R | €-756,04 |
| SHADOW_4H_WIDE | 29 | 265 | 265 | 19,62% | 0,68 | -0,22R | €-573,90 |
| SHADOW_BOLLINGER_MR_1H | 1 | 182 | 182 | 48,90% | 1,14 | 0,06R | €112,62 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 11 | 11 | 54,55% | 0,57 | -0,22R | €-23,77 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 14 | 14 | 28,57% | 0,22 | -0,63R | €-88,00 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,84 |
| SHADOW_BTC_EMA_1H | 1 | 15 | 15 | 46,67% | 0,78 | -0,13R | €-19,79 |
| SHADOW_BTC_EMA_4H | 1 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,26 |
| SHADOW_COMBO_ADAPTIVE | 14 | 535 | 535 | 36,64% | 0,97 | -0,01R | €-72,28 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 5 | 297 | 297 | 36,03% | 0,97 | -0,02R | €-46,20 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 11 | 578 | 578 | 40,66% | 0,98 | -0,01R | €-50,22 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 14 | 476 | 476 | 39,29% | 0,93 | -0,03R | €-164,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 63 | 63 | 46,03% | 1,25 | 0,11R | €70,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 63 | 63 | 38,10% | 1,17 | 0,08R | €47,92 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 152 | 152 | 31,58% | 0,88 | -0,06R | €-93,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 7 | 192 | 192 | 35,42% | 0,87 | -0,06R | €-121,65 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 89 | 89 | 49,44% | 1,20 | 0,09R | €79,28 |
| SHADOW_COMBO_SCANNER | 6 | 336 | 336 | 35,42% | 1,08 | 0,04R | €145,15 |
| SHADOW_COMBO_TREND | 14 | 444 | 444 | 31,53% | 0,92 | -0,05R | €-203,27 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 12 | 12 | 33,33% | 0,51 | -0,36R | €-43,62 |
| SHADOW_DOGE_EMA_1H | 0 | 18 | 18 | 27,78% | 0,40 | -0,41R | €-73,66 |
| SHADOW_DONCHIAN_1H | 6 | 210 | 210 | 29,52% | 0,83 | -0,11R | €-226,02 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 6 | 140 | 140 | 31,43% | 0,80 | -0,11R | €-160,94 |
| SHADOW_EMA_TREND_1H | 16 | 448 | 448 | 31,03% | 0,89 | -0,06R | €-284,94 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 14 | 14 | 28,57% | 0,30 | -0,56R | €-77,90 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 13 | 13 | 23,08% | 0,28 | -0,63R | €-81,36 |
| SHADOW_ETH_EMA_1H | 1 | 20 | 20 | 30,00% | 0,29 | -0,55R | €-110,17 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 1 | 12 | 12 | 41,67% | 0,89 | -0,07R | €-8,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 10 | 264 | 264 | 32,58% | 1,00 | 0,00R | €8,05 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 492 | 492 | 66,46% | 1,40 | 0,13R | €634,09 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 10 | 232 | 232 | 32,76% | 1,02 | 0,01R | €31,01 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 9 | 242 | 242 | 30,58% | 0,97 | -0,02R | €-41,81 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 7 | 167 | 167 | 32,93% | 1,01 | 0,01R | €13,08 |
| SHADOW_MASTER_ADAPTIVE_V1 | 10 | 254 | 254 | 31,89% | 0,97 | -0,02R | €-46,49 |
| Forza relativa 1H V1 | 16 | 559 | 559 | 29,52% | 0,87 | -0,07R | €-408,30 |
| Forza relativa 1H V2 | 10 | 239 | 223 | 35,56% | 1,16 | 0,08R | €192,29 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 10 | 197 | 197 | 26,40% | 0,50 | -0,28R | €-556,57 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 10 | 197 | 197 | 26,40% | 0,50 | -0,28R | €-556,57 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 10 | 197 | 197 | 26,40% | 0,50 | -0,28R | €-556,57 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 10 | 230 | 230 | 29,13% | 0,69 | -0,17R | €-394,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 8 | 236 | 236 | 52,54% | 0,77 | -0,11R | €-248,64 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 8 | 213 | 213 | 51,64% | 0,66 | -0,15R | €-321,20 |
| SHADOW_SCANNER_TOP10_LONG | 7 | 274 | 274 | 34,67% | 0,98 | -0,01R | €-22,66 |
| SHADOW_SCANNER_TOP15_LONG | 7 | 275 | 275 | 34,55% | 0,97 | -0,01R | €-33,77 |
| SHADOW_SCANNER_TOP20_LONG | 7 | 275 | 275 | 34,55% | 0,97 | -0,01R | €-33,77 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 324 | 324 | 34,88% | 1,10 | 0,05R | €166,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 1 | 127 | 127 | 30,71% | 0,85 | -0,09R | €-112,63 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 5 | 277 | 277 | 33,21% | 0,95 | -0,03R | €-76,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 5 | 292 | 292 | 45,21% | 1,17 | 0,07R | €210,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 6 | 242 | 242 | 35,12% | 1,04 | 0,02R | €48,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 303 | 303 | 44,88% | 1,17 | 0,07R | €222,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 6 | 250 | 250 | 34,80% | 1,05 | 0,02R | €58,86 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 5 | 345 | 345 | 43,48% | 1,07 | 0,03R | €107,11 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 5 | 273 | 273 | 32,60% | 0,99 | -0,00R | €-10,28 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 5 | 259 | 259 | 31,66% | 0,98 | -0,01R | €-25,85 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 352 | 352 | 36,08% | 1,09 | 0,05R | €166,78 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 21 | 21 | 23,81% | 0,36 | -0,54R | €-113,90 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 3 | 3 | 33,33% | 0,58 | -0,30R | €-8,87 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 12 | 12 | 50,00% | 0,81 | -0,11R | €-12,76 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 15 | 15 | 33,33% | 0,55 | -0,34R | €-50,34 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 3 | 3 | 33,33% | 0,63 | -0,26R | €-7,86 |
| SHADOW_SOL_EMA_1H | 1 | 19 | 19 | 26,32% | 0,51 | -0,40R | €-76,60 |
| SHADOW_SOL_EMA_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,50 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 5 | 40 | 40 | 22,50% | 0,52 | -0,30R | €-120,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 54 | 54 | 40,74% | 1,26 | 0,12R | €66,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 110 | 110 | 33,64% | 0,63 | -0,19R | €-212,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 3 | 15 | 15 | 33,33% | 0,78 | -0,10R | €-14,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 2 | 53 | 53 | 32,08% | 0,97 | -0,01R | €-6,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 52 | 52 | 17,31% | 0,47 | -0,26R | €-137,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 5 | 38 | 38 | 21,05% | 0,32 | -0,48R | €-182,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 41 | 41 | 41,46% | 1,39 | 0,17R | €69,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 1 | 103 | 103 | 33,01% | 0,52 | -0,25R | €-259,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 3 | 14 | 14 | 28,57% | 0,68 | -0,15R | €-20,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 2 | 52 | 52 | 32,69% | 1,07 | 0,03R | €15,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 49 | 49 | 16,33% | 0,31 | -0,36R | €-177,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 1 | 7 | 7 | 42,86% | 0,59 | -0,25R | €-17,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 64 | 64 | 39,06% | 0,48 | -0,33R | €-208,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 2 | 31 | 31 | 54,84% | 1,03 | 0,01R | €4,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 33,33% | 0,73 | -0,14R | €-8,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-207,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 2 | 31 | 31 | 29,03% | 0,88 | -0,05R | €-15,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,39 | -0,35R | €-45,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 0,99 | -0,00R | €-1,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 79 | 79 | 34,18% | 0,62 | -0,21R | €-166,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 1 | 14 | 14 | 21,43% | 0,50 | -0,28R | €-38,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 2 | 42 | 42 | 33,33% | 1,17 | 0,07R | €29,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,25 | -0,43R | €-55,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 44 | 44 | 36,36% | 1,02 | 0,01R | €4,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 69 | 69 | 36,23% | 0,56 | -0,23R | €-160,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 1 | 13 | 13 | 23,08% | 0,51 | -0,25R | €-32,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 2 | 41 | 41 | 34,15% | 1,26 | 0,10R | €41,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 119 | 119 | 33,61% | 0,65 | -0,18R | €-217,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,73 | -0,16R | €-83,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 104 | 104 | 32,69% | 0,66 | -0,19R | €-193,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 1 | 32 | 32 | 21,88% | 0,69 | -0,15R | €-47,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 4 | 31 | 31 | 16,13% | 0,25 | -0,53R | €-164,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 135 | 135 | 33,33% | 0,65 | -0,19R | €-256,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 2 | 50 | 50 | 26,00% | 0,80 | -0,09R | €-43,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 71 | 71 | 23,94% | 0,65 | -0,17R | €-119,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 4 | 30 | 30 | 16,67% | 0,16 | -0,61R | €-183,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 126 | 126 | 32,54% | 0,57 | -0,22R | €-281,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 2 | 49 | 49 | 26,53% | 0,78 | -0,09R | €-45,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 66 | 66 | 22,73% | 0,47 | -0,27R | €-176,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,39 | -0,35R | €-45,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 53 | 53 | 37,74% | 1,07 | 0,03R | €18,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 79 | 79 | 36,71% | 0,75 | -0,14R | €-107,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 1 | 14 | 14 | 21,43% | 0,50 | -0,28R | €-38,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 2 | 42 | 42 | 33,33% | 1,17 | 0,07R | €29,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 5 | 61 | 61 | 36,07% | 0,52 | -0,27R | €-163,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 67 | 67 | 46,27% | 1,03 | 0,01R | €9,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 149 | 149 | 37,58% | 0,79 | -0,10R | €-145,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 3 | 27 | 27 | 37,04% | 0,67 | -0,17R | €-46,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 2 | 66 | 66 | 46,97% | 1,41 | 0,13R | €85,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 81 | 81 | 40,74% | 0,84 | -0,07R | €-56,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 48 | 48 | 37,50% | 0,47 | -0,32R | €-151,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 1 | 4 | 4 | 50,00% | 0,92 | -0,05R | €-1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 5 | 55 | 55 | 20,00% | 0,37 | -0,38R | €-211,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 0 | 61 | 61 | 34,43% | 0,98 | -0,01R | €-5,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 1 | 131 | 131 | 32,82% | 0,63 | -0,20R | €-261,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 3 | 27 | 27 | 29,63% | 0,59 | -0,21R | €-56,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 2 | 60 | 60 | 33,33% | 1,24 | 0,10R | €57,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 5 | 55 | 55 | 20,00% | 0,37 | -0,38R | €-211,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 0 | 63 | 63 | 34,92% | 1,01 | 0,01R | €4,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 1 | 132 | 132 | 32,58% | 0,62 | -0,21R | €-271,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 3 | 27 | 27 | 29,63% | 0,59 | -0,21R | €-56,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 2 | 60 | 60 | 33,33% | 1,24 | 0,10R | €57,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 5 | 54 | 54 | 20,37% | 0,29 | -0,45R | €-244,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 51 | 51 | 35,29% | 1,04 | 0,02R | €11,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 1 | 124 | 124 | 31,45% | 0,50 | -0,27R | €-332,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 3 | 23 | 23 | 26,09% | 0,61 | -0,20R | €-46,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 2 | 59 | 59 | 33,90% | 1,31 | 0,12R | €72,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 65 | 65 | 21,54% | 0,39 | -0,31R | €-201,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 4 | 22 | 22 | 27,27% | 0,73 | -0,14R | €-31,06 |
| MAIN | ALT_ROTATION_UP | 1 | 41 | 41 | 17,07% | 0,31 | -0,48R | €-197,22 |
| MAIN | RANGE | 2 | 73 | 73 | 21,92% | 0,64 | -0,23R | €-165,36 |
| MAIN | RANGE_HIGH_VOL | 2 | 17 | 17 | 17,65% | 0,47 | -0,29R | €-48,55 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 4 | 35 | 35 | 25,71% | 0,65 | -0,23R | €-79,75 |
| MAIN | TREND_DOWN | 2 | 45 | 45 | 28,89% | 0,82 | -0,10R | €-46,67 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 1 | 38 | 38 | 31,58% | 1,05 | 0,03R | €11,82 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,42 | 0,25R | €17,52 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 0,85 | -0,07R | €-9,35 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 5 | 58 | 58 | 22,41% | 0,43 | -0,40R | €-229,51 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 86 | 86 | 33,72% | 0,90 | -0,06R | €-51,31 |
| Bilanciata 1H V1 | RANGE | 2 | 169 | 169 | 39,05% | 1,07 | 0,03R | €56,92 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 3 | 39 | 39 | 25,64% | 0,53 | -0,31R | €-120,94 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 4 | 93 | 93 | 38,71% | 1,25 | 0,12R | €113,98 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 85 | 85 | 30,59% | 0,70 | -0,16R | €-135,86 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 1 | 109 | 109 | 30,28% | 0,92 | -0,04R | €-40,50 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 62 | 52 | 35,48% | 1,01 | 0,00R | €2,56 |
| Bilanciata 1H V2 | RANGE | 4 | 122 | 110 | 35,25% | 0,84 | -0,09R | €-113,72 |
| Bilanciata 1H V2 | TRANSITION | 4 | 79 | 67 | 40,51% | 1,39 | 0,19R | €150,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 5 | 44 | 44 | 29,55% | 0,57 | -0,27R | €-119,76 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 47 | 47 | 29,79% | 1,04 | 0,02R | €9,50 |
| Bilanciata 1H V3 Filtered | RANGE | 2 | 116 | 116 | 40,52% | 1,08 | 0,04R | €43,95 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 16 | 16 | 25,00% | 0,61 | -0,25R | €-40,63 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 3 | 51 | 51 | 35,29% | 1,10 | 0,05R | €24,61 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 2 | 59 | 59 | 35,59% | 0,66 | -0,19R | €-114,01 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 62 | 62 | 30,65% | 1,06 | 0,03R | €18,24 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 5 | 33 | 33 | 24,24% | 0,30 | -0,46R | €-153,14 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 45 | 45 | 31,11% | 1,12 | 0,07R | €30,49 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 2 | 94 | 94 | 38,30% | 0,85 | -0,08R | €-72,21 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 28,57% | 0,77 | -0,14R | €-19,81 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 3 | 43 | 43 | 34,88% | 1,10 | 0,04R | €18,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 2 | 60 | 60 | 35,00% | 0,64 | -0,21R | €-125,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 1 | 41 | 41 | 24,39% | 0,78 | -0,10R | €-42,60 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 12 | 12 | 16,67% | 0,22 | -0,54R | €-64,95 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 48,84% | 1,27 | 0,11R | €46,79 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 42 | 42 | 38,10% | 0,93 | -0,04R | €-16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 30,61% | 0,80 | -0,08R | €-38,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 23 | 23 | 17,39% | 0,31 | -0,46R | €-106,72 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 64 | 64 | 45,31% | 1,11 | 0,05R | €33,16 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 143 | 143 | 34,97% | 0,78 | -0,12R | €-166,44 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 2 | 57 | 57 | 38,60% | 1,06 | 0,03R | €14,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 1 | 74 | 74 | 28,38% | 0,78 | -0,10R | €-70,48 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 41 | 41 | 19,51% | 0,35 | -0,46R | €-188,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 173 | 173 | 39,31% | 0,98 | -0,01R | €-21,26 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 2 | 59 | 59 | 40,68% | 1,20 | 0,07R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 1 | 90 | 90 | 27,78% | 0,68 | -0,16R | €-142,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 4 | 84 | 84 | 22,62% | 0,41 | -0,40R | €-332,44 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 37,84% | 0,85 | -0,08R | €-62,01 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 195 | 195 | 36,92% | 0,82 | -0,09R | €-184,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 2 | 32 | 32 | 43,75% | 1,17 | 0,07R | €23,95 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 3 | 83 | 83 | 40,96% | 1,29 | 0,11R | €91,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 1 | 104 | 104 | 27,88% | 0,70 | -0,15R | €-160,49 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 4 | 48 | 48 | 25,00% | 0,44 | -0,39R | €-185,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 0,89 | -0,06R | €-29,98 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 113 | 113 | 42,48% | 1,11 | 0,05R | €59,96 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 2 | 14 | 14 | 50,00% | 1,43 | 0,16R | €22,79 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 52 | 52 | 40,38% | 1,25 | 0,10R | €50,06 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 59 | 59 | 27,12% | 0,60 | -0,22R | €-127,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 82 | 82 | 21,95% | 0,41 | -0,39R | €-319,14 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 76 | 76 | 39,47% | 1,03 | 0,02R | €13,46 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 1 | 179 | 179 | 34,64% | 0,77 | -0,12R | €-219,83 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 3 | 31 | 31 | 32,26% | 0,80 | -0,10R | €-29,60 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 77 | 77 | 37,66% | 1,39 | 0,15R | €117,34 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 95 | 95 | 21,05% | 0,53 | -0,25R | €-237,49 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 0 | 40 | 33 | 37,50% | 0,73 | -0,14R | €-57,99 |
| Rapida 1H V2 | TRANSITION | 0 | 7 | 7 | 57,14% | 0,81 | -0,07R | €-4,61 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 82 | 82 | 23,17% | 0,43 | -0,37R | €-303,34 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 70 | 70 | 38,57% | 0,94 | -0,03R | €-23,47 |
| Rapida 1H V3 Filtered | RANGE | 1 | 174 | 174 | 37,36% | 0,82 | -0,09R | €-164,09 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 3 | 28 | 28 | 42,86% | 1,06 | 0,03R | €7,87 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 3 | 74 | 74 | 37,84% | 1,08 | 0,04R | €26,23 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 108 | 108 | 37,04% | 1,00 | 0,00R | €0,97 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 61 | 61 | 24,59% | 0,46 | -0,37R | €-225,53 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 61 | 61 | 40,98% | 1,03 | 0,01R | €8,26 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 141 | 141 | 38,30% | 0,90 | -0,05R | €-68,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 3 | 17 | 17 | 47,06% | 1,38 | 0,14R | €24,46 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 2 | 56 | 56 | 37,50% | 0,98 | -0,01R | €-5,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 69 | 69 | 28,99% | 0,67 | -0,17R | €-116,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 14 | 14 | 21,43% | 0,17 | -0,68R | €-94,58 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 79 | 79 | 43,04% | 0,86 | -0,08R | €-63,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 2 | 32 | 32 | 56,25% | 1,29 | 0,11R | €36,12 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 15,38% | 0,18 | -0,66R | €-85,74 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 81 | 81 | 39,51% | 0,94 | -0,03R | €-27,15 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 2 | 32 | 32 | 37,50% | 1,09 | 0,03R | €10,98 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 22 | 22 | 13,64% | 0,19 | -0,62R | €-136,40 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 61 | 61 | 37,70% | 0,87 | -0,07R | €-40,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 98 | 98 | 40,82% | 0,93 | -0,04R | €-34,70 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 35,71% | 0,87 | -0,06R | €-8,64 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 2 | 47 | 47 | 40,43% | 1,17 | 0,07R | €32,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 4 | 53 | 53 | 20,75% | 0,38 | -0,44R | €-235,44 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 176 | 176 | 38,64% | 0,87 | -0,07R | €-116,04 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 2 | 58 | 58 | 32,76% | 0,91 | -0,04R | €-22,74 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 94 | 94 | 31,91% | 0,79 | -0,11R | €-104,22 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 4 | 81 | 81 | 23,46% | 0,44 | -0,36R | €-291,91 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 36,23% | 0,83 | -0,09R | €-64,59 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 172 | 172 | 37,21% | 0,80 | -0,10R | €-178,82 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 3 | 27 | 27 | 44,44% | 1,15 | 0,07R | €18,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 3 | 69 | 69 | 37,68% | 1,10 | 0,04R | €28,99 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 91 | 91 | 30,77% | 0,75 | -0,13R | €-121,78 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 6 | 18 | 18 | 22,22% | 0,98 | -0,01R | €-1,83 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 4 | 34 | 34 | 23,53% | 0,48 | -0,41R | €-138,96 |
| SHADOW_4H_WIDE | RANGE | 6 | 66 | 66 | 15,15% | 0,59 | -0,29R | €-194,14 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 1 | 15 | 15 | 13,33% | 0,60 | -0,24R | €-36,41 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 4 | 37 | 37 | 13,51% | 0,37 | -0,47R | €-173,36 |
| SHADOW_4H_WIDE | TREND_DOWN | 4 | 43 | 43 | 27,91% | 1,03 | 0,02R | €9,48 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 38 | 38 | 23,68% | 1,04 | 0,02R | €8,48 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 0,99 | -0,00R | €-0,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 64 | 64 | 48,44% | 1,13 | 0,06R | €37,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 1 | 6 | 6 | 50,00% | 0,99 | -0,00R | €-0,21 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 13 | 13 | 53,85% | 1,74 | 0,31R | €39,93 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 5 | 49 | 49 | 26,53% | 0,60 | -0,24R | €-118,41 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 62 | 62 | 33,87% | 0,89 | -0,06R | €-39,82 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 140 | 140 | 41,43% | 0,97 | -0,01R | €-20,28 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 2 | 28 | 28 | 39,29% | 1,10 | 0,04R | €12,47 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 72 | 72 | 41,67% | 1,46 | 0,21R | €150,67 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 4 | 71 | 71 | 35,21% | 0,91 | -0,05R | €-32,20 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 94 | 94 | 36,17% | 1,12 | 0,05R | €48,17 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 18,75% | 0,45 | -0,32R | €-51,25 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 56 | 56 | 33,93% | 0,90 | -0,06R | €-32,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 68 | 68 | 47,06% | 1,21 | 0,10R | €70,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,85 | -0,07R | €-8,04 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 39 | 39 | 46,15% | 2,07 | 0,34R | €133,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 2 | 42 | 42 | 35,71% | 1,10 | 0,05R | €19,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 4 | 62 | 62 | 32,26% | 0,62 | -0,21R | €-127,56 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 69 | 69 | 37,68% | 0,88 | -0,06R | €-41,75 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 138 | 138 | 41,30% | 1,11 | 0,05R | €67,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 2 | 34 | 34 | 44,12% | 0,99 | -0,00R | €-0,84 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 63 | 63 | 46,03% | 1,24 | 0,10R | €64,17 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 3 | 95 | 95 | 37,89% | 0,91 | -0,04R | €-34,85 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 96 | 96 | 50,00% | 1,33 | 0,13R | €127,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 5 | 49 | 49 | 26,53% | 0,64 | -0,22R | €-107,16 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 35,00% | 0,91 | -0,05R | €-29,68 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 128 | 128 | 44,53% | 1,04 | 0,02R | €26,19 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 2 | 26 | 26 | 46,15% | 1,34 | 0,14R | €35,41 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 55 | 55 | 45,45% | 1,36 | 0,16R | €86,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 4 | 71 | 71 | 39,44% | 0,91 | -0,04R | €-31,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 1 | 73 | 73 | 36,99% | 0,73 | -0,12R | €-87,95 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 2 | 33 | 33 | 36,36% | 0,91 | -0,05R | €-16,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 2 | 33 | 33 | 36,36% | 0,90 | -0,06R | €-18,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 18 | 18 | 27,78% | 0,63 | -0,21R | €-38,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 38 | 38 | 39,47% | 1,17 | 0,09R | €34,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 2 | 26 | 26 | 34,62% | 0,99 | -0,01R | €-1,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 6 | 80 | 80 | 40,00% | 1,10 | 0,05R | €40,40 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 1 | 99 | 99 | 34,34% | 0,80 | -0,09R | €-93,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,36 | -0,53R | €-68,31 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 12 | 12 | 25,00% | 0,36 | -0,37R | €-43,88 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 2,02 | 0,45R | €22,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 32 | 32 | 50,00% | 1,38 | 0,18R | €57,26 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,84R | €-33,76 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 1 | 5 | 5 | 80,00% | 4,65 | 0,83R | €41,31 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 2 | 18 | 18 | 11,11% | 0,20 | -0,51R | €-92,01 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 54 | 54 | 35,19% | 1,01 | 0,01R | €4,26 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 78 | 78 | 44,87% | 1,42 | 0,20R | €156,89 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,67 | -0,16R | €-17,68 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 2 | 55 | 55 | 43,64% | 1,74 | 0,34R | €186,29 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 43 | 43 | 30,23% | 0,73 | -0,15R | €-65,86 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 5 | 37 | 37 | 27,03% | 0,63 | -0,22R | €-82,70 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 56 | 56 | 28,57% | 0,69 | -0,21R | €-118,27 |
| SHADOW_COMBO_TREND | RANGE | 0 | 120 | 120 | 34,17% | 0,99 | -0,01R | €-7,70 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 19 | 19 | 36,84% | 1,37 | 0,14R | €27,46 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 60 | 60 | 36,67% | 1,36 | 0,19R | €114,33 |
| SHADOW_COMBO_TREND | TREND_DOWN | 5 | 62 | 62 | 30,65% | 0,73 | -0,14R | €-89,10 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 1 | 72 | 72 | 29,17% | 1,03 | 0,01R | €9,60 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-52,46 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,61 | -0,25R | €-17,63 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -0,75R | €-45,24 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,97 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 28 | 28 | 21,43% | 0,49 | -0,39R | €-109,94 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 22 | 22 | 18,18% | 0,23 | -0,63R | €-139,43 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 57 | 57 | 31,58% | 0,94 | -0,04R | €-20,96 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 11 | 11 | 45,45% | 1,53 | 0,25R | €27,28 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 2 | 24 | 24 | 41,67% | 1,71 | 0,34R | €82,19 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 2 | 20 | 20 | 25,00% | 0,29 | -0,51R | €-102,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 16,67% | 0,21 | -0,66R | €-118,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 21,43% | 0,16 | -0,64R | €-89,01 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 1 | 37 | 37 | 32,43% | 0,84 | -0,10R | €-36,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 55,56% | 2,51 | 0,53R | €47,54 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 2 | 17 | 17 | 52,94% | 2,80 | 0,66R | €111,46 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 2 | 18 | 18 | 27,78% | 0,32 | -0,51R | €-92,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 5 | 40 | 40 | 25,00% | 0,53 | -0,30R | €-120,35 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 52 | 52 | 26,92% | 0,66 | -0,24R | €-123,18 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 119 | 119 | 34,45% | 1,04 | 0,02R | €27,38 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 2 | 21 | 21 | 42,86% | 1,74 | 0,26R | €55,14 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 58 | 58 | 36,21% | 1,25 | 0,14R | €78,65 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 4 | 65 | 65 | 30,77% | 0,70 | -0,17R | €-107,60 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 75 | 75 | 28,00% | 0,95 | -0,03R | €-21,00 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-53,00 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,10 | -0,75R | €-29,95 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,18 | -0,69R | €-27,47 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,50R | €5,03 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,11R | €1,10 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 20,00% | 0,15 | -0,77R | €-38,41 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,66 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,08 | -0,77R | €-30,63 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 6 | 6 | 33,33% | 0,68 | -0,24R | €-14,10 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 0,02R | €0,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 2 | 17 | 17 | 23,53% | 0,63 | -0,27R | €-45,34 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 32,35% | 0,94 | -0,04R | €-13,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 1 | 77 | 77 | 31,17% | 1,00 | 0,00R | €0,98 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 4 | 30 | 30 | 46,67% | 1,78 | 0,40R | €120,27 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 2 | 46 | 46 | 34,78% | 1,09 | 0,06R | €25,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 1 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 4 | 22 | 22 | 50,00% | 0,99 | -0,01R | €-1,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 140 | 140 | 65,00% | 1,37 | 0,12R | €168,51 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 72 | 72 | 75,00% | 1,91 | 0,22R | €160,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 2 | 75 | 75 | 65,33% | 1,35 | 0,12R | €90,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 3 | 15 | 15 | 20,00% | 0,57 | -0,29R | €-44,23 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 1 | 78 | 78 | 33,33% | 1,11 | 0,06R | €49,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 4 | 29 | 29 | 37,93% | 1,23 | 0,14R | €40,36 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 2 | 42 | 42 | 38,10% | 1,23 | 0,14R | €58,57 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 11 | 11 | 27,27% | 0,97 | -0,02R | €-2,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 1 | 70 | 70 | 30,00% | 1,10 | 0,06R | €43,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 3 | 27 | 27 | 40,74% | 1,41 | 0,24R | €64,16 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 2 | 39 | 39 | 38,46% | 1,25 | 0,16R | €60,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 0,00% | 0,00 | -0,91R | €-82,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 58 | 58 | 36,21% | 1,14 | 0,09R | €51,45 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 4 | 22 | 22 | 50,00% | 2,31 | 0,56R | €122,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 31 | 31 | 25,81% | 0,70 | -0,22R | €-66,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 3 | 15 | 15 | 20,00% | 0,52 | -0,36R | €-54,10 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 1 | 73 | 73 | 32,88% | 1,10 | 0,06R | €44,42 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 4 | 29 | 29 | 41,38% | 1,42 | 0,24R | €70,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 2 | 40 | 40 | 37,50% | 1,20 | 0,12R | €48,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 6 | 48 | 48 | 20,83% | 0,43 | -0,37R | €-177,94 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 31,88% | 0,83 | -0,11R | €-74,86 |
| Forza relativa 1H V1 | RANGE | 2 | 162 | 162 | 30,86% | 0,85 | -0,08R | €-129,80 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 24 | 24 | 29,17% | 0,67 | -0,16R | €-38,30 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 2 | 71 | 71 | 38,03% | 1,46 | 0,23R | €161,78 |
| Forza relativa 1H V1 | TREND_DOWN | 3 | 72 | 72 | 29,17% | 0,87 | -0,07R | €-50,78 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 1 | 95 | 95 | 25,26% | 0,91 | -0,05R | €-45,58 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 3 | 22 | 22 | 31,82% | 0,84 | -0,08R | €-18,61 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 29 | 26 | 34,48% | 1,17 | 0,09R | €26,73 |
| Forza relativa 1H V2 | RANGE | 3 | 70 | 67 | 35,71% | 0,98 | -0,01R | €-9,06 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 3 | 39 | 34 | 41,03% | 1,80 | 0,36R | €140,16 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 34 | 33 | 29,41% | 0,95 | -0,02R | €-7,23 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 4 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 16 | 16 | 37,50% | 1,22 | 0,10R | €15,71 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 2 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 1 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 4 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 16 | 16 | 37,50% | 1,22 | 0,10R | €15,71 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 2 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 1 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 4 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 16 | 16 | 37,50% | 1,22 | 0,10R | €15,71 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 2 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 1 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 4 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,07 | 0,03R | €4,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 71 | 71 | 29,58% | 0,65 | -0,19R | €-135,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,32 | 0,14R | €23,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 35 | 35 | 40,00% | 1,09 | 0,05R | €17,72 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 40 | 40 | 27,50% | 0,38 | -0,36R | €-144,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 23 | 23 | 4,35% | 0,16 | -0,42R | €-97,06 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 2 | 30 | 30 | 36,67% | 0,35 | -0,39R | €-117,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 63 | 63 | 55,56% | 0,69 | -0,13R | €-84,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 2 | 20 | 20 | 65,00% | 1,57 | 0,20R | €40,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 28 | 28 | 60,71% | 1,52 | 0,22R | €60,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 64 | 64 | 54,69% | 0,65 | -0,15R | €-95,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 1 | 19 | 19 | 42,11% | 0,65 | -0,16R | €-29,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 2 | 26 | 26 | 34,62% | 0,24 | -0,47R | €-121,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 56 | 56 | 55,36% | 0,42 | -0,25R | €-138,62 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 2 | 18 | 18 | 61,11% | 1,41 | 0,16R | €29,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 27 | 27 | 62,96% | 1,58 | 0,23R | €61,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 54 | 54 | 53,70% | 0,65 | -0,15R | €-81,86 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 1 | 18 | 18 | 38,89% | 0,34 | -0,31R | €-55,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,67 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 54 | 54 | 29,63% | 0,76 | -0,13R | €-71,01 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,77 | -0,13R | €-12,60 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,67 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 55 | 55 | 29,09% | 0,74 | -0,15R | €-82,12 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,77 | -0,13R | €-12,60 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,67 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 55 | 55 | 29,09% | 0,74 | -0,15R | €-82,12 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,77 | -0,13R | €-12,60 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 17 | 17 | 11,76% | 0,23 | -0,48R | €-80,99 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 54 | 54 | 35,19% | 1,02 | 0,01R | €4,85 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 73 | 73 | 45,21% | 1,57 | 0,26R | €189,87 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,67 | -0,16R | €-17,68 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 2 | 51 | 51 | 43,14% | 1,81 | 0,36R | €183,87 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 62 | 62 | 29,03% | 0,95 | -0,02R | €-14,90 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 0,00% | 0,00 | -0,76R | €-53,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 47 | 47 | 27,66% | 0,81 | -0,10R | €-47,19 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 6,67% | 0,02 | -0,68R | €-102,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 35,29% | 0,94 | -0,03R | €-16,02 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 68 | 68 | 44,12% | 1,42 | 0,20R | €136,64 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,84 | -0,07R | €-6,98 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 2 | 39 | 39 | 46,15% | 2,24 | 0,46R | €179,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 13,33% | 0,15 | -0,41R | €-61,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 1 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 40,00% | 1,09 | 0,03R | €3,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 40 | 40 | 50,00% | 1,40 | 0,16R | €62,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 7,69% | 0,02 | -0,70R | €-91,01 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 71 | 71 | 46,48% | 1,52 | 0,23R | €166,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 45,45% | 0,93 | -0,03R | €-2,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 3 | 35 | 35 | 40,00% | 1,71 | 0,29R | €102,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 26,32% | 0,57 | -0,21R | €-39,94 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 1 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 40,00% | 1,09 | 0,03R | €3,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 42 | 42 | 47,62% | 1,32 | 0,13R | €52,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 13,33% | 0,25 | -0,47R | €-69,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 71 | 71 | 46,48% | 1,52 | 0,23R | €166,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 45,45% | 0,93 | -0,03R | €-2,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 3 | 36 | 36 | 38,89% | 1,59 | 0,26R | €91,94 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 21 | 21 | 28,57% | 0,53 | -0,23R | €-48,61 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 57 | 57 | 43,86% | 0,96 | -0,02R | €-11,39 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 1 | 74 | 74 | 45,95% | 1,40 | 0,16R | €119,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,89 | -0,03R | €-4,89 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 2 | 47 | 47 | 48,94% | 1,35 | 0,14R | €66,28 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 56 | 56 | 44,64% | 0,92 | -0,03R | €-18,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 10 | 10 | 20,00% | 0,44 | -0,30R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 55 | 55 | 32,73% | 0,98 | -0,01R | €-7,49 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 64 | 64 | 42,19% | 1,44 | 0,21R | €136,38 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,83 | -0,07R | €-7,48 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 2 | 39 | 39 | 43,59% | 1,98 | 0,39R | €152,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 41 | 41 | 29,27% | 0,77 | -0,13R | €-54,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 9 | 9 | 11,11% | 0,03 | -0,56R | €-50,03 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 56 | 56 | 33,93% | 0,92 | -0,04R | €-23,50 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 59 | 59 | 40,68% | 1,44 | 0,22R | €131,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,58 | -0,21R | €-23,05 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 2 | 33 | 33 | 42,42% | 2,48 | 0,51R | €169,33 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 38 | 38 | 28,95% | 0,79 | -0,11R | €-43,01 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 2 | 18 | 18 | 16,67% | 0,33 | -0,46R | €-83,20 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 56 | 56 | 32,14% | 0,86 | -0,08R | €-42,22 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 75 | 75 | 49,33% | 1,64 | 0,27R | €205,66 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 12 | 12 | 25,00% | 0,56 | -0,28R | €-33,43 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 2 | 55 | 55 | 41,82% | 1,62 | 0,26R | €142,69 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 78 | 78 | 34,62% | 1,08 | 0,04R | €29,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,84 | -0,09R | €-1,73 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,41 | -0,47R | €-32,89 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,86 | 0,38R | €19,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-19T04:06:06+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **656**
- Scenari virtuali ancora attivi: **13970**
- Gruppi in attesa dell'uscita originale: **337**
- Gruppi con originale chiuso ma Shadow ancora attive: **319**
- Confronti completati: **253342**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 5919 | 5992 | +€0,96 | 48,2% | 1327 | 711 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5916 | 5989 | +€1,05 | 43,7% | 844 | 1061 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 5904 | 5973 | +€9,05 | 52,4% | 1663 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5904 | 5973 | +€8,16 | 51,8% | 1646 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5904 | 5973 | +€6,91 | 50,3% | 1656 | 129 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5904 | 5973 | +€5,68 | 49,8% | 1820 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5898 | 5967 | +€8,02 | 45,5% | 1350 | 111 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5898 | 5967 | +€6,82 | 45,5% | 1285 | 177 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5898 | 5967 | +€6,21 | 43,8% | 1469 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5896 | 5965 | +€5,81 | 44,9% | 1165 | 307 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5894 | 5963 | +€5,54 | 50,4% | 1572 | 193 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5894 | 5963 | +€2,74 | 39,1% | 760 | 946 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5890 | 5963 | €-3,49 | 35,7% | 514 | 1502 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5881 | 5950 | +€3,97 | 43,3% | 1040 | 530 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5880 | 5949 | +€1,92 | 36,7% | 619 | 1210 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5863 | 5932 | +€5,27 | 35,8% | 898 | 533 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5843 | 5909 | +€4,96 | 39,2% | 482 | 842 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5825 | 5894 | €-1,88 | 33,8% | 527 | 1401 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5796 | 5865 | €-2,52 | 36,9% | 1048 | 1087 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5702 | 5771 | €-6,42 | 28,8% | 491 | 1607 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-19T04:06:17+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **253342**
- Valutazioni prodotte: **19467**
- Candidature al Blocco 5: **50**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 317 | 0,464 | 0,309 | 0,355 | 62,5% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 4492 | 0,241 | 0,159 | 0,207 | 55,8% | 88,8 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 4492 | 0,226 | 0,149 | 0,194 | 55,7% | 88,7 | ELIGIBLE_FOR_MUTATION |
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

Generato: 2026-08-19T04:08:56+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 73 | 100,00% | 1,01 | +€10,08 | +€0,14 | 2,31% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 73 | 100,00% | 1,00 | +€3,17 | +€0,04 | 2,58% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 39 | 97,50% | 0,99 | €-5,57 | €-0,14 | 2,95% | EARLY_NOT_CONFIRMED |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 31 | 93,94% | 0,00 | €-346,24 | €-11,17 | 3,46% | EARLY_NOT_CONFIRMED |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 74 | 100,00% | 1,06 | +€76,98 | +€1,04 | 2,13% | NOT_READY_FOR_PROMOTION |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-19T04:05:55+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **63**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **620.38 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 174 | 0 | 22970.67 |
| DOWN_20 | 174 | 0 | 45941.33 |
| DOWN_30 | 174 | 8 | 69040.67 |
| DOWN_40 | 174 | 52 | 86563.10 |
| UP_10 | 154 | 0 | 21179.34 |
| UP_20 | 154 | 0 | 42358.67 |
| UP_30 | 154 | 0 | 63538.01 |
| UP_40 | 154 | 66 | 78252.35 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-19T04:05:15+00:00

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

Generato: 2026-08-19T04:09:00+00:00

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

Generato: 2026-08-19T04:09:00+00:00

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

Generato: 2026-08-19T04:09:00+00:00

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

Generato: 2026-08-19T04:09:00+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 19.1 | E | 131 | 1.12 | 0.056 | 8.02 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 15.1 | E | 74 | 1.17 | 0.079 | 5.98 |
| 3 | SHADOW_1H_FAST_V3 | BASELINE | 15.0 | E | 153 | 0.86 | -0.069 | 21.37 |
| 4 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.4 | E | 127 | 0.95 | -0.024 | 16.32 |
| 5 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 13.4 | E | 50 | 1.22 | 0.108 | 5.87 |
| 6 | SHADOW_DONCHIAN_1H | BASELINE | 13.2 | E | 64 | 1.16 | 0.093 | 8.55 |
| 7 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 12.9 | E | 116 | 0.92 | -0.043 | 23.13 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 12.7 | E | 106 | 0.94 | -0.033 | 12.98 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 11.7 | E | 127 | 0.79 | -0.115 | 21.34 |
| 10 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 11.2 | E | 121 | 0.78 | -0.128 | 25.12 |

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

Generato: 2026-08-19T04:09:00+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **644**
- Strategie preferite nel regime corrente: **2**
- Strategie da evitare nel regime corrente: **20**
- Memorie contestuali: **304**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.6 | 4 | 99.00 | 0.972 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.5 | 12 | 2.82 | 0.322 | 1.04 |
| 5 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 70.0 | 8 | 2.44 | 0.587 | 2.16 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | COMPATIBLE | 65.8 | 48 | 1.39 | 0.174 | 5.17 |
| 7 | SHADOW_RSI_LONG_5X_RSI20 | shadow-rsi-long-5x-rsi20 | INSUFFICIENT | 65.1 | 9 | 1.80 | 0.319 | 2.40 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 61.6 | 9 | 1.61 | 0.224 | 2.21 |
| 9 | SHADOW_1H_FAST | shadow-1h-fast | COMPATIBLE | 55.1 | 61 | 1.27 | 0.113 | 6.50 |
| 10 | SHADOW_1H_FAST_NO_PEPE_V1 | shadow-1h-fast-no-pepe-v1 | NEUTRAL | 53.8 | 87 | 1.15 | 0.073 | 6.07 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-19T04:09:00+00:00

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

Generato: 2026-08-19T04:05:55+00:00

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
