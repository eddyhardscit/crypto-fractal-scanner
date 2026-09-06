# Paper trading automatico KuCoin

Generato: 2026-09-06T05:33:29+00:00

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
| Combo Trend Side Regime Guard V1 | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | ZEC | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Adaptive 1H | SOL | 60m | LONG | 5,34 | 5,00 | 0,00 | OPENED | 6,2 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Ema 1H | SOL | 60m | LONG | 5,34 | 5,00 | 0,00 | OPENED | 6,2 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Tp3 V1 | DOGE | 60m | LONG | 5,04 | 5,00 | 0,00 | OPENED | 6,2 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Runner25 V1 | DOGE | 60m | LONG | 5,04 | 5,00 | 0,00 | OPENED | 6,2 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | HYPE | 60m | LONG | 8,26 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Tp3 V1 | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 V1 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc Le3 V1 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | UNI | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
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
| 1H Fast Long Btc 1 3 Cap75 V1 | SOL | 60m | LONG | 5,34 | 4,50 | 0,00 | OPENED | 6,2 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | HYPE | 60m | LONG | 8,26 | 5,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | DASH | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,67 | 6,00 | 0,33 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,53 | 6,00 | 0,47 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,91 | 6,00 | 1,09 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 4,90 | 6,00 | 1,10 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,00 | 6,00 | 2,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.2 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | DASH | 60m | LONG | 9,75 | 5,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | DASH | 60m | LONG | 9,75 | 5,00 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | OPENED | 6,2 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | DASH | 60m | LONG | 9,75 | 4,50 | 0,00 | READY | 6,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
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
| TEST | Main Side Regime Guard V1 | 6 | €11.508,55 | €470,58 | €1.411,74 | €165,83 | €334,25 |
| TEST | Scanner Top 5 Long 1H | 7 | €11.382,37 | €1.205,54 | €2.411,09 | €227,65 | €407,08 |
| TEST | Donchian 1H Gb20 120R V1 | 7 | €11.294,64 | €3.466,90 | €6.933,81 | €225,89 | €23,86 |
| TEST | Combo Trend Side Regime Guard V1 | 8 | €11.161,57 | €1.474,38 | €2.948,76 | €162,57 | €372,98 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.069,93 | €716,47 | €2.149,41 | €167,48 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 10 | €10.962,78 | €2.458,63 | €4.917,26 | €217,06 | €395,54 |
| TEST | Scanner Top15 Long | 9 | €10.852,42 | €2.966,35 | €5.932,70 | €217,06 | €381,24 |
| TEST | Scanner Top20 Long | 9 | €10.852,42 | €2.966,35 | €5.932,70 | €217,06 | €381,24 |
| TEST | Combo Adaptive | 9 | €10.753,00 | €1.354,71 | €2.709,42 | €163,02 | €380,91 |
| TEST | Combo Scanner | 8 | €10.678,82 | €1.527,78 | €3.055,57 | €212,04 | €377,45 |
| TEST | Scanner Top 5 + forza BTC 1H | 7 | €10.662,49 | €1.133,67 | €2.267,34 | €213,25 | €381,26 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €10.647,52 | €816,83 | €2.450,48 | €53,70 | €-0,60 |
| TEST | Scanner Top10 Long | 7 | €10.598,31 | €2.354,93 | €4.709,86 | €210,16 | €383,41 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.578,23 | €1.339,25 | €4.017,76 | €211,57 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.578,15 | €477,99 | €1.433,96 | €104,48 | €-0,16 |
| TEST | Rapida 1H V2 | 4 | €10.524,39 | €3.167,07 | €9.501,20 | €209,94 | €-3,02 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.397,05 | €1.562,50 | €4.687,49 | €207,96 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 8 | €10.396,84 | €1.669,91 | €3.339,81 | €205,51 | €8,65 |
| TEST | Scanner Top5 Btc Runner25 V1 | 8 | €10.390,76 | €1.668,93 | €3.337,86 | €205,39 | €8,64 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.330,25 | €1.552,46 | €4.657,37 | €206,63 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 8 | €10.320,77 | €2.090,66 | €6.271,98 | €206,42 | €0,31 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.293,59 | €1.341,14 | €4.023,41 | €51,50 | €-3,92 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.293,18 | €1.023,38 | €3.070,15 | €102,35 | €-13,16 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 9 | €10.258,26 | €1.141,10 | €2.282,21 | €105,30 | €349,79 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.236,06 | €283,45 | €850,36 | €102,04 | €-21,90 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.206,43 | €1.074,29 | €2.148,59 | €203,40 | €40,62 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.161,66 | €574,98 | €1.149,96 | €50,72 | €17,55 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €10.130,56 | €1.075,61 | €3.226,84 | €101,77 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.090,56 | €985,68 | €1.971,36 | €50,34 | €23,12 |
| TEST | Sol Ema 1H | 1 | €10.070,61 | €1.165,90 | €3.497,71 | €50,37 | €-0,70 |
| TEST | Doge Donchian 1H | 0 | €10.066,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 7 | €10.064,80 | €1.048,03 | €2.096,07 | €201,30 | €359,87 |
| TEST | Master Adaptive Gb20 Be V1 | 7 | €10.060,17 | €1.126,02 | €2.252,04 | €201,76 | €330,62 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.054,78 | €1.966,66 | €3.933,32 | €151,23 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.053,19 | €601,17 | €1.803,52 | €150,77 | €-0,01 |
| TEST | Master Adaptive Gb20 Partial V1 | 7 | €10.049,48 | €1.124,82 | €2.249,64 | €201,54 | €330,27 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.039,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Scanner Top5 Btc Mfe V1 | 7 | €9.995,56 | €1.062,76 | €2.125,52 | €199,91 | €357,42 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €9.991,36 | €185,32 | €926,58 | €9,99 | €0,53 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 7 | €9.983,46 | €2.378,63 | €7.135,89 | €199,67 | €0,31 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.979,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 5 | €9.951,01 | €2.590,77 | €7.772,30 | €199,09 | €-6,06 |
| TEST | Btc Ema 4H | 1 | €9.943,99 | €887,05 | €1.774,10 | €49,83 | €-21,51 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.927,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €9.906,26 | €872,82 | €1.745,65 | €48,89 | €71,18 |
| TEST | Master Adaptive Runner25 V1 | 9 | €9.906,22 | €1.426,19 | €2.852,39 | €198,12 | €342,21 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €9.893,29 | €713,30 | €2.139,90 | €147,42 | €-3,22 |
| TEST | Btc Donchian 4H | 1 | €9.890,79 | €882,31 | €1.764,61 | €49,57 | €-21,39 |
| TEST | Eth Ema 4H | 1 | €9.889,03 | €690,19 | €1.380,39 | €49,44 | €2,75 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.886,07 | €1.297,12 | €3.891,37 | €197,72 | €0,02 |
| TEST | Master Adaptive Gb20 V1 | 7 | €9.878,50 | €1.105,61 | €2.211,23 | €198,11 | €324,65 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €9.860,65 | €2.325,88 | €6.977,65 | €189,11 | €369,88 |
| TEST | Forza relativa 1H V2 | 5 | €9.839,23 | €828,41 | €1.656,82 | €98,36 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 7 | €9.830,73 | €1.023,66 | €2.047,32 | €196,62 | €351,50 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 3 | €9.823,03 | €496,99 | €1.490,96 | €144,94 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.819,89 | €1.363,89 | €4.091,66 | €49,10 | €2,35 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.781,66 | €861,84 | €1.723,69 | €48,27 | €70,28 |
| TEST | Eth Adaptive 1H | 1 | €9.762,70 | €1.128,47 | €3.385,42 | €48,75 | €14,71 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.726,53 | €1.123,27 | €3.369,80 | €0,00 | €23,53 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.719,02 | €1.004,71 | €3.014,12 | €145,58 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.717,32 | €1.262,13 | €3.786,39 | €0,00 | €26,43 |
| TEST | Eth Bollinger 1H | 1 | €9.711,84 | €1.349,47 | €4.048,41 | €48,58 | €-1,91 |
| TEST | Bilanciata 1H V1 | 10 | €9.700,72 | €969,94 | €2.909,82 | €146,99 | €327,53 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.653,74 | €1.132,92 | €3.398,77 | €193,08 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.647,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.557,95 | €1.491,54 | €2.983,09 | €93,59 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 7 | €9.552,88 | €1.251,09 | €2.502,18 | €99,78 | €413,30 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.552,51 | €1.053,15 | €3.159,44 | €191,07 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €9.539,07 | €294,25 | €882,74 | €49,48 | €30,35 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 3 | €9.514,97 | €271,48 | €814,44 | €48,63 | €29,68 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.498,89 | €989,44 | €1.978,87 | €139,00 | €317,85 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.476,95 | €979,65 | €2.938,95 | €141,95 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.463,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 7 | €9.451,40 | €1.490,82 | €2.981,65 | €189,10 | €13,00 |
| TEST | Combo Adaptive Mfe Trail | 9 | €9.382,00 | €1.147,04 | €2.294,09 | €153,41 | €329,49 |
| TEST | Bilanciata 1H V2 | 7 | €9.376,04 | €974,39 | €2.923,18 | €141,82 | €8,87 |
| TEST | Combo Trend | 7 | €9.374,47 | €1.996,25 | €3.992,49 | €89,81 | €305,13 |
| TEST | Combo Adaptive Tp3 V1 | 7 | €9.374,18 | €1.227,70 | €2.455,40 | €97,92 | €405,56 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.369,88 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 7 | €9.367,56 | €989,24 | €1.978,48 | €187,35 | €-2,38 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.362,76 | €1.133,32 | €2.266,63 | €138,90 | €48,51 |
| TEST | 1H Balanced V3 Long Only V1 | 7 | €9.326,37 | €2.199,86 | €6.599,57 | €178,87 | €349,84 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 5 | €9.177,18 | €1.730,31 | €3.460,61 | €138,34 | €51,27 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €9.117,85 | €1.000,45 | €2.000,90 | €134,93 | €50,88 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.009,68 | €634,74 | €1.269,48 | €134,42 | €4,80 |
| TEST | 1H Fast V3 Cap75 V1 | 3 | €9.005,94 | €381,54 | €1.144,62 | €88,57 | €-27,56 |
| TEST | Forza relativa 1H V1 | 7 | €8.985,97 | €1.568,29 | €3.136,58 | €95,38 | €367,81 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €8.903,47 | €1.761,92 | €3.523,83 | €178,08 | €-2,87 |
| TEST | Combo Mean Reversion | 1 | €8.636,37 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €8.264,79 | €2.613,27 | €5.226,54 | €124,12 | €0,68 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 | Momentum / breakout | Versione originale V1 a 1 ora che cerca momentum e breakout. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | Versione V3 derivata dalla V1: mantiene la logica momentum originale ma esclude i segnali con score assoluto da 5,0 a meno di 6,0, fascia risultata negativa nel confronto Paper vs Shadow. |
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
| TEST | Global Confluence puro 1H | Global Confluence puro | Opera soltanto quando Global Confluence, dati exchange e struttura tecnica sono allineati. |
| TEST | Combo Trend | Combo Trend | Portafoglio sperimentale separato. |
| TEST | Combo Mean Reversion | Combo Mean Reversion | Portafoglio sperimentale separato. |
| TEST | Combo Scanner | Combo Scanner | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | Portafoglio sperimentale separato. |
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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,27 | €-181,91 | 59 | 59 | 42,37% | 0,88 | €-3,08 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.566,98 | €1.545,98 | 137 | 137 | 45,99% | 1,51 | €11,28 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.508,55 | €1.175,76 | 49 | 49 | 59,18% | 2,53 | €24,00 | 3,82% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.382,37 | €976,77 | 167 | 167 | 48,50% | 1,32 | €5,85 | 8,85% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.294,64 | €1.274,14 | 105 | 105 | 44,76% | 1,60 | €12,13 | 6,75% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.161,57 | €790,53 | 148 | 148 | 50,68% | 1,27 | €5,34 | 10,10% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.069,93 | €1.071,35 | 191 | 191 | 50,26% | 1,27 | €5,61 | 7,95% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.962,78 | €570,20 | 152 | 152 | 48,68% | 1,20 | €3,75 | 7,78% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.852,42 | €474,77 | 185 | 185 | 48,65% | 1,16 | €2,57 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.852,42 | €474,77 | 185 | 185 | 48,65% | 1,16 | €2,57 | 10,31% |
| TEST | Combo Adaptive | Combo Adaptive | €10.753,00 | €373,88 | 196 | 196 | 45,92% | 1,11 | €1,91 | 8,17% |
| TEST | Combo Scanner | Combo Scanner | €10.678,82 | €303,24 | 178 | 178 | 44,38% | 1,09 | €1,70 | 11,38% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.662,49 | €282,62 | 150 | 150 | 46,00% | 1,10 | €1,88 | 11,27% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.647,52 | €649,42 | 113 | 113 | 50,44% | 1,28 | €5,75 | 4,50% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.598,31 | €217,73 | 164 | 164 | 48,17% | 1,08 | €1,33 | 10,31% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.578,23 | €580,48 | 266 | 266 | 44,36% | 1,13 | €2,18 | 9,28% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.578,15 | €579,29 | 122 | 122 | 50,82% | 1,28 | €4,75 | 5,24% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.524,39 | €533,23 | 70 | 62 | 50,00% | 1,32 | €7,62 | 3,89% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.397,05 | €399,98 | 213 | 213 | 49,30% | 1,11 | €1,88 | 9,50% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.396,84 | €390,22 | 146 | 146 | 43,84% | 1,13 | €2,67 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.390,76 | €384,14 | 150 | 150 | 44,00% | 1,13 | €2,56 | 12,06% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.330,25 | €333,16 | 257 | 257 | 44,36% | 1,07 | €1,30 | 9,48% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.320,77 | €324,23 | 221 | 221 | 43,89% | 1,07 | €1,47 | 10,60% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.293,59 | €299,93 | 18 | 18 | 61,11% | 1,99 | €16,66 | 2,77% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.293,18 | €308,00 | 74 | 74 | 45,95% | 1,18 | €4,16 | 6,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.258,26 | €-89,93 | 149 | 149 | 44,30% | 0,97 | €-0,60 | 11,68% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.236,06 | €258,82 | 17 | 17 | 41,18% | 1,58 | €15,22 | 3,39% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Ampia 4H | Confluenza trend | €10.206,43 | €167,06 | 54 | 54 | 33,33% | 1,13 | €3,09 | 4,45% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.161,66 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.130,56 | €132,30 | 51 | 51 | 43,14% | 1,10 | €2,59 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.090,56 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | Sol Ema 1H | Trend following EMA | €10.070,61 | €73,41 | 23 | 23 | 43,48% | 1,11 | €3,19 | 3,33% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.066,52 | €66,52 | 17 | 17 | 58,82% | 1,16 | €3,91 | 3,08% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €10.064,80 | €-294,31 | 139 | 139 | 39,57% | 0,91 | €-2,12 | 7,34% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €10.060,17 | €-270,31 | 101 | 101 | 32,67% | 0,90 | €-2,68 | 8,39% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.054,78 | €57,13 | 175 | 175 | 44,57% | 1,02 | €0,33 | 8,69% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.053,19 | €54,27 | 263 | 263 | 39,92% | 1,01 | €0,21 | 6,56% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €10.049,48 | €-280,65 | 96 | 96 | 35,42% | 0,89 | €-2,92 | 7,98% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.039,42 | €39,42 | 29 | 29 | 44,83% | 1,33 | €1,36 | 0,33% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
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
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.995,56 | €-360,55 | 142 | 142 | 45,07% | 0,87 | €-2,54 | 12,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,36 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.983,46 | €-12,56 | 221 | 221 | 43,44% | 1,00 | €-0,06 | 12,52% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.979,42 | €-20,58 | 15 | 15 | 60,00% | 0,94 | €-1,37 | 1,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.951,01 | €-38,22 | 124 | 124 | 41,94% | 0,99 | €-0,31 | 7,99% |
| TEST | Btc Ema 4H | Trend following EMA | €9.943,99 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.927,41 | €-72,59 | 29 | 29 | 44,83% | 0,56 | €-2,50 | 0,84% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.906,26 | €-163,52 | 53 | 53 | 47,17% | 0,88 | €-3,09 | 4,27% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.906,22 | €-435,35 | 81 | 81 | 32,10% | 0,82 | €-5,37 | 8,44% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.893,29 | €-102,20 | 145 | 145 | 47,59% | 0,97 | €-0,70 | 8,44% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.890,79 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.889,03 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.886,07 | €-111,88 | 166 | 166 | 45,18% | 0,96 | €-0,67 | 7,10% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.878,50 | €-446,01 | 132 | 132 | 44,70% | 0,85 | €-3,38 | 9,02% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.860,65 | €-505,26 | 192 | 192 | 40,10% | 0,87 | €-2,63 | 12,68% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.839,23 | €-159,49 | 137 | 130 | 40,88% | 0,95 | €-1,16 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.830,73 | €-520,02 | 156 | 156 | 40,38% | 0,85 | €-3,33 | 8,78% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.823,03 | €-176,07 | 143 | 143 | 44,76% | 0,95 | €-1,23 | 6,64% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.819,89 | €-180,01 | 16 | 16 | 43,75% | 0,68 | €-11,25 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.781,66 | €-287,24 | 53 | 53 | 43,40% | 0,79 | €-5,42 | 5,41% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.762,70 | €-249,98 | 18 | 18 | 38,89% | 0,59 | €-13,89 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Ema 1H | Trend following EMA | €9.726,53 | €-294,97 | 26 | 26 | 38,46% | 0,65 | €-11,35 | 4,80% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.719,02 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,60% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.717,32 | €-306,84 | 17 | 17 | 29,41% | 0,54 | €-18,05 | 3,74% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.711,84 | €-283,82 | 9 | 9 | 33,33% | 0,35 | €-31,54 | 4,16% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.700,72 | €-624,68 | 161 | 161 | 39,13% | 0,80 | €-3,88 | 15,68% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.653,74 | €-344,15 | 120 | 120 | 44,17% | 0,85 | €-2,87 | 9,26% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.647,46 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.557,95 | €-440,16 | 83 | 83 | 45,78% | 0,78 | €-5,30 | 6,28% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.552,88 | €-858,91 | 131 | 131 | 36,64% | 0,68 | €-6,56 | 14,10% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.552,51 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.539,07 | €-490,75 | 177 | 177 | 41,81% | 0,90 | €-2,77 | 15,64% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.514,97 | €-514,23 | 135 | 135 | 43,70% | 0,87 | €-3,81 | 15,94% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.498,89 | €-817,80 | 153 | 153 | 38,56% | 0,71 | €-5,35 | 12,31% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.476,95 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,60% |
| TEST | Btc Ema 1H | Trend following EMA | €9.463,59 | €-536,41 | 20 | 20 | 20,00% | 0,33 | €-26,82 | 5,46% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.451,40 | €-561,26 | 86 | 86 | 26,74% | 0,77 | €-6,53 | 11,41% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.382,00 | €-946,13 | 210 | 210 | 41,43% | 0,76 | €-4,51 | 15,45% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.376,04 | €-630,25 | 151 | 138 | 41,72% | 0,81 | €-4,17 | 11,82% |
| TEST | Combo Trend | Combo Trend | €9.374,47 | €-928,01 | 189 | 189 | 39,15% | 0,78 | €-4,91 | 14,08% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.374,18 | €-1.029,91 | 111 | 111 | 36,04% | 0,57 | €-9,28 | 14,10% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,88 | €-629,45 | 85 | 85 | 34,12% | 0,73 | €-7,41 | 7,96% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.367,56 | €-629,35 | 99 | 99 | 38,38% | 0,77 | €-6,36 | 11,79% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.362,76 | €-684,27 | 96 | 96 | 34,38% | 0,77 | €-7,13 | 10,13% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.326,37 | €-1.019,71 | 146 | 146 | 39,73% | 0,66 | €-6,98 | 12,43% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.177,18 | €-871,94 | 49 | 49 | 26,53% | 0,44 | €-17,79 | 12,23% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.117,85 | €-932,24 | 124 | 124 | 37,90% | 0,72 | €-7,52 | 13,91% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.009,68 | €-994,35 | 78 | 78 | 29,49% | 0,67 | €-12,75 | 13,60% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.005,94 | €-965,81 | 184 | 184 | 39,13% | 0,79 | €-5,25 | 17,41% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.985,97 | €-1.379,65 | 139 | 139 | 32,37% | 0,59 | €-9,93 | 19,11% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.903,47 | €-1.091,54 | 98 | 98 | 35,71% | 0,59 | €-11,14 | 16,19% |
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
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,20444 | 2,20444 | 2,11218 | 1,48065 | 2,38896 | €24,38 | €73,14 | €3,06 | €0,00 |
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
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,19323 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €30,49 |
| 1H Fast Score 6 75 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 80028,10242 | 79820,80000 | 79131,78767 | 53752,20879 | 81372,57454 | €18,39 | €55,17 | €0,62 | €-0,14 |
| 1H Fast Score 6 75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €127,25 | €381,75 | €45,81 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,19323 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €29,68 |
| 1H Fast Score 6 75 No Trend Up V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €126,82 | €380,47 | €45,66 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,25201 | 0,25201 | 0,22400 | 0,16927 | 0,29402 | €141,43 | €424,29 | €47,15 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €-0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €138,86 | €416,57 | €49,99 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09064 | 0,09051 | 0,08874 | 0,06088 | 0,09348 | €763,02 | €2.289,07 | €47,86 | €-3,24 |
| 1H Fast Long Btc 1 3 Cap75 V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,26226 | 0,24740 | 0,23610 | 0,17615 | 0,30151 | €11,39 | €34,18 | €3,41 | €-1,94 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 105,84416 | 105,82300 | 104,65871 | 71,09200 | 107,62235 | €1.471,82 | €4.415,46 | €49,45 | €-0,88 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,22344 | 2,22344 | 2,15077 | 1,49341 | 2,33246 | €23,87 | €71,62 | €2,34 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | DASH | LONG | Momentum / breakout | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 81,83087 | €15,93 | €47,79 | €2,45 | €-0,01 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V2 | NEAR | LONG | Momentum / breakout V2 | 60m | 3,0x | 2,22144 | 2,22144 | 2,14439 | 1,49207 | 2,33703 | €507,73 | €1.523,18 | €52,84 | €0,00 |
| Rapida 1H V2 | DASH | LONG | Momentum / breakout V2 | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 79,93186 | €343,06 | €1.029,17 | €52,65 | €-0,21 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 86,70099 | 86,64900 | 85,72994 | 58,23416 | 88,15757 | €1.566,97 | €4.700,91 | €52,65 | €-2,82 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €-0,00 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €125,88 | €377,63 | €45,32 | €0,00 |
| 1H Fast V3 Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,26573 | 0,24740 | 0,23696 | 0,17848 | 0,30889 | €133,17 | €399,50 | €43,26 | €-27,56 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22344 | 2,22344 | 2,15077 | 1,49341 | 2,33246 | €25,86 | €77,58 | €2,54 | €0,00 |
| 1H Fast V3 Nohigh V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,14073 | 2504,32000 | 2476,09435 | 1681,94786 | 2546,21029 | €91,13 | €273,39 | €3,06 | €0,02 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22144 | 2,22144 | 2,14439 | 1,49207 | 2,33703 | €9,64 | €28,92 | €1,00 | €0,00 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,14073 | 2504,32000 | 2476,09435 | 1681,94786 | 2546,21029 | €1.485,82 | €4.457,47 | €49,92 | €0,32 |
| 1H Fast V3 Long Only V1 | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 79,93186 | €22,01 | €66,04 | €3,38 | €-0,01 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €134,15 | €402,44 | €48,29 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22144 | 2,22144 | 2,14439 | 1,49207 | 2,33703 | €9,92 | €29,77 | €1,03 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,14073 | 2504,32000 | 2476,09435 | 1681,94786 | 2546,21029 | €1.535,98 | €4.607,93 | €51,61 | €0,33 |
| 1H Fast V3 No Esports Long Only V1 | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,23484 | 74,22000 | 70,43683 | 49,86107 | 79,93186 | €28,86 | €86,57 | €4,43 | €-0,02 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79820,80000 | 79131,78767 | 53752,20879 | 81372,57454 | €77,79 | €233,37 | €2,61 | €-0,60 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,20944 | 2,20944 | 2,14340 | 1,48401 | 2,30850 | €42,71 | €128,14 | €3,83 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,19389 | 0,19323 | 0,18384 | 0,13023 | 0,20896 | €315,97 | €947,90 | €49,13 | €-3,22 |
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
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €362,26 |
| Scanner Top5 Btc Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €30,68 | €61,37 | €7,36 | €-4,84 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €-0,01 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €364,76 |
| Scanner Top5 Btc Guard V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €30,96 | €61,93 | €7,43 | €-4,88 |
| Scanner Top5 Btc Guard V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €18,63 | €37,25 | €2,45 | €-0,01 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,22144 | 2,22144 | 2,12237 | 1,12183 | 2,43940 | €12,72 | €25,44 | €1,13 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19389 | 0,19323 | 0,18097 | 0,09791 | 0,22231 | €331,93 | €663,86 | €44,24 | €-2,26 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 7,86292 | €16,52 | €33,03 | €1,39 | €-0,48 |
| Scanner Top5 Btc Btc Le3 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €337,21 | €674,41 | €44,36 | €-0,13 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,93378 | 74,22000 | 70,72471 | 34,81156 | 79,16182 | €335,09 | €670,19 | €0,00 | €51,39 |
| Scanner Top5 Btc Btc 2 3 V1 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €188,32 | €376,64 | €45,20 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19327 | 0,19323 | 0,17837 | 0,09760 | 0,22605 | €297,63 | €595,27 | €45,89 | €-0,12 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €-0,01 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €356,28 |
| Scanner Top5 Btc Guard Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33949 | €30,24 | €60,49 | €7,26 | €-4,77 |
| Scanner Top5 Btc Guard Mfe V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €18,19 | €36,39 | €2,39 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,42902 | €14,83 | €29,66 | €1,25 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19389 | 0,19323 | 0,18097 | 0,09791 | 0,22231 | €349,38 | €698,77 | €46,57 | €-2,37 |
| Scanner Top5 Btc Guard Btc Le3 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 74,23484 | 74,22000 | 69,35168 | 37,48860 | 84,97780 | €18,90 | €37,80 | €2,49 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,93378 | 74,22000 | 70,72471 | 34,81156 | 79,16182 | €332,51 | €665,01 | €0,00 | €51,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €186,87 | €373,73 | €44,85 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,19327 | 0,19323 | 0,17837 | 0,09760 | 0,22605 | €295,71 | €591,42 | €45,59 | €-0,12 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €24,76 |
| Scanner Top5 Btc Runner25 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,76375 | 74,22000 | 70,64887 | 34,72569 | 82,94613 | €17,67 | €35,33 | €0,00 | €2,80 |
| Scanner Top5 Btc Runner25 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,20944 | 2,20944 | 2,12454 | 1,11577 | 2,46416 | €13,56 | €27,12 | €1,04 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01887 | 0,01799 | 0,01660 | 0,00953 | 0,02566 | €203,31 | €406,63 | €48,80 | €-18,92 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €-0,01 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €24,78 |
| Scanner Top5 Btc Tp3 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,76375 | 74,22000 | 70,64887 | 34,72569 | 82,94613 | €17,68 | €35,35 | €0,00 | €2,81 |
| Scanner Top5 Btc Tp3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,20944 | 2,20944 | 2,12454 | 1,11577 | 2,46416 | €13,57 | €27,13 | €1,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01887 | 0,01799 | 0,01660 | 0,00953 | 0,02566 | €203,43 | €406,87 | €48,82 | €-18,93 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €-0,01 |
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
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €382,54 |
| Combo Adaptive | DASH | LONG | Combo Adaptive | 60m | 2,0x | 68,77375 | 74,22000 | 71,35148 | 34,73074 | 77,16470 | €15,14 | €30,28 | €0,00 | €2,40 |
| Combo Adaptive | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €33,75 | €67,50 | €8,10 | €-3,83 |
| Combo Adaptive | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09110 | 0,09051 | 0,08904 | 0,04600 | 0,09522 | €15,70 | €31,39 | €0,71 | €-0,20 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €334,13 |
| Combo Adaptive Mfe Trail | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €28,33 | €56,67 | €6,80 | €-4,47 |
| Combo Adaptive Mfe Trail | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09110 | 0,09051 | 0,08904 | 0,04600 | 0,09522 | €12,72 | €25,45 | €0,58 | €-0,16 |
| Combo Adaptive Mfe Trail | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,09542 | 7,09400 | 6,78408 | 3,58319 | 7,71810 | €14,17 | €28,34 | €1,24 | €-0,01 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,41742 | €504,48 | €1.008,96 | €44,51 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,23245 | 2,23245 | 2,13521 | 1,12739 | 2,42693 | €554,11 | €1.108,22 | €48,27 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 66,61332 | 74,22000 | 70,42020 | 33,63973 | 77,04227 | €307,73 | €615,47 | €0,00 | €70,28 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €397,14 |
| Combo Adaptive Long Only V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 68,24365 | 74,22000 | 70,56985 | 34,46304 | 78,54894 | €14,55 | €29,11 | €0,00 | €2,55 |
| Combo Adaptive Long Only V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,33304 | €24,77 | €49,53 | €5,94 | €-3,91 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2504,14073 | 2504,32000 | 2468,08110 | 1264,59107 | 2576,25998 | €61,52 | €123,03 | €1,77 | €0,01 |
| Combo Adaptive Long Only V1 | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09110 | 0,09051 | 0,08904 | 0,04600 | 0,09522 | €17,12 | €34,23 | €0,77 | €-0,22 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 86,70099 | 86,64900 | 85,45250 | 43,78400 | 89,19798 | €25,35 | €50,70 | €0,73 | €-0,03 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,41742 | €45,81 | €91,62 | €4,04 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,23245 | 2,23245 | 2,13521 | 1,12739 | 2,42693 | €561,17 | €1.122,34 | €48,89 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 66,61332 | 74,22000 | 70,42020 | 33,63973 | 77,04227 | €311,65 | €623,31 | €0,00 | €71,18 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €342,16 |
| Combo Adaptive Runner25 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,36527 | €26,79 | €53,59 | €6,43 | €-4,23 |
| Combo Adaptive Runner25 V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 67,61352 | 74,22000 | 71,34596 | 34,14483 | 80,00838 | €387,84 | €775,69 | €0,00 | €75,79 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 8,10454 | €14,09 | €28,18 | €1,18 | €-0,41 |
| Combo Adaptive Runner25 V1 | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09053 | 0,09051 | 0,08848 | 0,04572 | 0,09668 | €59,13 | €118,27 | €2,68 | €-0,02 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €335,76 |
| Combo Adaptive Tp3 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26858 | 0,24740 | 0,23635 | 0,13563 | 0,36527 | €26,29 | €52,58 | €6,31 | €-4,15 |
| Combo Adaptive Tp3 V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 67,61352 | 74,22000 | 71,34596 | 34,14483 | 80,00838 | €380,59 | €761,18 | €0,00 | €74,37 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,19844 | 7,09400 | 6,89640 | 3,63521 | 8,10454 | €13,85 | €27,69 | €1,16 | €-0,40 |
| Combo Adaptive Tp3 V1 | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09053 | 0,09051 | 0,08848 | 0,04572 | 0,09668 | €58,03 | €116,06 | €2,63 | €-0,02 |
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
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,19323 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €350,32 |
| Combo Adaptive Side Regime Guard V1 | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09066 | 0,09051 | 0,08827 | 0,04578 | 0,09543 | €13,22 | €26,44 | €0,70 | €-0,04 |
| Combo Adaptive Side Regime Guard V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 68,77375 | 74,22000 | 71,35148 | 34,73074 | 77,16470 | €13,88 | €27,76 | €0,00 | €2,20 |
| Combo Adaptive Side Regime Guard V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €23,30 | €46,60 | €5,59 | €-2,64 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,92618 | 105,82300 | 104,40084 | 53,49272 | 108,97686 | €23,43 | €46,87 | €0,67 | €-0,05 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €354,25 |
| Master Adaptive Gb20 Be V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,41033 | €25,53 | €51,06 | €2,15 | €0,00 |
| Master Adaptive Gb20 Be V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,58 | €45,17 | €5,42 | €0,00 |
| Master Adaptive Gb20 Be V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €208,45 | €416,91 | €50,03 | €-23,63 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €353,87 |
| Master Adaptive Gb20 Partial V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22344 | 2,22344 | 2,13000 | 1,12284 | 2,41033 | €25,50 | €51,01 | €2,14 | €0,00 |
| Master Adaptive Gb20 Partial V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,56 | €45,12 | €5,41 | €0,00 |
| Master Adaptive Gb20 Partial V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23079 | 0,13244 | 0,32521 | €208,23 | €416,47 | €49,98 | €-23,60 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,19323 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €16,60 |
| Master Adaptive Gb20 Loss Cap V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,22144 | 2,14795 | 1,12183 | 2,41742 | €689,28 | €1.378,56 | €45,61 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26226 | 0,24740 | 0,23703 | 0,13244 | 0,32954 | €31,77 | €63,55 | €6,11 | €-3,60 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01854 | 0,01799 | 0,01639 | 0,01245 | 0,02176 | €147,26 | €441,78 | €51,15 | €-13,16 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79820,80000 | 79131,78767 | 53752,20879 | 81372,57454 | €20,36 | €61,08 | €0,68 | €-0,16 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01799 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €333,44 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2504,32000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,81 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,28046 | 2,28046 | 2,11906 | 1,53171 | 2,60325 | €9,22 | €27,66 | €1,96 | €0,00 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | USELESS | LONG | Confluenza trend | 240m | 3,0x | 0,26076 | 0,24740 | 0,22947 | 0,17515 | 0,32335 | €142,48 | €427,43 | €51,29 | €-21,90 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,19323 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €363,41 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,41420 | 1,42064 | 1,39158 | 0,71417 | 1,46398 | €20,70 | €41,41 | €0,66 | €0,19 |
| Combo Trend Side Regime Guard V1 | DASH | LONG | Combo Trend | 60m | 2,0x | 68,77375 | 74,22000 | 70,84555 | 34,73074 | 79,02935 | €61,86 | €123,73 | €0,00 | €9,80 |
| Combo Trend Side Regime Guard V1 | DOGE | LONG | Combo Trend | 60m | 2,0x | 0,09110 | 0,09051 | 0,08881 | 0,04600 | 0,09614 | €16,34 | €32,68 | €0,82 | €-0,21 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,09400 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €-0,21 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,19323 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €338,85 |
| 1H Balanced V3 Long Only V1 | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,19544 | 2,19544 | 2,10498 | 1,47460 | 2,37635 | €8,42 | €25,26 | €1,04 | €0,00 |
| 1H Balanced V3 Long Only V1 | DASH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 68,77375 | 74,22000 | 71,09852 | 46,19304 | 77,16470 | €35,89 | €107,67 | €0,00 | €8,53 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,81046 | 2504,32000 | 2466,76999 | 1681,05436 | 2574,89140 | €912,88 | €2.738,63 | €39,44 | €1,65 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 85,86049 | 86,64900 | 84,62409 | 57,66963 | 88,33327 | €29,28 | €87,83 | €1,26 | €0,81 |
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
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1162,87912 | €4,70 | 2,95 | TARGET |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1162,87912 | €4,70 | 2,95 | TARGET |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1134,72912 | €3,54 | 2,18 | TARGET |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1134,72912 | €5,60 | 2,18 | TARGET |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1134,72912 | €5,47 | 2,18 | TARGET |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1142,93676 | €5,36 | 2,17 | TARGET |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1142,93676 | €96,41 | 2,17 | TARGET |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1134,72912 | €95,27 | 2,18 | TARGET |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1134,72912 | €97,17 | 2,18 | TARGET |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-09-06T05:00:00+00:00 | 1134,72912 | €3,78 | 2,18 | TARGET |
| Scanner Top20 Long | DASH | LONG | 2026-09-06T05:00:00+00:00 | 75,86158 | €104,28 | 1,98 | TARGET |
| Scanner Top15 Long | DASH | LONG | 2026-09-06T05:00:00+00:00 | 75,86158 | €104,28 | 1,98 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
