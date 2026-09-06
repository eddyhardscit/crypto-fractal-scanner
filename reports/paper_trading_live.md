# Paper trading automatico KuCoin

Generato: 2026-09-06T05:18:44+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-06T05:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-06T05:05:31+00:00 | 2026-09-06T05:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-06T04:45:00+00:00 | 2026-09-06T04:45:00+00:00 | 6,2 min | 25,0 min | OK |
| 60m | 12 | 2026-09-06T04:00:00+00:00 | 2026-09-06T04:00:00+00:00 | 6,2 min | 45,0 min | OK |
| 240m | 12 | 2026-09-06T00:00:00+00:00 | 2026-09-06T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend — Side × Regime Guard | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | ZEC | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Adaptive 1H | SOL | 60m | LONG | 5,34 | 5,00 | 0,00 | OPENED | 6,2 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Ema 1H | SOL | 60m | LONG | 5,34 | 5,00 | 0,00 | OPENED | 6,2 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | DOGE | 60m | LONG | 5,04 | 5,00 | 0,00 | OPENED | 6,2 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | 60m | LONG | 5,04 | 5,00 | 0,00 | OPENED | 6,2 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — MFE Trail esistente | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ARB | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC 2–3 | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC 2–3 | ARB | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC≤3 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | DOGE | 60m | LONG | 5,04 | 5,00 | 0,00 | OPENED | 6,2 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | DOGE | 60m | LONG | 5,04 | 5,00 | 0,00 | OPENED | 6,2 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | HYPE | 60m | LONG | 8,26 | 4,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SOL | 60m | LONG | 5,34 | 4,50 | 0,00 | OPENED | 6,2 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | HYPE | 60m | LONG | 8,26 | 5,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | DASH | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,67 | 6,00 | 0,33 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,53 | 6,00 | 0,47 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,91 | 6,00 | 1,09 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 4,90 | 6,00 | 1,10 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,00 | 6,00 | 2,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Bilanciata 1H — LONG senza Range High Vol | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | DASH | 60m | LONG | 9,75 | 5,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — target pieno 2R | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — no volatilità HIGH | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — Long Only | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 senza ESPORTS — Long Only | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | DASH | 60m | LONG | 9,75 | 5,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,27 | -1,84% | €7,71 | €3.000,00 | 0,26% | 5 | 59 | 42,37% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 59 | 3058 | PRIME INDICAZIONI | 100 (mancano 41) |

- Trade del Principale 4H chiusi: **59**; win rate **42,37%**; profit factor **0,88**.
- Expectancy: **€-3,08** per trade; P&L netto: **€-181,91**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,27 | €690,48 | €2.071,43 | €194,16 | €-0,70 |
| TEST | Benchmark Donchian breakout 1H | 7 | €11.566,98 | €3.550,50 | €7.100,99 | €231,34 | €24,44 |
| TEST | MAIN — Side × Regime Guard | 6 | €11.508,55 | €470,58 | €1.411,74 | €165,83 | €334,25 |
| TEST | Scanner Top 5 Long 1H | 7 | €11.382,37 | €1.205,54 | €2.411,09 | €227,65 | €407,08 |
| TEST | Donchian 1H Gb20 120R V1 | 7 | €11.294,64 | €3.466,90 | €6.933,81 | €225,89 | €23,86 |
| TEST | Combo Trend — Side × Regime Guard | 8 | €11.161,57 | €1.474,38 | €2.948,76 | €162,57 | €372,98 |
| TEST | Rapida score 6–7,5 — Cost Aware | 6 | €11.069,93 | €716,47 | €2.149,41 | €167,48 | €0,00 |
| TEST | Combo Adaptive — Long Only | 10 | €10.962,78 | €2.458,63 | €4.917,26 | €217,06 | €395,54 |
| TEST | Scanner Top15 Long | 9 | €10.852,42 | €2.966,35 | €5.932,70 | €217,06 | €381,24 |
| TEST | Scanner Top20 Long | 9 | €10.852,42 | €2.966,35 | €5.932,70 | €217,06 | €381,24 |
| TEST | Combo Adaptive — madre | 9 | €10.753,00 | €1.354,71 | €2.709,42 | €163,02 | €380,91 |
| TEST | Combo Scanner | 8 | €10.678,82 | €1.527,78 | €3.055,57 | €212,04 | €377,45 |
| TEST | Scanner Top 5 + forza BTC 1H | 7 | €10.662,49 | €1.133,67 | €2.267,34 | €213,25 | €381,26 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 2 | €10.647,52 | €816,83 | €2.450,48 | €53,70 | €-0,60 |
| TEST | Scanner Top10 Long | 7 | €10.598,31 | €2.354,93 | €4.709,86 | €210,16 | €383,41 |
| TEST | Rapida V1 — senza PEPE | 7 | €10.578,23 | €1.339,25 | €4.017,76 | €211,57 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 5 | €10.578,15 | €477,99 | €1.433,96 | €104,48 | €-0,16 |
| TEST | Rapida 1H V2 | 4 | €10.524,39 | €3.167,07 | €9.501,20 | €209,94 | €-3,02 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.397,05 | €1.562,50 | €4.687,49 | €207,96 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 8 | €10.396,84 | €1.669,91 | €3.339,81 | €205,51 | €8,65 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 8 | €10.390,76 | €1.668,93 | €3.337,86 | €205,39 | €8,64 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.330,25 | €1.552,46 | €4.657,37 | €206,63 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 8 | €10.320,77 | €2.090,66 | €6.271,98 | €206,42 | €0,31 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.293,59 | €1.341,14 | €4.023,41 | €51,50 | €-3,92 |
| TEST | Rapida V3 NoHigh — Range Only | 3 | €10.293,18 | €1.023,38 | €3.070,15 | €102,35 | €-13,16 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 9 | €10.258,26 | €1.141,10 | €2.282,21 | €105,30 | €349,79 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 2 | €10.236,06 | €283,45 | €850,36 | €102,04 | €-21,90 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.206,43 | €1.074,29 | €2.148,59 | €203,40 | €40,62 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.161,66 | €574,98 | €1.149,96 | €50,72 | €17,55 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 3 | €10.130,56 | €1.075,61 | €3.226,84 | €101,77 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.090,56 | €985,68 | €1.971,36 | €50,34 | €23,12 |
| TEST | Sol Ema 1H | 1 | €10.070,61 | €1.165,90 | €3.497,71 | €50,37 | €-0,70 |
| TEST | Doge Donchian 1H | 0 | €10.066,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 7 | €10.064,80 | €1.048,03 | €2.096,07 | €201,30 | €359,87 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 7 | €10.060,17 | €1.126,02 | €2.252,04 | €201,76 | €330,62 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.054,78 | €1.966,66 | €3.933,32 | €151,23 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 6 | €10.053,19 | €601,17 | €1.803,52 | €150,77 | €-0,01 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 7 | €10.049,48 | €1.124,82 | €2.249,64 | €201,54 | €330,27 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.039,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.023,43 | €636,41 | €1.909,22 | €50,21 | €-17,73 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €10.017,96 | €50,00 | €750,00 | €8,09 | €0,43 |
| TEST | Master Adaptive V1 | 7 | €10.010,60 | €1.120,47 | €2.240,94 | €200,76 | €328,99 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.007,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €10.006,51 | €1.158,48 | €3.475,45 | €50,05 | €-0,69 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €10.003,59 | €10,00 | €150,00 | €1,62 | €0,09 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.996,50 | €817,27 | €1.634,54 | €50,09 | €-19,82 |
| TEST | Top 5 + BTC — solo MFE | 7 | €9.995,56 | €1.062,76 | €2.125,52 | €199,91 | €357,42 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €9.991,36 | €185,32 | €926,58 | €9,99 | €0,53 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 7 | €9.983,46 | €2.378,63 | €7.135,89 | €199,67 | €0,31 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.979,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 5 | €9.951,01 | €2.590,77 | €7.772,30 | €199,09 | €-6,06 |
| TEST | Btc Ema 4H | 1 | €9.943,99 | €887,05 | €1.774,10 | €49,83 | €-21,51 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.927,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.906,26 | €872,82 | €1.745,65 | €48,89 | €71,18 |
| TEST | Master Adaptive Runner25 V1 | 9 | €9.906,22 | €1.426,19 | €2.852,39 | €198,12 | €342,21 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 4 | €9.893,29 | €713,30 | €2.139,90 | €147,42 | €-3,22 |
| TEST | Btc Donchian 4H | 1 | €9.890,79 | €882,31 | €1.764,61 | €49,57 | €-21,39 |
| TEST | Eth Ema 4H | 1 | €9.889,03 | €690,19 | €1.380,39 | €49,44 | €2,75 |
| TEST | Rapida V3 — no volatilità HIGH | 6 | €9.886,07 | €1.297,12 | €3.891,37 | €197,72 | €0,02 |
| TEST | Master Adaptive Gb20 V1 | 7 | €9.878,50 | €1.105,61 | €2.211,23 | €198,11 | €324,65 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €9.860,65 | €2.325,88 | €6.977,65 | €189,11 | €369,88 |
| TEST | Forza relativa 1H V2 | 5 | €9.839,23 | €828,41 | €1.656,82 | €98,36 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 7 | €9.830,73 | €1.023,66 | €2.047,32 | €196,62 | €351,50 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.823,03 | €496,99 | €1.490,96 | €144,94 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.819,89 | €1.363,89 | €4.091,66 | €49,10 | €2,35 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.781,66 | €861,84 | €1.723,69 | €48,27 | €70,28 |
| TEST | Eth Adaptive 1H | 1 | €9.762,70 | €1.128,47 | €3.385,42 | €48,75 | €14,71 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.726,53 | €1.123,27 | €3.369,80 | €0,00 | €23,53 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €9.719,02 | €1.004,71 | €3.014,12 | €145,58 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.717,32 | €1.262,13 | €3.786,39 | €0,00 | €26,43 |
| TEST | Eth Bollinger 1H | 1 | €9.711,84 | €1.349,47 | €4.048,41 | €48,58 | €-1,91 |
| TEST | Bilanciata 1H V1 | 10 | €9.700,72 | €969,94 | €2.909,82 | €146,99 | €327,53 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.653,74 | €1.132,92 | €3.398,77 | €193,08 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.647,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.557,95 | €1.491,54 | €2.983,09 | €93,59 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 7 | €9.552,88 | €1.251,09 | €2.502,18 | €99,78 | €413,30 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.552,51 | €1.053,15 | €3.159,44 | €191,07 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €9.539,07 | €294,25 | €882,74 | €49,48 | €30,35 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €9.514,97 | €271,48 | €814,44 | €48,63 | €29,68 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.498,89 | €989,44 | €1.978,87 | €139,00 | €317,85 |
| TEST | FAST NoHigh <7,5 · SHORT only | 4 | €9.476,95 | €979,65 | €2.938,95 | €141,95 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.463,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 7 | €9.451,40 | €1.490,82 | €2.981,65 | €189,10 | €13,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 9 | €9.382,00 | €1.147,04 | €2.294,09 | €153,41 | €329,49 |
| TEST | Bilanciata 1H V2 | 7 | €9.376,04 | €974,39 | €2.923,18 | €141,82 | €8,87 |
| TEST | Combo Trend | 7 | €9.374,47 | €1.996,25 | €3.992,49 | €89,81 | €305,13 |
| TEST | Combo Adaptive — target pieno 3R | 7 | €9.374,18 | €1.227,70 | €2.455,40 | €97,92 | €405,56 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.369,88 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 7 | €9.367,56 | €989,24 | €1.978,48 | €187,35 | €-2,38 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.362,76 | €1.133,32 | €2.266,63 | €138,90 | €48,51 |
| TEST | Bilanciata V3 · LONG only | 7 | €9.326,37 | €2.199,86 | €6.599,57 | €178,87 | €349,84 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 5 | €9.177,18 | €1.730,31 | €3.460,61 | €138,34 | €51,27 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €9.117,85 | €1.000,45 | €2.000,90 | €134,93 | €50,88 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.009,68 | €634,74 | €1.269,48 | €134,42 | €4,80 |
| TEST | Rapida V3 — score <7,5 | 3 | €9.005,94 | €381,54 | €1.144,62 | €88,57 | €-27,56 |
| TEST | Forza relativa 1H V1 | 7 | €8.985,97 | €1.568,29 | €3.136,58 | €95,38 | €367,81 |
| TEST | Top 5 + BTC — BTC≤3 | 6 | €8.903,47 | €1.761,92 | €3.523,83 | €178,08 | €-2,87 |
| TEST | Combo Mean Reversion | 1 | €8.636,37 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €8.264,79 | €2.613,27 | €5.226,54 | €124,12 | €0,68 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,27 | €-181,91 | 59 | 59 | 42,37% | 0,88 | €-3,08 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.566,98 | €1.545,98 | 137 | 137 | 45,99% | 1,51 | €11,28 | 6,75% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €11.508,55 | €1.175,76 | 49 | 49 | 59,18% | 2,53 | €24,00 | 3,82% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.382,37 | €976,77 | 167 | 167 | 48,50% | 1,32 | €5,85 | 8,85% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.294,64 | €1.274,14 | 105 | 105 | 44,76% | 1,60 | €12,13 | 6,75% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.161,57 | €790,53 | 148 | 148 | 50,68% | 1,27 | €5,34 | 10,10% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.069,93 | €1.071,35 | 191 | 191 | 50,26% | 1,27 | €5,61 | 7,95% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.962,78 | €570,20 | 152 | 152 | 48,68% | 1,20 | €3,75 | 7,78% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.852,42 | €474,77 | 185 | 185 | 48,65% | 1,16 | €2,57 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.852,42 | €474,77 | 185 | 185 | 48,65% | 1,16 | €2,57 | 10,31% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.753,00 | €373,88 | 196 | 196 | 45,92% | 1,11 | €1,91 | 8,17% |
| TEST | Combo Scanner | Combo Scanner | €10.678,82 | €303,24 | 178 | 178 | 44,38% | 1,09 | €1,70 | 11,38% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.662,49 | €282,62 | 150 | 150 | 46,00% | 1,10 | €1,88 | 11,27% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.647,52 | €649,42 | 113 | 113 | 50,44% | 1,28 | €5,75 | 4,50% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.598,31 | €217,73 | 164 | 164 | 48,17% | 1,08 | €1,33 | 10,31% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.578,23 | €580,48 | 266 | 266 | 44,36% | 1,13 | €2,18 | 9,28% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.578,15 | €579,29 | 122 | 122 | 50,82% | 1,28 | €4,75 | 5,24% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.524,39 | €533,23 | 70 | 62 | 50,00% | 1,32 | €7,62 | 3,89% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.397,05 | €399,98 | 213 | 213 | 49,30% | 1,11 | €1,88 | 9,50% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.396,84 | €390,22 | 146 | 146 | 43,84% | 1,13 | €2,67 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.390,76 | €384,14 | 150 | 150 | 44,00% | 1,13 | €2,56 | 12,06% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.330,25 | €333,16 | 257 | 257 | 44,36% | 1,07 | €1,30 | 9,48% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.320,77 | €324,23 | 221 | 221 | 43,89% | 1,07 | €1,47 | 10,60% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.293,59 | €299,93 | 18 | 18 | 61,11% | 1,99 | €16,66 | 2,77% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.293,18 | €308,00 | 74 | 74 | 45,95% | 1,18 | €4,16 | 6,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.258,26 | €-89,93 | 149 | 149 | 44,30% | 0,97 | €-0,60 | 11,68% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.236,06 | €258,82 | 17 | 17 | 41,18% | 1,58 | €15,22 | 3,39% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Ampia 4H | Confluenza trend | €10.206,43 | €167,06 | 54 | 54 | 33,33% | 1,13 | €3,09 | 4,45% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.161,66 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.130,56 | €132,30 | 51 | 51 | 43,14% | 1,10 | €2,59 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.090,56 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | Sol Ema 1H | Trend following EMA | €10.070,61 | €73,41 | 23 | 23 | 43,48% | 1,11 | €3,19 | 3,33% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.066,52 | €66,52 | 17 | 17 | 58,82% | 1,16 | €3,91 | 3,08% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €10.064,80 | €-294,31 | 139 | 139 | 39,57% | 0,91 | €-2,12 | 7,34% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €10.060,17 | €-270,31 | 101 | 101 | 32,67% | 0,90 | €-2,68 | 8,39% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.054,78 | €57,13 | 175 | 175 | 44,57% | 1,02 | €0,33 | 8,69% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.053,19 | €54,27 | 263 | 263 | 39,92% | 1,01 | €0,21 | 6,56% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €10.049,48 | €-280,65 | 96 | 96 | 35,42% | 0,89 | €-2,92 | 7,98% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.039,42 | €39,42 | 29 | 29 | 44,83% | 1,33 | €1,36 | 0,33% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Ema 1H | Trend following EMA | €10.023,43 | €42,34 | 25 | 25 | 60,00% | 1,07 | €1,69 | 2,77% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,96 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €10.010,60 | €-318,25 | 98 | 98 | 34,69% | 0,88 | €-3,25 | 7,80% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.007,88 | €7,88 | 29 | 29 | 44,83% | 1,33 | €0,27 | 0,07% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.006,51 | €9,29 | 24 | 24 | 45,83% | 1,01 | €0,39 | 4,59% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,59 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.996,50 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.995,56 | €-360,55 | 142 | 142 | 45,07% | 0,87 | €-2,54 | 12,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,36 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.983,46 | €-12,56 | 221 | 221 | 43,44% | 1,00 | €-0,06 | 12,52% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.979,42 | €-20,58 | 15 | 15 | 60,00% | 0,94 | €-1,37 | 1,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.951,01 | €-38,22 | 124 | 124 | 41,94% | 0,99 | €-0,31 | 7,99% |
| TEST | Btc Ema 4H | Trend following EMA | €9.943,99 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.927,41 | €-72,59 | 29 | 29 | 44,83% | 0,56 | €-2,50 | 0,84% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.906,26 | €-163,52 | 53 | 53 | 47,17% | 0,88 | €-3,09 | 4,27% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.906,22 | €-435,35 | 81 | 81 | 32,10% | 0,82 | €-5,37 | 8,44% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.893,29 | €-102,20 | 145 | 145 | 47,59% | 0,97 | €-0,70 | 8,44% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.890,79 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.889,03 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.886,07 | €-111,88 | 166 | 166 | 45,18% | 0,96 | €-0,67 | 7,10% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.878,50 | €-446,01 | 132 | 132 | 44,70% | 0,85 | €-3,38 | 9,02% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.860,65 | €-505,26 | 192 | 192 | 40,10% | 0,87 | €-2,63 | 12,68% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.839,23 | €-159,49 | 137 | 130 | 40,88% | 0,95 | €-1,16 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.830,73 | €-520,02 | 156 | 156 | 40,38% | 0,85 | €-3,33 | 8,78% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.823,03 | €-176,07 | 143 | 143 | 44,76% | 0,95 | €-1,23 | 6,64% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.819,89 | €-180,01 | 16 | 16 | 43,75% | 0,68 | €-11,25 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.781,66 | €-287,24 | 53 | 53 | 43,40% | 0,79 | €-5,42 | 5,41% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.762,70 | €-249,98 | 18 | 18 | 38,89% | 0,59 | €-13,89 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Ema 1H | Trend following EMA | €9.726,53 | €-294,97 | 26 | 26 | 38,46% | 0,65 | €-11,35 | 4,80% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.719,02 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,60% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.717,32 | €-306,84 | 17 | 17 | 29,41% | 0,54 | €-18,05 | 3,74% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.711,84 | €-283,82 | 9 | 9 | 33,33% | 0,35 | €-31,54 | 4,16% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.700,72 | €-624,68 | 161 | 161 | 39,13% | 0,80 | €-3,88 | 15,68% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.653,74 | €-344,15 | 120 | 120 | 44,17% | 0,85 | €-2,87 | 9,26% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.647,46 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.557,95 | €-440,16 | 83 | 83 | 45,78% | 0,78 | €-5,30 | 6,28% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.552,88 | €-858,91 | 131 | 131 | 36,64% | 0,68 | €-6,56 | 14,10% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.552,51 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.539,07 | €-490,75 | 177 | 177 | 41,81% | 0,90 | €-2,77 | 15,64% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.514,97 | €-514,23 | 135 | 135 | 43,70% | 0,87 | €-3,81 | 15,94% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.498,89 | €-817,80 | 153 | 153 | 38,56% | 0,71 | €-5,35 | 12,31% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.476,95 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,60% |
| TEST | Btc Ema 1H | Trend following EMA | €9.463,59 | €-536,41 | 20 | 20 | 20,00% | 0,33 | €-26,82 | 5,46% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.451,40 | €-561,26 | 86 | 86 | 26,74% | 0,77 | €-6,53 | 11,41% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.382,00 | €-946,13 | 210 | 210 | 41,43% | 0,76 | €-4,51 | 15,45% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.376,04 | €-630,25 | 151 | 138 | 41,72% | 0,81 | €-4,17 | 11,82% |
| TEST | Combo Trend | Combo Trend | €9.374,47 | €-928,01 | 189 | 189 | 39,15% | 0,78 | €-4,91 | 14,08% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.374,18 | €-1.029,91 | 111 | 111 | 36,04% | 0,57 | €-9,28 | 14,10% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,88 | €-629,45 | 85 | 85 | 34,12% | 0,73 | €-7,41 | 7,96% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.367,56 | €-629,35 | 99 | 99 | 38,38% | 0,77 | €-6,36 | 11,79% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.362,76 | €-684,27 | 96 | 96 | 34,38% | 0,77 | €-7,13 | 10,13% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.326,37 | €-1.019,71 | 146 | 146 | 39,73% | 0,66 | €-6,98 | 12,43% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.177,18 | €-871,94 | 49 | 49 | 26,53% | 0,44 | €-17,79 | 12,23% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.117,85 | €-932,24 | 124 | 124 | 37,90% | 0,72 | €-7,52 | 13,91% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.009,68 | €-994,35 | 78 | 78 | 29,49% | 0,67 | €-12,75 | 13,60% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.005,94 | €-965,81 | 184 | 184 | 39,13% | 0,79 | €-5,25 | 17,41% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.985,97 | €-1.379,65 | 139 | 139 | 32,37% | 0,59 | €-9,93 | 19,11% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.903,47 | €-1.091,54 | 98 | 98 | 35,71% | 0,59 | €-11,14 | 16,19% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.636,37 | €-1.362,34 | 60 | 60 | 33,33% | 0,44 | €-22,71 | 16,00% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.264,79 | €-1.732,98 | 107 | 107 | 38,32% | 0,51 | €-16,20 | 19,25% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,42064 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-0,70 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,19323 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €349,39 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €-0,00 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,20444 | 2,20444 | 2,11218 | 1,48065 | 2,38896 | €350,15 | €1.050,46 | €43,96 | €0,00 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,41290 | 1,42064 | 1,39256 | 0,94900 | 1,45359 | €9,02 | €27,05 | €0,39 | €0,15 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2479,17574 | 2504,32000 | 2486,97083 | 1665,17970 | 2550,57600 | €16,68 | €50,03 | €0,00 | €0,51 |
| Bilanciata 1H V1 | DOGE | LONG | Confluenza trend | 60m | 3,0x | 0,09066 | 0,09051 | 0,08827 | 0,06089 | 0,09543 | €9,89 | €29,68 | €0,78 | €-0,05 |
| Bilanciata 1H V1 | DASH | LONG | Confluenza trend | 60m | 3,0x | 68,77375 | 74,22000 | 71,09852 | 46,19304 | 77,16470 | €9,27 | €27,80 | €0,00 | €2,20 |
| Bilanciata 1H V1 | USELESS | LONG | Confluenza trend | 60m | 3,0x | 0,26226 | 0,24740 | 0,23079 | 0,17615 | 0,32521 | €134,97 | €404,91 | €48,59 | €-22,95 |
| Bilanciata 1H V1 | UNI | LONG | Confluenza trend | 60m | 3,0x | 7,19844 | 7,09400 | 6,89640 | 4,83495 | 7,80251 | €39,62 | €118,87 | €4,99 | €-1,72 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,20444 | 2,20444 | 2,11218 | 1,48065 | 2,38896 | €24,38 | €73,14 | €3,06 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,19323 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €25,53 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01887 | 0,01799 | 0,01660 | 0,01267 | 0,02339 | €120,86 | €362,58 | €43,51 | €-16,87 |
| Bilanciata 1H V2 | ETH | LONG | Confluenza trend V2 | 60m | 3,0x | 2493,48860 | 2504,32000 | 2457,58236 | 1674,79317 | 2565,30107 | €29,33 | €88,00 | €1,27 | €0,38 |
| Bilanciata 1H V2 | DASH | LONG | Confluenza trend V2 | 60m | 3,0x | 74,23484 | 74,22000 | 69,35168 | 49,86107 | 84,00116 | €237,58 | €712,73 | €46,88 | €-0,14 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 86,70099 | 86,64900 | 85,45250 | 58,23416 | 89,19798 | €17,58 | €52,75 | €0,76 | €-0,03 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,19323 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €358,26 |
| Bilanciata 1H V3 Filtered | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,19544 | 2,19544 | 2,10498 | 1,47460 | 2,37635 | €8,90 | €26,71 | €1,10 | €0,00 |
| Bilanciata 1H V3 Filtered | DASH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 68,77375 | 74,22000 | 71,09852 | 46,19304 | 77,16470 | €37,94 | €113,83 | €0,00 | €9,01 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,81046 | 2504,32000 | 2466,76999 | 1681,05436 | 2574,89140 | €965,17 | €2.895,52 | €41,70 | €1,75 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 85,86049 | 86,64900 | 84,62409 | 57,66963 | 88,33327 | €30,96 | €92,87 | €1,34 | €0,85 |
| Rapida V1 — score 6–7,5 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| Rapida V1 — score 6–7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,19323 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €30,49 |
| Rapida V1 — score 6–7,5 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 80028,10242 | 79820,80000 | 79131,78767 | 53752,20879 | 81372,57454 | €18,39 | €55,17 | €0,62 | €-0,14 |
| Rapida V1 — score 6–7,5 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €127,25 | €381,75 | €45,81 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,19323 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €29,68 |
| Rapida score 6–7,5 — senza Trend Up | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €126,82 | €380,47 | €45,66 | €0,00 |
| Rapida score 6–7,5 — Range Only | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| Rapida score 6–7,5 — Range Only | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| Rapida score 6–7,5 — Range Only | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,25201 | 0,25201 | 0,22400 | 0,16927 | 0,29402 | €141,43 | €424,29 | €47,15 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €-0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €138,86 | €416,57 | €49,99 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09064 | 0,09051 | 0,08874 | 0,06088 | 0,09348 | €763,02 | €2.289,07 | €47,86 | €-3,24 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,26226 | 0,24740 | 0,23610 | 0,17615 | 0,30151 | €11,39 | €34,18 | €3,41 | €-1,94 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 105,84416 | 105,82300 | 104,65871 | 71,09200 | 107,62235 | €1.471,82 | €4.415,46 | €49,45 | €-0,88 |
| Rapida V1 — senza PEPE | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| Rapida V1 — senza PEPE | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| Rapida V1 — senza PEPE | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| Rapida V1 — senza PEPE | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| Rapida V1 — senza PEPE | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,22344 | 2,22344 | 2,15077 | 1,49341 | 2,33246 | €23,87 | €71,62 | €2,34 | €0,00 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| Rapida V1 — target pieno 2R | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| Rapida V1 — target pieno 2R | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| Rapida V1 — target pieno 2R | DASH | LONG | Momentum / breakout | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 81,83087 | €15,93 | €47,79 | €2,45 | €-0,01 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V2 | NEAR | LONG | Momentum / breakout V2 | 60m | 3,0x | 2,22144 | 2,22144 | 2,14439 | 1,49207 | 2,33703 | €507,73 | €1.523,18 | €52,84 | €0,00 |
| Rapida 1H V2 | DASH | LONG | Momentum / breakout V2 | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 79,93186 | €343,06 | €1.029,17 | €52,65 | €-0,21 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 86,70099 | 86,64900 | 85,72994 | 58,23416 | 88,15757 | €1.566,97 | €4.700,91 | €52,65 | €-2,82 |
| Rapida 1H V3 Filtered — madre | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered — madre | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered — madre | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €-0,00 |
| Rapida V3 — score <7,5 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| Rapida V3 — score <7,5 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €125,88 | €377,63 | €45,32 | €0,00 |
| Rapida V3 — score <7,5 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,26573 | 0,24740 | 0,23696 | 0,17848 | 0,30889 | €133,17 | €399,50 | €43,26 | €-27,56 |
| Rapida V3 — no volatilità HIGH | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| Rapida V3 — no volatilità HIGH | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| Rapida V3 — no volatilità HIGH | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22344 | 2,22344 | 2,15077 | 1,49341 | 2,33246 | €25,86 | €77,58 | €2,54 | €0,00 |
| Rapida V3 — no volatilità HIGH | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,14073 | 2504,32000 | 2476,09435 | 1681,94786 | 2546,21029 | €91,13 | €273,39 | €3,06 | €0,02 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| Rapida V3 — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| Rapida V3 — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| Rapida V3 — Long Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22144 | 2,22144 | 2,14439 | 1,49207 | 2,33703 | €9,64 | €28,92 | €1,00 | €0,00 |
| Rapida V3 — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,14073 | 2504,32000 | 2476,09435 | 1681,94786 | 2546,21029 | €1.485,82 | €4.457,47 | €49,92 | €0,32 |
| Rapida V3 — Long Only | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 79,93186 | €22,01 | €66,04 | €3,38 | €-0,01 |
| Rapida V3 — Long + no HIGH + score <7,5 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €134,15 | €402,44 | €48,29 | €0,00 |
| Rapida V3 — senza ESPORTS | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| Rapida V3 — senza ESPORTS | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €-0,00 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22144 | 2,22144 | 2,14439 | 1,49207 | 2,33703 | €9,92 | €29,77 | €1,03 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,14073 | 2504,32000 | 2476,09435 | 1681,94786 | 2546,21029 | €1.535,98 | €4.607,93 | €51,61 | €0,33 |
| Rapida V3 senza ESPORTS — Long Only | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 79,93186 | €28,86 | €86,57 | €4,43 | €-0,02 |
| Rapida V3 senza ESPORTS — MFE Lock | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €-0,00 |
| Rapida V3 senza ESPORTS — Stress Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79820,80000 | 79131,78767 | 53752,20879 | 81372,57454 | €77,79 | €233,37 | €2,61 | €-0,60 |
| Rapida V3 — qualità completa + profit lock | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| Rapida V3 — qualità completa + profit lock | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| Rapida V3 — qualità completa + profit lock | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,20944 | 2,20944 | 2,14340 | 1,48401 | 2,30850 | €42,71 | €128,14 | €3,83 | €0,00 |
| Rapida V3 — qualità completa + profit lock | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,19389 | 0,19323 | 0,18384 | 0,13023 | 0,20896 | €315,97 | €947,90 | €49,13 | €-3,22 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2504,32000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,15 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 86,64900 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €2,56 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 105,82300 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €0,54 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 1072,22440 | 1142,46000 | 981,26963 | 541,47332 | 1326,89776 | €277,64 | €555,28 | €47,10 | €36,37 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €320,80 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €-0,00 |
| Forza relativa 1H V1 | DASH | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 68,42368 | 74,22000 | 70,21891 | 34,55396 | 79,12329 | €298,34 | €596,68 | €0,00 | €50,55 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,01854 | 0,01799 | 0,01632 | 0,00936 | 0,02344 | €25,32 | €50,64 | €6,08 | €-1,51 |
| Forza relativa 1H V1 | USELESS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,33150 | €17,47 | €34,93 | €4,19 | €-1,98 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 86,70099 | 86,64900 | 85,45250 | 43,78400 | 89,44768 | €38,20 | €76,41 | €1,10 | €-0,05 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Scalp RSI Short 85 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 105,88382 | 105,82300 | 107,02557 | 112,41332 | 104,17119 | €10,00 | €150,00 | €1,62 | €0,09 |
| Scalp RSI Short 85 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 105,88382 | 105,82300 | 107,02557 | 112,41332 | 104,17119 | €50,00 | €750,00 | €8,09 | €0,43 |
| Scalp RSI Short 85 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 105,88382 | 105,82300 | 107,02557 | 126,53116 | 103,60031 | €185,32 | €926,58 | €9,99 | €0,53 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2486,95729 | 2504,32000 | 2447,16598 | 1255,91343 | 2586,43558 | €1.753,97 | €3.507,94 | €56,13 | €24,49 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 105,92618 | 105,82300 | 104,23136 | 53,49272 | 110,16323 | €20,43 | €40,86 | €0,65 | €-0,04 |
| Benchmark Donchian breakout 1H | DASH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 74,23484 | 74,22000 | 68,80911 | 37,48860 | 87,79918 | €30,65 | €61,30 | €4,48 | €-0,01 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2486,95729 | 2504,32000 | 2447,16598 | 1255,91343 | 2586,43558 | €1.712,67 | €3.425,35 | €54,81 | €23,91 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 105,92618 | 105,82300 | 104,23136 | 53,49272 | 110,16323 | €19,95 | €39,90 | €0,64 | €-0,04 |
| Donchian 1H Gb20 120R V1 | DASH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 74,23484 | 74,22000 | 68,80911 | 37,48860 | 87,79918 | €29,93 | €59,86 | €4,37 | €-0,01 |
| Benchmark Bollinger mean reversion 1H | NEAR | SHORT | Bollinger mean reversion | 60m | 2,0x | 2,22056 | 2,22056 | 2,30308 | 3,31973 | 2,09677 | €570,99 | €1.141,97 | €42,44 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 2503,13927 | 2504,32000 | 2533,17694 | 3742,19321 | 2458,08277 | €1.667,15 | €3.334,30 | €40,01 | €-1,57 |
| Benchmark Bollinger mean reversion 1H | ARB | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,19381 | 0,19323 | 0,20457 | 0,28975 | 0,17767 | €375,13 | €750,26 | €41,67 | €2,25 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,19323 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €310,66 |
| Benchmark trend following EMA 1H | DASH | LONG | Trend following EMA | 60m | 2,0x | 68,77375 | 74,22000 | 70,84555 | 34,73074 | 79,02935 | €46,57 | €93,14 | €0,00 | €7,38 |
| Benchmark trend following EMA 1H | DOGE | LONG | Trend following EMA | 60m | 2,0x | 0,09110 | 0,09051 | 0,08881 | 0,04600 | 0,09614 | €12,72 | €25,43 | €0,64 | €-0,16 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 86,70099 | 86,64900 | 85,31377 | 43,78400 | 89,75286 | €19,85 | €39,71 | €0,64 | €-0,02 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €412,60 |
| Scanner Top 5 Long 1H | USELESS | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €34,92 | €69,83 | €8,38 | €-5,51 |
| Scanner Top 5 Long 1H | UNI | LONG | Scanner Top 5 Long | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,71810 | €13,87 | €27,74 | €1,22 | €-0,01 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €383,90 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,41742 | €32,93 | €65,86 | €2,91 | €0,00 |
| Scanner Top10 Long | DASH | LONG | Scanner Top10 Long | 60m | 2,0x | 68,77375 | 74,22000 | 71,09852 | 34,73074 | 77,16470 | €15,19 | €30,39 | €0,00 | €2,41 |
| Scanner Top10 Long | USELESS | LONG | Scanner Top10 Long | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €25,54 | €51,08 | €6,13 | €-2,89 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €387,47 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €32,67 | €65,33 | €7,84 | €-5,15 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 7,80251 | €12,82 | €25,64 | €1,08 | €-0,37 |
| Scanner Top15 Long | DOGE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,09053 | 0,09051 | 0,08848 | 0,04572 | 0,09463 | €1.198,57 | €2.397,13 | €54,27 | €-0,48 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 86,70099 | 86,64900 | 85,45250 | 43,78400 | 89,19798 | €187,72 | €375,44 | €5,41 | €-0,23 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €387,47 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €32,67 | €65,33 | €7,84 | €-5,15 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 7,80251 | €12,82 | €25,64 | €1,08 | €-0,37 |
| Scanner Top20 Long | DOGE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,09053 | 0,09051 | 0,08848 | 0,04572 | 0,09463 | €1.198,57 | €2.397,13 | €54,27 | €-0,48 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 86,70099 | 86,64900 | 85,45250 | 43,78400 | 89,19798 | €187,72 | €375,44 | €5,41 | €-0,23 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €386,44 |
| Scanner Top 5 + forza BTC 1H | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €32,73 | €65,46 | €7,86 | €-5,16 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €-0,01 |
| Top 5 + BTC — solo MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Top 5 + BTC — solo MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Top 5 + BTC — solo MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Top 5 + BTC — solo MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €362,26 |
| Top 5 + BTC — solo MFE | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €30,68 | €61,37 | €7,36 | €-4,84 |
| Top 5 + BTC — solo MFE | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €-0,01 |
| Top 5 + BTC — Guard | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Top 5 + BTC — Guard | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Top 5 + BTC — Guard | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Top 5 + BTC — Guard | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Top 5 + BTC — Guard | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €364,76 |
| Top 5 + BTC — Guard | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €30,96 | €61,93 | €7,43 | €-4,88 |
| Top 5 + BTC — Guard | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €18,63 | €37,25 | €2,45 | €-0,01 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Top 5 + BTC — BTC≤3 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Top 5 + BTC — BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,22144 | 2,22144 | 2,12237 | 1,12183 | 2,43940 | €12,72 | €25,44 | €1,13 | €0,00 |
| Top 5 + BTC — BTC≤3 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19389 | 0,19323 | 0,18097 | 0,09791 | 0,22231 | €331,93 | €663,86 | €44,24 | €-2,26 |
| Top 5 + BTC — BTC≤3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 7,86292 | €16,52 | €33,03 | €1,39 | €-0,48 |
| Top 5 + BTC — BTC≤3 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €337,21 | €674,41 | €44,36 | €-0,13 |
| Top 5 + BTC — BTC 2–3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Top 5 + BTC — BTC 2–3 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,93378 | 74,22000 | 70,72471 | 34,81156 | 79,16182 | €335,09 | €670,19 | €0,00 | €51,39 |
| Top 5 + BTC — BTC 2–3 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €188,32 | €376,64 | €45,20 | €0,00 |
| Top 5 + BTC — BTC 2–3 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19327 | 0,19323 | 0,17837 | 0,09760 | 0,22605 | €297,63 | €595,27 | €45,89 | €-0,12 |
| Top 5 + BTC — BTC 2–3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €-0,01 |
| Top 5 + BTC — Guard + MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Top 5 + BTC — Guard + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Top 5 + BTC — Guard + MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Top 5 + BTC — Guard + MFE | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Top 5 + BTC — Guard + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €356,28 |
| Top 5 + BTC — Guard + MFE | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €30,24 | €60,49 | €7,26 | €-4,77 |
| Top 5 + BTC — Guard + MFE | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €18,19 | €36,39 | €2,39 | €-0,01 |
| Top 5 + BTC — Guard + BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,42902 | €14,83 | €29,66 | €1,25 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19389 | 0,19323 | 0,18097 | 0,09791 | 0,22231 | €349,38 | €698,77 | €46,57 | €-2,37 |
| Top 5 + BTC — Guard + BTC≤3 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €18,90 | €37,80 | €2,49 | €-0,01 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,93378 | 74,22000 | 70,72471 | 34,81156 | 79,16182 | €332,51 | €665,01 | €0,00 | €51,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €186,87 | €373,73 | €44,85 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19327 | 0,19323 | 0,17837 | 0,09760 | 0,22605 | €295,71 | €591,42 | €45,59 | €-0,12 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €24,76 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,76375 | 74,22000 | 70,64887 | 34,72569 | 82,94613 | €17,67 | €35,33 | €0,00 | €2,80 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,20944 | 2,20944 | 2,12454 | 1,11577 | 2,46416 | €13,56 | €27,12 | €1,04 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01887 | 0,01799 | 0,01660 | 0,00953 | 0,02566 | €203,31 | €406,63 | €48,80 | €-18,92 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €-0,01 |
| Top 5 + BTC — target pieno 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Top 5 + BTC — target pieno 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €24,78 |
| Top 5 + BTC — target pieno 3R | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,76375 | 74,22000 | 70,64887 | 34,72569 | 82,94613 | €17,68 | €35,35 | €0,00 | €2,81 |
| Top 5 + BTC — target pieno 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,20944 | 2,20944 | 2,12454 | 1,11577 | 2,46416 | €13,57 | €27,13 | €1,04 | €0,00 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01887 | 0,01799 | 0,01660 | 0,00953 | 0,02566 | €203,43 | €406,87 | €48,82 | €-18,93 |
| Top 5 + BTC — target pieno 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €-0,01 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,19323 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €298,11 |
| Combo Trend | DASH | LONG | Combo Trend | 60m | 2,0x | 68,77375 | 74,22000 | 70,84555 | 34,73074 | 79,02935 | €44,73 | €89,45 | €0,00 | €7,08 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 105,92618 | 105,82300 | 104,23136 | 53,49272 | 109,65478 | €19,15 | €38,30 | €0,61 | €-0,04 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 86,70099 | 86,64900 | 85,31377 | 43,78400 | 89,75286 | €17,04 | €34,07 | €0,55 | €-0,02 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €381,15 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,43702 | €40,95 | €81,89 | €3,61 | €0,00 |
| Combo Scanner | USELESS | LONG | Combo Scanner | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €37,75 | €75,50 | €9,06 | €-5,95 |
| Combo Scanner | DASH | LONG | Combo Scanner | 60m | 2,0x | 67,61352 | 74,22000 | 71,09257 | 34,14483 | 76,70308 | €12,75 | €25,51 | €0,00 | €2,49 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €-0,23 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive — madre | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive — madre | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive — madre | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive — madre | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €382,54 |
| Combo Adaptive — madre | DASH | LONG | Combo Adaptive | 60m | 2,0x | 68,77375 | 74,22000 | 71,35148 | 34,73074 | 77,16470 | €15,14 | €30,28 | €0,00 | €2,40 |
| Combo Adaptive — madre | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €33,75 | €67,50 | €8,10 | €-3,83 |
| Combo Adaptive — madre | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09110 | 0,09051 | 0,08904 | 0,04600 | 0,09522 | €15,70 | €31,39 | €0,71 | €-0,20 |
| Combo Adaptive — MFE Trail esistente | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive — MFE Trail esistente | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €334,13 |
| Combo Adaptive — MFE Trail esistente | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €28,33 | €56,67 | €6,80 | €-4,47 |
| Combo Adaptive — MFE Trail esistente | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09110 | 0,09051 | 0,08904 | 0,04600 | 0,09522 | €12,72 | €25,45 | €0,58 | €-0,16 |
| Combo Adaptive — MFE Trail esistente | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,71810 | €14,17 | €28,34 | €1,24 | €-0,01 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive — Quality7 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive — Quality7 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive — Trend/Transition | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive — Trend/Transition | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,41742 | €504,48 | €1.008,96 | €44,51 | €0,00 |
| Combo Adaptive — Quality7 + Regime | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,23245 | 2,23245 | 2,13521 | 1,12739 | 2,42693 | €554,11 | €1.108,22 | €48,27 | €0,00 |
| Combo Adaptive — Quality7 + Regime | DASH | LONG | Combo Adaptive | 60m | 2,0x | 66,61332 | 74,22000 | 70,42020 | 33,63973 | 77,04227 | €307,73 | €615,47 | €0,00 | €70,28 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive — Long Only | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive — Long Only | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €397,14 |
| Combo Adaptive — Long Only | DASH | LONG | Combo Adaptive | 60m | 2,0x | 68,24365 | 74,22000 | 70,56985 | 34,46304 | 78,54894 | €14,55 | €29,11 | €0,00 | €2,55 |
| Combo Adaptive — Long Only | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €24,77 | €49,53 | €5,94 | €-3,91 |
| Combo Adaptive — Long Only | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2504,14073 | 2504,32000 | 2468,08110 | 1264,59107 | 2576,25998 | €61,52 | €123,03 | €1,77 | €0,01 |
| Combo Adaptive — Long Only | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09110 | 0,09051 | 0,08904 | 0,04600 | 0,09522 | €17,12 | €34,23 | €0,77 | €-0,22 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 86,70099 | 86,64900 | 85,45250 | 43,78400 | 89,19798 | €25,35 | €50,70 | €0,73 | €-0,03 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive — parziale 1R | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive — parziale 1R | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,41742 | €45,81 | €91,62 | €4,04 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,23245 | 2,23245 | 2,13521 | 1,12739 | 2,42693 | €561,17 | €1.122,34 | €48,89 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | DASH | LONG | Combo Adaptive | 60m | 2,0x | 66,61332 | 74,22000 | 70,42020 | 33,63973 | 77,04227 | €311,65 | €623,31 | €0,00 | €71,18 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €342,16 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,36527 | €26,79 | €53,59 | €6,43 | €-4,23 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DASH | LONG | Combo Adaptive | 60m | 2,0x | 67,61352 | 74,22000 | 71,34596 | 34,14483 | 80,00838 | €387,84 | €775,69 | €0,00 | €75,79 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 8,10454 | €14,09 | €28,18 | €1,18 | €-0,41 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09053 | 0,09051 | 0,08848 | 0,04572 | 0,09668 | €59,13 | €118,27 | €2,68 | €-0,02 |
| Combo Adaptive — target pieno 3R | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive — target pieno 3R | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive — target pieno 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €335,76 |
| Combo Adaptive — target pieno 3R | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,36527 | €26,29 | €52,58 | €6,31 | €-4,15 |
| Combo Adaptive — target pieno 3R | DASH | LONG | Combo Adaptive | 60m | 2,0x | 67,61352 | 74,22000 | 71,34596 | 34,14483 | 80,00838 | €380,59 | €761,18 | €0,00 | €74,37 |
| Combo Adaptive — target pieno 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 8,10454 | €13,85 | €27,69 | €1,16 | €-0,40 |
| Combo Adaptive — target pieno 3R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09053 | 0,09051 | 0,08848 | 0,04572 | 0,09668 | €58,03 | €116,06 | €2,63 | €-0,02 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80800,35684 | 79820,80000 | 78530,68128 | 40804,18020 | 86474,54655 | €887,05 | €1.774,10 | €49,83 | €-21,51 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80800,35684 | 79820,80000 | 78530,68128 | 40804,18020 | 87155,44873 | €882,31 | €1.764,61 | €49,57 | €-21,39 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80768,04316 | 79820,80000 | 82830,55933 | 120748,22452 | 77055,51340 | €985,68 | €1.971,36 | €50,34 | €23,12 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80800,35684 | 79820,80000 | 78324,34707 | 40804,18020 | 86990,38168 | €817,27 | €1.634,54 | €50,09 | €-19,82 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 105,84416 | 105,82300 | 104,32001 | 71,09200 | 108,89248 | €1.165,90 | €3.497,71 | €50,37 | €-0,70 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 105,92618 | 105,82300 | 104,57033 | 71,14708 | 108,63789 | €1.341,14 | €4.023,41 | €51,50 | €-3,92 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 105,82300 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €17,55 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 105,88382 | 105,82300 | 107,15442 | 140,64901 | 103,97791 | €1.363,89 | €4.091,66 | €49,10 | €2,35 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 105,84416 | 105,82300 | 104,32001 | 71,09200 | 108,89248 | €1.158,48 | €3.475,45 | €50,05 | €-0,69 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2486,95729 | 2504,32000 | 2488,66876 | 1670,40631 | 2558,58166 | €1.123,27 | €3.369,80 | €0,00 | €23,53 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2504,32000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €2,75 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2486,95729 | 2504,32000 | 2488,66876 | 1670,40631 | 2550,62340 | €1.262,13 | €3.786,39 | €0,00 | €26,43 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2503,13927 | 2504,32000 | 2533,17694 | 3325,00333 | 2458,08277 | €1.349,47 | €4.048,41 | €48,58 | €-1,91 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2493,48860 | 2504,32000 | 2457,58236 | 1674,79317 | 2565,30107 | €1.128,47 | €3.385,42 | €48,75 | €14,71 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09136 | 0,09051 | 0,08896 | 0,06136 | 0,09616 | €636,41 | €1.909,22 | €50,21 | €-17,73 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €352,50 |
| Master Adaptive V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,41033 | €25,40 | €50,81 | €2,14 | €0,00 |
| Master Adaptive V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,47 | €44,95 | €5,39 | €0,00 |
| Master Adaptive V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €207,43 | €414,85 | €49,78 | €-23,51 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,12142 | 2,12142 | 2,02723 | 1,07132 | 2,30981 | €24,83 | €49,65 | €2,20 | €0,00 |
| Master Adaptive No Alt V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 74,22000 | 64,01551 | 34,80651 | 78,74032 | €315,67 | €631,34 | €44,96 | €48,51 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 74,22000 | 64,01551 | 34,80651 | 78,74032 | €31,26 | €62,52 | €4,45 | €4,80 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €347,85 |
| Master Adaptive Gb20 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,41033 | €24,97 | €49,93 | €2,10 | €0,00 |
| Master Adaptive Gb20 V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,18 | €44,35 | €5,32 | €0,00 |
| Master Adaptive Gb20 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €204,69 | €409,38 | €49,13 | €-23,20 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,75415 | 0,75415 | 0,73459 | 0,38085 | 0,81282 | €26,15 | €52,29 | €1,36 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €343,56 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,51541 | €477,69 | €955,38 | €42,14 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01854 | 0,01799 | 0,01632 | 0,00936 | 0,02522 | €22,54 | €45,08 | €5,41 | €-1,34 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1142,68849 | 1142,46000 | 1099,52971 | 577,05769 | 1272,16483 | €18,41 | €36,81 | €1,39 | €-0,01 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive — Side × Regime Guard | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €350,32 |
| Combo Adaptive — Side × Regime Guard | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09066 | 0,09051 | 0,08827 | 0,04578 | 0,09543 | €13,22 | €26,44 | €0,70 | €-0,04 |
| Combo Adaptive — Side × Regime Guard | DASH | LONG | Combo Adaptive | 60m | 2,0x | 68,77375 | 74,22000 | 71,35148 | 34,73074 | 77,16470 | €13,88 | €27,76 | €0,00 | €2,20 |
| Combo Adaptive — Side × Regime Guard | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €23,30 | €46,60 | €5,59 | €-2,64 |
| Combo Adaptive — Side × Regime Guard | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,92618 | 105,82300 | 104,40084 | 53,49272 | 108,97686 | €23,43 | €46,87 | €0,67 | €-0,05 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €354,25 |
| Master Adaptive GB20 — Breakeven 0,5R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,41033 | €25,53 | €51,06 | €2,15 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,58 | €45,17 | €5,42 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €208,45 | €416,91 | €50,03 | €-23,63 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €353,87 |
| Master Adaptive GB20 — 50% a 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,41033 | €25,50 | €51,01 | €2,14 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,56 | €45,12 | €5,41 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €208,23 | €416,47 | €49,98 | €-23,60 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €16,60 |
| Master Adaptive GB20 — Loss Cap 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,22144 | 2,14795 | 1,12183 | 2,41742 | €689,28 | €1.378,56 | €45,61 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23703 | 0,13244 | 0,32954 | €31,77 | €63,55 | €6,11 | €-3,60 |
| Rapida V3 NoHigh — Range Only | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| Rapida V3 NoHigh — Range Only | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| Rapida V3 NoHigh — Range Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01854 | 0,01799 | 0,01639 | 0,01245 | 0,02176 | €147,26 | €441,78 | €51,15 | €-13,16 |
| Rapida V3 NoHigh — Regime Guard | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79820,80000 | 79131,78767 | 53752,20879 | 81372,57454 | €20,36 | €61,08 | €0,68 | €-0,16 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01799 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €333,44 |
| MAIN — Side × Regime Guard | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2504,32000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,81 |
| MAIN — Side × Regime Guard | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| MAIN — Side × Regime Guard | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| MAIN — Side × Regime Guard | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,28046 | 2,28046 | 2,11906 | 1,53171 | 2,60325 | €9,22 | €27,66 | €1,96 | €0,00 |
| MAIN — Dynamic Asset Selector | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| MAIN — Dynamic Asset Selector | USELESS | LONG | Confluenza trend | 240m | 3,0x | 0,26076 | 0,24740 | 0,22947 | 0,17515 | 0,32335 | €142,48 | €427,43 | €51,29 | €-21,90 |
| Combo Trend — Side × Regime Guard | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend — Side × Regime Guard | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,19323 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €363,41 |
| Combo Trend — Side × Regime Guard | XRP | LONG | Combo Trend | 60m | 2,0x | 1,41420 | 1,42064 | 1,39158 | 0,71417 | 1,46398 | €20,70 | €41,41 | €0,66 | €0,19 |
| Combo Trend — Side × Regime Guard | DASH | LONG | Combo Trend | 60m | 2,0x | 68,77375 | 74,22000 | 70,84555 | 34,73074 | 79,02935 | €61,86 | €123,73 | €0,00 | €9,80 |
| Combo Trend — Side × Regime Guard | DOGE | LONG | Combo Trend | 60m | 2,0x | 0,09110 | 0,09051 | 0,08881 | 0,04600 | 0,09614 | €16,34 | €32,68 | €0,82 | €-0,21 |
| Combo Trend — Side × Regime Guard | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,09400 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €-0,21 |
| FAST NoHigh <7,5 · SHORT only | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €-0,00 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| Bilanciata V3 · LONG only | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,19323 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €338,85 |
| Bilanciata V3 · LONG only | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,19544 | 2,19544 | 2,10498 | 1,47460 | 2,37635 | €8,42 | €25,26 | €1,04 | €0,00 |
| Bilanciata V3 · LONG only | DASH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 68,77375 | 74,22000 | 71,09852 | 46,19304 | 77,16470 | €35,89 | €107,67 | €0,00 | €8,53 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,81046 | 2504,32000 | 2466,76999 | 1681,05436 | 2574,89140 | €912,88 | €2.738,63 | €39,44 | €1,65 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 85,86049 | 86,64900 | 84,62409 | 57,66963 | 88,33327 | €29,28 | €87,83 | €1,26 | €0,81 |
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
| Bilanciata V3 · LONG only | ZEC | LONG | 2026-09-06T04:45:00+00:00 | 1102,89952 | €3,44 | 1,97 | TARGET |
| Combo Trend — Side × Regime Guard | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1159,16754 | €109,04 | 2,18 | TARGET |
| MAIN — Side × Regime Guard | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1145,68961 | €12,12 | 1,98 | TARGET |
| Rapida V3 NoHigh — Regime Guard | ZEC | LONG | 2026-09-06T04:45:00+00:00 | 1102,59349 | €74,29 | 1,44 | TARGET |
| Rapida V3 NoHigh — Regime Guard | ARB | LONG | 2026-09-06T04:30:00+00:00 | 0,19056 | €-0,64 | -0,35 | STOP_GAP_STRESS |
| Rapida V3 NoHigh — Regime Guard | DASH | LONG | 2026-09-06T05:00:00+00:00 | 74,32565 | €2,92 | 1,47 | TARGET |
| Master Adaptive Runner25 V1 | UNI | LONG | 2026-09-06T04:30:00+00:00 | 7,07998 | €-1,53 | -1,03 | STOP |
| Combo Adaptive — target pieno 3R | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1174,74335 | €6,33 | 2,98 | TARGET |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1174,74335 | €6,45 | 2,98 | TARGET |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1137,33707 | €96,40 | 1,98 | TARGET |
| Combo Adaptive — Long Only | ZEC | LONG | 2026-09-06T04:45:00+00:00 | 1124,72555 | €3,07 | 1,98 | TARGET |
| Combo Adaptive — Quality7 + Regime | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1137,33707 | €95,19 | 1,98 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 691/30 | 33/30 | 0,91 | 2,04 | -0,05R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 645/30 | 20/30 | 0,88 | 1,90 | -0,06R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 313/30 | 22/30 | 1,00 | 1,74 | 0,00R | €12,35 | 1,72% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 318/30 | 22/30 | 0,97 | 1,57 | -0,02R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 602/30 | 31/30 | 1,02 | 0,62 | 0,01R | €-8,91 | 4,83% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 554/30 | 11/30 | 1,00 | 0,00 | -0,00R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 177/30 | 8/30 | 0,97 | 1,02 | -0,01R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 420/30 | 17/30 | 0,85 | 4,50 | -0,08R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 609/30 | 24/30 | 0,84 | 0,64 | -0,08R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 562/30 | 7/30 | 0,76 | 0,02 | -0,12R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 602/30 | 30/30 | 1,04 | 1,02 | 0,02R | €0,30 | 4,84% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 985/30 | 55/30 | 0,94 | 1,12 | -0,03R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 212/30 | 15/30 | 0,72 | 0,99 | -0,17R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 863/30 | 44/30 | 0,87 | 1,20 | -0,07R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 867/30 | 37/30 | 0,87 | 0,76 | -0,07R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 803/30 | 23/30 | 0,82 | 1,12 | -0,09R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 396/30 | 59/30 | 0,85 | 0,88 | -0,09R | €-3,08 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 17/30 | 0,00 | 1,58 | 0,00R | €15,22 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 49/30 | 0,00 | 2,53 | 0,00R | €24,00 | 3,82% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 32/30 | 18/30 | 0,45 | 0,63 | -0,28R | €-2,05 | 0,71% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 51/30 | 29/30 | 0,64 | 0,56 | -0,20R | €-2,50 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 1007/30 | 161/30 | 0,93 | 0,80 | -0,04R | €-3,88 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 120/30 | 0,00 | 0,85 | 0,00R | €-2,87 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 339/30 | 138/30 | 1,21 | 0,81 | 0,10R | €-4,17 | 11,82% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 645/30 | 192/30 | 1,00 | 0,87 | -0,00R | €-2,63 | 12,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 566/30 | 146/30 | 0,95 | 0,66 | -0,03R | €-6,98 | 12,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 314/30 | 124/30 | 0,98 | 0,99 | -0,01R | €-0,31 | 7,99% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 642/30 | 162/30 | 0,93 | 0,84 | -0,03R | €-3,22 | 10,60% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 709/30 | 199/30 | 0,95 | 0,93 | -0,03R | €-1,40 | 10,60% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1141/30 | 266/30 | 0,88 | 1,13 | -0,06R | €2,18 | 9,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 191/30 | 0,00 | 1,27 | 0,00R | €5,61 | 7,95% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 135/30 | 0,00 | 0,87 | 0,00R | €-3,81 | 15,94% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 51/30 | 0,00 | 1,10 | 0,00R | €2,59 | 6,49% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 652/30 | 177/30 | 0,94 | 0,90 | -0,03R | €-2,77 | 15,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1093/30 | 263/30 | 0,87 | 1,01 | -0,06R | €0,21 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 87/30 | 62/30 | 1,01 | 1,32 | 0,01R | €7,62 | 3,89% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 1055/30 | 257/30 | 0,90 | 1,07 | -0,05R | €1,30 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 793/30 | 184/30 | 0,93 | 0,79 | -0,03R | €-5,25 | 17,41% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 362/30 | 145/30 | 1,06 | 0,97 | 0,03R | €-0,70 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 366/30 | 143/30 | 1,03 | 0,95 | 0,01R | €-1,23 | 6,64% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 688/30 | 221/30 | 1,02 | 1,00 | 0,01R | €-0,06 | 12,52% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 74/30 | 0,00 | 1,18 | 0,00R | €4,16 | 6,05% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 122/30 | 0,00 | 1,28 | 0,00R | €4,75 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 733/30 | 166/30 | 0,88 | 0,96 | -0,06R | €-0,67 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 221/30 | 0,00 | 1,07 | 0,00R | €1,47 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 213/30 | 0,00 | 1,11 | 0,00R | €1,88 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 113/30 | 0,00 | 1,28 | 0,00R | €5,75 | 4,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 1008/30 | 225/30 | 0,88 | 0,91 | -0,06R | €-1,98 | 10,92% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 368/30 | 54/30 | 0,89 | 1,13 | -0,07R | €3,09 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 353/30 | 107/30 | 1,12 | 0,51 | 0,05R | €-16,20 | 19,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 15/30 | 9/30 | 0,64 | 0,86 | -0,19R | €-3,49 | 1,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 3/30 | 3/30 | 1,15 | 1,17 | 0,10R | €5,87 | 0,96% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 9/30 | 6/30 | 3,40 | 4,66 | 0,60R | €34,87 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 3/30 | 3/30 | 2,22 | 2,25 | 0,45R | €22,76 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 19/30 | 12/30 | 0,29 | 0,70 | -0,55R | €-8,55 | 1,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 7/30 | 5/30 | 0,42 | 0,61 | -0,53R | €-17,29 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 26/30 | 20/30 | 0,48 | 0,33 | -0,37R | €-26,82 | 5,46% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 5/30 | 4/30 | 0,56 | 0,78 | -0,37R | €-8,28 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 834/30 | 196/30 | 1,01 | 1,11 | 0,01R | €1,91 | 8,17% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 531/30 | 152/30 | 1,10 | 1,20 | 0,05R | €3,75 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 931/30 | 210/30 | 1,02 | 0,76 | 0,01R | €-4,51 | 15,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 775/30 | 175/30 | 0,98 | 1,02 | -0,01R | €0,33 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 97/30 | 53/30 | 1,31 | 0,88 | 0,13R | €-3,09 | 4,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 97/30 | 53/30 | 1,29 | 0,79 | 0,12R | €-5,42 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 285/30 | 98/30 | 1,00 | 0,80 | 0,00R | €-4,94 | 8,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 274/30 | 83/30 | 1,02 | 0,78 | 0,01R | €-5,30 | 6,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 131/30 | 0,74 | 0,68 | -0,20R | €-6,56 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 149/30 | 0,00 | 0,97 | 0,00R | €-0,60 | 11,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 111/30 | 0,74 | 0,57 | -0,20R | €-9,28 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 130/30 | 60/30 | 1,04 | 0,44 | 0,02R | €-22,71 | 16,00% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 537/30 | 178/30 | 1,12 | 1,09 | 0,06R | €1,70 | 11,38% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 700/30 | 189/30 | 1,00 | 0,78 | -0,00R | €-4,91 | 14,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 148/30 | 0,00 | 1,27 | 0,00R | €5,34 | 10,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 18/30 | 15/30 | 1,84 | 0,94 | 0,26R | €-1,37 | 1,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 22/30 | 17/30 | 0,66 | 1,16 | -0,22R | €3,91 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 37/30 | 25/30 | 0,52 | 1,07 | -0,31R | €1,69 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 370/30 | 137/30 | 0,91 | 1,51 | -0,05R | €11,28 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 300/30 | 105/30 | 0,92 | 1,60 | -0,04R | €12,13 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 713/30 | 153/30 | 0,96 | 0,71 | -0,02R | €-5,35 | 12,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 27/30 | 18/30 | 0,53 | 0,59 | -0,35R | €-13,89 | 3,14% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 18/30 | 9/30 | 1,96 | 0,35 | 0,36R | €-31,54 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 25/30 | 17/30 | 0,45 | 0,54 | -0,42R | €-18,05 | 3,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 40/30 | 26/30 | 0,48 | 0,65 | -0,36R | €-11,35 | 4,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 7/30 | 7/30 | 0,49 | 0,57 | -0,31R | €-16,10 | 1,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 18/30 | 21/30 | 0,85 | 0,46 | -0,09R | €-16,79 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 360/30 | 85/30 | 1,15 | 0,73 | 0,09R | €-7,41 | 7,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 101/30 | 0,00 | 0,90 | 0,00R | €-2,68 | 8,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 86/30 | 0,00 | 0,77 | 0,00R | €-6,53 | 11,41% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 96/30 | 0,00 | 0,89 | 0,00R | €-2,92 | 7,98% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 682/30 | 132/30 | 1,38 | 0,85 | 0,12R | €-3,38 | 9,02% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 300/30 | 96/30 | 1,15 | 0,77 | 0,09R | €-7,13 | 10,13% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 329/30 | 81/30 | 1,17 | 0,82 | 0,10R | €-5,37 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 214/30 | 78/30 | 1,03 | 0,67 | 0,02R | €-12,75 | 13,60% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 344/30 | 98/30 | 1,14 | 0,88 | 0,09R | €-3,25 | 7,80% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 840/30 | 139/30 | 0,94 | 0,59 | -0,03R | €-9,93 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 331/30 | 130/30 | 1,19 | 0,95 | 0,09R | €-1,16 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 272/30 | 70/30 | 0,51 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 272/30 | 70/30 | 0,51 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 272/30 | 70/30 | 0,51 | 0,65 | -0,28R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 301/30 | 89/30 | 0,64 | 0,64 | -0,20R | €-9,30 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 330/30 | 61/30 | 0,75 | 0,58 | -0,11R | €-12,17 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 299/30 | 62/30 | 0,67 | 0,56 | -0,15R | €-12,20 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 536/30 | 164/30 | 1,07 | 1,08 | 0,04R | €1,33 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 538/30 | 185/30 | 1,07 | 1,16 | 0,04R | €2,57 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 538/30 | 185/30 | 1,07 | 1,16 | 0,04R | €2,57 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 517/30 | 150/30 | 1,13 | 1,10 | 0,07R | €1,88 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 184/30 | 49/30 | 0,75 | 0,44 | -0,15R | €-17,79 | 12,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 375/30 | 98/30 | 0,92 | 0,59 | -0,04R | €-11,14 | 16,19% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 399/30 | 124/30 | 1,13 | 0,72 | 0,05R | €-7,52 | 13,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 333/30 | 99/30 | 0,98 | 0,77 | -0,01R | €-6,36 | 11,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 527/30 | 156/30 | 1,20 | 0,85 | 0,08R | €-3,33 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 430/30 | 139/30 | 1,14 | 0,91 | 0,07R | €-2,12 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 588/30 | 142/30 | 1,11 | 0,87 | 0,05R | €-2,54 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 464/30 | 150/30 | 1,09 | 1,13 | 0,05R | €2,56 | 12,06% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 438/30 | 146/30 | 1,12 | 1,13 | 0,06R | €2,67 | 11,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 567/30 | 167/30 | 1,14 | 1,32 | 0,07R | €5,85 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 38/30 | 24/30 | 0,82 | 1,01 | -0,12R | €0,39 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 10/30 | 9/30 | 1,92 | 2,16 | 0,39R | €21,25 | 1,01% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 27/30 | 16/30 | 0,78 | 0,68 | -0,12R | €-11,25 | 2,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 6/30 | 5/30 | 2,48 | 0,88 | 0,51R | €-3,80 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 29/30 | 18/30 | 1,06 | 1,99 | 0,03R | €16,66 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 8/30 | 7/30 | 1,01 | 1,87 | 0,01R | €20,67 | 1,61% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 36/30 | 23/30 | 0,90 | 1,11 | -0,06R | €3,19 | 3,33% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 11/30 | 10/30 | 0,73 | 1,22 | -0,18R | €5,77 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.09051**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 33.4 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 79820.8 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, stop_within_limit**
- High **0.09066**; close **0.09047**; wick alta **23.8%**; volume **x0.32**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=515; LEGACY_RESEARCH_EVIDENCE_V3=9365; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **90,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +6.46%, 100% oltre +1%.
- BTC trend score: **3,00**; ADX: **17,10**; breadth sopra EMA50: **100,00%**
- Mediana alt vs BTC: **6,46%**; dispersione: **12,65%**

- Aperti in questo ciclo: **145**
- Chiusi in questo ciclo: **170**
- Posizioni research aperte: **1090**
- Trade research chiusi: **41634**
- Eventi di mercato indipendenti chiusi: **5577**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **111876**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 13 | 691 | 691 | 36,90% | 0,91 | -0,05R | €-314,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 14 | 645 | 645 | 36,43% | 0,88 | -0,06R | €-382,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 9 | 313 | 313 | 49,20% | 1,00 | 0,00R | €1,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 7 | 318 | 318 | 38,36% | 0,97 | -0,02R | €-53,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 11 | 602 | 602 | 38,54% | 1,02 | 0,01R | €44,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 12 | 554 | 554 | 38,81% | 1,00 | -0,00R | €-8,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 3 | 177 | 177 | 38,98% | 0,97 | -0,01R | €-20,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 9 | 420 | 420 | 34,29% | 0,85 | -0,08R | €-331,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 12 | 609 | 609 | 34,15% | 0,84 | -0,08R | €-480,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 13 | 562 | 562 | 33,10% | 0,76 | -0,12R | €-677,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 11 | 602 | 602 | 38,87% | 1,04 | 0,02R | €104,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 15 | 985 | 985 | 41,12% | 0,94 | -0,03R | €-257,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 2 | 212 | 212 | 37,26% | 0,72 | -0,17R | €-353,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 15 | 863 | 863 | 34,76% | 0,87 | -0,07R | €-571,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 15 | 867 | 867 | 34,72% | 0,87 | -0,07R | €-572,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 16 | 803 | 803 | 34,12% | 0,82 | -0,09R | €-734,34 |
| MAIN | 27 | 396 | 396 | 30,81% | 0,85 | -0,09R | €-344,65 |
| RSI_EXTREME_LONG_15M | 0 | 32 | 32 | 40,62% | 0,45 | -0,28R | €-90,05 |
| RSI_EXTREME_SHORT_15M | 1 | 51 | 51 | 37,25% | 0,64 | -0,20R | €-100,30 |
| Bilanciata 1H V1 | 28 | 1007 | 1007 | 37,14% | 0,93 | -0,04R | €-362,28 |
| Bilanciata 1H V2 | 12 | 390 | 339 | 42,31% | 1,21 | 0,10R | €405,52 |
| Bilanciata 1H V3 Filtered | 16 | 645 | 645 | 38,60% | 1,00 | -0,00R | €-5,89 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 16 | 566 | 566 | 38,52% | 0,95 | -0,03R | €-151,23 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 9 | 314 | 314 | 40,13% | 0,98 | -0,01R | €-23,15 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 15 | 642 | 642 | 38,16% | 0,93 | -0,03R | €-213,46 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 15 | 709 | 709 | 38,65% | 0,95 | -0,03R | €-179,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 21 | 1141 | 1141 | 37,16% | 0,88 | -0,06R | €-699,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 10 | 652 | 652 | 39,42% | 0,94 | -0,03R | €-179,88 |
| SHADOW_1H_FAST_TP2_V1 | 20 | 1093 | 1093 | 35,13% | 0,87 | -0,06R | €-707,29 |
| Rapida 1H V2 | 3 | 101 | 87 | 45,54% | 1,01 | 0,01R | €6,07 |
| Rapida 1H V3 Filtered | 17 | 1055 | 1055 | 37,54% | 0,90 | -0,05R | €-547,33 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 13 | 793 | 793 | 39,47% | 0,93 | -0,03R | €-271,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 8 | 362 | 362 | 50,28% | 1,06 | 0,03R | €115,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 7 | 366 | 366 | 40,98% | 1,03 | 0,01R | €51,88 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 13 | 688 | 688 | 40,70% | 1,02 | 0,01R | €53,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 14 | 733 | 733 | 36,70% | 0,88 | -0,06R | €-429,57 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 17 | 1008 | 1008 | 37,10% | 0,88 | -0,06R | €-629,28 |
| SHADOW_4H_WIDE | 39 | 368 | 368 | 25,00% | 0,89 | -0,07R | €-252,35 |
| SHADOW_BOLLINGER_MR_1H | 5 | 353 | 353 | 49,01% | 1,12 | 0,05R | €179,89 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 15 | 15 | 46,67% | 0,64 | -0,19R | €-28,10 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 3 | 3 | 33,33% | 1,15 | 0,10R | €3,08 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 9 | 9 | 77,78% | 3,40 | 0,60R | €54,38 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 3 | 3 | 66,67% | 2,22 | 0,45R | €13,43 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-104,12 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 7 | 7 | 14,29% | 0,42 | -0,53R | €-37,20 |
| SHADOW_BTC_EMA_1H | 0 | 26 | 26 | 34,62% | 0,48 | -0,37R | €-97,25 |
| SHADOW_BTC_EMA_4H | 1 | 5 | 5 | 20,00% | 0,56 | -0,37R | €-18,62 |
| SHADOW_COMBO_ADAPTIVE | 24 | 834 | 834 | 40,05% | 1,01 | 0,01R | €43,19 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 19 | 531 | 531 | 42,00% | 1,10 | 0,05R | €268,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 23 | 931 | 931 | 41,57% | 1,02 | 0,01R | €83,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 24 | 775 | 775 | 42,19% | 0,98 | -0,01R | €-94,14 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 97 | 97 | 47,42% | 1,31 | 0,13R | €129,61 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 97 | 97 | 42,27% | 1,29 | 0,12R | €119,82 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 12 | 285 | 285 | 38,95% | 1,00 | 0,00R | €2,87 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 274 | 274 | 40,88% | 1,02 | 0,01R | €27,59 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 130 | 130 | 46,15% | 1,04 | 0,02R | €26,23 |
| SHADOW_COMBO_SCANNER | 16 | 537 | 537 | 39,29% | 1,12 | 0,06R | €334,17 |
| SHADOW_COMBO_TREND | 25 | 700 | 700 | 37,00% | 1,00 | -0,00R | €-12,80 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 18 | 18 | 66,67% | 1,84 | 0,26R | €47,07 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 22 | 22 | 40,91% | 0,66 | -0,22R | €-49,16 |
| SHADOW_DOGE_EMA_1H | 1 | 37 | 37 | 32,43% | 0,52 | -0,31R | €-114,24 |
| SHADOW_DONCHIAN_1H | 14 | 370 | 370 | 35,14% | 0,91 | -0,05R | €-197,77 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 14 | 300 | 300 | 37,33% | 0,92 | -0,04R | €-132,69 |
| SHADOW_EMA_TREND_1H | 25 | 713 | 713 | 36,33% | 0,96 | -0,02R | €-148,12 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 27 | 27 | 33,33% | 0,53 | -0,35R | €-93,51 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 18 | 18 | 61,11% | 1,96 | 0,36R | €63,90 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 25 | 25 | 28,00% | 0,45 | -0,42R | €-105,46 |
| SHADOW_ETH_EMA_1H | 1 | 40 | 40 | 35,00% | 0,48 | -0,36R | €-142,45 |
| SHADOW_ETH_EMA_4H | 0 | 7 | 7 | 42,86% | 0,49 | -0,31R | €-21,53 |
| SHADOW_GLOBAL_PURE | 0 | 18 | 18 | 44,44% | 0,85 | -0,09R | €-16,16 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 13 | 360 | 360 | 35,83% | 1,15 | 0,09R | €326,79 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 10 | 682 | 682 | 67,30% | 1,38 | 0,12R | €803,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 10 | 300 | 300 | 35,67% | 1,15 | 0,09R | €279,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 13 | 329 | 329 | 35,26% | 1,17 | 0,10R | €336,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 214 | 214 | 33,18% | 1,03 | 0,02R | €34,70 |
| SHADOW_MASTER_ADAPTIVE_V1 | 13 | 344 | 344 | 35,76% | 1,14 | 0,09R | €305,46 |
| Forza relativa 1H V1 | 29 | 840 | 840 | 33,81% | 0,94 | -0,03R | €-279,10 |
| Forza relativa 1H V2 | 14 | 357 | 331 | 38,94% | 1,19 | 0,09R | €338,21 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 7 | 272 | 272 | 27,57% | 0,51 | -0,28R | €-769,09 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 7 | 272 | 272 | 27,57% | 0,51 | -0,28R | €-769,09 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 7 | 272 | 272 | 27,57% | 0,51 | -0,28R | €-769,09 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 301 | 301 | 29,24% | 0,64 | -0,20R | €-607,62 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 7 | 330 | 330 | 52,73% | 0,75 | -0,11R | €-374,85 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 7 | 299 | 299 | 52,17% | 0,67 | -0,15R | €-445,60 |
| SHADOW_SCANNER_TOP10_LONG | 20 | 536 | 536 | 41,04% | 1,07 | 0,04R | €189,36 |
| SHADOW_SCANNER_TOP15_LONG | 20 | 538 | 538 | 41,08% | 1,07 | 0,04R | €192,88 |
| SHADOW_SCANNER_TOP20_LONG | 20 | 538 | 538 | 41,08% | 1,07 | 0,04R | €192,88 |
| SHADOW_SCANNER_TOP5_BTC | 16 | 517 | 517 | 39,07% | 1,13 | 0,07R | €361,65 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 13 | 184 | 184 | 31,52% | 0,75 | -0,15R | €-273,37 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 15 | 375 | 375 | 34,93% | 0,92 | -0,04R | €-161,72 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 13 | 399 | 399 | 43,86% | 1,13 | 0,05R | €215,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 14 | 333 | 333 | 36,34% | 0,98 | -0,01R | €-26,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 14 | 527 | 527 | 44,97% | 1,20 | 0,08R | €433,69 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 15 | 430 | 430 | 39,77% | 1,14 | 0,07R | €295,24 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 15 | 588 | 588 | 43,88% | 1,11 | 0,05R | €276,09 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 16 | 464 | 464 | 38,36% | 1,09 | 0,05R | €215,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 15 | 438 | 438 | 37,90% | 1,12 | 0,06R | €260,04 |
| SHADOW_SCANNER_TOP5_LONG | 15 | 567 | 567 | 40,56% | 1,14 | 0,07R | €399,72 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 38 | 38 | 39,47% | 0,82 | -0,12R | €-44,67 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 10 | 10 | 60,00% | 1,92 | 0,39R | €38,66 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 27 | 27 | 48,15% | 0,78 | -0,12R | €-33,53 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 6 | 6 | 66,67% | 2,48 | 0,51R | €30,82 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 29 | 29 | 48,28% | 1,06 | 0,03R | €9,31 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 8 | 8 | 37,50% | 1,01 | 0,01R | €0,57 |
| SHADOW_SOL_EMA_1H | 1 | 36 | 36 | 38,89% | 0,90 | -0,06R | €-23,36 |
| SHADOW_SOL_EMA_4H | 0 | 11 | 11 | 36,36% | 0,73 | -0,18R | €-20,11 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 2 | 94 | 94 | 27,66% | 0,51 | -0,29R | €-270,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 6 | 190 | 190 | 46,32% | 1,18 | 0,08R | €158,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 3 | 151 | 151 | 37,75% | 0,83 | -0,08R | €-120,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,23R | €-49,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 7 | 7 | 71,43% | 2,09 | 0,32R | €22,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 1 | 66 | 66 | 36,36% | 1,37 | 0,15R | €97,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 63 | 63 | 22,22% | 0,51 | -0,25R | €-154,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 2 | 88 | 88 | 27,27% | 0,42 | -0,36R | €-316,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 6 | 171 | 171 | 45,03% | 1,17 | 0,08R | €141,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 3 | 144 | 144 | 37,50% | 0,79 | -0,10R | €-142,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,57 | -0,25R | €-50,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 5,17 | 0,70R | €42,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 1 | 65 | 65 | 36,92% | 1,33 | 0,13R | €85,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 59 | 59 | 23,73% | 0,43 | -0,29R | €-171,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 12 | 12 | 41,67% | 0,62 | -0,24R | €-28,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 6 | 95 | 95 | 50,53% | 1,17 | 0,09R | €82,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 81 | 81 | 44,44% | 0,73 | -0,16R | €-126,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 41 | 41 | 63,41% | 2,06 | 0,35R | €143,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 48 | 48 | 45,83% | 0,81 | -0,09R | €-42,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,66 | -0,20R | €-21,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 4 | 99 | 99 | 43,43% | 1,09 | 0,04R | €44,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 84 | 84 | 40,48% | 0,78 | -0,11R | €-93,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 41 | 41 | 36,59% | 1,70 | 0,22R | €90,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 47 | 47 | 29,79% | 0,82 | -0,07R | €-33,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 43 | 43 | 32,56% | 0,81 | -0,07R | €-32,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 9 | 223 | 223 | 40,36% | 0,94 | -0,03R | €-71,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 1 | 112 | 112 | 41,07% | 1,02 | 0,01R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 56 | 56 | 41,07% | 1,68 | 0,23R | €128,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 67 | 67 | 32,84% | 0,85 | -0,07R | €-47,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 42 | 42 | 33,33% | 0,81 | -0,08R | €-32,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 8 | 203 | 203 | 40,39% | 0,96 | -0,02R | €-42,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 1 | 99 | 99 | 43,43% | 1,06 | 0,03R | €27,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 1 | 54 | 54 | 40,74% | 1,63 | 0,21R | €113,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 1 | 61 | 61 | 32,79% | 0,63 | -0,17R | €-106,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 3 | 173 | 173 | 38,73% | 0,97 | -0,01R | €-21,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 2 | 31 | 31 | 25,81% | 0,36 | -0,47R | €-146,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 6 | 112 | 112 | 37,50% | 0,92 | -0,04R | €-50,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 1 | 156 | 156 | 38,46% | 0,99 | -0,00R | €-5,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 48 | 48 | 35,42% | 1,25 | 0,10R | €49,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 2 | 54 | 54 | 27,78% | 0,52 | -0,29R | €-155,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 7 | 123 | 123 | 38,21% | 0,94 | -0,03R | €-37,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 2 | 195 | 195 | 37,44% | 0,91 | -0,05R | €-88,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 66 | 66 | 33,33% | 1,13 | 0,05R | €33,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 84 | 84 | 27,38% | 0,69 | -0,15R | €-127,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 2 | 52 | 52 | 26,92% | 0,49 | -0,32R | €-167,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 6 | 108 | 108 | 37,04% | 0,88 | -0,07R | €-72,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 2 | 182 | 182 | 36,81% | 0,86 | -0,07R | €-118,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 1 | 64 | 64 | 32,81% | 1,02 | 0,01R | €4,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 78 | 78 | 26,92% | 0,52 | -0,24R | €-190,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 43 | 43 | 32,56% | 0,81 | -0,07R | €-32,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 9 | 224 | 224 | 40,62% | 0,95 | -0,02R | €-51,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 1 | 112 | 112 | 42,86% | 1,14 | 0,06R | €72,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 56 | 56 | 41,07% | 1,68 | 0,23R | €128,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 67 | 67 | 32,84% | 0,85 | -0,07R | €-47,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 141 | 141 | 36,17% | 0,58 | -0,21R | €-301,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 9 | 264 | 264 | 42,42% | 1,04 | 0,02R | €46,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 2 | 220 | 220 | 41,82% | 1,03 | 0,01R | €30,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 32 | 32 | 34,38% | 0,58 | -0,23R | €-73,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 8 | 8 | 50,00% | 0,84 | -0,08R | €-6,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 1 | 86 | 86 | 47,67% | 1,64 | 0,19R | €163,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 96 | 96 | 40,62% | 0,82 | -0,09R | €-82,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 32 | 32 | 31,25% | 0,52 | -0,34R | €-109,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 2 | 48 | 48 | 35,42% | 0,76 | -0,15R | €-72,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 75 | 75 | 42,67% | 0,79 | -0,10R | €-78,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 14 | 14 | 57,14% | 1,67 | 0,31R | €43,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 29 | 29 | 24,14% | 0,38 | -0,42R | €-121,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 2 | 118 | 118 | 26,27% | 0,50 | -0,28R | €-325,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 9 | 235 | 235 | 40,00% | 0,96 | -0,02R | €-46,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 2 | 191 | 191 | 37,17% | 0,90 | -0,05R | €-93,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 1 | 77 | 77 | 37,66% | 1,42 | 0,16R | €124,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 83 | 83 | 26,51% | 0,64 | -0,18R | €-146,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 2 | 118 | 118 | 26,27% | 0,50 | -0,28R | €-325,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 9 | 237 | 237 | 40,08% | 0,97 | -0,02R | €-36,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 2 | 192 | 192 | 36,98% | 0,89 | -0,05R | €-103,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 1 | 77 | 77 | 37,66% | 1,42 | 0,16R | €124,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 83 | 83 | 26,51% | 0,64 | -0,18R | €-146,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 112 | 112 | 26,79% | 0,49 | -0,29R | €-326,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 8 | 213 | 213 | 39,91% | 0,96 | -0,02R | €-45,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 2 | 180 | 180 | 36,11% | 0,80 | -0,09R | €-169,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 28 | 28 | 25,00% | 0,63 | -0,20R | €-56,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 2 | 75 | 75 | 37,33% | 1,39 | 0,15R | €112,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 77 | 77 | 25,97% | 0,45 | -0,28R | €-215,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 2 | 37 | 37 | 29,73% | 0,82 | -0,10R | €-36,29 |
| MAIN | ALT_ROTATION_UP | 9 | 98 | 98 | 33,67% | 0,75 | -0,15R | €-150,19 |
| MAIN | RANGE | 5 | 88 | 88 | 26,14% | 0,75 | -0,15R | €-130,62 |
| MAIN | RANGE_HIGH_VOL | 1 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 4 | 41 | 41 | 29,27% | 0,81 | -0,11R | €-45,07 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 4 | 45 | 45 | 28,89% | 1,00 | 0,00R | €0,31 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 17 | 17 | 35,29% | 0,15 | -0,54R | €-90,98 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 1 | 23 | 23 | 43,48% | 0,95 | -0,02R | €-4,78 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 3 | 117 | 117 | 26,50% | 0,50 | -0,33R | €-386,52 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 17 | 244 | 244 | 43,44% | 1,09 | 0,05R | €112,19 |
| Bilanciata 1H V1 | RANGE | 2 | 220 | 220 | 42,27% | 1,12 | 0,06R | €123,45 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 27,66% | 0,51 | -0,32R | €-151,94 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-2,77 |
| Bilanciata 1H V1 | TRANSITION | 1 | 113 | 113 | 38,05% | 1,11 | 0,05R | €60,46 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 1 | 125 | 125 | 32,00% | 0,91 | -0,05R | €-57,79 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 9 | 136 | 114 | 49,26% | 1,55 | 0,24R | €328,22 |
| Bilanciata 1H V2 | RANGE | 3 | 159 | 143 | 38,36% | 0,96 | -0,02R | €-32,17 |
| Bilanciata 1H V2 | TRANSITION | 0 | 95 | 82 | 38,95% | 1,23 | 0,12R | €109,47 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 86 | 86 | 26,74% | 0,45 | -0,37R | €-318,47 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 9 | 149 | 149 | 43,62% | 1,20 | 0,10R | €155,76 |
| Bilanciata 1H V3 Filtered | RANGE | 3 | 152 | 152 | 43,42% | 1,15 | 0,07R | €106,58 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,52 | -0,32R | €-61,13 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 62 | 62 | 37,10% | 1,12 | 0,06R | €35,50 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 72 | 72 | 34,72% | 1,14 | 0,07R | €48,38 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 75 | 75 | 24,00% | 0,31 | -0,47R | €-351,84 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 9 | 147 | 147 | 44,22% | 1,23 | 0,12R | €176,75 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 3 | 130 | 130 | 42,31% | 0,98 | -0,01R | €-9,58 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,62 | -0,24R | €-40,30 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 54 | 54 | 37,04% | 1,13 | 0,06R | €29,82 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 1 | 51 | 51 | 31,37% | 0,95 | -0,02R | €-12,46 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 22,58% | 0,49 | -0,26R | €-80,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 8 | 94 | 94 | 46,81% | 1,11 | 0,05R | €42,66 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 62 | 62 | 45,16% | 1,15 | 0,08R | €48,63 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -1,10R | €-76,85 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 45,95% | 1,50 | 0,20R | €74,56 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 63 | 63 | 33,33% | 0,87 | -0,06R | €-35,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 50 | 50 | 32,00% | 0,77 | -0,12R | €-58,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 8 | 140 | 140 | 46,43% | 1,13 | 0,06R | €89,96 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 2 | 194 | 194 | 38,14% | 0,89 | -0,05R | €-100,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 1 | 76 | 76 | 39,47% | 1,13 | 0,05R | €37,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 91 | 91 | 31,87% | 0,87 | -0,05R | €-49,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 68 | 68 | 29,41% | 0,64 | -0,21R | €-140,90 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 8 | 141 | 141 | 46,81% | 1,16 | 0,07R | €103,85 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 2 | 224 | 224 | 41,07% | 1,04 | 0,02R | €44,33 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 78 | 78 | 41,03% | 1,22 | 0,09R | €67,63 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 107 | 107 | 30,84% | 0,77 | -0,11R | €-121,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 153 | 153 | 28,10% | 0,56 | -0,26R | €-401,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 14 | 290 | 290 | 41,38% | 0,92 | -0,04R | €-115,44 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 2 | 268 | 268 | 39,93% | 0,98 | -0,01R | €-23,40 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 40 | 40 | 37,50% | 0,86 | -0,07R | €-29,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 54,55% | 1,45 | 0,17R | €18,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 105 | 105 | 41,90% | 1,33 | 0,13R | €133,57 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 122 | 122 | 30,33% | 0,77 | -0,11R | €-140,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 50 | 50 | 46,00% | 1,46 | 0,17R | €87,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 2 | 88 | 88 | 27,27% | 0,45 | -0,37R | €-321,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 5 | 172 | 172 | 45,35% | 1,09 | 0,04R | €75,46 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 2 | 149 | 149 | 43,62% | 1,16 | 0,08R | €113,99 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 38,89% | 0,78 | -0,12R | €-21,79 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 100,00% | ∞ | 0,89R | €62,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 60 | 60 | 41,67% | 1,53 | 0,18R | €106,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 71 | 71 | 29,58% | 0,69 | -0,16R | €-116,97 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 2 | 152 | 152 | 27,63% | 0,58 | -0,24R | €-370,68 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 13 | 287 | 287 | 41,81% | 1,02 | 0,01R | €31,95 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 246 | 246 | 37,80% | 0,95 | -0,02R | €-60,10 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 39 | 39 | 28,21% | 0,64 | -0,20R | €-78,08 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 50,00% | 1,49 | 0,20R | €20,16 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 100 | 100 | 40,00% | 1,37 | 0,15R | €148,42 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 112 | 112 | 24,11% | 0,56 | -0,23R | €-253,95 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 2 | 32 | 29 | 46,88% | 0,97 | -0,02R | €-5,69 |
| Rapida 1H V2 | RANGE | 0 | 60 | 49 | 43,33% | 1,05 | 0,02R | €13,54 |
| Rapida 1H V2 | TRANSITION | 1 | 9 | 9 | 55,56% | 0,95 | -0,02R | €-1,77 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 146 | 146 | 28,08% | 0,51 | -0,29R | €-421,63 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 10 | 262 | 262 | 42,75% | 1,02 | 0,01R | €19,60 |
| Rapida 1H V3 Filtered | RANGE | 2 | 241 | 241 | 39,42% | 0,97 | -0,01R | €-30,10 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 34 | 34 | 38,24% | 0,87 | -0,07R | €-23,20 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| Rapida 1H V3 Filtered | TRANSITION | 2 | 90 | 90 | 40,00% | 1,27 | 0,11R | €96,33 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 121 | 121 | 38,02% | 1,03 | 0,01R | €16,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 61 | 61 | 36,07% | 0,87 | -0,07R | €-42,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 116 | 116 | 29,31% | 0,49 | -0,31R | €-364,95 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 6 | 208 | 208 | 47,60% | 1,17 | 0,08R | €162,85 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 3 | 182 | 182 | 40,11% | 0,99 | -0,00R | €-7,95 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 24 | 24 | 37,50% | 0,79 | -0,11R | €-26,88 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 87,50% | 6,12 | 0,65R | €51,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 1 | 69 | 69 | 40,58% | 1,26 | 0,10R | €71,64 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 81 | 81 | 30,86% | 0,72 | -0,15R | €-117,55 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,24 | -0,58R | €-110,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 5 | 106 | 106 | 52,83% | 1,13 | 0,06R | €66,86 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 97 | 97 | 46,39% | 1,00 | -0,00R | €-1,92 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 42 | 42 | 64,29% | 2,11 | 0,33R | €140,23 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 59 | 59 | 50,85% | 1,05 | 0,02R | €14,03 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 16,67% | 0,23 | -0,58R | €-104,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 4 | 108 | 108 | 44,44% | 1,07 | 0,03R | €36,99 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 99 | 99 | 44,44% | 1,10 | 0,05R | €50,44 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 42 | 42 | 42,86% | 1,74 | 0,23R | €95,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 60 | 60 | 35,00% | 0,94 | -0,03R | €-15,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 53 | 53 | 26,42% | 0,45 | -0,29R | €-151,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 10 | 250 | 250 | 42,40% | 0,99 | -0,01R | €-16,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 1 | 134 | 134 | 44,78% | 1,19 | 0,09R | €117,12 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 59 | 59 | 45,76% | 1,67 | 0,23R | €134,88 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 80 | 80 | 36,25% | 0,95 | -0,02R | €-18,57 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 43,59% | 1,23 | 0,10R | €40,01 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 76 | 76 | 28,95% | 0,53 | -0,29R | €-221,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 8 | 136 | 136 | 40,44% | 0,95 | -0,02R | €-33,16 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 2 | 243 | 243 | 40,33% | 1,02 | 0,01R | €17,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 72 | 72 | 37,50% | 1,21 | 0,08R | €58,34 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 107 | 107 | 33,64% | 0,84 | -0,08R | €-89,18 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 145 | 145 | 28,28% | 0,52 | -0,28R | €-410,20 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 10 | 261 | 261 | 42,15% | 0,98 | -0,01R | €-21,52 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 2 | 239 | 239 | 39,33% | 0,96 | -0,02R | €-44,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,92 | -0,04R | €-13,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 2 | 85 | 85 | 40,00% | 1,30 | 0,12R | €99,10 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 104 | 104 | 32,69% | 0,80 | -0,10R | €-106,74 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 41 | 41 | 41,46% | 1,16 | 0,07R | €29,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 5 | 32 | 32 | 25,00% | 1,09 | 0,05R | €15,87 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 12 | 80 | 80 | 37,50% | 1,08 | 0,05R | €37,62 |
| SHADOW_4H_WIDE | RANGE | 6 | 82 | 82 | 17,07% | 0,70 | -0,20R | €-165,97 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 1 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 41 | 41 | 17,07% | 0,55 | -0,31R | €-128,31 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 45 | 45 | 28,89% | 1,28 | 0,16R | €70,22 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 3 | 19 | 19 | 21,05% | 0,75 | -0,17R | €-31,47 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 38 | 38 | 52,63% | 1,17 | 0,07R | €27,21 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 4 | 115 | 115 | 50,43% | 1,19 | 0,08R | €91,90 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 88 | 88 | 45,45% | 0,89 | -0,05R | €-47,29 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 60,00% | 2,25 | 0,41R | €41,08 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 1 | 17 | 17 | 52,94% | 1,54 | 0,24R | €40,26 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 44 | 44 | 40,91% | 0,79 | -0,11R | €-47,95 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 45,00% | 1,00 | 0,00R | €0,09 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 0,83 | -0,08R | €-4,03 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,32 | 0,69R | €13,75 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 1,54 | 0,20R | €6,15 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 2,22 | 0,45R | €13,43 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 33,33% | 0,43 | -0,43R | €-25,78 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 14,29% | 0,18 | -0,68R | €-47,37 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 1,28 | 0,20R | €5,87 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,28 | -0,68R | €-47,66 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,15 | -0,70R | €-28,17 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 6 | 6 | 50,00% | 1,03 | 0,01R | €0,85 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 4 | 102 | 102 | 29,41% | 0,63 | -0,23R | €-231,69 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 13 | 203 | 203 | 44,33% | 1,14 | 0,08R | €156,60 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 3 | 180 | 180 | 45,00% | 1,05 | 0,02R | €39,97 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 33 | 33 | 39,39% | 0,91 | -0,04R | €-14,24 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,95 | -0,03R | €-3,06 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 88 | 88 | 42,05% | 1,28 | 0,13R | €110,65 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 75 | 75 | 34,67% | 0,89 | -0,05R | €-37,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 104 | 104 | 37,50% | 1,07 | 0,03R | €32,77 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 38 | 38 | 31,58% | 0,83 | -0,09R | €-35,31 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 13 | 195 | 195 | 44,10% | 1,12 | 0,06R | €123,88 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 2 | 91 | 91 | 51,65% | 1,37 | 0,16R | €149,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 49 | 49 | 46,94% | 1,81 | 0,26R | €126,92 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 1 | 63 | 63 | 31,75% | 0,64 | -0,17R | €-106,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 120 | 120 | 35,83% | 0,73 | -0,14R | €-162,29 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 14 | 235 | 235 | 40,43% | 1,01 | 0,01R | €16,52 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 3 | 190 | 190 | 43,16% | 1,23 | 0,09R | €176,52 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 40 | 40 | 40,00% | 0,75 | -0,11R | €-43,81 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,51 | -0,30R | €-35,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 82 | 82 | 45,12% | 1,20 | 0,08R | €65,50 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 98 | 98 | 36,73% | 0,88 | -0,05R | €-46,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 107 | 107 | 50,47% | 1,28 | 0,11R | €123,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 102 | 102 | 29,41% | 0,64 | -0,22R | €-224,16 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 13 | 201 | 201 | 44,78% | 1,09 | 0,05R | €92,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 3 | 168 | 168 | 48,21% | 1,12 | 0,06R | €97,01 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 31 | 31 | 45,16% | 1,09 | 0,04R | €12,23 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,75 | -0,16R | €-15,75 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 71 | 71 | 46,48% | 1,24 | 0,11R | €75,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 75 | 75 | 38,67% | 0,90 | -0,05R | €-33,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 1 | 83 | 83 | 38,55% | 0,76 | -0,11R | €-93,63 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 43 | 43 | 39,53% | 0,90 | -0,05R | €-23,19 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 35 | 35 | 51,43% | 1,47 | 0,18R | €64,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 57,89% | 2,69 | 0,47R | €88,74 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 43 | 43 | 39,53% | 0,84 | -0,08R | €-35,35 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 35 | 35 | 40,00% | 1,31 | 0,12R | €42,81 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 3,13 | 0,59R | €112,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 26 | 26 | 30,77% | 0,61 | -0,21R | €-53,91 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 5 | 90 | 90 | 42,22% | 0,99 | -0,00R | €-4,33 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 56 | 56 | 41,07% | 1,06 | 0,03R | €17,01 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 36 | 36 | 38,89% | 0,90 | -0,05R | €-18,65 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 1 | 25 | 25 | 36,00% | 0,96 | -0,02R | €-4,09 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 2 | 105 | 105 | 40,95% | 1,05 | 0,02R | €23,31 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 1 | 118 | 118 | 37,29% | 0,82 | -0,09R | €-101,71 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 27 | 27 | 37,04% | 0,69 | -0,14R | €-38,44 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 16 | 16 | 37,50% | 0,81 | -0,12R | €-18,76 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 41 | 41 | 43,90% | 1,00 | -0,00R | €-0,70 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 7 | 7 | 71,43% | 5,11 | 0,67R | €47,21 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 41 | 41 | 24,39% | 0,41 | -0,40R | €-165,74 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 12 | 159 | 159 | 42,77% | 1,21 | 0,11R | €178,90 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 104 | 104 | 48,08% | 1,47 | 0,21R | €221,35 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 14 | 14 | 35,71% | 0,54 | -0,25R | €-35,18 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 68 | 68 | 44,12% | 1,62 | 0,27R | €180,91 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 1 | 71 | 71 | 30,99% | 1,03 | 0,01R | €9,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 4 | 79 | 79 | 29,11% | 0,52 | -0,31R | €-247,98 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 15 | 177 | 177 | 44,07% | 1,18 | 0,10R | €169,75 |
| SHADOW_COMBO_TREND | RANGE | 2 | 159 | 159 | 39,62% | 1,15 | 0,07R | €113,63 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 24 | 24 | 37,50% | 1,18 | 0,08R | €19,31 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 75 | 75 | 36,00% | 1,14 | 0,08R | €57,55 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 67 | 67 | 29,85% | 0,70 | -0,16R | €-107,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 1 | 80 | 80 | 31,25% | 1,04 | 0,02R | €15,11 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 0,93 | -0,03R | €-1,47 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 6 | 6 | 66,67% | 3,84 | 0,56R | €33,45 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 7 | 7 | 71,43% | 1,67 | 0,22R | €15,09 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,06 | -0,84R | €-41,90 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,14 | -0,73R | €-36,57 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,75 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 10 | 10 | 10,00% | 0,09 | -0,71R | €-70,70 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 1 | 10 | 10 | 20,00% | 0,46 | -0,46R | €-45,68 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 11 | 11 | 45,45% | 1,13 | 0,06R | €7,12 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,55R | €5,45 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 51 | 51 | 21,57% | 0,45 | -0,43R | €-217,14 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 6 | 99 | 99 | 35,35% | 0,74 | -0,18R | €-178,33 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 86 | 86 | 39,53% | 1,16 | 0,09R | €77,51 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 3 | 30 | 30 | 40,00% | 1,44 | 0,22R | €65,07 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 43 | 43 | 30,23% | 1,15 | 0,07R | €32,24 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 54,17% | 1,90 | 0,44R | €104,71 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 41 | 41 | 19,51% | 0,32 | -0,55R | €-225,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 6 | 91 | 91 | 37,36% | 0,79 | -0,14R | €-127,91 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 66 | 66 | 42,42% | 1,18 | 0,09R | €62,45 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 3 | 23 | 23 | 47,83% | 2,01 | 0,41R | €94,34 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 29 | 29 | 27,59% | 1,04 | 0,02R | €5,27 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,36 | 0,56R | €99,93 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 86 | 86 | 27,91% | 0,46 | -0,37R | €-314,83 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 15 | 179 | 179 | 43,58% | 1,16 | 0,08R | €151,02 |
| SHADOW_EMA_TREND_1H | RANGE | 2 | 155 | 155 | 38,06% | 1,09 | 0,04R | €68,25 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 72 | 72 | 34,72% | 1,04 | 0,02R | €17,55 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 85 | 85 | 29,41% | 0,90 | -0,06R | €-46,82 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,55 | -0,34R | €-34,23 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 1 | 7 | 7 | 28,57% | 0,45 | -0,44R | €-30,80 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 8 | 8 | 62,50% | 3,25 | 0,61R | €48,51 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 66,67% | 1,30 | 0,11R | €3,44 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,21 | -0,60R | €-18,01 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 7 | 7 | 14,29% | 0,29 | -0,66R | €-46,36 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 25,00% | 0,44 | -0,40R | €-32,16 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 14 | 14 | 42,86% | 0,75 | -0,14R | €-19,41 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,25 | -0,55R | €-49,78 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,64 | -0,19R | €-7,65 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,35R | €3,51 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 8 | 8 | 37,50% | 0,75 | -0,17R | €-13,63 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 37,50% | 1,22 | 0,14R | €32,47 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 6 | 66 | 66 | 36,36% | 1,10 | 0,07R | €44,94 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 2 | 102 | 102 | 35,29% | 1,16 | 0,10R | €97,85 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 44 | 44 | 45,45% | 1,79 | 0,39R | €173,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 3 | 67 | 67 | 29,85% | 0,86 | -0,09R | €-63,43 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 59,46% | 1,16 | 0,06R | €22,59 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 8 | 140 | 140 | 70,71% | 1,58 | 0,16R | €224,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 188 | 188 | 67,55% | 1,45 | 0,14R | €258,25 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 98 | 98 | 72,45% | 1,70 | 0,17R | €169,91 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 127 | 127 | 62,20% | 1,04 | 0,02R | €19,40 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 36,36% | 1,27 | 0,15R | €33,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 4 | 103 | 103 | 36,89% | 1,25 | 0,14R | €146,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 2 | 44 | 44 | 43,18% | 1,62 | 0,32R | €142,83 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 3 | 78 | 78 | 26,92% | 0,74 | -0,19R | €-146,97 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 47,37% | 2,00 | 0,49R | €93,92 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 6 | 68 | 68 | 33,82% | 0,99 | -0,01R | €-5,91 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 91 | 91 | 36,26% | 1,36 | 0,21R | €187,81 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 1 | 39 | 39 | 41,03% | 1,52 | 0,28R | €107,45 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 3 | 63 | 63 | 25,40% | 0,71 | -0,21R | €-131,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 18,75% | 0,48 | -0,40R | €-64,65 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 69 | 69 | 37,68% | 1,21 | 0,13R | €88,19 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 34 | 34 | 47,06% | 2,14 | 0,49R | €166,90 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 56 | 56 | 28,57% | 0,81 | -0,14R | €-75,63 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 36,36% | 1,18 | 0,11R | €23,42 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 6 | 67 | 67 | 37,31% | 1,15 | 0,09R | €62,79 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 2 | 95 | 95 | 37,89% | 1,32 | 0,18R | €172,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 43 | 43 | 41,86% | 1,54 | 0,29R | €123,39 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 3 | 66 | 66 | 25,76% | 0,70 | -0,21R | €-141,84 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 5 | 100 | 100 | 30,00% | 0,63 | -0,22R | €-224,34 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 14 | 195 | 195 | 41,54% | 1,13 | 0,07R | €146,23 |
| Forza relativa 1H V1 | RANGE | 3 | 201 | 201 | 32,84% | 0,85 | -0,08R | €-160,65 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 29 | 29 | 27,59% | 0,49 | -0,28R | €-81,70 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 11 | 11 | 27,27% | 0,72 | -0,18R | €-19,83 |
| Forza relativa 1H V1 | TRANSITION | 2 | 88 | 88 | 39,77% | 1,42 | 0,20R | €178,69 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 75 | 75 | 28,00% | 0,87 | -0,07R | €-51,18 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 2 | 105 | 105 | 27,62% | 0,92 | -0,04R | €-44,16 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 34 | 34 | 26,47% | 0,77 | -0,15R | €-50,36 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 3 | 45 | 43 | 37,78% | 0,71 | -0,16R | €-72,73 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 6 | 77 | 71 | 48,05% | 1,65 | 0,31R | €241,09 |
| Forza relativa 1H V2 | RANGE | 3 | 91 | 86 | 34,07% | 0,92 | -0,04R | €-40,26 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 8 | 7 | 25,00% | 0,66 | -0,18R | €-14,36 |
| Forza relativa 1H V2 | TRANSITION | 0 | 48 | 43 | 39,58% | 1,52 | 0,25R | €119,42 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 35 | 34 | 28,57% | 0,95 | -0,02R | €-7,36 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 1 | 41 | 37 | 46,34% | 1,70 | 0,32R | €131,11 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 64 | 64 | 15,62% | 0,19 | -0,63R | €-400,57 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 1,18 | 0,09R | €13,09 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 82 | 82 | 30,49% | 0,52 | -0,24R | €-196,85 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 1 | 25 | 25 | 44,00% | 1,23 | 0,13R | €32,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 64 | 64 | 15,62% | 0,19 | -0,63R | €-400,57 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 1,18 | 0,09R | €13,09 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 82 | 82 | 30,49% | 0,52 | -0,24R | €-196,85 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 1 | 25 | 25 | 44,00% | 1,23 | 0,13R | €32,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 64 | 64 | 15,62% | 0,19 | -0,63R | €-400,57 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 1,18 | 0,09R | €13,09 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 82 | 82 | 30,49% | 0,52 | -0,24R | €-196,85 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 1 | 25 | 25 | 44,00% | 1,23 | 0,13R | €32,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 55 | 55 | 21,82% | 0,38 | -0,44R | €-239,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 16 | 16 | 43,75% | 1,44 | 0,21R | €32,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 96 | 96 | 31,25% | 0,69 | -0,16R | €-154,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 19 | 19 | 47,37% | 1,39 | 0,15R | €28,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 1 | 41 | 41 | 39,02% | 1,06 | 0,03R | €13,35 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 2 | 67 | 67 | 40,30% | 0,40 | -0,35R | €-237,63 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 0,92 | -0,04R | €-4,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 103 | 103 | 61,17% | 0,91 | -0,03R | €-33,86 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 23 | 23 | 65,22% | 1,43 | 0,16R | €35,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 1 | 32 | 32 | 59,38% | 1,40 | 0,17R | €54,53 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 2 | 55 | 55 | 36,36% | 0,25 | -0,46R | €-255,47 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,28 | 0,12R | €17,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 96 | 96 | 62,50% | 0,69 | -0,11R | €-103,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 21 | 21 | 61,90% | 1,24 | 0,10R | €20,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 1 | 31 | 31 | 61,29% | 1,62 | 0,25R | €78,45 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 35 | 35 | 37,14% | 0,93 | -0,04R | €-13,46 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 16 | 205 | 205 | 41,95% | 1,01 | 0,00R | €7,15 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 85 | 85 | 52,94% | 1,47 | 0,19R | €160,92 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 53 | 53 | 41,51% | 1,48 | 0,17R | €90,11 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 1 | 61 | 61 | 31,15% | 0,67 | -0,16R | €-98,71 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 35 | 35 | 37,14% | 0,93 | -0,04R | €-13,40 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 16 | 209 | 209 | 42,58% | 1,02 | 0,01R | €17,85 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 85 | 85 | 52,94% | 1,47 | 0,19R | €160,92 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 53 | 53 | 41,51% | 1,48 | 0,17R | €90,11 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 1 | 61 | 61 | 31,15% | 0,67 | -0,16R | €-98,71 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 35 | 35 | 37,14% | 0,93 | -0,04R | €-13,40 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 16 | 209 | 209 | 42,58% | 1,02 | 0,01R | €17,85 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 85 | 85 | 52,94% | 1,47 | 0,19R | €160,92 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 53 | 53 | 41,51% | 1,48 | 0,17R | €90,11 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 1 | 61 | 61 | 31,15% | 0,67 | -0,16R | €-98,71 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 38 | 38 | 26,32% | 0,46 | -0,35R | €-132,82 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 12 | 158 | 158 | 43,04% | 1,22 | 0,12R | €190,60 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 96 | 96 | 48,96% | 1,59 | 0,25R | €244,38 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 63 | 63 | 42,86% | 1,61 | 0,26R | €166,22 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 1 | 70 | 70 | 30,00% | 0,97 | -0,02R | €-10,90 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,18 | -0,67R | €-119,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 10 | 57 | 57 | 33,33% | 0,77 | -0,15R | €-85,44 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 1 | 8 | 8 | 37,50% | 0,21 | -0,54R | €-42,98 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 30 | 30 | 53,33% | 2,17 | 0,40R | €120,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 57 | 57 | 28,07% | 0,79 | -0,11R | €-64,64 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 32 | 32 | 25,00% | 0,43 | -0,37R | €-119,01 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 10 | 71 | 71 | 32,39% | 0,78 | -0,13R | €-95,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 92 | 92 | 47,83% | 1,43 | 0,19R | €178,64 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 50 | 50 | 48,00% | 2,23 | 0,41R | €204,25 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 51 | 51 | 21,57% | 0,51 | -0,28R | €-144,31 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 33,33% | 0,76 | -0,10R | €-27,82 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 8 | 69 | 69 | 37,68% | 0,91 | -0,04R | €-28,48 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 2 | 112 | 112 | 46,43% | 1,47 | 0,18R | €203,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,63 | -0,15R | €-29,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 50 | 50 | 48,00% | 1,35 | 0,13R | €65,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 1 | 52 | 52 | 50,00% | 1,29 | 0,12R | €64,10 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 57,14% | 1,17 | 0,07R | €5,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 24 | 24 | 29,17% | 0,40 | -0,36R | €-85,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 9 | 55 | 55 | 32,73% | 0,90 | -0,06R | €-34,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 2 | 96 | 96 | 48,96% | 1,46 | 0,21R | €198,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,47 | -0,31R | €-45,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 45 | 45 | 40,00% | 1,61 | 0,24R | €107,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 1 | 40 | 40 | 25,00% | 0,68 | -0,17R | €-69,45 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,42 | -0,37R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 35 | 35 | 40,00% | 0,92 | -0,03R | €-12,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 10 | 162 | 162 | 43,21% | 1,16 | 0,07R | €113,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 1 | 113 | 113 | 46,90% | 1,50 | 0,19R | €216,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,63 | -0,15R | €-29,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 55 | 55 | 43,64% | 1,27 | 0,10R | €54,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 58 | 58 | 50,00% | 1,35 | 0,14R | €80,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 30,00% | 0,51 | -0,30R | €-90,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 11 | 132 | 132 | 45,45% | 1,39 | 0,20R | €261,75 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 95 | 95 | 49,47% | 1,51 | 0,22R | €210,85 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,47 | -0,31R | €-45,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 48 | 48 | 39,58% | 1,46 | 0,19R | €91,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 45 | 45 | 24,44% | 0,71 | -0,16R | €-69,96 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 44 | 44 | 38,64% | 0,82 | -0,08R | €-34,29 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 11 | 187 | 187 | 41,71% | 1,01 | 0,00R | €9,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 1 | 104 | 104 | 48,08% | 1,55 | 0,21R | €218,38 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,53 | -0,21R | €-37,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 62 | 62 | 45,16% | 1,29 | 0,11R | €66,42 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 1 | 71 | 71 | 49,30% | 1,30 | 0,11R | €79,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 31 | 31 | 32,26% | 0,59 | -0,26R | €-80,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 12 | 159 | 159 | 42,77% | 1,24 | 0,13R | €200,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 87 | 87 | 47,13% | 1,50 | 0,23R | €195,90 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 51 | 51 | 41,18% | 1,58 | 0,24R | €120,03 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 1 | 53 | 53 | 22,64% | 0,61 | -0,21R | €-112,98 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 30,00% | 0,60 | -0,26R | €-77,86 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 11 | 150 | 150 | 41,33% | 1,19 | 0,10R | €154,72 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 81 | 81 | 46,91% | 1,60 | 0,28R | €223,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 45 | 45 | 40,00% | 1,82 | 0,30R | €137,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 52 | 52 | 25,00% | 0,69 | -0,16R | €-83,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 31,82% | 0,68 | -0,19R | €-81,80 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 11 | 165 | 165 | 41,21% | 1,05 | 0,03R | €47,23 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 99 | 99 | 51,52% | 1,54 | 0,23R | €226,11 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 66 | 66 | 42,42% | 1,52 | 0,21R | €136,15 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 1 | 90 | 90 | 37,78% | 1,12 | 0,06R | €50,45 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -1,10R | €-76,72 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 11 | 11 | 63,64% | 2,49 | 0,58R | €64,35 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 10 | 10 | 50,00% | 0,90 | -0,05R | €-5,33 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,86 | -0,10R | €-3,05 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 100,00% | ∞ | 1,14R | €34,32 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 80,00% | 2,30 | 0,28R | €13,97 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 10 | 10 | 30,00% | 0,41 | -0,45R | €-45,27 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,53 | -0,33R | €-26,28 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,97 | -0,01R | €-0,27 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 20,00% | 0,16 | -0,75R | €-37,55 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 8 | 8 | 50,00% | 1,36 | 0,20R | €15,94 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 75,00% | 3,12 | 0,60R | €47,76 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,72R | €27,23 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 1,20 | 0,10R | €2,07 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,64 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 1 | 11 | 11 | 63,64% | 2,49 | 0,59R | €64,41 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 9 | 9 | 44,44% | 1,09 | 0,06R | €5,08 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,29 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 1,81 | 0,28R | €8,45 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-06T05:11:06+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **523**
- Scenari virtuali ancora attivi: **9426**
- Gruppi in attesa dell'uscita originale: **482**
- Gruppi con originale chiuso ma Shadow ancora attive: **41**
- Confronti completati: **530842**

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

Generato: 2026-09-06T05:12:52+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **530842**
- Valutazioni prodotte: **27918**
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

Generato: 2026-09-06T05:18:02+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Operativo | Identità | Gross cert. | Net cert. | Pending | Gap | Conflict | Formal review NET | PF storico | PnL storico | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,16 | +€67,59 | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | 22 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,01 | +€2,56 | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,11 | +€95,26 | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | 81 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,09 | +€75,72 | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | 90 | 120 | 28 | 0 | 11 | 80 | 1 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,55 | +€846,28 | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | 38 | 87 | 29 | 0 | 12 | 44 | 2 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 5,77 | +€1.682,13 | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | 154 | 163 | 30 | 0 | 5 | 126 | 2 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 1,65 | +€1.253,39 | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NET_CERTIFIED_CLOSED_PAIRS=0; PROMOTION_TARGET=50 | 0,00 | €0,00 | COLLECTING |

## Regole di valutazione

- Il campione operativo resta esposto per continuità storica, ma non è il campione formale.
- La soglia 50 usa esclusivamente NET_CERTIFIED_CLOSED_PAIRS.
- P0C produce FORMAL_CERTIFIED_OUTCOME; Block-3 produce SIMULATION_RUNTIME_OUTCOME.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-06T05:08:07+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **118**
- Simulazioni completate nel ciclo: **1**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **455.00 R**
- Profitto virtuale mancato: **1738.91 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 391 | 0 | 21826.59 |
| DOWN_20 | 391 | 0 | 43653.18 |
| DOWN_30 | 391 | 5 | 65534.06 |
| DOWN_40 | 391 | 117 | 80864.12 |
| UP_10 | 113 | 2 | 8876.44 |
| UP_20 | 113 | 3 | 17692.88 |
| UP_30 | 113 | 3 | 26416.66 |
| UP_40 | 113 | 52 | 32294.08 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-06T05:05:18+00:00

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

Generato: 2026-09-06T05:18:16+00:00

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

Generato: 2026-09-06T05:18:16+00:00

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

Generato: 2026-09-06T05:18:16+00:00

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

Generato: 2026-09-06T05:18:16+00:00

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
| 1 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 23.9 | E | 49 | 2.17 | 0.483 | 4.71 |
| 2 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 23.5 | E | 148 | 1.49 | 0.241 | 23.36 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 21.1 | E | 191 | 1.26 | 0.128 | 24.60 |
| 4 | SHADOW_DONCHIAN_1H | BASELINE | 20.6 | E | 137 | 1.35 | 0.202 | 18.83 |
| 5 | SHADOW_COMBO_ADAPTIVE | BASELINE | 20.6 | E | 196 | 1.26 | 0.127 | 23.82 |
| 6 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 19.4 | E | 213 | 1.13 | 0.065 | 30.08 |
| 7 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | BASELINE | 19.2 | E | 113 | 1.21 | 0.099 | 7.62 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 19.1 | E | 166 | 1.14 | 0.069 | 14.78 |
| 9 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 19.1 | E | 122 | 1.33 | 0.153 | 14.92 |
| 10 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 18.9 | E | 266 | 1.13 | 0.064 | 32.30 |

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

Generato: 2026-09-06T05:18:16+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BULL_TREND**
- Righe di performance: **1104**
- Strategie preferite nel regime corrente: **18**
- Strategie da evitare nel regime corrente: **11**
- Memorie contestuali: **527**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.621 | 0.00 |
| 2 | SHADOW_SOL_ADAPTIVE_1H | shadow-sol-adaptive-1h | INSUFFICIENT | 77.1 | 8 | 3.44 | 0.678 | 1.17 |
| 3 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | INSUFFICIENT | 75.6 | 8 | 3.45 | 0.679 | 2.14 |
| 4 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 75.5 | 3 | 2.66 | 0.572 | 1.04 |
| 5 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.8 | 12 | 4.37 | 0.378 | 1.07 |
| 6 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 72.7 | 5 | 3.47 | 0.591 | 1.20 |
| 7 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | COMPATIBLE | 68.3 | 51 | 1.53 | 0.300 | 8.09 |
| 8 | SHADOW_SCANNER_TOP15_LONG | shadow-scanner-top15-long | COMPATIBLE | 67.6 | 89 | 1.70 | 0.301 | 11.55 |
| 9 | SHADOW_SCANNER_TOP20_LONG | shadow-scanner-top20-long | COMPATIBLE | 67.6 | 89 | 1.70 | 0.301 | 11.55 |
| 10 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | shadow-donchian-1h-gb20-120r-v1 | COMPATIBLE | 66.6 | 37 | 1.61 | 0.368 | 8.09 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-06T05:18:17+00:00

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

Generato: 2026-09-06T05:08:07+00:00

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
