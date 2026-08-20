# Paper trading automatico KuCoin

Generato: 2026-08-20T00:09:17+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-20T00:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-20T00:05:28+00:00 | 2026-08-20T00:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-19T23:45:00+00:00 | 2026-08-19T23:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-19T23:00:00+00:00 | 2026-08-19T23:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-19T20:00:00+00:00 | 2026-08-19T20:00:00+00:00 | 5,6 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Scanner | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | ZEC | 60m | LONG | 5,18 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ETH | 240m | LONG | 7,75 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | LINK | 240m | LONG | 7,50 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 6,78 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | HYPE | 240m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | SOL | 240m | LONG | 5,83 | 6,00 | 0,17 | BELOW_SCORE | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Punteggio +5.83; soglia ±6.00; mancano 0.17 punti. |
| Ampia 4H | ETH | 240m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Eth Ema 4H | ETH | 240m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Ampia 4H | ZEC | 240m | LONG | 6,78 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Ampia 4H | HYPE | 240m | LONG | 6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | SOL | 240m | LONG | 5,83 | 5,00 | 0,00 | READY | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Sol Ema 4H | SOL | 240m | LONG | 5,83 | 5,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Donchian 4H | SOL | 240m | LONG | 5,83 | 5,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 4H | SOL | 240m | LONG | 5,83 | 5,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Adaptive 4H | SOL | 240m | LONG | 5,83 | 5,00 | 0,00 | OPENED | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H — LONG senza Range High Vol | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | XRP | 60m | LONG | 5,26 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top10 Long | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top15 Long | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top20 Long | XRP | 60m | LONG | 5,26 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.664,69 | -3,35% | €-83,66 | €3.000,00 | -2,79% | 5 | 46 | 34,78% | 0,76 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 46 | 1735 | PRIME INDICAZIONI | 50 (mancano 4) |

- Trade del Principale 4H chiusi: **46**; win rate **34,78%**; profit factor **0,76**.
- Expectancy: **€-7,25** per trade; P&L netto: **€-333,55**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.664,69 | €979,58 | €2.938,74 | €193,29 | €-0,26 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.810,07 | €3.984,43 | €7.968,86 | €163,26 | €-37,52 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.555,56 | €3.890,62 | €7.781,24 | €159,42 | €-36,64 |
| TEST | Rapida score 6–7,5 — Cost Aware | 3 | €10.480,14 | €2.195,09 | €6.585,26 | €158,14 | €-56,46 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.476,87 | €288,21 | €864,64 | €103,76 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.447,44 | €3.354,76 | €6.709,52 | €157,26 | €-11,26 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.327,06 | €3.588,32 | €7.176,64 | €156,16 | €-25,21 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.151,01 | €386,22 | €1.158,67 | €51,78 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €10.134,15 | €1.651,70 | €3.303,41 | €153,03 | €67,78 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.065,17 | €727,07 | €1.454,13 | €50,33 | €-0,29 |
| TEST | Rapida V1 — senza PEPE | 2 | €10.060,64 | €165,08 | €495,24 | €53,36 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.048,04 | €665,34 | €1.330,67 | €50,25 | €-0,27 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €10.040,93 | €333,06 | €999,18 | €49,31 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.032,41 | €797,18 | €1.594,36 | €50,17 | €-0,32 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 1 | €10.029,22 | €155,86 | €467,58 | €51,44 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.997,32 | €1.902,37 | €3.804,75 | €48,94 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €9.997,31 | €10,00 | €150,00 | €0,00 | €2,79 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.991,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €9.986,56 | €50,00 | €750,00 | €0,00 | €13,95 |
| TEST | Sol Donchian 1H | 1 | €9.982,96 | €1.046,71 | €3.140,14 | €0,00 | €15,95 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.942,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 6 | €9.940,89 | €2.430,99 | €7.292,98 | €149,30 | €8,64 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.934,78 | €94,26 | €471,29 | €0,00 | €8,77 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.910,16 | €715,87 | €1.431,74 | €49,56 | €-0,29 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.907,94 | €1.683,65 | €5.050,95 | €148,89 | €-40,66 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.892,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 5 | €9.892,95 | €3.474,41 | €6.948,81 | €149,34 | €-10,84 |
| TEST | Sol Ema 1H | 1 | €9.865,00 | €919,56 | €2.758,69 | €0,00 | €14,02 |
| TEST | Eth Donchian 1H | 1 | €9.854,37 | €760,21 | €2.280,63 | €49,27 | €0,84 |
| TEST | Eth Ema 4H | 1 | €9.841,08 | €577,20 | €1.154,41 | €49,21 | €-0,23 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €9.840,24 | €4.053,32 | €8.106,64 | €148,94 | €-34,59 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 4 | €9.817,05 | €3.967,89 | €7.935,78 | €148,00 | €-32,75 |
| TEST | Eth Bollinger 1H | 1 | €9.787,42 | €679,82 | €2.039,45 | €48,91 | €6,44 |
| TEST | Eth Adaptive 1H | 1 | €9.784,04 | €670,92 | €2.012,75 | €48,92 | €0,74 |
| TEST | FAST NoHigh <7,5 · SHORT only | 1 | €9.779,65 | €151,98 | €455,94 | €50,16 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.751,16 | €2.743,93 | €5.487,86 | €146,41 | €-19,65 |
| TEST | Scanner Bottom15 Short | 4 | €9.751,16 | €2.743,93 | €5.487,86 | €146,41 | €-19,65 |
| TEST | Scanner Bottom20 Short | 4 | €9.751,16 | €2.743,93 | €5.487,86 | €146,41 | €-19,65 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.730,39 | €404,89 | €809,78 | €48,76 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.724,81 | €563,60 | €1.690,79 | €48,66 | €-6,02 |
| TEST | Sol Adaptive 1H | 1 | €9.724,69 | €906,48 | €2.719,45 | €0,00 | €13,82 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.702,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.683,59 | €2.724,94 | €5.449,88 | €145,40 | €-19,51 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.668,86 | €2.720,79 | €5.441,59 | €145,18 | €-19,48 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €9.620,68 | €3.838,69 | €7.677,38 | €192,44 | €-38,12 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.608,00 | €399,80 | €799,60 | €48,15 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.594,45 | €2.699,86 | €5.399,71 | €144,06 | €-19,33 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €9.520,81 | €3.050,88 | €6.101,75 | €143,32 | €-10,20 |
| TEST | Scanner Top15 Long | 5 | €9.520,81 | €3.050,88 | €6.101,75 | €143,32 | €-10,20 |
| TEST | Scanner Top20 Long | 5 | €9.520,81 | €3.050,88 | €6.101,75 | €143,32 | €-10,20 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 1 | €9.518,26 | €196,64 | €589,91 | €45,15 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 5 | €9.499,66 | €3.336,28 | €6.672,56 | €143,40 | €-10,41 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 2 | €9.473,78 | €159,62 | €478,85 | €51,41 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.469,83 | €774,53 | €2.323,58 | €97,36 | €8,81 |
| TEST | Top 5 + BTC — Guard | 5 | €9.459,22 | €3.027,78 | €6.055,55 | €189,21 | €-14,30 |
| TEST | Rapida V3 — qualità completa + profit lock | 1 | €9.448,26 | €195,47 | €586,41 | €44,88 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.444,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 2 | €9.436,68 | €361,89 | €1.085,67 | €96,46 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 2 | €9.411,88 | €158,57 | €475,72 | €51,08 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 6 | €9.387,03 | €1.243,32 | €3.729,96 | €186,30 | €-14,74 |
| TEST | Master Adaptive Runner25 V1 | 2 | €9.378,60 | €211,06 | €422,12 | €50,65 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 0 | €9.377,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.371,33 | €1.592,46 | €4.777,39 | €140,82 | €-38,46 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 2 | €9.332,66 | €220,83 | €441,66 | €0,59 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 1 | €9.288,56 | €371,68 | €743,36 | €47,16 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €9.286,47 | €3.612,51 | €7.225,01 | €185,76 | €-23,44 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €9.281,04 | €3.610,39 | €7.220,78 | €185,65 | €-23,43 |
| TEST | Rapida V3 — senza ESPORTS | 2 | €9.266,23 | €153,88 | €461,65 | €49,68 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 5 | €9.239,23 | €2.957,36 | €5.914,72 | €184,81 | €-13,97 |
| TEST | Top 5 + BTC — BTC≤3 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 4 | €9.230,24 | €3.682,90 | €7.365,81 | €184,63 | €-36,57 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 1 | €9.151,18 | €135,05 | €405,16 | €0,00 | €0,00 |
| TEST | Combo Trend | 2 | €9.148,47 | €222,82 | €445,65 | €0,96 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.114,86 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.057,29 | €186,88 | €373,77 | €44,85 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 4 | €9.018,92 | €3.598,58 | €7.197,17 | €180,40 | €-35,73 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 0 | €8.928,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 2 | €8.883,06 | €208,04 | €416,07 | €0,72 | €0,00 |
| TEST | Forza relativa 1H V1 | 1 | €8.800,06 | €1.513,47 | €3.026,93 | €45,42 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €8.741,01 | €202,90 | €405,81 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 0 | €8.519,16 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.664,69 | €-333,55 | 46 | 46 | 34,78% | 0,76 | €-7,25 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.810,07 | €852,38 | 74 | 74 | 50,00% | 1,49 | €11,52 | 3,63% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.555,56 | €596,87 | 42 | 42 | 50,00% | 1,69 | €14,21 | 3,63% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.480,14 | €540,56 | 83 | 83 | 49,40% | 1,28 | €6,51 | 4,41% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.476,87 | €477,55 | 29 | 29 | 48,28% | 1,77 | €16,47 | 2,40% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.447,44 | €462,84 | 93 | 93 | 46,24% | 1,21 | €4,98 | 8,85% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.327,06 | €356,57 | 60 | 60 | 50,00% | 1,29 | €5,94 | 4,33% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.151,01 | €151,70 | 36 | 36 | 47,22% | 1,14 | €4,21 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Ampia 4H | Confluenza trend | €10.134,15 | €68,13 | 44 | 44 | 27,27% | 1,06 | €1,55 | 4,45% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.065,17 | €66,34 | 4 | 4 | 50,00% | 1,63 | €16,58 | 1,05% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.060,64 | €60,94 | 135 | 135 | 44,44% | 1,02 | €0,45 | 4,46% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.048,04 | €49,10 | 4 | 4 | 50,00% | 1,47 | €12,27 | 1,01% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.040,93 | €41,53 | 34 | 30 | 44,12% | 1,05 | €1,22 | 3,89% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.032,41 | €33,68 | 2 | 2 | 50,00% | 1,63 | €16,84 | 0,72% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.029,22 | €29,50 | 121 | 121 | 43,80% | 1,01 | €0,24 | 7,10% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
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
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.997,32 | €-0,41 | 37 | 37 | 43,24% | 1,00 | €-0,01 | 3,91% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.997,31 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,28 | €-8,72 | 13 | 13 | 61,54% | 0,97 | €-0,67 | 2,10% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.986,56 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.982,96 | €-31,11 | 9 | 9 | 44,44% | 0,87 | €-3,46 | 2,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Ema 1H | Trend following EMA | €9.942,20 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.940,89 | €-119,73 | 154 | 153 | 36,36% | 0,96 | €-0,78 | 6,56% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.934,78 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Sol Ema 4H | Trend following EMA | €9.910,16 | €-88,69 | 5 | 5 | 20,00% | 0,57 | €-17,74 | 2,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.907,94 | €-48,37 | 114 | 114 | 38,60% | 0,98 | €-0,42 | 9,12% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.892,99 | €-107,01 | 8 | 8 | 37,50% | 0,66 | €-13,38 | 1,89% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.892,95 | €-92,05 | 96 | 96 | 39,58% | 0,95 | €-0,96 | 7,91% |
| TEST | Sol Ema 1H | Trend following EMA | €9.865,00 | €-147,36 | 10 | 10 | 30,00% | 0,61 | €-14,74 | 3,33% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.854,37 | €-145,10 | 8 | 8 | 25,00% | 0,56 | €-18,14 | 2,63% |
| TEST | Eth Ema 4H | Trend following EMA | €9.841,08 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,74% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.840,24 | €-120,30 | 69 | 69 | 42,03% | 0,92 | €-1,74 | 8,68% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.817,05 | €-145,44 | 66 | 66 | 40,91% | 0,91 | €-2,20 | 6,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.787,42 | €-217,80 | 4 | 4 | 25,00% | 0,07 | €-54,45 | 2,69% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.784,04 | €-215,49 | 9 | 9 | 33,33% | 0,34 | €-23,94 | 3,14% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.779,65 | €-220,08 | 85 | 85 | 42,35% | 0,88 | €-2,59 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.751,16 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.751,16 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.751,16 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.730,39 | €-272,05 | 25 | 25 | 40,00% | 0,64 | €-10,88 | 4,21% |
| TEST | Eth Ema 1H | Trend following EMA | €9.724,81 | €-268,16 | 13 | 13 | 30,77% | 0,47 | €-20,63 | 4,80% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.724,69 | €-287,49 | 11 | 11 | 27,27% | 0,36 | €-26,14 | 4,59% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.702,33 | €-365,26 | 131 | 130 | 41,98% | 0,90 | €-2,79 | 9,66% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.683,59 | €-293,72 | 57 | 57 | 33,33% | 0,78 | €-5,15 | 5,27% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.668,86 | €-308,49 | 58 | 58 | 32,76% | 0,76 | €-5,32 | 5,27% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.620,68 | €-336,60 | 81 | 81 | 37,04% | 0,84 | €-4,16 | 11,27% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.608,00 | €-394,41 | 25 | 25 | 32,00% | 0,49 | €-15,78 | 5,41% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.594,45 | €-383,06 | 85 | 85 | 32,94% | 0,79 | €-4,51 | 6,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.520,81 | €-465,22 | 66 | 66 | 42,42% | 0,73 | €-7,05 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.520,81 | €-465,22 | 66 | 66 | 42,42% | 0,73 | €-7,05 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.520,81 | €-465,22 | 66 | 66 | 42,42% | 0,73 | €-7,05 | 10,31% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.518,26 | €-481,39 | 77 | 77 | 40,26% | 0,78 | €-6,25 | 6,59% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.499,66 | €-485,93 | 97 | 97 | 38,14% | 0,77 | €-5,01 | 8,69% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.473,78 | €-531,48 | 115 | 114 | 44,35% | 0,77 | €-4,62 | 8,96% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.469,83 | €-537,49 | 78 | 71 | 41,03% | 0,72 | €-6,89 | 8,50% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.459,22 | €-522,74 | 64 | 64 | 35,94% | 0,73 | €-8,17 | 7,34% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.448,26 | €-614,84 | 83 | 82 | 44,58% | 0,76 | €-7,41 | 7,69% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.444,37 | €-621,42 | 89 | 88 | 43,82% | 0,78 | €-6,98 | 9,98% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.436,68 | €-562,66 | 110 | 110 | 40,91% | 0,80 | €-5,12 | 6,91% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.411,88 | €-593,35 | 159 | 158 | 37,74% | 0,83 | €-3,73 | 8,93% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.387,03 | €-598,45 | 59 | 59 | 37,29% | 0,67 | €-10,14 | 9,26% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,60 | €-623,54 | 50 | 50 | 30,00% | 0,65 | €-12,47 | 8,18% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.377,75 | €-622,25 | 75 | 75 | 34,67% | 0,69 | €-8,30 | 9,68% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.371,33 | €-587,35 | 70 | 70 | 35,71% | 0,65 | €-8,39 | 8,85% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.332,66 | €-667,07 | 85 | 81 | 37,65% | 0,77 | €-7,85 | 10,56% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.288,56 | €-710,99 | 50 | 50 | 28,00% | 0,55 | €-14,22 | 8,87% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.286,47 | €-685,75 | 65 | 65 | 33,85% | 0,64 | €-10,55 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.281,04 | €-691,20 | 69 | 69 | 34,78% | 0,64 | €-10,02 | 12,06% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.266,23 | €-788,05 | 131 | 130 | 37,40% | 0,73 | €-6,02 | 8,44% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.239,23 | €-743,14 | 81 | 81 | 38,27% | 0,67 | €-9,17 | 8,78% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Combo Scanner | Combo Scanner | €9.230,24 | €-728,77 | 85 | 85 | 36,47% | 0,70 | €-8,57 | 11,38% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.151,18 | €-848,58 | 120 | 120 | 36,67% | 0,69 | €-7,07 | 13,99% |
| TEST | Combo Trend | Combo Trend | €9.148,47 | €-851,27 | 122 | 122 | 33,61% | 0,74 | €-6,98 | 10,47% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,86 | €-884,87 | 37 | 37 | 37,84% | 0,48 | €-23,92 | 10,64% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.057,29 | €-942,10 | 52 | 52 | 28,85% | 0,59 | €-18,12 | 11,51% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.018,92 | €-941,03 | 73 | 73 | 34,25% | 0,50 | €-12,89 | 12,28% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €8.928,64 | €-1.071,36 | 95 | 95 | 29,47% | 0,59 | €-11,28 | 11,62% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €8.883,06 | €-1.116,73 | 91 | 91 | 29,67% | 0,49 | €-12,27 | 11,93% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.800,06 | €-1.198,23 | 104 | 104 | 27,88% | 0,54 | €-11,52 | 13,92% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.741,01 | €-1.258,75 | 80 | 80 | 38,75% | 0,55 | €-15,73 | 14,60% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €8.519,16 | €-1.480,84 | 103 | 103 | 30,10% | 0,42 | €-14,38 | 15,36% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2258,11153 | 2257,66000 | 2170,60386 | 1516,69825 | 2433,12687 | €415,70 | €1.247,11 | €48,33 | €-0,25 |
| Principale 4H | LINK | LONG | Confluenza trend | 240m | 3,0x | 10,58112 | 10,57900 | 10,13407 | 7,10698 | 11,47522 | €16,96 | €50,87 | €2,15 | €-0,01 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H — LONG senza Range High Vol | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HYPE | LONG | Confluenza trend | 60m | 3,0x | 70,90318 | 69,57800 | 68,23231 | 47,62330 | 76,24492 | €415,85 | €1.247,54 | €46,99 | €-23,32 |
| Bilanciata 1H — LONG senza Range High Vol | SOL | LONG | Confluenza trend | 60m | 3,0x | 85,02400 | 85,45600 | 85,02400 | 57,10779 | 88,06063 | €34,12 | €102,36 | €0,00 | €0,52 |
| Bilanciata 1H — LONG senza Range High Vol | ETH | LONG | Confluenza trend | 60m | 3,0x | 2265,72305 | 2257,66000 | 2200,51783 | 1521,81065 | 2396,13352 | €43,23 | €129,69 | €3,73 | €-0,46 |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | LONG | Confluenza trend | 60m | 3,0x | 561,75233 | 565,16000 | 543,45247 | 377,31031 | 598,35205 | €467,90 | €1.403,69 | €45,73 | €8,52 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | SUI | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,65261 | 0,65261 | 0,66201 | 0,86688 | 0,63381 | €26,68 | €80,03 | €1,15 | €-0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 561,75233 | 565,16000 | 543,45247 | 377,31031 | 598,35205 | €484,09 | €1.452,26 | €47,31 | €8,81 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 70,90318 | 69,57800 | 68,23231 | 47,62330 | 76,24492 | €440,14 | €1.320,43 | €49,74 | €-24,68 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 572,55449 | 565,16000 | 555,45616 | 384,56576 | 606,75113 | €559,22 | €1.677,67 | €50,10 | €-21,67 |
| Bilanciata 1H V3 Filtered | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 10,71314 | 10,57900 | 10,42552 | 7,19566 | 11,28838 | €15,59 | €46,76 | €1,26 | €-0,59 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2257,66000 | 2181,35381 | 1510,45050 | 2383,72136 | €531,07 | €1.593,21 | €47,79 | €6,27 |
| Rapida score 6–7,5 — Range Only | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 70,90318 | 69,57800 | 68,82584 | 47,62330 | 74,01919 | €598,62 | €1.795,86 | €52,62 | €-33,56 |
| Rapida score 6–7,5 — Cost Aware | LINK | LONG | Momentum / breakout | 60m | 3,0x | 10,71314 | 10,57900 | 10,48944 | 7,19566 | 11,04870 | €845,57 | €2.536,71 | €52,97 | €-31,76 |
| Rapida score 6–7,5 — Cost Aware | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2248,80967 | 2257,66000 | 2196,34402 | 1510,45050 | 2327,50816 | €750,90 | €2.252,70 | €52,56 | €8,87 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| Rapida V1 — senza PEPE | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| Rapida V1 — target pieno 2R | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| Rapida V1 — target pieno 2R | SOL | LONG | Momentum / breakout | 60m | 3,0x | 85,02400 | 85,45600 | 85,02400 | 57,10779 | 87,38582 | €1.180,81 | €3.542,44 | €0,00 | €18,00 |
| Rapida V1 — target pieno 2R | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 568,28363 | 565,16000 | 556,06598 | 381,69717 | 592,71894 | €11,94 | €35,83 | €0,77 | €-0,20 |
| Rapida V1 — target pieno 2R | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2265,72305 | 2257,66000 | 2215,00788 | 1521,81065 | 2367,15340 | €742,72 | €2.228,16 | €49,87 | €-7,93 |
| Rapida V1 — target pieno 2R | LINK | LONG | Momentum / breakout | 60m | 3,0x | 10,71314 | 10,57900 | 10,48944 | 7,19566 | 11,16055 | €32,78 | €98,34 | €2,05 | €-1,23 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered — madre | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| Rapida V3 — no volatilità HIGH | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| Rapida V3 — senza ESPORTS | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,65521 | 0,65521 | 0,67955 | 0,97953 | 0,58704 | €31,61 | €63,21 | €2,35 | €-0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 9,97398 | 10,57900 | 10,38253 | 5,03686 | 11,21104 | €560,46 | €1.120,91 | €0,00 | €67,99 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2257,66000 | 2144,35158 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €50,68 | €-0,20 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 565,27303 | 565,16000 | 531,45855 | 285,46288 | 659,95358 | €31,20 | €62,41 | €3,73 | €-0,01 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,65491 | 0,65491 | 0,66473 | 0,97909 | 0,63329 | €1.513,47 | €3.026,93 | €45,42 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SUI | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,65001 | 0,65001 | 0,65937 | 0,97176 | 0,62942 | €20,45 | €40,91 | €0,59 | €-0,00 |
| Scalp RSI Short 80 · €10 · 15x | HYPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 70,89682 | 69,57800 | 70,61254 | 75,26879 | 68,65699 | €10,00 | €150,00 | €0,00 | €2,79 |
| Scalp RSI Short 80 · €50 · 15x | HYPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 70,89682 | 69,57800 | 70,61254 | 75,26879 | 68,65699 | €50,00 | €750,00 | €0,00 | €13,95 |
| Scalp RSI Short 80 · prudente · 5x | HYPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 70,89682 | 69,57800 | 70,74186 | 84,72170 | 67,91038 | €94,26 | €471,29 | €0,00 | €8,77 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1149,26000 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €-27,38 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 89,24154 | €1.360,31 | €2.720,62 | €0,00 | €13,82 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2257,66000 | 2195,88092 | 1139,69979 | 2409,20720 | €999,19 | €1.998,39 | €53,97 | €0,73 |
| Benchmark Donchian breakout 1H | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,57900 | 10,39356 | 5,41014 | 11,51209 | €910,44 | €1.820,87 | €54,32 | €-22,80 |
| Benchmark Donchian breakout 1H | ZEC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 572,55449 | 565,16000 | 553,55635 | 289,14002 | 620,04983 | €73,24 | €146,49 | €4,86 | €-1,89 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1149,26000 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €-26,74 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 89,24154 | €1.328,28 | €2.656,56 | €0,00 | €13,50 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2257,66000 | 2195,88092 | 1139,69979 | 2409,20720 | €975,67 | €1.951,34 | €52,70 | €0,72 |
| Donchian 1H Gb20 120R V1 | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,57900 | 10,39356 | 5,41014 | 11,51209 | €889,00 | €1.778,00 | €53,04 | €-22,26 |
| Donchian 1H Gb20 120R V1 | ZEC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 572,55449 | 565,16000 | 553,55635 | 289,14002 | 620,04983 | €71,52 | €143,04 | €4,75 | €-1,85 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €21,92 | €43,84 | €0,72 | €-0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €694,13 | €1.388,25 | €52,29 | €-25,95 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.463,73 | €2.927,46 | €0,00 | €14,87 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2265,72305 | 2257,66000 | 2200,51783 | 1144,19014 | 2396,13352 | €95,49 | €190,98 | €5,50 | €-0,68 |
| Scanner Top 5 Long 1H | LINK | LONG | Scanner Top 5 Long | 60m | 2,0x | 10,57611 | 10,57900 | 10,27850 | 5,34094 | 11,17135 | €897,38 | €1.794,76 | €50,51 | €0,49 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.627,25 | €3.254,49 | €48,28 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1592,75000 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-19,33 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €632,56 | €1.265,11 | €47,66 | €-23,64 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.333,90 | €2.667,79 | €0,00 | €13,55 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2265,72305 | 2257,66000 | 2200,51783 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €4,53 | €-0,56 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 10,57611 | 10,57900 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,45 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1592,75000 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-19,65 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €632,56 | €1.265,11 | €47,66 | €-23,64 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.333,90 | €2.667,79 | €0,00 | €13,55 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2265,72305 | 2257,66000 | 2200,51783 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €4,53 | €-0,56 |
| Scanner Top15 Long | LINK | LONG | Scanner Top15 Long | 60m | 2,0x | 10,57611 | 10,57900 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,45 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1592,75000 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-19,65 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €632,56 | €1.265,11 | €47,66 | €-23,64 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.333,90 | €2.667,79 | €0,00 | €13,55 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2265,72305 | 2257,66000 | 2200,51783 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €4,53 | €-0,56 |
| Scanner Top20 Long | LINK | LONG | Scanner Top20 Long | 60m | 2,0x | 10,57611 | 10,57900 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,45 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1592,75000 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-19,65 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2377,51300 | €996,44 | €1.992,87 | €48,44 | €0,73 |
| Scanner Top 5 + forza BTC 1H | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,30153 | €968,26 | €1.936,52 | €48,43 | €-24,07 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 90,05113 | €1.131,85 | €2.263,69 | €48,39 | €-14,48 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 604,79730 | €742,15 | €1.484,30 | €47,17 | €-0,30 |
| Top 5 + BTC — solo MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2377,51300 | €934,11 | €1.868,22 | €45,41 | €0,69 |
| Top 5 + BTC — solo MFE | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,30153 | €907,70 | €1.815,39 | €45,40 | €-22,56 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 90,05113 | €1.061,05 | €2.122,10 | €45,37 | €-13,58 |
| Top 5 + BTC — solo MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 604,79730 | €695,73 | €1.391,46 | €44,22 | €-0,28 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Top 5 + BTC — Guard | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2377,51300 | €977,21 | €1.954,43 | €47,50 | €0,72 |
| Top 5 + BTC — Guard | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,30153 | €22,13 | €44,26 | €1,11 | €-0,55 |
| Top 5 + BTC — Guard | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 90,05113 | €1.108,06 | €2.216,13 | €47,38 | €-14,18 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 604,79730 | €723,60 | €1.447,20 | €46,00 | €-0,29 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2377,51300 | €954,49 | €1.908,97 | €46,40 | €0,70 |
| Top 5 + BTC — Guard + MFE | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,30153 | €21,61 | €43,23 | €1,08 | €-0,54 |
| Top 5 + BTC — Guard + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 90,05113 | €1.082,29 | €2.164,59 | €46,27 | €-13,85 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 604,79730 | €706,77 | €1.413,54 | €44,93 | €-0,28 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2421,39727 | €964,53 | €1.929,06 | €46,89 | €0,71 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,51586 | €937,26 | €1.874,52 | €46,88 | €-23,30 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 91,52201 | €12,51 | €25,03 | €0,54 | €-0,16 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 619,16975 | €730,27 | €1.460,53 | €46,42 | €-0,29 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,10808 | 1,10786 | 1,08231 | 0,55958 | 1,18540 | €965,82 | €1.931,64 | €44,93 | €-0,39 |
| Top 5 + BTC — target pieno 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2421,39727 | €965,10 | €1.930,19 | €46,92 | €0,71 |
| Top 5 + BTC — target pieno 3R | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,51586 | €937,81 | €1.875,62 | €46,91 | €-23,31 |
| Top 5 + BTC — target pieno 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 91,52201 | €12,52 | €25,04 | €0,54 | €-0,16 |
| Top 5 + BTC — target pieno 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 619,16975 | €730,69 | €1.461,39 | €46,45 | €-0,29 |
| Top 5 + BTC — target pieno 3R | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,10808 | 1,10786 | 1,08231 | 0,55958 | 1,18540 | €966,39 | €1.932,77 | €44,95 | €-0,39 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €29,12 | €58,23 | €0,96 | €-0,00 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2377,51300 | €956,00 | €1.911,99 | €46,47 | €0,70 |
| Combo Scanner | LINK | LONG | Combo Scanner | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,30153 | €928,96 | €1.857,93 | €46,47 | €-23,09 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 86,00620 | 85,45600 | 84,16759 | 43,43313 | 90,05113 | €1.085,91 | €2.171,82 | €46,43 | €-13,89 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 565,27303 | 565,16000 | 547,30746 | 285,46288 | 604,79730 | €712,03 | €1.424,06 | €45,26 | €-0,28 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2366,54194 | €1.019,03 | €2.038,05 | €49,54 | €0,75 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €657,43 | €1.314,85 | €49,53 | €-24,57 |
| Combo Adaptive — madre | SOL | LONG | Combo Adaptive | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.386,65 | €2.773,30 | €0,00 | €14,09 |
| Combo Adaptive — madre | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71314 | 10,57900 | 10,42552 | 5,41014 | 11,28838 | €44,00 | €88,00 | €2,36 | €-1,10 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive — Trend/Transition | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,65421 | 0,65421 | 0,66363 | 0,97804 | 0,63537 | €1.699,46 | €3.398,92 | €48,94 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive — Long Only | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2366,54194 | €1.013,64 | €2.027,27 | €49,28 | €0,74 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €653,95 | €1.307,90 | €49,27 | €-24,44 |
| Combo Adaptive — Long Only | SOL | LONG | Combo Adaptive | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.379,32 | €2.758,63 | €0,00 | €14,02 |
| Combo Adaptive — Long Only | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71314 | 10,57900 | 10,42552 | 5,41014 | 11,28838 | €920,99 | €1.841,98 | €49,45 | €-23,06 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2366,54194 | €978,51 | €1.957,03 | €47,57 | €0,72 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €631,29 | €1.262,58 | €47,56 | €-23,60 |
| Combo Adaptive — parziale 1R | SOL | LONG | Combo Adaptive | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.331,52 | €2.663,05 | €0,00 | €13,53 |
| Combo Adaptive — parziale 1R | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71314 | 10,57900 | 10,42552 | 5,41014 | 11,28838 | €42,25 | €84,51 | €2,27 | €-1,06 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 85,02400 | 85,45600 | 85,02400 | 57,10779 | 88,06063 | €919,56 | €2.758,69 | €0,00 | €14,02 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 85,47309 | 85,45600 | 82,51462 | 43,16391 | 92,86927 | €715,87 | €1.431,74 | €49,56 | €-0,29 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 85,02400 | 85,45600 | 85,02400 | 57,10779 | 87,72323 | €1.046,71 | €3.140,14 | €0,00 | €15,95 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 85,47309 | 85,45600 | 82,51462 | 43,16391 | 93,75681 | €727,07 | €1.454,13 | €50,33 | €-0,29 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 85,43891 | 85,45600 | 88,12735 | 127,73117 | 80,59971 | €797,18 | €1.594,36 | €50,17 | €-0,32 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 85,02400 | 85,45600 | 85,02400 | 57,10779 | 88,06063 | €906,48 | €2.719,45 | €0,00 | €13,82 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 85,47309 | 85,45600 | 82,24567 | 43,16391 | 93,54165 | €665,34 | €1.330,67 | €50,25 | €-0,27 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2265,72305 | 2257,66000 | 2200,51783 | 1521,81065 | 2396,13352 | €563,60 | €1.690,79 | €48,66 | €-6,02 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2258,11153 | 2257,66000 | 2161,85309 | 1140,34632 | 2498,75762 | €577,20 | €1.154,41 | €49,21 | €-0,23 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2256,83128 | 2257,66000 | 2208,07099 | 1515,83834 | 2354,35187 | €760,21 | €2.280,63 | €49,27 | €0,84 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2264,81695 | 2257,66000 | 2319,13290 | 3008,43184 | 2183,34301 | €679,82 | €2.039,45 | €48,91 | €6,44 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1515,83834 | 2366,54194 | €670,92 | €2.012,75 | €48,92 | €0,74 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2256,83128 | 2257,66000 | 2201,97595 | 1139,69979 | 2366,54194 | €1.016,16 | €2.032,33 | €49,40 | €0,75 |
| Combo Adaptive — Side × Regime Guard | LINK | LONG | Combo Adaptive | 60m | 2,0x | 10,71214 | 10,57900 | 10,44424 | 5,40963 | 11,24795 | €987,43 | €1.974,86 | €49,39 | €-24,55 |
| Combo Adaptive — Side × Regime Guard | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 70,90318 | 69,57800 | 68,23231 | 35,80610 | 76,24492 | €655,47 | €1.310,95 | €49,38 | €-24,50 |
| Combo Adaptive — Side × Regime Guard | SOL | LONG | Combo Adaptive | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,06063 | €1.381,43 | €2.762,85 | €0,00 | €14,04 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 572,55449 | 565,16000 | 555,45616 | 289,14002 | 606,75113 | €12,82 | €25,65 | €0,77 | €-0,33 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Combo Trend — Side × Regime Guard | HYPE | LONG | Combo Trend | 60m | 2,0x | 70,90318 | 69,57800 | 67,93555 | 35,80610 | 77,43197 | €617,91 | €1.235,82 | €51,72 | €-23,10 |
| Combo Trend — Side × Regime Guard | SOL | LONG | Combo Trend | 60m | 2,0x | 85,02400 | 85,45600 | 85,02400 | 42,93712 | 88,73544 | €1.303,32 | €2.606,64 | €0,00 | €13,24 |
| Combo Trend — Side × Regime Guard | ZEC | LONG | Combo Trend | 60m | 2,0x | 568,28363 | 565,16000 | 550,82984 | 286,98324 | 606,68197 | €841,81 | €1.683,63 | €51,71 | €-9,25 |
| Combo Trend — Side × Regime Guard | ETH | LONG | Combo Trend | 60m | 2,0x | 2265,72305 | 2257,66000 | 2193,27280 | 1144,19014 | 2425,11361 | €812,72 | €1.625,45 | €51,98 | €-5,78 |
| Combo Trend — Side × Regime Guard | LINK | LONG | Combo Trend | 60m | 2,0x | 10,71314 | 10,57900 | 10,39356 | 5,41014 | 11,41622 | €12,55 | €25,10 | €0,75 | €-0,31 |
| FAST NoHigh <7,5 · SHORT only | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| Bilanciata V3 · LONG only | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 70,90318 | 69,57800 | 68,23231 | 47,62330 | 76,24492 | €416,31 | €1.248,92 | €47,05 | €-23,34 |
| Bilanciata V3 · LONG only | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 572,55449 | 565,16000 | 555,45616 | 384,56576 | 606,75113 | €528,93 | €1.586,80 | €47,39 | €-20,49 |
| Bilanciata V3 · LONG only | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 10,71314 | 10,57900 | 10,42552 | 7,19566 | 11,28838 | €14,74 | €44,23 | €1,19 | €-0,55 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2257,66000 | 2181,35381 | 1510,45050 | 2383,72136 | €502,31 | €1.506,93 | €45,20 | €5,93 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.639,87 | €3.279,73 | €48,65 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1592,75000 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-19,48 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.642,36 | €3.284,73 | €48,72 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1592,75000 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-19,51 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive — Quality7 + Regime + parziale 1R | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,92 | -0,04 | STOP |
| Combo Adaptive — Quality7 + Regime | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,89 | -0,04 | STOP |
| Combo Adaptive — Trend/Transition | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-0,05 | -0,04 | STOP |
| Combo Scanner | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,81 | -0,04 | STOP |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,83 | -0,04 | STOP |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,83 | -0,04 | STOP |
| Top 5 + BTC — Guard + MFE | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,81 | -0,04 | STOP |
| Top 5 + BTC — Guard | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,85 | -0,04 | STOP |
| Top 5 + BTC — solo MFE | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,77 | -0,04 | STOP |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-1,89 | -0,04 | STOP |
| Rapida V1 — target pieno 2R | HYPE | LONG | 2026-08-20T00:05:51+00:00 | 69,45400 | €-0,05 | -0,05 | STOP |
| Scanner Top 5 Long 1H | XRP | LONG | 2026-08-19T23:06:21+00:00 | 1,10232 | €3,62 | 0,07 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 423/30 | 33/30 | 0,70 | 2,04 | -0,16R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 390/30 | 20/30 | 0,64 | 1,90 | -0,19R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 222/30 | 22/30 | 0,81 | 1,74 | -0,10R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 225/30 | 22/30 | 0,78 | 1,57 | -0,11R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 332/30 | 31/30 | 0,81 | 0,62 | -0,09R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 301/30 | 11/30 | 0,75 | 0,00 | -0,13R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 130/30 | 8/30 | 0,75 | 1,02 | -0,13R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 285/30 | 17/30 | 0,62 | 4,50 | -0,21R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 447/30 | 24/30 | 0,70 | 0,64 | -0,16R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 409/30 | 7/30 | 0,60 | 0,02 | -0,21R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 332/30 | 30/30 | 0,85 | 1,02 | -0,08R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 593/30 | 55/30 | 0,82 | 1,12 | -0,08R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 125/30 | 15/30 | 0,49 | 0,99 | -0,33R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 531/30 | 44/30 | 0,70 | 1,20 | -0,16R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 535/30 | 37/30 | 0,70 | 0,76 | -0,16R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 493/30 | 23/30 | 0,62 | 1,12 | -0,20R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 294/30 | 46/30 | 0,73 | 0,76 | -0,16R | €-7,25 | 6,39% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 12/30 | 0,00 | 1,74 | 0,00R | €17,78 | 1,54% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 29/30 | 0,00 | 1,77 | 0,00R | €16,47 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 701/30 | 120/30 | 0,85 | 0,69 | -0,08R | €-7,07 | 13,99% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 59/30 | 0,00 | 0,67 | 0,00R | €-10,14 | 9,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 238/30 | 71/30 | 1,03 | 0,72 | 0,02R | €-6,89 | 8,50% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 440/30 | 114/30 | 0,90 | 0,98 | -0,05R | €-0,42 | 9,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 361/30 | 70/30 | 0,80 | 0,65 | -0,11R | €-8,39 | 8,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 189/30 | 40/30 | 0,92 | 1,13 | -0,04R | €3,16 | 3,73% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 461/30 | 85/30 | 0,82 | 0,88 | -0,09R | €-2,59 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 528/30 | 121/30 | 0,86 | 1,01 | -0,07R | €0,24 | 7,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 737/30 | 135/30 | 0,76 | 1,02 | -0,13R | €0,45 | 4,46% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 83/30 | 0,00 | 1,28 | 0,00R | €6,51 | 4,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 88/30 | 0,00 | 0,78 | 0,00R | €-6,98 | 9,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 36/30 | 0,00 | 1,14 | 0,00R | €4,21 | 3,33% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 426/30 | 130/30 | 0,78 | 0,90 | -0,11R | €-2,79 | 9,66% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 698/30 | 153/30 | 0,73 | 0,96 | -0,15R | €-0,78 | 6,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 52/30 | 30/30 | 0,67 | 1,05 | -0,19R | €1,22 | 3,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 695/30 | 158/30 | 0,78 | 0,83 | -0,11R | €-3,73 | 8,93% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 510/30 | 126/30 | 0,77 | 0,80 | -0,12R | €-5,12 | 11,75% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 263/30 | 82/30 | 0,93 | 0,76 | -0,04R | €-7,41 | 7,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 267/30 | 77/30 | 0,90 | 0,78 | -0,05R | €-6,25 | 6,59% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 395/30 | 95/30 | 0,86 | 0,59 | -0,07R | €-11,28 | 11,62% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 41/30 | 0,00 | 1,25 | 0,00R | €6,05 | 3,97% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 63/30 | 0,00 | 1,10 | 0,00R | €2,24 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 557/30 | 110/30 | 0,77 | 0,80 | -0,12R | €-5,12 | 6,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 75/30 | 0,00 | 0,69 | 0,00R | €-8,30 | 9,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 114/30 | 0,00 | 0,77 | 0,00R | €-4,62 | 8,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 41/30 | 0,00 | 1,01 | 0,00R | €0,34 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 648/30 | 130/30 | 0,74 | 0,73 | -0,14R | €-6,02 | 8,44% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 283/30 | 44/30 | 0,75 | 1,06 | -0,16R | €1,55 | 4,45% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 205/30 | 80/30 | 1,17 | 0,55 | 0,07R | €-15,73 | 14,60% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 12/30 | 6/30 | 0,91 | 1,77 | -0,04R | €13,88 | 1,13% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 2/30 | 2/30 | 2,26 | 2,39 | 0,67R | €35,09 | 0,96% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 2/30 | 2/30 | 1,56 | 1,54 | 0,31R | €14,72 | 0,82% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 15/30 | 8/30 | 0,38 | 1,41 | -0,46R | €8,50 | 1,49% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 6/30 | 4/30 | 0,50 | 0,80 | -0,45R | €-8,55 | 2,43% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 16/30 | 10/30 | 0,99 | 0,82 | -0,01R | €-5,78 | 1,94% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 4/30 | 3/30 | 0,75 | 1,19 | -0,20R | €6,47 | 1,76% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 570/30 | 96/30 | 0,95 | 0,95 | -0,03R | €-0,96 | 7,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 323/30 | 66/30 | 0,97 | 0,91 | -0,02R | €-2,20 | 6,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 614/30 | 103/30 | 0,96 | 0,42 | -0,02R | €-14,38 | 15,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 511/30 | 97/30 | 0,90 | 0,77 | -0,05R | €-5,01 | 8,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 66/30 | 25/30 | 1,34 | 0,64 | 0,15R | €-10,88 | 4,21% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 66/30 | 25/30 | 1,27 | 0,49 | 0,11R | €-15,78 | 5,41% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 161/30 | 50/30 | 0,85 | 0,55 | -0,07R | €-14,22 | 8,87% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 205/30 | 37/30 | 0,88 | 1,00 | -0,06R | €-0,01 | 3,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 94/30 | 0,74 | 0,53 | -0,20R | €-11,02 | 12,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 69/30 | 0,00 | 0,92 | 0,00R | €-1,74 | 8,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 75/30 | 0,74 | 0,38 | -0,20R | €-16,04 | 12,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 92/30 | 37/30 | 1,24 | 0,48 | 0,11R | €-23,92 | 10,64% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 353/30 | 85/30 | 1,05 | 0,70 | 0,03R | €-8,57 | 11,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 478/30 | 122/30 | 0,90 | 0,74 | -0,06R | €-6,98 | 10,47% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 60/30 | 0,00 | 1,29 | 0,00R | €5,94 | 4,33% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 12/30 | 10/30 | 0,51 | 0,62 | -0,36R | €-10,55 | 2,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 18/30 | 13/30 | 0,40 | 0,97 | -0,41R | €-0,67 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 235/30 | 74/30 | 0,85 | 1,49 | -0,09R | €11,52 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 165/30 | 42/30 | 0,84 | 1,69 | -0,09R | €14,21 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 480/30 | 91/30 | 0,88 | 0,49 | -0,07R | €-12,27 | 11,93% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 17/30 | 9/30 | 0,39 | 0,34 | -0,47R | €-23,94 | 3,14% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 10/30 | 4/30 | 2,20 | 0,07 | 0,41R | €-54,45 | 2,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 16/30 | 8/30 | 0,37 | 0,56 | -0,53R | €-18,14 | 2,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 24/30 | 13/30 | 0,34 | 0,47 | -0,52R | €-20,63 | 4,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 13/30 | 16/30 | 0,78 | 0,32 | -0,15R | €-23,25 | 3,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 273/30 | 61/30 | 1,04 | 0,66 | 0,02R | €-11,15 | 7,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 55/30 | 0,00 | 0,62 | 0,00R | €-11,41 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 42/30 | 0,00 | 0,53 | 0,00R | €-17,80 | 11,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 50/30 | 0,00 | 0,60 | 0,00R | €-12,75 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 504/30 | 87/30 | 1,43 | 0,60 | 0,14R | €-9,17 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 241/30 | 58/30 | 1,06 | 0,67 | 0,03R | €-11,13 | 7,26% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 250/30 | 50/30 | 1,02 | 0,65 | 0,01R | €-12,47 | 8,18% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 172/30 | 52/30 | 1,02 | 0,59 | 0,01R | €-18,12 | 11,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 263/30 | 52/30 | 1,00 | 0,62 | 0,00R | €-12,96 | 7,80% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 587/30 | 104/30 | 0,83 | 0,54 | -0,10R | €-11,52 | 13,92% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 230/30 | 81/30 | 1,12 | 0,77 | 0,06R | €-7,85 | 10,56% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 206/30 | 66/30 | 0,47 | 0,85 | -0,31R | €-3,42 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 206/30 | 66/30 | 0,47 | 0,85 | -0,31R | €-3,42 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 206/30 | 66/30 | 0,47 | 0,85 | -0,31R | €-3,42 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 239/30 | 85/30 | 0,64 | 0,79 | -0,20R | €-4,51 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 244/30 | 57/30 | 0,73 | 0,78 | -0,13R | €-5,15 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 221/30 | 58/30 | 0,62 | 0,76 | -0,17R | €-5,32 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 304/30 | 66/30 | 0,94 | 0,73 | -0,03R | €-7,05 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 305/30 | 66/30 | 0,94 | 0,73 | -0,03R | €-7,05 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 305/30 | 66/30 | 0,94 | 0,73 | -0,03R | €-7,05 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 340/30 | 81/30 | 1,07 | 0,84 | 0,04R | €-4,16 | 11,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 128/30 | 13/30 | 0,83 | 0,41 | -0,10R | €-22,20 | 4,35% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 286/30 | 59/30 | 0,94 | 0,57 | -0,03R | €-12,93 | 11,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 302/30 | 73/30 | 1,18 | 0,73 | 0,07R | €-7,80 | 7,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 252/30 | 58/30 | 1,05 | 0,78 | 0,02R | €-6,97 | 7,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 322/30 | 81/30 | 1,14 | 0,67 | 0,06R | €-9,17 | 8,78% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 267/30 | 64/30 | 1,03 | 0,73 | 0,01R | €-8,17 | 7,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 364/30 | 73/30 | 1,05 | 0,50 | 0,02R | €-12,89 | 12,28% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 289/30 | 69/30 | 0,97 | 0,64 | -0,02R | €-10,02 | 12,06% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 275/30 | 65/30 | 0,96 | 0,64 | -0,02R | €-10,55 | 11,78% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 376/30 | 93/30 | 1,07 | 1,21 | 0,04R | €4,98 | 8,85% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 24/30 | 11/30 | 0,41 | 0,36 | -0,49R | €-26,14 | 4,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 5/30 | 4/30 | 1,15 | 1,47 | 0,10R | €12,27 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 15/30 | 8/30 | 1,04 | 0,66 | 0,02R | €-13,38 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 3/30 | 2/30 | ∞ | 1,63 | 1,38R | €16,84 | 0,72% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 18/30 | 9/30 | 0,60 | 0,87 | -0,30R | €-3,46 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 5/30 | 4/30 | 1,27 | 1,63 | 0,18R | €16,58 | 1,05% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 22/30 | 10/30 | 0,55 | 0,61 | -0,36R | €-14,74 | 3,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 6/30 | 5/30 | 0,46 | 0,57 | -0,48R | €-17,74 | 2,27% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.0751**
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
| BTC sotto filtro | 69514.5 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07511**; close **0.075**; wick alta **0.0%**; volume **x0.26**

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
- Confidenza: **90,00%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +3.56%, 64% oltre +1%.
- BTC trend score: **4,00**; ADX: **33,74**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **3,56%**; dispersione: **7,61%**

- Aperti in questo ciclo: **38**
- Chiusi in questo ciclo: **13**
- Posizioni research aperte: **477**
- Trade research chiusi: **27706**
- Eventi di mercato indipendenti chiusi: **3772**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **69340**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 6 | 423 | 423 | 30,02% | 0,70 | -0,16R | €-663,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 6 | 390 | 390 | 29,23% | 0,64 | -0,19R | €-747,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 1 | 222 | 222 | 45,95% | 0,81 | -0,10R | €-226,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 1 | 225 | 225 | 32,89% | 0,78 | -0,11R | €-253,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 4 | 332 | 332 | 32,53% | 0,81 | -0,09R | €-314,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 4 | 301 | 301 | 32,23% | 0,75 | -0,13R | €-379,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 130 | 130 | 35,38% | 0,75 | -0,13R | €-164,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 0 | 285 | 285 | 27,72% | 0,62 | -0,21R | €-607,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 3 | 447 | 447 | 29,75% | 0,70 | -0,16R | €-710,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 3 | 409 | 409 | 28,61% | 0,60 | -0,21R | €-855,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 4 | 332 | 332 | 33,13% | 0,85 | -0,08R | €-254,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 7 | 593 | 593 | 39,46% | 0,82 | -0,08R | €-492,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 0 | 125 | 125 | 30,40% | 0,49 | -0,33R | €-417,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 7 | 531 | 531 | 29,38% | 0,70 | -0,16R | €-840,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 7 | 535 | 535 | 29,35% | 0,70 | -0,16R | €-840,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 7 | 493 | 493 | 28,19% | 0,62 | -0,20R | €-986,96 |
| MAIN | 13 | 294 | 294 | 26,19% | 0,73 | -0,16R | €-472,89 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 1 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 13 | 701 | 701 | 32,95% | 0,85 | -0,08R | €-569,39 |
| Bilanciata 1H V2 | 4 | 272 | 238 | 36,76% | 1,03 | 0,02R | €44,50 |
| Bilanciata 1H V3 Filtered | 9 | 440 | 440 | 34,32% | 0,90 | -0,05R | €-234,57 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 9 | 361 | 361 | 33,24% | 0,80 | -0,11R | €-379,92 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 189 | 189 | 38,10% | 0,92 | -0,04R | €-70,27 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 2 | 461 | 461 | 34,92% | 0,82 | -0,09R | €-419,02 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 2 | 528 | 528 | 35,98% | 0,86 | -0,07R | €-384,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 10 | 737 | 737 | 33,65% | 0,76 | -0,13R | €-922,39 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 426 | 426 | 34,27% | 0,78 | -0,11R | €-484,24 |
| SHADOW_1H_FAST_TP2_V1 | 10 | 698 | 698 | 30,66% | 0,73 | -0,15R | €-1026,13 |
| Rapida 1H V2 | 0 | 61 | 52 | 39,34% | 0,67 | -0,19R | €-113,28 |
| Rapida 1H V3 Filtered | 7 | 695 | 695 | 34,24% | 0,78 | -0,11R | €-796,89 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 5 | 510 | 510 | 34,31% | 0,77 | -0,12R | €-605,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 1 | 263 | 263 | 47,53% | 0,93 | -0,04R | €-100,07 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 1 | 267 | 267 | 37,45% | 0,90 | -0,05R | €-135,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 395 | 395 | 36,71% | 0,86 | -0,07R | €-278,96 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 3 | 557 | 557 | 33,75% | 0,77 | -0,12R | €-684,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 7 | 648 | 648 | 33,33% | 0,74 | -0,14R | €-878,84 |
| SHADOW_4H_WIDE | 23 | 283 | 283 | 20,85% | 0,75 | -0,16R | €-464,46 |
| SHADOW_BOLLINGER_MR_1H | 6 | 205 | 205 | 48,29% | 1,17 | 0,07R | €152,86 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 12 | 12 | 58,33% | 0,91 | -0,04R | €-4,88 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 2 | 2 | 50,00% | 2,26 | 0,67R | €13,50 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 15 | 15 | 33,33% | 0,38 | -0,46R | €-69,25 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 6 | 6 | 16,67% | 0,50 | -0,45R | €-26,75 |
| SHADOW_BTC_EMA_1H | 0 | 16 | 16 | 50,00% | 0,99 | -0,01R | €-0,90 |
| SHADOW_BTC_EMA_4H | 0 | 4 | 4 | 25,00% | 0,75 | -0,20R | €-8,17 |
| SHADOW_COMBO_ADAPTIVE | 12 | 570 | 570 | 36,49% | 0,95 | -0,03R | €-162,97 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 8 | 323 | 323 | 36,53% | 0,97 | -0,02R | €-53,91 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 11 | 614 | 614 | 40,23% | 0,96 | -0,02R | €-119,98 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 12 | 511 | 511 | 38,94% | 0,90 | -0,05R | €-269,66 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 66 | 66 | 46,97% | 1,34 | 0,15R | €96,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 66 | 66 | 39,39% | 1,27 | 0,11R | €75,56 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 3 | 161 | 161 | 31,68% | 0,85 | -0,07R | €-116,66 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 205 | 205 | 35,61% | 0,88 | -0,06R | €-126,28 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 92 | 92 | 50,00% | 1,24 | 0,11R | €98,52 |
| SHADOW_COMBO_SCANNER | 9 | 353 | 353 | 35,13% | 1,05 | 0,03R | €91,34 |
| SHADOW_COMBO_TREND | 12 | 478 | 478 | 31,59% | 0,90 | -0,06R | €-264,32 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 12 | 12 | 33,33% | 0,51 | -0,36R | €-43,62 |
| SHADOW_DOGE_EMA_1H | 0 | 18 | 18 | 27,78% | 0,40 | -0,41R | €-73,66 |
| SHADOW_DONCHIAN_1H | 6 | 235 | 235 | 29,79% | 0,85 | -0,09R | €-219,94 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 6 | 165 | 165 | 31,52% | 0,84 | -0,09R | €-154,85 |
| SHADOW_EMA_TREND_1H | 12 | 480 | 480 | 31,25% | 0,88 | -0,07R | €-325,78 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 17 | 17 | 29,41% | 0,39 | -0,47R | €-80,53 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 10 | 10 | 70,00% | 2,20 | 0,41R | €40,93 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 16 | 16 | 25,00% | 0,37 | -0,53R | €-84,32 |
| SHADOW_ETH_EMA_1H | 1 | 24 | 24 | 29,17% | 0,34 | -0,52R | €-123,92 |
| SHADOW_ETH_EMA_4H | 1 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 0 | 13 | 13 | 38,46% | 0,78 | -0,15R | €-19,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 4 | 273 | 273 | 33,33% | 1,04 | 0,02R | €61,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 3 | 504 | 504 | 66,87% | 1,43 | 0,14R | €691,75 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 4 | 241 | 241 | 33,61% | 1,06 | 0,03R | €83,96 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 4 | 250 | 250 | 31,60% | 1,02 | 0,01R | €31,75 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 3 | 172 | 172 | 33,14% | 1,02 | 0,01R | €19,85 |
| SHADOW_MASTER_ADAPTIVE_V1 | 4 | 263 | 263 | 32,70% | 1,00 | 0,00R | €6,46 |
| Forza relativa 1H V1 | 18 | 587 | 587 | 28,79% | 0,83 | -0,10R | €-578,19 |
| Forza relativa 1H V2 | 7 | 246 | 230 | 34,96% | 1,12 | 0,06R | €151,65 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 6 | 206 | 206 | 25,73% | 0,47 | -0,31R | €-640,06 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 6 | 206 | 206 | 25,73% | 0,47 | -0,31R | €-640,06 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 6 | 206 | 206 | 25,73% | 0,47 | -0,31R | €-640,06 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 6 | 239 | 239 | 28,45% | 0,64 | -0,20R | €-477,56 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 5 | 244 | 244 | 51,64% | 0,73 | -0,13R | €-305,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 5 | 221 | 221 | 50,68% | 0,62 | -0,17R | €-382,19 |
| SHADOW_SCANNER_TOP10_LONG | 7 | 304 | 304 | 34,54% | 0,94 | -0,03R | €-84,81 |
| SHADOW_SCANNER_TOP15_LONG | 7 | 305 | 305 | 34,43% | 0,94 | -0,03R | €-95,92 |
| SHADOW_SCANNER_TOP20_LONG | 7 | 305 | 305 | 34,43% | 0,94 | -0,03R | €-95,92 |
| SHADOW_SCANNER_TOP5_BTC | 9 | 340 | 340 | 34,71% | 1,07 | 0,04R | €123,48 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 128 | 128 | 30,47% | 0,83 | -0,10R | €-122,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 3 | 286 | 286 | 33,57% | 0,94 | -0,03R | €-85,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 3 | 302 | 302 | 45,03% | 1,18 | 0,07R | €222,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 3 | 252 | 252 | 35,71% | 1,05 | 0,02R | €59,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 9 | 322 | 322 | 44,41% | 1,14 | 0,06R | €198,35 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 9 | 267 | 267 | 34,83% | 1,03 | 0,01R | €37,39 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 9 | 364 | 364 | 43,13% | 1,05 | 0,02R | €83,42 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 9 | 289 | 289 | 32,53% | 0,97 | -0,02R | €-49,48 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 9 | 275 | 275 | 31,64% | 0,96 | -0,02R | €-65,28 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 376 | 376 | 35,90% | 1,07 | 0,04R | €142,60 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 24 | 24 | 25,00% | 0,41 | -0,49R | €-117,02 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 5 | 5 | 40,00% | 1,15 | 0,10R | €4,88 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 15 | 15 | 53,33% | 1,04 | 0,02R | €3,50 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 3 | 3 | 100,00% | ∞ | 1,38R | €41,37 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 18 | 18 | 33,33% | 0,60 | -0,30R | €-53,85 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 5 | 5 | 40,00% | 1,27 | 0,18R | €8,78 |
| SHADOW_SOL_EMA_1H | 1 | 22 | 22 | 27,27% | 0,55 | -0,36R | €-79,72 |
| SHADOW_SOL_EMA_4H | 1 | 6 | 6 | 16,67% | 0,46 | -0,48R | €-28,86 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 1 | 44 | 44 | 25,00% | 0,55 | -0,28R | €-121,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 3 | 59 | 59 | 37,29% | 1,04 | 0,02R | €11,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 117 | 117 | 34,19% | 0,63 | -0,19R | €-227,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,71 | -0,15R | €-28,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 1 | 54 | 54 | 33,33% | 1,02 | 0,01R | €3,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 53 | 53 | 16,98% | 0,45 | -0,28R | €-147,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 31,25% | 1,14 | 0,06R | €9,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 1 | 42 | 42 | 23,81% | 0,38 | -0,43R | €-179,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 3 | 46 | 46 | 36,96% | 1,07 | 0,03R | €15,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 1 | 110 | 110 | 33,64% | 0,54 | -0,25R | €-269,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,69 | -0,17R | €-30,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 1 | 53 | 53 | 33,96% | 1,11 | 0,05R | €26,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 50 | 50 | 16,00% | 0,30 | -0,38R | €-188,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,44 | 0,20R | €29,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 8 | 8 | 50,00% | 1,03 | 0,02R | €1,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 68 | 68 | 39,71% | 0,51 | -0,31R | €-208,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 1 | 32 | 32 | 56,25% | 1,17 | 0,07R | €23,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 42,86% | 1,32 | 0,14R | €10,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 71 | 71 | 33,80% | 0,50 | -0,28R | €-201,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 1 | 32 | 32 | 31,25% | 0,96 | -0,02R | €-5,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 28,57% | 0,64 | -0,19R | €-27,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 3 | 58 | 58 | 32,76% | 0,80 | -0,11R | €-66,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 88 | 88 | 35,23% | 0,68 | -0,17R | €-151,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 1 | 43 | 43 | 34,88% | 1,24 | 0,09R | €39,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,13 | 0,06R | €9,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 28,57% | 0,57 | -0,23R | €-32,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 3 | 50 | 50 | 32,00% | 0,79 | -0,12R | €-60,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 77 | 77 | 36,36% | 0,59 | -0,21R | €-159,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 1 | 42 | 42 | 35,71% | 1,33 | 0,12R | €52,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,43 | 0,19R | €29,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 128 | 128 | 35,16% | 0,73 | -0,14R | €-174,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,73 | -0,16R | €-83,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 112 | 112 | 33,93% | 0,71 | -0,15R | €-168,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 33 | 33 | 24,24% | 0,76 | -0,11R | €-37,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 1 | 34 | 34 | 20,59% | 0,33 | -0,45R | €-154,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 147 | 147 | 33,33% | 0,66 | -0,19R | €-272,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 1 | 51 | 51 | 27,45% | 0,85 | -0,07R | €-33,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 72 | 72 | 23,61% | 0,63 | -0,18R | €-129,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 1 | 33 | 33 | 21,21% | 0,26 | -0,51R | €-168,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 137 | 137 | 32,12% | 0,57 | -0,23R | €-312,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 1 | 50 | 50 | 28,00% | 0,83 | -0,07R | €-35,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 67 | 67 | 22,39% | 0,45 | -0,28R | €-187,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 28,57% | 0,64 | -0,19R | €-27,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 3 | 59 | 59 | 33,90% | 0,86 | -0,08R | €-47,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 88 | 88 | 37,50% | 0,80 | -0,10R | €-91,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 1 | 43 | 43 | 34,88% | 1,24 | 0,09R | €39,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,13 | 0,06R | €9,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 1 | 65 | 65 | 36,92% | 0,55 | -0,25R | €-165,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 3 | 76 | 76 | 40,79% | 0,86 | -0,08R | €-57,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 163 | 163 | 38,04% | 0,83 | -0,08R | €-124,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 31 | 31 | 35,48% | 0,58 | -0,24R | €-73,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 1 | 67 | 67 | 47,76% | 1,43 | 0,14R | €91,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 82 | 82 | 40,24% | 0,82 | -0,08R | €-67,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 41,18% | 1,11 | 0,05R | €8,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,17 | -0,75R | €-119,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 50 | 50 | 40,00% | 0,55 | -0,26R | €-128,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 5 | 5 | 60,00% | 1,39 | 0,17R | €8,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 1 | 59 | 59 | 22,03% | 0,40 | -0,36R | €-212,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 3 | 67 | 67 | 31,34% | 0,81 | -0,10R | €-70,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 1 | 143 | 143 | 32,87% | 0,64 | -0,19R | €-277,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 31 | 31 | 29,03% | 0,59 | -0,23R | €-70,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 1 | 61 | 61 | 34,43% | 1,28 | 0,11R | €68,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 71 | 71 | 22,54% | 0,58 | -0,21R | €-149,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,99 | -0,01R | €-1,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 1 | 59 | 59 | 22,03% | 0,40 | -0,36R | €-212,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 3 | 69 | 69 | 31,88% | 0,84 | -0,09R | €-60,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 1 | 144 | 144 | 32,64% | 0,63 | -0,20R | €-287,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 31 | 31 | 29,03% | 0,59 | -0,23R | €-70,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 1 | 61 | 61 | 34,43% | 1,28 | 0,11R | €68,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 71 | 71 | 22,54% | 0,58 | -0,21R | €-149,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,98 | -0,01R | €-1,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 1 | 58 | 58 | 22,41% | 0,34 | -0,42R | €-241,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 3 | 57 | 57 | 31,58% | 0,84 | -0,09R | €-53,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 1 | 135 | 135 | 31,11% | 0,50 | -0,27R | €-362,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 27 | 27 | 25,93% | 0,63 | -0,21R | €-55,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 1 | 60 | 60 | 35,00% | 1,36 | 0,14R | €83,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 66 | 66 | 21,21% | 0,38 | -0,32R | €-211,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 29,41% | 1,24 | 0,11R | €18,87 |
| MAIN | ALT_ROTATION_DOWN | 2 | 24 | 24 | 29,17% | 0,82 | -0,09R | €-22,13 |
| MAIN | ALT_ROTATION_UP | 5 | 41 | 41 | 17,07% | 0,31 | -0,48R | €-197,22 |
| MAIN | RANGE | 1 | 76 | 76 | 21,05% | 0,61 | -0,24R | €-185,76 |
| MAIN | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 2 | 37 | 37 | 27,03% | 0,70 | -0,19R | €-70,98 |
| MAIN | TREND_DOWN | 1 | 46 | 46 | 28,26% | 0,79 | -0,12R | €-57,38 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 1 | 38 | 38 | 31,58% | 1,05 | 0,03R | €11,82 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 50,00% | 1,55 | 0,28R | €28,41 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 1 | 13 | 13 | 46,15% | 0,85 | -0,07R | €-9,35 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 61 | 61 | 22,95% | 0,46 | -0,38R | €-231,33 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 6 | 93 | 93 | 32,26% | 0,79 | -0,12R | €-115,71 |
| Bilanciata 1H V1 | RANGE | 1 | 179 | 179 | 39,66% | 1,05 | 0,03R | €49,71 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 46 | 46 | 26,09% | 0,50 | -0,34R | €-156,31 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 1 | 96 | 96 | 37,50% | 1,19 | 0,10R | €92,29 |
| Bilanciata 1H V1 | TREND_DOWN | 1 | 86 | 86 | 30,23% | 0,70 | -0,16R | €-135,99 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 110 | 110 | 30,00% | 0,91 | -0,05R | €-50,84 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 26 | 26 | 26,92% | 0,83 | -0,10R | €-26,87 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 62 | 52 | 35,48% | 1,01 | 0,00R | €2,56 |
| Bilanciata 1H V2 | RANGE | 2 | 128 | 116 | 35,16% | 0,84 | -0,09R | €-116,73 |
| Bilanciata 1H V2 | TRANSITION | 1 | 82 | 70 | 40,24% | 1,41 | 0,19R | €158,67 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 49 | 49 | 30,61% | 0,58 | -0,27R | €-132,34 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 4 | 50 | 50 | 28,00% | 0,92 | -0,05R | €-22,83 |
| Bilanciata 1H V3 Filtered | RANGE | 2 | 122 | 122 | 40,98% | 1,09 | 0,04R | €52,16 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,56 | -0,28R | €-50,80 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 53 | 53 | 33,96% | 1,05 | 0,03R | €13,37 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 60 | 60 | 35,00% | 0,66 | -0,19R | €-114,14 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €7,90 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 31,82% | 0,97 | -0,02R | €-4,51 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 38 | 38 | 26,32% | 0,34 | -0,44R | €-165,71 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 48 | 48 | 29,17% | 0,99 | -0,00R | €-1,83 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 2 | 100 | 100 | 39,00% | 0,87 | -0,06R | €-64,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 31,25% | 0,69 | -0,19R | €-29,97 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 45 | 45 | 33,33% | 1,04 | 0,02R | €7,69 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 61 | 61 | 34,43% | 0,63 | -0,21R | €-125,26 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 42 | 42 | 23,81% | 0,74 | -0,13R | €-52,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 50,00% | 1,84 | 0,44R | €35,49 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 28,57% | 0,56 | -0,26R | €-36,53 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 48,84% | 1,27 | 0,11R | €46,79 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 51 | 51 | 41,18% | 0,97 | -0,01R | €-6,96 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,70 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 30,61% | 0,80 | -0,08R | €-38,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 26 | 26 | 26,92% | 0,50 | -0,29R | €-76,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 64 | 64 | 45,31% | 1,11 | 0,05R | €33,16 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 154 | 154 | 35,71% | 0,78 | -0,12R | €-177,39 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 59 | 59 | 38,98% | 1,12 | 0,05R | €27,90 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 75 | 75 | 28,00% | 0,76 | -0,11R | €-80,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 44 | 44 | 25,00% | 0,46 | -0,36R | €-158,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 184 | 184 | 39,67% | 0,97 | -0,02R | €-32,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 61 | 61 | 40,98% | 1,26 | 0,09R | €57,59 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 91 | 91 | 27,47% | 0,67 | -0,17R | €-153,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 88 | 88 | 25,00% | 0,46 | -0,36R | €-313,50 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 6 | 83 | 83 | 34,94% | 0,73 | -0,16R | €-134,85 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 212 | 212 | 37,26% | 0,83 | -0,09R | €-188,13 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 39 | 39 | 38,46% | 0,86 | -0,07R | €-29,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 85 | 85 | 41,18% | 1,33 | 0,12R | €105,09 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 105 | 105 | 27,62% | 0,69 | -0,16R | €-170,93 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 1 | 20 | 20 | 40,00% | 1,11 | 0,05R | €9,93 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 52 | 52 | 26,92% | 0,46 | -0,37R | €-191,88 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 57 | 57 | 33,33% | 0,74 | -0,15R | €-84,20 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 118 | 118 | 42,37% | 1,06 | 0,03R | €37,21 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 41,18% | 0,87 | -0,07R | €-11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 52 | 52 | 40,38% | 1,25 | 0,10R | €50,06 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 60 | 60 | 26,67% | 0,58 | -0,23R | €-137,91 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,31 | -0,38R | €-30,51 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 1 | 86 | 86 | 24,42% | 0,45 | -0,36R | €-305,47 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 6 | 85 | 85 | 36,47% | 0,85 | -0,08R | €-71,97 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 1 | 194 | 194 | 35,05% | 0,80 | -0,11R | €-206,68 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 38 | 38 | 28,95% | 0,64 | -0,20R | €-77,77 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,43 | 0,16R | €127,75 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 96 | 96 | 20,83% | 0,52 | -0,26R | €-247,93 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 1 | 22 | 22 | 27,27% | 0,73 | -0,14R | €-30,24 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 0 | 44 | 36 | 40,91% | 0,84 | -0,08R | €-36,12 |
| Rapida 1H V2 | TRANSITION | 0 | 7 | 7 | 57,14% | 0,81 | -0,07R | €-4,61 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 86 | 86 | 24,42% | 0,44 | -0,36R | €-309,86 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 3 | 76 | 76 | 35,53% | 0,79 | -0,12R | €-88,54 |
| Rapida 1H V3 Filtered | RANGE | 1 | 187 | 187 | 37,43% | 0,82 | -0,09R | €-176,17 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 33 | 33 | 39,39% | 0,87 | -0,07R | €-22,89 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 2 | 75 | 75 | 38,67% | 1,13 | 0,05R | €39,80 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 109 | 109 | 36,70% | 0,98 | -0,01R | €-9,47 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 30,56% | 0,67 | -0,19R | €-68,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 65 | 65 | 26,15% | 0,47 | -0,36R | €-232,05 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 66 | 66 | 37,88% | 0,87 | -0,07R | €-45,97 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 148 | 148 | 38,51% | 0,88 | -0,06R | €-87,89 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 22 | 22 | 40,91% | 0,94 | -0,03R | €-6,30 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 1 | 57 | 57 | 38,60% | 1,03 | 0,01R | €8,23 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 70 | 70 | 28,57% | 0,65 | -0,18R | €-127,20 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 35,71% | 0,99 | -0,00R | €-0,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,29 | -0,54R | €-81,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 83 | 83 | 43,37% | 0,86 | -0,08R | €-68,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 1 | 33 | 33 | 57,58% | 1,39 | 0,15R | €49,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,31 | -0,52R | €-72,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 86 | 86 | 40,70% | 0,94 | -0,03R | €-25,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 1 | 33 | 33 | 39,39% | 1,19 | 0,07R | €24,55 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 17,39% | 0,27 | -0,53R | €-122,83 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 67 | 67 | 34,33% | 0,73 | -0,16R | €-105,49 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 108 | 108 | 41,67% | 0,97 | -0,01R | €-15,59 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 48 | 48 | 41,67% | 1,24 | 0,10R | €45,62 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 42,86% | 1,25 | 0,10R | €14,27 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 1 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-230,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 189 | 189 | 38,62% | 0,87 | -0,07R | €-128,12 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 59 | 59 | 33,90% | 0,96 | -0,02R | €-9,17 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 95 | 95 | 31,58% | 0,77 | -0,12R | €-114,65 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 85 | 85 | 24,71% | 0,45 | -0,35R | €-298,43 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 75 | 75 | 33,33% | 0,70 | -0,17R | €-129,66 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 185 | 185 | 37,30% | 0,81 | -0,10R | €-190,91 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 32 | 32 | 40,62% | 0,92 | -0,04R | €-12,76 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 2 | 70 | 70 | 38,57% | 1,15 | 0,06R | €42,57 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 92 | 92 | 30,43% | 0,73 | -0,14R | €-132,21 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 37,50% | 1,06 | 0,03R | €4,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 3 | 21 | 21 | 33,33% | 1,86 | 0,38R | €80,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 8 | 35 | 35 | 25,71% | 0,58 | -0,32R | €-111,31 |
| SHADOW_4H_WIDE | RANGE | 4 | 71 | 71 | 15,49% | 0,62 | -0,26R | €-187,12 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 38 | 38 | 15,79% | 0,47 | -0,38R | €-145,68 |
| SHADOW_4H_WIDE | TREND_DOWN | 2 | 45 | 45 | 26,67% | 0,96 | -0,03R | €-11,28 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 39 | 39 | 23,08% | 0,99 | -0,01R | €-2,00 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 7,14% | 0,24 | -0,61R | €-85,99 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 5 | 28 | 28 | 50,00% | 1,49 | 0,19R | €53,76 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 69 | 69 | 44,93% | 0,98 | -0,01R | €-6,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 1 | 9 | 9 | 66,67% | 2,26 | 0,46R | €41,22 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 13 | 13 | 53,85% | 1,74 | 0,31R | €39,93 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,86 | -0,09R | €-9,15 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,96R | €19,19 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,42R | €24,17 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 1,70 | 0,26R | €7,84 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,52 | 0,82R | €16,32 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,41R | €24,09 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 2 | 52 | 52 | 26,92% | 0,62 | -0,23R | €-120,23 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 6 | 69 | 69 | 31,88% | 0,75 | -0,15R | €-103,65 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 149 | 149 | 42,28% | 1,00 | -0,00R | €-2,37 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 32 | 32 | 37,50% | 0,88 | -0,06R | €-19,15 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 73 | 73 | 41,10% | 1,42 | 0,19R | €140,22 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 73 | 73 | 35,62% | 0,90 | -0,05R | €-37,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 95 | 95 | 35,79% | 1,09 | 0,04R | €37,83 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 24,00% | 0,68 | -0,22R | €-55,89 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,59 | -0,24R | €-42,50 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 6 | 63 | 63 | 31,75% | 0,75 | -0,15R | €-96,64 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 75 | 75 | 49,33% | 1,31 | 0,14R | €108,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 39 | 39 | 46,15% | 2,07 | 0,34R | €133,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 43 | 43 | 37,21% | 1,13 | 0,06R | €26,23 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 1 | 65 | 65 | 32,31% | 0,65 | -0,18R | €-119,37 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 6 | 76 | 76 | 35,53% | 0,76 | -0,13R | €-98,63 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 148 | 148 | 41,89% | 1,16 | 0,07R | €105,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 38 | 38 | 42,11% | 0,80 | -0,09R | €-32,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 63 | 63 | 46,03% | 1,24 | 0,10R | €64,17 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 96 | 96 | 37,50% | 0,88 | -0,05R | €-45,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 97 | 97 | 49,48% | 1,29 | 0,12R | €117,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 24,14% | 0,44 | -0,38R | €-108,76 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 2 | 52 | 52 | 26,92% | 0,65 | -0,22R | €-112,94 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 6 | 67 | 67 | 32,84% | 0,76 | -0,14R | €-93,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 137 | 137 | 45,26% | 1,05 | 0,02R | €33,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 30 | 30 | 43,33% | 1,03 | 0,01R | €3,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 56 | 56 | 44,64% | 1,30 | 0,14R | €75,84 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 73 | 73 | 39,73% | 0,91 | -0,05R | €-33,53 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 74 | 74 | 36,49% | 0,71 | -0,13R | €-98,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 30,00% | 0,68 | -0,22R | €-44,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 34 | 34 | 38,24% | 0,96 | -0,02R | €-7,01 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 75,00% | 82,10 | 0,91R | €36,53 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 34 | 34 | 38,24% | 0,95 | -0,03R | €-9,65 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 66,90 | 0,96R | €38,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,04 | -0,63R | €-81,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 1 | 19 | 19 | 26,32% | 0,57 | -0,26R | €-49,20 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 42 | 42 | 38,10% | 1,02 | 0,01R | €4,16 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 27 | 27 | 37,04% | 1,05 | 0,03R | €7,06 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 66,90 | 0,96R | €38,48 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 3 | 83 | 83 | 39,76% | 1,07 | 0,03R | €27,74 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 100 | 100 | 34,00% | 0,78 | -0,10R | €-104,07 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 27,27% | 0,67 | -0,23R | €-49,95 |
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
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 1 | 5 | 5 | 80,00% | 4,65 | 0,83R | €41,31 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,69 | -0,22R | €-6,71 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 20 | 20 | 10,00% | 0,17 | -0,57R | €-113,25 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 6 | 58 | 58 | 32,76% | 0,89 | -0,07R | €-38,83 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 84 | 84 | 46,43% | 1,45 | 0,21R | €179,30 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 2 | 55 | 55 | 43,64% | 1,74 | 0,34R | €186,29 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 43 | 43 | 30,23% | 0,73 | -0,15R | €-65,86 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,87 | -0,08R | €-12,45 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 2 | 40 | 40 | 27,50% | 0,66 | -0,21R | €-82,34 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 6 | 63 | 63 | 25,40% | 0,59 | -0,29R | €-182,74 |
| SHADOW_COMBO_TREND | RANGE | 0 | 128 | 128 | 35,16% | 1,04 | 0,02R | €24,85 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 23 | 23 | 34,78% | 1,15 | 0,07R | €15,88 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 61 | 61 | 36,07% | 1,32 | 0,17R | €103,93 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 65 | 65 | 30,77% | 0,70 | -0,17R | €-107,46 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 73 | 73 | 28,77% | 1,00 | -0,00R | €-0,70 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 23 | 23 | 30,43% | 0,79 | -0,14R | €-31,29 |
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
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 29 | 29 | 24,14% | 0,60 | -0,30R | €-85,94 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 3 | 28 | 28 | 14,29% | 0,17 | -0,73R | €-203,47 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 65 | 65 | 32,31% | 1,02 | 0,01R | €8,90 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 25 | 25 | 40,00% | 1,57 | 0,29R | €71,79 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 13 | 13 | 46,15% | 1,71 | 0,41R | €53,89 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 21,05% | 0,37 | -0,50R | €-94,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 3 | 20 | 20 | 15,00% | 0,10 | -0,77R | €-153,05 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 0 | 45 | 45 | 33,33% | 0,98 | -0,01R | €-6,16 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 18 | 18 | 50,00% | 2,40 | 0,56R | €101,05 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 57,14% | 2,54 | 0,70R | €49,11 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 2 | 43 | 43 | 25,58% | 0,57 | -0,28R | €-120,00 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 6 | 59 | 59 | 23,73% | 0,56 | -0,32R | €-187,65 |
| SHADOW_EMA_TREND_1H | RANGE | 0 | 125 | 125 | 35,20% | 1,08 | 0,04R | €49,33 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 60 | 60 | 35,00% | 1,17 | 0,10R | €57,24 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 67 | 67 | 31,34% | 0,68 | -0,17R | €-114,96 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 76 | 76 | 27,63% | 0,92 | -0,04R | €-31,30 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 31,82% | 0,84 | -0,10R | €-21,70 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 5 | 5 | 20,00% | 0,08 | -0,81R | €-40,61 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,74 | -0,17R | €-8,58 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,50R | €5,03 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 100,00% | ∞ | 1,39R | €27,88 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,23 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,24 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,56 | -0,33R | €-19,66 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,66 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 5 | 5 | 20,00% | 0,06 | -0,83R | €-41,29 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 6 | 6 | 33,33% | 0,68 | -0,24R | €-14,10 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 22,22% | 0,59 | -0,31R | €-55,48 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 32,35% | 0,94 | -0,04R | €-13,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 0 | 81 | 81 | 32,10% | 1,04 | 0,02R | €18,15 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 2 | 32 | 32 | 46,88% | 1,77 | 0,40R | €128,05 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 47 | 47 | 36,17% | 1,16 | 0,10R | €44,95 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 60 | 60 | 30,00% | 0,87 | -0,08R | €-50,78 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 25 | 25 | 52,00% | 1,10 | 0,04R | €11,03 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 149 | 149 | 66,44% | 1,46 | 0,14R | €213,68 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 72 | 72 | 75,00% | 1,91 | 0,22R | €160,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 2 | 75 | 75 | 65,33% | 1,35 | 0,12R | €90,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 23,53% | 0,69 | -0,21R | €-35,48 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 0 | 82 | 82 | 34,15% | 1,14 | 0,08R | €66,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 2 | 31 | 31 | 38,71% | 1,26 | 0,16R | €48,14 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 43 | 43 | 39,53% | 1,30 | 0,18R | €77,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 30,77% | 1,10 | 0,07R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 0 | 74 | 74 | 31,08% | 1,15 | 0,09R | €65,91 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 2 | 28 | 28 | 42,86% | 1,55 | 0,31R | €85,55 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 40 | 40 | 40,00% | 1,33 | 0,20R | €79,25 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,20 | -0,67R | €-73,38 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 59 | 59 | 35,59% | 1,11 | 0,07R | €41,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 2 | 24 | 24 | 50,00% | 2,25 | 0,54R | €130,72 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 31 | 31 | 25,81% | 0,70 | -0,22R | €-66,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 23,53% | 0,63 | -0,27R | €-45,34 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 0 | 77 | 77 | 33,77% | 1,14 | 0,08R | €61,59 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 2 | 31 | 31 | 41,94% | 1,44 | 0,25R | €78,11 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 41 | 41 | 39,02% | 1,27 | 0,17R | €68,09 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 3 | 52 | 52 | 19,23% | 0,38 | -0,42R | €-219,23 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 6 | 76 | 76 | 28,95% | 0,72 | -0,18R | €-139,82 |
| Forza relativa 1H V1 | RANGE | 1 | 169 | 169 | 30,18% | 0,81 | -0,10R | €-171,44 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 28 | 28 | 28,57% | 0,53 | -0,25R | €-70,96 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 2 | 71 | 71 | 38,03% | 1,46 | 0,23R | €161,78 |
| Forza relativa 1H V1 | TREND_DOWN | 3 | 72 | 72 | 29,17% | 0,87 | -0,07R | €-50,78 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 96 | 96 | 25,00% | 0,89 | -0,06R | €-55,92 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 20 | 20 | 20,00% | 0,63 | -0,25R | €-49,89 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 24 | 24 | 29,17% | 0,71 | -0,16R | €-39,30 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 29 | 26 | 34,48% | 1,17 | 0,09R | €26,73 |
| Forza relativa 1H V2 | RANGE | 2 | 73 | 70 | 34,25% | 0,90 | -0,05R | €-39,79 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 1 | 41 | 36 | 41,46% | 1,81 | 0,37R | €150,95 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 34 | 33 | 29,41% | 0,95 | -0,02R | €-7,23 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 31 | 31 | 12,90% | 0,15 | -0,65R | €-202,51 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 60 | 60 | 23,33% | 0,33 | -0,39R | €-236,12 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 31 | 31 | 12,90% | 0,15 | -0,65R | €-202,51 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 60 | 60 | 23,33% | 0,33 | -0,39R | €-236,12 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 31 | 31 | 12,90% | 0,15 | -0,65R | €-202,51 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 60 | 60 | 23,33% | 0,33 | -0,39R | €-236,12 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 27 | 27 | 22,22% | 0,57 | -0,29R | €-77,85 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,07 | 0,03R | €4,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 73 | 73 | 28,77% | 0,61 | -0,21R | €-156,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,33 | 0,13R | €23,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 37 | 37 | 37,84% | 0,98 | -0,01R | €-3,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 40 | 40 | 27,50% | 0,38 | -0,36R | €-144,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,63 | -0,23R | €-11,64 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 31 | 31 | 38,71% | 0,36 | -0,37R | €-116,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 65 | 65 | 53,85% | 0,64 | -0,16R | €-104,63 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 22 | 22 | 63,64% | 1,42 | 0,16R | €34,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 28 | 28 | 60,71% | 1,52 | 0,22R | €60,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 1 | 65 | 65 | 53,85% | 0,63 | -0,16R | €-106,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 50,00% | 0,18 | -0,41R | €-8,27 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 37,04% | 0,25 | -0,45R | €-120,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 58 | 58 | 53,45% | 0,38 | -0,27R | €-159,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 60,00% | 1,23 | 0,10R | €19,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 27 | 27 | 62,96% | 1,58 | 0,23R | €61,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 1 | 55 | 55 | 52,73% | 0,62 | -0,17R | €-92,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 50,00% | 0,18 | -0,41R | €-8,27 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 13 | 13 | 30,77% | 0,84 | -0,09R | €-11,54 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 6 | 61 | 61 | 27,87% | 0,63 | -0,22R | €-135,41 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 1 | 43 | 43 | 39,53% | 1,62 | 0,22R | €96,51 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,88 | -0,07R | €-7,90 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 13 | 13 | 30,77% | 0,84 | -0,09R | €-11,54 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 6 | 62 | 62 | 27,42% | 0,61 | -0,24R | €-146,52 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 1 | 43 | 43 | 39,53% | 1,62 | 0,22R | €96,51 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,88 | -0,07R | €-7,90 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 13 | 13 | 30,77% | 0,84 | -0,09R | €-11,54 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 6 | 62 | 62 | 27,42% | 0,61 | -0,24R | €-146,52 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 1 | 43 | 43 | 39,53% | 1,62 | 0,22R | €96,51 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,88 | -0,07R | €-7,90 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 18 | 18 | 11,11% | 0,21 | -0,51R | €-91,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 6 | 58 | 58 | 32,76% | 0,89 | -0,07R | €-38,24 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 79 | 79 | 46,84% | 1,60 | 0,27R | €212,29 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 2 | 51 | 51 | 43,14% | 1,81 | 0,36R | €183,87 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 62 | 62 | 29,03% | 0,95 | -0,02R | €-14,90 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,87 | -0,08R | €-12,45 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,79R | €-63,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 47 | 47 | 27,66% | 0,81 | -0,10R | €-47,19 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 6,25% | 0,02 | -0,70R | €-112,31 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 35,29% | 0,94 | -0,03R | €-16,02 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,46 | 0,21R | €159,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 2 | 39 | 39 | 46,15% | 2,24 | 0,46R | €179,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,13 | -0,45R | €-71,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 40 | 40 | 50,00% | 1,40 | 0,16R | €62,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,02 | -0,72R | €-101,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 2 | 36 | 36 | 41,67% | 1,85 | 0,34R | €123,31 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,52 | -0,25R | €-50,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 6 | 45 | 45 | 42,22% | 1,03 | 0,02R | €7,48 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 42 | 42 | 47,62% | 1,32 | 0,13R | €52,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 44,44% | 0,68 | -0,15R | €-13,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,23 | -0,50R | €-79,96 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 6 | 38 | 38 | 34,21% | 1,06 | 0,03R | €12,48 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 2 | 37 | 37 | 40,54% | 1,73 | 0,31R | €113,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,51 | -0,29R | €-20,55 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 27,27% | 0,48 | -0,27R | €-58,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 6 | 61 | 61 | 40,98% | 0,82 | -0,09R | €-54,48 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 81 | 81 | 46,91% | 1,52 | 0,20R | €162,96 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,61 | -0,16R | €-26,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 2 | 47 | 47 | 48,94% | 1,35 | 0,14R | €66,28 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 56 | 56 | 44,64% | 0,92 | -0,03R | €-18,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 33,33% | 0,65 | -0,21R | €-37,86 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,37 | -0,36R | €-39,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 6 | 59 | 59 | 30,51% | 0,86 | -0,09R | €-50,58 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 0 | 70 | 70 | 44,29% | 1,49 | 0,23R | €162,79 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 2 | 39 | 39 | 43,59% | 1,98 | 0,39R | €152,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 41 | 41 | 29,27% | 0,77 | -0,13R | €-54,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,28 | -0,54R | €-54,21 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 10,00% | 0,03 | -0,60R | €-60,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 6 | 60 | 60 | 31,67% | 0,81 | -0,11R | €-66,59 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 65 | 65 | 43,08% | 1,53 | 0,26R | €169,81 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 2 | 33 | 33 | 42,42% | 2,48 | 0,51R | €169,33 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 38 | 38 | 28,95% | 0,79 | -0,11R | €-43,01 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,11 | -0,66R | €-66,43 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 20 | 20 | 20,00% | 0,45 | -0,37R | €-74,45 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 6 | 60 | 60 | 30,00% | 0,76 | -0,14R | €-85,31 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 81 | 81 | 49,38% | 1,55 | 0,24R | €194,78 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 56 | 56 | 41,07% | 1,62 | 0,25R | €142,55 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 78 | 78 | 34,62% | 1,08 | 0,04R | €29,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 33,33% | 1,18 | 0,10R | €17,48 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,43 | -0,42R | €-12,62 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,75 | -0,18R | €-14,00 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,43R | €24,29 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,61 | -0,29R | €-8,74 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,60 | -0,30R | €-18,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,26 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 66,67% | 2,69 | 0,63R | €38,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,72R | €27,23 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 0,86 | -0,08R | €-1,51 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 1,02 | 0,01R | €1,11 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 1,15 | 0,11R | €3,17 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-20T00:06:04+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **652**
- Scenari virtuali ancora attivi: **12733**
- Gruppi in attesa dell'uscita originale: **208**
- Gruppi con originale chiuso ma Shadow ancora attive: **444**
- Confronti completati: **277433**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 6433 | 6502 | +€9,78 | 52,7% | 1856 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 6433 | 6502 | +€9,22 | 52,5% | 1813 | 60 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 6433 | 6502 | +€5,70 | 49,7% | 2057 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 6430 | 6499 | +€9,56 | 46,7% | 1501 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 6430 | 6499 | +€8,83 | 47,3% | 1394 | 189 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 6430 | 6499 | +€6,27 | 43,9% | 1698 | 106 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 6427 | 6496 | +€5,26 | 42,2% | 812 | 967 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 6420 | 6489 | +€5,67 | 36,4% | 1093 | 568 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 6420 | 6493 | +€3,58 | 50,0% | 1445 | 714 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 6407 | 6476 | +€4,70 | 39,9% | 646 | 1256 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 6398 | 6467 | +€7,76 | 51,1% | 1806 | 139 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 6396 | 6465 | +€5,43 | 39,8% | 553 | 891 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 6346 | 6415 | +€7,19 | 46,5% | 1238 | 325 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 6338 | 6407 | +€6,42 | 51,2% | 1695 | 207 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 6329 | 6398 | +€1,21 | 36,7% | 556 | 1463 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 6313 | 6386 | +€2,41 | 45,1% | 936 | 1070 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 6279 | 6352 | €-2,43 | 37,5% | 551 | 1558 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 6260 | 6329 | +€5,00 | 44,7% | 1089 | 556 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 6195 | 6264 | €-1,61 | 38,1% | 1121 | 1145 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 6091 | 6160 | €-5,89 | 30,3% | 525 | 1694 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-20T00:06:16+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **277433**
- Valutazioni prodotte: **19700**
- Candidature al Blocco 5: **78**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 379 | 0,489 | 0,265 | 0,380 | 61,2% | 93,8 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 5022 | 0,233 | 0,149 | 0,199 | 55,8% | 88,8 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 5022 | 0,235 | 0,161 | 0,204 | 55,5% | 88,4 | ELIGIBLE_FOR_MUTATION |
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

Generato: 2026-08-20T00:09:07+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 80 | 100,00% | 1,08 | +€70,32 | +€0,88 | 2,32% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 80 | 100,00% | 1,06 | +€54,59 | +€0,68 | 2,59% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 47 | 95,92% | 1,38 | +€375,14 | +€7,98 | 2,95% | EARLY_NOT_CONFIRMED |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 35 | 89,74% | 0,00 | €-352,22 | €-10,06 | 3,52% | EARLY_NOT_CONFIRMED |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 80 | 100,00% | 1,18 | +€226,56 | +€2,83 | 2,13% | NOT_READY_FOR_PROMOTION |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-20T00:05:51+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **54**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **656.84 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 142 | 0 | 17591.25 |
| DOWN_20 | 142 | 0 | 35182.50 |
| DOWN_30 | 142 | 0 | 52773.75 |
| DOWN_40 | 142 | 43 | 67236.36 |
| UP_10 | 59 | 2 | 5468.19 |
| UP_20 | 59 | 2 | 10876.38 |
| UP_30 | 59 | 3 | 16237.43 |
| UP_40 | 59 | 20 | 20953.67 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-20T00:05:15+00:00

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

Generato: 2026-08-20T00:09:11+00:00

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

Generato: 2026-08-20T00:09:11+00:00

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

Generato: 2026-08-20T00:09:11+00:00

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

Generato: 2026-08-20T00:09:11+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 19.0 | E | 135 | 1.08 | 0.039 | 8.23 |
| 2 | SHADOW_DONCHIAN_1H | BASELINE | 17.9 | E | 74 | 1.43 | 0.239 | 8.55 |
| 3 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | BASELINE | 16.9 | E | 42 | 1.62 | 0.323 | 8.16 |
| 4 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 16.1 | E | 60 | 1.40 | 0.203 | 7.65 |
| 5 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 15.7 | E | 83 | 1.20 | 0.095 | 8.50 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 14.0 | E | 159 | 0.79 | -0.117 | 29.49 |
| 7 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 13.1 | E | 121 | 0.90 | -0.058 | 24.39 |
| 8 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 12.9 | E | 131 | 0.82 | -0.106 | 25.05 |
| 9 | SHADOW_COMBO_ADAPTIVE | BASELINE | 12.8 | E | 96 | 1.10 | 0.048 | 14.19 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 11.4 | E | 110 | 0.87 | -0.075 | 14.74 |

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

Generato: 2026-08-20T00:09:11+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **UNKNOWN**
- Righe di performance: **652**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **308**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | MAIN | main | INSUFFICIENT | 81.6 | 4 | 99.00 | 0.750 | 0.00 |
| 2 | EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | momentum_breakout_v3_filtered | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.775 | 0.00 |
| 3 | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | shadow-1h-fast-v3-long-nohigh-cap75-lock-v1 | INSUFFICIENT | 80.5 | 5 | 3.14 | 0.433 | 1.01 |
| 4 | SHADOW_MASTER_ADAPTIVE_GB20_V1 | shadow-master-adaptive-gb20-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.550 | 0.00 |
| 5 | SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | shadow-master-adaptive-gb20-be-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.986 | 0.00 |
| 6 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | OBSERVING | 79.5 | 13 | 5.50 | 0.771 | 2.15 |
| 7 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | momentum_breakout_v3_filtered | OBSERVING | 79.4 | 27 | 2.37 | 0.308 | 2.85 |
| 8 | MAIN_SIDE_REGIME_GUARD_V1 | main-side-regime-guard-v1 | INSUFFICIENT | 77.6 | 4 | 2.87 | 0.469 | 1.00 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | shadow-1h-fast-v3-no-esports-stress-guard-v1 | INSUFFICIENT | 76.1 | 4 | 36.04 | 0.330 | 0.04 |
| 10 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | shadow-donchian-1h-gb20-120r-v1 | INSUFFICIENT | 75.6 | 8 | 3.33 | 0.651 | 2.16 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-20T00:09:11+00:00

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

Generato: 2026-08-20T00:05:51+00:00

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
