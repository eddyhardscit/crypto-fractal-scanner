# Paper trading automatico KuCoin

Generato: 2026-07-28T14:10:04+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-28T14:08:26+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-28T14:08:26+00:00 | 2026-07-28T14:08:26+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-28T13:45:00+00:00 | 2026-07-28T13:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-28T13:00:00+00:00 | 2026-07-28T13:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-28T08:00:00+00:00 | 2026-07-28T08:00:00+00:00 | 2,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | ZEC | 60m | SHORT | -6,54 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | ZEC | 60m | SHORT | -6,54 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Side × Regime Guard | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SUI | 60m | SHORT | -6,65 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom20 Short | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom15 Short | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom10 Short | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom 5 Short 1H | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | ZEC | 60m | SHORT | -6,54 | 4,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | SUI | 60m | SHORT | -6,65 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | ZEC | 60m | SHORT | -6,54 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -7,55 | 6,00 | 0,00 | STALE_CANDLE | 2,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,50 | 6,00 | 0,00 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -7,36 | 6,00 | 0,00 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -6,78 | 6,00 | 0,00 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -5,97 | 6,00 | 0,03 | STALE_CANDLE | 2,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -5,36 | 6,00 | 0,64 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -4,50 | 6,00 | 1,50 | STALE_CANDLE | 2,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,42 | 6,00 | 5,58 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 0,05 | 6,00 | 5,95 | STALE_CANDLE | 2,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 128.5 minuti; tolleranza 60 minuti. |
| Rapida V1 — target pieno 2R | SOL | 60m | SHORT | -9,04 | 4,50 | 0,00 | OPENED | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | SOL | 60m | SHORT | -9,04 | 5,00 | 0,00 | OPENED | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | SOL | 60m | SHORT | -9,04 | 5,00 | 0,00 | OPENED | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | SOL | 60m | SHORT | -9,04 | 5,00 | 0,00 | OPENED | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | SOL | 60m | SHORT | -9,04 | 5,00 | 0,00 | READY | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — MFE Trail esistente | SOL | 60m | SHORT | -9,04 | 5,00 | 0,00 | READY | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — target pieno 3R | SOL | 60m | SHORT | -9,04 | 5,00 | 0,00 | READY | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | SOL | 60m | SHORT | -9,04 | 4,50 | 0,00 | OPENED | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.722,66 | -2,77% | €-277,34 | €3.000,00 | -9,24% | 6 | 26 | 30,77% | 0,67 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 26 | 896 | CAMPIONE INSUFFICIENTE | 30 (mancano 4) |

- Trade del Principale 4H chiusi: **26**; win rate **30,77%**; profit factor **0,67**.
- Expectancy: **€-13,46** per trade; P&L netto: **€-349,93**; max drawdown: **6,36%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.722,66 | €1.313,84 | €3.941,53 | €99,53 | €74,12 |
| TEST | Rapida V1 — score 6–7,5 | 5 | €10.678,53 | €2.881,83 | €8.645,50 | €104,40 | €50,56 |
| TEST | Rapida score 6–7,5 — Cost Aware | 5 | €10.638,17 | €2.881,44 | €8.644,31 | €105,56 | €50,42 |
| TEST | Benchmark Donchian breakout 1H | 6 | €10.629,54 | €2.830,47 | €5.660,94 | €153,09 | €54,82 |
| TEST | Bilanciata 1H V3 Filtered | 8 | €10.603,51 | €2.407,02 | €7.221,05 | €210,27 | €15,58 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 6 | €10.494,86 | €2.960,00 | €8.879,99 | €52,77 | €131,19 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 6 | €10.490,86 | €5.014,31 | €15.042,92 | €55,23 | €164,04 |
| TEST | Rapida V3 — score <7,5 | 5 | €10.466,95 | €2.797,25 | €8.391,75 | €102,89 | €48,83 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 7 | €10.424,09 | €3.833,71 | €11.501,13 | €99,89 | €98,28 |
| TEST | Bilanciata 1H V1 | 10 | €10.423,26 | €3.167,47 | €9.502,42 | €106,97 | €69,95 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 5 | €10.419,48 | €3.800,58 | €11.401,75 | €102,45 | €65,56 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.416,26 | €70,71 | €141,42 | €2,58 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 1 | €10.415,57 | €225,73 | €677,19 | €51,70 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.406,55 | €3.842,38 | €7.684,77 | €110,19 | €120,58 |
| TEST | Rapida V3 NoHigh — Regime Guard | 1 | €10.395,73 | €172,19 | €516,57 | €51,51 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 6 | €10.364,72 | €3.327,39 | €9.982,18 | €102,91 | €26,50 |
| TEST | Combo Adaptive — Side × Regime Guard | 7 | €10.348,92 | €3.702,73 | €7.405,46 | €156,53 | €37,41 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 7 | €10.328,47 | €5.009,31 | €15.027,93 | €104,26 | €109,78 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.312,84 | €143,54 | €430,62 | €51,67 | €-21,68 |
| TEST | Rapida V1 — senza PEPE | 6 | €10.309,14 | €2.438,40 | €7.315,20 | €50,18 | €45,76 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.296,85 | €313,60 | €940,79 | €102,49 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €10.284,11 | €37,16 | €74,32 | €1,36 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.276,57 | €2.225,27 | €6.675,81 | €51,14 | €80,78 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.267,93 | €1.459,95 | €4.379,86 | €101,81 | €97,87 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.235,71 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.224,48 | €2.386,28 | €7.158,85 | €49,95 | €44,19 |
| TEST | Rapida score 6–7,5 — Range Only | 1 | €10.218,59 | €143,01 | €429,04 | €51,48 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 6 | €10.181,32 | €2.682,91 | €5.365,82 | €202,59 | €-0,86 |
| TEST | Bilanciata 1H V2 | 3 | €10.181,14 | €1.358,78 | €4.076,33 | €101,14 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 10 | €10.162,81 | €4.112,17 | €8.224,35 | €202,87 | €45,06 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.157,10 | €141,34 | €424,02 | €50,88 | €-19,22 |
| TEST | FAST NoHigh <7,5 · SHORT only | 1 | €10.156,35 | €212,58 | €637,75 | €48,69 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.145,37 | €1.254,69 | €3.764,07 | €0,00 | €55,88 |
| TEST | Combo Trend — Side × Regime Guard | 7 | €10.140,27 | €3.527,57 | €7.055,14 | €200,54 | €30,87 |
| TEST | Rapida V1 — target pieno 2R | 7 | €10.128,50 | €4.184,75 | €12.554,25 | €148,49 | €73,08 |
| TEST | Forza relativa 1H V2 | 5 | €10.118,14 | €3.817,55 | €7.635,10 | €104,77 | €99,53 |
| TEST | Doge Ema 1H | 1 | €10.117,26 | €1.101,76 | €3.305,29 | €0,00 | €27,06 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €10.090,19 | €1.220,11 | €3.660,32 | €50,47 | €-1,78 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 1 | €10.071,75 | €140,15 | €420,46 | €50,46 | €-19,06 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.071,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.071,01 | €1.784,35 | €3.568,70 | €152,43 | €95,94 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 9 | €10.058,88 | €2.607,30 | €5.214,60 | €102,82 | €46,84 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 7 | €10.051,18 | €2.817,41 | €8.452,23 | €98,01 | €73,99 |
| TEST | Combo Adaptive — Quality7 | 4 | €10.044,09 | €2.502,69 | €5.005,39 | €200,34 | €10,34 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €10.034,36 | €1.158,94 | €3.476,83 | €50,07 | €22,83 |
| TEST | Bilanciata V3 · LONG only | 6 | €10.033,48 | €2.380,43 | €7.141,30 | €149,24 | €-6,70 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €10.016,38 | €2.338,25 | €7.014,75 | €48,93 | €43,32 |
| TEST | Sol Donchian 4H | 1 | €10.014,99 | €830,21 | €1.660,43 | €0,00 | €67,56 |
| TEST | Btc Donchian 1H | 1 | €10.011,95 | €1.299,56 | €3.898,68 | €0,00 | €33,28 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.009,58 | €761,04 | €1.522,08 | €0,00 | €61,93 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 2 | €9.993,33 | €1.397,03 | €2.794,06 | €51,31 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.990,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.975,58 | €2.754,35 | €5.508,69 | €198,97 | €-26,76 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.973,08 | €1.091,78 | €3.275,34 | €49,89 | €-1,78 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.953,85 | €1.196,13 | €2.392,26 | €49,75 | €4,36 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.951,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 2 | €9.939,55 | €293,75 | €587,51 | €53,17 | €-11,95 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 2 | €9.933,70 | €279,19 | €558,38 | €52,62 | €-11,94 |
| TEST | Btc Ema 1H | 1 | €9.932,73 | €1.147,21 | €3.441,62 | €49,56 | €22,59 |
| TEST | Scanner Bottom10 Short | 9 | €9.928,60 | €3.367,81 | €6.735,63 | €102,75 | €45,91 |
| TEST | Scanner Bottom15 Short | 9 | €9.928,60 | €3.367,81 | €6.735,63 | €102,75 | €45,91 |
| TEST | Scanner Bottom20 Short | 9 | €9.928,60 | €3.367,81 | €6.735,63 | €102,75 | €45,91 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 6 | €9.913,75 | €1.574,83 | €3.149,66 | €198,32 | €-10,80 |
| TEST | Combo Adaptive — Trend/Transition | 1 | €9.903,77 | €206,52 | €413,04 | €49,56 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 1 | €9.903,06 | €206,57 | €413,13 | €49,58 | €-11,83 |
| TEST | Sol Ema 4H | 1 | €9.902,12 | €780,22 | €1.560,44 | €49,48 | €6,77 |
| TEST | Sol Bollinger 1H | 1 | €9.899,78 | €1.300,18 | €3.900,53 | €49,51 | €0,56 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 9 | €9.883,72 | €3.003,31 | €6.006,62 | €52,76 | €46,14 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.867,68 | €137,31 | €411,94 | €49,43 | €-18,68 |
| TEST | Rapida V3 — no volatilità HIGH | 0 | €9.865,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 2 | €9.865,63 | €244,69 | €489,37 | €51,07 | €-11,86 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 9 | €9.857,23 | €2.955,13 | €5.910,25 | €196,16 | €22,19 |
| TEST | Global Confluence puro 1H | 1 | €9.846,04 | €1.428,07 | €2.856,13 | €49,20 | €8,00 |
| TEST | Combo Scanner | 2 | €9.841,61 | €230,44 | €460,88 | €50,44 | €-11,83 |
| TEST | Combo Mean Reversion | 0 | €9.832,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.831,70 | €1.267,95 | €3.803,86 | €49,17 | €0,33 |
| TEST | Sol Adaptive 1H | 1 | €9.831,24 | €1.076,25 | €3.228,75 | €49,18 | €-1,75 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 1 | €9.813,54 | €194,51 | €583,53 | €49,25 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 1 | €9.806,54 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.799,16 | €33,54 | €67,08 | €1,22 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 1 | €9.796,05 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 2 | €9.776,14 | €2.043,62 | €4.087,25 | €100,09 | €42,12 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.771,73 | €20,87 | €41,74 | €0,76 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 1 | €9.758,94 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.757,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 1 | €9.754,92 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Top 5 + BTC — Guard | 0 | €9.745,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.721,66 | €135,28 | €405,85 | €48,70 | €-18,40 |
| TEST | Forza relativa 1H V1 | 8 | €9.719,61 | €3.336,10 | €6.672,20 | €155,85 | €36,83 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 1 | €9.717,28 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 8 | €9.713,82 | €2.573,93 | €5.147,87 | €129,13 | €31,70 |
| TEST | Combo Trend | 9 | €9.703,95 | €4.136,96 | €8.273,93 | €192,92 | €19,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.695,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.669,36 | €2.839,99 | €5.679,98 | €73,94 | €-8,64 |
| TEST | Top 5 + BTC — solo MFE | 1 | €9.643,08 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| TEST | Scanner Top10 Long | 3 | €9.634,63 | €1.597,71 | €3.195,42 | €101,26 | €-11,58 |
| TEST | Scanner Top15 Long | 3 | €9.634,63 | €1.597,71 | €3.195,42 | €101,26 | €-11,58 |
| TEST | Scanner Top20 Long | 3 | €9.634,63 | €1.597,71 | €3.195,42 | €101,26 | €-11,58 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.628,98 | €1.549,90 | €3.099,79 | €97,01 | €0,00 |
| TEST | Rapida V3 — Long Only | 1 | €9.589,41 | €133,44 | €400,32 | €48,04 | €-18,15 |
| TEST | Combo Adaptive — MFE Trail esistente | 6 | €9.530,34 | €3.263,97 | €6.527,95 | €98,82 | €57,17 |
| TEST | Top 5 + BTC — Guard + MFE | 0 | €9.518,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.408,26 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.722,66 | €-349,93 | 26 | 26 | 30,77% | 0,67 | €-13,46 | 6,36% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.678,53 | €633,16 | 64 | 64 | 46,88% | 1,59 | €9,89 | 2,49% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.638,17 | €592,93 | 27 | 27 | 59,26% | 2,63 | €21,96 | 1,96% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.629,54 | €578,41 | 34 | 34 | 55,88% | 1,67 | €17,01 | 3,09% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.603,51 | €591,88 | 55 | 55 | 43,64% | 1,52 | €10,76 | 2,20% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.494,86 | €369,41 | 22 | 22 | 54,55% | 3,28 | €16,79 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.490,86 | €335,84 | 9 | 9 | 55,56% | 5,00 | €37,32 | 1,14% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.466,95 | €423,14 | 58 | 58 | 48,28% | 1,40 | €7,30 | 2,49% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.424,09 | €332,24 | 31 | 31 | 48,39% | 1,67 | €10,72 | 2,70% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.423,26 | €361,85 | 60 | 60 | 51,67% | 1,33 | €6,03 | 3,56% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.419,48 | €360,75 | 23 | 23 | 65,22% | 1,87 | €15,68 | 2,01% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.416,26 | €416,34 | 48 | 48 | 45,83% | 1,38 | €8,67 | 4,23% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.415,57 | €415,97 | 60 | 60 | 46,67% | 1,35 | €6,93 | 2,83% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.406,55 | €290,37 | 3 | 3 | 100,00% | ∞ | €96,79 | 1,09% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.395,73 | €396,49 | 18 | 18 | 66,67% | 3,42 | €22,03 | 1,39% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.364,72 | €343,76 | 43 | 43 | 58,14% | 1,62 | €7,99 | 2,51% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.348,92 | €315,83 | 22 | 22 | 68,18% | 2,35 | €14,36 | 1,41% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.328,47 | €226,85 | 11 | 11 | 45,45% | 2,20 | €20,62 | 1,99% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.312,84 | €334,77 | 9 | 9 | 55,56% | 3,00 | €37,20 | 1,50% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.309,14 | €267,05 | 59 | 59 | 45,76% | 1,25 | €4,53 | 2,15% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.296,85 | €297,96 | 10 | 10 | 70,00% | 2,84 | €29,80 | 1,78% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.284,11 | €284,16 | 39 | 39 | 41,03% | 1,34 | €7,29 | 3,38% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.276,57 | €200,23 | 48 | 48 | 52,08% | 1,32 | €4,17 | 2,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.267,93 | €172,76 | 12 | 12 | 41,67% | 1,53 | €14,40 | 2,40% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.235,71 | €236,97 | 14 | 14 | 57,14% | 4,59 | €16,93 | 1,01% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.224,48 | €183,88 | 92 | 92 | 39,13% | 1,10 | €2,00 | 2,89% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.218,59 | €218,95 | 12 | 12 | 58,33% | 1,75 | €18,25 | 2,28% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.181,32 | €186,51 | 30 | 30 | 46,67% | 1,44 | €6,22 | 1,77% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.181,14 | €183,58 | 38 | 36 | 52,63% | 1,24 | €4,83 | 2,75% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.162,81 | €121,20 | 30 | 30 | 43,33% | 1,23 | €4,04 | 2,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.157,10 | €176,58 | 26 | 26 | 42,31% | 1,45 | €6,79 | 3,57% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.156,35 | €156,74 | 24 | 24 | 45,83% | 1,47 | €6,53 | 1,76% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.145,37 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.140,27 | €113,03 | 21 | 21 | 52,38% | 1,33 | €5,38 | 1,73% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.128,50 | €62,53 | 65 | 65 | 36,92% | 1,05 | €0,96 | 2,58% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.118,14 | €23,01 | 46 | 45 | 39,13% | 1,02 | €0,50 | 5,10% |
| TEST | Doge Ema 1H | Trend following EMA | €10.117,26 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.090,19 | €93,80 | 5 | 5 | 80,00% | 2,64 | €18,76 | 1,08% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.071,75 | €91,07 | 32 | 32 | 43,75% | 1,15 | €2,85 | 3,13% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.071,28 | €71,28 | 19 | 19 | 42,11% | 1,16 | €3,75 | 2,17% |
| TEST | Ampia 4H | Confluenza trend | €10.071,01 | €-23,31 | 21 | 21 | 23,81% | 0,96 | €-1,11 | 3,68% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €10.058,88 | €15,82 | 9 | 9 | 66,67% | 1,10 | €1,76 | 1,53% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €10.051,18 | €-18,16 | 26 | 26 | 50,00% | 0,96 | €-0,70 | 3,08% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.044,09 | €37,50 | 22 | 22 | 36,36% | 1,12 | €1,70 | 1,85% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.034,36 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €10.033,48 | €44,79 | 14 | 14 | 42,86% | 1,16 | €3,20 | 1,46% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.016,38 | €-23,42 | 66 | 66 | 39,39% | 0,98 | €-0,35 | 2,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.014,99 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,79% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.011,95 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,36 | €10,36 | 10 | 10 | 30,00% | 1,22 | €1,04 | 0,25% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.009,58 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,77% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,07 | €2,07 | 10 | 10 | 30,00% | 1,22 | €0,21 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.993,33 | €-4,99 | 17 | 17 | 29,41% | 0,98 | €-0,29 | 2,34% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.990,65 | €-9,35 | 14 | 14 | 42,86% | 0,97 | €-0,67 | 2,46% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.975,58 | €5,91 | 10 | 10 | 70,00% | 1,04 | €0,59 | 1,38% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | Sol Ema 1H | Trend following EMA | €9.973,08 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.953,85 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,07% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.951,70 | €-48,30 | 10 | 10 | 30,00% | 0,27 | €-4,83 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.939,55 | €-48,15 | 23 | 23 | 34,78% | 0,93 | €-2,09 | 3,83% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.933,70 | €-54,02 | 27 | 27 | 37,04% | 0,92 | €-2,00 | 4,14% |
| TEST | Btc Ema 1H | Trend following EMA | €9.932,73 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.928,60 | €-112,62 | 10 | 10 | 50,00% | 0,59 | €-11,26 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.928,60 | €-112,62 | 10 | 10 | 50,00% | 0,59 | €-11,26 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.928,60 | €-112,62 | 10 | 10 | 50,00% | 0,59 | €-11,26 | 2,72% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.913,75 | €-72,48 | 15 | 15 | 40,00% | 0,74 | €-4,83 | 1,49% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.903,77 | €-95,76 | 21 | 21 | 47,62% | 0,79 | €-4,56 | 2,18% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.903,06 | €-84,85 | 17 | 17 | 35,29% | 0,84 | €-4,99 | 3,57% |
| TEST | Sol Ema 4H | Trend following EMA | €9.902,12 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,13% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.899,78 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.883,72 | €-155,18 | 33 | 33 | 39,39% | 0,79 | €-4,70 | 5,48% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.867,68 | €-113,40 | 27 | 27 | 37,04% | 0,80 | €-4,20 | 3,56% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.865,90 | €-134,10 | 61 | 61 | 37,70% | 0,90 | €-2,20 | 2,96% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.865,63 | €-122,22 | 19 | 19 | 36,84% | 0,77 | €-6,43 | 3,58% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.857,23 | €-160,48 | 34 | 34 | 35,29% | 0,81 | €-4,72 | 3,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.846,04 | €-160,53 | 11 | 11 | 36,36% | 0,52 | €-14,59 | 2,92% |
| TEST | Combo Scanner | Combo Scanner | €9.841,61 | €-146,28 | 46 | 46 | 39,13% | 0,87 | €-3,18 | 3,71% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.832,55 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,60% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.831,70 | €-165,97 | 3 | 3 | 0,00% | 0,00 | €-55,32 | 1,88% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.831,24 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,65% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.813,54 | €-186,11 | 22 | 22 | 40,91% | 0,63 | €-8,46 | 2,93% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.806,54 | €-191,77 | 21 | 21 | 19,05% | 0,67 | €-9,13 | 3,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.799,16 | €-200,80 | 21 | 21 | 33,33% | 0,74 | €-9,56 | 3,64% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.796,05 | €-202,30 | 16 | 16 | 31,25% | 0,62 | €-12,64 | 2,89% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.776,14 | €-263,40 | 17 | 17 | 23,53% | 0,60 | €-15,49 | 3,84% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.771,73 | €-228,24 | 20 | 20 | 30,00% | 0,69 | €-11,41 | 3,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.758,94 | €-241,03 | 18 | 18 | 27,78% | 0,66 | €-13,39 | 4,03% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.757,70 | €-242,30 | 6 | 6 | 0,00% | 0,00 | €-40,38 | 2,42% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.754,92 | €-245,05 | 18 | 18 | 27,78% | 0,66 | €-13,61 | 4,07% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.745,31 | €-254,69 | 23 | 23 | 26,09% | 0,64 | €-11,07 | 3,65% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.721,66 | €-259,70 | 7 | 7 | 0,00% | 0,00 | €-37,10 | 2,92% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.719,61 | €-313,22 | 38 | 38 | 28,95% | 0,71 | €-8,24 | 7,55% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.717,28 | €-281,07 | 17 | 17 | 29,41% | 0,52 | €-16,53 | 3,70% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.713,82 | €-314,53 | 30 | 30 | 43,33% | 0,53 | €-10,48 | 3,32% |
| TEST | Combo Trend | Combo Trend | €9.703,95 | €-309,81 | 49 | 49 | 34,69% | 0,81 | €-6,32 | 7,02% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.695,77 | €-304,23 | 33 | 33 | 36,36% | 0,65 | €-9,22 | 3,93% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.669,36 | €-318,30 | 48 | 48 | 37,50% | 0,76 | €-6,63 | 5,69% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.643,08 | €-355,29 | 32 | 32 | 34,38% | 0,50 | €-11,10 | 4,44% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.634,63 | €-351,86 | 18 | 18 | 33,33% | 0,41 | €-19,55 | 5,45% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.634,63 | €-351,86 | 18 | 18 | 33,33% | 0,41 | €-19,55 | 5,45% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.634,63 | €-351,86 | 18 | 18 | 33,33% | 0,41 | €-19,55 | 5,45% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.628,98 | €-369,16 | 52 | 52 | 57,69% | 0,60 | €-7,10 | 4,27% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.589,41 | €-392,20 | 52 | 52 | 30,77% | 0,70 | €-7,54 | 5,22% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.530,34 | €-522,70 | 41 | 41 | 31,71% | 0,48 | €-12,75 | 5,33% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.518,67 | €-481,33 | 40 | 40 | 35,00% | 0,55 | €-12,03 | 5,08% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.408,26 | €-590,15 | 26 | 26 | 23,08% | 0,49 | €-22,70 | 6,12% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 54,28900 | 55,59343 | 76,08234 | 53,15302 | €419,05 | €1.257,15 | €0,00 | €65,57 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 72,87300 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €0,12 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,06978 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €8,43 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63620,87328 | 63203,20000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.153,42 | €3.460,26 | €49,83 | €22,72 |
| Bilanciata 1H V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 72,83343 | 72,87300 | 73,94273 | 96,74707 | 70,61483 | €70,54 | €211,63 | €3,22 | €-0,11 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06986 | 0,06978 | 0,07086 | 0,09279 | 0,06784 | €9,58 | €28,74 | €0,41 | €0,03 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 55,45791 | 54,28900 | 55,03797 | 73,66659 | 53,07120 | €749,39 | €2.248,16 | €0,00 | €47,39 |
| Bilanciata 1H V1 | SUI | SHORT | Confluenza trend | 60m | 3,0x | 0,67989 | 0,68120 | 0,68980 | 0,90312 | 0,66007 | €9,22 | €27,67 | €0,40 | €-0,05 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,05070 | 1,05073 | 1,06583 | 1,39568 | 1,02044 | €9,71 | €29,14 | €0,42 | €-0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 461,98758 | 462,08000 | 472,28995 | 613,67351 | 441,38284 | €25,84 | €77,53 | €1,73 | €-0,02 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,97120 | 72,87300 | 73,55885 | 98,25841 | 71,73999 | €39,75 | €119,24 | €0,00 | €1,77 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63046,01827 | 63203,20000 | 63953,88094 | 83746,12761 | 61230,29295 | €1.219,33 | €3.657,98 | €52,67 | €-9,12 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 54,81304 | 54,28900 | 55,99251 | 72,80998 | 52,45408 | €780,21 | €2.340,62 | €50,37 | €22,38 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 465,14695 | 462,08000 | 475,14156 | 617,87020 | 445,15774 | €29,03 | €87,10 | €1,87 | €0,57 |
| Bilanciata 1H V3 Filtered | SUI | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,68079 | 0,68120 | 0,69075 | 0,90432 | 0,66088 | €11,70 | €35,10 | €0,51 | €-0,02 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,68319 | 0,68120 | 0,68319 | 0,90750 | 0,66864 | €37,40 | €112,21 | €0,00 | €0,33 |
| Rapida V1 — score 6–7,5 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €1.060,53 | €3.181,60 | €0,00 | €50,07 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 464,73703 | 462,08000 | 464,73703 | 617,32569 | 453,08694 | €17,51 | €52,52 | €0,00 | €0,30 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05070 | 1,05073 | 1,06247 | 1,39568 | 1,03305 | €1.553,72 | €4.661,16 | €52,20 | €-0,13 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63046,01827 | 63203,20000 | 63752,13368 | 83746,12761 | 61986,84517 | €30,09 | €90,27 | €1,01 | €-0,23 |
| Rapida score 6–7,5 — senza Trend Up | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €1.037,84 | €3.113,52 | €0,00 | €49,00 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 464,73703 | 462,08000 | 464,73703 | 617,32569 | 453,08694 | €986,77 | €2.960,31 | €0,00 | €16,92 |
| Rapida score 6–7,5 — senza Trend Up | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05070 | 1,05073 | 1,06247 | 1,39568 | 1,03305 | €1.526,97 | €4.580,92 | €51,31 | €-0,13 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06998 | 0,06978 | 0,07082 | 0,09295 | 0,06871 | €43,95 | €131,85 | €1,59 | €0,37 |
| Rapida score 6–7,5 — Cost Aware | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €1.056,48 | €3.169,45 | €0,00 | €49,88 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 464,73703 | 462,08000 | 464,73703 | 617,32569 | 453,08694 | €18,17 | €54,52 | €0,00 | €0,31 |
| Rapida score 6–7,5 — Cost Aware | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05070 | 1,05073 | 1,06247 | 1,39568 | 1,03305 | €1.551,63 | €4.654,89 | €52,13 | €-0,13 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — senza PEPE | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63620,87328 | 63203,20000 | 63405,53224 | 84509,72667 | 62552,04261 | €19,21 | €57,62 | €0,00 | €0,38 |
| Rapida V1 — senza PEPE | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,18636 | 72,87300 | 73,18636 | 97,21588 | 71,83419 | €8,54 | €25,63 | €0,00 | €0,11 |
| Rapida V1 — senza PEPE | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05690 | 1,05073 | 1,05690 | 1,40391 | 1,03914 | €9,88 | €29,65 | €0,00 | €0,17 |
| Rapida V1 — senza PEPE | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06871 | €1.435,95 | €4.307,84 | €50,18 | €9,61 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 467,76643 | 462,08000 | 467,76643 | 621,34974 | 454,86994 | €936,88 | €2.810,64 | €0,00 | €34,17 |
| Rapida V1 — senza PEPE | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €27,94 | €83,82 | €0,00 | €1,32 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | NEAR | SHORT | Momentum / breakout | 60m | 3,0x | 1,67599 | 1,67599 | 1,70517 | 2,22628 | 1,61763 | €25,97 | €77,91 | €1,36 | €-0,00 |
| Rapida V1 — target pieno 2R | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06831 | €1.394,41 | €4.183,24 | €48,73 | €9,33 |
| Rapida V1 — target pieno 2R | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 55,45791 | 54,28900 | 54,90855 | 73,66659 | 53,60158 | €1.005,49 | €3.016,47 | €0,00 | €63,58 |
| Rapida V1 — target pieno 2R | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 465,14695 | 462,08000 | 465,14695 | 617,87020 | 449,59978 | €54,37 | €163,12 | €0,00 | €1,08 |
| Rapida V1 — target pieno 2R | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05070 | 1,05073 | 1,06247 | 1,39568 | 1,02716 | €9,41 | €28,24 | €0,32 | €-0,00 |
| Rapida V1 — target pieno 2R | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 72,85843 | 72,87300 | 73,67444 | 96,78028 | 71,22640 | €1.507,76 | €4.523,27 | €50,66 | €-0,90 |
| Rapida 1H V3 Filtered — madre | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 72,87300 | 73,18636 | 97,21588 | 71,83419 | €8,54 | €25,62 | €0,00 | €0,11 |
| Rapida 1H V3 Filtered — madre | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05073 | 1,05690 | 1,40391 | 1,03914 | €9,49 | €28,48 | €0,00 | €0,17 |
| Rapida 1H V3 Filtered — madre | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06871 | €1.429,19 | €4.287,56 | €49,95 | €9,56 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 467,76643 | 462,08000 | 467,76643 | 621,34974 | 454,86994 | €929,36 | €2.788,07 | €0,00 | €33,89 |
| Rapida 1H V3 Filtered — madre | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €9,71 | €29,13 | €0,00 | €0,46 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63203,20000 | 63752,13368 | 83746,12761 | 61986,84517 | €54,22 | €162,67 | €1,82 | €-0,41 |
| Rapida V3 — score <7,5 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €1.039,15 | €3.117,44 | €0,00 | €49,06 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 464,73703 | 462,08000 | 464,73703 | 617,32569 | 453,08694 | €17,98 | €53,94 | €0,00 | €0,31 |
| Rapida V3 — score <7,5 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05070 | 1,05073 | 1,06247 | 1,39568 | 1,03305 | €1.458,58 | €4.375,74 | €49,01 | €-0,13 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00469 | 0,00447 | 0,00412 | 0,00315 | 0,00553 | €133,44 | €400,32 | €48,04 | €-18,15 |
| Rapida V3 — senza ESPORTS | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 72,87300 | 73,18636 | 97,21588 | 71,83419 | €8,36 | €25,09 | €0,00 | €0,11 |
| Rapida V3 — senza ESPORTS | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05073 | 1,05690 | 1,40391 | 1,03914 | €9,31 | €27,93 | €0,00 | €0,16 |
| Rapida V3 — senza ESPORTS | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06871 | €1.400,09 | €4.200,28 | €48,93 | €9,37 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 467,76643 | 462,08000 | 467,76643 | 621,34974 | 454,86994 | €910,44 | €2.731,31 | €0,00 | €33,20 |
| Rapida V3 — senza ESPORTS | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,15697 | 54,28900 | 54,90855 | 73,26684 | 53,77228 | €10,05 | €30,14 | €0,00 | €0,47 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00469 | 0,00447 | 0,00412 | 0,00315 | 0,00553 | €140,15 | €420,46 | €50,46 | €-19,06 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 72,87300 | 73,18636 | 97,21588 | 71,83419 | €13,72 | €41,16 | €0,00 | €0,18 |
| Rapida V3 senza ESPORTS — MFE Lock | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,07018 | 0,06978 | 0,06997 | 0,09322 | 0,06895 | €37,48 | €112,45 | €0,00 | €0,63 |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32093 | 54,28900 | 54,53677 | 73,48464 | 53,90994 | €1.011,79 | €3.035,38 | €0,00 | €56,62 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 465,73683 | 462,08000 | 463,80129 | 618,65376 | 454,12355 | €991,31 | €2.973,93 | €0,00 | €23,35 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 54,28900 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €59,26 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00412 | 0,00447 | 0,00412 | 0,00208 | 0,00550 | €208,53 | €417,05 | €0,00 | €36,17 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,05073 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €0,34 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63318,66373 | 63203,20000 | 64874,97444 | 94661,40228 | 58960,99415 | €18,28 | €36,56 | €0,90 | €0,07 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,06978 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €0,12 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,05518 | 1,05073 | 1,07037 | 1,57749 | 1,02175 | €24,53 | €49,07 | €0,71 | €0,21 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,67919 | 0,68120 | 0,69024 | 1,01539 | 0,65489 | €32,42 | €64,83 | €1,05 | €-0,19 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 55,45791 | 54,28900 | 55,10269 | 82,90957 | 52,83253 | €883,62 | €1.767,24 | €0,00 | €37,25 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 439,32237 | €1.089,83 | €2.179,67 | €48,61 | €-0,44 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 477,51448 | 462,08000 | 470,42964 | 713,88414 | 452,76011 | €1.065,11 | €2.130,22 | €0,00 | €68,85 |
| Forza relativa 1H V2 | HYPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 55,41391 | 54,28900 | 55,29106 | 82,84380 | 52,71367 | €1.050,01 | €2.100,03 | €0,00 | €42,63 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00582 | €208,61 | €417,23 | €50,07 | €-11,95 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 462,08000 | 470,84446 | 723,19613 | 452,69979 | €19,59 | €39,18 | €0,00 | €1,75 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63620,87328 | 63203,20000 | 64638,80725 | 95113,20555 | 61076,03835 | €1.401,20 | €2.802,39 | €44,84 | €18,40 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 72,83343 | 72,87300 | 74,06598 | 108,88598 | 69,75205 | €39,01 | €78,03 | €1,32 | €-0,04 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,28900 | 56,47572 | 82,45966 | 51,86008 | €1.103,00 | €2.206,00 | €52,74 | €34,71 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 462,08000 | 470,84446 | 723,19613 | 452,69979 | €978,17 | €1.956,34 | €0,00 | €87,61 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63046,01827 | 63203,20000 | 64054,75457 | 94253,79732 | 60524,17754 | €69,70 | €139,41 | €2,23 | €-0,35 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,28900 | 56,47572 | 82,45966 | 51,86008 | €1.079,15 | €2.158,31 | €51,60 | €33,96 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 72,85843 | 72,87300 | 74,02416 | 108,92335 | 69,94409 | €1.626,43 | €3.252,86 | €52,05 | €-0,65 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06977 | 0,06978 | 0,06887 | 0,03524 | 0,07113 | €1.881,64 | €3.763,27 | €48,65 | €0,33 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,21564 | 72,87300 | 72,24942 | 36,97390 | 74,66497 | €958,36 | €1.916,71 | €25,29 | €-8,97 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,67450 | 0,68120 | 0,68819 | 1,00837 | 0,64436 | €18,93 | €37,85 | €0,77 | €-0,38 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 55,41391 | 54,28900 | 56,77767 | 82,84380 | 52,41364 | €13,15 | €26,30 | €0,65 | €0,53 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 464,73703 | 462,08000 | 475,83237 | 694,78187 | 440,32730 | €966,09 | €1.932,18 | €46,13 | €11,05 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,05463 | 1,05073 | 1,07150 | 1,57667 | 1,01751 | €1.486,17 | €2.972,35 | €47,56 | €10,99 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 72,85843 | 72,87300 | 74,02416 | 108,92335 | 70,29381 | €14,13 | €28,25 | €0,45 | €-0,01 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €21,90 | €43,79 | €0,80 | €-0,44 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,10338 | 72,87300 | 74,15607 | 109,28955 | 70,99800 | €27,09 | €54,19 | €0,78 | €0,17 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 55,45791 | 54,28900 | 55,03797 | 82,90957 | 53,07120 | €1.100,97 | €2.201,93 | €0,00 | €46,41 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,05070 | 1,05073 | 1,06583 | 1,57080 | 1,02044 | €25,29 | €50,57 | €0,73 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 441,38284 | €23,94 | €47,87 | €1,07 | €-0,01 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00571 | €202,21 | €404,42 | €48,53 | €-11,58 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,43 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 73,10338 | 72,87300 | 74,15607 | 109,28955 | 70,99800 | €26,88 | €53,75 | €0,77 | €0,17 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 55,45791 | 54,28900 | 55,03797 | 82,90957 | 53,07120 | €1.092,08 | €2.184,17 | €0,00 | €46,04 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63364,29461 | 63203,20000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €0,14 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 441,38284 | €21,74 | €43,48 | €0,97 | €-0,01 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00571 | €202,21 | €404,42 | €48,53 | €-11,58 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,43 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 73,10338 | 72,87300 | 74,15607 | 109,28955 | 70,99800 | €26,88 | €53,75 | €0,77 | €0,17 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 55,45791 | 54,28900 | 55,03797 | 82,90957 | 53,07120 | €1.092,08 | €2.184,17 | €0,00 | €46,04 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63364,29461 | 63203,20000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €0,14 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 441,38284 | €21,74 | €43,48 | €0,97 | €-0,01 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00571 | €202,21 | €404,42 | €48,53 | €-11,58 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,43 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 73,10338 | 72,87300 | 74,15607 | 109,28955 | 70,99800 | €26,88 | €53,75 | €0,77 | €0,17 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 55,45791 | 54,28900 | 55,03797 | 82,90957 | 53,07120 | €1.092,08 | €2.184,17 | €0,00 | €46,04 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63364,29461 | 63203,20000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €0,14 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 441,38284 | €21,74 | €43,48 | €0,97 | €-0,01 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00582 | €207,06 | €414,11 | €49,69 | €-11,86 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00582 | €206,57 | €413,13 | €49,58 | €-11,83 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00626 | €208,49 | €416,97 | €50,04 | €-11,94 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00626 | €208,61 | €417,22 | €50,07 | €-11,95 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06998 | 0,06978 | 0,07118 | 0,10461 | 0,06696 | €1.428,07 | €2.856,13 | €49,20 | €8,00 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,68120 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,26 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63046,01827 | 63203,20000 | 64054,75457 | 94253,79732 | 60826,79843 | €59,43 | €118,86 | €1,90 | €-0,30 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06998 | 0,06978 | 0,07118 | 0,10461 | 0,06732 | €1.373,53 | €2.747,07 | €47,32 | €7,69 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,39612 | 54,28900 | 55,62490 | 81,32220 | 51,69281 | €13,60 | €27,19 | €0,61 | €0,05 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,05070 | 1,05073 | 1,06751 | 1,57080 | 1,01372 | €1.464,34 | €2.928,68 | €46,86 | €-0,08 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 465,15695 | 462,08000 | 476,12662 | 695,40964 | 441,02368 | €899,45 | €1.798,91 | €42,42 | €11,90 |
| Combo Trend | SOL | SHORT | Combo Trend | 60m | 2,0x | 72,85843 | 72,87300 | 74,02416 | 108,92335 | 70,29381 | €23,66 | €47,32 | €0,76 | €-0,01 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00582 | €206,55 | €413,11 | €49,57 | €-11,83 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive — madre | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07028 | 0,06978 | 0,07026 | 0,10506 | 0,06825 | €37,75 | €75,50 | €0,00 | €0,53 |
| Combo Adaptive — madre | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,25915 | 54,28900 | 55,30803 | 81,11742 | 52,16137 | €1.263,54 | €2.527,08 | €48,85 | €-1,39 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €24,23 | €48,47 | €0,89 | €-0,48 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06986 | 0,06978 | 0,07086 | 0,10443 | 0,06784 | €45,11 | €90,23 | €1,30 | €0,10 |
| Combo Adaptive — MFE Trail esistente | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 55,41391 | 54,28900 | 54,99794 | 82,84380 | 52,95915 | €1.083,24 | €2.166,47 | €0,00 | €43,98 |
| Combo Adaptive — MFE Trail esistente | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 465,15695 | 462,08000 | 465,15695 | 695,40964 | 445,41154 | €1.025,91 | €2.051,82 | €0,00 | €13,57 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive — Quality7 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,28900 | 55,99251 | 81,94549 | 52,45408 | €1.166,31 | €2.332,62 | €50,19 | €22,30 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00571 | €208,78 | €417,57 | €50,11 | €-11,96 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €12,97 | €25,95 | €0,47 | €-0,26 |
| Combo Adaptive — parziale 1R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,05724 | 1,05073 | 1,07246 | 1,58057 | 1,02679 | €204,10 | €408,19 | €5,88 | €2,51 |
| Combo Adaptive — parziale 1R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,28900 | 55,99251 | 81,94549 | 52,45408 | €1.130,49 | €2.260,99 | €48,65 | €21,62 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06986 | 0,06978 | 0,07086 | 0,10443 | 0,06784 | €18,68 | €37,37 | €0,54 | €0,04 |
| Combo Adaptive — parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 472,36551 | 462,08000 | 469,20611 | 706,18643 | 450,14836 | €177,47 | €354,93 | €0,00 | €7,73 |
| Combo Adaptive — parziale 1R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 72,93441 | 72,87300 | 73,98467 | 109,03694 | 70,83390 | €36,23 | €72,47 | €1,04 | €0,06 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 488,51228 | 462,08000 | 467,85888 | 730,32586 | 454,08996 | €8,17 | €16,35 | €0,00 | €0,88 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,28900 | 55,99251 | 81,94549 | 51,27460 | €1.151,04 | €2.302,07 | €49,54 | €22,01 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06997 | 0,06978 | 0,07097 | 0,10460 | 0,06694 | €32,83 | €65,65 | €0,95 | €0,17 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,05070 | 1,05073 | 1,06583 | 1,57080 | 1,00531 | €52,33 | €104,66 | €1,51 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 73,35633 | 72,87300 | 74,41266 | 109,66771 | 70,18733 | €1.670,32 | €3.340,64 | €48,11 | €22,01 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,68079 | 0,68120 | 0,69075 | 1,01778 | 0,65092 | €13,80 | €27,59 | €0,40 | €-0,02 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Combo Adaptive — target pieno 3R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 55,41391 | 54,28900 | 54,99794 | 82,84380 | 51,73176 | €21,07 | €42,14 | €0,00 | €0,86 |
| Combo Adaptive — target pieno 3R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00461 | 0,00447 | 0,00405 | 0,00233 | 0,00626 | €203,43 | €406,87 | €48,82 | €-11,65 |
| Combo Adaptive — target pieno 3R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,05070 | 1,05073 | 1,06583 | 1,57080 | 1,00531 | €26,10 | €52,21 | €0,75 | €-0,00 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 63620,87328 | 63203,20000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.147,21 | €3.441,62 | €49,56 | €22,59 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63747,34798 | 63203,20000 | 63405,98497 | 84677,72723 | 62115,41587 | €1.299,56 | €3.898,68 | €0,00 | €33,28 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63318,66373 | 63203,20000 | 64635,54187 | 94661,40228 | 59631,40456 | €1.196,13 | €2.392,26 | €49,75 | €4,36 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63620,87328 | 63203,20000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.158,94 | €3.476,83 | €50,07 | €22,83 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 72,83343 | 72,87300 | 73,94273 | 96,74707 | 70,61483 | €1.091,78 | €3.275,34 | €49,89 | €-1,78 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 72,87300 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €6,77 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 73,97120 | 72,87300 | 73,43702 | 98,25841 | 71,98791 | €1.254,69 | €3.764,07 | €0,00 | €55,88 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 72,87300 | 74,19099 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €0,00 | €67,56 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 72,86257 | 72,87300 | 71,93778 | 48,93936 | 74,24975 | €1.300,18 | €3.900,53 | €49,51 | €0,56 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 72,83343 | 72,87300 | 73,94273 | 96,74707 | 70,61483 | €1.076,25 | €3.228,75 | €49,18 | €-1,75 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 72,87300 | 74,19099 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €0,00 | €61,93 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07036 | 0,06978 | 0,07026 | 0,09346 | 0,06821 | €1.101,76 | €3.305,29 | €0,00 | €27,06 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06975 | 0,06978 | 0,07071 | 0,09265 | 0,06782 | €1.220,11 | €3.660,32 | €50,47 | €-1,78 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06977 | 0,06978 | 0,06887 | 0,04686 | 0,07113 | €1.267,95 | €3.803,86 | €49,17 | €0,33 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €0,00 |
| Combo Adaptive — Side × Regime Guard | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63046,01827 | 63203,20000 | 63953,88094 | 94253,79732 | 61230,29295 | €1.798,90 | €3.597,79 | €51,81 | €-8,97 |
| Combo Adaptive — Side × Regime Guard | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 55,41391 | 54,28900 | 54,99794 | 82,84380 | 52,95915 | €1.138,77 | €2.277,53 | €0,00 | €46,23 |
| Combo Adaptive — Side × Regime Guard | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07010 | 0,06978 | 0,07111 | 0,10479 | 0,06808 | €13,69 | €27,39 | €0,39 | €0,12 |
| Combo Adaptive — Side × Regime Guard | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 72,93441 | 72,87300 | 73,98467 | 109,03694 | 70,83390 | €21,80 | €43,60 | €0,63 | €0,04 |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 441,38284 | €42,78 | €85,57 | €1,91 | €-0,02 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00447 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €42,12 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 54,28900 | 55,59343 | 76,08234 | 53,15302 | €471,26 | €1.413,79 | €0,00 | €73,74 |
| MAIN — Side × Regime Guard | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,06978 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €8,50 |
| MAIN — Side × Regime Guard | ZEC | SHORT | Confluenza trend | 240m | 3,0x | 469,12616 | 462,08000 | 492,16341 | 623,15591 | 423,05164 | €346,80 | €1.040,39 | €51,09 | €15,63 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00471 | 0,00447 | 0,00415 | 0,00316 | 0,00584 | €143,54 | €430,62 | €51,67 | €-21,68 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend — Side × Regime Guard | ZEC | SHORT | Combo Trend | 60m | 2,0x | 477,71444 | 462,08000 | 470,54913 | 714,18308 | 449,83512 | €19,75 | €39,50 | €0,00 | €1,29 |
| Combo Trend — Side × Regime Guard | BTC | SHORT | Combo Trend | 60m | 2,0x | 63620,87328 | 63203,20000 | 64638,80725 | 95113,20555 | 61381,41854 | €1.578,90 | €3.157,81 | €50,52 | €20,73 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,06427 | 1,05073 | 1,06170 | 1,59108 | 1,02680 | €32,70 | €65,39 | €0,00 | €0,83 |
| Combo Trend — Side × Regime Guard | SOL | SHORT | Combo Trend | 60m | 2,0x | 72,83343 | 72,87300 | 74,06598 | 108,88598 | 70,12181 | €45,02 | €90,04 | €1,52 | €-0,05 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06998 | 0,06978 | 0,07118 | 0,10461 | 0,06732 | €1.439,06 | €2.878,12 | €49,58 | €8,06 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,97120 | 72,87300 | 73,55885 | 98,25841 | 71,73999 | €36,55 | €109,64 | €0,00 | €1,63 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63046,01827 | 63203,20000 | 63953,88094 | 83746,12761 | 61230,29295 | €1.127,91 | €3.383,73 | €48,73 | €-8,44 |
| Bilanciata V3 · LONG only | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 54,50310 | 54,28900 | 55,59912 | 72,39828 | 52,31106 | €9,00 | €26,99 | €0,54 | €0,11 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €22,23 | €44,47 | €0,81 | €-0,44 |
| Scanner Bottom5 Short Profit Lock V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,10338 | 72,87300 | 74,15607 | 109,28955 | 70,99800 | €27,51 | €55,02 | €0,79 | €0,17 |
| Scanner Bottom5 Short Profit Lock V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 55,45791 | 54,28900 | 55,03797 | 82,90957 | 53,07120 | €1.117,89 | €2.235,78 | €0,00 | €47,12 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,05070 | 1,05073 | 1,06583 | 1,57080 | 1,02044 | €25,67 | €51,35 | €0,74 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 461,98758 | 462,08000 | 472,28995 | 690,67144 | 441,38284 | €24,30 | €48,61 | €1,08 | €-0,01 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €15,45 | €30,90 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68120 | 0,68682 | 1,00837 | 0,64984 | €1.350,73 | €2.701,46 | €49,38 | €-26,85 |
| Scanner Bottom5 Short Mfe Trail V1 | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,10338 | 72,87300 | 74,15607 | 109,28955 | 70,99800 | €15,32 | €30,65 | €0,44 | €0,10 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 72,87300 | 73,43702 | 98,25841 | 71,80197 | €1.442,22 | €4.326,65 | €0,00 | €64,23 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05948 | 1,05073 | 1,05816 | 1,40734 | 1,02981 | €1.444,58 | €4.333,74 | €0,00 | €35,78 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,68319 | 0,68120 | 0,68319 | 0,90750 | 0,65893 | €87,71 | €263,14 | €0,00 | €0,77 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,45791 | 54,28900 | 54,90855 | 73,66659 | 53,13750 | €1.027,84 | €3.083,51 | €0,00 | €64,99 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00469 | 0,00447 | 0,00412 | 0,00315 | 0,00609 | €8,36 | €25,09 | €3,01 | €-1,14 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 461,98758 | 462,08000 | 470,00054 | 613,67351 | 441,95520 | €1.003,60 | €3.010,80 | €52,22 | €-0,60 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 72,87300 | 73,18636 | 97,21588 | 71,38347 | €8,38 | €25,15 | €0,00 | €0,11 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05073 | 1,05690 | 1,40391 | 1,03322 | €9,61 | €28,84 | €0,00 | €0,17 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06831 | €1.395,23 | €4.185,70 | €48,76 | €9,34 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,45791 | 54,28900 | 54,90855 | 73,66659 | 53,60158 | €991,38 | €2.974,15 | €0,00 | €62,69 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 465,14695 | 462,08000 | 465,14695 | 617,87020 | 449,59978 | €85,39 | €256,18 | €0,00 | €1,69 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 72,87300 | 73,43702 | 98,25841 | 72,23582 | €21,56 | €64,67 | €0,00 | €0,96 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,06424 | 1,05073 | 1,05818 | 1,41366 | 1,04040 | €82,60 | €247,81 | €0,00 | €3,15 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63203,20000 | 63752,13368 | 83746,12761 | 61633,78746 | €68,64 | €205,91 | €2,31 | €-0,51 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06831 | €1.410,51 | €4.231,54 | €49,29 | €9,44 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,45791 | 54,28900 | 54,90855 | 73,66659 | 53,60158 | €1.024,40 | €3.073,19 | €0,00 | €64,77 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 465,14695 | 462,08000 | 465,14695 | 617,87020 | 449,59978 | €1.035,29 | €3.105,87 | €0,00 | €20,48 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 72,87300 | 73,43702 | 98,25841 | 71,80197 | €78,41 | €235,23 | €0,00 | €3,49 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63203,20000 | 63752,13368 | 83746,12761 | 61280,72976 | €90,53 | €271,58 | €3,04 | €-0,68 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05948 | 1,05073 | 1,05816 | 1,40734 | 1,02981 | €1.431,80 | €4.295,40 | €0,00 | €35,47 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,68319 | 0,68120 | 0,68319 | 0,90750 | 0,65893 | €8,84 | €26,52 | €0,00 | €0,08 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,06978 | 0,07075 | 0,09290 | 0,06790 | €1.418,23 | €4.254,70 | €49,56 | €9,49 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,45791 | 54,28900 | 54,90855 | 73,66659 | 53,13750 | €988,79 | €2.966,37 | €0,00 | €62,52 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 461,98758 | 462,08000 | 470,00054 | 613,67351 | 441,95520 | €992,71 | €2.978,13 | €51,65 | €-0,60 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | NEAR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,66900 | 1,66900 | 1,69806 | 2,21699 | 1,61088 | €52,00 | €156,00 | €2,72 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,07018 | 0,06978 | 0,06997 | 0,09322 | 0,06854 | €1.466,24 | €4.398,72 | €0,00 | €24,82 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32093 | 54,28900 | 54,53677 | 73,48464 | 53,43961 | €40,51 | €121,52 | €0,00 | €2,27 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 465,73683 | 462,08000 | 463,80129 | 618,65376 | 450,25245 | €14,62 | €43,86 | €0,00 | €0,34 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 72,85843 | 72,87300 | 73,67444 | 96,78028 | 71,22640 | €1.542,92 | €4.628,76 | €51,84 | €-0,93 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00469 | 0,00447 | 0,00412 | 0,00315 | 0,00581 | €137,31 | €411,94 | €49,43 | €-18,68 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00469 | 0,00447 | 0,00412 | 0,00315 | 0,00581 | €141,34 | €424,02 | €50,88 | €-19,22 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 72,87300 | 73,43702 | 98,25841 | 72,23582 | €1.460,75 | €4.382,26 | €0,00 | €65,06 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63203,20000 | 63752,13368 | 83746,12761 | 61633,78746 | €49,42 | €148,27 | €1,66 | €-0,37 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,45791 | 54,28900 | 54,90855 | 73,66659 | 53,60158 | €1.028,10 | €3.084,31 | €0,00 | €65,01 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 465,14695 | 462,08000 | 465,14695 | 617,87020 | 449,59978 | €75,42 | €226,25 | €0,00 | €1,49 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00469 | 0,00447 | 0,00412 | 0,00315 | 0,00609 | €135,28 | €405,85 | €48,70 | €-18,40 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 461,48423 | €1,73 | 1,95 | TARGET |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 461,48423 | €1,70 | 1,95 | TARGET |
| Scanner Bottom20 Short | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 461,48423 | €1,69 | 1,95 | TARGET |
| Scanner Bottom15 Short | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 461,48423 | €1,69 | 1,95 | TARGET |
| Scanner Bottom10 Short | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 461,48423 | €1,69 | 1,95 | TARGET |
| Forza relativa 1H V1 | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 459,24865 | €101,97 | 2,15 | TARGET |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | 2026-07-28T13:53:47+00:00 | 1,04603 | €121,32 | 2,43 | TARGET |
| Benchmark Donchian breakout 1H | XRP | SHORT | 2026-07-28T13:53:47+00:00 | 1,04603 | €129,11 | 2,43 | TARGET |
| Combo Mean Reversion | BTC | LONG | 2026-07-28T13:53:47+00:00 | 62994,97628 | €-53,64 | -1,12 | STOP |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | 2026-07-28T13:53:47+00:00 | 461,48423 | €3,12 | 1,95 | TARGET |
| Btc Bollinger 1H | BTC | LONG | 2026-07-28T13:53:47+00:00 | 62994,97628 | €-57,15 | -1,12 | STOP |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | 2026-07-28T13:53:47+00:00 | 62994,97628 | €-53,46 | -1,12 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 32/30 | 22/30 | 0,98 | 3,28 | -0,01R | €16,79 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 13/30 | 9/30 | 0,79 | 5,00 | -0,16R | €37,32 | 1,14% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 18/30 | 22/30 | 0,69 | 1,74 | -0,24R | €12,35 | 1,72% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 18/30 | 22/30 | 0,69 | 1,57 | -0,24R | €8,43 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 24/30 | 27/30 | 0,64 | 0,80 | -0,27R | €-4,20 | 3,56% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 7/30 | 7/30 | 0,48 | 0,00 | -0,39R | €-37,10 | 2,92% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 5/30 | 7/30 | 1,28 | 1,03 | 0,17R | €0,61 | 2,15% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 14/30 | 14/30 | 1,38 | 4,59 | 0,23R | €16,93 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 26/30 | 22/30 | 0,82 | 0,63 | -0,13R | €-8,46 | 2,93% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 6/30 | 6/30 | 0,48 | 0,00 | -0,45R | €-40,38 | 2,42% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 24/30 | 26/30 | 0,97 | 1,45 | -0,02R | €6,79 | 3,57% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 41/30 | 43/30 | 1,01 | 1,62 | 0,01R | €7,99 | 2,51% | COERENTE + | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 11/30 | 14/30 | 1,00 | 0,97 | -0,00R | €-0,67 | 2,46% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 38/30 | 31/30 | 0,82 | 1,67 | -0,12R | €10,72 | 2,70% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 41/30 | 26/30 | 0,83 | 0,96 | -0,11R | €-0,70 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 20/30 | 11/30 | 0,78 | 2,20 | -0,14R | €20,62 | 1,99% | DIVERGENTE | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 78/30 | 26/30 | 1,04 | 0,67 | 0,03R | €-13,46 | 6,36% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 9/30 | 0,00 | 3,00 | 0,00R | €37,20 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 12/30 | 0,00 | 1,53 | 0,00R | €14,40 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 12/30 | 7/30 | 0,24 | 0,12 | -0,63R | €-6,34 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 13/30 | 10/30 | 0,40 | 0,27 | -0,39R | €-4,83 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 205/30 | 60/30 | 1,08 | 1,33 | 0,05R | €6,03 | 3,56% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 17/30 | 0,00 | 0,52 | 0,00R | €-16,53 | 3,70% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 54/30 | 36/30 | 1,45 | 1,24 | 0,26R | €4,83 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 99/30 | 55/30 | 1,14 | 1,52 | 0,08R | €10,76 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 23/30 | 14/30 | 0,73 | 1,16 | -0,19R | €3,20 | 1,46% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 28/30 | 25/30 | 1,46 | 0,99 | 0,23R | €-0,14 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 28/30 | 24/30 | 1,45 | 1,47 | 0,22R | €6,53 | 1,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 95/30 | 60/30 | 1,19 | 1,35 | 0,10R | €6,93 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 124/30 | 59/30 | 1,02 | 1,25 | 0,01R | €4,53 | 2,15% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 27/30 | 0,00 | 2,63 | 0,00R | €21,96 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 23/30 | 0,00 | 1,87 | 0,00R | €15,68 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 12/30 | 0,00 | 1,75 | 0,00R | €18,25 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 83/30 | 64/30 | 1,11 | 1,59 | 0,06R | €9,89 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 118/30 | 65/30 | 0,99 | 1,05 | -0,01R | €0,96 | 2,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 15/30 | 15/30 | 0,62 | 0,93 | -0,26R | €-1,52 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 161/30 | 92/30 | 1,04 | 1,10 | 0,02R | €2,00 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 98/30 | 58/30 | 1,07 | 1,40 | 0,04R | €7,30 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 48/30 | 49/30 | 1,06 | 0,93 | 0,04R | €-1,56 | 3,21% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 48/30 | 44/30 | 1,06 | 0,86 | 0,04R | €-3,24 | 2,86% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 63/30 | 52/30 | 0,99 | 0,70 | -0,00R | €-7,54 | 5,22% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 10/30 | 0,00 | 2,84 | 0,00R | €29,80 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 18/30 | 0,00 | 3,42 | 0,00R | €22,03 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 99/30 | 61/30 | 1,04 | 0,90 | 0,02R | €-2,20 | 2,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 32/30 | 0,00 | 1,15 | 0,00R | €2,85 | 3,13% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 48/30 | 0,00 | 1,32 | 0,00R | €4,17 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 19/30 | 0,00 | 1,16 | 0,00R | €3,75 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 115/30 | 66/30 | 0,93 | 0,98 | -0,04R | €-0,35 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 63/30 | 21/30 | 0,95 | 0,96 | -0,04R | €-1,11 | 3,68% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 67/30 | 48/30 | 1,17 | 0,76 | 0,09R | €-6,63 | 5,69% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 4/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 5/30 | 4/30 | 3,94 | 2,94 | 0,67R | €27,74 | 0,70% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 6/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,07% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 5/30 | 6/30 | 1,13 | 0,59 | 0,09R | €-14,69 | 1,56% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 151/30 | 30/30 | 1,19 | 1,44 | 0,12R | €6,22 | 1,77% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 54/30 | 17/30 | 0,96 | 0,98 | -0,02R | €-0,29 | 2,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 121/30 | 41/30 | 1,15 | 0,48 | 0,09R | €-12,75 | 5,33% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 92/30 | 30/30 | 1,04 | 0,53 | 0,03R | €-10,48 | 3,32% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 11/30 | 11/30 | 0,80 | 0,71 | -0,14R | €-7,09 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 11/30 | 11/30 | 0,80 | 0,31 | -0,14R | €-18,43 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 28/30 | 22/30 | 1,38 | 1,12 | 0,21R | €1,70 | 1,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 43/30 | 21/30 | 0,59 | 0,79 | -0,32R | €-4,56 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 44/30 | 30/30 | 0,66 | 1,23 | -0,27R | €4,04 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 22/30 | 0,00 | 2,35 | 0,00R | €14,36 | 1,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 44/30 | 15/30 | 0,66 | 0,74 | -0,27R | €-4,83 | 1,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 26/30 | 20/30 | 0,95 | 0,76 | -0,03R | €-8,37 | 3,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 91/30 | 46/30 | 1,41 | 0,87 | 0,24R | €-3,18 | 3,71% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 116/30 | 49/30 | 1,01 | 0,81 | 0,01R | €-6,32 | 7,02% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 21/30 | 0,00 | 1,33 | 0,00R | €5,38 | 1,73% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 3/30 | 3/30 | 0,00 | 0,00 | -1,12R | €-55,32 | 1,88% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 4/30 | 5/30 | 1,68 | 2,64 | 0,38R | €18,76 | 1,08% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 6/30 | 8/30 | 1,11 | 1,55 | 0,06R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 74/30 | 34/30 | 0,81 | 1,67 | -0,15R | €17,01 | 3,09% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 6/30 | 3/30 | 1,13 | ∞ | 0,09R | €96,79 | 1,09% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 121/30 | 34/30 | 1,01 | 0,81 | 0,01R | €-4,72 | 3,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 6/30 | 6/30 | 0,34 | 0,08 | -0,61R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 2/30 | 2/30 | 1,21 | 0,28 | 0,12R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 5/30 | 5/30 | 0,42 | 0,42 | -0,52R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 6/30 | 8/30 | 0,34 | 0,16 | -0,61R | €-34,02 | 2,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-52,87 | 1,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 11/30 | 1,75 | 0,52 | 0,41R | €-14,59 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 50/30 | 21/30 | 0,88 | 0,74 | -0,08R | €-9,56 | 3,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 21/30 | 0,00 | 0,67 | 0,00R | €-9,13 | 3,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 17/30 | 0,00 | 0,60 | 0,00R | €-15,49 | 3,84% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 16/30 | 0,00 | 0,62 | 0,00R | €-12,64 | 2,89% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 50/30 | 52/30 | 0,80 | 0,60 | -0,14R | €-7,10 | 4,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 45/30 | 18/30 | 0,84 | 0,66 | -0,11R | €-13,39 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 40/30 | 20/30 | 0,78 | 0,69 | -0,17R | €-11,41 | 3,98% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 39/30 | 26/30 | 0,87 | 0,49 | -0,09R | €-22,70 | 6,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 50/30 | 18/30 | 0,80 | 0,66 | -0,14R | €-13,61 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 151/30 | 38/30 | 0,96 | 0,71 | -0,02R | €-8,24 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 56/30 | 45/30 | 1,40 | 1,02 | 0,24R | €0,50 | 5,10% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 17/30 | 10/30 | 0,79 | 0,59 | -0,15R | €-11,26 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 17/30 | 10/30 | 0,79 | 0,59 | -0,15R | €-11,26 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 17/30 | 10/30 | 0,79 | 0,59 | -0,15R | €-11,26 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 60/30 | 33/30 | 1,04 | 0,79 | 0,02R | €-4,70 | 5,48% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 12/30 | 10/30 | 2,03 | 1,04 | 0,46R | €0,59 | 1,38% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 11/30 | 9/30 | 1,82 | 1,10 | 0,40R | €1,76 | 1,53% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 21/30 | 18/30 | 1,26 | 0,41 | 0,16R | €-19,55 | 5,45% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 22/30 | 18/30 | 1,16 | 0,41 | 0,10R | €-19,55 | 5,45% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 22/30 | 18/30 | 1,16 | 0,41 | 0,10R | €-19,55 | 5,45% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 89/30 | 39/30 | 1,39 | 1,34 | 0,23R | €7,29 | 3,38% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 23/30 | 10/30 | 0,68 | 0,87 | -0,22R | €-3,13 | 2,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 45/30 | 19/30 | 0,97 | 0,77 | -0,02R | €-6,43 | 3,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 37/30 | 33/30 | 1,22 | 0,65 | 0,13R | €-9,22 | 3,93% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 36/30 | 17/30 | 1,21 | 0,84 | 0,13R | €-4,99 | 3,57% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 42/30 | 40/30 | 1,20 | 0,55 | 0,12R | €-12,03 | 5,08% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 41/30 | 23/30 | 1,14 | 0,64 | 0,08R | €-11,07 | 3,65% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 52/30 | 32/30 | 1,08 | 0,50 | 0,05R | €-11,10 | 4,44% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 38/30 | 27/30 | 1,13 | 0,92 | 0,09R | €-2,00 | 4,14% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 38/30 | 23/30 | 1,13 | 0,93 | 0,09R | €-2,09 | 3,83% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 102/30 | 48/30 | 1,33 | 1,38 | 0,19R | €8,67 | 4,23% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 7/30 | 6/30 | 0,68 | 0,29 | -0,25R | €-27,47 | 2,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 4/30 | 4/30 | 0,71 | 0,41 | -0,17R | €-24,69 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 5/30 | 3/30 | 0,42 | 21,53 | -0,52R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 6/30 | 5/30 | 0,85 | 0,86 | -0,11R | €-4,58 | 1,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-51,84 | 1,13% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06978**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 25.1 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63203.2 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation, volume_valid**
- High **0.06971**; close **0.06955**; wick alta **34.8%**; volume **x6.02**

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
- Confidenza: **88,30%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -1.91%, 82% sotto -1%.
- BTC trend score: **-2,00**; ADX: **21,75**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-1,91%**; dispersione: **8,09%**

- Aperti in questo ciclo: **25**
- Chiusi in questo ciclo: **24**
- Posizioni research aperte: **500**
- Trade research chiusi: **4642**
- Eventi di mercato indipendenti chiusi: **1023**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **20363**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 13 | 32 | 32 | 34,38% | 0,98 | -0,01R | €-3,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 11 | 13 | 13 | 30,77% | 0,79 | -0,16R | €-20,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 0 | 18 | 18 | 27,78% | 0,69 | -0,24R | €-42,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 0 | 18 | 18 | 27,78% | 0,69 | -0,24R | €-42,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 1 | 24 | 24 | 25,00% | 0,64 | -0,27R | €-64,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 1 | 7 | 7 | 14,29% | 0,48 | -0,39R | €-27,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 5 | 5 | 40,00% | 1,28 | 0,17R | €8,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 1 | 14 | 14 | 42,86% | 1,38 | 0,23R | €31,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 1 | 26 | 26 | 30,77% | 0,82 | -0,13R | €-34,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 1 | 24 | 24 | 33,33% | 0,97 | -0,02R | €-4,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 10 | 41 | 41 | 41,46% | 1,01 | 0,01R | €3,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 0 | 11 | 11 | 36,36% | 1,00 | -0,00R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 11 | 38 | 38 | 28,95% | 0,82 | -0,12R | €-46,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 12 | 41 | 41 | 29,27% | 0,83 | -0,11R | €-46,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 10 | 20 | 20 | 25,00% | 0,78 | -0,14R | €-28,38 |
| MAIN | 16 | 78 | 78 | 34,62% | 1,04 | 0,03R | €19,94 |
| RSI_EXTREME_LONG_15M | 0 | 12 | 12 | 25,00% | 0,24 | -0,63R | €-75,99 |
| RSI_EXTREME_SHORT_15M | 0 | 13 | 13 | 30,77% | 0,40 | -0,39R | €-50,12 |
| Bilanciata 1H V1 | 16 | 205 | 205 | 35,12% | 1,08 | 0,05R | €99,82 |
| Bilanciata 1H V2 | 5 | 61 | 54 | 42,62% | 1,45 | 0,26R | €156,65 |
| Bilanciata 1H V3 Filtered | 16 | 99 | 99 | 36,36% | 1,14 | 0,08R | €84,08 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 13 | 23 | 23 | 26,09% | 0,73 | -0,19R | €-43,77 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 28 | 28 | 50,00% | 1,46 | 0,23R | €64,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 2 | 28 | 28 | 50,00% | 1,45 | 0,22R | €62,44 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 2 | 95 | 95 | 45,26% | 1,19 | 0,10R | €96,78 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 10 | 124 | 124 | 41,13% | 1,02 | 0,01R | €14,73 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 11 | 83 | 83 | 44,58% | 1,11 | 0,06R | €52,15 |
| SHADOW_1H_FAST_TP2_V1 | 12 | 118 | 118 | 33,90% | 0,99 | -0,01R | €-7,28 |
| Rapida 1H V2 | 0 | 17 | 15 | 29,41% | 0,62 | -0,26R | €-43,50 |
| Rapida 1H V3 Filtered | 12 | 161 | 161 | 41,61% | 1,04 | 0,02R | €32,53 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 13 | 98 | 98 | 42,86% | 1,07 | 0,04R | €37,05 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 0 | 48 | 48 | 43,75% | 1,06 | 0,04R | €18,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 0 | 48 | 48 | 43,75% | 1,06 | 0,04R | €18,29 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 1 | 63 | 63 | 41,27% | 0,99 | -0,00R | €-2,63 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 2 | 99 | 99 | 42,42% | 1,04 | 0,02R | €21,82 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 11 | 115 | 115 | 39,13% | 0,93 | -0,04R | €-49,56 |
| SHADOW_4H_WIDE | 25 | 63 | 63 | 25,40% | 0,95 | -0,04R | €-25,06 |
| SHADOW_BOLLINGER_MR_1H | 3 | 67 | 67 | 47,76% | 1,17 | 0,09R | €61,81 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,44 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 5 | 5 | 80,00% | 3,94 | 0,67R | €33,34 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 6 | 6 | 0,00% | 0,00 | -1,12R | €-67,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 5 | 5 | 40,00% | 1,13 | 0,09R | €4,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 16 | 151 | 151 | 37,75% | 1,19 | 0,12R | €175,84 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 2 | 54 | 54 | 31,48% | 0,96 | -0,02R | €-13,36 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 15 | 121 | 121 | 38,02% | 1,15 | 0,09R | €110,05 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 16 | 92 | 92 | 34,78% | 1,04 | 0,03R | €24,66 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 11 | 11 | 27,27% | 0,80 | -0,14R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 11 | 11 | 27,27% | 0,80 | -0,14R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 28 | 28 | 39,29% | 1,38 | 0,21R | €59,93 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 0 | 43 | 43 | 23,26% | 0,59 | -0,32R | €-137,20 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 3 | 44 | 44 | 18,18% | 0,66 | -0,27R | €-120,26 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 3 | 44 | 44 | 18,18% | 0,66 | -0,27R | €-120,26 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 26 | 26 | 42,31% | 0,95 | -0,03R | €-8,07 |
| SHADOW_COMBO_SCANNER | 2 | 91 | 91 | 38,46% | 1,41 | 0,24R | €214,41 |
| SHADOW_COMBO_TREND | 19 | 116 | 116 | 31,90% | 1,01 | 0,01R | €7,86 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,71 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 4 | 4 | 50,00% | 1,68 | 0,38R | €15,21 |
| SHADOW_DOGE_EMA_1H | 1 | 6 | 6 | 33,33% | 1,11 | 0,06R | €3,73 |
| SHADOW_DONCHIAN_1H | 10 | 74 | 74 | 25,68% | 0,81 | -0,15R | €-110,80 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 7 | 6 | 6 | 33,33% | 1,13 | 0,09R | €5,48 |
| SHADOW_EMA_TREND_1H | 19 | 121 | 121 | 31,40% | 1,01 | 0,01R | €8,09 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,67 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 5 | 5 | 20,00% | 0,42 | -0,52R | €-26,11 |
| SHADOW_ETH_EMA_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,55 |
| SHADOW_ETH_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_GLOBAL_PURE | 1 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 2 | 50 | 50 | 30,00% | 0,88 | -0,08R | €-41,98 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 2 | 50 | 50 | 28,00% | 0,80 | -0,14R | €-71,19 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 2 | 45 | 45 | 28,89% | 0,84 | -0,11R | €-48,29 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 3 | 40 | 40 | 20,00% | 0,78 | -0,17R | €-67,92 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 1 | 39 | 39 | 30,77% | 0,87 | -0,09R | €-34,83 |
| SHADOW_MASTER_ADAPTIVE_V1 | 2 | 50 | 50 | 28,00% | 0,80 | -0,14R | €-71,19 |
| Forza relativa 1H V1 | 17 | 151 | 151 | 30,46% | 0,96 | -0,02R | €-36,92 |
| Forza relativa 1H V2 | 7 | 61 | 56 | 39,34% | 1,40 | 0,24R | €148,74 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 13 | 17 | 17 | 29,41% | 0,79 | -0,15R | €-24,70 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 13 | 17 | 17 | 29,41% | 0,79 | -0,15R | €-24,70 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 13 | 17 | 17 | 29,41% | 0,79 | -0,15R | €-24,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 11 | 60 | 60 | 33,33% | 1,04 | 0,02R | €14,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 10 | 12 | 12 | 58,33% | 2,03 | 0,46R | €55,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 10 | 11 | 11 | 54,55% | 1,82 | 0,40R | €43,83 |
| SHADOW_SCANNER_TOP10_LONG | 2 | 21 | 21 | 38,10% | 1,26 | 0,16R | €32,89 |
| SHADOW_SCANNER_TOP15_LONG | 2 | 22 | 22 | 36,36% | 1,16 | 0,10R | €21,78 |
| SHADOW_SCANNER_TOP20_LONG | 2 | 22 | 22 | 36,36% | 1,16 | 0,10R | €21,78 |
| SHADOW_SCANNER_TOP5_BTC | 1 | 89 | 89 | 37,08% | 1,39 | 0,23R | €201,49 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 23 | 23 | 21,74% | 0,68 | -0,22R | €-51,58 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 1 | 45 | 45 | 28,89% | 0,97 | -0,02R | €-10,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 0 | 37 | 37 | 35,14% | 1,22 | 0,13R | €47,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 0 | 36 | 36 | 33,33% | 1,21 | 0,13R | €45,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 0 | 42 | 42 | 35,71% | 1,20 | 0,12R | €49,29 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 0 | 41 | 41 | 31,71% | 1,14 | 0,08R | €34,30 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 1 | 52 | 52 | 32,69% | 1,08 | 0,05R | €24,78 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 4 | 38 | 38 | 26,32% | 1,13 | 0,09R | €33,62 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 4 | 38 | 38 | 26,32% | 1,13 | 0,09R | €33,62 |
| SHADOW_SCANNER_TOP5_LONG | 2 | 102 | 102 | 39,22% | 1,33 | 0,19R | €195,66 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,57 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 4 | 4 | 50,00% | 0,71 | -0,17R | €-6,62 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 5 | 5 | 20,00% | 0,42 | -0,52R | €-25,96 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,46 |
| SHADOW_SOL_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,12 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 11 | 11 | 11 | 36,36% | 1,16 | 0,10R | €10,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 1,27 | 0,17R | €20,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 11 | 10 | 10 | 30,00% | 0,69 | -0,24R | €-23,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,38R | €23,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,16 | 0,11R | €10,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,16 | 0,11R | €10,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 1 | 9 | 9 | 44,44% | 1,43 | 0,26R | €23,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 9 | 9 | 44,44% | 1,39 | 0,24R | €21,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 5 | 5 | 60,00% | 2,86 | 0,76R | €38,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 9 | 15 | 15 | 53,33% | 1,13 | 0,06R | €8,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 1 | 9 | 9 | 44,44% | 1,39 | 0,24R | €21,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 6 | 6 | 50,00% | 1,91 | 0,47R | €28,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,30 | 0,19R | €13,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 10 | 12 | 12 | 25,00% | 0,84 | -0,09R | €-10,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 10 | 12 | 12 | 25,00% | 0,84 | -0,09R | €-10,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,31 | -0,62R | €-43,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 10 | 12 | 12 | 25,00% | 0,78 | -0,12R | €-15,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,38R | €23,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 6 | 6 | 16,67% | 0,48 | -0,45R | €-27,08 |
| MAIN | ALT_ROTATION_DOWN | 6 | 7 | 7 | 28,57% | 0,97 | -0,02R | €-1,41 |
| MAIN | ALT_ROTATION_UP | 2 | 10 | 10 | 10,00% | 0,22 | -0,72R | €-72,20 |
| MAIN | RANGE | 6 | 26 | 26 | 34,62% | 1,02 | 0,01R | €3,46 |
| MAIN | RANGE_HIGH_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_UP | 1 | 19 | 19 | 36,84% | 1,12 | 0,08R | €14,71 |
| MAIN | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,94 | -0,04R | €-2,34 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,05 | -0,86R | €-34,43 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 5 | 5 | 20,00% | 0,43 | -0,34R | €-17,24 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 11 | 21 | 21 | 28,57% | 0,91 | -0,06R | €-12,10 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 1 | 21 | 21 | 38,10% | 1,12 | 0,08R | €16,39 |
| Bilanciata 1H V1 | RANGE | 2 | 54 | 54 | 42,59% | 1,41 | 0,24R | €130,11 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 7,69% | 0,15 | -0,84R | €-109,02 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 0 | 33 | 33 | 39,39% | 1,29 | 0,17R | €56,83 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Bilanciata 1H V1 | TREND_UP | 0 | 48 | 48 | 37,50% | 1,23 | 0,14R | €66,63 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 2 | 11 | 9 | 36,36% | 1,04 | 0,02R | €2,70 |
| Bilanciata 1H V2 | RANGE | 3 | 29 | 27 | 41,38% | 1,36 | 0,21R | €61,60 |
| Bilanciata 1H V2 | TRANSITION | 0 | 21 | 18 | 47,62% | 1,88 | 0,44R | €92,35 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 11 | 18 | 18 | 33,33% | 1,08 | 0,05R | €8,87 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 2 | 8 | 8 | 25,00% | 0,61 | -0,32R | €-25,49 |
| Bilanciata 1H V3 Filtered | RANGE | 2 | 23 | 23 | 52,17% | 2,00 | 0,51R | €116,91 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 9 | 9 | 44,44% | 1,46 | 0,28R | €24,77 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 23 | 23 | 39,13% | 1,30 | 0,17R | €40,12 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 10 | 8 | 8 | 25,00% | 0,88 | -0,07R | €-5,41 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,50 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 0 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,91R | €19,09 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,25 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,72 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 16,67% | 0,36 | -0,44R | €-26,51 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 0,95 | -0,03R | €-2,21 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 6 | 6 | 83,33% | 7,11 | 1,06R | €63,32 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 5 | 5 | 40,00% | 0,89 | -0,07R | €-3,68 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 1 | 14 | 14 | 42,86% | 1,00 | -0,00R | €-0,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 4 | 4 | 50,00% | 1,41 | 0,21R | €8,41 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,55R | €-10,97 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 5 | 5 | 60,00% | 1,95 | 0,42R | €21,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,40 | -0,46R | €-82,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 15 | 15 | 46,67% | 1,16 | 0,09R | €13,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 34 | 34 | 58,82% | 2,17 | 0,45R | €153,60 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,55R | €-10,97 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 21 | 21 | 33,33% | 0,66 | -0,24R | €-51,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 8 | 39 | 39 | 28,21% | 0,62 | -0,25R | €-95,79 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,86 | -0,09R | €-13,18 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 35 | 35 | 54,29% | 1,68 | 0,31R | €109,88 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,38 | 0,19R | €3,82 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 6 | 6 | 83,33% | 6,30 | 1,01R | €60,52 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,20 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 21 | 21 | 28,57% | 0,55 | -0,34R | €-72,31 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 10 | 23 | 23 | 30,43% | 0,60 | -0,29R | €-66,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,92 | -0,05R | €-8,25 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 27 | 27 | 59,26% | 2,13 | 0,45R | €121,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,43R | €28,69 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 11 | 11 | 27,27% | 0,49 | -0,40R | €-43,48 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 10 | 35 | 35 | 22,86% | 0,64 | -0,25R | €-86,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 41,18% | 1,23 | 0,15R | €24,85 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 30 | 30 | 46,67% | 1,61 | 0,33R | €98,09 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,93 | -0,04R | €-1,33 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,39 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 6 | 6 | 83,33% | 8,41 | 1,41R | €84,61 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,20 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 21 | 21 | 19,05% | 0,43 | -0,50R | €-104,08 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,77 |
| Rapida 1H V2 | RANGE | 0 | 12 | 10 | 33,33% | 0,82 | -0,10R | €-12,29 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 10 | 37 | 37 | 27,03% | 0,56 | -0,30R | €-110,64 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 16 | 16 | 50,00% | 1,30 | 0,16R | €26,17 |
| Rapida 1H V3 Filtered | RANGE | 1 | 35 | 35 | 54,29% | 1,69 | 0,32R | €111,57 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 62,50% | 2,25 | 0,51R | €40,77 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,20 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 38 | 38 | 47,37% | 1,23 | 0,13R | €49,02 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 11 | 30 | 30 | 30,00% | 0,59 | -0,29R | €-88,48 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,91 | -0,06R | €-9,61 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 30 | 30 | 56,67% | 2,03 | 0,41R | €124,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,43R | €28,69 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,55R | €-10,97 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 15 | 15 | 33,33% | 0,66 | -0,24R | €-36,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 0,82 | -0,12R | €-15,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 16 | 16 | 62,50% | 2,40 | 0,54R | €86,58 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 11 | 11 | 36,36% | 0,74 | -0,18R | €-20,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 0,82 | -0,12R | €-15,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 16 | 16 | 62,50% | 2,40 | 0,54R | €86,58 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 36,36% | 0,74 | -0,18R | €-20,19 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 9 | 9 | 0,00% | 0,00 | -0,92R | €-82,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 0,95 | -0,03R | €-4,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 20 | 20 | 60,00% | 2,17 | 0,48R | €95,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 15 | 15 | 26,67% | 0,49 | -0,40R | €-60,35 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 28,57% | 0,56 | -0,31R | €-65,39 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,11 | 0,07R | €8,74 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 35 | 35 | 54,29% | 1,69 | 0,32R | €111,57 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,20 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 23 | 23 | 30,43% | 0,58 | -0,31R | €-71,03 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 10 | 36 | 36 | 27,78% | 0,58 | -0,28R | €-99,21 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,85 | -0,10R | €-14,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 34 | 34 | 52,94% | 1,60 | 0,28R | €96,70 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,45R | €43,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,20 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 21 | 21 | 28,57% | 0,54 | -0,35R | €-73,72 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 6 | 5 | 5 | 40,00% | 2,73 | 0,71R | €35,33 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_4H_WIDE | RANGE | 8 | 23 | 23 | 30,43% | 1,19 | 0,13R | €30,86 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 16 | 16 | 37,50% | 1,63 | 0,40R | €64,58 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 0,00% | 0,00 | -1,03R | €-72,07 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 3 | 13 | 13 | 46,15% | 0,69 | -0,18R | €-23,91 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 0,79 | -0,14R | €-11,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,67 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 16 | 16 | 56,25% | 1,67 | 0,32R | €50,98 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,75 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 11 | 20 | 20 | 30,00% | 0,91 | -0,06R | €-12,05 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 13 | 13 | 30,77% | 0,80 | -0,15R | €-18,85 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 2 | 42 | 42 | 42,86% | 1,37 | 0,22R | €94,39 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,62 | -0,29R | €-11,77 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 22 | 22 | 50,00% | 2,00 | 0,49R | €106,98 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 36 | 36 | 41,67% | 1,48 | 0,26R | €95,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 14,29% | 0,49 | -0,30R | €-20,95 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 1,02 | 0,01R | €1,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 15 | 15 | 60,00% | 2,92 | 0,78R | €117,34 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 12 | 12 | 8,33% | 0,21 | -0,64R | €-76,92 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 10 | 23 | 23 | 39,13% | 1,03 | 0,02R | €3,62 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 14 | 14 | 28,57% | 0,72 | -0,21R | €-29,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 2 | 30 | 30 | 50,00% | 1,83 | 0,44R | €132,86 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,62 | -0,29R | €-11,77 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 6 | 6 | 66,67% | 3,52 | 0,92R | €55,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 28 | 28 | 39,29% | 1,39 | 0,22R | €60,29 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 11 | 20 | 20 | 30,00% | 0,91 | -0,06R | €-12,05 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 1 | 11 | 11 | 36,36% | 1,02 | 0,01R | €1,26 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 2 | 30 | 30 | 50,00% | 1,83 | 0,44R | €132,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 5 | 5 | 60,00% | 2,65 | 0,72R | €36,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 15 | 15 | 13,33% | 0,34 | -0,52R | €-77,39 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 8 | 8 | 25,00% | 0,75 | -0,16R | €-13,19 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 8 | 8 | 25,00% | 0,75 | -0,16R | €-13,19 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 0,00% | 0,00 | -0,67R | €-33,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,22 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 13 | 13 | 69,23% | 4,32 | 1,05R | €137,01 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 4 | 4 | 25,00% | 0,63 | -0,29R | €-11,45 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 10 | 10 | 40,00% | 1,19 | 0,12R | €12,10 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 25 | 25 | 20,00% | 0,51 | -0,37R | €-93,43 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 9 | 9 | 33,33% | 1,60 | 0,36R | €32,58 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 1 | 9 | 9 | 33,33% | 1,60 | 0,36R | €32,58 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,54 | -0,26R | €-21,14 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 11 | 11 | 45,45% | 1,15 | 0,09R | €9,62 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 2 | 2 | 50,00% | 1,32 | 0,18R | €3,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 4 | 4 | 50,00% | 1,53 | 0,27R | €10,70 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 9 | 9 | 0,00% | 0,00 | -0,69R | €-62,20 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 1,02 | 0,02R | €1,43 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 19 | 19 | 57,89% | 2,89 | 0,82R | €155,76 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 15 | 15 | 46,67% | 1,60 | 0,34R | €50,68 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 27 | 27 | 40,74% | 1,60 | 0,33R | €89,86 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 9 | 14 | 14 | 21,43% | 0,66 | -0,23R | €-32,07 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 12 | 12 | 25,00% | 0,68 | -0,26R | €-30,82 |
| SHADOW_COMBO_TREND | RANGE | 3 | 31 | 31 | 38,71% | 1,29 | 0,19R | €58,86 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,76 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 17 | 17 | 47,06% | 2,04 | 0,52R | €88,27 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 27 | 27 | 33,33% | 1,04 | 0,03R | €6,90 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 18,18% | 0,50 | -0,38R | €-42,23 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,26 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -0,60R | €-12,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 7 | 12 | 12 | 16,67% | 0,45 | -0,49R | €-58,29 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 12,50% | 0,32 | -0,63R | €-50,42 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 20 | 20 | 30,00% | 0,99 | -0,01R | €-2,06 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 9 | 9 | 33,33% | 1,35 | 0,21R | €18,91 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 14 | 14 | 35,71% | 1,28 | 0,19R | €26,97 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 33,33% | 1,11 | 0,08R | €4,78 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 6 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 2,41R | €48,18 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 9 | 15 | 15 | 20,00% | 0,60 | -0,29R | €-42,81 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 12 | 12 | 16,67% | 0,41 | -0,53R | €-63,15 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 29 | 29 | 41,38% | 1,54 | 0,31R | €91,14 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 1,03 | 0,02R | €0,63 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 17 | 17 | 41,18% | 1,59 | 0,33R | €56,40 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 32 | 32 | 31,25% | 0,98 | -0,01R | €-3,92 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,87 | -0,09R | €-9,90 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,32 | -0,53R | €-42,06 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-23,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 1 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,96R | €58,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 19 | 19 | 10,53% | 0,25 | -0,64R | €-121,97 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,39 | -0,44R | €-30,95 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 13 | 13 | 61,54% | 3,11 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 21 | 21 | 9,52% | 0,22 | -0,68R | €-143,21 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,39 | -0,44R | €-30,95 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 1 | 13 | 13 | 61,54% | 3,11 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 21 | 21 | 9,52% | 0,22 | -0,68R | €-143,39 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 224,00 | 1,49R | €29,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,19 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 1 | 13 | 13 | 46,15% | 2,51 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 17 | 17 | 5,88% | 0,20 | -0,71R | €-120,76 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 16 | 16 | 62,50% | 3,25 | 0,86R | €137,25 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 17 | 17 | 5,88% | 0,12 | -0,83R | €-141,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,39 | -0,44R | €-30,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 1 | 13 | 13 | 61,54% | 3,11 | 0,83R | €107,61 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 21 | 21 | 9,52% | 0,22 | -0,68R | €-143,21 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 8 | 19 | 19 | 15,79% | 0,44 | -0,42R | €-80,46 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 19 | 19 | 26,32% | 0,73 | -0,21R | €-40,77 |
| Forza relativa 1H V1 | RANGE | 3 | 41 | 41 | 34,15% | 1,11 | 0,07R | €29,13 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 0 | 17 | 17 | 47,06% | 1,88 | 0,48R | €80,99 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Forza relativa 1H V1 | TREND_UP | 2 | 41 | 41 | 36,59% | 1,36 | 0,21R | €86,81 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 3 | 9 | 9 | 33,33% | 1,22 | 0,13R | €11,64 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 8 | 7 | 25,00% | 0,68 | -0,25R | €-19,89 |
| Forza relativa 1H V2 | RANGE | 1 | 13 | 13 | 61,54% | 3,40 | 0,95R | €123,51 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 0 | 13 | 11 | 38,46% | 1,31 | 0,20R | €25,87 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TREND_UP | 0 | 14 | 13 | 42,86% | 1,60 | 0,35R | €49,20 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 9 | 6 | 6 | 16,67% | 0,44 | -0,40R | €-24,18 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 9 | 6 | 6 | 16,67% | 0,44 | -0,40R | €-24,18 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 9 | 6 | 6 | 16,67% | 0,44 | -0,40R | €-24,18 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 7 | 9 | 9 | 44,44% | 1,77 | 0,37R | €33,49 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 21 | 21 | 33,33% | 0,88 | -0,09R | €-18,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 17 | 17 | 41,18% | 1,49 | 0,26R | €43,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 7 | 5 | 5 | 60,00% | 1,53 | 0,23R | €11,30 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 7 | 4 | 4 | 50,00% | 1,00 | -0,00R | €-0,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,89 | 0,45R | €9,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,90R | €56,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 1,94 | 0,32R | €9,60 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 16,67% | 0,36 | -0,57R | €-34,49 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,53 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 1,94 | 0,32R | €9,60 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,30 | -0,65R | €-45,60 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,53 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 1,94 | 0,32R | €9,60 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 7 | 7 | 14,29% | 0,30 | -0,65R | €-45,60 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,53 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 9 | 9 | 0,00% | 0,00 | -0,69R | €-62,20 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-9,09 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 19 | 19 | 57,89% | 3,31 | 0,88R | €166,71 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 13 | 13 | 46,15% | 1,79 | 0,45R | €58,04 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 26 | 26 | 38,46% | 1,47 | 0,27R | €69,15 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,03R | €-0,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,95 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 8 | 8 | 25,00% | 0,82 | -0,12R | €-9,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,64R | €-51,51 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 16,67% | 0,40 | -0,54R | €-32,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,41 | -0,45R | €-31,39 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,06 | -0,49R | €-39,01 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 5 | 5 | 20,00% | 0,53 | -0,38R | €-19,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,59R | €-41,38 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 5 | 5 | 20,00% | 0,53 | -0,38R | €-19,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,29 | -0,41R | €-37,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,69 | -0,21R | €-19,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,65R | €-52,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,69 | -0,21R | €-19,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 20,00% | 0,24 | -0,47R | €-47,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 16,67% | 0,40 | -0,54R | €-32,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 14 | 14 | 57,14% | 2,86 | 0,81R | €113,47 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 9 | 9 | 22,22% | 0,81 | -0,11R | €-10,01 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 22,22% | 0,78 | -0,19R | €-16,96 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 11 | 11 | 54,55% | 3,52 | 1,16R | €128,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 1 | 10 | 10 | 10,00% | 0,40 | -0,45R | €-45,34 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 22,22% | 0,78 | -0,19R | €-16,96 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 11 | 11 | 54,55% | 3,52 | 1,16R | €128,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 10 | 10 | 10,00% | 0,40 | -0,45R | €-45,34 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 10 | 10 | 10,00% | 0,27 | -0,53R | €-53,31 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 11 | 11 | 27,27% | 0,69 | -0,24R | €-26,69 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 20 | 20 | 60,00% | 3,28 | 0,82R | €164,58 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 35 | 35 | 42,86% | 1,54 | 0,29R | €102,79 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,05 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 0,24R | €2,38 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,38 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,05 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,55 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-28T14:08:54+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **777**
- Scenari virtuali ancora attivi: **15429**
- Gruppi in attesa dell'uscita originale: **347**
- Gruppi con originale chiuso ma Shadow ancora attive: **430**
- Confronti completati: **87672**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 2632 | 2697 | €-2,83 | 44,6% | 598 | 432 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 2610 | 2675 | +€8,17 | 50,3% | 807 | 2 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 2610 | 2675 | +€3,68 | 47,0% | 900 | 1 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 2610 | 2675 | €-2,19 | 39,7% | 345 | 649 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 2594 | 2659 | +€6,56 | 49,0% | 811 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 2583 | 2648 | +€4,43 | 47,8% | 816 | 40 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 2579 | 2644 | +€2,89 | 47,4% | 771 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 2559 | 2624 | +€7,09 | 44,7% | 652 | 67 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 2559 | 2624 | +€4,59 | 42,0% | 723 | 65 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 2539 | 2604 | +€5,20 | 44,3% | 623 | 95 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 2537 | 2602 | +€3,59 | 44,1% | 535 | 159 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 2528 | 2593 | +€1,75 | 41,8% | 458 | 310 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 2506 | 2571 | +€5,90 | 34,0% | 388 | 269 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2460 | 2525 | +€5,65 | 38,7% | 184 | 428 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 2460 | 2525 | €-1,82 | 33,7% | 302 | 544 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 2433 | 2498 | €-5,55 | 33,5% | 163 | 745 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 2408 | 2473 | €-2,81 | 31,3% | 265 | 599 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2403 | 2468 | €-8,01 | 32,7% | 466 | 492 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2369 | 2434 | €-7,17 | 29,4% | 218 | 643 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2318 | 2383 | €-14,05 | 23,4% | 217 | 746 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-28T14:08:59+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **87672**
- Valutazioni prodotte: **17179**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_MBV3_GB20_R100 | 45 | 0,266 | 0,269 | 0,023 | 71,1% | 87,8 | EARLY_SIGNAL |
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

Generato: 2026-07-28T14:09:58+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 21 | 95,45% | 1,35 | +€125,64 | +€5,98 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 21 | 95,45% | 1,17 | +€60,61 | +€2,89 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 16 | 100,00% | 1,43 | +€81,44 | +€5,09 | 0,91% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 16 | 100,00% | 1,31 | +€58,13 | +€3,63 | 0,91% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 8 | 100,00% | 0,72 | €-59,78 | €-7,47 | 1,08% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 6 | 100,00% | 0,00 | €-104,80 | €-17,47 | 1,05% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 13 | 92,86% | 0,83 | €-45,75 | €-3,52 | 2,13% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-28T14:08:40+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **23**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **143.26 R**
- Profitto virtuale mancato: **287.32 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 64 | 0 | 6610.40 |
| DOWN_20 | 64 | 0 | 13220.80 |
| DOWN_30 | 64 | 7 | 19915.14 |
| DOWN_40 | 64 | 13 | 25341.60 |
| UP_10 | 266 | 0 | 32170.32 |
| UP_20 | 266 | 0 | 64340.63 |
| UP_30 | 266 | 0 | 96510.95 |
| UP_40 | 266 | 130 | 115520.58 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-28T14:08:13+00:00

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

Generato: 2026-07-28T14:10:00+00:00

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

Generato: 2026-07-28T14:10:00+00:00

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

Generato: 2026-07-28T14:10:00+00:00

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

Generato: 2026-07-28T14:10:00+00:00

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
| 1 | SHADOW_COMBO_ADAPTIVE | BASELINE | 19.1 | E | 30 | 2.03 | 0.284 | 2.72 |
| 2 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 16.9 | E | 59 | 1.44 | 0.175 | 3.55 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 16.8 | E | 64 | 1.39 | 0.148 | 3.78 |
| 4 | SHADOW_1H_FAST_V3 | BASELINE | 16.6 | E | 92 | 1.23 | 0.094 | 5.36 |
| 5 | SHADOW_1H_BALANCED_V3 | BASELINE | 16.4 | E | 55 | 1.45 | 0.208 | 4.23 |
| 6 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 16.4 | E | 48 | 1.48 | 0.147 | 3.79 |
| 7 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 16.2 | E | 58 | 1.35 | 0.145 | 3.68 |
| 8 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 16.0 | E | 60 | 1.39 | 0.162 | 5.40 |
| 9 | SHADOW_DONCHIAN_1H | BASELINE | 15.7 | E | 34 | 1.53 | 0.293 | 8.55 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 13.6 | E | 66 | 1.16 | 0.070 | 4.74 |

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

Generato: 2026-07-28T14:10:00+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **UNKNOWN**
- Righe di performance: **568**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **269**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_BALANCED | shadow-1h-balanced | OBSERVING | 83.6 | 13 | 11.52 | 0.910 | 1.05 |
| 2 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | INSUFFICIENT | 83.2 | 8 | 99.00 | 1.327 | 0.00 |
| 3 | EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | momentum_breakout_v3_filtered | INSUFFICIENT | 82.7 | 7 | 89.25 | 1.080 | 0.07 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | momentum_breakout_v3_filtered | OBSERVING | 82.7 | 19 | 4.89 | 0.532 | 1.61 |
| 5 | SHADOW_1H_FAST_V3_CAP75_V1 | shadow-1h-fast-v3-cap75-v1 | OBSERVING | 82.3 | 12 | 3.82 | 0.547 | 1.14 |
| 6 | SHADOW_EMA_TREND_1H | shadow-ema-trend-1h | INSUFFICIENT | 82.2 | 7 | 12.43 | 0.800 | 0.38 |
| 7 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | shadow-combo-adaptive-side-regime-guard-v1 | INSUFFICIENT | 82.0 | 5 | 193.94 | 1.066 | 0.03 |
| 8 | EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | momentum_breakout_v3_filtered | INSUFFICIENT | 81.6 | 4 | 99.00 | 1.505 | 0.00 |
| 9 | SHADOW_1H_FAST_V3 | shadow-1h-fast-v3 | OBSERVING | 81.6 | 18 | 2.46 | 0.454 | 2.27 |
| 10 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | shadow-1h-fast-nohigh-cap75-v1 | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.950 | 0.00 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-28T14:10:00+00:00

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

Generato: 2026-07-28T14:08:40+00:00

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
