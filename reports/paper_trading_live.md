# Paper trading automatico KuCoin

Generato: 2026-08-19T13:10:14+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-19T13:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-19T13:05:28+00:00 | 2026-08-19T13:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-19T12:45:00+00:00 | 2026-08-19T12:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-08-19T12:00:00+00:00 | 2026-08-19T12:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-08-19T08:00:00+00:00 | 2026-08-19T08:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend — Side × Regime Guard | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Regime Guard | XRP | 60m | LONG | 6,17 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Regime Guard | BTW | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Range Only | XRP | 60m | LONG | 6,17 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Range Only | ETH | 60m | LONG | 7,88 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Range Only | BTW | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Loss Cap 0,75R | SKHYNIX | 60m | LONG | 5,96 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Side × Regime Guard | XRP | 60m | LONG | 6,17 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Side × Regime Guard | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Side × Regime Guard | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | BTW | 60m | LONG | 8,25 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | SKHYNIX | 60m | LONG | 5,96 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | SKHYNIX | 60m | LONG | 5,96 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Eth Adaptive 1H | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Eth Bollinger 1H | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Eth Donchian 1H | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 1H | SOL | 60m | LONG | 5,57 | 5,00 | 0,00 | OPENED | 5,8 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Donchian 1H | SOL | 60m | LONG | 5,57 | 5,00 | 0,00 | OPENED | 5,8 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Long Only | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | SKHYNIX | 60m | LONG | 5,96 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | 60m | LONG | 5,96 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | 60m | LONG | 5,96 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | SOL | 60m | LONG | 5,57 | 5,00 | 0,00 | OPENED | 5,8 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | SOL | 60m | LONG | 5,57 | 5,00 | 0,00 | OPENED | 5,8 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | SOL | 60m | LONG | 5,57 | 5,00 | 0,00 | OPENED | 5,8 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — qualità completa + profit lock | XRP | 60m | LONG | 6,17 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | 60m | LONG | 6,17 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | 60m | LONG | 7,88 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long + no HIGH + score <7,5 | XRP | 60m | LONG | 6,17 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | XRP | 60m | LONG | 6,17 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | ETH | 60m | LONG | 7,88 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SNDK | 60m | LONG | 5,80 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ACE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOXL | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 6,51 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTW | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 5,32 | 6,00 | 0,68 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,08 | 6,00 | 0,92 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,34 | 6,00 | 1,66 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 3,33 | 6,00 | 2,67 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -2,90 | 6,00 | 3,10 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 1,69 | 6,00 | 4,31 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -0,65 | 6,00 | 5,35 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H — LONG senza Range High Vol | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | BTW | 60m | LONG | 8,25 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | BTW | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Quality7 | BTW | 60m | LONG | 8,25 | 7,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.621,57 | -3,78% | €-126,77 | €3.000,00 | -4,23% | 5 | 43 | 32,56% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 43 | 1646 | PRIME INDICAZIONI | 50 (mancano 7) |

- Trade del Principale 4H chiusi: **43**; win rate **32,56%**; profit factor **0,72**.
- Expectancy: **€-8,84** per trade; P&L netto: **€-380,23**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.621,57 | €1.270,72 | €3.812,15 | €192,21 | €0,38 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.570,38 | €3.888,62 | €7.777,24 | €157,85 | €-2,51 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.365,54 | €1.934,28 | €5.802,85 | €207,05 | €31,55 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.321,51 | €3.797,07 | €7.594,13 | €154,13 | €-2,45 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Cost Aware | 1 | €10.294,93 | €1.566,58 | €4.699,75 | €52,64 | €0,16 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.151,01 | €386,22 | €1.158,67 | €51,78 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 3 | €10.150,69 | €3.181,19 | €9.543,56 | €152,35 | €-1,91 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 2 | €10.117,06 | €1.664,00 | €4.991,99 | €101,21 | €-1,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.084,35 | €1.575,64 | €3.151,29 | €50,42 | €1,92 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.072,95 | €2.466,71 | €4.933,42 | €200,66 | €-41,76 |
| TEST | Ampia 4H | 7 | €10.061,21 | €1.684,90 | €3.369,80 | €202,02 | €-28,22 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €10.035,96 | €1.394,35 | €4.183,04 | €50,20 | €-0,84 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €10.035,68 | €4.914,99 | €9.829,97 | €200,72 | €-28,56 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 3 | €10.026,85 | €409,12 | €1.227,35 | €103,40 | €0,01 |
| TEST | Rapida V1 — score 6–7,5 | 1 | €10.009,44 | €1.575,03 | €4.725,08 | €52,92 | €0,00 |
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
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.991,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 3 | €9.989,66 | €1.642,70 | €4.928,09 | €103,01 | €0,15 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.986,13 | €1.156,05 | €3.468,16 | €49,94 | €0,12 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.971,32 | €1.298,67 | €3.896,00 | €49,87 | €0,13 |
| TEST | Sol Donchian 4H | 1 | €9.959,00 | €1.200,73 | €2.401,46 | €49,66 | €29,68 |
| TEST | Eth Bollinger 1H | 1 | €9.956,17 | €1.383,26 | €4.149,79 | €49,80 | €-0,83 |
| TEST | Sol Adaptive 4H | 1 | €9.954,04 | €1.100,38 | €2.200,75 | €49,64 | €27,20 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.945,29 | €1.295,52 | €2.591,05 | €49,75 | €-2,61 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 4 | €9.912,44 | €4.082,92 | €12.248,77 | €198,20 | €28,06 |
| TEST | Btc Ema 4H | 1 | €9.895,08 | €1.406,22 | €2.812,44 | €49,50 | €-2,84 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €9.872,53 | €1.285,89 | €3.857,66 | €49,38 | €-0,77 |
| TEST | Btc Ema 1H | 1 | €9.846,44 | €1.139,88 | €3.419,65 | €49,24 | €0,12 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 2 | €9.831,63 | €2.927,65 | €8.782,95 | €98,37 | €-1,76 |
| TEST | Btc Donchian 4H | 1 | €9.827,59 | €1.396,63 | €2.793,26 | €49,16 | €-2,82 |
| TEST | Sol Ema 4H | 1 | €9.820,14 | €1.183,99 | €2.367,98 | €48,96 | €29,26 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.809,59 | €1.902,37 | €3.804,75 | €48,94 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.807,41 | €1.129,69 | €3.389,07 | €0,00 | €49,59 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 3 | €9.801,95 | €4.378,88 | €13.136,65 | €147,13 | €-1,60 |
| TEST | FAST NoHigh <7,5 · SHORT only | 3 | €9.777,33 | €398,94 | €1.196,81 | €100,82 | €0,01 |
| TEST | Scanner Bottom10 Short | 2 | €9.771,86 | €1.858,06 | €3.716,13 | €49,06 | €0,00 |
| TEST | Scanner Bottom15 Short | 2 | €9.771,86 | €1.858,06 | €3.716,13 | €49,06 | €0,00 |
| TEST | Scanner Bottom20 Short | 2 | €9.771,86 | €1.858,06 | €3.716,13 | €49,06 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.763,59 | €3.472,94 | €10.418,83 | €144,09 | €27,71 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.759,64 | €1.271,18 | €3.813,55 | €48,81 | €-0,76 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 1 | €9.743,31 | €1.533,15 | €4.599,45 | €51,51 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 3 | €9.729,87 | €436,17 | €872,34 | €50,02 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 4 | €9.726,55 | €5.269,54 | €10.539,08 | €145,66 | €30,74 |
| TEST | Top 5 + BTC — BTC 2–3 | 1 | €9.725,07 | €209,35 | €418,71 | €49,71 | €-43,94 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.704,15 | €1.845,18 | €3.690,35 | €48,72 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.689,68 | €1.121,80 | €3.365,41 | €48,46 | €-0,67 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.689,39 | €1.842,37 | €3.684,74 | €48,65 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 1 | €9.666,98 | €1.494,66 | €4.483,99 | €50,22 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.662,69 | €1.512,09 | €3.024,18 | €48,39 | €-17,42 |
| TEST | Sol Adaptive 1H | 1 | €9.650,68 | €1.113,55 | €3.340,64 | €0,00 | €31,63 |
| TEST | Combo Mean Reversion | 1 | €9.647,37 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.614,83 | €1.828,19 | €3.656,39 | €48,28 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 3 | €9.607,49 | €430,68 | €861,36 | €49,39 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.590,38 | €1.105,17 | €3.315,52 | €0,00 | €43,96 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 2 | €9.516,45 | €1.806,65 | €3.613,30 | €47,93 | €8,82 |
| TEST | Rapida V1 — target pieno 2R | 3 | €9.513,38 | €1.695,00 | €5.085,01 | €100,60 | €0,15 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 4 | €9.507,29 | €333,84 | €1.001,51 | €100,09 | €-29,79 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.497,61 | €4.003,77 | €8.007,54 | €91,22 | €-1,52 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 5 | €9.490,69 | €2.311,11 | €4.622,22 | €142,62 | €-5,98 |
| TEST | Bilanciata 1H V2 | 5 | €9.480,50 | €1.519,31 | €4.557,94 | €143,55 | €15,94 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €9.478,87 | €3.702,88 | €7.405,75 | €143,20 | €8,26 |
| TEST | Combo Adaptive — Long Only | 5 | €9.449,96 | €3.659,88 | €7.319,77 | €141,62 | €-10,50 |
| TEST | Forza relativa 1H V2 | 4 | €9.446,49 | €622,54 | €1.245,09 | €96,48 | €-40,65 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €9.445,16 | €331,65 | €994,96 | €99,44 | €-29,60 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.442,04 | €3.034,14 | €9.102,43 | €140,49 | €-0,70 |
| TEST | Rapida V3 — no volatilità HIGH | 2 | €9.436,68 | €361,89 | €1.085,67 | €96,46 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 1 | €9.406,15 | €147,98 | €443,93 | €47,30 | €-29,45 |
| TEST | Combo Adaptive — Quality7 | 2 | €9.400,69 | €396,23 | €792,46 | €94,58 | €-42,13 |
| TEST | Top 5 + BTC — Guard | 5 | €9.375,51 | €2.283,06 | €4.566,12 | €140,89 | €-5,91 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.372,69 | €3.010,23 | €9.030,69 | €139,46 | €-0,69 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 5 | €9.366,77 | €3.707,11 | €7.414,23 | €186,54 | €83,15 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 5 | €9.356,81 | €3.703,17 | €7.406,34 | €186,34 | €83,06 |
| TEST | Master Adaptive No Alt V1 | 7 | €9.338,45 | €3.656,41 | €7.312,82 | €186,77 | €62,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 5 | €9.327,85 | €2.271,46 | €4.542,91 | €140,17 | €-5,88 |
| TEST | Master Adaptive V1 | 5 | €9.320,62 | €3.688,85 | €7.377,69 | €185,62 | €82,74 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.279,45 | €3.505,28 | €7.010,56 | €185,60 | €71,89 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €9.269,80 | €172,23 | €516,69 | €50,30 | €0,00 |
| TEST | Scanner Top10 Long | 7 | €9.262,28 | €2.293,27 | €4.586,54 | €182,66 | €-37,68 |
| TEST | Scanner Top15 Long | 7 | €9.262,28 | €2.293,27 | €4.586,54 | €182,66 | €-37,68 |
| TEST | Scanner Top20 Long | 7 | €9.262,28 | €2.293,27 | €4.586,54 | €182,66 | €-37,68 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.234,79 | €3.284,85 | €9.854,54 | €136,28 | €26,21 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.230,16 | €2.666,32 | €5.332,65 | €184,62 | €-13,12 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.196,78 | €3.639,83 | €7.279,67 | €183,15 | €81,64 |
| TEST | Combo Trend | 6 | €9.194,41 | €609,76 | €1.219,51 | €50,17 | €-17,20 |
| TEST | Bilanciata 1H V1 | 3 | €9.182,93 | €1.265,90 | €3.797,69 | €48,85 | €-26,40 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.164,90 | €1.529,06 | €4.587,18 | €183,57 | €-12,37 |
| TEST | Top 5 + BTC — Guard + MFE | 5 | €9.157,47 | €2.229,96 | €4.459,93 | €137,61 | €-5,77 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €9.140,12 | €4.044,77 | €8.089,54 | €136,83 | €48,29 |
| TEST | Combo Adaptive — parziale 1R | 2 | €9.138,13 | €1.734,83 | €3.469,65 | €46,02 | €8,47 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €9.134,77 | €4.042,40 | €8.084,81 | €136,75 | €48,26 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 6 | €9.113,73 | €5.952,41 | €11.904,82 | €182,28 | €185,99 |
| TEST | Combo Scanner | 4 | €9.093,05 | €3.547,37 | €7.094,75 | €136,54 | €8,08 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €9.058,03 | €3.525,97 | €7.051,94 | €135,94 | €7,90 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.028,23 | €1.454,19 | €2.908,37 | €3,83 | €3,64 |
| TEST | Master Adaptive Strict3 V1 | 5 | €8.988,68 | €3.385,41 | €6.770,81 | €179,13 | €5,03 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 1 | €8.955,68 | €140,89 | €422,67 | €45,04 | €-28,04 |
| TEST | Top 5 + BTC — solo MFE | 4 | €8.885,09 | €3.458,65 | €6.917,30 | €133,35 | €7,75 |
| TEST | Forza relativa 1H V1 | 2 | €8.802,41 | €1.530,35 | €3.060,70 | €45,90 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 1 | €8.466,89 | €1.412,29 | €2.824,57 | €0,00 | €26,75 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.621,57 | €-380,23 | 43 | 43 | 32,56% | 0,72 | €-8,84 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.570,38 | €578,49 | 66 | 66 | 46,97% | 1,36 | €8,77 | 3,63% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.365,54 | €334,47 | 24 | 24 | 45,83% | 1,59 | €13,94 | 2,40% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.321,51 | €329,43 | 34 | 34 | 44,12% | 1,45 | €9,69 | 3,63% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.294,93 | €297,88 | 76 | 76 | 47,37% | 1,16 | €3,92 | 4,41% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.151,01 | €151,70 | 36 | 36 | 47,22% | 1,14 | €4,21 | 3,33% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.150,69 | €158,33 | 37 | 37 | 43,24% | 1,18 | €4,28 | 3,97% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.117,06 | €121,06 | 60 | 60 | 43,33% | 1,09 | €2,02 | 5,24% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,35 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.072,95 | €116,81 | 82 | 82 | 41,46% | 1,06 | €1,42 | 8,85% |
| TEST | Ampia 4H | Confluenza trend | €10.061,21 | €88,49 | 39 | 39 | 25,64% | 1,09 | €2,27 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.035,96 | €39,30 | 6 | 6 | 50,00% | 1,24 | €6,55 | 1,89% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.035,68 | €61,73 | 51 | 51 | 47,06% | 1,06 | €1,21 | 2,94% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.026,85 | €27,83 | 119 | 119 | 43,70% | 1,01 | €0,23 | 7,10% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.009,44 | €-55,31 | 130 | 129 | 42,31% | 0,98 | €-0,43 | 6,80% |
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
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,28 | €-8,72 | 13 | 13 | 61,54% | 0,97 | €-0,67 | 2,10% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.989,66 | €-7,26 | 134 | 134 | 44,03% | 1,00 | €-0,05 | 4,46% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.986,13 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.971,32 | €-26,23 | 7 | 7 | 57,14% | 0,84 | €-3,75 | 1,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.959,00 | €-68,81 | 3 | 3 | 33,33% | 0,35 | €-22,94 | 1,05% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.956,17 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,94% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.954,04 | €-71,45 | 3 | 3 | 33,33% | 0,32 | €-23,82 | 1,01% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.945,29 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,96% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.912,44 | €-107,99 | 32 | 32 | 37,50% | 0,87 | €-3,37 | 3,56% |
| TEST | Btc Ema 4H | Trend following EMA | €9.895,08 | €-100,21 | 2 | 2 | 0,00% | 0,00 | €-50,11 | 1,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.872,53 | €-124,38 | 8 | 8 | 37,50% | 0,49 | €-15,55 | 2,77% |
| TEST | Btc Ema 1H | Trend following EMA | €9.846,44 | €-151,42 | 9 | 9 | 33,33% | 0,53 | €-16,82 | 1,94% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.831,63 | €-161,34 | 31 | 28 | 38,71% | 0,80 | €-5,20 | 3,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.827,59 | €-167,74 | 3 | 3 | 0,00% | 0,00 | €-55,91 | 2,43% |
| TEST | Sol Ema 4H | Trend following EMA | €9.820,14 | €-207,28 | 4 | 4 | 0,00% | 0,00 | €-51,82 | 2,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.809,59 | €-188,14 | 34 | 34 | 41,18% | 0,76 | €-5,53 | 3,91% |
| TEST | Sol Ema 1H | Trend following EMA | €9.807,41 | €-239,48 | 9 | 9 | 22,22% | 0,37 | €-26,61 | 3,33% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.801,95 | €-188,30 | 38 | 38 | 44,74% | 0,80 | €-4,96 | 4,50% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.777,33 | €-221,71 | 83 | 83 | 42,17% | 0,88 | €-2,67 | 7,10% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.771,86 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.771,86 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.771,86 | €-225,99 | 66 | 66 | 33,33% | 0,85 | €-3,42 | 5,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.763,59 | €-257,75 | 105 | 105 | 36,19% | 0,89 | €-2,45 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.759,64 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,63% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.743,31 | €-319,72 | 88 | 87 | 44,32% | 0,87 | €-3,63 | 7,13% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.729,87 | €-272,53 | 23 | 23 | 39,13% | 0,64 | €-11,85 | 4,21% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.726,55 | €-297,87 | 64 | 64 | 39,06% | 0,79 | €-4,65 | 8,68% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.725,07 | €-231,87 | 12 | 12 | 25,00% | 0,47 | €-19,32 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.704,15 | €-293,72 | 57 | 57 | 33,33% | 0,78 | €-5,15 | 5,27% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.689,68 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,14% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.689,39 | €-308,49 | 58 | 58 | 32,76% | 0,76 | €-5,32 | 5,27% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.666,98 | €-330,33 | 125 | 125 | 38,40% | 0,89 | €-2,64 | 8,81% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.662,69 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,57% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.650,68 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,59% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.647,37 | €-352,36 | 35 | 35 | 40,00% | 0,70 | €-10,07 | 5,48% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.614,83 | €-383,06 | 85 | 85 | 32,94% | 0,79 | €-4,51 | 6,41% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.607,49 | €-394,88 | 23 | 23 | 30,43% | 0,49 | €-17,17 | 5,41% |
| TEST | Eth Ema 1H | Trend following EMA | €9.590,38 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,80% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.516,45 | €-490,20 | 89 | 89 | 35,96% | 0,74 | €-5,51 | 7,91% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.513,38 | €-539,80 | 147 | 146 | 34,69% | 0,84 | €-3,67 | 6,56% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.507,29 | €-467,86 | 113 | 112 | 45,13% | 0,79 | €-4,14 | 8,63% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.497,61 | €-496,07 | 74 | 74 | 41,89% | 0,76 | €-6,70 | 7,21% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.490,69 | €-500,92 | 53 | 53 | 37,74% | 0,71 | €-9,45 | 7,74% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.480,50 | €-532,60 | 75 | 68 | 40,00% | 0,71 | €-7,10 | 8,30% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.478,87 | €-525,43 | 73 | 73 | 35,62% | 0,73 | €-7,20 | 11,27% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.449,96 | €-536,27 | 56 | 56 | 35,71% | 0,64 | €-9,58 | 6,25% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.446,49 | €-513,21 | 83 | 79 | 38,55% | 0,81 | €-6,18 | 9,47% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.445,16 | €-530,15 | 157 | 156 | 38,22% | 0,84 | €-3,38 | 8,61% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.442,04 | €-551,54 | 74 | 74 | 39,19% | 0,74 | €-7,45 | 6,59% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.436,68 | €-562,66 | 110 | 110 | 40,91% | 0,80 | €-5,12 | 6,91% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.406,15 | €-564,14 | 74 | 74 | 35,14% | 0,71 | €-7,62 | 9,40% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.400,69 | €-557,78 | 48 | 48 | 29,17% | 0,60 | €-11,62 | 7,77% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.375,51 | €-616,20 | 58 | 58 | 34,48% | 0,66 | €-10,62 | 7,34% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.372,69 | €-684,39 | 80 | 79 | 43,75% | 0,72 | €-8,55 | 7,69% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.366,77 | €-713,06 | 49 | 49 | 24,49% | 0,54 | €-14,55 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.356,81 | €-722,93 | 44 | 44 | 29,55% | 0,52 | €-16,43 | 7,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.338,45 | €-720,06 | 50 | 50 | 30,00% | 0,61 | €-14,40 | 7,26% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.327,85 | €-663,90 | 68 | 68 | 38,24% | 0,66 | €-9,76 | 7,02% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.320,62 | €-758,82 | 46 | 46 | 28,26% | 0,55 | €-16,50 | 7,80% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.279,45 | €-790,54 | 45 | 45 | 24,44% | 0,54 | €-17,57 | 8,18% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.269,80 | €-784,44 | 130 | 129 | 37,69% | 0,73 | €-6,03 | 8,41% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.262,28 | €-698,07 | 54 | 54 | 33,33% | 0,55 | €-12,93 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.262,28 | €-698,07 | 54 | 54 | 33,33% | 0,55 | €-12,93 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.262,28 | €-698,07 | 54 | 54 | 33,33% | 0,55 | €-12,93 | 10,31% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.234,79 | €-785,39 | 61 | 61 | 31,15% | 0,46 | €-12,88 | 8,85% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.230,16 | €-753,32 | 55 | 55 | 30,91% | 0,60 | €-13,70 | 7,96% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.196,78 | €-881,60 | 81 | 81 | 46,91% | 0,53 | €-10,88 | 9,02% |
| TEST | Combo Trend | Combo Trend | €9.194,41 | €-787,75 | 118 | 118 | 33,90% | 0,75 | €-6,68 | 10,02% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.182,93 | €-789,70 | 118 | 118 | 37,29% | 0,70 | €-6,69 | 13,69% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.164,90 | €-823,44 | 52 | 52 | 30,77% | 0,53 | €-15,84 | 9,26% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.157,47 | €-834,43 | 75 | 75 | 37,33% | 0,61 | €-11,13 | 8,78% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.140,12 | €-902,69 | 58 | 58 | 31,03% | 0,50 | €-15,56 | 11,78% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.138,13 | €-868,26 | 90 | 90 | 34,44% | 0,57 | €-9,65 | 8,69% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.134,77 | €-908,01 | 62 | 62 | 32,26% | 0,50 | €-14,65 | 12,06% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.113,73 | €-1.064,35 | 36 | 36 | 16,67% | 0,33 | €-29,57 | 11,41% |
| TEST | Combo Scanner | Combo Scanner | €9.093,05 | €-911,23 | 78 | 78 | 34,62% | 0,61 | €-11,68 | 11,38% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.058,03 | €-946,10 | 54 | 54 | 31,48% | 0,43 | €-17,52 | 11,72% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.028,23 | €-973,32 | 85 | 85 | 29,41% | 0,52 | €-11,45 | 10,49% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.988,68 | €-1.011,64 | 48 | 48 | 27,08% | 0,54 | €-21,08 | 11,51% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €8.955,68 | €-1.016,03 | 94 | 94 | 29,79% | 0,60 | €-10,81 | 11,36% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €8.885,09 | €-1.118,96 | 66 | 66 | 31,82% | 0,36 | €-16,95 | 12,28% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.802,41 | €-1.195,86 | 103 | 103 | 28,16% | 0,54 | €-11,61 | 13,90% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €8.466,89 | €-1.558,17 | 102 | 102 | 29,41% | 0,39 | €-15,28 | 15,36% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01050 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €-0,07 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | SOL | LONG | Confluenza trend | 240m | 3,0x | 77,23844 | 78,19300 | 75,78654 | 51,87849 | 80,14224 | €11,96 | €35,87 | €0,67 | €0,44 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,93 | €104,79 | €1,51 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06998 | 0,07054 | 0,07099 | 0,09295 | 0,06796 | €1.095,91 | €3.287,73 | €47,34 | €-26,40 |
| Bilanciata 1H — LONG senza Range High Vol | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BTC | LONG | Confluenza trend | 60m | 3,0x | 64764,77036 | 64767,00000 | 63832,15767 | 43500,33743 | 66629,99575 | €87,47 | €262,41 | €3,78 | €0,01 |
| Bilanciata 1H — LONG senza Range High Vol | ACE | LONG | Confluenza trend | 60m | 3,0x | 0,22764 | 0,20330 | 0,20039 | 0,15290 | 0,28213 | €126,17 | €378,51 | €45,31 | €-40,47 |
| Bilanciata 1H — LONG senza Range High Vol | ETH | LONG | Confluenza trend | 60m | 3,0x | 1915,38300 | 1932,74000 | 1887,80148 | 1286,49891 | 1970,54603 | €1.033,20 | €3.099,59 | €44,63 | €28,09 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | SUI | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,65261 | 0,65261 | 0,66201 | 0,86688 | 0,63381 | €26,68 | €80,03 | €1,15 | €-0,00 |
| Bilanciata 1H V2 | ETH | LONG | Confluenza trend V2 | 60m | 3,0x | 1923,41461 | 1932,74000 | 1895,71744 | 1291,89348 | 1978,80895 | €1.101,28 | €3.303,84 | €47,58 | €16,02 |
| Bilanciata 1H V2 | BTW | LONG | Confluenza trend V2 | 60m | 3,0x | 0,64030 | 0,64018 | 0,56347 | 0,43007 | 0,79398 | €127,59 | €382,78 | €45,93 | €-0,08 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 1,01050 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €-1,71 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.164,76 | €3.494,29 | €50,32 | €-0,00 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 64764,77036 | 64767,00000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.042,91 | €3.128,72 | €45,05 | €0,11 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1915,38300 | 1932,74000 | 1887,80148 | 1286,49891 | 1970,54603 | €1.078,24 | €3.234,71 | €46,58 | €29,31 |
| Rapida V1 — score 6–7,5 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.575,03 | €4.725,08 | €52,92 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.533,15 | €4.599,45 | €51,51 | €-0,00 |
| Rapida score 6–7,5 — Range Only | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.566,58 | €4.699,75 | €52,64 | €0,16 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €63,61 | €190,84 | €2,14 | €0,01 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.488,39 | €4.465,16 | €50,01 | €0,15 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1174,33482 | 1185,69000 | 1142,21538 | 788,76155 | 1222,51398 | €603,85 | €1.811,55 | €49,55 | €17,52 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,00789 | 1,01050 | 0,99660 | 0,67697 | 1,02482 | €1.460,53 | €4.381,58 | €49,07 | €11,34 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1688,96277 | 1687,95000 | 1636,32184 | 1134,41999 | 1767,92416 | €530,16 | €1.590,49 | €49,57 | €-0,95 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| Rapida V1 — senza PEPE | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| Rapida V1 — senza PEPE | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.477,62 | €4.432,85 | €49,65 | €0,15 |
| Rapida V1 — target pieno 2R | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €115,44 | €346,32 | €3,88 | €-0,00 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| Rapida V1 — target pieno 2R | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 66215,50122 | €1.432,32 | €4.296,97 | €48,13 | €0,15 |
| Rapida 1H V2 | ETH | LONG | Momentum / breakout V2 | 60m | 3,0x | 1933,12655 | 1932,74000 | 1911,47553 | 1298,41666 | 1965,60307 | €1.464,09 | €4.392,26 | €49,19 | €-0,88 |
| Rapida 1H V2 | XRP | LONG | Momentum / breakout V2 | 60m | 3,0x | 1,01070 | 1,01050 | 0,99938 | 0,67885 | 1,02768 | €1.463,56 | €4.390,69 | €49,18 | €-0,88 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,35 | €73,04 | €0,82 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21774 | 0,20330 | 0,19454 | 0,14625 | 0,25255 | €148,74 | €446,21 | €47,55 | €-29,60 |
| Rapida V3 — score <7,5 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.494,66 | €4.483,99 | €50,22 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| Rapida V3 — no volatilità HIGH | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| Rapida V3 — Long Only | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21774 | 0,20330 | 0,19454 | 0,14625 | 0,25255 | €140,89 | €422,67 | €45,04 | €-28,04 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.431,94 | €4.295,82 | €48,11 | €0,15 |
| Rapida V3 — Long + no HIGH + score <7,5 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01070 | 1,01050 | 0,99938 | 0,67885 | 1,02768 | €1.405,57 | €4.216,70 | €47,23 | €-0,84 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,35 | €55,04 | €0,62 | €-0,00 |
| Rapida V3 — senza ESPORTS | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| Rapida V3 senza ESPORTS — Long Only | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21774 | 0,20330 | 0,19454 | 0,14625 | 0,25255 | €147,98 | €443,93 | €47,30 | €-29,45 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,51 | €73,52 | €0,82 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21774 | 0,20330 | 0,19454 | 0,14625 | 0,25255 | €149,71 | €449,14 | €47,86 | €-29,79 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.460,07 | €4.380,22 | €49,06 | €0,15 |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1933,12655 | 1932,74000 | 1911,47553 | 1298,41666 | 1965,60307 | €1.459,67 | €4.379,00 | €49,04 | €-0,88 |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01070 | 1,01050 | 0,99938 | 0,67885 | 1,02768 | €1.459,14 | €4.377,43 | €49,03 | €-0,88 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| Rapida V3 — qualità completa + profit lock | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.419,52 | €4.258,55 | €47,70 | €0,15 |
| Rapida V3 — qualità completa + profit lock | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01070 | 1,01050 | 0,99938 | 0,67885 | 1,02768 | €1.395,24 | €4.185,73 | €46,88 | €-0,84 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,01050 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €-0,05 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,07054 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-1,05 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,65521 | 0,65521 | 0,67955 | 0,97953 | 0,58704 | €31,61 | €63,21 | €2,35 | €-0,00 |
| Ampia 4H | ACE | LONG | Confluenza trend | 240m | 2,0x | 0,21774 | 0,20330 | 0,19161 | 0,10996 | 0,29091 | €210,44 | €420,89 | €50,51 | €-27,92 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1916,70326 | 1932,74000 | 1876,83584 | 967,93515 | 2028,33206 | €47,80 | €95,59 | €1,99 | €0,80 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,49 | €-0,00 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,65491 | 0,65491 | 0,66473 | 0,97909 | 0,63329 | €1.513,47 | €3.026,93 | €45,42 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ACE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,22714 | 0,20330 | 0,20017 | 0,11470 | 0,28646 | €202,95 | €405,90 | €48,19 | €-42,60 |
| Forza relativa 1H V2 | SUI | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,65001 | 0,65001 | 0,65937 | 0,97176 | 0,62942 | €20,45 | €40,91 | €0,59 | €-0,00 |
| Forza relativa 1H V2 | BTW | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,63707 | 0,64018 | 0,56062 | 0,32172 | 0,80525 | €198,76 | €397,53 | €47,70 | €1,94 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €0,00 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 64764,77036 | 64767,00000 | 63728,53404 | 32706,20903 | 67355,36118 | €59,87 | €119,74 | €1,92 | €0,00 |
| Benchmark Donchian breakout 1H | BTW | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,66024 | 0,64018 | 0,58556 | 0,33342 | 0,84694 | €234,57 | €469,14 | €53,06 | €-14,26 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1185,69000 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €12,40 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 78,20864 | 78,19300 | 76,95730 | 39,49536 | 81,33698 | €1.648,59 | €3.297,18 | €52,75 | €-0,66 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €0,00 | €-0,00 |
| Donchian 1H Gb20 120R V1 | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 64764,77036 | 64767,00000 | 63728,53404 | 32706,20903 | 67355,36118 | €58,46 | €116,93 | €1,87 | €0,00 |
| Donchian 1H Gb20 120R V1 | BTW | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,66024 | 0,64018 | 0,58556 | 0,33342 | 0,84694 | €229,05 | €458,10 | €51,82 | €-13,92 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1185,69000 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €12,11 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 78,20864 | 78,19300 | 76,95730 | 39,49536 | 81,33698 | €1.609,77 | €3.219,55 | €51,51 | €-0,64 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark Bollinger mean reversion 1H | SOL | SHORT | Bollinger mean reversion | 60m | 2,0x | 78,17736 | 78,19300 | 79,11549 | 116,87516 | 76,77017 | €1.900,74 | €3.801,48 | €45,62 | €-0,76 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1932,35345 | 1932,74000 | 1955,54169 | 2888,86841 | 1897,57109 | €1.900,13 | €3.800,26 | €45,60 | €-0,76 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07054 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €-0,27 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 1,01050 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €-0,66 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 1911,30218 | 1932,74000 | 1880,72135 | 965,20760 | 1978,58002 | €44,44 | €88,89 | €1,42 | €1,00 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €21,92 | €43,84 | €0,72 | €-0,00 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 76,97239 | 78,19300 | 77,63795 | 38,87106 | 79,68182 | €112,49 | €224,99 | €0,00 | €3,57 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | BTC | LONG | Scanner Top 5 Long | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.762,47 | €3.524,93 | €50,76 | €0,12 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1914,76288 | 1932,74000 | 1887,19029 | 966,95525 | 1969,90805 | €57,06 | €114,13 | €1,64 | €1,07 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,28489 | €28,12 | €56,23 | €0,00 | €0,82 |
| Scanner Top 5 Long 1H | ACE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28044 | €213,82 | €427,63 | €50,99 | €-43,69 |
| Scanner Top 5 Long 1H | BTW | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €201,21 | €402,43 | €48,29 | €-0,08 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.627,25 | €3.254,49 | €48,28 | €-0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 1911,30218 | 1932,74000 | 1921,51422 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,00 | €0,76 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €0,11 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,28489 | €55,73 | €111,47 | €0,00 | €1,63 |
| Scanner Top10 Long | ACE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-40,21 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,00789 | 1,01050 | 0,99338 | 0,50899 | 1,03692 | €18,34 | €36,68 | €0,53 | €0,09 |
| Scanner Top10 Long | BTW | LONG | Scanner Top10 Long | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €181,13 | €362,25 | €43,47 | €-0,07 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 1911,30218 | 1932,74000 | 1921,51422 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,00 | €0,76 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €0,11 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,28489 | €55,73 | €111,47 | €0,00 | €1,63 |
| Scanner Top15 Long | ACE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-40,21 |
| Scanner Top15 Long | XRP | LONG | Scanner Top15 Long | 60m | 2,0x | 1,00789 | 1,01050 | 0,99338 | 0,50899 | 1,03692 | €18,34 | €36,68 | €0,53 | €0,09 |
| Scanner Top15 Long | BTW | LONG | Scanner Top15 Long | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €181,13 | €362,25 | €43,47 | €-0,07 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 1911,30218 | 1932,74000 | 1921,51422 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,00 | €0,76 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €0,11 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,28489 | €55,73 | €111,47 | €0,00 | €1,63 |
| Scanner Top20 Long | ACE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-40,21 |
| Scanner Top20 Long | XRP | LONG | Scanner Top20 Long | 60m | 2,0x | 1,00789 | 1,01050 | 0,99338 | 0,50899 | 1,03692 | €18,34 | €36,68 | €0,53 | €0,09 |
| Scanner Top20 Long | BTW | LONG | Scanner Top20 Long | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €181,13 | €362,25 | €43,47 | €-0,07 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.610,50 | €3.221,00 | €0,00 | €47,13 |
| Scanner Top 5 + forza BTC 1H | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €199,35 | €398,70 | €47,54 | €-40,74 |
| Scanner Top 5 + forza BTC 1H | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €232,11 | €464,22 | €47,26 | €-14,11 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €1.647,84 | €3.295,67 | €47,46 | €15,98 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1185,92714 | 1185,69000 | 1143,43457 | 598,89320 | 1279,41076 | €13,08 | €26,16 | €0,94 | €-0,01 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.509,61 | €3.019,22 | €0,00 | €44,18 |
| Top 5 + BTC — solo MFE | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €186,86 | €373,72 | €44,57 | €-38,18 |
| Top 5 + BTC — solo MFE | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €217,57 | €435,14 | €44,30 | €-13,22 |
| Top 5 + BTC — solo MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €1.544,61 | €3.089,22 | €44,48 | €14,98 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Top 5 + BTC — Guard | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.636,11 | €3.272,21 | €0,00 | €47,88 |
| Top 5 + BTC — Guard | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €197,83 | €395,66 | €47,18 | €-40,43 |
| Top 5 + BTC — Guard | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €224,35 | €448,70 | €45,68 | €-13,63 |
| Top 5 + BTC — Guard | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €28,01 | €56,01 | €0,81 | €0,27 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.538,99 | €3.077,99 | €0,00 | €45,04 |
| Top 5 + BTC — BTC≤3 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €190,50 | €381,00 | €45,43 | €-38,93 |
| Top 5 + BTC — BTC≤3 | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €221,80 | €443,61 | €45,16 | €-13,48 |
| Top 5 + BTC — BTC≤3 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €1.574,67 | €3.149,35 | €45,35 | €15,27 |
| Top 5 + BTC — BTC 2–3 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22714 | 0,20330 | 0,20017 | 0,11470 | 0,28646 | €209,35 | €418,71 | €49,71 | €-43,94 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.598,05 | €3.196,11 | €0,00 | €46,76 |
| Top 5 + BTC — Guard + MFE | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €193,23 | €386,45 | €46,08 | €-39,49 |
| Top 5 + BTC — Guard + MFE | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €219,13 | €438,26 | €44,61 | €-13,32 |
| Top 5 + BTC — Guard + MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €27,36 | €54,71 | €0,79 | €0,27 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.656,20 | €3.312,41 | €0,00 | €48,47 |
| Top 5 + BTC — Guard + BTC≤3 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €200,26 | €400,52 | €47,76 | €-40,92 |
| Top 5 + BTC — Guard + BTC≤3 | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €227,10 | €454,21 | €46,24 | €-13,80 |
| Top 5 + BTC — Guard + BTC≤3 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €28,35 | €56,70 | €0,82 | €0,27 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.627,79 | €3.255,58 | €0,00 | €47,63 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €196,82 | €393,65 | €46,94 | €-40,22 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €223,21 | €446,42 | €45,44 | €-13,57 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €27,86 | €55,73 | €0,80 | €0,27 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 80,39464 | €1.595,98 | €3.191,96 | €0,00 | €46,70 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,86187 | €223,61 | €447,23 | €45,53 | €-13,59 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 2006,50612 | €1.588,02 | €3.176,05 | €45,74 | €15,40 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1185,92714 | 1185,69000 | 1143,43457 | 598,89320 | 1313,40482 | €634,79 | €1.269,58 | €45,49 | €-0,25 |
| Top 5 + BTC — target pieno 3R | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 80,39464 | €1.596,91 | €3.193,82 | €0,00 | €46,73 |
| Top 5 + BTC — target pieno 3R | BTW | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,86187 | €223,74 | €447,49 | €45,55 | €-13,60 |
| Top 5 + BTC — target pieno 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 2006,50612 | €1.588,95 | €3.177,91 | €45,76 | €15,41 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1185,92714 | 1185,69000 | 1143,43457 | 598,89320 | 1313,40482 | €635,16 | €1.270,32 | €45,52 | €-0,25 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07054 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €-17,42 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07054 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €-0,34 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €118,87 | €237,73 | €3,80 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | BTC | LONG | Combo Trend | 60m | 2,0x | 64764,77036 | 64767,00000 | 63728,53404 | 32706,20903 | 67044,49028 | €47,89 | €95,77 | €1,53 | €0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €29,12 | €58,23 | €0,96 | €-0,00 |
| Combo Trend | BTW | LONG | Combo Trend | 60m | 2,0x | 0,66973 | 0,64018 | 0,59446 | 0,33821 | 0,83531 | €191,09 | €382,17 | €42,95 | €-16,86 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 77,06541 | 78,19300 | 77,63817 | 38,91803 | 79,50684 | €1.552,40 | €3.104,81 | €0,00 | €45,43 |
| Combo Scanner | ACE | LONG | Combo Scanner | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28584 | €191,56 | €383,13 | €45,69 | €-39,15 |
| Combo Scanner | BTW | LONG | Combo Scanner | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,80810 | €222,66 | €445,31 | €45,33 | €-13,53 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 1923,41461 | 1932,74000 | 1895,71744 | 971,32438 | 1984,34838 | €1.580,75 | €3.161,50 | €45,53 | €15,33 |
| Combo Adaptive — madre | BTW | LONG | Combo Adaptive | 60m | 2,0x | 0,66973 | 0,64018 | 0,60199 | 0,33821 | 0,80520 | €236,94 | €473,88 | €47,93 | €-20,91 |
| Combo Adaptive — madre | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,45949 | 78,19300 | 77,69801 | 39,11704 | 79,69032 | €1.569,71 | €3.139,42 | €0,00 | €29,73 |
| Combo Adaptive — MFE Trail esistente | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,45949 | 78,19300 | 77,73834 | 39,11704 | 79,69032 | €1.412,29 | €2.824,57 | €0,00 | €26,75 |
| Combo Adaptive — Quality7 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,22714 | 0,20330 | 0,20017 | 0,11470 | 0,28107 | €200,38 | €400,75 | €47,58 | €-42,06 |
| Combo Adaptive — Quality7 | BTW | LONG | Combo Adaptive | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €195,85 | €391,71 | €47,01 | €-0,08 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive — Trend/Transition | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,65421 | 0,65421 | 0,66363 | 0,97804 | 0,63537 | €1.699,46 | €3.398,92 | €48,94 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive — Quality7 + Regime | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive — Long Only | BTC | LONG | Combo Adaptive | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €18,79 | €37,57 | €0,54 | €0,00 |
| Combo Adaptive — Long Only | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28044 | €200,54 | €401,09 | €47,83 | €-40,98 |
| Combo Adaptive — Long Only | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,45949 | 78,19300 | 77,69801 | 39,11704 | 79,69032 | €1.647,05 | €3.294,10 | €0,00 | €31,19 |
| Combo Adaptive — Long Only | BTW | LONG | Combo Adaptive | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €196,93 | €393,87 | €47,26 | €-0,08 |
| Combo Adaptive — Long Only | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1933,12655 | 1932,74000 | 1905,28953 | 976,22891 | 1988,80059 | €1.596,57 | €3.193,14 | €45,98 | €-0,64 |
| Combo Adaptive — parziale 1R | BTW | LONG | Combo Adaptive | 60m | 2,0x | 0,66973 | 0,64018 | 0,60199 | 0,33821 | 0,80520 | €227,52 | €455,04 | €46,02 | €-20,08 |
| Combo Adaptive — parziale 1R | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,45949 | 78,19300 | 77,69801 | 39,11704 | 79,69032 | €1.507,31 | €3.014,61 | €0,00 | €28,55 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64764,77036 | 64767,00000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.139,88 | €3.419,65 | €49,24 | €0,12 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 64832,38388 | 64767,00000 | 63691,33393 | 32740,35386 | 67685,00877 | €1.406,22 | €2.812,44 | €49,50 | €-2,84 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 64764,77036 | 64767,00000 | 63935,78130 | 43500,33743 | 66422,74849 | €1.298,67 | €3.896,00 | €49,87 | €0,13 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 64832,38388 | 64767,00000 | 63691,33393 | 32740,35386 | 68027,32376 | €1.396,63 | €2.793,26 | €49,16 | €-2,82 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 64806,45612 | 64767,00000 | 65843,35941 | 96885,65189 | 62940,03018 | €1.575,64 | €3.151,29 | €50,42 | €1,92 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 64764,77036 | 64767,00000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.156,05 | €3.468,16 | €49,94 | €0,12 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 64832,38388 | 64767,00000 | 63587,60211 | 32740,35386 | 67944,33831 | €1.295,52 | €2.591,05 | €49,75 | €-2,61 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,06541 | 78,19300 | 77,71743 | 51,76227 | 79,28489 | €1.129,69 | €3.389,07 | €0,00 | €49,59 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 77,23844 | 78,19300 | 75,64136 | 39,00541 | 81,23117 | €1.183,99 | €2.367,98 | €48,96 | €29,26 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 78,20864 | 78,19300 | 77,20757 | 52,53014 | 80,21078 | €1.285,89 | €3.857,66 | €49,38 | €-0,77 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 77,23844 | 78,19300 | 75,64136 | 39,00541 | 81,71030 | €1.200,73 | €2.401,46 | €49,66 | €29,68 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 78,17736 | 78,19300 | 79,11549 | 103,84560 | 76,77017 | €1.394,35 | €4.183,04 | €50,20 | €-0,84 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,45949 | 78,19300 | 77,73608 | 52,02696 | 79,69032 | €1.113,55 | €3.340,64 | €0,00 | €31,63 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 77,23844 | 78,19300 | 75,49616 | 39,00541 | 81,59414 | €1.100,38 | €2.200,75 | €49,64 | €27,20 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1907,45141 | 1932,74000 | 1922,43204 | 1281,17153 | 1962,38601 | €1.105,17 | €3.315,52 | €0,00 | €43,96 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1933,12655 | 1932,74000 | 1908,38253 | 1298,41666 | 1982,61459 | €1.271,18 | €3.813,55 | €48,81 | €-0,76 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1932,35345 | 1932,74000 | 1955,54169 | 2566,80950 | 1897,57109 | €1.383,26 | €4.149,79 | €49,80 | €-0,83 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1933,12655 | 1932,74000 | 1905,28953 | 1298,41666 | 1988,80059 | €1.121,80 | €3.365,41 | €48,46 | €-0,67 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1932,74000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €1,49 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €64,51 |
| Master Adaptive V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,20330 | 0,18931 | 0,10864 | 0,26676 | €194,21 | €388,43 | €46,61 | €-21,36 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 78,19300 | 75,85610 | 38,86702 | 79,18096 | €1.611,05 | €3.222,10 | €46,40 | €51,44 |
| Master Adaptive V1 | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,79466 | €219,45 | €438,91 | €44,68 | €-13,34 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1932,74000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,85 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €65,26 |
| Master Adaptive No Alt V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22644 | 0,20330 | 0,19943 | 0,11435 | 0,28044 | €194,09 | €388,18 | €46,29 | €-39,66 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 78,19300 | 75,85610 | 38,86702 | 79,18096 | €1.548,55 | €3.097,10 | €44,60 | €49,44 |
| Master Adaptive No Alt V1 | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,79466 | €228,41 | €456,83 | €46,50 | €-13,88 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1185,92714 | 1185,69000 | 1143,43457 | 598,89320 | 1270,91228 | €15,39 | €30,77 | €1,10 | €-0,01 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,07600 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €7,81 |
| Master Adaptive Strict3 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.579,70 | €3.159,40 | €45,50 | €0,11 |
| Master Adaptive Strict3 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22714 | 0,20330 | 0,20017 | 0,11470 | 0,28107 | €22,04 | €44,08 | €5,23 | €-4,63 |
| Master Adaptive Strict3 V1 | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,63707 | 0,64018 | 0,56062 | 0,32172 | 0,78996 | €177,86 | €355,71 | €42,69 | €1,74 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1932,74000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €0,48 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 64764,77036 | 64767,00000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.591,99 | €3.183,97 | €45,85 | €0,11 |
| Master Adaptive Expanded V1 | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,79466 | €226,79 | €453,57 | €46,17 | €-13,78 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 77,45949 | 78,19300 | 76,34407 | 39,11704 | 79,69032 | €17,12 | €34,25 | €0,49 | €0,32 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1185,92714 | 1185,69000 | 1143,43457 | 598,89320 | 1270,91228 | €617,77 | €1.235,55 | €44,27 | €-0,25 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1932,74000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €1,47 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €63,65 |
| Master Adaptive Gb20 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,20330 | 0,18931 | 0,10864 | 0,26676 | €191,63 | €383,27 | €45,99 | €-21,07 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 78,19300 | 75,85610 | 38,86702 | 79,18096 | €1.589,64 | €3.179,29 | €45,78 | €50,75 |
| Master Adaptive Gb20 V1 | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,79466 | €216,54 | €433,07 | €44,09 | €-13,16 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,07600 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €8,13 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €63,83 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,87081 | €188,10 | €376,20 | €45,14 | €-0,08 |
| Combo Adaptive — Side × Regime Guard | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,45949 | 78,19300 | 77,69801 | 39,11704 | 79,69032 | €1.698,72 | €3.397,44 | €0,00 | €32,17 |
| Combo Adaptive — Side × Regime Guard | BTW | LONG | Combo Adaptive | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,79398 | €202,76 | €405,51 | €48,66 | €-0,08 |
| Combo Adaptive — Side × Regime Guard | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1933,12655 | 1932,74000 | 1905,28953 | 976,22891 | 1988,80059 | €1.689,57 | €3.379,14 | €48,66 | €-0,68 |
| Combo Adaptive — Side × Regime Guard | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,01070 | 1,01050 | 0,99615 | 0,51040 | 1,03981 | €1.678,49 | €3.356,98 | €48,34 | €-0,67 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1932,74000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €1,50 |
| Master Adaptive GB20 — Breakeven 0,5R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €64,83 |
| Master Adaptive GB20 — Breakeven 0,5R | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,20330 | 0,18931 | 0,10864 | 0,26676 | €195,18 | €390,35 | €46,84 | €-21,46 |
| Master Adaptive GB20 — Breakeven 0,5R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 78,19300 | 75,85610 | 38,86702 | 79,18096 | €1.619,03 | €3.238,05 | €46,63 | €51,69 |
| Master Adaptive GB20 — Breakeven 0,5R | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,79466 | €220,54 | €441,08 | €44,90 | €-13,40 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1932,74000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €1,50 |
| Master Adaptive GB20 — 50% a 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €64,76 |
| Master Adaptive GB20 — 50% a 0,75R | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,20330 | 0,18931 | 0,10864 | 0,26676 | €194,97 | €389,94 | €46,79 | €-21,44 |
| Master Adaptive GB20 — 50% a 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 78,19300 | 75,85610 | 38,86702 | 79,18096 | €1.617,31 | €3.234,61 | €46,58 | €51,64 |
| Master Adaptive GB20 — 50% a 0,75R | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,59303 | 0,33342 | 0,79466 | €220,31 | €440,61 | €44,85 | €-13,39 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1932,74000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €57,35 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64767,00000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €72,62 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 78,19300 | 76,13317 | 38,86702 | 79,18096 | €1.799,28 | €3.598,56 | €38,86 | €57,45 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTW | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,66024 | 0,64018 | 0,60983 | 0,33342 | 0,79466 | €21,57 | €43,15 | €3,29 | €-1,31 |
| Master Adaptive GB20 — Loss Cap 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1185,92714 | 1185,69000 | 1154,05771 | 598,89320 | 1270,91228 | €293,81 | €587,62 | €15,79 | €-0,12 |
| Rapida V3 NoHigh — Range Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,64030 | 0,64018 | 0,57192 | 0,43007 | 0,74288 | €158,53 | €475,58 | €50,79 | €-0,10 |
| Rapida V3 NoHigh — Range Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1933,12655 | 1932,74000 | 1911,47553 | 1298,41666 | 1965,60307 | €1.511,60 | €4.534,80 | €50,79 | €-0,91 |
| Rapida V3 NoHigh — Range Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01070 | 1,01050 | 0,99938 | 0,67885 | 1,02768 | €1.511,06 | €4.533,18 | €50,77 | €-0,91 |
| Rapida V3 NoHigh — Regime Guard | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,64030 | 0,64018 | 0,57192 | 0,43007 | 0,74288 | €157,95 | €473,84 | €50,61 | €-0,09 |
| Rapida V3 NoHigh — Regime Guard | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01070 | 1,01050 | 0,99938 | 0,67885 | 1,02768 | €1.506,05 | €4.518,16 | €50,60 | €-0,90 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01050 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €-0,07 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 59,42488 | 59,07600 | 57,77054 | 39,91371 | 62,73356 | €20,16 | €60,47 | €1,68 | €-0,36 |
| MAIN — Side × Regime Guard | SOL | LONG | Confluenza trend | 240m | 3,0x | 77,23844 | 78,19300 | 75,78654 | 51,87849 | 80,14224 | €862,59 | €2.587,77 | €48,64 | €31,98 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07054 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-39,43 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,01050 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €-18,81 |
| Combo Trend — Side × Regime Guard | SOL | LONG | Combo Trend | 60m | 2,0x | 77,45949 | 78,19300 | 76,22014 | 39,11704 | 80,18606 | €1.571,08 | €3.142,16 | €50,27 | €29,76 |
| Combo Trend — Side × Regime Guard | BTW | LONG | Combo Trend | 60m | 2,0x | 0,64030 | 0,64018 | 0,56347 | 0,32335 | 0,80934 | €208,85 | €417,70 | €50,12 | €-0,08 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64767,00000 | 64039,40494 | 43500,33743 | 65852,81851 | €62,03 | €186,09 | €2,08 | €0,01 |
| Bilanciata V3 · LONG only | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 1,01050 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €-1,61 |
| Bilanciata V3 · LONG only | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.101,68 | €3.305,04 | €47,59 | €-0,00 |
| Bilanciata V3 · LONG only | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | BTC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 64764,77036 | 64767,00000 | 63832,15767 | 43500,33743 | 66629,99575 | €986,42 | €2.959,27 | €42,61 | €0,10 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1915,38300 | 1932,74000 | 1887,80148 | 1286,49891 | 1970,54603 | €1.019,84 | €3.059,52 | €44,06 | €27,73 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.639,87 | €3.279,73 | €48,65 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.642,36 | €3.284,73 | €48,72 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | 2026-08-19T13:06:40+00:00 | 135,16213 | €-66,92 | -1,38 | STOP_GAP_STRESS |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | 2026-08-19T13:06:40+00:00 | 0,07074 | €-53,46 | -1,10 | STOP |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | 2026-08-19T13:06:40+00:00 | 135,16213 | €-66,82 | -1,38 | STOP_GAP_STRESS |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | 2026-08-19T13:06:40+00:00 | 0,07074 | €-53,38 | -1,10 | STOP |
| FAST NoHigh <7,5 · SHORT only | SOXL | SHORT | 2026-08-19T13:06:40+00:00 | 135,16213 | €-81,69 | -1,64 | STOP_GAP_STRESS |
| Combo Trend — Side × Regime Guard | ACE | LONG | 2026-08-19T13:06:40+00:00 | 0,20646 | €-63,30 | -1,25 | STOP_GAP_STRESS |
| MAIN — Dynamic Asset Selector | ACE | LONG | 2026-08-19T13:06:40+00:00 | 0,20646 | €-16,95 | -0,33 | STOP_GAP_STRESS |
| Rapida V3 NoHigh — Regime Guard | ACE | LONG | 2026-08-19T13:06:40+00:00 | 0,20646 | €-60,10 | -1,18 | STOP_GAP_STRESS |
| Rapida V3 NoHigh — Regime Guard | ETH | LONG | 2026-08-19T13:06:40+00:00 | 1934,37041 | €68,96 | 1,36 | TARGET |
| Rapida V3 NoHigh — Range Only | ACE | LONG | 2026-08-19T13:06:40+00:00 | 0,20646 | €-60,54 | -1,18 | STOP_GAP_STRESS |
| Master Adaptive GB20 — Loss Cap 0,75R | ACE | LONG | 2026-08-19T13:06:40+00:00 | 0,20531 | €-14,45 | -1,06 | STOP_STRESS_SLIPPAGE |
| Combo Adaptive — Side × Regime Guard | ACE | LONG | 2026-08-19T13:06:40+00:00 | 0,20646 | €-61,30 | -1,25 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 399/30 | 33/30 | 0,69 | 2,04 | -0,16R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 366/30 | 20/30 | 0,61 | 1,90 | -0,21R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 218/30 | 22/30 | 0,77 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 220/30 | 22/30 | 0,74 | 1,57 | -0,13R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 309/30 | 31/30 | 0,80 | 0,62 | -0,10R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 278/30 | 11/30 | 0,70 | 0,00 | -0,15R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 125/30 | 8/30 | 0,65 | 1,02 | -0,18R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 280/30 | 17/30 | 0,59 | 4,50 | -0,24R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 440/30 | 24/30 | 0,68 | 0,64 | -0,17R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 402/30 | 7/30 | 0,58 | 0,02 | -0,22R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 309/30 | 30/30 | 0,84 | 1,02 | -0,08R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 563/30 | 55/30 | 0,83 | 1,12 | -0,08R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 121/30 | 15/30 | 0,42 | 0,99 | -0,39R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 504/30 | 44/30 | 0,69 | 1,20 | -0,16R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 508/30 | 37/30 | 0,70 | 0,76 | -0,16R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 466/30 | 23/30 | 0,60 | 1,12 | -0,21R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 285/30 | 43/30 | 0,70 | 0,72 | -0,18R | €-8,84 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 12/30 | 0,00 | 1,74 | 0,00R | €17,78 | 1,54% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 24/30 | 0,00 | 1,59 | 0,00R | €13,94 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 667/30 | 118/30 | 0,87 | 0,70 | -0,07R | €-6,69 | 13,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 52/30 | 0,00 | 0,53 | 0,00R | €-15,84 | 9,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 232/30 | 68/30 | 1,01 | 0,71 | 0,00R | €-7,10 | 8,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 422/30 | 105/30 | 0,89 | 0,89 | -0,06R | €-2,45 | 9,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 343/30 | 61/30 | 0,78 | 0,46 | -0,12R | €-12,88 | 8,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 176/30 | 32/30 | 0,94 | 0,87 | -0,03R | €-3,37 | 3,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 451/30 | 83/30 | 0,80 | 0,88 | -0,10R | €-2,67 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 518/30 | 119/30 | 0,85 | 1,01 | -0,08R | €0,23 | 7,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 696/30 | 134/30 | 0,78 | 1,00 | -0,12R | €-0,05 | 4,46% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 76/30 | 0,00 | 1,16 | 0,00R | €3,92 | 4,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 87/30 | 0,00 | 0,87 | 0,00R | €-3,63 | 7,13% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 36/30 | 0,00 | 1,14 | 0,00R | €4,21 | 3,33% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 410/30 | 129/30 | 0,81 | 0,98 | -0,10R | €-0,43 | 6,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 656/30 | 146/30 | 0,74 | 0,84 | -0,14R | €-3,67 | 6,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 49/30 | 28/30 | 0,59 | 0,80 | -0,24R | €-5,20 | 3,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 667/30 | 156/30 | 0,80 | 0,84 | -0,11R | €-3,38 | 8,61% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 486/30 | 125/30 | 0,79 | 0,89 | -0,11R | €-2,64 | 8,81% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 260/30 | 79/30 | 0,91 | 0,72 | -0,05R | €-8,55 | 7,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 263/30 | 74/30 | 0,88 | 0,74 | -0,06R | €-7,45 | 6,59% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 371/30 | 94/30 | 0,87 | 0,60 | -0,06R | €-10,81 | 11,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 37/30 | 0,00 | 1,18 | 0,00R | €4,28 | 3,97% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 60/30 | 0,00 | 1,09 | 0,00R | €2,02 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 550/30 | 110/30 | 0,76 | 0,80 | -0,13R | €-5,12 | 6,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 74/30 | 0,00 | 0,71 | 0,00R | €-7,62 | 9,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 112/30 | 0,00 | 0,79 | 0,00R | €-4,14 | 8,63% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 38/30 | 0,00 | 0,80 | 0,00R | €-4,96 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 620/30 | 129/30 | 0,76 | 0,73 | -0,13R | €-6,03 | 8,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 269/30 | 39/30 | 0,69 | 1,09 | -0,21R | €2,27 | 4,45% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 185/30 | 74/30 | 1,11 | 0,76 | 0,05R | €-6,70 | 7,21% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 11/30 | 5/30 | 0,57 | 0,89 | -0,22R | €-2,34 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 14/30 | 7/30 | 0,22 | 0,84 | -0,63R | €-3,75 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 5/30 | 3/30 | 0,00 | 0,00 | -1,08R | €-55,91 | 2,43% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 15/30 | 9/30 | 0,78 | 0,53 | -0,13R | €-16,82 | 1,94% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 3/30 | 2/30 | 0,00 | 0,00 | -1,08R | €-50,11 | 1,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 542/30 | 89/30 | 0,96 | 0,74 | -0,02R | €-5,51 | 7,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 299/30 | 56/30 | 0,97 | 0,64 | -0,01R | €-9,58 | 6,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 586/30 | 102/30 | 0,97 | 0,39 | -0,01R | €-15,28 | 15,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 483/30 | 90/30 | 0,91 | 0,57 | -0,04R | €-9,65 | 8,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 63/30 | 23/30 | 1,25 | 0,64 | 0,11R | €-11,85 | 4,21% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 63/30 | 23/30 | 1,17 | 0,49 | 0,08R | €-17,17 | 5,41% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 154/30 | 48/30 | 0,86 | 0,60 | -0,07R | €-11,62 | 7,77% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 194/30 | 34/30 | 0,85 | 0,76 | -0,07R | €-5,53 | 3,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 94/30 | 0,74 | 0,53 | -0,20R | €-11,02 | 12,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 64/30 | 0,00 | 0,79 | 0,00R | €-4,65 | 8,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 75/30 | 0,74 | 0,38 | -0,20R | €-16,04 | 12,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 89/30 | 35/30 | 1,20 | 0,70 | 0,09R | €-10,07 | 5,48% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 339/30 | 78/30 | 1,08 | 0,61 | 0,04R | €-11,68 | 11,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 450/30 | 118/30 | 0,90 | 0,75 | -0,05R | €-6,68 | 10,02% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 51/30 | 0,00 | 1,06 | 0,00R | €1,21 | 2,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 12/30 | 10/30 | 0,51 | 0,62 | -0,36R | €-10,55 | 2,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 18/30 | 13/30 | 0,40 | 0,97 | -0,41R | €-0,67 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 213/30 | 66/30 | 0,82 | 1,36 | -0,12R | €8,77 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 143/30 | 34/30 | 0,78 | 1,45 | -0,13R | €9,69 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 453/30 | 85/30 | 0,88 | 0,52 | -0,07R | €-11,45 | 10,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 14/30 | 8/30 | 0,30 | 0,05 | -0,56R | €-38,45 | 3,14% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,94% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 13/30 | 7/30 | 0,28 | 0,28 | -0,63R | €-33,90 | 2,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 20/30 | 11/30 | 0,29 | 0,11 | -0,55R | €-41,03 | 4,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 12/30 | 15/30 | 0,89 | 0,35 | -0,07R | €-21,51 | 3,57% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 265/30 | 55/30 | 1,00 | 0,60 | -0,00R | €-13,70 | 7,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 49/30 | 0,00 | 0,54 | 0,00R | €-14,55 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 36/30 | 0,00 | 0,33 | 0,00R | €-29,57 | 11,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 44/30 | 0,00 | 0,52 | 0,00R | €-16,43 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 498/30 | 81/30 | 1,41 | 0,53 | 0,13R | €-10,88 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 233/30 | 50/30 | 1,01 | 0,61 | 0,01R | €-14,40 | 7,26% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 242/30 | 45/30 | 0,97 | 0,54 | -0,02R | €-17,57 | 8,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 168/30 | 48/30 | 1,00 | 0,54 | 0,00R | €-21,08 | 11,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 255/30 | 46/30 | 0,97 | 0,55 | -0,02R | €-16,50 | 7,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 567/30 | 103/30 | 0,85 | 0,54 | -0,08R | €-11,61 | 13,90% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 226/30 | 79/30 | 1,13 | 0,81 | 0,07R | €-6,18 | 9,47% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 202/30 | 66/30 | 0,48 | 0,85 | -0,30R | €-3,42 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 202/30 | 66/30 | 0,48 | 0,85 | -0,30R | €-3,42 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 202/30 | 66/30 | 0,48 | 0,85 | -0,30R | €-3,42 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 235/30 | 85/30 | 0,66 | 0,79 | -0,19R | €-4,51 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 241/30 | 57/30 | 0,74 | 0,78 | -0,12R | €-5,15 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 218/30 | 58/30 | 0,64 | 0,76 | -0,17R | €-5,32 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 276/30 | 54/30 | 0,98 | 0,55 | -0,01R | €-12,93 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 277/30 | 54/30 | 0,98 | 0,55 | -0,01R | €-12,93 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 277/30 | 54/30 | 0,98 | 0,55 | -0,01R | €-12,93 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 326/30 | 73/30 | 1,10 | 0,73 | 0,05R | €-7,20 | 11,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 127/30 | 12/30 | 0,85 | 0,47 | -0,09R | €-19,32 | 4,21% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 279/30 | 54/30 | 0,95 | 0,43 | -0,03R | €-17,52 | 11,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 296/30 | 68/30 | 1,17 | 0,66 | 0,07R | €-9,76 | 7,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 244/30 | 53/30 | 1,04 | 0,71 | 0,02R | €-9,45 | 7,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 307/30 | 75/30 | 1,17 | 0,61 | 0,07R | €-11,13 | 8,78% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 252/30 | 58/30 | 1,05 | 0,66 | 0,02R | €-10,62 | 7,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 349/30 | 66/30 | 1,07 | 0,36 | 0,03R | €-16,95 | 12,28% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 275/30 | 62/30 | 0,99 | 0,50 | -0,00R | €-14,65 | 12,06% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 262/30 | 58/30 | 0,97 | 0,50 | -0,01R | €-15,56 | 11,78% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 354/30 | 82/30 | 1,09 | 1,06 | 0,05R | €1,42 | 8,85% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 21/30 | 10/30 | 0,36 | 0,15 | -0,54R | €-37,89 | 4,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 3/30 | 3/30 | 0,58 | 0,32 | -0,30R | €-23,82 | 1,01% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 12/30 | 6/30 | 0,81 | 1,24 | -0,11R | €6,55 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 15/30 | 8/30 | 0,55 | 0,49 | -0,34R | €-15,55 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 3/30 | 3/30 | 0,63 | 0,35 | -0,26R | €-22,94 | 1,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 19/30 | 9/30 | 0,51 | 0,37 | -0,40R | €-26,61 | 3,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 4/30 | 4/30 | 0,00 | 0,00 | -1,06R | €-51,82 | 2,27% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07054**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 25.2 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64767 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation, volume_valid**
- High **0.07077**; close **0.07059**; wick alta **54.5%**; volume **x2.58**

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
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 100%, ADX 23.1.
- BTC trend score: **1,00**; ADX: **23,08**; breadth sopra EMA50: **100,00%**
- Mediana alt vs BTC: **0,32%**; dispersione: **19,22%**

- Aperti in questo ciclo: **103**
- Chiusi in questo ciclo: **109**
- Posizioni research aperte: **651**
- Trade research chiusi: **26477**
- Eventi di mercato indipendenti chiusi: **3648**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **68672**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 7 | 399 | 399 | 29,82% | 0,69 | -0,16R | €-637,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 7 | 366 | 366 | 28,96% | 0,61 | -0,21R | €-751,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 4 | 218 | 218 | 45,41% | 0,77 | -0,12R | €-271,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 4 | 220 | 220 | 31,82% | 0,74 | -0,13R | €-295,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 5 | 309 | 309 | 32,36% | 0,80 | -0,10R | €-308,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 5 | 278 | 278 | 32,01% | 0,70 | -0,15R | €-404,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 3 | 125 | 125 | 33,60% | 0,65 | -0,18R | €-225,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 3 | 280 | 280 | 26,79% | 0,59 | -0,24R | €-659,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 7 | 440 | 440 | 29,32% | 0,68 | -0,17R | €-742,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 7 | 402 | 402 | 28,11% | 0,58 | -0,22R | €-896,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 5 | 309 | 309 | 33,01% | 0,84 | -0,08R | €-249,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 8 | 563 | 563 | 39,96% | 0,83 | -0,08R | €-444,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 121 | 121 | 28,10% | 0,42 | -0,39R | €-469,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 8 | 504 | 504 | 29,37% | 0,69 | -0,16R | €-792,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 8 | 508 | 508 | 29,33% | 0,70 | -0,16R | €-793,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 8 | 466 | 466 | 28,11% | 0,60 | -0,21R | €-969,55 |
| MAIN | 15 | 285 | 285 | 25,26% | 0,70 | -0,18R | €-510,28 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 19 | 667 | 667 | 33,13% | 0,87 | -0,07R | €-483,22 |
| Bilanciata 1H V2 | 8 | 266 | 232 | 36,47% | 1,01 | 0,00R | €7,93 |
| Bilanciata 1H V3 Filtered | 13 | 422 | 422 | 34,12% | 0,89 | -0,06R | €-253,79 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 13 | 343 | 343 | 32,94% | 0,78 | -0,12R | €-399,14 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 6 | 176 | 176 | 38,07% | 0,94 | -0,03R | €-44,40 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 9 | 451 | 451 | 34,59% | 0,80 | -0,10R | €-439,14 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 9 | 518 | 518 | 35,71% | 0,85 | -0,08R | €-404,81 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 11 | 696 | 696 | 33,91% | 0,78 | -0,12R | €-807,24 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 410 | 410 | 34,88% | 0,81 | -0,10R | €-395,52 |
| SHADOW_1H_FAST_TP2_V1 | 13 | 656 | 656 | 30,79% | 0,74 | -0,14R | €-915,31 |
| Rapida 1H V2 | 2 | 57 | 49 | 36,84% | 0,59 | -0,24R | €-135,15 |
| Rapida 1H V3 Filtered | 8 | 667 | 667 | 34,48% | 0,80 | -0,11R | €-711,05 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 5 | 486 | 486 | 34,57% | 0,79 | -0,11R | €-527,51 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 260 | 260 | 47,31% | 0,91 | -0,05R | €-117,06 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 263 | 263 | 36,88% | 0,88 | -0,06R | €-157,46 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 5 | 371 | 371 | 36,93% | 0,87 | -0,06R | €-235,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 7 | 550 | 550 | 33,45% | 0,76 | -0,13R | €-708,89 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 8 | 620 | 620 | 33,55% | 0,76 | -0,13R | €-793,01 |
| SHADOW_4H_WIDE | 28 | 269 | 269 | 19,70% | 0,69 | -0,21R | €-556,44 |
| SHADOW_BOLLINGER_MR_1H | 3 | 185 | 185 | 48,11% | 1,11 | 0,05R | €92,06 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 11 | 11 | 54,55% | 0,57 | -0,22R | €-23,77 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 14 | 14 | 28,57% | 0,22 | -0,63R | €-88,00 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,84 |
| SHADOW_BTC_EMA_1H | 1 | 15 | 15 | 46,67% | 0,78 | -0,13R | €-19,79 |
| SHADOW_BTC_EMA_4H | 1 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,26 |
| SHADOW_COMBO_ADAPTIVE | 15 | 542 | 542 | 36,53% | 0,96 | -0,02R | €-122,67 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 10 | 299 | 299 | 36,45% | 0,97 | -0,01R | €-43,75 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 12 | 586 | 586 | 40,44% | 0,97 | -0,01R | €-80,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 15 | 483 | 483 | 39,13% | 0,91 | -0,04R | €-214,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 63 | 63 | 46,03% | 1,25 | 0,11R | €70,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 63 | 63 | 38,10% | 1,17 | 0,08R | €47,92 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 154 | 154 | 31,82% | 0,86 | -0,07R | €-103,13 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 194 | 194 | 35,05% | 0,85 | -0,07R | €-142,43 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 89 | 89 | 49,44% | 1,20 | 0,09R | €79,28 |
| SHADOW_COMBO_SCANNER | 8 | 339 | 339 | 35,69% | 1,08 | 0,04R | €135,25 |
| SHADOW_COMBO_TREND | 15 | 450 | 450 | 31,33% | 0,90 | -0,05R | €-245,18 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 12 | 12 | 33,33% | 0,51 | -0,36R | €-43,62 |
| SHADOW_DOGE_EMA_1H | 0 | 18 | 18 | 27,78% | 0,40 | -0,41R | €-73,66 |
| SHADOW_DONCHIAN_1H | 9 | 213 | 213 | 29,11% | 0,82 | -0,12R | €-247,57 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 9 | 143 | 143 | 30,77% | 0,78 | -0,13R | €-182,48 |
| SHADOW_EMA_TREND_1H | 15 | 453 | 453 | 30,91% | 0,88 | -0,07R | €-315,86 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 14 | 14 | 28,57% | 0,30 | -0,56R | €-77,90 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 13 | 13 | 23,08% | 0,28 | -0,63R | €-81,36 |
| SHADOW_ETH_EMA_1H | 1 | 20 | 20 | 30,00% | 0,29 | -0,55R | €-110,17 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 1 | 12 | 12 | 41,67% | 0,89 | -0,07R | €-8,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 11 | 265 | 265 | 32,45% | 1,00 | -0,00R | €-3,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 498 | 498 | 66,67% | 1,41 | 0,13R | €647,74 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 11 | 233 | 233 | 32,62% | 1,01 | 0,01R | €19,90 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 11 | 242 | 242 | 30,58% | 0,97 | -0,02R | €-41,81 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 7 | 168 | 168 | 32,74% | 1,00 | 0,00R | €1,97 |
| SHADOW_MASTER_ADAPTIVE_V1 | 11 | 255 | 255 | 31,76% | 0,97 | -0,02R | €-57,60 |
| Forza relativa 1H V1 | 13 | 567 | 567 | 29,28% | 0,85 | -0,08R | €-470,97 |
| Forza relativa 1H V2 | 8 | 242 | 226 | 35,12% | 1,13 | 0,07R | €160,94 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 6 | 202 | 202 | 25,74% | 0,48 | -0,30R | €-609,41 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 6 | 202 | 202 | 25,74% | 0,48 | -0,30R | €-609,41 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 6 | 202 | 202 | 25,74% | 0,48 | -0,30R | €-609,41 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 6 | 235 | 235 | 28,51% | 0,66 | -0,19R | €-446,90 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 4 | 241 | 241 | 51,87% | 0,74 | -0,12R | €-290,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 4 | 218 | 218 | 50,92% | 0,64 | -0,17R | €-362,69 |
| SHADOW_SCANNER_TOP10_LONG | 11 | 276 | 276 | 35,14% | 0,98 | -0,01R | €-21,44 |
| SHADOW_SCANNER_TOP15_LONG | 11 | 277 | 277 | 35,02% | 0,98 | -0,01R | €-32,55 |
| SHADOW_SCANNER_TOP20_LONG | 11 | 277 | 277 | 35,02% | 0,98 | -0,01R | €-32,55 |
| SHADOW_SCANNER_TOP5_BTC | 8 | 326 | 326 | 35,28% | 1,10 | 0,05R | €167,40 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 1 | 127 | 127 | 30,71% | 0,85 | -0,09R | €-112,63 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 8 | 279 | 279 | 33,69% | 0,95 | -0,03R | €-75,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 7 | 296 | 296 | 45,27% | 1,17 | 0,07R | €213,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 9 | 244 | 244 | 35,66% | 1,04 | 0,02R | €49,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 7 | 307 | 307 | 44,95% | 1,17 | 0,07R | €224,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 9 | 252 | 252 | 35,32% | 1,05 | 0,02R | €60,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 349 | 349 | 43,55% | 1,07 | 0,03R | €109,39 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 8 | 275 | 275 | 33,09% | 0,99 | -0,00R | €-9,06 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 262 | 262 | 32,06% | 0,97 | -0,01R | €-34,77 |
| SHADOW_SCANNER_TOP5_LONG | 10 | 354 | 354 | 36,44% | 1,09 | 0,05R | €168,00 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 21 | 21 | 23,81% | 0,36 | -0,54R | €-113,90 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 3 | 3 | 33,33% | 0,58 | -0,30R | €-8,87 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 12 | 12 | 50,00% | 0,81 | -0,11R | €-12,76 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 15 | 15 | 33,33% | 0,55 | -0,34R | €-50,34 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 3 | 3 | 33,33% | 0,63 | -0,26R | €-7,86 |
| SHADOW_SOL_EMA_1H | 1 | 19 | 19 | 26,32% | 0,51 | -0,40R | €-76,60 |
| SHADOW_SOL_EMA_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,50 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 2 | 43 | 43 | 23,26% | 0,48 | -0,33R | €-140,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 54 | 54 | 40,74% | 1,26 | 0,12R | €66,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 2 | 113 | 113 | 33,63% | 0,61 | -0,20R | €-230,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 17 | 17 | 35,29% | 0,92 | -0,04R | €-6,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 2 | 53 | 53 | 32,08% | 0,97 | -0,01R | €-6,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 53 | 53 | 16,98% | 0,45 | -0,28R | €-147,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 2 | 41 | 41 | 21,95% | 0,30 | -0,49R | €-202,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 41 | 41 | 41,46% | 1,39 | 0,17R | €69,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 2 | 106 | 106 | 33,02% | 0,50 | -0,26R | €-277,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 16 | 16 | 31,25% | 0,90 | -0,05R | €-7,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 2 | 52 | 52 | 32,69% | 1,07 | 0,03R | €15,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 50 | 50 | 16,00% | 0,30 | -0,38R | €-188,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 1 | 7 | 7 | 42,86% | 0,59 | -0,25R | €-17,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 66 | 66 | 39,39% | 0,47 | -0,33R | €-216,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 2 | 31 | 31 | 54,84% | 1,03 | 0,01R | €4,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 33,33% | 0,73 | -0,14R | €-8,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 1 | 68 | 68 | 32,35% | 0,45 | -0,32R | €-214,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 2 | 31 | 31 | 29,03% | 0,88 | -0,05R | €-15,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,39 | -0,35R | €-45,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 0,99 | -0,00R | €-1,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 2 | 85 | 85 | 34,12% | 0,63 | -0,21R | €-174,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,76 | -0,13R | €-18,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 2 | 42 | 42 | 33,33% | 1,17 | 0,07R | €29,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,25 | -0,43R | €-55,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 44 | 44 | 36,36% | 1,02 | 0,01R | €4,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 2 | 74 | 74 | 35,14% | 0,52 | -0,25R | €-187,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 14 | 14 | 28,57% | 0,88 | -0,06R | €-7,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 2 | 41 | 41 | 34,15% | 1,26 | 0,10R | €41,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 3 | 123 | 123 | 33,33% | 0,63 | -0,19R | €-234,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,73 | -0,16R | €-83,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 108 | 108 | 32,41% | 0,64 | -0,20R | €-210,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 1 | 32 | 32 | 21,88% | 0,69 | -0,15R | €-47,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 2 | 33 | 33 | 18,18% | 0,25 | -0,52R | €-172,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 3 | 142 | 142 | 33,10% | 0,64 | -0,19R | €-274,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 2 | 50 | 50 | 26,00% | 0,80 | -0,09R | €-43,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 72 | 72 | 23,61% | 0,63 | -0,18R | €-129,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 2 | 32 | 32 | 18,75% | 0,16 | -0,60R | €-192,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 3 | 132 | 132 | 31,82% | 0,54 | -0,24R | €-320,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 2 | 49 | 49 | 26,53% | 0,78 | -0,09R | €-45,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 67 | 67 | 22,39% | 0,45 | -0,28R | €-187,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,39 | -0,35R | €-45,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 53 | 53 | 37,74% | 1,07 | 0,03R | €18,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 2 | 85 | 85 | 36,47% | 0,75 | -0,14R | €-115,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,76 | -0,13R | €-18,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 2 | 42 | 42 | 33,33% | 1,17 | 0,07R | €29,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 64 | 64 | 35,94% | 0,49 | -0,29R | €-183,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 67 | 67 | 46,27% | 1,03 | 0,01R | €9,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 4 | 157 | 157 | 37,58% | 0,80 | -0,09R | €-145,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 29 | 29 | 37,93% | 0,66 | -0,17R | €-50,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 1 | 67 | 67 | 47,76% | 1,43 | 0,14R | €91,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 82 | 82 | 40,24% | 0,82 | -0,08R | €-67,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 1 | 48 | 48 | 37,50% | 0,47 | -0,32R | €-151,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 1 | 4 | 4 | 50,00% | 0,92 | -0,05R | €-1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 2 | 58 | 58 | 20,69% | 0,35 | -0,40R | €-231,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 0 | 61 | 61 | 34,43% | 0,98 | -0,01R | €-5,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 3 | 138 | 138 | 32,61% | 0,63 | -0,20R | €-280,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 29 | 29 | 31,03% | 0,68 | -0,17R | €-48,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 2 | 60 | 60 | 33,33% | 1,24 | 0,10R | €57,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 71 | 71 | 22,54% | 0,58 | -0,21R | €-149,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 2 | 58 | 58 | 20,69% | 0,35 | -0,40R | €-231,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 0 | 63 | 63 | 34,92% | 1,01 | 0,01R | €4,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 3 | 139 | 139 | 32,37% | 0,62 | -0,21R | €-290,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 29 | 29 | 31,03% | 0,68 | -0,17R | €-48,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 2 | 60 | 60 | 33,33% | 1,24 | 0,10R | €57,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 71 | 71 | 22,54% | 0,58 | -0,21R | €-149,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 57 | 57 | 21,05% | 0,27 | -0,46R | €-264,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 51 | 51 | 35,29% | 1,04 | 0,02R | €11,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 3 | 130 | 130 | 30,77% | 0,47 | -0,29R | €-370,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 25 | 25 | 28,00% | 0,74 | -0,13R | €-33,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 2 | 59 | 59 | 33,90% | 1,31 | 0,12R | €72,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 66 | 66 | 21,21% | 0,38 | -0,32R | €-211,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 3 | 23 | 23 | 26,09% | 0,67 | -0,18R | €-41,28 |
| MAIN | ALT_ROTATION_UP | 1 | 41 | 41 | 17,07% | 0,31 | -0,48R | €-197,22 |
| MAIN | RANGE | 2 | 75 | 75 | 21,33% | 0,62 | -0,23R | €-175,62 |
| MAIN | RANGE_HIGH_VOL | 1 | 18 | 18 | 22,22% | 0,69 | -0,16R | €-28,68 |
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
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 59 | 59 | 22,03% | 0,42 | -0,41R | €-240,08 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 86 | 86 | 33,72% | 0,90 | -0,06R | €-51,31 |
| Bilanciata 1H V1 | RANGE | 7 | 172 | 172 | 39,53% | 1,05 | 0,03R | €47,77 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 3 | 39 | 39 | 25,64% | 0,53 | -0,31R | €-120,94 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 3 | 94 | 94 | 38,30% | 1,22 | 0,11R | €103,53 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 85 | 85 | 30,59% | 0,70 | -0,16R | €-135,86 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 110 | 110 | 30,00% | 0,91 | -0,05R | €-50,84 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 62 | 52 | 35,48% | 1,01 | 0,00R | €2,56 |
| Bilanciata 1H V2 | RANGE | 5 | 124 | 112 | 34,68% | 0,82 | -0,11R | €-134,20 |
| Bilanciata 1H V2 | TRANSITION | 3 | 80 | 68 | 40,00% | 1,36 | 0,17R | €139,57 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 48 | 48 | 29,17% | 0,51 | -0,32R | €-151,23 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 47 | 47 | 29,79% | 1,04 | 0,02R | €9,50 |
| Bilanciata 1H V3 Filtered | RANGE | 5 | 118 | 118 | 40,68% | 1,06 | 0,03R | €34,65 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 16 | 16 | 25,00% | 0,61 | -0,25R | €-40,63 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 3 | 51 | 51 | 35,29% | 1,10 | 0,05R | €24,61 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 2 | 59 | 59 | 35,59% | 0,66 | -0,19R | €-114,01 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €7,90 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 37 | 37 | 24,32% | 0,26 | -0,50R | €-184,60 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 45 | 45 | 31,11% | 1,12 | 0,07R | €30,49 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 5 | 96 | 96 | 38,54% | 0,83 | -0,08R | €-81,51 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 28,57% | 0,77 | -0,14R | €-19,81 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 3 | 43 | 43 | 34,88% | 1,10 | 0,04R | €18,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 2 | 60 | 60 | 35,00% | 0,64 | -0,21R | €-125,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 42 | 42 | 23,81% | 0,74 | -0,13R | €-52,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,40 | -0,39R | €-50,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 48,84% | 1,27 | 0,11R | €46,79 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 5 | 44 | 44 | 38,64% | 0,90 | -0,05R | €-24,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 30,61% | 0,80 | -0,08R | €-38,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 25 | 25 | 24,00% | 0,42 | -0,36R | €-89,92 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 64 | 64 | 45,31% | 1,11 | 0,05R | €33,16 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 6 | 146 | 146 | 34,93% | 0,76 | -0,13R | €-184,09 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 1 | 58 | 58 | 39,66% | 1,12 | 0,05R | €28,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 75 | 75 | 28,00% | 0,76 | -0,11R | €-80,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 43 | 43 | 23,26% | 0,41 | -0,40R | €-172,14 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 176 | 176 | 39,20% | 0,96 | -0,02R | €-38,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 60 | 60 | 41,67% | 1,26 | 0,10R | €57,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 91 | 91 | 27,47% | 0,67 | -0,17R | €-153,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 1 | 87 | 87 | 24,14% | 0,43 | -0,38R | €-327,07 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 37,84% | 0,85 | -0,08R | €-62,01 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 8 | 202 | 202 | 36,63% | 0,81 | -0,10R | €-208,09 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 34 | 34 | 44,12% | 1,18 | 0,08R | €27,34 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 2 | 84 | 84 | 41,67% | 1,33 | 0,13R | €105,25 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 105 | 105 | 27,62% | 0,69 | -0,16R | €-170,93 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 51 | 51 | 25,49% | 0,42 | -0,40R | €-205,45 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 0,89 | -0,06R | €-29,98 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 2 | 116 | 116 | 42,24% | 1,07 | 0,04R | €42,31 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 15 | 15 | 46,67% | 1,18 | 0,08R | €11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 52 | 52 | 40,38% | 1,25 | 0,10R | €50,06 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 60 | 60 | 26,67% | 0,58 | -0,23R | €-137,91 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 2 | 85 | 85 | 23,53% | 0,42 | -0,38R | €-324,04 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 76 | 76 | 39,47% | 1,03 | 0,02R | €13,46 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 8 | 184 | 184 | 34,78% | 0,78 | -0,12R | €-217,92 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 33 | 33 | 33,33% | 0,87 | -0,06R | €-21,22 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 77 | 77 | 37,66% | 1,39 | 0,15R | €117,34 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 96 | 96 | 20,83% | 0,52 | -0,26R | €-247,93 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 2 | 40 | 33 | 37,50% | 0,73 | -0,14R | €-57,99 |
| Rapida 1H V2 | TRANSITION | 0 | 7 | 7 | 57,14% | 0,81 | -0,07R | €-4,61 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 85 | 85 | 23,53% | 0,42 | -0,38R | €-323,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 70 | 70 | 38,57% | 0,94 | -0,03R | €-23,47 |
| Rapida 1H V3 Filtered | RANGE | 4 | 181 | 181 | 37,02% | 0,80 | -0,10R | €-187,49 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 30 | 30 | 43,33% | 1,08 | 0,04R | €11,26 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 2 | 75 | 75 | 38,67% | 1,13 | 0,05R | €39,80 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 109 | 109 | 36,70% | 0,98 | -0,01R | €-9,47 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 64 | 64 | 25,00% | 0,44 | -0,38R | €-245,63 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 61 | 61 | 40,98% | 1,03 | 0,01R | €8,26 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 2 | 144 | 144 | 38,19% | 0,88 | -0,06R | €-85,96 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 1 | 19 | 19 | 47,37% | 1,37 | 0,15R | €27,85 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 1 | 57 | 57 | 38,60% | 1,03 | 0,01R | €8,23 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 70 | 70 | 28,57% | 0,65 | -0,18R | €-127,20 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 14 | 14 | 21,43% | 0,17 | -0,68R | €-94,58 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 81 | 81 | 43,21% | 0,85 | -0,09R | €-71,52 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 1 | 33 | 33 | 57,58% | 1,39 | 0,15R | €49,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 15,38% | 0,18 | -0,66R | €-85,74 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 1 | 83 | 83 | 39,76% | 0,92 | -0,04R | €-34,32 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 1 | 33 | 33 | 39,39% | 1,19 | 0,07R | €24,55 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 22 | 22 | 13,64% | 0,19 | -0,62R | €-136,40 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 61 | 61 | 37,70% | 0,87 | -0,07R | €-40,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 3 | 104 | 104 | 40,38% | 0,91 | -0,05R | €-47,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 40,00% | 1,09 | 0,04R | €6,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 48 | 48 | 41,67% | 1,24 | 0,10R | €45,62 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 55 | 55 | 21,82% | 0,37 | -0,44R | €-244,11 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 4 | 183 | 183 | 38,25% | 0,85 | -0,08R | €-139,44 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 59 | 59 | 33,90% | 0,96 | -0,02R | €-9,17 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 95 | 95 | 31,58% | 0,77 | -0,12R | €-114,65 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 1 | 84 | 84 | 23,81% | 0,43 | -0,37R | €-312,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 36,23% | 0,83 | -0,09R | €-64,59 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 179 | 179 | 36,87% | 0,79 | -0,11R | €-202,23 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 29 | 29 | 44,83% | 1,17 | 0,07R | €21,39 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 2 | 70 | 70 | 38,57% | 1,15 | 0,06R | €42,57 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 92 | 92 | 30,43% | 0,73 | -0,14R | €-132,21 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 6 | 18 | 18 | 22,22% | 0,98 | -0,01R | €-1,83 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 4 | 34 | 34 | 23,53% | 0,48 | -0,41R | €-138,96 |
| SHADOW_4H_WIDE | RANGE | 6 | 69 | 69 | 14,49% | 0,58 | -0,30R | €-204,54 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 4 | 37 | 37 | 13,51% | 0,37 | -0,47R | €-173,36 |
| SHADOW_4H_WIDE | TREND_DOWN | 4 | 43 | 43 | 27,91% | 1,03 | 0,02R | €9,48 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 38 | 38 | 23,68% | 1,04 | 0,02R | €8,48 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 21 | 21 | 47,62% | 0,99 | -0,00R | €-0,73 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 2 | 67 | 67 | 46,27% | 1,05 | 0,02R | €16,55 |
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
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 4 | 50 | 50 | 26,00% | 0,58 | -0,26R | €-128,98 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 62 | 62 | 33,87% | 0,89 | -0,06R | €-39,82 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 5 | 143 | 143 | 41,96% | 0,96 | -0,02R | €-28,20 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 2 | 28 | 28 | 39,29% | 1,10 | 0,04R | €12,47 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 73 | 73 | 41,10% | 1,42 | 0,19R | €140,22 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 3 | 72 | 72 | 34,72% | 0,88 | -0,06R | €-43,31 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 95 | 95 | 35,79% | 1,09 | 0,04R | €37,83 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 18,75% | 0,45 | -0,32R | €-51,25 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 56 | 56 | 33,93% | 0,90 | -0,06R | €-32,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 5 | 70 | 70 | 48,57% | 1,22 | 0,10R | €72,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,85 | -0,07R | €-8,04 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 39 | 39 | 46,15% | 2,07 | 0,34R | €133,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 2 | 42 | 42 | 35,71% | 1,10 | 0,05R | €19,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 2 | 64 | 64 | 31,25% | 0,60 | -0,22R | €-138,25 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 69 | 69 | 37,68% | 0,88 | -0,06R | €-41,75 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 5 | 142 | 142 | 41,55% | 1,11 | 0,05R | €69,17 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 2 | 34 | 34 | 44,12% | 0,99 | -0,00R | €-0,84 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 63 | 63 | 46,03% | 1,24 | 0,10R | €64,17 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 96 | 96 | 37,50% | 0,88 | -0,05R | €-45,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 97 | 97 | 49,48% | 1,29 | 0,12R | €117,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 50 | 50 | 26,00% | 0,62 | -0,24R | €-117,73 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 60 | 60 | 35,00% | 0,91 | -0,05R | €-29,68 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 5 | 131 | 131 | 45,04% | 1,03 | 0,01R | €18,26 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 2 | 26 | 26 | 46,15% | 1,34 | 0,14R | €35,41 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 56 | 56 | 44,64% | 1,30 | 0,14R | €75,84 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 3 | 72 | 72 | 38,89% | 0,88 | -0,06R | €-42,22 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 74 | 74 | 36,49% | 0,71 | -0,13R | €-98,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 2 | 33 | 33 | 36,36% | 0,91 | -0,05R | €-16,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 2 | 33 | 33 | 36,36% | 0,90 | -0,06R | €-18,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 18 | 18 | 27,78% | 0,63 | -0,21R | €-38,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 40 | 40 | 40,00% | 1,12 | 0,06R | €24,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 2 | 26 | 26 | 34,62% | 0,99 | -0,01R | €-1,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 5 | 81 | 81 | 39,51% | 1,07 | 0,04R | €29,95 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 100 | 100 | 34,00% | 0,78 | -0,10R | €-104,07 |
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
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 19 | 19 | 10,53% | 0,19 | -0,54R | €-103,12 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 54 | 54 | 35,19% | 1,01 | 0,01R | €4,26 |
| SHADOW_COMBO_SCANNER | RANGE | 4 | 80 | 80 | 46,25% | 1,42 | 0,20R | €158,10 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,67 | -0,16R | €-17,68 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 2 | 55 | 55 | 43,64% | 1,74 | 0,34R | €186,29 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 43 | 43 | 30,23% | 0,73 | -0,15R | €-65,86 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 4 | 38 | 38 | 26,32% | 0,60 | -0,25R | €-93,21 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 56 | 56 | 28,57% | 0,69 | -0,21R | €-118,27 |
| SHADOW_COMBO_TREND | RANGE | 5 | 122 | 122 | 34,43% | 0,99 | -0,01R | €-7,39 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 19 | 19 | 36,84% | 1,37 | 0,14R | €27,46 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 61 | 61 | 36,07% | 1,32 | 0,17R | €103,93 |
| SHADOW_COMBO_TREND | TREND_DOWN | 4 | 63 | 63 | 30,16% | 0,71 | -0,16R | €-100,10 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 73 | 73 | 28,77% | 1,00 | -0,00R | €-0,70 |
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
| SHADOW_DONCHIAN_1H | RANGE | 6 | 58 | 58 | 31,03% | 0,94 | -0,04R | €-21,10 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 11 | 11 | 45,45% | 1,53 | 0,25R | €27,28 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 25 | 25 | 40,00% | 1,57 | 0,29R | €71,79 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 16,67% | 0,21 | -0,66R | €-118,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 21,43% | 0,16 | -0,64R | €-89,01 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 6 | 38 | 38 | 31,58% | 0,84 | -0,10R | €-36,17 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 55,56% | 2,51 | 0,53R | €47,54 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 18 | 18 | 50,00% | 2,40 | 0,56R | €101,05 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 41 | 41 | 24,39% | 0,51 | -0,32R | €-130,86 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 52 | 52 | 26,92% | 0,66 | -0,24R | €-123,18 |
| SHADOW_EMA_TREND_1H | RANGE | 3 | 121 | 121 | 34,71% | 1,04 | 0,02R | €27,69 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 2 | 21 | 21 | 42,86% | 1,74 | 0,26R | €55,14 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 59 | 59 | 35,59% | 1,21 | 0,12R | €68,24 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 4 | 65 | 65 | 30,77% | 0,70 | -0,17R | €-107,60 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 76 | 76 | 27,63% | 0,92 | -0,04R | €-31,30 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-53,00 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,10 | -0,75R | €-29,95 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 1 | 4 | 4 | 25,00% | 0,18 | -0,69R | €-27,47 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,50R | €5,03 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 0,11R | €1,10 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 1 | 5 | 5 | 20,00% | 0,15 | -0,77R | €-38,41 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 3 | 77 | 77 | 31,17% | 1,00 | 0,00R | €0,98 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 3 | 31 | 31 | 45,16% | 1,66 | 0,35R | €109,16 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 2 | 46 | 46 | 34,78% | 1,09 | 0,06R | €25,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 1 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 2 | 24 | 24 | 50,00% | 0,93 | -0,03R | €-7,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 144 | 144 | 65,97% | 1,42 | 0,13R | €188,57 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 72 | 72 | 75,00% | 1,91 | 0,22R | €160,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 2 | 75 | 75 | 65,33% | 1,35 | 0,12R | €90,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 3 | 15 | 15 | 20,00% | 0,57 | -0,29R | €-44,23 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 78 | 78 | 33,33% | 1,11 | 0,06R | €49,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 3 | 30 | 30 | 36,67% | 1,16 | 0,10R | €29,25 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 2 | 42 | 42 | 38,10% | 1,23 | 0,14R | €58,57 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 11 | 11 | 27,27% | 0,97 | -0,02R | €-2,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 70 | 70 | 30,00% | 1,10 | 0,06R | €43,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 3 | 27 | 27 | 40,74% | 1,41 | 0,24R | €64,16 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 2 | 39 | 39 | 38,46% | 1,25 | 0,16R | €60,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 0,00% | 0,00 | -0,91R | €-82,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 58 | 58 | 36,21% | 1,14 | 0,09R | €51,45 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 3 | 23 | 23 | 47,83% | 2,07 | 0,48R | €111,47 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 31 | 31 | 25,81% | 0,70 | -0,22R | €-66,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 3 | 15 | 15 | 20,00% | 0,52 | -0,36R | €-54,10 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 73 | 73 | 32,88% | 1,10 | 0,06R | €44,42 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 3 | 30 | 30 | 40,00% | 1,33 | 0,20R | €59,22 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 2 | 40 | 40 | 37,50% | 1,20 | 0,12R | €48,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 4 | 51 | 51 | 19,61% | 0,39 | -0,41R | €-209,10 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 31,88% | 0,83 | -0,11R | €-74,86 |
| Forza relativa 1H V1 | RANGE | 3 | 165 | 165 | 30,91% | 0,84 | -0,08R | €-139,88 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 25 | 25 | 28,00% | 0,61 | -0,20R | €-49,41 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 2 | 71 | 71 | 38,03% | 1,46 | 0,23R | €161,78 |
| Forza relativa 1H V1 | TREND_DOWN | 3 | 72 | 72 | 29,17% | 0,87 | -0,07R | €-50,78 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 96 | 96 | 25,00% | 0,89 | -0,06R | €-55,92 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 23 | 23 | 30,43% | 0,77 | -0,13R | €-29,17 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 29 | 26 | 34,48% | 1,17 | 0,09R | €26,73 |
| Forza relativa 1H V2 | RANGE | 3 | 71 | 68 | 35,21% | 0,95 | -0,03R | €-19,41 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 2 | 40 | 35 | 40,00% | 1,70 | 0,32R | €129,71 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 34 | 33 | 29,41% | 0,95 | -0,02R | €-7,23 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 31 | 31 | 12,90% | 0,15 | -0,65R | €-202,51 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 59 | 59 | 23,73% | 0,34 | -0,38R | €-225,86 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 16 | 16 | 37,50% | 1,22 | 0,10R | €15,71 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 1 | 20 | 20 | 45,00% | 1,25 | 0,13R | €25,98 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 31 | 31 | 12,90% | 0,15 | -0,65R | €-202,51 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 59 | 59 | 23,73% | 0,34 | -0,38R | €-225,86 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 16 | 16 | 37,50% | 1,22 | 0,10R | €15,71 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 1 | 20 | 20 | 45,00% | 1,25 | 0,13R | €25,98 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 31 | 31 | 12,90% | 0,15 | -0,65R | €-202,51 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 59 | 59 | 23,73% | 0,34 | -0,38R | €-225,86 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 16 | 16 | 37,50% | 1,22 | 0,10R | €15,71 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 1 | 20 | 20 | 45,00% | 1,25 | 0,13R | €25,98 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 27 | 27 | 22,22% | 0,57 | -0,29R | €-77,85 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,07 | 0,03R | €4,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 72 | 72 | 29,17% | 0,63 | -0,20R | €-145,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,32 | 0,14R | €23,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 1 | 36 | 36 | 38,89% | 1,04 | 0,02R | €7,27 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 40 | 40 | 27,50% | 0,38 | -0,36R | €-144,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 31 | 31 | 38,71% | 0,36 | -0,37R | €-116,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 64 | 64 | 54,69% | 0,66 | -0,15R | €-94,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 21 | 21 | 61,90% | 1,36 | 0,14R | €29,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 28 | 28 | 60,71% | 1,52 | 0,22R | €60,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 1 | 65 | 65 | 53,85% | 0,63 | -0,16R | €-106,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 37,04% | 0,25 | -0,45R | €-120,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 57 | 57 | 54,39% | 0,40 | -0,26R | €-148,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 19 | 19 | 57,89% | 1,22 | 0,10R | €18,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 27 | 27 | 62,96% | 1,58 | 0,23R | €61,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 1 | 55 | 55 | 52,73% | 0,62 | -0,17R | €-92,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,67 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 54 | 54 | 29,63% | 0,76 | -0,13R | €-71,01 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 5 | 62 | 62 | 51,61% | 1,55 | 0,22R | €136,36 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,77 | -0,13R | €-12,60 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,67 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 55 | 55 | 29,09% | 0,74 | -0,15R | €-82,12 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 5 | 62 | 62 | 51,61% | 1,55 | 0,22R | €136,36 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,77 | -0,13R | €-12,60 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 2 | 11 | 11 | 27,27% | 0,67 | -0,18R | €-20,30 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 55 | 55 | 29,09% | 0,74 | -0,15R | €-82,12 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 5 | 62 | 62 | 51,61% | 1,55 | 0,22R | €136,36 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,77 | -0,13R | €-12,60 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 17 | 17 | 11,76% | 0,23 | -0,48R | €-80,99 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 54 | 54 | 35,19% | 1,02 | 0,01R | €4,85 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 4 | 75 | 75 | 46,67% | 1,57 | 0,25R | €191,09 |
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
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 4 | 70 | 70 | 45,71% | 1,43 | 0,20R | €137,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,84 | -0,07R | €-6,98 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 2 | 39 | 39 | 46,15% | 2,24 | 0,46R | €179,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,13 | -0,45R | €-71,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 4 | 84 | 84 | 46,43% | 1,48 | 0,18R | €150,78 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 40,00% | 1,09 | 0,03R | €3,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 40 | 40 | 50,00% | 1,40 | 0,16R | €62,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 7,69% | 0,02 | -0,70R | €-91,01 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 4 | 73 | 73 | 47,95% | 1,52 | 0,23R | €167,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 45,45% | 0,93 | -0,03R | €-2,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 3 | 35 | 35 | 40,00% | 1,71 | 0,29R | €102,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,52 | -0,25R | €-50,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 84 | 84 | 46,43% | 1,48 | 0,18R | €150,78 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 40,00% | 1,09 | 0,03R | €3,89 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 42 | 42 | 47,62% | 1,32 | 0,13R | €52,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 13,33% | 0,25 | -0,47R | €-69,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 4 | 73 | 73 | 47,95% | 1,52 | 0,23R | €167,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 45,45% | 0,93 | -0,03R | €-2,88 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 3 | 36 | 36 | 38,89% | 1,59 | 0,26R | €91,94 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 27,27% | 0,48 | -0,27R | €-58,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 57 | 57 | 43,86% | 0,96 | -0,02R | €-11,39 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 77 | 77 | 46,75% | 1,44 | 0,17R | €131,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,89 | -0,03R | €-4,89 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 2 | 47 | 47 | 48,94% | 1,35 | 0,14R | €66,28 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 56 | 56 | 44,64% | 0,92 | -0,03R | €-18,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 10 | 10 | 20,00% | 0,44 | -0,30R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 55 | 55 | 32,73% | 0,98 | -0,01R | €-7,49 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 66 | 66 | 43,94% | 1,44 | 0,21R | €137,59 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 0,83 | -0,07R | €-7,48 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 2 | 39 | 39 | 43,59% | 1,98 | 0,39R | €152,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 41 | 41 | 29,27% | 0,77 | -0,13R | €-54,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 10,00% | 0,03 | -0,60R | €-60,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 56 | 56 | 33,93% | 0,92 | -0,04R | €-23,50 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 61 | 61 | 42,62% | 1,44 | 0,22R | €132,62 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,58 | -0,21R | €-23,05 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 2 | 33 | 33 | 42,42% | 2,48 | 0,51R | €169,33 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 38 | 38 | 28,95% | 0,79 | -0,11R | €-43,01 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 2 | 18 | 18 | 16,67% | 0,33 | -0,46R | €-83,20 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 56 | 56 | 32,14% | 0,86 | -0,08R | €-42,22 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 77 | 77 | 50,65% | 1,64 | 0,27R | €206,88 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 12 | 12 | 25,00% | 0,56 | -0,28R | €-33,43 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 2 | 55 | 55 | 41,82% | 1,62 | 0,26R | €142,69 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 78 | 78 | 34,62% | 1,08 | 0,04R | €29,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,84 | -0,09R | €-1,73 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 7 | 7 | 28,57% | 0,41 | -0,47R | €-32,89 |
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
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 5 | 5 | 60,00% | 1,86 | 0,38R | €19,25 |
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

Generato: 2026-08-19T13:07:08+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **627**
- Scenari virtuali ancora attivi: **13167**
- Gruppi in attesa dell'uscita originale: **309**
- Gruppi con originale chiuso ma Shadow ancora attive: **318**
- Confronti completati: **261275**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 6072 | 6145 | +€1,48 | 49,0% | 1350 | 712 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 6069 | 6142 | +€1,31 | 44,6% | 860 | 1061 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 6065 | 6138 | €-3,51 | 36,4% | 524 | 1545 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 6057 | 6126 | +€9,83 | 53,2% | 1670 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 6057 | 6126 | +€8,91 | 52,6% | 1653 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 6057 | 6126 | +€7,68 | 51,2% | 1662 | 130 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 6057 | 6126 | +€6,47 | 50,6% | 1834 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 6057 | 6126 | +€6,24 | 51,3% | 1577 | 202 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 6051 | 6120 | +€8,53 | 46,2% | 1357 | 116 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 6051 | 6120 | +€7,32 | 46,3% | 1292 | 182 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 6051 | 6120 | +€6,75 | 44,6% | 1476 | 103 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 6049 | 6118 | +€6,30 | 45,6% | 1171 | 313 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 6046 | 6115 | +€3,19 | 40,0% | 768 | 952 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 6045 | 6114 | +€2,31 | 37,5% | 630 | 1228 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 6041 | 6110 | +€4,43 | 44,1% | 1042 | 544 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 6012 | 6081 | +€5,59 | 36,6% | 901 | 544 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5987 | 6056 | €-1,52 | 34,6% | 538 | 1422 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5985 | 6051 | +€5,08 | 39,9% | 486 | 859 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5962 | 6031 | €-2,01 | 37,7% | 1071 | 1103 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5869 | 5938 | €-6,11 | 29,7% | 507 | 1633 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-19T13:07:20+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **261275**
- Valutazioni prodotte: **19520**
- Candidature al Blocco 5: **75**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 319 | 0,463 | 0,309 | 0,357 | 62,7% | 95,1 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 4644 | 0,265 | 0,184 | 0,232 | 56,8% | 89,9 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 4644 | 0,249 | 0,164 | 0,219 | 56,7% | 89,7 | ELIGIBLE_FOR_MUTATION |
| GB40_R040 | 4644 | 0,221 | 0,149 | 0,187 | 55,5% | 88,5 | ELIGIBLE_FOR_MUTATION |
| TP_R035 | 4647 | 0,170 | 0,144 | 0,139 | 54,6% | 87,9 | VALIDATING |
| GB20_R050 | 4644 | 0,268 | 0,158 | 0,233 | 54,8% | 87,8 | VALIDATING |
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

Generato: 2026-08-19T13:10:04+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 79 | 100,00% | 1,08 | +€70,87 | +€0,90 | 2,31% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 79 | 100,00% | 1,06 | +€55,14 | +€0,70 | 2,58% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 39 | 95,12% | 0,99 | €-5,57 | €-0,14 | 2,95% | EARLY_NOT_CONFIRMED |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 31 | 93,94% | 0,00 | €-346,24 | €-11,17 | 3,46% | EARLY_NOT_CONFIRMED |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 78 | 100,00% | 1,22 | +€275,65 | +€3,53 | 2,13% | NOT_READY_FOR_PROMOTION |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-19T13:06:40+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **76**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **620.39 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 228 | 0 | 29305.41 |
| DOWN_20 | 228 | 0 | 58610.82 |
| DOWN_30 | 228 | 16 | 88158.38 |
| DOWN_40 | 228 | 64 | 110683.61 |
| UP_10 | 106 | 0 | 14974.33 |
| UP_20 | 106 | 0 | 29948.65 |
| UP_30 | 106 | 8 | 45293.94 |
| UP_40 | 106 | 41 | 56581.59 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-19T13:05:15+00:00

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

Generato: 2026-08-19T13:10:08+00:00

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

Generato: 2026-08-19T13:10:08+00:00

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

Generato: 2026-08-19T13:10:08+00:00

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

Generato: 2026-08-19T13:10:08+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 18.6 | E | 134 | 1.06 | 0.029 | 8.23 |
| 2 | SHADOW_1H_FAST_V3 | BASELINE | 14.9 | E | 157 | 0.86 | -0.074 | 23.16 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 13.7 | E | 130 | 0.89 | -0.062 | 19.20 |
| 4 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 13.4 | E | 76 | 1.09 | 0.042 | 8.50 |
| 5 | SHADOW_DONCHIAN_1H | BASELINE | 13.2 | E | 66 | 1.14 | 0.084 | 8.55 |
| 6 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 12.6 | E | 119 | 0.88 | -0.071 | 24.39 |
| 7 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 12.3 | E | 51 | 1.16 | 0.082 | 7.12 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 11.5 | E | 130 | 0.75 | -0.141 | 25.05 |
| 9 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 11.4 | E | 110 | 0.87 | -0.075 | 14.74 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 11.2 | E | 113 | 0.79 | -0.107 | 23.71 |

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

Generato: 2026-08-19T13:10:08+00:00

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
| 5 | MAIN_DYNAMIC_ASSET_SELECTOR_V1 | main-dynamic-asset-selector-v1 | INSUFFICIENT | 68.5 | 9 | 2.21 | 0.485 | 2.49 |
| 6 | SHADOW_RSI_LONG_5X_RSI20 | shadow-rsi-long-5x-rsi20 | INSUFFICIENT | 65.1 | 9 | 1.80 | 0.319 | 2.40 |
| 7 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 61.6 | 9 | 1.61 | 0.224 | 2.21 |
| 8 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | COMPATIBLE | 61.5 | 49 | 1.33 | 0.149 | 5.17 |
| 9 | SHADOW_1H_FAST | shadow-1h-fast | COMPATIBLE | 55.1 | 61 | 1.27 | 0.113 | 6.50 |
| 10 | SHADOW_RELATIVE_STRENGTH_V2 | shadow-relative-strength-v2 | NEUTRAL | 50.8 | 64 | 1.11 | 0.064 | 8.69 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-19T13:10:08+00:00

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

Generato: 2026-08-19T13:06:40+00:00

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
