# Paper trading automatico KuCoin

Generato: 2026-08-13T21:14:40+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-13T21:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-13T21:05:31+00:00 | 2026-08-13T21:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-13T20:45:00+00:00 | 2026-08-13T20:45:00+00:00 | 6,5 min | 25,0 min | OK |
| 60m | 12 | 2026-08-13T20:00:00+00:00 | 2026-08-13T20:00:00+00:00 | 6,5 min | 45,0 min | OK |
| 240m | 12 | 2026-08-13T16:00:00+00:00 | 2026-08-13T16:00:00+00:00 | 1,11 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive — target pieno 3R | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — parziale 1R | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | SKHYNIX | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | APR | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | SHORT | -8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -7,32 | 6,00 | 0,00 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -7,25 | 6,00 | 0,00 | STALE_CANDLE | 1,11 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -5,68 | 6,00 | 0,32 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,39 | 6,00 | 1,61 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,18 | 6,00 | 1,82 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,09 | 6,00 | 2,91 | STALE_CANDLE | 1,11 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,06 | 6,00 | 3,94 | STALE_CANDLE | 1,11 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,21 | 6,00 | 5,79 | STALE_CANDLE | 1,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | AKE | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | AKE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | AKE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered — madre | AKE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — no volatilità HIGH | AKE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — senza ESPORTS | AKE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | 60m | LONG | 8,25 | 4,50 | 0,00 | READY | 6,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.718,14 | -2,82% | €-30,20 | €3.000,00 | -1,01% | 5 | 40 | 35,00% | 0,78 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 40 | 1267 | PRIME INDICAZIONI | 50 (mancano 10) |

- Trade del Principale 4H chiusi: **40**; win rate **35,00%**; profit factor **0,78**.
- Expectancy: **€-7,08** per trade; P&L netto: **€-283,07**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.718,14 | €1.286,74 | €3.860,23 | €194,28 | €1,56 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.700,20 | €4.841,80 | €9.683,61 | €160,83 | €102,49 |
| TEST | Rapida score 6–7,5 — Cost Aware | 4 | €10.591,25 | €3.032,10 | €9.096,30 | €105,92 | €81,31 |
| TEST | Rapida V1 — score 6–7,5 | 5 | €10.583,14 | €2.049,68 | €6.149,04 | €159,34 | €31,37 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.448,27 | €4.727,81 | €9.455,62 | €157,05 | €100,08 |
| TEST | MAIN — Side × Regime Guard | 5 | €10.366,64 | €2.118,53 | €6.355,60 | €155,48 | €0,65 |
| TEST | Rapida V3 NoHigh — Range Only | 4 | €10.345,90 | €3.399,91 | €10.199,73 | €156,23 | €7,99 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.336,91 | €1.685,04 | €5.055,13 | €51,81 | €27,64 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 5 | €10.301,76 | €1.995,18 | €5.985,55 | €155,10 | €30,53 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 4 | €10.283,18 | €2.006,67 | €6.020,01 | €206,08 | €28,35 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.276,82 | €3.038,97 | €9.116,92 | €205,43 | €21,92 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 5 | €10.248,95 | €3.479,15 | €10.437,44 | €204,90 | €6,97 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.198,41 | €4.275,18 | €8.550,36 | €153,33 | €92,48 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €10.130,84 | €139,31 | €417,94 | €50,15 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.125,19 | €2.477,91 | €7.433,72 | €202,34 | €26,91 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 4 | €10.088,72 | €5.432,18 | €10.864,35 | €202,34 | €-11,86 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.051,75 | €3.841,61 | €11.524,84 | €152,42 | €7,73 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €10.019,84 | €1.301,67 | €3.905,01 | €49,98 | €23,33 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.013,38 | €3.574,44 | €7.148,87 | €151,50 | €-41,48 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.002,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 5 | €9.993,91 | €3.392,57 | €10.177,71 | €199,80 | €6,80 |
| TEST | Bilanciata 1H V1 | 6 | €9.992,98 | €1.980,18 | €5.940,53 | €151,21 | €-0,68 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.979,91 | €1.152,72 | €3.458,17 | €49,80 | €20,66 |
| TEST | Doge Ema 1H | 1 | €9.978,23 | €1.155,63 | €3.466,88 | €49,92 | €-4,65 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 7 | €9.973,00 | €2.545,57 | €7.636,70 | €198,77 | €26,47 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 4 | €9.972,89 | €3.303,34 | €9.910,01 | €149,55 | €35,38 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.972,07 | €4.759,21 | €9.518,42 | €197,93 | €75,22 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.961,66 | €1.413,45 | €2.826,90 | €49,75 | €11,26 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.949,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 3 | €9.933,37 | €4.073,97 | €12.221,90 | €100,16 | €57,88 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.932,03 | €1.722,58 | €3.445,15 | €49,61 | €12,12 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.903,21 | €1.406,00 | €2.812,00 | €49,49 | €5,23 |
| TEST | Combo Adaptive — madre | 7 | €9.894,34 | €5.402,95 | €10.805,90 | €150,04 | €97,18 |
| TEST | Btc Ema 1H | 1 | €9.893,41 | €1.141,05 | €3.423,15 | €49,29 | €34,43 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €9.890,18 | €3.601,51 | €7.203,01 | €147,13 | €100,19 |
| TEST | Combo Adaptive — Quality7 | 2 | €9.886,55 | €1.924,79 | €3.849,59 | €99,00 | €-9,78 |
| TEST | Ampia 4H | 5 | €9.875,17 | €1.961,33 | €3.922,65 | €148,09 | €1,19 |
| TEST | Rapida V3 — qualità completa + profit lock | 4 | €9.850,97 | €2.567,00 | €7.700,99 | €195,67 | €36,81 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 4 | €9.835,32 | €2.562,05 | €7.686,16 | €195,05 | €36,75 |
| TEST | Bilanciata 1H V2 | 6 | €9.824,38 | €2.621,48 | €7.864,44 | €146,25 | €9,61 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €9.819,31 | €4.167,60 | €8.335,20 | €146,92 | €81,66 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 2 | €9.813,85 | €2.917,96 | €8.753,88 | €98,04 | €-3,57 |
| TEST | Sol Ema 1H | 0 | €9.813,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.807,10 | €1.700,91 | €3.401,82 | €48,99 | €11,97 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €9.787,75 | €3.793,76 | €11.381,27 | €194,67 | €42,77 |
| TEST | Top 5 + BTC — Guard | 4 | €9.770,15 | €3.557,80 | €7.115,60 | €145,35 | €98,98 |
| TEST | Combo Adaptive — Long Only | 5 | €9.768,70 | €4.107,55 | €8.215,10 | €147,00 | €71,12 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.753,83 | €3.946,15 | €7.892,29 | €194,87 | €43,11 |
| TEST | Scanner Bottom10 Short | 6 | €9.747,21 | €4.868,27 | €9.736,53 | €147,50 | €43,36 |
| TEST | Scanner Bottom15 Short | 6 | €9.747,21 | €4.868,27 | €9.736,53 | €147,50 | €43,36 |
| TEST | Scanner Bottom20 Short | 6 | €9.747,21 | €4.868,27 | €9.736,53 | €147,50 | €43,36 |
| TEST | Forza relativa 1H V2 | 4 | €9.732,78 | €4.814,47 | €9.628,95 | €97,33 | €109,21 |
| TEST | Combo Mean Reversion | 0 | €9.732,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 7 | €9.724,55 | €5.309,06 | €10.618,12 | €147,47 | €95,21 |
| TEST | Rapida 1H V3 Filtered — madre | 6 | €9.723,79 | €3.768,97 | €11.306,90 | €193,40 | €42,49 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €9.720,48 | €3.539,71 | €7.079,43 | €144,61 | €98,47 |
| TEST | Bilanciata V3 · LONG only | 6 | €9.720,23 | €2.874,38 | €8.623,15 | €194,31 | €20,73 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.681,23 | €4.839,94 | €9.679,89 | €146,50 | €43,31 |
| TEST | Sol Adaptive 1H | 0 | €9.674,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.671,79 | €1.512,09 | €3.024,18 | €48,39 | €-4,05 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.666,51 | €4.832,58 | €9.665,16 | €146,28 | €43,24 |
| TEST | Rapida V3 — no volatilità HIGH | 6 | €9.643,08 | €4.471,70 | €13.415,10 | €192,24 | €23,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.634,58 | €1.935,76 | €3.871,51 | €46,46 | €-18,28 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.629,94 | €4.122,84 | €8.245,69 | €192,39 | €42,71 |
| TEST | Eth Ema 1H | 0 | €9.622,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.592,12 | €4.795,39 | €9.590,79 | €145,15 | €42,91 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 5 | €9.565,01 | €4.096,68 | €8.193,36 | €191,16 | €24,49 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €9.562,71 | €799,57 | €2.398,70 | €49,58 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 5 | €9.554,84 | €4.092,33 | €8.184,65 | €190,96 | €24,47 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.542,93 | €3.475,06 | €6.950,11 | €141,97 | €96,67 |
| TEST | Combo Adaptive — target pieno 3R | 7 | €9.542,88 | €5.209,88 | €10.419,75 | €144,71 | €93,43 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.534,01 | €2.318,74 | €6.956,22 | €95,80 | €86,95 |
| TEST | Rapida V3 — senza ESPORTS | 6 | €9.525,86 | €3.692,25 | €11.076,74 | €189,46 | €41,63 |
| TEST | Master Adaptive V1 | 5 | €9.517,88 | €4.076,50 | €8.152,99 | €190,22 | €24,37 |
| TEST | Combo Adaptive — parziale 1R | 7 | €9.500,99 | €5.188,16 | €10.376,32 | €144,08 | €93,32 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €9.453,53 | €4.012,35 | €8.024,71 | €141,45 | €78,62 |
| TEST | Combo Trend | 7 | €9.451,50 | €3.871,51 | €7.743,02 | €143,34 | €79,83 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €9.448,00 | €4.010,01 | €8.020,01 | €141,36 | €78,57 |
| TEST | Benchmark trend following EMA 1H | 6 | €9.432,06 | €4.629,52 | €9.259,04 | €144,29 | €89,90 |
| TEST | Forza relativa 1H V1 | 7 | €9.412,31 | €2.865,53 | €5.731,07 | €187,75 | €1,69 |
| TEST | Scanner Top10 Long | 5 | €9.393,36 | €3.941,75 | €7.883,50 | €141,42 | €85,02 |
| TEST | Scanner Top15 Long | 5 | €9.393,36 | €3.941,75 | €7.883,50 | €141,42 | €85,02 |
| TEST | Scanner Top20 Long | 5 | €9.393,36 | €3.941,75 | €7.883,50 | €141,42 | €85,02 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.391,42 | €4.022,33 | €8.044,67 | €187,69 | €24,05 |
| TEST | Top 5 + BTC — BTC≤3 | 5 | €9.383,34 | €3.982,56 | €7.965,12 | €140,40 | €78,04 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.371,84 | €2.769,33 | €5.538,67 | €141,27 | €-4,22 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.289,65 | €2.711,74 | €5.423,49 | €138,00 | €38,56 |
| TEST | Combo Scanner | 4 | €9.244,01 | €4.090,61 | €8.181,22 | €139,75 | €59,94 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.204,19 | €3.906,52 | €7.813,04 | €137,72 | €76,55 |
| TEST | Rapida V3 — Long Only | 2 | €9.104,74 | €761,28 | €2.283,83 | €47,21 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 1 | €9.101,40 | €192,15 | €384,31 | €46,12 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 5 | €9.005,58 | €4.911,72 | €9.823,43 | €180,18 | €21,47 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.718,14 | €-283,07 | 40 | 40 | 35,00% | 0,78 | €-7,08 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.700,20 | €602,99 | 57 | 57 | 47,37% | 1,43 | €10,58 | 3,63% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.591,25 | €514,12 | 53 | 53 | 50,94% | 1,50 | €9,70 | 3,00% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.583,14 | €553,05 | 100 | 100 | 45,00% | 1,27 | €5,53 | 3,21% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.448,27 | €353,35 | 25 | 25 | 44,00% | 1,65 | €14,13 | 3,63% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.366,64 | €367,24 | 20 | 20 | 50,00% | 1,85 | €18,36 | 2,40% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.345,90 | €340,71 | 29 | 29 | 48,28% | 1,57 | €11,75 | 3,55% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.336,91 | €309,95 | 29 | 29 | 51,72% | 1,42 | €10,69 | 2,31% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.301,76 | €272,47 | 58 | 58 | 50,00% | 1,20 | €4,70 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.283,18 | €256,02 | 37 | 37 | 51,35% | 1,36 | €6,92 | 4,32% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.276,82 | €258,01 | 81 | 81 | 39,51% | 1,16 | €3,19 | 4,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.248,95 | €244,87 | 90 | 90 | 42,22% | 1,12 | €2,72 | 6,15% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.198,41 | €110,95 | 65 | 65 | 43,08% | 1,07 | €1,71 | 7,66% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.130,84 | €131,11 | 28 | 28 | 39,29% | 1,25 | €4,68 | 2,27% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.125,19 | €99,65 | 90 | 90 | 42,22% | 1,05 | €1,11 | 5,76% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.088,72 | €103,88 | 50 | 50 | 46,00% | 1,11 | €2,08 | 5,79% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.051,75 | €46,91 | 91 | 91 | 42,86% | 1,03 | €0,52 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.019,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.013,38 | €57,88 | 42 | 42 | 50,00% | 1,07 | €1,38 | 2,94% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.002,03 | €2,03 | 6 | 6 | 50,00% | 1,02 | €0,34 | 1,50% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.993,91 | €-10,06 | 54 | 54 | 38,89% | 0,99 | €-0,19 | 6,15% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.992,98 | €-3,47 | 92 | 92 | 42,39% | 1,00 | €-0,04 | 6,27% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.979,91 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 1,13% |
| TEST | Doge Ema 1H | Trend following EMA | €9.978,23 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.973,00 | €-51,97 | 101 | 101 | 35,64% | 0,97 | €-0,51 | 3,95% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.972,89 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,36% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.972,07 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Btc Ema 4H | Trend following EMA | €9.961,66 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.949,30 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 1,59% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.933,37 | €-119,29 | 29 | 29 | 41,38% | 0,84 | €-4,11 | 3,94% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.932,03 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.903,21 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.894,34 | €-198,26 | 55 | 55 | 36,36% | 0,81 | €-3,60 | 5,27% |
| TEST | Btc Ema 1H | Trend following EMA | €9.893,41 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,72% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.890,18 | €-205,80 | 32 | 32 | 37,50% | 0,80 | €-6,43 | 6,54% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.886,55 | €-101,30 | 31 | 31 | 32,26% | 0,83 | €-3,27 | 3,10% |
| TEST | Ampia 4H | Confluenza trend | €9.875,17 | €-125,24 | 34 | 34 | 23,53% | 0,86 | €-3,68 | 4,36% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.850,97 | €-181,09 | 63 | 63 | 46,03% | 0,89 | €-2,87 | 4,39% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.835,32 | €-196,68 | 58 | 58 | 41,38% | 0,87 | €-3,39 | 4,70% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.824,38 | €-181,86 | 58 | 54 | 43,10% | 0,87 | €-3,14 | 5,62% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.819,31 | €-257,74 | 53 | 53 | 33,96% | 0,82 | €-4,86 | 8,43% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.813,85 | €-178,13 | 27 | 24 | 37,04% | 0,76 | €-6,60 | 3,89% |
| TEST | Sol Ema 1H | Trend following EMA | €9.813,68 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 2,63% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.807,10 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,40% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.787,75 | €-251,18 | 70 | 70 | 50,00% | 0,82 | €-3,59 | 6,78% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.770,15 | €-324,66 | 37 | 37 | 32,43% | 0,72 | €-8,77 | 6,13% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.768,70 | €-297,71 | 33 | 33 | 30,30% | 0,65 | €-9,02 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.753,83 | €-284,52 | 38 | 38 | 31,58% | 0,77 | €-7,49 | 4,45% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.747,21 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.747,21 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.747,21 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.732,78 | €-369,36 | 67 | 64 | 37,31% | 0,83 | €-5,51 | 8,11% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.732,10 | €-267,90 | 28 | 28 | 35,71% | 0,72 | €-9,57 | 4,71% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.724,55 | €-366,18 | 62 | 62 | 32,26% | 0,71 | €-5,91 | 6,25% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.723,79 | €-314,88 | 114 | 114 | 38,60% | 0,87 | €-2,76 | 6,75% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.720,48 | €-373,84 | 47 | 47 | 38,30% | 0,71 | €-7,95 | 5,80% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.720,23 | €-297,57 | 37 | 37 | 35,14% | 0,60 | €-8,04 | 4,03% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.681,23 | €-358,39 | 36 | 36 | 33,33% | 0,58 | €-9,96 | 5,27% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.674,16 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 3,94% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.671,79 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.666,51 | €-373,06 | 37 | 37 | 32,43% | 0,53 | €-10,08 | 5,27% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.643,08 | €-374,91 | 79 | 79 | 40,51% | 0,81 | €-4,75 | 5,62% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.634,58 | €-344,88 | 66 | 66 | 42,42% | 0,80 | €-5,23 | 6,53% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.629,94 | €-407,76 | 34 | 34 | 26,47% | 0,67 | €-11,99 | 6,03% |
| TEST | Eth Ema 1H | Trend following EMA | €9.622,18 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 3,78% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.592,12 | €-447,14 | 64 | 64 | 32,81% | 0,68 | €-6,99 | 6,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.565,01 | €-453,76 | 38 | 38 | 21,05% | 0,60 | €-11,94 | 6,68% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.562,71 | €-436,58 | 49 | 49 | 34,69% | 0,68 | €-8,91 | 7,90% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.554,84 | €-463,92 | 33 | 33 | 27,27% | 0,57 | €-14,06 | 6,27% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.542,93 | €-549,67 | 54 | 54 | 37,04% | 0,64 | €-10,18 | 7,59% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.542,88 | €-546,16 | 43 | 43 | 30,23% | 0,47 | €-12,70 | 6,25% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.534,01 | €-548,20 | 37 | 37 | 29,73% | 0,54 | €-14,82 | 7,00% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.525,86 | €-512,03 | 88 | 88 | 38,64% | 0,75 | €-5,82 | 6,72% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.517,88 | €-500,80 | 35 | 35 | 25,71% | 0,60 | €-14,31 | 6,08% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.500,99 | €-587,93 | 56 | 56 | 33,93% | 0,52 | €-10,50 | 6,07% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.453,53 | €-620,65 | 38 | 38 | 26,32% | 0,51 | €-16,33 | 9,13% |
| TEST | Combo Trend | Combo Trend | €9.451,50 | €-625,34 | 87 | 87 | 31,03% | 0,74 | €-7,19 | 9,82% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.448,00 | €-626,14 | 42 | 42 | 28,57% | 0,51 | €-14,91 | 9,42% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.432,06 | €-654,34 | 57 | 57 | 28,07% | 0,55 | €-11,48 | 7,38% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.412,31 | €-586,57 | 76 | 76 | 28,95% | 0,67 | €-7,72 | 8,31% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.393,36 | €-687,03 | 37 | 37 | 32,43% | 0,42 | €-18,57 | 9,13% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.393,36 | €-687,03 | 37 | 37 | 32,43% | 0,42 | €-18,57 | 9,13% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.393,36 | €-687,03 | 37 | 37 | 32,43% | 0,42 | €-18,57 | 9,13% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.391,42 | €-627,01 | 70 | 70 | 48,57% | 0,57 | €-8,96 | 7,33% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.383,34 | €-690,30 | 34 | 34 | 26,47% | 0,39 | €-20,30 | 8,89% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.371,84 | €-620,05 | 33 | 33 | 21,21% | 0,51 | €-18,79 | 6,64% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.289,65 | €-745,57 | 37 | 37 | 24,32% | 0,53 | €-20,15 | 9,06% |
| TEST | Combo Scanner | Combo Scanner | €9.244,01 | €-812,06 | 63 | 63 | 31,75% | 0,56 | €-12,89 | 10,13% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.204,19 | €-868,04 | 46 | 46 | 28,26% | 0,31 | €-18,87 | 9,46% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.104,74 | €-894,59 | 69 | 69 | 27,54% | 0,56 | €-12,97 | 9,88% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.101,40 | €-898,33 | 31 | 31 | 16,13% | 0,32 | €-28,98 | 10,58% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.005,58 | €-1.011,88 | 69 | 69 | 30,43% | 0,39 | €-14,66 | 10,41% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00972 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €1,58 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | CYS | LONG | Confluenza trend | 240m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,91631 | €134,84 | €404,53 | €48,54 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63426,03000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €-0,02 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,91631 | €134,24 | €402,71 | €48,32 | €0,00 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,04289 | 1,04289 | 1,03001 | 1,38531 | 0,79260 | €139,17 | €417,52 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,07023 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €-0,34 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00972 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €-0,34 |
| Bilanciata 1H — LONG senza Range High Vol | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,86025 | €131,62 | €394,86 | €0,00 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HYPE | LONG | Confluenza trend | 60m | 3,0x | 56,32678 | 57,52600 | 56,99628 | 37,83282 | 57,95427 | €1.091,23 | €3.273,70 | €0,00 | €69,70 |
| Bilanciata 1H — LONG senza Range High Vol | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | APR | LONG | Confluenza trend | 60m | 3,0x | 0,49291 | 0,51414 | 0,43376 | 0,33107 | 0,61121 | €131,87 | €395,61 | €47,47 | €17,04 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1186,90171 | 1193,87000 | 1157,32162 | 797,20232 | 1246,06190 | €11,99 | €35,96 | €0,90 | €0,21 |
| Bilanciata 1H — SHORT Trend Down stretto | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,03900 | 1,03900 | 1,03001 | 1,38014 | 0,78964 | €138,10 | €414,31 | €0,00 | €-0,00 |
| Bilanciata 1H — SHORT Trend Down stretto | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63436,91008 | 63426,03000 | 64350,40159 | 84265,36222 | 61609,92707 | €1.150,82 | €3.452,45 | €49,72 | €0,59 |
| Bilanciata 1H — SHORT Trend Down stretto | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €39,44 |
| Bilanciata 1H — SHORT Trend Down stretto | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,07023 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €-4,65 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 63596,27820 | 63426,03000 | 64512,06461 | 84477,05621 | 61764,70539 | €1.127,13 | €3.381,38 | €48,69 | €9,05 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,86025 | €136,27 | €408,82 | €0,00 | €0,00 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 56,32678 | 57,52600 | 56,99628 | 37,83282 | 57,95427 | €16,33 | €48,98 | €0,00 | €1,04 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00972 | 1,01986 | 1,33548 | 0,97642 | €37,09 | €111,28 | €1,60 | €-0,48 |
| Bilanciata 1H V2 | BEAT | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,96465 | 0,96465 | 1,08040 | 1,28137 | 0,73313 | €124,99 | €374,96 | €45,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.129,53 | €3.388,60 | €48,80 | €20,24 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,91879 | €140,87 | €422,61 | €50,71 | €0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 56,61695 | 57,52600 | 57,00586 | 38,02772 | 58,24752 | €9,40 | €28,20 | €0,00 | €0,45 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €1,22 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.575,50 | €4.726,51 | €52,94 | €28,24 |
| Rapida V1 — score 6–7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €145,36 | €436,08 | €0,00 | €0,00 |
| Rapida V1 — score 6–7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €142,15 | €426,45 | €51,17 | €-0,00 |
| Rapida V1 — score 6–7,5 | APR | LONG | Momentum / breakout | 60m | 3,0x | 0,51132 | 0,51414 | 0,44996 | 0,34344 | 0,60336 | €146,99 | €440,98 | €52,92 | €2,43 |
| Rapida V1 — score 6–7,5 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €39,67 | €119,02 | €2,31 | €0,70 |
| Rapida score 6–7,5 — senza Trend Up | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.533,61 | €4.600,84 | €51,53 | €27,49 |
| Rapida score 6–7,5 — senza Trend Up | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €141,49 | €424,48 | €0,00 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €138,37 | €415,11 | €49,81 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | APR | LONG | Momentum / breakout | 60m | 3,0x | 0,51132 | 0,51414 | 0,44996 | 0,34344 | 0,60336 | €143,09 | €429,26 | €51,51 | €2,37 |
| Rapida score 6–7,5 — senza Trend Up | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €38,62 | €115,85 | €2,25 | €0,68 |
| Rapida score 6–7,5 — Range Only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.542,02 | €4.626,07 | €51,81 | €27,64 |
| Rapida score 6–7,5 — Range Only | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,48830 | 1,48830 | 1,48830 | 0,99964 | 1,75619 | €143,02 | €429,06 | €0,00 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.591,68 | €4.775,04 | €53,48 | €28,53 |
| Rapida score 6–7,5 — Cost Aware | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €145,92 | €437,77 | €0,00 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.148,84 | €3.446,52 | €0,00 | €52,78 |
| Rapida score 6–7,5 — Cost Aware | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95974 | 0,95974 | 1,07491 | 1,27485 | 0,78699 | €145,66 | €436,97 | €52,44 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.585,67 | €4.757,02 | €53,28 | €28,42 |
| Rapida V1 — no HIGH + score <7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €200,91 | €602,72 | €51,68 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,07023 | 0,07069 | 0,09286 | 0,06873 | €1.537,89 | €4.613,67 | €51,67 | €-21,38 |
| Rapida V1 — no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,64657 | 57,52600 | 57,00093 | 38,71928 | 58,61503 | €10,86 | €32,58 | €0,36 | €-0,07 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €143,81 | €431,44 | €47,91 | €-0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €139,31 | €417,94 | €50,15 | €0,00 |
| Rapida V1 — senza PEPE | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €682,89 | €2.048,66 | €50,88 | €0,00 |
| Rapida V1 — senza PEPE | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.518,20 | €4.554,59 | €51,01 | €27,21 |
| Rapida V1 — senza PEPE | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,51880 | 1,51880 | 1,51880 | 1,02013 | 1,79219 | €136,73 | €410,18 | €0,00 | €0,00 |
| Rapida V1 — senza PEPE | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,00538 | 1,00972 | 1,01664 | 1,33548 | 0,98849 | €1.503,80 | €4.511,41 | €50,53 | €-19,48 |
| Rapida V1 — target pieno 2R | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 143,59705 | €668,73 | €2.006,20 | €49,82 | €0,00 |
| Rapida V1 — target pieno 2R | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62377,95391 | €1.482,17 | €4.446,51 | €49,80 | €26,56 |
| Rapida V1 — target pieno 2R | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64299 | 1,64299 | 1,47977 | 1,10354 | 1,96941 | €161,09 | €483,28 | €48,01 | €0,00 |
| Rapida V1 — target pieno 2R | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,00538 | 1,00972 | 1,01664 | 1,33548 | 0,98286 | €55,98 | €167,93 | €1,88 | €-0,73 |
| Rapida V1 — target pieno 2R | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €15,78 | €47,34 | €0,00 | €0,72 |
| Rapida V1 — target pieno 2R | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,64657 | 57,52600 | 57,00093 | 38,71928 | 58,93785 | €15,51 | €46,53 | €0,52 | €-0,10 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,68886 | €146,30 | €438,91 | €48,73 | €-0,00 |
| Rapida 1H V2 | XRP | SHORT | Momentum / breakout V2 | 60m | 3,0x | 1,00538 | 1,00972 | 1,01664 | 1,33548 | 0,98849 | €1.461,59 | €4.384,76 | €49,11 | €-18,93 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 57,32437 | 57,52600 | 56,68234 | 38,50287 | 58,28742 | €1.456,37 | €4.369,12 | €48,93 | €15,37 |
| Rapida 1H V3 Filtered — madre | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €672,56 | €2.017,68 | €50,11 | €0,00 |
| Rapida 1H V3 Filtered — madre | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.474,48 | €4.423,44 | €49,54 | €26,43 |
| Rapida 1H V3 Filtered — madre | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €177,34 | €532,02 | €45,61 | €0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,81 | €62,42 | €0,00 | €0,96 |
| Rapida 1H V3 Filtered — madre | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,32437 | 57,52600 | 56,68234 | 38,50287 | 58,28742 | €1.411,81 | €4.235,42 | €47,44 | €14,90 |
| Rapida 1H V3 Filtered — madre | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €11,97 | €35,92 | €0,70 | €0,21 |
| Rapida V3 — score <7,5 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €685,11 | €2.055,32 | €51,04 | €0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.501,29 | €4.503,87 | €50,44 | €26,91 |
| Rapida V3 — score <7,5 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €139,51 | €418,54 | €50,22 | €0,00 |
| Rapida V3 — score <7,5 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €152,00 | €456,00 | €50,63 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.489,03 | €4.467,09 | €50,03 | €26,69 |
| Rapida V3 — no volatilità HIGH | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €187,10 | €561,31 | €48,13 | €0,00 |
| Rapida V3 — no volatilità HIGH | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06991 | 0,07023 | 0,07069 | 0,09286 | 0,06873 | €1.375,16 | €4.125,47 | €46,21 | €-19,12 |
| Rapida V3 — no volatilità HIGH | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,82 | €26,46 | €0,00 | €0,41 |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,32437 | 57,52600 | 56,68234 | 38,50287 | 58,28742 | €1.393,53 | €4.180,59 | €46,82 | €14,70 |
| Rapida V3 — no volatilità HIGH | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €18,06 | €54,19 | €1,05 | €0,32 |
| Rapida V3 — Long Only | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €633,63 | €1.900,88 | €47,21 | €0,00 |
| Rapida V3 — Long Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,46019 | 1,46056 | 0,98076 | 1,72303 | €127,65 | €382,94 | €0,00 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €135,24 | €405,73 | €48,69 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,51414 | 0,42033 | 0,32082 | 0,56362 | €135,15 | €405,45 | €48,65 | €30,98 |
| Rapida V3 — Long + no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,64657 | 57,52600 | 57,00093 | 38,71928 | 58,61503 | €1.448,19 | €4.344,58 | €48,66 | €-9,09 |
| Rapida V3 — Long + no HIGH + score <7,5 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €843,47 | €2.530,40 | €49,05 | €14,86 |
| Rapida V3 — senza ESPORTS | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €658,87 | €1.976,61 | €49,09 | €0,00 |
| Rapida V3 — senza ESPORTS | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.444,46 | €4.333,39 | €48,53 | €25,89 |
| Rapida V3 — senza ESPORTS | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €173,73 | €521,19 | €44,69 | €0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,38 | €61,15 | €0,00 | €0,94 |
| Rapida V3 — senza ESPORTS | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,32437 | 57,52600 | 56,68234 | 38,50287 | 58,28742 | €1.383,07 | €4.149,20 | €46,47 | €14,59 |
| Rapida V3 — senza ESPORTS | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €11,73 | €35,19 | €0,68 | €0,21 |
| Rapida V3 senza ESPORTS — Long Only | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €665,50 | €1.996,50 | €49,58 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,46019 | 1,46056 | 0,98076 | 1,72303 | €134,07 | €402,21 | €0,00 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €676,98 | €2.030,95 | €50,44 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.484,18 | €4.452,53 | €49,87 | €26,60 |
| Rapida V3 senza ESPORTS — MFE Lock | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €178,51 | €535,52 | €45,91 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,94 | €62,83 | €0,00 | €0,96 |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,32437 | 57,52600 | 56,68234 | 38,50287 | 58,28742 | €1.421,09 | €4.263,28 | €47,75 | €15,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €12,05 | €36,16 | €0,70 | €0,21 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.498,86 | €4.496,57 | €50,36 | €26,86 |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00538 | 1,00972 | 1,01664 | 1,33548 | 0,98849 | €1.482,09 | €4.446,28 | €49,80 | €-19,20 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,02 | €3.279,06 | €0,00 | €50,22 |
| Rapida V3 — qualità completa + profit lock | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €136,31 | €408,93 | €49,07 | €0,00 |
| Rapida V3 — qualità completa + profit lock | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,51414 | 0,42033 | 0,32082 | 0,56362 | €135,37 | €406,10 | €48,73 | €31,03 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,64657 | 57,52600 | 57,00093 | 38,71928 | 58,61503 | €1.450,51 | €4.351,54 | €48,74 | €-9,10 |
| Rapida V3 — qualità completa + profit lock | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,90171 | 1193,87000 | 1163,89498 | 797,20232 | 1221,41183 | €844,81 | €2.534,42 | €49,13 | €14,88 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00972 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €1,23 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 63426,03000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €-0,04 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 56,45529 | 57,52600 | 56,97575 | 28,50992 | 58,24379 | €16,76 | €33,52 | €0,00 | €0,64 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,62778 | 1,62778 | 1,43244 | 0,82203 | 2,05751 | €195,68 | €391,36 | €46,96 | €0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €169,57 | €339,13 | €40,70 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €0,35 |
| Forza relativa 1H V1 | SKHYNIX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32162 | 599,38537 | 1251,97793 | €59,56 | €119,13 | €2,97 | €0,70 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 56,32678 | 57,52600 | 56,95002 | 28,44502 | 58,11702 | €1.666,21 | €3.332,42 | €0,00 | €70,95 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €200,27 | €400,55 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €38,27 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 63426,03000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.676,44 | €3.352,88 | €53,65 | €20,03 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 55,85717 | 57,52600 | 57,04128 | 28,20787 | 58,09146 | €1.637,81 | €3.275,62 | €0,00 | €97,86 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €8,26 |
| Benchmark Donchian breakout 1H | TUT | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,03711 | 0,03908 | 0,04157 | 0,05548 | 0,02598 | €223,22 | €446,43 | €53,57 | €-23,67 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 63426,03000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.636,97 | €3.273,94 | €52,38 | €19,56 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 55,85717 | 57,52600 | 57,04128 | 28,20787 | 58,09146 | €1.599,25 | €3.198,50 | €0,00 | €95,56 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €8,07 |
| Donchian 1H Gb20 120R V1 | TUT | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,03711 | 0,03908 | 0,04157 | 0,05548 | 0,02598 | €217,96 | €435,92 | €52,31 | €-23,11 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 57,25563 | 57,52600 | 57,94269 | 85,59716 | 56,22502 | €1.935,76 | €3.871,51 | €46,46 | €-18,28 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 63426,03000 | 65095,57044 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €48,54 | €30,51 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 56,45585 | 57,52600 | 56,99793 | 28,51021 | 58,44310 | €1.366,30 | €2.732,59 | €0,00 | €51,80 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €7,64 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07023 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €-0,06 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 57,95427 | €1.745,25 | €3.490,50 | €0,00 | €74,31 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | APR | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,61121 | €209,11 | €418,21 | €50,19 | €18,01 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32162 | 599,38537 | 1246,06190 | €12,61 | €25,22 | €0,63 | €0,15 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63426,03000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €49,45 | €34,54 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €199,49 | €398,98 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €8,80 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €-0,40 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 485,58000 | 493,83011 | 725,16914 | 467,52868 | €12,76 | €25,52 | €0,46 | €-0,03 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 57,95427 | €1.607,51 | €3.215,02 | €0,00 | €68,45 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | APR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €16,59 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1253,47570 | €15,59 | €31,19 | €0,77 | €-0,02 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 63426,03000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €34,77 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €9,03 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,41 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 485,06297 | 485,58000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,03 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 57,95427 | €1.607,51 | €3.215,02 | €0,00 | €68,45 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | APR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €16,59 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1253,47570 | €15,59 | €31,19 | €0,77 | €-0,02 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 63426,03000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €34,77 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €9,03 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,41 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 485,06297 | 485,58000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,03 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 57,95427 | €1.607,51 | €3.215,02 | €0,00 | €68,45 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | APR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €16,59 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1253,47570 | €15,59 | €31,19 | €0,77 | €-0,02 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 63426,03000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €34,77 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €9,03 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €-0,41 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 485,06297 | 485,58000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,03 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,45585 | 57,52600 | 57,04100 | 28,51021 | 58,24437 | €1.717,61 | €3.435,23 | €0,00 | €65,12 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €192,28 | €384,55 | €46,15 | €16,56 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1259,36464 | €16,15 | €32,30 | €0,80 | €-0,02 |
| Top 5 + BTC — solo MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,45585 | 57,52600 | 57,04100 | 28,51021 | 58,24437 | €1.610,01 | €3.220,03 | €0,00 | €61,04 |
| Top 5 + BTC — solo MFE | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Top 5 + BTC — solo MFE | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €180,23 | €360,46 | €43,26 | €15,53 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1259,36464 | €15,14 | €30,28 | €0,75 | €-0,02 |
| Top 5 + BTC — Guard | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Top 5 + BTC — Guard | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 58,11702 | €1.648,77 | €3.297,53 | €0,00 | €70,21 |
| Top 5 + BTC — Guard | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €200,65 | €401,31 | €48,16 | €17,29 |
| Top 5 + BTC — Guard | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32162 | 599,38537 | 1251,97793 | €978,05 | €1.956,11 | €48,75 | €11,48 |
| Top 5 + BTC — BTC≤3 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Top 5 + BTC — BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,45585 | 57,52600 | 57,04100 | 28,51021 | 58,24437 | €1.641,35 | €3.282,70 | €0,00 | €62,23 |
| Top 5 + BTC — BTC≤3 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Top 5 + BTC — BTC≤3 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €183,74 | €367,48 | €44,10 | €15,83 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1259,36464 | €15,44 | €30,87 | €0,76 | €-0,02 |
| Top 5 + BTC — Guard + MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Top 5 + BTC — Guard + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 58,11702 | €1.610,42 | €3.220,84 | €0,00 | €68,57 |
| Top 5 + BTC — Guard + MFE | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €195,99 | €391,97 | €47,04 | €16,88 |
| Top 5 + BTC — Guard + MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32162 | 599,38537 | 1251,97793 | €955,31 | €1.910,62 | €47,62 | €11,22 |
| Top 5 + BTC — Guard + BTC≤3 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 58,11702 | €1.669,02 | €3.338,04 | €0,00 | €71,07 |
| Top 5 + BTC — Guard + BTC≤3 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €203,12 | €406,24 | €48,75 | €17,50 |
| Top 5 + BTC — Guard + BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32162 | 599,38537 | 1251,97793 | €990,07 | €1.980,14 | €49,35 | €11,63 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,32678 | 57,52600 | 56,99628 | 28,44502 | 58,11702 | €1.640,38 | €3.280,77 | €0,00 | €69,85 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €199,63 | €399,27 | €47,91 | €17,20 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32162 | 599,38537 | 1251,97793 | €973,08 | €1.946,17 | €48,50 | €11,43 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,45585 | 57,52600 | 57,04100 | 28,51021 | 58,89475 | €1.652,66 | €3.305,33 | €0,00 | €62,65 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,67036 | €185,01 | €370,01 | €44,40 | €15,94 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1282,92039 | €15,54 | €31,08 | €0,77 | €-0,02 |
| Top 5 + BTC — target pieno 3R | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 56,45585 | 57,52600 | 57,04100 | 28,51021 | 58,89475 | €1.653,63 | €3.307,26 | €0,00 | €62,69 |
| Top 5 + BTC — target pieno 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Top 5 + BTC — target pieno 3R | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,67036 | €185,11 | €370,23 | €44,43 | €15,95 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1282,92039 | €15,55 | €31,10 | €0,77 | €-0,02 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07023 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €-4,05 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63807,23600 | 63426,03000 | 64828,15178 | 95391,81782 | 61561,22129 | €1.485,14 | €2.970,29 | €47,52 | €17,75 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 56,32678 | 57,52600 | 56,95002 | 28,44502 | 58,31593 | €1.416,08 | €2.832,16 | €0,00 | €60,30 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €179,75 | €359,50 | €43,14 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €1,86 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07023 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €-0,08 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,07023 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €-15,01 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 56,45585 | 57,52600 | 57,04100 | 28,51021 | 58,24437 | €1.554,43 | €3.108,86 | €0,00 | €58,93 |
| Combo Scanner | APR | LONG | Combo Scanner | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,62304 | €186,01 | €372,01 | €44,64 | €16,02 |
| Combo Adaptive — madre | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive — madre | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive — madre | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63426,03000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.768,38 | €3.536,76 | €50,93 | €21,13 |
| Combo Adaptive — madre | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €9,27 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 56,39081 | 57,52600 | 57,08182 | 28,47736 | 58,01487 | €1.661,23 | €3.322,46 | €0,00 | €66,88 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07023 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €-0,08 |
| Combo Adaptive — madre | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1253,47570 | €14,63 | €29,26 | €0,72 | €-0,02 |
| Combo Adaptive — MFE Trail esistente | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive — MFE Trail esistente | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63426,03000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.608,91 | €3.217,82 | €46,34 | €19,22 |
| Combo Adaptive — MFE Trail esistente | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €8,54 |
| Combo Adaptive — MFE Trail esistente | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,64657 | 57,52600 | 56,81646 | 29,11152 | 59,30679 | €1.514,92 | €3.029,83 | €43,63 | €-6,34 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07030 | 0,07023 | 0,07131 | 0,10509 | 0,06827 | €23,31 | €46,62 | €0,67 | €0,04 |
| Combo Adaptive — Quality7 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,32437 | 57,52600 | 56,49890 | 28,94881 | 58,97532 | €1.718,52 | €3.437,05 | €49,49 | €12,09 |
| Combo Adaptive — Quality7 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,03711 | 0,03908 | 0,04157 | 0,05548 | 0,02821 | €206,27 | €412,54 | €49,50 | €-21,87 |
| Combo Adaptive — Trend/Transition | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,00918 | 57,52600 | 56,18825 | 28,78964 | 58,65105 | €1.719,32 | €3.438,64 | €49,52 | €31,17 |
| Combo Adaptive — Trend/Transition | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,96465 | 0,96465 | 1,08040 | 1,44215 | 0,73313 | €206,23 | €412,46 | €49,50 | €-0,00 |
| Combo Adaptive — Trend/Transition | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €44,05 |
| Combo Adaptive — Trend/Transition | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive — Quality7 + Regime | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,32437 | 57,52600 | 56,49890 | 28,94881 | 58,97532 | €1.700,91 | €3.401,82 | €48,99 | €11,97 |
| Combo Adaptive — Long Only | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 56,61695 | 57,52600 | 57,05144 | 28,59156 | 58,24752 | €1.679,64 | €3.359,28 | €0,00 | €53,94 |
| Combo Adaptive — Long Only | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive — Long Only | APR | LONG | Combo Adaptive | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,61121 | €199,74 | €399,48 | €47,94 | €17,21 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1253,47570 | €16,24 | €32,48 | €0,80 | €-0,02 |
| Combo Adaptive — parziale 1R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive — parziale 1R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive — parziale 1R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63426,03000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.698,08 | €3.396,15 | €48,90 | €20,29 |
| Combo Adaptive — parziale 1R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €8,90 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 56,39081 | 57,52600 | 57,08182 | 28,47736 | 58,01487 | €1.595,19 | €3.190,37 | €0,00 | €64,22 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07023 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €-0,08 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1253,47570 | €14,05 | €28,10 | €0,69 | €-0,02 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,32437 | 57,52600 | 56,49890 | 28,94881 | 58,97532 | €1.722,58 | €3.445,15 | €49,61 | €12,12 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63426,03000 | 64726,06020 | 95391,81782 | 61050,76340 | €1.736,70 | €3.473,39 | €50,02 | €20,75 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €8,82 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 56,39081 | 57,52600 | 57,08182 | 28,47736 | 58,82690 | €1.632,80 | €3.265,61 | €0,00 | €65,74 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07023 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €-0,08 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1282,92039 | €14,14 | €28,27 | €0,70 | €-0,02 |
| Combo Adaptive — target pieno 3R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive — target pieno 3R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63426,03000 | 64726,06020 | 95391,81782 | 61050,76340 | €1.704,25 | €3.408,50 | €49,08 | €20,36 |
| Combo Adaptive — target pieno 3R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive — target pieno 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €8,65 |
| Combo Adaptive — target pieno 3R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 56,39081 | 57,52600 | 57,08182 | 28,47736 | 58,82690 | €1.602,30 | €3.204,60 | €0,00 | €64,51 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07023 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €-0,08 |
| Combo Adaptive — target pieno 3R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1194,58632 | 1193,87000 | 1165,14163 | 603,26609 | 1282,92039 | €13,87 | €27,75 | €0,68 | €-0,02 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 63426,03000 | 64993,05773 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €49,29 | €34,43 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 63426,03000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €11,26 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63807,23600 | 63426,03000 | 64623,96862 | 84757,27849 | 62173,77076 | €1.301,67 | €3.905,01 | €49,98 | €23,33 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 63426,03000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €5,23 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63807,23600 | 63426,03000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.152,72 | €3.458,17 | €49,80 | €20,66 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,07023 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €-4,65 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1887,36000 | 1863,55088 | 954,84293 | 1945,23249 | €1.570,92 | €3.141,85 | €45,24 | €-5,68 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,51414 | 0,42033 | 0,24121 | 0,59228 | €198,13 | €396,27 | €47,55 | €30,28 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,61252 | 57,52600 | 56,68430 | 29,09432 | 59,46896 | €75,42 | €150,84 | €2,43 | €-0,23 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,51414 | 0,42033 | 0,24121 | 0,59228 | €199,48 | €398,96 | €47,88 | €30,48 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,32437 | 57,52600 | 56,49890 | 28,94881 | 58,97532 | €1.663,87 | €3.327,74 | €47,92 | €11,70 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32161 | 599,38537 | 1246,06192 | €44,14 | €88,27 | €2,20 | €0,52 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,32437 | 57,52600 | 56,49890 | 28,94881 | 58,97532 | €1.590,84 | €3.181,67 | €45,82 | €11,19 |
| Master Adaptive Strict3 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,49291 | 0,51414 | 0,43376 | 0,24892 | 0,61121 | €190,97 | €381,94 | €45,83 | €16,45 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32161 | 599,38537 | 1246,06192 | €929,94 | €1.859,88 | €46,35 | €10,92 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,51414 | 0,42033 | 0,24121 | 0,59228 | €202,38 | €404,77 | €48,57 | €30,93 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,32437 | 57,52600 | 56,49890 | 28,94881 | 58,97532 | €1.685,04 | €3.370,08 | €48,53 | €11,85 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,90171 | 1193,87000 | 1157,32161 | 599,38537 | 1246,06192 | €27,92 | €55,84 | €1,39 | €0,33 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1887,36000 | 1863,55088 | 954,84293 | 1945,23249 | €1.550,05 | €3.100,10 | €44,64 | €-5,60 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,51414 | 0,42033 | 0,24121 | 0,59228 | €195,50 | €391,00 | €46,92 | €29,87 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,61252 | 57,52600 | 56,68430 | 29,09432 | 59,46896 | €74,42 | €148,83 | €2,40 | €-0,22 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,31376 | 1,15611 | 0,66345 | 1,78672 | €188,92 | €377,85 | €45,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 57,52600 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €1,47 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1887,36000 | 1863,55088 | 954,84293 | 1972,45969 | €1.573,63 | €3.147,26 | €45,32 | €-5,69 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Combo Adaptive — Side × Regime Guard | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63426,03000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.842,32 | €3.684,64 | €53,06 | €22,01 |
| Combo Adaptive — Side × Regime Guard | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive — Side × Regime Guard | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,07023 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €-15,38 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €-18,49 |
| Master Adaptive GB20 — Breakeven 0,5R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1887,36000 | 1863,55088 | 954,84293 | 1945,23249 | €1.578,70 | €3.157,40 | €45,47 | €-5,71 |
| Master Adaptive GB20 — Breakeven 0,5R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,51414 | 0,42033 | 0,24121 | 0,59228 | €199,12 | €398,23 | €47,79 | €30,43 |
| Master Adaptive GB20 — Breakeven 0,5R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,61252 | 57,52600 | 56,68430 | 29,09432 | 59,46896 | €75,79 | €151,58 | €2,44 | €-0,23 |
| Master Adaptive GB20 — 50% a 0,75R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1887,36000 | 1863,55088 | 954,84293 | 1945,23249 | €1.577,02 | €3.154,05 | €45,42 | €-5,70 |
| Master Adaptive GB20 — 50% a 0,75R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,51414 | 0,42033 | 0,24121 | 0,59228 | €198,90 | €397,81 | €47,74 | €30,39 |
| Master Adaptive GB20 — 50% a 0,75R | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 57,61252 | 57,52600 | 56,68430 | 29,09432 | 59,46896 | €75,71 | €151,42 | €2,44 | €-0,23 |
| Master Adaptive GB20 — Loss Cap 0,75R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,46019 | 1,46019 | 1,28497 | 0,73740 | 1,92745 | €192,15 | €384,31 | €46,12 | €0,00 |
| Rapida V3 NoHigh — Range Only | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.566,03 | €4.698,09 | €52,62 | €28,07 |
| Rapida V3 NoHigh — Range Only | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €143,18 | €429,53 | €51,54 | €0,00 |
| Rapida V3 NoHigh — Range Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,48830 | 1,48830 | 1,48830 | 0,99964 | 1,75619 | €141,11 | €423,32 | €0,00 | €0,00 |
| Rapida V3 NoHigh — Range Only | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00538 | 1,00972 | 1,01664 | 1,33548 | 0,98849 | €1.549,60 | €4.648,80 | €52,07 | €-20,07 |
| Rapida V3 NoHigh — Regime Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.581,87 | €4.745,62 | €53,15 | €28,35 |
| Rapida V3 NoHigh — Regime Guard | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €144,63 | €433,88 | €52,07 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,82358 | €144,27 | €432,81 | €51,94 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93367 | 0,93367 | 1,04571 | 1,24023 | 0,76561 | €135,90 | €407,70 | €48,92 | €-0,00 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00972 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €1,66 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 63426,03000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €-1,09 |
| MAIN — Side × Regime Guard | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,03900 | 1,03900 | 1,03900 | 1,38014 | 0,78964 | €144,10 | €432,31 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €0,08 |
| Combo Trend — Side × Regime Guard | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend — Side × Regime Guard | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €209,53 | €419,07 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07023 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-25,44 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00972 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €-16,38 |
| Combo Trend — Side × Regime Guard | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €0,34 |
| FAST NoHigh <7,5 · SHORT only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63426,03000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.546,22 | €4.638,65 | €51,95 | €27,71 |
| FAST NoHigh <7,5 · SHORT only | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €195,91 | €587,73 | €50,39 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,07023 | 0,07069 | 0,09286 | 0,06873 | €1.499,62 | €4.498,86 | €50,39 | €-20,85 |
| FAST NoHigh <7,5 · SHORT only | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 57,64657 | 57,52600 | 57,00093 | 38,71928 | 58,61503 | €10,59 | €31,77 | €0,36 | €-0,07 |
| FAST NoHigh <7,5 · SHORT only | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €140,23 | €420,70 | €46,71 | €-0,00 |
| Bilanciata V3 · LONG only | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 63426,03000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.068,36 | €3.205,08 | €46,15 | €19,15 |
| Bilanciata V3 · LONG only | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,91879 | €133,24 | €399,72 | €47,97 | €0,00 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 56,61695 | 57,52600 | 57,00586 | 38,02772 | 58,24752 | €8,89 | €26,67 | €0,00 | €0,43 |
| Bilanciata V3 · LONG only | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €1,16 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63426,03000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €49,84 | €34,81 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,04 | €402,07 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €8,86 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €-0,40 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 485,58000 | 493,83011 | 725,16914 | 467,52868 | €12,86 | €25,72 | €0,46 | €-0,03 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63426,03000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €49,91 | €34,86 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,34 | €402,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €8,88 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00972 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €-0,40 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 485,58000 | 493,83011 | 725,16914 | 467,52868 | €12,88 | €25,76 | €0,47 | €-0,03 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Top 5 + BTC — Guard | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00855 | €105,48 | 2,19 | TARGET |
| Top 5 + BTC — Guard + MFE | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00855 | €103,03 | 2,19 | TARGET |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00855 | €106,78 | 2,19 | TARGET |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00855 | €104,94 | 2,19 | TARGET |
| Forza relativa 1H V1 | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00855 | €7,18 | 2,19 | TARGET |
| Master Adaptive Strict3 V1 | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00840 | €91,21 | 1,99 | TARGET |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00777 | €72,26 | 1,48 | TARGET |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00777 | €72,26 | 1,48 | TARGET |
| Rapida V1 — score 6–7,5 | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00777 | €78,09 | 1,48 | TARGET |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | 2026-08-13T20:06:51+00:00 | 0,00777 | €76,02 | 1,48 | TARGET |
| Forza relativa 1H V1 | TUT | SHORT | 2026-08-13T19:39:48+00:00 | 0,04419 | €7,02 | 2,19 | TARGET |
| Master Adaptive V1 | ZEC | LONG | 2026-08-13T19:39:48+00:00 | 482,95066 | €-2,55 | -1,51 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 324/30 | 33/30 | 0,69 | 2,04 | -0,16R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 293/30 | 20/30 | 0,59 | 1,90 | -0,22R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 184/30 | 22/30 | 0,75 | 1,74 | -0,14R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 187/30 | 22/30 | 0,76 | 1,57 | -0,12R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 248/30 | 31/30 | 0,76 | 0,62 | -0,13R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 220/30 | 11/30 | 0,69 | 0,00 | -0,16R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 117/30 | 8/30 | 0,66 | 1,02 | -0,18R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 232/30 | 17/30 | 0,55 | 4,50 | -0,27R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 348/30 | 24/30 | 0,68 | 0,64 | -0,17R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 315/30 | 7/30 | 0,59 | 0,02 | -0,22R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 248/30 | 30/30 | 0,80 | 1,02 | -0,10R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 447/30 | 55/30 | 0,80 | 1,12 | -0,10R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 113/30 | 15/30 | 0,44 | 0,99 | -0,38R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 399/30 | 44/30 | 0,69 | 1,20 | -0,16R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 403/30 | 37/30 | 0,69 | 0,76 | -0,16R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 366/30 | 23/30 | 0,60 | 1,12 | -0,21R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 224/30 | 40/30 | 0,70 | 0,78 | -0,19R | €-7,08 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 20/30 | 0,00 | 1,85 | 0,00R | €18,36 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 24/30 | 14/30 | 0,51 | 0,61 | -0,28R | €-2,07 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 561/30 | 92/30 | 0,89 | 1,00 | -0,06R | €-0,04 | 6,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 37/30 | 0,00 | 0,54 | 0,00R | €-14,82 | 7,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 2/30 | 0,00 | 0,00 | 0,00R | €-28,31 | 1,36% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 201/30 | 54/30 | 1,05 | 0,87 | 0,03R | €-3,14 | 5,62% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 349/30 | 81/30 | 0,91 | 1,16 | -0,05R | €3,19 | 4,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 270/30 | 37/30 | 0,78 | 0,60 | -0,12R | €-8,04 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 171/30 | 28/30 | 0,96 | 1,25 | -0,02R | €4,68 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 370/30 | 54/30 | 0,82 | 0,99 | -0,09R | €-0,19 | 6,15% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 437/30 | 90/30 | 0,86 | 1,12 | -0,07R | €2,72 | 6,15% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 565/30 | 91/30 | 0,78 | 1,03 | -0,12R | €0,52 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 53/30 | 0,00 | 1,50 | 0,00R | €9,70 | 3,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 58/30 | 0,00 | 1,20 | 0,00R | €4,70 | 3,56% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 29/30 | 0,00 | 1,42 | 0,00R | €10,69 | 2,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 341/30 | 100/30 | 0,83 | 1,27 | -0,09R | €5,53 | 3,21% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 535/30 | 101/30 | 0,74 | 0,97 | -0,14R | €-0,51 | 3,95% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 45/30 | 24/30 | 0,54 | 0,76 | -0,28R | €-6,60 | 3,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 555/30 | 114/30 | 0,81 | 0,87 | -0,10R | €-2,76 | 6,75% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 409/30 | 90/30 | 0,79 | 1,05 | -0,11R | €1,11 | 5,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 225/30 | 63/30 | 0,90 | 0,89 | -0,05R | €-2,87 | 4,39% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 229/30 | 58/30 | 0,89 | 0,87 | -0,05R | €-3,39 | 4,70% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 306/30 | 69/30 | 0,85 | 0,56 | -0,08R | €-12,97 | 9,88% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 29/30 | 0,00 | 1,57 | 0,00R | €11,75 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 37/30 | 0,00 | 1,36 | 0,00R | €6,92 | 4,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 452/30 | 79/30 | 0,78 | 0,81 | -0,12R | €-4,75 | 5,62% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 49/30 | 0,00 | 0,68 | 0,00R | €-8,91 | 7,90% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 70/30 | 0,00 | 0,82 | 0,00R | €-3,59 | 6,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 29/30 | 0,00 | 0,84 | 0,00R | €-4,11 | 3,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 508/30 | 88/30 | 0,76 | 0,75 | -0,13R | €-5,82 | 6,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 209/30 | 34/30 | 0,70 | 0,86 | -0,21R | €-3,68 | 4,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 172/30 | 66/30 | 1,11 | 0,80 | 0,05R | €-5,23 | 6,53% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 10/30 | 4/30 | 0,72 | 0,63 | -0,13R | €-10,11 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 13/30 | 5/30 | 0,24 | 0,97 | -0,59R | €-0,63 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 4/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 13/30 | 7/30 | 0,78 | 0,48 | -0,13R | €-20,19 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,23% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 454/30 | 55/30 | 0,93 | 0,81 | -0,04R | €-3,60 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 245/30 | 33/30 | 0,89 | 0,65 | -0,06R | €-9,02 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 473/30 | 69/30 | 0,93 | 0,39 | -0,03R | €-14,66 | 10,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 395/30 | 56/30 | 0,87 | 0,52 | -0,07R | €-10,50 | 6,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 44/30 | 11/30 | 1,58 | 0,71 | 0,22R | €-7,09 | 1,95% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 44/30 | 11/30 | 1,45 | 0,31 | 0,17R | €-18,43 | 2,40% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 121/30 | 31/30 | 0,89 | 0,83 | -0,05R | €-3,27 | 3,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 161/30 | 22/30 | 0,85 | 0,79 | -0,08R | €-4,40 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 62/30 | 0,74 | 0,71 | -0,20R | €-5,91 | 6,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 50/30 | 0,00 | 1,11 | 0,00R | €2,08 | 5,79% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 43/30 | 0,74 | 0,47 | -0,20R | €-12,70 | 6,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 81/30 | 28/30 | 1,25 | 0,72 | 0,11R | €-9,57 | 4,71% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_SCANNER | Combo Scanner | 281/30 | 63/30 | 1,04 | 0,56 | 0,02R | €-12,89 | 10,13% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 376/30 | 87/30 | 0,87 | 0,74 | -0,08R | €-7,19 | 9,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 42/30 | 0,00 | 1,07 | 0,00R | €1,38 | 2,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 11/30 | 9/30 | 0,59 | 0,77 | -0,29R | €-5,63 | 1,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 17/30 | 12/30 | 0,39 | 0,94 | -0,44R | €-1,28 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 188/30 | 57/30 | 0,81 | 1,43 | -0,12R | €10,58 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 118/30 | 25/30 | 0,76 | 1,65 | -0,14R | €14,13 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 379/30 | 57/30 | 0,85 | 0,55 | -0,09R | €-11,48 | 7,38% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 14/30 | 8/30 | 0,30 | 0,05 | -0,56R | €-38,45 | 3,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 12/30 | 6/30 | 0,31 | 0,34 | -0,58R | €-30,47 | 2,06% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 19/30 | 10/30 | 0,31 | 0,12 | -0,52R | €-37,78 | 3,78% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 12/30 | 15/30 | 0,89 | 0,35 | -0,07R | €-21,51 | 3,52% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 229/30 | 38/30 | 0,98 | 0,77 | -0,01R | €-7,49 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 38/30 | 0,00 | 0,60 | 0,00R | €-11,94 | 6,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 31/30 | 0,00 | 0,32 | 0,00R | €-28,98 | 10,58% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 33/30 | 0,00 | 0,57 | 0,00R | €-14,06 | 6,27% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 417/30 | 70/30 | 1,32 | 0,57 | 0,11R | €-8,96 | 7,33% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 202/30 | 34/30 | 0,99 | 0,67 | -0,01R | €-11,99 | 6,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 210/30 | 33/30 | 0,94 | 0,51 | -0,04R | €-18,79 | 6,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 142/30 | 37/30 | 0,96 | 0,53 | -0,03R | €-20,15 | 9,06% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 223/30 | 35/30 | 0,94 | 0,60 | -0,04R | €-14,31 | 6,08% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 475/30 | 76/30 | 0,82 | 0,67 | -0,10R | €-7,72 | 8,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 187/30 | 64/30 | 1,15 | 0,83 | 0,08R | €-5,51 | 8,11% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 157/30 | 44/30 | 0,52 | 0,72 | -0,27R | €-6,65 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 157/30 | 44/30 | 0,52 | 0,72 | -0,27R | €-6,65 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 157/30 | 44/30 | 0,52 | 0,72 | -0,27R | €-6,65 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 191/30 | 64/30 | 0,73 | 0,68 | -0,14R | €-6,99 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 180/30 | 36/30 | 0,77 | 0,58 | -0,11R | €-9,96 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 161/30 | 37/30 | 0,66 | 0,53 | -0,16R | €-10,08 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 217/30 | 37/30 | 0,94 | 0,42 | -0,03R | €-18,57 | 9,13% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 218/30 | 37/30 | 0,93 | 0,42 | -0,04R | €-18,57 | 9,13% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 218/30 | 37/30 | 0,93 | 0,42 | -0,04R | €-18,57 | 9,13% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 270/30 | 53/30 | 1,06 | 0,82 | 0,03R | €-4,86 | 8,43% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 124/30 | 10/30 | 0,87 | 0,87 | -0,07R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 224/30 | 34/30 | 0,88 | 0,39 | -0,07R | €-20,30 | 8,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 231/30 | 47/30 | 1,12 | 0,71 | 0,06R | €-7,95 | 5,80% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 195/30 | 32/30 | 0,99 | 0,80 | -0,01R | €-6,43 | 6,54% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 241/30 | 54/30 | 1,13 | 0,64 | 0,06R | €-10,18 | 7,59% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 202/30 | 37/30 | 1,00 | 0,72 | 0,00R | €-8,77 | 6,13% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 276/30 | 46/30 | 1,03 | 0,31 | 0,01R | €-18,87 | 9,46% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 220/30 | 42/30 | 0,92 | 0,51 | -0,04R | €-14,91 | 9,42% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 209/30 | 38/30 | 0,93 | 0,51 | -0,04R | €-16,33 | 9,13% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 295/30 | 65/30 | 1,08 | 1,07 | 0,04R | €1,71 | 7,66% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 20/30 | 9/30 | 0,38 | 0,17 | -0,51R | €-36,20 | 3,94% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 2/30 | 2/30 | 1,18 | 0,65 | 0,10R | €-8,96 | 0,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 11/30 | 5/30 | 0,61 | 0,82 | -0,24R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 13/30 | 6/30 | 0,60 | 1,02 | -0,31R | €0,34 | 1,50% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 2/30 | 2/30 | 1,29 | 0,71 | 0,15R | €-7,50 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 18/30 | 8/30 | 0,54 | 0,43 | -0,36R | €-23,29 | 2,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,05R | €-51,41 | 1,57% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07023**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 29.6 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63426.03 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07023**; close **0.07016**; wick alta **0.0%**; volume **x0.23**

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
- Confidenza: **68,90%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC ribassista confermato dalla breadth: score -3.0, 42% sopra EMA50, ADX 24.2.
- BTC trend score: **-3,00**; ADX: **24,19**; breadth sopra EMA50: **41,67%**
- Mediana alt vs BTC: **0,31%**; dispersione: **27,33%**

- Aperti in questo ciclo: **52**
- Chiusi in questo ciclo: **56**
- Posizioni research aperte: **575**
- Trade research chiusi: **21805**
- Eventi di mercato indipendenti chiusi: **3096**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **56553**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 5 | 324 | 324 | 29,94% | 0,69 | -0,16R | €-530,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 5 | 293 | 293 | 29,01% | 0,59 | -0,22R | €-646,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 3 | 184 | 184 | 44,02% | 0,75 | -0,14R | €-250,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 3 | 187 | 187 | 32,62% | 0,76 | -0,12R | €-232,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 4 | 248 | 248 | 31,85% | 0,76 | -0,13R | €-312,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 4 | 220 | 220 | 32,27% | 0,69 | -0,16R | €-351,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 3 | 117 | 117 | 33,33% | 0,66 | -0,18R | €-214,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 6 | 232 | 232 | 27,16% | 0,55 | -0,27R | €-624,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 7 | 348 | 348 | 29,60% | 0,68 | -0,17R | €-593,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 7 | 315 | 315 | 28,57% | 0,59 | -0,22R | €-696,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 4 | 248 | 248 | 32,66% | 0,80 | -0,10R | €-252,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 7 | 447 | 447 | 40,04% | 0,80 | -0,10R | €-429,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 113 | 113 | 27,43% | 0,44 | -0,38R | €-428,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 7 | 399 | 399 | 29,32% | 0,69 | -0,16R | €-658,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 7 | 403 | 403 | 29,28% | 0,69 | -0,16R | €-658,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 7 | 366 | 366 | 28,14% | 0,60 | -0,21R | €-784,71 |
| MAIN | 14 | 224 | 224 | 25,45% | 0,70 | -0,19R | €-423,83 |
| RSI_EXTREME_LONG_15M | 0 | 24 | 24 | 41,67% | 0,51 | -0,28R | €-68,24 |
| RSI_EXTREME_SHORT_15M | 0 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 19 | 561 | 561 | 33,51% | 0,89 | -0,06R | €-347,63 |
| Bilanciata 1H V2 | 6 | 228 | 201 | 37,28% | 1,05 | 0,03R | €68,23 |
| Bilanciata 1H V3 Filtered | 14 | 349 | 349 | 33,81% | 0,91 | -0,05R | €-181,60 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 14 | 270 | 270 | 32,22% | 0,78 | -0,12R | €-326,95 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 1 | 171 | 171 | 38,01% | 0,96 | -0,02R | €-31,73 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 8 | 370 | 370 | 34,86% | 0,82 | -0,09R | €-338,10 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 8 | 437 | 437 | 36,16% | 0,86 | -0,07R | €-303,76 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 9 | 565 | 565 | 34,16% | 0,78 | -0,12R | €-658,93 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 341 | 341 | 35,19% | 0,83 | -0,09R | €-308,18 |
| SHADOW_1H_FAST_TP2_V1 | 9 | 535 | 535 | 30,84% | 0,74 | -0,14R | €-755,55 |
| Rapida 1H V2 | 1 | 53 | 45 | 33,96% | 0,54 | -0,28R | €-147,64 |
| Rapida 1H V3 Filtered | 7 | 555 | 555 | 34,77% | 0,81 | -0,10R | €-573,68 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 5 | 409 | 409 | 34,47% | 0,79 | -0,11R | €-454,57 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 225 | 225 | 46,22% | 0,90 | -0,05R | €-121,25 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 229 | 229 | 37,12% | 0,89 | -0,05R | €-125,22 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 306 | 306 | 36,27% | 0,85 | -0,08R | €-247,52 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 7 | 452 | 452 | 34,07% | 0,78 | -0,12R | €-541,64 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 7 | 508 | 508 | 33,66% | 0,76 | -0,13R | €-655,64 |
| SHADOW_4H_WIDE | 25 | 209 | 209 | 20,57% | 0,70 | -0,21R | €-430,02 |
| SHADOW_BOLLINGER_MR_1H | 0 | 172 | 172 | 48,26% | 1,11 | 0,05R | €86,27 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 10 | 10 | 60,00% | 0,72 | -0,13R | €-12,66 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 13 | 13 | 30,77% | 0,24 | -0,59R | €-76,75 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,93 |
| SHADOW_BTC_EMA_1H | 1 | 13 | 13 | 46,15% | 0,78 | -0,13R | €-17,00 |
| SHADOW_BTC_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 14 | 454 | 454 | 36,12% | 0,93 | -0,04R | €-160,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 8 | 245 | 245 | 35,10% | 0,89 | -0,06R | €-139,35 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 12 | 473 | 473 | 40,17% | 0,93 | -0,03R | €-152,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 14 | 395 | 395 | 37,97% | 0,87 | -0,07R | €-267,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 44 | 44 | 50,00% | 1,58 | 0,22R | €98,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 44 | 44 | 38,64% | 1,45 | 0,17R | €75,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 2 | 121 | 121 | 32,23% | 0,89 | -0,05R | €-64,87 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 2 | 161 | 161 | 34,78% | 0,85 | -0,08R | €-124,58 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 81 | 81 | 49,38% | 1,25 | 0,11R | €89,20 |
| SHADOW_COMBO_SCANNER | 10 | 281 | 281 | 34,88% | 1,04 | 0,02R | €65,79 |
| SHADOW_COMBO_TREND | 15 | 376 | 376 | 30,59% | 0,87 | -0,08R | €-293,43 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 11 | 11 | 36,36% | 0,59 | -0,29R | €-32,37 |
| SHADOW_DOGE_EMA_1H | 1 | 17 | 17 | 23,53% | 0,39 | -0,44R | €-74,91 |
| SHADOW_DONCHIAN_1H | 6 | 188 | 188 | 29,26% | 0,81 | -0,12R | €-233,45 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 6 | 118 | 118 | 31,36% | 0,76 | -0,14R | €-168,36 |
| SHADOW_EMA_TREND_1H | 14 | 379 | 379 | 29,82% | 0,85 | -0,09R | €-340,37 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 14 | 14 | 28,57% | 0,30 | -0,56R | €-77,90 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 12 | 12 | 25,00% | 0,31 | -0,58R | €-70,11 |
| SHADOW_ETH_EMA_1H | 0 | 19 | 19 | 31,58% | 0,31 | -0,52R | €-99,06 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 1 | 12 | 12 | 41,67% | 0,89 | -0,07R | €-8,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 8 | 229 | 229 | 32,31% | 0,98 | -0,01R | €-29,09 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 417 | 417 | 64,99% | 1,32 | 0,11R | €445,27 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 7 | 202 | 202 | 32,18% | 0,99 | -0,01R | €-18,25 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 8 | 210 | 210 | 30,00% | 0,94 | -0,04R | €-79,86 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 142 | 142 | 31,69% | 0,96 | -0,03R | €-39,06 |
| SHADOW_MASTER_ADAPTIVE_V1 | 8 | 223 | 223 | 31,39% | 0,94 | -0,04R | €-95,11 |
| Forza relativa 1H V1 | 16 | 475 | 475 | 28,63% | 0,82 | -0,10R | €-481,12 |
| Forza relativa 1H V2 | 8 | 201 | 187 | 36,32% | 1,15 | 0,08R | €154,86 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 10 | 157 | 157 | 26,75% | 0,52 | -0,27R | €-426,89 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 10 | 157 | 157 | 26,75% | 0,52 | -0,27R | €-426,89 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 10 | 157 | 157 | 26,75% | 0,52 | -0,27R | €-426,89 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 191 | 191 | 29,84% | 0,73 | -0,14R | €-275,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 8 | 180 | 180 | 51,11% | 0,77 | -0,11R | €-193,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 8 | 161 | 161 | 49,69% | 0,66 | -0,16R | €-254,59 |
| SHADOW_SCANNER_TOP10_LONG | 8 | 217 | 217 | 34,56% | 0,94 | -0,03R | €-67,97 |
| SHADOW_SCANNER_TOP15_LONG | 8 | 218 | 218 | 34,40% | 0,93 | -0,04R | €-79,08 |
| SHADOW_SCANNER_TOP20_LONG | 8 | 218 | 218 | 34,40% | 0,93 | -0,04R | €-79,08 |
| SHADOW_SCANNER_TOP5_BTC | 9 | 270 | 270 | 34,44% | 1,06 | 0,03R | €87,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 1 | 124 | 124 | 31,45% | 0,87 | -0,07R | €-90,72 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 8 | 224 | 224 | 32,14% | 0,88 | -0,07R | €-155,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 231 | 231 | 44,16% | 1,12 | 0,06R | €129,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 195 | 195 | 33,85% | 0,99 | -0,01R | €-10,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 241 | 241 | 43,98% | 1,13 | 0,06R | €140,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 6 | 202 | 202 | 33,66% | 1,00 | 0,00R | €0,40 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 8 | 276 | 276 | 42,39% | 1,03 | 0,01R | €36,78 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 9 | 220 | 220 | 31,36% | 0,92 | -0,04R | €-95,85 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 9 | 209 | 209 | 31,10% | 0,93 | -0,04R | €-76,83 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 295 | 295 | 36,27% | 1,08 | 0,04R | €121,47 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 20 | 20 | 25,00% | 0,38 | -0,51R | €-102,79 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,93 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 11 | 11 | 45,45% | 0,61 | -0,24R | €-26,43 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 13 | 13 | 30,77% | 0,60 | -0,31R | €-40,17 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 2 | 2 | 50,00% | 1,29 | 0,15R | €3,02 |
| SHADOW_SOL_EMA_1H | 0 | 18 | 18 | 27,78% | 0,54 | -0,36R | €-65,49 |
| SHADOW_SOL_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,62 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 36 | 36 | 22,22% | 0,48 | -0,32R | €-116,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 1 | 51 | 51 | 43,14% | 1,38 | 0,17R | €88,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 109 | 109 | 33,94% | 0,64 | -0,19R | €-202,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,22 | -0,53R | €-42,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 33 | 33 | 33,33% | 1,09 | 0,05R | €14,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 4 | 28 | 28 | 25,00% | 0,39 | -0,41R | €-114,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 52 | 52 | 17,31% | 0,47 | -0,26R | €-137,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 35 | 35 | 20,00% | 0,30 | -0,49R | €-170,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 1 | 38 | 38 | 44,74% | 1,58 | 0,24R | €91,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 102 | 102 | 33,33% | 0,53 | -0,24R | €-249,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,17 | -0,64R | €-44,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 32 | 32 | 34,38% | 1,23 | 0,12R | €37,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 4 | 25 | 25 | 24,00% | 0,26 | -0,49R | €-122,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 49 | 49 | 16,33% | 0,31 | -0,36R | €-177,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,78 | -0,12R | €-7,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 1 | 43 | 43 | 55,81% | 1,36 | 0,16R | €67,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 64 | 64 | 39,06% | 0,48 | -0,33R | €-208,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 1 | 15 | 15 | 46,67% | 1,02 | 0,01R | €1,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 1 | 17 | 17 | 35,29% | 0,43 | -0,38R | €-64,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 1,08 | 0,04R | €1,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 1 | 45 | 45 | 42,22% | 1,30 | 0,13R | €60,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-207,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 16 | 16 | 31,25% | 1,10 | 0,05R | €7,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 2 | 17 | 17 | 29,41% | 0,53 | -0,34R | €-57,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 1 | 49 | 49 | 38,78% | 1,08 | 0,04R | €20,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 78 | 78 | 33,33% | 0,62 | -0,22R | €-170,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 22 | 22 | 36,36% | 1,49 | 0,18R | €40,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 3 | 21 | 21 | 33,33% | 0,63 | -0,26R | €-54,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,18 | -0,48R | €-43,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 1 | 41 | 41 | 39,02% | 1,14 | 0,07R | €27,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 68 | 68 | 35,29% | 0,55 | -0,24R | €-163,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,92R | €-55,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 21 | 21 | 38,10% | 1,83 | 0,29R | €60,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 3 | 20 | 20 | 35,00% | 0,52 | -0,32R | €-64,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 3 | 115 | 115 | 33,04% | 0,64 | -0,19R | €-223,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 1 | 50 | 50 | 32,00% | 0,78 | -0,12R | €-61,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 102 | 102 | 32,35% | 0,64 | -0,20R | €-200,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 17 | 17 | 11,76% | 0,34 | -0,44R | €-74,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 3 | 30 | 30 | 30,00% | 0,50 | -0,31R | €-92,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,14 | -0,67R | €-161,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 60 | 60 | 36,67% | 1,09 | 0,04R | €26,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 132 | 132 | 32,58% | 0,64 | -0,19R | €-257,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 25 | 25 | 24,00% | 0,72 | -0,13R | €-32,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 5 | 33 | 33 | 33,33% | 0,59 | -0,24R | €-79,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 71 | 71 | 23,94% | 0,65 | -0,17R | €-119,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,09 | -0,71R | €-171,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 1 | 48 | 48 | 37,50% | 1,14 | 0,07R | €33,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 123 | 123 | 31,71% | 0,57 | -0,23R | €-282,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 24 | 24 | 25,00% | 0,79 | -0,09R | €-21,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 5 | 30 | 30 | 33,33% | 0,56 | -0,26R | €-78,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 66 | 66 | 22,73% | 0,47 | -0,27R | €-176,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 1 | 50 | 50 | 40,00% | 1,16 | 0,08R | €40,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 78 | 78 | 35,90% | 0,74 | -0,14R | €-110,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 22 | 22 | 36,36% | 1,49 | 0,18R | €40,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 3 | 21 | 21 | 33,33% | 0,63 | -0,26R | €-54,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 0 | 53 | 53 | 32,08% | 0,42 | -0,35R | €-184,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 1 | 64 | 64 | 46,88% | 1,06 | 0,03R | €19,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 146 | 146 | 37,67% | 0,79 | -0,10R | €-143,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 18 | 18 | 33,33% | 0,47 | -0,34R | €-61,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 38 | 38 | 47,37% | 1,35 | 0,12R | €43,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 5 | 40 | 40 | 45,00% | 0,77 | -0,11R | €-42,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 81 | 81 | 40,74% | 0,84 | -0,07R | €-56,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 15 | 15 | 26,67% | 0,68 | -0,24R | €-35,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 1 | 47 | 47 | 36,17% | 0,44 | -0,34R | €-159,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,76 | 0,41R | €8,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 9 | 9 | 33,33% | 0,74 | -0,10R | €-8,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 58 | 58 | 36,21% | 1,06 | 0,03R | €16,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 1 | 128 | 128 | 32,03% | 0,62 | -0,20R | €-262,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,35 | -0,42R | €-76,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 35 | 35 | 37,14% | 1,51 | 0,20R | €69,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 5 | 33 | 33 | 33,33% | 0,59 | -0,24R | €-79,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 60 | 60 | 36,67% | 1,09 | 0,04R | €26,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 1 | 129 | 129 | 31,78% | 0,62 | -0,21R | €-272,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,35 | -0,42R | €-76,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 35 | 35 | 37,14% | 1,51 | 0,20R | €69,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 5 | 33 | 33 | 33,33% | 0,59 | -0,24R | €-79,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,26 | -0,48R | €-230,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 1 | 48 | 48 | 37,50% | 1,14 | 0,07R | €33,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 1 | 121 | 121 | 30,58% | 0,49 | -0,28R | €-333,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,36 | -0,44R | €-61,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 34 | 34 | 38,24% | 1,77 | 0,28R | €96,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 5 | 30 | 30 | 33,33% | 0,56 | -0,26R | €-78,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 65 | 65 | 21,54% | 0,39 | -0,31R | €-201,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,89 | -0,05R | €-10,79 |
| MAIN | ALT_ROTATION_UP | 4 | 38 | 38 | 18,42% | 0,33 | -0,49R | €-186,82 |
| MAIN | RANGE | 4 | 69 | 69 | 21,74% | 0,64 | -0,23R | €-160,37 |
| MAIN | RANGE_HIGH_VOL | 0 | 10 | 10 | 30,00% | 1,06 | 0,03R | €2,61 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 1 | 21 | 21 | 23,81% | 0,52 | -0,35R | €-74,24 |
| MAIN | TREND_DOWN | 2 | 19 | 19 | 26,32% | 0,71 | -0,18R | €-33,28 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 2 | 37 | 37 | 29,73% | 0,96 | -0,02R | €-8,04 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,42 | 0,25R | €17,52 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 4 | 4 | 75,00% | 5,55 | 0,50R | €20,01 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 0,85 | -0,07R | €-9,35 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 21,43% | 0,44 | -0,39R | €-221,17 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 2 | 79 | 79 | 35,44% | 0,99 | -0,01R | €-4,93 |
| Bilanciata 1H V1 | RANGE | 3 | 164 | 164 | 39,02% | 1,06 | 0,03R | €55,82 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 27 | 27 | 18,52% | 0,35 | -0,49R | €-131,16 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 1 | 71 | 71 | 40,85% | 1,24 | 0,13R | €91,68 |
| Bilanciata 1H V1 | TREND_DOWN | 10 | 35 | 35 | 31,43% | 0,68 | -0,18R | €-62,84 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 2 | 107 | 107 | 30,84% | 0,93 | -0,04R | €-39,55 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 4 | 54 | 48 | 37,04% | 1,12 | 0,06R | €33,13 |
| Bilanciata 1H V2 | RANGE | 2 | 117 | 105 | 35,04% | 0,82 | -0,11R | €-126,88 |
| Bilanciata 1H V2 | TRANSITION | 0 | 57 | 48 | 42,11% | 1,61 | 0,28R | €161,98 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 42 | 42 | 26,19% | 0,54 | -0,30R | €-128,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 1 | 43 | 43 | 32,56% | 1,18 | 0,10R | €42,44 |
| Bilanciata 1H V3 Filtered | RANGE | 3 | 111 | 111 | 40,54% | 1,08 | 0,04R | €42,84 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 7 | 7 | 28,57% | 0,50 | -0,37R | €-26,19 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 37 | 37 | 35,14% | 1,09 | 0,05R | €19,63 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 7 | 28 | 28 | 28,57% | 0,32 | -0,45R | €-126,58 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 61 | 61 | 31,15% | 1,06 | 0,03R | €18,88 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 19,35% | 0,26 | -0,52R | €-161,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 41 | 41 | 34,15% | 1,30 | 0,15R | €63,43 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 3 | 89 | 89 | 38,20% | 0,84 | -0,08R | €-73,32 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 5 | 5 | 40,00% | 0,83 | -0,11R | €-5,36 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 29 | 29 | 34,48% | 1,09 | 0,05R | €13,94 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 7 | 29 | 29 | 27,59% | 0,30 | -0,47R | €-137,69 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 1 | 40 | 40 | 25,00% | 0,78 | -0,10R | €-41,96 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,25 | -0,50R | €-54,74 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 42 | 42 | 50,00% | 1,35 | 0,14R | €56,92 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 42 | 42 | 38,10% | 0,93 | -0,04R | €-16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 30,61% | 0,80 | -0,08R | €-38,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 15,79% | 0,25 | -0,52R | €-99,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 1 | 62 | 62 | 46,77% | 1,20 | 0,09R | €54,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 2 | 140 | 140 | 35,71% | 0,79 | -0,11R | €-154,85 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 33 | 33 | 36,36% | 0,94 | -0,03R | €-8,31 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 5 | 40 | 40 | 30,00% | 0,63 | -0,22R | €-89,43 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 73 | 73 | 27,40% | 0,74 | -0,12R | €-84,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 18,92% | 0,33 | -0,49R | €-181,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 63 | 63 | 47,62% | 1,25 | 0,11R | €68,46 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 2 | 170 | 170 | 40,00% | 0,99 | -0,01R | €-9,66 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 35 | 35 | 40,00% | 1,14 | 0,06R | €21,38 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 5 | 40 | 40 | 30,00% | 0,63 | -0,22R | €-89,43 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 89 | 89 | 26,97% | 0,65 | -0,18R | €-156,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 77 | 77 | 20,78% | 0,38 | -0,43R | €-330,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 1 | 70 | 70 | 40,00% | 0,92 | -0,04R | €-29,81 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 2 | 191 | 191 | 36,65% | 0,81 | -0,10R | €-190,16 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 20 | 20 | 40,00% | 0,96 | -0,02R | €-4,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 49 | 49 | 42,86% | 1,39 | 0,15R | €73,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 6 | 45 | 45 | 35,56% | 0,71 | -0,17R | €-75,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 104 | 104 | 27,88% | 0,70 | -0,15R | €-160,49 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 22,73% | 0,37 | -0,46R | €-202,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 49 | 49 | 38,78% | 0,97 | -0,02R | €-7,93 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 112 | 112 | 42,86% | 1,13 | 0,06R | €70,10 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 50,00% | 1,08 | 0,04R | €3,46 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 34 | 34 | 41,18% | 1,24 | 0,10R | €35,46 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 4 | 30 | 30 | 23,33% | 0,48 | -0,33R | €-98,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,60 | -0,22R | €-127,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 75 | 75 | 20,00% | 0,42 | -0,40R | €-298,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 1 | 72 | 72 | 41,67% | 1,13 | 0,06R | €45,66 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 175 | 175 | 34,29% | 0,77 | -0,13R | €-219,21 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,51 | -0,30R | €-57,10 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 47 | 47 | 40,43% | 1,63 | 0,24R | €114,48 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 6 | 41 | 41 | 34,15% | 0,63 | -0,22R | €-91,51 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 95 | 95 | 21,05% | 0,53 | -0,25R | €-237,49 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 1 | 39 | 32 | 35,90% | 0,67 | -0,18R | €-71,56 |
| Rapida 1H V2 | TRANSITION | 0 | 4 | 4 | 50,00% | 0,71 | -0,09R | €-3,53 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 74 | 74 | 20,27% | 0,37 | -0,43R | €-315,89 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 67 | 67 | 40,30% | 1,00 | -0,00R | €-1,42 |
| Rapida 1H V3 Filtered | RANGE | 1 | 171 | 171 | 36,84% | 0,81 | -0,10R | €-170,90 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 19 | 19 | 36,84% | 0,84 | -0,09R | €-17,03 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 45 | 45 | 42,22% | 1,29 | 0,12R | €55,52 |
| Rapida 1H V3 Filtered | TREND_DOWN | 5 | 43 | 43 | 30,23% | 0,61 | -0,23R | €-97,22 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 108 | 108 | 37,04% | 1,00 | 0,00R | €0,97 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-232,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 58 | 58 | 43,10% | 1,11 | 0,05R | €30,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 140 | 140 | 38,57% | 0,92 | -0,04R | €-58,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,84 | -0,08R | €-8,44 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 36 | 36 | 38,89% | 1,02 | 0,01R | €3,89 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 4 | 34 | 34 | 23,53% | 0,50 | -0,30R | €-103,50 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 69 | 69 | 28,99% | 0,67 | -0,17R | €-116,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 23,08% | 0,19 | -0,65R | €-84,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 1 | 48 | 48 | 56,25% | 1,21 | 0,09R | €43,66 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 79 | 79 | 43,04% | 0,86 | -0,08R | €-63,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 1 | 16 | 16 | 50,00% | 1,26 | 0,12R | €18,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 1 | 20 | 20 | 35,00% | 0,68 | -0,21R | €-42,79 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 16,67% | 0,19 | -0,63R | €-75,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 49 | 49 | 42,86% | 1,07 | 0,03R | €16,55 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 81 | 81 | 39,51% | 0,94 | -0,03R | €-27,15 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 17 | 17 | 41,18% | 1,22 | 0,10R | €16,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 2 | 20 | 20 | 30,00% | 0,66 | -0,23R | €-45,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 5,56% | 0,10 | -0,73R | €-131,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 58 | 58 | 39,66% | 0,94 | -0,03R | €-18,37 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 97 | 97 | 40,21% | 0,92 | -0,04R | €-38,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,27 | -0,57R | €-40,24 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 25 | 25 | 44,00% | 1,33 | 0,14R | €34,11 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 3 | 27 | 27 | 33,33% | 0,69 | -0,20R | €-54,75 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 17,39% | 0,32 | -0,51R | €-234,33 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 1 | 64 | 64 | 39,06% | 0,94 | -0,03R | €-18,85 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 173 | 173 | 38,15% | 0,86 | -0,07R | €-122,85 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 29 | 29 | 34,48% | 1,06 | 0,02R | €6,56 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 5 | 43 | 43 | 30,23% | 0,61 | -0,23R | €-97,22 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 94 | 94 | 31,91% | 0,79 | -0,11R | €-104,22 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 73 | 73 | 20,55% | 0,38 | -0,42R | €-304,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 1 | 66 | 66 | 37,88% | 0,88 | -0,06R | €-42,54 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 169 | 169 | 36,69% | 0,80 | -0,11R | €-185,63 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 38,89% | 0,93 | -0,04R | €-6,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 40 | 40 | 42,50% | 1,37 | 0,15R | €58,29 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 5 | 43 | 43 | 30,23% | 0,61 | -0,23R | €-97,22 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 91 | 91 | 30,77% | 0,75 | -0,13R | €-121,78 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 1,26 | 0,13R | €18,79 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 4 | 33 | 33 | 24,24% | 0,49 | -0,39R | €-128,82 |
| SHADOW_4H_WIDE | RANGE | 7 | 61 | 61 | 16,39% | 0,62 | -0,28R | €-172,63 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 7 | 7 | 28,57% | 1,10 | 0,07R | €5,07 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 22 | 22 | 13,64% | 0,40 | -0,47R | €-103,38 |
| SHADOW_4H_WIDE | TREND_DOWN | 4 | 20 | 20 | 30,00% | 1,14 | 0,09R | €17,52 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 37 | 37 | 21,62% | 0,91 | -0,05R | €-19,38 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 0,99 | -0,00R | €-0,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 64 | 64 | 48,44% | 1,13 | 0,06R | €37,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-3,07 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 11 | 11 | 54,55% | 2,06 | 0,41R | €45,29 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 11 | 11 | 72,73% | 3,28 | 0,47R | €52,06 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 4 | 4 | 50,00% | 1,16 | 0,09R | €3,64 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,56 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,62 | -0,24R | €-109,67 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 59 | 59 | 35,59% | 0,97 | -0,01R | €-8,05 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 3 | 137 | 137 | 41,61% | 0,97 | -0,02R | €-24,49 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 16 | 16 | 31,25% | 0,83 | -0,09R | €-14,08 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 53 | 53 | 41,51% | 1,41 | 0,21R | €113,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 8 | 31 | 31 | 29,03% | 0,50 | -0,30R | €-93,78 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 93 | 93 | 36,56% | 1,12 | 0,05R | €48,80 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 15,38% | 0,48 | -0,33R | €-42,51 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 35,85% | 1,00 | -0,00R | €-1,04 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 67 | 67 | 47,76% | 1,21 | 0,10R | €70,23 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 23 | 23 | 47,83% | 2,29 | 0,46R | €106,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 4 | 23 | 23 | 26,09% | 0,52 | -0,32R | €-73,77 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 1 | 53 | 53 | 28,30% | 0,61 | -0,19R | €-101,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,58 | -0,25R | €-135,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 66 | 66 | 39,39% | 0,91 | -0,05R | €-30,78 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 2 | 136 | 136 | 41,18% | 1,10 | 0,04R | €61,04 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 17 | 17 | 47,06% | 0,79 | -0,10R | €-17,15 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 40 | 40 | 42,50% | 1,18 | 0,09R | €34,19 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 7 | 43 | 43 | 32,56% | 0,58 | -0,21R | €-88,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 95 | 95 | 50,53% | 1,33 | 0,14R | €128,57 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,65 | -0,22R | €-102,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 57 | 57 | 36,84% | 1,01 | 0,00R | €2,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 3 | 125 | 125 | 44,80% | 1,03 | 0,02R | €19,61 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 42,86% | 1,15 | 0,07R | €9,49 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 36 | 36 | 38,89% | 1,17 | 0,09R | €31,92 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 8 | 31 | 31 | 32,26% | 0,54 | -0,27R | €-84,87 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 1 | 72 | 72 | 37,50% | 0,74 | -0,12R | €-87,32 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 14 | 14 | 35,71% | 1,16 | 0,09R | €11,97 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 14 | 14 | 35,71% | 1,12 | 0,06R | €9,04 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 23,53% | 0,44 | -0,34R | €-57,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 38 | 38 | 39,47% | 1,17 | 0,09R | €34,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,65 | -0,18R | €-10,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 13 | 13 | 38,46% | 1,32 | 0,15R | €19,91 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 2 | 13 | 13 | 30,77% | 0,66 | -0,22R | €-28,31 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 50 | 50 | 40,00% | 1,14 | 0,07R | €36,83 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 1 | 98 | 98 | 34,69% | 0,80 | -0,09R | €-93,10 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,42 | -0,30R | €-33,27 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 2,02 | 0,45R | €22,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 32 | 32 | 50,00% | 1,38 | 0,18R | €57,26 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,79R | €-23,63 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 4 | 4 | 75,00% | 4,12 | 0,88R | €35,34 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 9 | 9 | 66,67% | 1,56 | 0,21R | €18,66 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,21 | -0,55R | €-82,64 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 1,09 | 0,05R | €25,32 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 76 | 76 | 44,74% | 1,40 | 0,20R | €150,28 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,76 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 38 | 38 | 47,37% | 1,73 | 0,34R | €129,44 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 5 | 22 | 22 | 18,18% | 0,36 | -0,45R | €-98,87 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 61 | 61 | 31,15% | 1,02 | 0,01R | €6,58 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 0 | 35 | 35 | 25,71% | 0,65 | -0,21R | €-73,73 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,77 | -0,15R | €-76,54 |
| SHADOW_COMBO_TREND | RANGE | 5 | 113 | 113 | 32,74% | 0,91 | -0,05R | €-59,09 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 12 | 12 | 33,33% | 1,06 | 0,03R | €3,37 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 46 | 46 | 36,96% | 1,22 | 0,13R | €57,58 |
| SHADOW_COMBO_TREND | TREND_DOWN | 7 | 30 | 30 | 23,33% | 0,47 | -0,33R | €-98,42 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 70 | 70 | 30,00% | 1,03 | 0,01R | €10,31 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-52,46 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,61 | -0,25R | €-17,63 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -0,75R | €-45,24 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,97 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 1 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,59 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 27 | 27 | 22,22% | 0,51 | -0,37R | €-98,95 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 22 | 22 | 18,18% | 0,23 | -0,63R | €-139,43 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 55 | 55 | 29,09% | 0,81 | -0,13R | €-70,05 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 9 | 9 | 44,44% | 1,63 | 0,28R | €25,45 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 0 | 17 | 17 | 41,18% | 1,67 | 0,33R | €56,40 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 13 | 13 | 30,77% | 0,45 | -0,35R | €-45,38 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 37 | 37 | 29,73% | 1,09 | 0,05R | €19,00 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,23 | -0,63R | €-107,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 21,43% | 0,16 | -0,64R | €-89,01 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 35 | 35 | 28,57% | 0,62 | -0,24R | €-85,11 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 57,14% | 3,24 | 0,65R | €45,72 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 0 | 10 | 10 | 60,00% | 3,77 | 0,86R | €85,66 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 11 | 11 | 36,36% | 0,51 | -0,32R | €-35,09 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 3 | 23 | 23 | 26,09% | 0,92 | -0,03R | €-7,97 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 0 | 37 | 37 | 24,32% | 0,57 | -0,27R | €-100,46 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 49 | 49 | 28,57% | 0,72 | -0,19R | €-91,58 |
| SHADOW_EMA_TREND_1H | RANGE | 5 | 113 | 113 | 33,63% | 0,99 | -0,00R | €-3,46 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 13 | 13 | 38,46% | 1,56 | 0,23R | €29,62 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 45 | 45 | 35,56% | 1,14 | 0,08R | €37,57 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 7 | 30 | 30 | 23,33% | 0,37 | -0,39R | €-117,66 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 74 | 74 | 28,38% | 0,95 | -0,03R | €-20,43 |
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
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,08 | -0,77R | €-30,63 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,84R | €8,38 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 6 | 6 | 33,33% | 0,68 | -0,24R | €-14,10 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 0,02R | €0,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,69 | -0,22R | €-35,19 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 1 | 33 | 33 | 33,33% | 0,94 | -0,04R | €-13,12 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 73 | 73 | 31,51% | 0,97 | -0,02R | €-16,29 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 2 | 17 | 17 | 47,06% | 1,90 | 0,44R | €74,45 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 2 | 30 | 30 | 36,67% | 1,23 | 0,14R | €40,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 44,44% | 0,85 | -0,08R | €-14,12 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 73 | 73 | 75,34% | 2,04 | 0,27R | €195,75 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 137 | 137 | 64,96% | 1,36 | 0,12R | €162,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 39 | 39 | 69,23% | 1,43 | 0,12R | €48,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 4 | 42 | 42 | 59,52% | 1,19 | 0,08R | €32,02 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 107 | 107 | 62,62% | 1,08 | 0,03R | €31,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,63 | -0,24R | €-34,08 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 75 | 75 | 34,67% | 1,11 | 0,07R | €51,34 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 2 | 16 | 16 | 31,25% | 0,96 | -0,03R | €-4,49 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 2 | 29 | 29 | 37,93% | 1,24 | 0,15R | €42,36 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 1,36 | 0,21R | €18,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 36 | 36 | 27,78% | 0,74 | -0,20R | €-71,92 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 67 | 67 | 31,34% | 1,11 | 0,07R | €45,38 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 2 | 14 | 14 | 35,71% | 1,23 | 0,14R | €19,31 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 2 | 26 | 26 | 38,46% | 1,28 | 0,17R | €43,78 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,90R | €-71,98 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 57 | 57 | 36,84% | 1,14 | 0,09R | €51,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 12 | 12 | 41,67% | 1,89 | 0,39R | €46,35 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 3 | 18 | 18 | 22,22% | 0,60 | -0,30R | €-53,20 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,57 | -0,31R | €-43,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 1 | 35 | 35 | 34,29% | 0,98 | -0,02R | €-5,41 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 70 | 70 | 34,29% | 1,11 | 0,07R | €46,06 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 2 | 16 | 16 | 37,50% | 1,27 | 0,16R | €25,48 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 2 | 27 | 27 | 37,04% | 1,20 | 0,12R | €32,63 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 19,57% | 0,44 | -0,37R | €-168,98 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 33,33% | 0,89 | -0,06R | €-42,82 |
| Forza relativa 1H V1 | RANGE | 4 | 157 | 157 | 31,21% | 0,87 | -0,07R | €-114,56 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 13 | 13 | 7,69% | 0,26 | -0,48R | €-62,75 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 1 | 51 | 51 | 39,22% | 1,35 | 0,18R | €92,51 |
| Forza relativa 1H V1 | TREND_DOWN | 7 | 32 | 32 | 21,88% | 0,56 | -0,27R | €-87,02 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 3 | 92 | 92 | 26,09% | 0,91 | -0,05R | €-44,68 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,64 | -0,21R | €-41,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 26 | 23 | 38,46% | 1,35 | 0,18R | €47,67 |
| Forza relativa 1H V2 | RANGE | 2 | 66 | 64 | 36,36% | 0,95 | -0,03R | €-19,55 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 0 | 28 | 24 | 42,86% | 1,83 | 0,37R | €103,63 |
| Forza relativa 1H V2 | TREND_DOWN | 5 | 17 | 16 | 29,41% | 1,04 | 0,02R | €3,42 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 1 | 35 | 32 | 45,71% | 1,70 | 0,33R | €116,73 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 11 | 11 | 27,27% | 0,63 | -0,21R | €-23,14 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 2 | 55 | 55 | 23,64% | 0,33 | -0,39R | €-212,06 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 16 | 16 | 50,00% | 1,32 | 0,17R | €26,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 6 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 1 | 15 | 15 | 6,67% | 0,29 | -0,30R | €-45,71 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 11 | 11 | 27,27% | 0,63 | -0,21R | €-23,14 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 55 | 55 | 23,64% | 0,33 | -0,39R | €-212,06 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 16 | 16 | 50,00% | 1,32 | 0,17R | €26,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 6 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 1 | 15 | 15 | 6,67% | 0,29 | -0,30R | €-45,71 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 11 | 11 | 27,27% | 0,63 | -0,21R | €-23,14 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 55 | 55 | 23,64% | 0,33 | -0,39R | €-212,06 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 1,27 | 0,12R | €13,95 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 16 | 16 | 50,00% | 1,32 | 0,17R | €26,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 6 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 1 | 15 | 15 | 6,67% | 0,29 | -0,30R | €-45,71 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 12 | 12 | 33,33% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 68 | 68 | 29,41% | 0,64 | -0,19R | €-132,03 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 1,42 | 0,16R | €21,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 31 | 31 | 41,94% | 1,11 | 0,06R | €19,23 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 5 | 14 | 14 | 42,86% | 0,66 | -0,16R | €-22,16 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 22 | 22 | 4,55% | 0,16 | -0,44R | €-96,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 29,63% | 0,29 | -0,48R | €-128,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 2 | 60 | 60 | 56,67% | 0,72 | -0,12R | €-73,65 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 68,75% | 1,69 | 0,22R | €34,79 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 19 | 19 | 63,16% | 1,78 | 0,31R | €58,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 5 | 28 | 28 | 50,00% | 0,73 | -0,12R | €-32,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 1 | 18 | 18 | 44,44% | 0,65 | -0,16R | €-29,35 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,22 | -0,52R | €-124,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 2 | 53 | 53 | 56,60% | 0,43 | -0,24R | €-128,27 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 61,54% | 1,54 | 0,21R | €27,39 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 19 | 19 | 63,16% | 1,88 | 0,35R | €65,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 5 | 21 | 21 | 47,62% | 0,70 | -0,12R | €-25,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 1 | 17 | 17 | 41,18% | 0,34 | -0,33R | €-55,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 50 | 50 | 32,00% | 0,86 | -0,08R | €-38,14 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 58 | 58 | 50,00% | 1,52 | 0,23R | €130,60 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 1 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,52 | -0,34R | €-74,17 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 1 | 47 | 47 | 27,66% | 0,58 | -0,20R | €-94,62 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 51 | 51 | 31,37% | 0,82 | -0,10R | €-49,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 58 | 58 | 50,00% | 1,52 | 0,23R | €130,60 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 1 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,52 | -0,34R | €-74,17 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 1 | 47 | 47 | 27,66% | 0,58 | -0,20R | €-94,62 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 51 | 51 | 31,37% | 0,82 | -0,10R | €-49,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 58 | 58 | 50,00% | 1,52 | 0,23R | €130,60 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 1 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,52 | -0,34R | €-74,17 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 1 | 47 | 47 | 27,66% | 0,58 | -0,20R | €-94,62 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,23 | -0,51R | €-71,62 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 1,09 | 0,05R | €25,90 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 71 | 71 | 45,07% | 1,55 | 0,26R | €183,27 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,76 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 34 | 34 | 47,06% | 1,82 | 0,37R | €127,02 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,36 | -0,45R | €-98,87 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 60 | 60 | 30,00% | 0,96 | -0,02R | €-14,13 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,64R | €-31,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 46 | 46 | 28,26% | 0,81 | -0,10R | €-46,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 0,00% | 0,00 | -0,77R | €-92,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 49 | 49 | 36,73% | 1,02 | 0,01R | €5,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 66 | 66 | 43,94% | 1,40 | 0,20R | €130,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 22 | 22 | 54,55% | 2,71 | 0,56R | €122,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,36 | -0,45R | €-98,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 40 | 40 | 20,00% | 0,46 | -0,32R | €-126,23 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,04 | -0,54R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 38 | 38 | 50,00% | 1,37 | 0,16R | €61,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,35 | -0,46R | €-13,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 23 | 23 | 52,17% | 1,81 | 0,29R | €66,69 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 3 | 25 | 25 | 32,00% | 0,48 | -0,34R | €-85,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -0,75R | €-82,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 33 | 33 | 39,39% | 1,40 | 0,20R | €65,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 20 | 20 | 45,00% | 2,15 | 0,42R | €83,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 3 | 20 | 20 | 20,00% | 0,36 | -0,49R | €-97,48 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,54 | -0,25R | €-38,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 38 | 38 | 50,00% | 1,37 | 0,16R | €61,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,35 | -0,46R | €-13,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 25 | 25 | 48,00% | 1,61 | 0,23R | €56,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 3 | 25 | 25 | 32,00% | 0,48 | -0,34R | €-85,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 49 | 49 | 48,98% | 1,25 | 0,11R | €52,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,26 | -0,47R | €-61,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 33 | 33 | 39,39% | 1,40 | 0,20R | €65,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 70 | 70 | 47,14% | 1,52 | 0,24R | €166,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 21 | 21 | 42,86% | 1,89 | 0,35R | €73,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 3 | 20 | 20 | 20,00% | 0,36 | -0,49R | €-97,48 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 38 | 38 | 21,05% | 0,59 | -0,22R | €-84,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,48 | -0,30R | €-48,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 45,28% | 0,99 | -0,00R | €-1,81 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,40 | 0,16R | €119,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,35 | -0,46R | €-13,67 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 28 | 28 | 46,43% | 1,48 | 0,20R | €55,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 4 | 29 | 29 | 31,03% | 0,52 | -0,28R | €-80,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 59 | 59 | 49,15% | 1,26 | 0,10R | €61,85 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,51 | -0,29R | €-20,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 33,96% | 1,05 | 0,03R | €13,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 62 | 62 | 41,94% | 1,42 | 0,21R | €129,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 22 | 22 | 50,00% | 2,20 | 0,45R | €98,34 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,37 | -0,44R | €-97,37 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 44 | 44 | 20,45% | 0,51 | -0,28R | €-125,08 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,60R | €-41,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 35,85% | 1,00 | -0,00R | €-1,34 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 58 | 58 | 41,38% | 1,44 | 0,23R | €131,53 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 18 | 18 | 50,00% | 3,26 | 0,65R | €117,37 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 4 | 20 | 20 | 20,00% | 0,43 | -0,38R | €-75,42 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 43 | 43 | 20,93% | 0,54 | -0,26R | €-112,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,35 | -0,47R | €-74,87 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 52 | 52 | 34,62% | 0,97 | -0,02R | €-9,35 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 73 | 73 | 49,32% | 1,62 | 0,28R | €201,13 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-41,89 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 37 | 37 | 45,95% | 1,78 | 0,35R | €129,86 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 4 | 22 | 22 | 18,18% | 0,52 | -0,34R | €-74,17 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 1 | 77 | 77 | 35,06% | 1,08 | 0,04R | €29,82 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,84 | -0,09R | €-1,73 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,41 | -0,47R | €-32,89 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,86 | 0,38R | €19,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-13T21:08:33+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **581**
- Scenari virtuali ancora attivi: **11182**
- Gruppi in attesa dell'uscita originale: **375**
- Gruppi con originale chiuso ma Shadow ancora attive: **206**
- Confronti completati: **181956**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 4476 | 4542 | +€8,06 | 50,4% | 1181 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 4476 | 4542 | +€7,07 | 49,3% | 1173 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 4476 | 4542 | +€6,63 | 42,8% | 924 | 102 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 4476 | 4542 | +€5,11 | 42,1% | 885 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 4476 | 4542 | +€4,37 | 40,6% | 1032 | 98 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 4476 | 4542 | +€4,26 | 47,4% | 1319 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 4475 | 4541 | +€5,76 | 47,6% | 1187 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 4474 | 4540 | +€4,42 | 47,9% | 1115 | 176 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 4469 | 4535 | +€5,24 | 33,1% | 557 | 447 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 4468 | 4534 | +€4,30 | 41,4% | 777 | 284 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 4468 | 4534 | +€2,54 | 40,2% | 654 | 476 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 4466 | 4532 | €-0,38 | 46,0% | 846 | 649 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 4466 | 4532 | €-0,71 | 40,1% | 482 | 940 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 4460 | 4526 | +€5,21 | 36,7% | 261 | 706 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 4457 | 4523 | +€0,79 | 33,6% | 474 | 833 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 4449 | 4515 | €-0,21 | 31,3% | 345 | 1049 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 4445 | 4511 | €-5,01 | 32,0% | 209 | 1292 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 4412 | 4478 | €-4,91 | 28,1% | 288 | 1193 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 4399 | 4465 | €-4,05 | 33,5% | 662 | 934 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 4380 | 4446 | €-8,86 | 23,9% | 288 | 1336 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-13T21:09:10+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **181956**
- Valutazioni prodotte: **18793**
- Candidature al Blocco 5: **28**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 147 | 0,423 | 0,384 | 0,330 | 61,9% | 95,8 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 3064 | 0,250 | 0,113 | 0,214 | 54,1% | 87,4 | VALIDATING |
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

Generato: 2026-08-13T21:14:12+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 52 | 100,00% | 1,01 | +€7,53 | +€0,14 | 2,09% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 52 | 100,00% | 1,03 | +€20,88 | +€0,40 | 2,19% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 21 | 100,00% | 0,57 | €-295,11 | €-14,05 | 2,95% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 21 | 95,45% | 0,00 | €-273,37 | €-13,02 | 2,73% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 36 | 100,00% | 0,90 | €-76,10 | €-2,11 | 2,13% | EARLY_NOT_CONFIRMED |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-13T21:07:57+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **43**
- Simulazioni bloccate attive: **111**
- Simulazioni completate nel ciclo: **41**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **477.25 R**
- Profitto virtuale mancato: **504.86 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 202 | 0 | 31541.95 |
| DOWN_20 | 202 | 0 | 63083.90 |
| DOWN_30 | 202 | 0 | 94625.86 |
| DOWN_40 | 202 | 71 | 120921.89 |
| UP_10 | 160 | 0 | 32896.46 |
| UP_20 | 160 | 0 | 65792.91 |
| UP_30 | 160 | 0 | 98689.37 |
| UP_40 | 160 | 67 | 120082.41 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-13T21:05:17+00:00

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

Generato: 2026-08-13T21:14:22+00:00

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

Generato: 2026-08-13T21:14:22+00:00

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

Generato: 2026-08-13T21:14:22+00:00

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

Generato: 2026-08-13T21:14:23+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 15.0 | E | 91 | 1.13 | 0.059 | 8.02 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 14.9 | E | 53 | 1.32 | 0.136 | 5.98 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.1 | E | 100 | 1.05 | 0.025 | 11.67 |
| 4 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 13.2 | E | 42 | 1.26 | 0.115 | 5.48 |
| 5 | SHADOW_DONCHIAN_1H | BASELINE | 13.2 | E | 57 | 1.21 | 0.124 | 8.55 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 13.2 | E | 114 | 0.96 | -0.019 | 13.25 |
| 7 | SHADOW_1H_BALANCED_V3 | BASELINE | 11.6 | E | 81 | 1.04 | 0.019 | 11.07 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 11.2 | E | 37 | 1.22 | 0.109 | 9.51 |
| 9 | SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | BASELINE | 10.6 | E | 58 | 1.05 | 0.030 | 11.67 |
| 10 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 10.2 | E | 90 | 0.93 | -0.040 | 21.02 |

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

Generato: 2026-08-13T21:14:23+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **628**
- Strategie preferite nel regime corrente: **2**
- Strategie da evitare nel regime corrente: **20**
- Memorie contestuali: **296**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.6 | 4 | 99.00 | 0.972 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.5 | 12 | 2.82 | 0.322 | 1.04 |
| 5 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 70.0 | 8 | 2.44 | 0.587 | 2.16 |
| 6 | SHADOW_RSI_LONG_5X_RSI20 | shadow-rsi-long-5x-rsi20 | INSUFFICIENT | 65.1 | 9 | 1.80 | 0.319 | 2.40 |
| 7 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | COMPATIBLE | 61.5 | 35 | 1.49 | 0.210 | 5.17 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 60.0 | 8 | 1.57 | 0.236 | 2.21 |
| 9 | SHADOW_1H_FAST | shadow-1h-fast | COMPATIBLE | 55.1 | 61 | 1.27 | 0.113 | 6.50 |
| 10 | SHADOW_1H_FAST_NO_PEPE_V1 | shadow-1h-fast-no-pepe-v1 | NEUTRAL | 51.1 | 63 | 1.10 | 0.046 | 6.07 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-13T21:14:24+00:00

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

Generato: 2026-08-13T21:07:57+00:00

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
