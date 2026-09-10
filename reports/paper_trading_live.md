# Paper trading automatico KuCoin

Generato: 2026-09-10T13:20:18+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-10T13:05:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-10T13:05:33+00:00 | 2026-09-10T13:05:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-10T12:45:00+00:00 | 2026-09-10T12:45:00+00:00 | 6,3 min | 25,0 min | OK |
| 60m | 12 | 2026-09-10T12:00:00+00:00 | 2026-09-10T12:00:00+00:00 | 6,3 min | 45,0 min | OK |
| 240m | 12 | 2026-09-10T08:00:00+00:00 | 2026-09-10T08:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FAST NoHigh <7,5 · SHORT only | BTC | 60m | SHORT | -7,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Regime Guard | SOL | 60m | SHORT | -7,73 | 4,50 | 0,00 | OPENED | 6,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 NoHigh — Regime Guard | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 1H | SOL | 60m | SHORT | -7,73 | 5,00 | 0,00 | OPENED | 6,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Btc Bollinger 1H | BTC | 60m | SHORT | -7,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — MFE Trail esistente | PEPE | 60m | SHORT | -7,59 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | PEPE | 60m | SHORT | -7,59 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | XRP | 60m | SHORT | -5,05 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | SOL | 60m | SHORT | -7,73 | 5,00 | 0,00 | OPENED | 6,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | HYPE | 60m | SHORT | -8,56 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | BTC | 60m | SHORT | -7,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | ENA | 60m | SHORT | -9,41 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | ENA | 60m | SHORT | -9,41 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | SOL | 60m | SHORT | -7,73 | 4,50 | 0,00 | OPENED | 6,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | 60m | SHORT | -4,82 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — score <7,5 | ETH | 60m | SHORT | -4,82 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — score <7,5 | BTC | 60m | SHORT | -7,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — no HIGH + score <7,5 | BTC | 60m | SHORT | -7,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — Cost Aware | BTC | 60m | SHORT | -7,25 | 6,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — senza Trend Up | BTC | 60m | SHORT | -7,25 | 6,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — score 6–7,5 | BTC | 60m | SHORT | -7,25 | 6,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | NEAR | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | SHORT | -3,90 | 6,00 | 2,10 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,10 | 6,00 | 2,90 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -3,00 | 6,00 | 3,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -2,89 | 6,00 | 3,11 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,63 | 6,00 | 4,37 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -1,50 | 6,00 | 4,50 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -0,91 | 6,00 | 5,09 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DASH | 240m | LONG | 0,69 | 6,00 | 5,31 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -0,35 | 6,00 | 5,65 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,19 | 6,00 | 5,81 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.3 minuti; tolleranza 60 minuti. |
| Rapida V1 — senza PEPE | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — target pieno 2R | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | ENA | 60m | SHORT | -9,41 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | ENA | 60m | SHORT | -9,41 | 4,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | ENA | 60m | SHORT | -9,41 | 5,50 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,14 | -1,84% | €7,58 | €3.000,00 | 0,25% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3391 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,14 | €700,63 | €2.101,90 | €196,32 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 8 | €11.491,29 | €2.928,17 | €5.856,35 | €173,56 | €137,62 |
| TEST | Donchian 1H Gb20 120R V1 | 8 | €11.220,74 | €2.859,23 | €5.718,47 | €169,47 | €134,38 |
| TEST | MAIN — Side × Regime Guard | 6 | €11.043,09 | €706,41 | €2.119,24 | €222,42 | €-78,25 |
| TEST | Rapida score 6–7,5 — Cost Aware | 7 | €11.038,13 | €725,93 | €2.177,78 | €166,69 | €19,85 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.942,98 | €1.156,76 | €2.313,52 | €218,05 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 6 | €10.790,32 | €1.449,24 | €2.898,47 | €167,65 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 5 | €10.736,09 | €4.363,20 | €13.089,61 | €212,22 | €-1,41 |
| TEST | Combo Adaptive — Long Only | 6 | €10.707,02 | €2.330,81 | €4.661,61 | €208,87 | €199,46 |
| TEST | Rapida V1 — senza PEPE | 7 | €10.572,52 | €1.343,54 | €4.030,62 | €211,45 | €-0,02 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.504,01 | €1.589,27 | €4.767,82 | €210,08 | €106,00 |
| TEST | Rapida 1H V2 | 1 | €10.464,00 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 6 | €10.436,53 | €1.579,06 | €4.737,19 | €208,73 | €105,32 |
| TEST | Rapida V3 NoHigh — Regime Guard | 6 | €10.432,02 | €1.181,91 | €3.545,74 | €158,58 | €-0,43 |
| TEST | Combo Adaptive — madre | 8 | €10.364,42 | €1.324,42 | €2.648,84 | €156,29 | €-0,01 |
| TEST | MAIN — Dynamic Asset Selector | 2 | €10.304,83 | €344,54 | €1.033,63 | €101,76 | €-40,04 |
| TEST | Sol Donchian 1H | 1 | €10.301,79 | €1.140,45 | €3.421,36 | €0,00 | €67,22 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €10.269,01 | €1.541,44 | €3.082,88 | €207,77 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.258,16 | €1.100,94 | €2.201,87 | €205,39 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 6 | €10.215,76 | €1.622,59 | €3.245,18 | €154,79 | €5,19 |
| TEST | Scanner Top20 Long | 6 | €10.215,76 | €1.622,59 | €3.245,18 | €154,79 | €5,19 |
| TEST | Btc Bollinger 1H | 1 | €10.205,80 | €1.417,94 | €4.253,83 | €51,05 | €-0,85 |
| TEST | Scanner Top10 Long | 5 | €10.196,28 | €2.296,37 | €4.592,74 | €202,25 | €0,00 |
| TEST | Ampia 4H | 8 | €10.191,65 | €1.010,84 | €2.021,68 | €202,87 | €-0,81 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.174,76 | €1.214,13 | €3.642,39 | €151,63 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.165,98 | €876,12 | €2.628,37 | €51,20 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.164,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.092,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.086,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €10.070,69 | €1.435,23 | €2.870,46 | €155,64 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.064,79 | €1.434,39 | €2.868,78 | €155,55 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €10.059,46 | €515,90 | €1.547,71 | €149,35 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.049,05 | €1.969,94 | €3.939,88 | €151,12 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 6 | €10.048,24 | €614,92 | €1.844,75 | €150,67 | €-0,02 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €10.044,18 | €362,84 | €1.088,52 | €96,64 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.018,94 | €986,59 | €2.959,78 | €0,00 | €58,15 |
| TEST | Sol Adaptive 1H | 1 | €10.015,85 | €987,60 | €2.962,81 | €0,00 | €63,87 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.014,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.994,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.988,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.974,10 | €1.292,04 | €3.876,13 | €0,00 | €53,38 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.970,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.970,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.966,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.959,98 | €1.147,51 | €3.442,53 | €0,00 | €47,41 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.944,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.925,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.917,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 6 | €9.916,79 | €1.079,81 | €2.159,63 | €99,18 | €23,95 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.888,15 | €354,62 | €1.063,86 | €94,46 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €9.868,35 | €1.246,44 | €3.739,31 | €197,37 | €-0,04 |
| TEST | Btc Donchian 4H | 0 | €9.861,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.837,21 | €845,40 | €1.690,80 | €98,36 | €1,07 |
| TEST | Eth Ema 4H | 0 | €9.834,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 5 | €9.814,83 | €1.061,19 | €3.183,56 | €147,48 | €94,05 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 4 | €9.795,42 | €861,15 | €2.583,46 | €145,36 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 5 | €9.790,35 | €1.748,09 | €5.244,28 | €100,25 | €-0,44 |
| TEST | Eth Adaptive 1H | 0 | €9.771,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.767,93 | €1.264,47 | €3.793,40 | €0,00 | €58,93 |
| TEST | Sol Bollinger 1H | 1 | €9.762,43 | €1.124,97 | €3.374,91 | €48,83 | €-0,67 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 5 | €9.748,97 | €1.746,00 | €5.238,01 | €100,25 | €-0,45 |
| TEST | Eth Bollinger 1H | 0 | €9.731,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.715,72 | €1.011,45 | €2.022,91 | €0,00 | €69,08 |
| TEST | Top 5 + BTC — Guard | 5 | €9.680,28 | €998,44 | €1.996,89 | €191,41 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.667,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 6 | €9.653,05 | €1.078,32 | €3.234,95 | €193,06 | €98,60 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.643,02 | €1.108,54 | €3.325,62 | €190,01 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 6 | €9.616,52 | €1.032,07 | €2.064,15 | €192,55 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 5 | €9.570,36 | €1.034,72 | €3.104,16 | €143,80 | €91,70 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.525,20 | €881,41 | €1.762,83 | €147,83 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 5 | €9.518,07 | €884,48 | €1.768,97 | €145,28 | €-0,78 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.512,30 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 5 | €9.507,94 | €883,54 | €1.767,09 | €145,13 | €-0,78 |
| TEST | Btc Ema 1H | 1 | €9.502,77 | €1.091,81 | €3.275,44 | €0,00 | €71,25 |
| TEST | Combo Adaptive — Trend/Transition | 1 | €9.495,26 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.471,17 | €880,13 | €1.760,25 | €144,57 | €-0,78 |
| TEST | Top 5 + BTC — Guard + MFE | 5 | €9.455,16 | €975,22 | €1.950,45 | €186,96 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.406,29 | €1.441,51 | €4.324,53 | €185,30 | €2,79 |
| TEST | Bilanciata 1H V2 | 5 | €9.377,54 | €1.729,35 | €5.188,06 | €96,00 | €67,27 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.369,67 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.346,20 | €868,43 | €1.736,86 | €142,66 | €-0,76 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 6 | €9.260,57 | €850,03 | €1.700,05 | €143,14 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €9.214,28 | €205,67 | €617,01 | €48,38 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.206,35 | €1.863,77 | €3.727,55 | €181,72 | €-30,64 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.187,13 | €981,82 | €1.963,65 | €144,18 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 5 | €9.137,61 | €619,10 | €1.238,19 | €138,02 | €0,00 |
| TEST | Bilanciata 1H V1 | 3 | €9.135,71 | €400,34 | €1.201,03 | €48,28 | €2,95 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 6 | €9.113,03 | €1.425,33 | €2.850,66 | €133,55 | €6,20 |
| TEST | Combo Trend | 5 | €9.075,62 | €1.983,96 | €3.967,91 | €94,84 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 7 | €9.034,08 | €1.121,13 | €2.242,27 | €146,45 | €-0,01 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €8.987,49 | €909,26 | €1.818,52 | €47,26 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 6 | €8.948,64 | €1.098,44 | €2.196,88 | €178,97 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 6 | €8.942,55 | €1.398,70 | €2.797,39 | €131,05 | €6,08 |
| TEST | Rapida V3 — score <7,5 | 5 | €8.911,48 | €2.313,88 | €6.941,63 | €134,13 | €-0,80 |
| TEST | Bilanciata V3 · LONG only | 6 | €8.896,63 | €1.363,40 | €4.090,20 | €175,26 | €2,64 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €8.782,35 | €1.320,60 | €2.641,20 | €132,81 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €8.581,38 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Forza relativa 1H V1 | 8 | €8.571,83 | €2.160,19 | €4.320,38 | €86,57 | €116,55 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €8.566,93 | €1.514,64 | €3.029,28 | €129,61 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 5 | €8.296,94 | €4.716,31 | €9.432,62 | €165,94 | €-9,37 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,14 | €-182,77 | 60 | 60 | 41,67% | 0,88 | €-3,05 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.491,29 | €1.356,07 | 145 | 145 | 43,45% | 1,42 | €9,35 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.220,74 | €1.088,70 | 113 | 113 | 41,59% | 1,47 | €9,63 | 6,75% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €11.043,09 | €1.123,15 | 53 | 53 | 60,38% | 2,36 | €21,19 | 4,04% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.038,13 | €1.019,71 | 202 | 202 | 49,50% | 1,25 | €5,05 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.942,98 | €944,40 | 178 | 178 | 46,63% | 1,30 | €5,31 | 8,85% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.790,32 | €792,30 | 155 | 155 | 50,32% | 1,27 | €5,11 | 10,10% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.736,09 | €745,16 | 148 | 148 | 48,65% | 1,24 | €5,03 | 5,29% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.707,02 | €510,37 | 170 | 170 | 45,88% | 1,17 | €3,00 | 7,78% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.572,52 | €574,78 | 276 | 276 | 44,20% | 1,13 | €2,08 | 9,28% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.504,01 | €400,99 | 219 | 219 | 49,77% | 1,11 | €1,83 | 9,50% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.464,00 | €465,15 | 84 | 75 | 47,62% | 1,22 | €5,54 | 3,89% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.436,53 | €334,16 | 263 | 263 | 44,87% | 1,07 | €1,27 | 9,48% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.432,02 | €434,70 | 152 | 152 | 49,34% | 1,18 | €2,86 | 5,24% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.364,42 | €366,19 | 211 | 211 | 46,45% | 1,11 | €1,74 | 8,17% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.304,83 | €345,60 | 21 | 21 | 42,86% | 1,62 | €16,46 | 3,39% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.301,79 | €236,75 | 20 | 20 | 55,00% | 1,65 | €11,84 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Scanner | Combo Scanner | €10.269,01 | €270,98 | 188 | 188 | 43,62% | 1,08 | €1,44 | 11,38% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.258,16 | €259,52 | 156 | 156 | 44,87% | 1,09 | €1,66 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.215,76 | €212,57 | 203 | 203 | 46,80% | 1,07 | €1,05 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.215,76 | €212,57 | 203 | 203 | 46,80% | 1,07 | €1,05 | 10,31% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.205,80 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.196,28 | €199,04 | 184 | 184 | 46,74% | 1,07 | €1,08 | 10,31% |
| TEST | Ampia 4H | Confluenza trend | €10.191,65 | €193,70 | 56 | 56 | 33,93% | 1,15 | €3,46 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.174,76 | €176,74 | 62 | 62 | 43,55% | 1,12 | €2,85 | 6,49% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.165,98 | €167,36 | 96 | 96 | 43,75% | 1,07 | €1,74 | 7,07% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.164,08 | €164,08 | 18 | 18 | 61,11% | 1,40 | €9,12 | 3,08% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.092,48 | €92,48 | 8 | 8 | 37,50% | 1,42 | €11,56 | 1,75% |
| TEST | Doge Ema 1H | Trend following EMA | €10.086,43 | €86,43 | 27 | 27 | 59,26% | 1,14 | €3,20 | 2,77% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.070,69 | €72,41 | 155 | 155 | 42,58% | 1,02 | €0,47 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.064,79 | €66,52 | 159 | 159 | 42,77% | 1,02 | €0,42 | 12,06% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.059,46 | €60,39 | 253 | 253 | 42,69% | 1,01 | €0,24 | 10,60% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.049,05 | €51,39 | 178 | 178 | 44,38% | 1,02 | €0,29 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.048,24 | €49,36 | 278 | 278 | 39,57% | 1,01 | €0,18 | 6,56% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €10.044,18 | €44,83 | 175 | 175 | 44,00% | 1,01 | €0,26 | 6,64% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Sol Ema 1H | Trend following EMA | €10.018,94 | €-37,32 | 25 | 25 | 40,00% | 0,95 | €-1,49 | 3,33% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.015,85 | €-46,13 | 25 | 25 | 44,00% | 0,94 | €-1,85 | 4,59% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.014,08 | €14,08 | 30 | 30 | 43,33% | 1,10 | €0,47 | 0,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,82 | €2,82 | 30 | 30 | 43,33% | 1,10 | €0,09 | 0,07% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.994,07 | €-5,93 | 4 | 4 | 25,00% | 0,06 | €-1,48 | 0,06% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.988,90 | €-11,10 | 19 | 19 | 36,84% | 0,37 | €-0,58 | 0,15% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.974,10 | €-77,12 | 13 | 13 | 46,15% | 0,77 | €-5,93 | 1,98% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.970,37 | €-29,63 | 4 | 4 | 25,00% | 0,06 | €-7,41 | 0,30% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.970,34 | €-29,66 | 4 | 4 | 25,00% | 0,13 | €-7,42 | 0,30% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.966,58 | €-33,42 | 19 | 19 | 36,84% | 0,66 | €-1,76 | 0,71% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.959,98 | €-85,51 | 10 | 10 | 40,00% | 0,69 | €-8,55 | 1,94% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.944,51 | €-55,49 | 19 | 19 | 36,84% | 0,37 | €-2,92 | 0,77% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.925,44 | €-74,56 | 16 | 16 | 56,25% | 0,82 | €-4,66 | 1,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.917,05 | €-82,95 | 30 | 30 | 43,33% | 0,52 | €-2,77 | 0,84% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.916,79 | €-105,63 | 167 | 167 | 43,11% | 0,97 | €-0,63 | 11,68% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.888,15 | €-111,22 | 174 | 174 | 46,55% | 0,97 | €-0,64 | 8,44% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.868,35 | €-129,65 | 181 | 181 | 44,75% | 0,96 | €-0,72 | 7,10% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.861,10 | €-138,90 | 6 | 6 | 16,67% | 0,49 | €-23,15 | 2,43% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.837,21 | €-162,56 | 142 | 135 | 40,14% | 0,95 | €-1,14 | 10,88% |
| TEST | Eth Ema 4H | Trend following EMA | €9.834,74 | €-165,26 | 8 | 8 | 25,00% | 0,47 | €-20,66 | 1,83% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.814,83 | €-277,32 | 201 | 201 | 40,80% | 0,93 | €-1,38 | 10,86% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.795,42 | €-203,03 | 257 | 257 | 42,02% | 0,96 | €-0,79 | 12,52% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.790,35 | €-206,06 | 166 | 166 | 45,18% | 0,95 | €-1,24 | 15,94% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.771,60 | €-228,40 | 19 | 19 | 42,11% | 0,63 | €-12,02 | 3,14% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.767,93 | €-288,89 | 18 | 18 | 33,33% | 0,56 | €-16,05 | 3,74% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.762,43 | €-234,87 | 17 | 17 | 41,18% | 0,62 | €-13,82 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.748,97 | €-247,44 | 208 | 208 | 42,79% | 0,95 | €-1,19 | 15,64% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.731,13 | €-268,87 | 10 | 10 | 40,00% | 0,38 | €-26,89 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.715,72 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.680,28 | €-319,02 | 148 | 148 | 37,84% | 0,90 | €-2,16 | 7,34% |
| TEST | Eth Ema 1H | Trend following EMA | €9.667,53 | €-332,47 | 28 | 28 | 39,29% | 0,63 | €-11,87 | 4,80% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.653,05 | €-443,49 | 227 | 227 | 42,73% | 0,91 | €-1,95 | 10,92% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.643,02 | €-354,92 | 128 | 128 | 43,75% | 0,84 | €-2,77 | 9,26% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.616,52 | €-382,21 | 148 | 148 | 43,92% | 0,86 | €-2,58 | 12,28% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.570,36 | €-519,48 | 164 | 164 | 39,02% | 0,84 | €-3,17 | 10,86% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.525,20 | €-474,94 | 93 | 93 | 31,18% | 0,82 | €-5,11 | 8,44% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.518,07 | €-481,31 | 110 | 110 | 30,91% | 0,83 | €-4,38 | 8,39% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.512,30 | €-486,49 | 99 | 99 | 38,38% | 0,80 | €-4,91 | 8,88% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.507,94 | €-491,43 | 105 | 105 | 33,33% | 0,82 | €-4,68 | 7,98% |
| TEST | Btc Ema 1H | Trend following EMA | €9.502,77 | €-566,72 | 22 | 22 | 22,73% | 0,34 | €-25,76 | 5,79% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.495,26 | €-503,55 | 88 | 88 | 45,45% | 0,77 | €-5,72 | 6,28% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.471,17 | €-528,21 | 107 | 107 | 32,71% | 0,82 | €-4,94 | 7,80% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.455,16 | €-544,16 | 165 | 165 | 38,79% | 0,84 | €-3,30 | 8,78% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.406,29 | €-594,13 | 208 | 208 | 41,35% | 0,86 | €-2,86 | 14,04% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.377,54 | €-686,01 | 173 | 159 | 43,35% | 0,81 | €-3,97 | 11,82% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,67 | €-629,66 | 88 | 88 | 34,09% | 0,73 | €-7,16 | 7,96% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.346,20 | €-653,20 | 141 | 141 | 42,55% | 0,79 | €-4,63 | 9,02% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.260,57 | €-739,99 | 102 | 102 | 24,51% | 0,74 | €-7,25 | 11,41% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.214,28 | €-785,35 | 146 | 146 | 38,36% | 0,78 | €-5,38 | 9,99% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.206,35 | €-761,05 | 107 | 107 | 32,71% | 0,76 | €-7,11 | 10,13% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.187,13 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.137,61 | €-862,13 | 114 | 114 | 37,72% | 0,72 | €-7,56 | 11,79% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.135,71 | €-866,26 | 181 | 181 | 38,12% | 0,75 | €-4,79 | 15,68% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.113,03 | €-891,42 | 149 | 149 | 35,57% | 0,69 | €-5,98 | 14,10% |
| TEST | Combo Trend | Combo Trend | €9.075,62 | €-921,72 | 192 | 192 | 39,58% | 0,78 | €-4,80 | 14,08% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.034,08 | €-964,58 | 226 | 226 | 41,15% | 0,75 | €-4,27 | 15,45% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €8.987,49 | €-1.011,42 | 54 | 54 | 25,93% | 0,42 | €-18,73 | 12,23% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.948,64 | €-1.050,04 | 82 | 82 | 28,05% | 0,65 | €-12,81 | 13,60% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €8.942,55 | €-1.061,82 | 129 | 129 | 34,88% | 0,59 | €-8,23 | 14,10% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €8.911,48 | €-1.083,55 | 217 | 217 | 39,63% | 0,79 | €-4,99 | 17,41% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €8.896,63 | €-1.103,76 | 162 | 162 | 41,36% | 0,65 | €-6,81 | 13,79% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.782,35 | €-1.216,55 | 141 | 141 | 37,59% | 0,67 | €-8,63 | 13,91% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.581,38 | €-1.417,33 | 65 | 65 | 33,85% | 0,44 | €-21,81 | 16,00% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.571,83 | €-1.542,08 | 156 | 156 | 32,05% | 0,57 | €-9,89 | 19,11% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.566,93 | €-1.431,25 | 115 | 115 | 34,78% | 0,53 | €-12,45 | 16,20% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.296,94 | €-1.687,93 | 118 | 118 | 40,68% | 0,55 | €-14,30 | 19,96% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €2,95 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,13495 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €0,00 |
| Bilanciata 1H V2 | SOPH | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €129,45 | €388,36 | €46,60 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 78718,15322 | 77005,80000 | 77538,04261 | 104563,94686 | 76451,07041 | €1.030,86 | €3.092,57 | €0,00 | €67,27 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €0,00 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €0,00 |
| Bilanciata 1H V3 Filtered | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €109,03 | €327,10 | €39,25 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08578 | 0,08379 | 0,08520 | 0,11395 | 0,08182 | €39,99 | €119,96 | €0,00 | €2,79 |
| Rapida V1 — score 6–7,5 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| Rapida V1 — score 6–7,5 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €0,00 |
| Rapida V1 — score 6–7,5 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,54 | €403,62 | €48,43 | €-0,00 |
| Rapida V1 — score 6–7,5 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,76095 | 0,75170 | 0,76095 | 1,01079 | 0,73449 | €11,60 | €34,80 | €0,00 | €0,42 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 76990,39884 | 77005,80000 | 77852,69131 | 102268,91313 | 75696,96014 | €1.451,26 | €4.353,78 | €48,76 | €-0,87 |
| Rapida score 6–7,5 — senza Trend Up | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,17 | €402,52 | €48,30 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,76095 | 0,75170 | 0,76095 | 1,01079 | 0,73449 | €11,85 | €35,54 | €0,00 | €0,43 |
| Rapida score 6–7,5 — senza Trend Up | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 76990,39884 | 77005,80000 | 77852,69131 | 102268,91313 | 75696,96014 | €1.457,42 | €4.372,25 | €48,97 | €-0,87 |
| Rapida score 6–7,5 — Range Only | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| Rapida score 6–7,5 — Range Only | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| Rapida score 6–7,5 — Range Only | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Range Only | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €138,52 | €415,55 | €49,87 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,40300 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €19,87 |
| Rapida score 6–7,5 — Cost Aware | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €126,49 | €379,47 | €45,54 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 76990,39884 | 77005,80000 | 77852,69131 | 102268,91313 | 75696,96014 | €24,40 | €73,19 | €0,82 | €-0,01 |
| Rapida V1 — no HIGH + score <7,5 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €94,09 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 76990,39884 | 77005,80000 | 77852,69131 | 102268,91313 | 75696,96014 | €56,48 | €169,44 | €1,90 | €-0,03 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| Rapida V1 — senza PEPE | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| Rapida V1 — senza PEPE | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| Rapida V1 — senza PEPE | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| Rapida V1 — senza PEPE | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| Rapida V1 — senza PEPE | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| Rapida V1 — senza PEPE | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €28,16 | €84,49 | €2,23 | €-0,02 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| Rapida V1 — target pieno 2R | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| Rapida V1 — target pieno 2R | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| Rapida V1 — target pieno 2R | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| Rapida V1 — target pieno 2R | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,13927 | €29,67 | €89,02 | €2,35 | €-0,02 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered — madre | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered — madre | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered — madre | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €105,34 |
| Rapida 1H V3 Filtered — madre | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €26,60 | €79,81 | €2,10 | €-0,02 |
| Rapida V3 — score <7,5 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| Rapida V3 — score <7,5 | SOPH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €123,86 | €371,59 | €44,59 | €-0,00 |
| Rapida V3 — score <7,5 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21686 | 0,21686 | 0,22128 | 0,28806 | 0,21022 | €726,90 | €2.180,71 | €44,50 | €-0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 76990,39884 | 77005,80000 | 77852,69131 | 102268,91313 | 75696,96014 | €1.326,59 | €3.979,78 | €44,57 | €-0,80 |
| Rapida V3 — score <7,5 | ETH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 2417,64637 | 2418,13000 | 2444,72401 | 3211,44027 | 2377,02991 | €14,02 | €42,07 | €0,47 | €-0,01 |
| Rapida V3 — no volatilità HIGH | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| Rapida V3 — no volatilità HIGH | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| Rapida V3 — no volatilità HIGH | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €66,30 | €198,91 | €5,24 | €-0,04 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| Rapida V3 — Long Only | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| Rapida V3 — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| Rapida V3 — senza ESPORTS | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| Rapida V3 — senza ESPORTS | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| Rapida V3 — senza ESPORTS | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €98,61 |
| Rapida V3 — senza ESPORTS | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €25,17 | €75,51 | €1,99 | €-0,02 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €106,02 |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €26,78 | €80,33 | €2,12 | €-0,02 |
| Rapida V3 senza ESPORTS — Stress Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| Rapida V3 senza ESPORTS — Stress Guard | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76095 | 0,75170 | 0,76095 | 1,01079 | 0,73449 | €20,61 | €61,84 | €0,00 | €0,75 |
| Rapida V3 senza ESPORTS — Stress Guard | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €679,31 | €2.037,93 | €53,72 | €-0,41 |
| Rapida V3 senza ESPORTS — Stress Guard | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 99,31813 | 99,33800 | 100,65920 | 131,92759 | 97,30653 | €1.326,04 | €3.978,12 | €53,72 | €-0,80 |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 2417,64637 | 2418,13000 | 2444,72401 | 3211,44027 | 2377,02991 | €1.598,20 | €4.794,61 | €53,70 | €-0,96 |
| Rapida V3 — qualità completa + profit lock | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| Rapida V3 — qualità completa + profit lock | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2418,13000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,18 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 80,86500 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,54 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 99,33800 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-1,17 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €73,09 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €0,00 |
| Forza relativa 1H V1 | DOGE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,08578 | 0,08379 | 0,08531 | 0,12825 | 0,08143 | €919,03 | €1.838,05 | €0,00 | €42,70 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,76095 | 0,75170 | 0,78362 | 1,13762 | 0,71106 | €12,54 | €25,08 | €0,75 | €0,30 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 82,37252 | 80,86500 | 81,99029 | 123,14692 | 78,87367 | €12,71 | €25,43 | €0,00 | €0,47 |
| Forza relativa 1H V1 | ENA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,14702 | 0,14705 | 0,15200 | 0,21980 | 0,13606 | €13,53 | €27,06 | €0,92 | €-0,01 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €16,99 | €33,97 | €0,00 | €1,07 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €84,68 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 78821,06263 | 77005,80000 | 77355,77403 | 117837,48864 | 75668,22013 | €123,54 | €247,07 | €0,00 | €5,69 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08578 | 0,08379 | 0,08542 | 0,12825 | 0,08028 | €1.019,54 | €2.039,09 | €0,00 | €47,37 |
| Benchmark Donchian breakout 1H | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,73000 | 59,42929 | 84,57018 | 49,41718 | €19,03 | €38,06 | €1,92 | €-0,11 |
| Benchmark Donchian breakout 1H | ENA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14702 | 0,14705 | 0,15256 | 0,21980 | 0,13318 | €20,62 | €41,24 | €1,55 | €-0,01 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €82,68 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 78821,06263 | 77005,80000 | 77355,77403 | 117837,48864 | 75668,22013 | €120,63 | €241,25 | €0,00 | €5,56 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08578 | 0,08379 | 0,08542 | 0,12825 | 0,08028 | €995,54 | €1.991,08 | €0,00 | €46,26 |
| Donchian 1H Gb20 120R V1 | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,73000 | 59,42929 | 84,57018 | 49,41718 | €18,58 | €37,16 | €1,88 | €-0,11 |
| Donchian 1H Gb20 120R V1 | ENA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14702 | 0,14705 | 0,15256 | 0,21980 | 0,13318 | €20,14 | €40,27 | €1,52 | €-0,01 |
| Benchmark Bollinger mean reversion 1H | DASH | LONG | Bollinger mean reversion | 60m | 2,0x | 57,17143 | 56,73000 | 54,76797 | 28,87157 | 60,77663 | €497,61 | €995,23 | €41,84 | €-7,68 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 77021,20116 | 77005,80000 | 76096,94675 | 38895,70659 | 78407,58278 | €1.660,74 | €3.321,48 | €39,86 | €-0,66 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 99,35787 | 99,33800 | 97,92043 | 50,17572 | 101,51402 | €1.434,45 | €2.868,91 | €41,51 | €-0,57 |
| Benchmark Bollinger mean reversion 1H | HYPE | LONG | Bollinger mean reversion | 60m | 2,0x | 80,88117 | 80,86500 | 79,33006 | 40,84499 | 83,20784 | €1.081,82 | €2.163,64 | €41,49 | €-0,43 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,36071 | 1,36044 | 1,34040 | 0,68716 | 1,39118 | €41,68 | €83,36 | €1,24 | €-0,02 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €0,00 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €0,00 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,40300 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €5,19 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,40300 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €5,19 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €0,00 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €0,00 |
| Top 5 + BTC — solo MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Top 5 + BTC — solo MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Top 5 + BTC — solo MFE | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Top 5 + BTC — solo MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Top 5 + BTC — solo MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €0,00 |
| Top 5 + BTC — solo MFE | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €0,00 |
| Top 5 + BTC — Guard | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Top 5 + BTC — Guard | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Top 5 + BTC — Guard | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Top 5 + BTC — Guard | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Top 5 + BTC — Guard | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €0,00 |
| Top 5 + BTC — BTC≤3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Top 5 + BTC — BTC≤3 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Top 5 + BTC — BTC≤3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €0,00 |
| Top 5 + BTC — BTC≤3 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €433,72 | €867,43 | €41,49 | €0,00 |
| Top 5 + BTC — BTC 2–3 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Top 5 + BTC — BTC 2–3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €0,00 |
| Top 5 + BTC — Guard + MFE | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Top 5 + BTC — Guard + MFE | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Top 5 + BTC — Guard + MFE | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Top 5 + BTC — Guard + MFE | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Top 5 + BTC — Guard + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,17903 | €673,21 | €1.346,41 | €44,12 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €462,02 | €924,05 | €44,20 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €0,00 |
| Top 5 + BTC — target pieno 3R | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Top 5 + BTC — target pieno 3R | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €0,00 |
| Top 5 + BTC — target pieno 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08675 | 0,08379 | 0,08520 | 0,12970 | 0,08158 | €1.011,45 | €2.022,91 | €0,00 | €69,08 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €0,00 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €0,00 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €0,00 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €0,00 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 288,22268 | €105,11 | €210,22 | €8,41 | €0,00 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive — madre | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive — madre | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive — madre | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive — madre | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €0,00 |
| Combo Adaptive — madre | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €0,00 |
| Combo Adaptive — madre | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,51 | €43,01 | €1,22 | €-0,01 |
| Combo Adaptive — MFE Trail esistente | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive — MFE Trail esistente | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive — MFE Trail esistente | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €0,00 |
| Combo Adaptive — MFE Trail esistente | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €29,32 | €58,63 | €1,66 | €-0,01 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive — Quality7 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive — Quality7 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive — Trend/Transition | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive — Long Only | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,40300 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €199,46 |
| Combo Adaptive — Long Only | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive — Long Only | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive — Long Only | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive — Long Only | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €0,00 |
| Combo Adaptive — Long Only | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €0,00 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive — parziale 1R | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive — parziale 1R | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive — parziale 1R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 286,10361 | €49,09 | €98,18 | €3,93 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €536,57 | €1.073,13 | €42,92 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08625 | 0,08379 | 0,08501 | 0,12895 | 0,08064 | €108,53 | €217,05 | €0,00 | €6,20 |
| Combo Adaptive — target pieno 3R | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive — target pieno 3R | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive — target pieno 3R | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €0,00 |
| Combo Adaptive — target pieno 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €0,00 |
| Combo Adaptive — target pieno 3R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €526,53 | €1.053,06 | €42,12 | €0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08625 | 0,08379 | 0,08501 | 0,12895 | 0,08064 | €106,53 | €213,07 | €0,00 | €6,08 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 78718,15322 | 77005,80000 | 77441,70795 | 104563,94686 | 76451,07041 | €1.091,81 | €3.275,44 | €0,00 | €71,25 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 78081,18064 | 77005,80000 | 77398,31624 | 103717,83495 | 76082,30242 | €1.292,04 | €3.876,13 | €0,00 | €53,38 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 77021,20116 | 77005,80000 | 76096,94675 | 51732,57345 | 78407,58278 | €1.417,94 | €4.253,83 | €51,05 | €-0,85 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 78081,18064 | 77005,80000 | 77398,31624 | 103717,83495 | 75832,44264 | €1.147,51 | €3.442,53 | €0,00 | €47,41 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 101,32873 | 99,33800 | 100,01977 | 134,59833 | 97,91799 | €986,59 | €2.959,78 | €0,00 | €58,15 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 101,32873 | 99,33800 | 100,01977 | 134,59833 | 98,29696 | €1.140,45 | €3.421,36 | €0,00 | €67,22 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 99,35787 | 99,33800 | 97,92043 | 66,73537 | 101,51402 | €1.124,97 | €3.374,91 | €48,83 | €-0,67 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 101,52669 | 99,33800 | 100,01766 | 134,86129 | 98,11580 | €987,60 | €2.962,81 | €0,00 | €63,87 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 2456,28864 | 2418,13000 | 2434,98610 | 3262,77008 | 2393,40765 | €1.264,47 | €3.793,40 | €0,00 | €58,93 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €0,00 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1184,18000 | 1170,51942 | 613,98057 | 1306,37049 | €14,96 | €29,92 | €1,11 | €-0,78 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €481,98 | €963,96 | €46,11 | €0,00 |
| Master Adaptive No Alt V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1184,18000 | 1170,51942 | 613,98057 | 1306,37049 | €588,97 | €1.177,95 | €43,87 | €-30,64 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,09236 | €13,27 | €26,55 | €0,87 | €0,00 |
| Master Adaptive Strict3 V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €465,87 | €931,73 | €44,57 | €0,00 |
| Master Adaptive Strict3 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28110 | 0,28110 | 0,24944 | 0,14195 | 0,34441 | €15,82 | €31,64 | €3,56 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €0,00 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1184,18000 | 1170,51942 | 613,98057 | 1306,37049 | €14,65 | €29,29 | €1,09 | €-0,76 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €0,00 |
| Combo Adaptive — Side × Regime Guard | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,40300 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €23,95 |
| Combo Adaptive — Side × Regime Guard | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €0,00 |
| Combo Adaptive — Side × Regime Guard | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1184,18000 | 1170,51942 | 613,98057 | 1306,37049 | €15,03 | €30,07 | €1,12 | €-0,78 |
| Master Adaptive GB20 — 50% a 0,75R | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1184,18000 | 1170,51942 | 613,98057 | 1306,37049 | €15,02 | €30,03 | €1,12 | €-0,78 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,45236 | 0,23694 | 0,51408 | €80,25 | €160,51 | €5,76 | €0,00 |
| Rapida V3 NoHigh — Range Only | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| Rapida V3 NoHigh — Range Only | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14702 | 0,14705 | 0,15090 | 0,19529 | 0,14121 | €659,65 | €1.978,95 | €52,17 | €-0,40 |
| Rapida V3 NoHigh — Regime Guard | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 99,31813 | 99,33800 | 100,65920 | 131,92759 | 97,30653 | €64,64 | €193,91 | €2,62 | €-0,04 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,14705 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €-39,32 |
| MAIN — Side × Regime Guard | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| MAIN — Side × Regime Guard | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1248,87973 | 1184,18000 | 1152,08799 | 838,83088 | 1442,46321 | €239,17 | €717,51 | €55,61 | €-37,17 |
| MAIN — Side × Regime Guard | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,49550 | 2,40300 | 2,26921 | 1,67614 | 2,94807 | €15,83 | €47,48 | €4,31 | €-1,76 |
| MAIN — Dynamic Asset Selector | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,14705 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €-36,84 |
| MAIN — Dynamic Asset Selector | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1190,40803 | 1184,18000 | 1090,98250 | 799,55740 | 1389,25911 | €203,57 | €610,70 | €51,01 | €-3,20 |
| Combo Trend — Side × Regime Guard | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend — Side × Regime Guard | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend — Side × Regime Guard | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend — Side × Regime Guard | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €0,00 |
| Combo Trend — Side × Regime Guard | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,09542 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €0,00 |
| Combo Trend — Side × Regime Guard | TAO | LONG | Combo Trend | 60m | 2,0x | 264,91297 | 264,91297 | 253,14039 | 133,78105 | 290,81264 | €73,76 | €147,52 | €6,56 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €91,74 |
| FAST NoHigh <7,5 · SHORT only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 76990,39884 | 77005,80000 | 77852,69131 | 102268,91313 | 75696,96014 | €55,07 | €165,21 | €1,85 | €-0,03 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| Bilanciata V3 · LONG only | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €0,00 |
| Bilanciata V3 · LONG only | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €0,00 |
| Bilanciata V3 · LONG only | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €103,13 | €309,38 | €37,13 | €-0,00 |
| Bilanciata V3 · LONG only | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08578 | 0,08379 | 0,08520 | 0,11395 | 0,08182 | €37,82 | €113,46 | €0,00 | €2,64 |
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
| FAST NoHigh <7,5 · SHORT only | HYPE | SHORT | 2026-09-10T13:00:00+00:00 | 80,53317 | €1,09 | 1,41 | TARGET |
| FAST NoHigh <7,5 · SHORT only | DOGE | SHORT | 2026-09-10T13:00:00+00:00 | 0,08409 | €0,72 | 1,42 | TARGET |
| Rapida V3 NoHigh — Regime Guard | HYPE | SHORT | 2026-09-10T13:00:00+00:00 | 80,53317 | €0,55 | 1,41 | TARGET |
| Rapida V3 NoHigh — Regime Guard | BTC | SHORT | 2026-09-10T13:00:00+00:00 | 76784,77069 | €71,48 | 1,38 | TARGET |
| Rapida V3 NoHigh — Regime Guard | DOGE | SHORT | 2026-09-10T12:45:00+00:00 | 0,08460 | €2,19 | 1,43 | TARGET |
| Rapida V3 NoHigh — Range Only | DOGE | SHORT | 2026-09-10T12:45:00+00:00 | 0,08460 | €72,20 | 1,43 | TARGET |
| Master Adaptive GB20 — Loss Cap 0,75R | ZEC | LONG | 2026-09-10T13:00:00+00:00 | 1181,60398 | €-1,18 | -1,04 | STOP |
| Combo Adaptive — Side × Regime Guard | SOL | SHORT | 2026-09-10T13:00:00+00:00 | 98,60559 | €0,82 | 1,91 | TARGET |
| Master Adaptive Runner25 V1 | ZEC | LONG | 2026-09-10T13:00:00+00:00 | 1203,23758 | €-45,19 | -1,04 | STOP |
| Doge Bollinger 1H | DOGE | LONG | 2026-09-10T12:45:00+00:00 | 0,08471 | €-53,98 | -1,08 | STOP |
| Doge Donchian 1H | DOGE | SHORT | 2026-09-10T13:00:00+00:00 | 0,08228 | €97,56 | 1,94 | TARGET |
| Doge Ema 1H | DOGE | SHORT | 2026-09-10T13:00:00+00:00 | 0,08253 | €96,97 | 1,94 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 748/30 | 33/30 | 0,90 | 2,04 | -0,05R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 699/30 | 20/30 | 0,87 | 1,90 | -0,07R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 357/30 | 22/30 | 0,94 | 1,74 | -0,03R | €12,35 | 1,72% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 363/30 | 22/30 | 0,90 | 1,57 | -0,05R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 656/30 | 31/30 | 0,96 | 0,62 | -0,02R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 608/30 | 11/30 | 0,94 | 0,00 | -0,03R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 213/30 | 8/30 | 0,93 | 1,02 | -0,04R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 481/30 | 17/30 | 0,85 | 4,50 | -0,08R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 674/30 | 24/30 | 0,83 | 0,64 | -0,08R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 624/30 | 7/30 | 0,75 | 0,02 | -0,13R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 656/30 | 30/30 | 0,97 | 1,02 | -0,01R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 1063/30 | 55/30 | 0,91 | 1,12 | -0,04R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 257/30 | 15/30 | 0,74 | 0,99 | -0,15R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 929/30 | 44/30 | 0,86 | 1,20 | -0,07R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 933/30 | 37/30 | 0,86 | 0,76 | -0,07R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 866/30 | 23/30 | 0,80 | 1,12 | -0,10R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 420/30 | 60/30 | 0,83 | 0,88 | -0,10R | €-3,05 | 6,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 21/30 | 0,00 | 1,62 | 0,00R | €16,46 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 53/30 | 0,00 | 2,36 | 0,00R | €21,19 | 4,04% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 34/30 | 19/30 | 0,45 | 0,66 | -0,28R | €-1,76 | 0,71% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 53/30 | 30/30 | 0,63 | 0,52 | -0,20R | €-2,77 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 1078/30 | 181/30 | 0,90 | 0,75 | -0,05R | €-4,79 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 128/30 | 0,00 | 0,84 | 0,00R | €-2,77 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 375/30 | 159/30 | 1,11 | 0,81 | 0,06R | €-3,97 | 11,82% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 693/30 | 208/30 | 0,97 | 0,86 | -0,01R | €-2,86 | 14,04% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 614/30 | 162/30 | 0,92 | 0,65 | -0,04R | €-6,81 | 13,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 357/30 | 146/30 | 0,86 | 0,78 | -0,07R | €-5,38 | 9,99% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 718/30 | 164/30 | 0,90 | 0,84 | -0,05R | €-3,17 | 10,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 785/30 | 201/30 | 0,92 | 0,93 | -0,04R | €-1,38 | 10,86% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1224/30 | 276/30 | 0,86 | 1,13 | -0,07R | €2,08 | 9,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 202/30 | 0,00 | 1,25 | 0,00R | €5,05 | 7,95% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 166/30 | 0,00 | 0,95 | 0,00R | €-1,24 | 15,94% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 62/30 | 0,00 | 1,12 | 0,00R | €2,85 | 6,49% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 697/30 | 208/30 | 0,95 | 0,95 | -0,03R | €-1,19 | 15,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1172/30 | 278/30 | 0,84 | 1,01 | -0,08R | €0,18 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 100/30 | 75/30 | 0,95 | 1,22 | -0,03R | €5,54 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 1128/30 | 263/30 | 0,89 | 1,07 | -0,06R | €1,27 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 852/30 | 217/30 | 0,92 | 0,79 | -0,04R | €-4,99 | 17,41% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 406/30 | 174/30 | 1,01 | 0,97 | 0,00R | €-0,64 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 412/30 | 175/30 | 0,96 | 1,01 | -0,02R | €0,26 | 6,64% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 747/30 | 257/30 | 0,96 | 0,96 | -0,02R | €-0,79 | 12,52% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 96/30 | 0,00 | 1,07 | 0,00R | €1,74 | 7,07% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 152/30 | 0,00 | 1,18 | 0,00R | €2,86 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 805/30 | 181/30 | 0,87 | 0,96 | -0,06R | €-0,72 | 7,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 253/30 | 0,00 | 1,01 | 0,00R | €0,24 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 219/30 | 0,00 | 1,11 | 0,00R | €1,83 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 148/30 | 0,00 | 1,24 | 0,00R | €5,03 | 5,29% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 1081/30 | 227/30 | 0,87 | 0,91 | -0,07R | €-1,95 | 10,92% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 387/30 | 56/30 | 0,86 | 1,15 | -0,09R | €3,46 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 371/30 | 118/30 | 1,12 | 0,55 | 0,05R | €-14,30 | 19,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 16/30 | 10/30 | 0,56 | 0,69 | -0,25R | €-8,55 | 1,94% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 4/30 | 4/30 | 0,76 | 0,77 | -0,19R | €-8,79 | 1,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 9/30 | 6/30 | 3,40 | 4,66 | 0,60R | €34,87 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 4/30 | 4/30 | 2,81 | 2,86 | 0,50R | €25,47 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 20/30 | 13/30 | 0,33 | 0,77 | -0,50R | €-5,93 | 1,98% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 8/30 | 6/30 | 0,36 | 0,49 | -0,60R | €-23,15 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 28/30 | 22/30 | 0,48 | 0,34 | -0,37R | €-25,76 | 5,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 6/30 | 5/30 | 0,45 | 0,58 | -0,49R | €-17,17 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 888/30 | 211/30 | 0,97 | 1,11 | -0,01R | €1,74 | 8,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 579/30 | 170/30 | 1,02 | 1,17 | 0,01R | €3,00 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 991/30 | 226/30 | 0,99 | 0,75 | -0,01R | €-4,27 | 15,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 829/30 | 178/30 | 0,94 | 1,02 | -0,03R | €0,29 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 102/30 | 58/30 | 1,37 | 0,95 | 0,16R | €-1,12 | 4,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 102/30 | 58/30 | 1,33 | 0,86 | 0,14R | €-3,27 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 311/30 | 99/30 | 0,93 | 0,80 | -0,04R | €-4,91 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 284/30 | 88/30 | 1,00 | 0,77 | -0,00R | €-5,72 | 6,28% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 149/30 | 0,74 | 0,69 | -0,20R | €-5,98 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 167/30 | 0,00 | 0,97 | 0,00R | €-0,63 | 11,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 129/30 | 0,74 | 0,59 | -0,20R | €-8,23 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 138/30 | 65/30 | 0,99 | 0,44 | -0,00R | €-21,81 | 16,00% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 580/30 | 188/30 | 1,05 | 1,08 | 0,03R | €1,44 | 11,38% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 742/30 | 192/30 | 0,96 | 0,78 | -0,02R | €-4,80 | 14,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 155/30 | 0,00 | 1,27 | 0,00R | €5,11 | 10,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 19/30 | 16/30 | 1,54 | 0,82 | 0,19R | €-4,66 | 1,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 23/30 | 18/30 | 0,79 | 1,40 | -0,13R | €9,12 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 39/30 | 27/30 | 0,58 | 1,14 | -0,27R | €3,20 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 393/30 | 145/30 | 0,86 | 1,42 | -0,09R | €9,35 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 323/30 | 113/30 | 0,85 | 1,47 | -0,09R | €9,63 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 754/30 | 158/30 | 0,92 | 0,71 | -0,04R | €-5,14 | 12,31% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 28/30 | 19/30 | 0,55 | 0,63 | -0,32R | €-12,02 | 3,14% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 19/30 | 10/30 | 2,00 | 0,38 | 0,35R | €-26,89 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 26/30 | 18/30 | 0,47 | 0,56 | -0,39R | €-16,05 | 3,74% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 42/30 | 28/30 | 0,48 | 0,63 | -0,36R | €-11,87 | 4,80% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 7/30 | 8/30 | 0,49 | 0,47 | -0,31R | €-20,66 | 1,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 18/30 | 21/30 | 0,85 | 0,46 | -0,09R | €-16,79 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 390/30 | 88/30 | 1,09 | 0,73 | 0,06R | €-7,16 | 7,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 110/30 | 0,00 | 0,83 | 0,00R | €-4,38 | 8,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 102/30 | 0,00 | 0,74 | 0,00R | €-7,25 | 11,41% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 105/30 | 0,00 | 0,82 | 0,00R | €-4,68 | 7,98% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 746/30 | 141/30 | 1,30 | 0,79 | 0,10R | €-4,63 | 9,02% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 324/30 | 107/30 | 1,07 | 0,76 | 0,05R | €-7,11 | 10,13% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 358/30 | 93/30 | 1,11 | 0,82 | 0,07R | €-5,11 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 230/30 | 82/30 | 0,97 | 0,65 | -0,02R | €-12,81 | 13,60% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 374/30 | 107/30 | 1,09 | 0,82 | 0,05R | €-4,94 | 7,80% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 900/30 | 156/30 | 0,90 | 0,57 | -0,05R | €-9,89 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 355/30 | 135/30 | 1,11 | 0,95 | 0,06R | €-1,14 | 10,88% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 283/30 | 70/30 | 0,55 | 0,65 | -0,26R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 283/30 | 70/30 | 0,55 | 0,65 | -0,26R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 283/30 | 70/30 | 0,55 | 0,65 | -0,26R | €-9,68 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 310/30 | 89/30 | 0,65 | 0,64 | -0,19R | €-9,30 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 343/30 | 61/30 | 0,75 | 0,58 | -0,11R | €-12,17 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 309/30 | 62/30 | 0,68 | 0,56 | -0,14R | €-12,20 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 588/30 | 184/30 | 0,99 | 1,07 | -0,01R | €1,08 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 590/30 | 203/30 | 0,99 | 1,07 | -0,00R | €1,05 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 590/30 | 203/30 | 0,99 | 1,07 | -0,00R | €1,05 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 559/30 | 156/30 | 1,06 | 1,09 | 0,03R | €1,66 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 203/30 | 54/30 | 0,70 | 0,42 | -0,18R | €-18,73 | 12,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 414/30 | 115/30 | 0,85 | 0,53 | -0,08R | €-12,45 | 16,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 440/30 | 141/30 | 1,04 | 0,67 | 0,02R | €-8,63 | 13,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 369/30 | 114/30 | 0,91 | 0,72 | -0,05R | €-7,56 | 11,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 570/30 | 165/30 | 1,12 | 0,84 | 0,05R | €-3,30 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 468/30 | 148/30 | 1,05 | 0,90 | 0,03R | €-2,16 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 635/30 | 148/30 | 1,04 | 0,86 | 0,02R | €-2,58 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 506/30 | 159/30 | 1,01 | 1,02 | 0,00R | €0,42 | 12,06% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 479/30 | 155/30 | 1,03 | 1,02 | 0,01R | €0,47 | 11,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 612/30 | 178/30 | 1,07 | 1,30 | 0,04R | €5,31 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 39/30 | 25/30 | 0,79 | 0,94 | -0,14R | €-1,85 | 4,59% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 11/30 | 10/30 | 1,54 | 1,64 | 0,26R | €13,87 | 1,37% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 28/30 | 17/30 | 0,79 | 0,62 | -0,12R | €-13,82 | 2,91% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 6/30 | 5/30 | 2,48 | 0,88 | 0,51R | €-3,80 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 31/30 | 20/30 | 0,98 | 1,65 | -0,01R | €11,84 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 9/30 | 8/30 | 0,84 | 1,42 | -0,11R | €11,56 | 1,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 38/30 | 25/30 | 0,83 | 0,95 | -0,12R | €-1,49 | 3,33% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 12/30 | 11/30 | 0,64 | 1,02 | -0,25R | €0,50 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08379**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 35.3 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 77005.8 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, volume_valid, stop_within_limit**
- High **0.08464**; close **0.0837**; wick alta **0.8%**; volume **x9.51**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=517; LEGACY_RESEARCH_EVIDENCE_V3=12782; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_DOWN**
- Famiglia: **ALT_ROTATION**
- Confidenza: **90,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -4.32%, 91% sotto -1%.
- BTC trend score: **-2,00**; ADX: **18,38**; breadth sopra EMA50: **0,00%**
- Mediana alt vs BTC: **-4,32%**; dispersione: **2,41%**

- Aperti in questo ciclo: **157**
- Chiusi in questo ciclo: **173**
- Posizioni research aperte: **1078**
- Trade research chiusi: **45053**
- Eventi di mercato indipendenti chiusi: **6019**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **122169**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 15 | 748 | 748 | 36,90% | 0,90 | -0,05R | €-358,64 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 18 | 699 | 699 | 36,34% | 0,87 | -0,07R | €-463,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 2 | 357 | 357 | 47,90% | 0,94 | -0,03R | €-111,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 2 | 363 | 363 | 37,19% | 0,90 | -0,05R | €-185,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 5 | 656 | 656 | 37,80% | 0,96 | -0,02R | €-143,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 5 | 608 | 608 | 37,99% | 0,94 | -0,03R | €-167,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 3 | 213 | 213 | 38,03% | 0,93 | -0,04R | €-75,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 17 | 481 | 481 | 34,93% | 0,85 | -0,08R | €-376,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 19 | 674 | 674 | 34,42% | 0,83 | -0,08R | €-569,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 19 | 624 | 624 | 33,17% | 0,75 | -0,13R | €-795,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 5 | 656 | 656 | 38,11% | 0,97 | -0,01R | €-83,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 20 | 1063 | 1063 | 40,73% | 0,91 | -0,04R | €-421,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 10 | 257 | 257 | 37,74% | 0,74 | -0,15R | €-389,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 21 | 929 | 929 | 34,88% | 0,86 | -0,07R | €-671,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 21 | 933 | 933 | 34,83% | 0,86 | -0,07R | €-671,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 21 | 866 | 866 | 34,06% | 0,80 | -0,10R | €-863,18 |
| MAIN | 22 | 420 | 420 | 31,19% | 0,83 | -0,10R | €-413,65 |
| RSI_EXTREME_LONG_15M | 0 | 34 | 34 | 41,18% | 0,45 | -0,28R | €-96,79 |
| RSI_EXTREME_SHORT_15M | 0 | 53 | 53 | 37,74% | 0,63 | -0,20R | €-104,96 |
| Bilanciata 1H V1 | 30 | 1078 | 1078 | 37,11% | 0,90 | -0,05R | €-561,81 |
| Bilanciata 1H V2 | 10 | 431 | 375 | 41,76% | 1,11 | 0,06R | €240,38 |
| Bilanciata 1H V3 Filtered | 18 | 693 | 693 | 38,82% | 0,97 | -0,01R | €-101,56 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 18 | 614 | 614 | 38,76% | 0,92 | -0,04R | €-246,91 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 357 | 357 | 37,54% | 0,86 | -0,07R | €-252,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 16 | 718 | 718 | 37,74% | 0,90 | -0,05R | €-349,88 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 16 | 785 | 785 | 38,22% | 0,92 | -0,04R | €-315,54 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 23 | 1224 | 1224 | 37,17% | 0,86 | -0,07R | €-849,31 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 12 | 697 | 697 | 39,45% | 0,95 | -0,03R | €-182,44 |
| SHADOW_1H_FAST_TP2_V1 | 24 | 1172 | 1172 | 34,81% | 0,84 | -0,08R | €-947,60 |
| Rapida 1H V2 | 0 | 115 | 100 | 44,35% | 0,95 | -0,03R | €-30,63 |
| Rapida 1H V3 Filtered | 21 | 1128 | 1128 | 37,68% | 0,89 | -0,06R | €-646,65 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 15 | 852 | 852 | 39,32% | 0,92 | -0,04R | €-332,90 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 406 | 406 | 48,77% | 1,01 | 0,00R | €12,94 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 412 | 412 | 39,56% | 0,96 | -0,02R | €-82,44 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 5 | 747 | 747 | 40,03% | 0,96 | -0,02R | €-132,61 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 19 | 805 | 805 | 37,02% | 0,87 | -0,06R | €-518,30 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 21 | 1081 | 1081 | 37,28% | 0,87 | -0,07R | €-728,61 |
| SHADOW_4H_WIDE | 34 | 387 | 387 | 25,06% | 0,86 | -0,09R | €-345,47 |
| SHADOW_BOLLINGER_MR_1H | 6 | 371 | 371 | 49,33% | 1,12 | 0,05R | €201,93 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 16 | 16 | 43,75% | 0,56 | -0,25R | €-39,21 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 4 | 4 | 25,00% | 0,76 | -0,19R | €-7,44 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 9 | 9 | 77,78% | 3,40 | 0,60R | €54,38 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 4 | 4 | 75,00% | 2,81 | 0,50R | €19,94 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 20 | 20 | 30,00% | 0,33 | -0,50R | €-99,02 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 8 | 8 | 12,50% | 0,36 | -0,60R | €-47,77 |
| SHADOW_BTC_EMA_1H | 1 | 28 | 28 | 35,71% | 0,48 | -0,37R | €-103,82 |
| SHADOW_BTC_EMA_4H | 0 | 6 | 6 | 16,67% | 0,45 | -0,49R | €-29,19 |
| SHADOW_COMBO_ADAPTIVE | 27 | 888 | 888 | 39,86% | 0,97 | -0,01R | €-125,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 11 | 579 | 579 | 41,28% | 1,02 | 0,01R | €57,88 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 26 | 991 | 991 | 40,97% | 0,99 | -0,01R | €-57,59 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 27 | 829 | 829 | 41,86% | 0,94 | -0,03R | €-241,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 102 | 102 | 49,02% | 1,37 | 0,16R | €159,66 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 102 | 102 | 44,12% | 1,33 | 0,14R | €140,93 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 15 | 311 | 311 | 38,59% | 0,93 | -0,04R | €-118,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 1 | 284 | 284 | 40,85% | 1,00 | -0,00R | €-6,04 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 138 | 138 | 45,65% | 0,99 | -0,00R | €-3,47 |
| SHADOW_COMBO_SCANNER | 11 | 580 | 580 | 38,97% | 1,05 | 0,03R | €158,08 |
| SHADOW_COMBO_TREND | 26 | 742 | 742 | 36,93% | 0,96 | -0,02R | €-155,31 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 19 | 19 | 63,16% | 1,54 | 0,19R | €36,19 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 23 | 23 | 43,48% | 0,79 | -0,13R | €-29,94 |
| SHADOW_DOGE_EMA_1H | 1 | 39 | 39 | 33,33% | 0,58 | -0,27R | €-105,57 |
| SHADOW_DONCHIAN_1H | 16 | 393 | 393 | 34,35% | 0,86 | -0,09R | €-350,08 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 16 | 323 | 323 | 36,22% | 0,85 | -0,09R | €-285,00 |
| SHADOW_EMA_TREND_1H | 26 | 754 | 754 | 36,07% | 0,92 | -0,04R | €-325,38 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 28 | 28 | 35,71% | 0,55 | -0,32R | €-88,89 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 19 | 19 | 63,16% | 2,00 | 0,35R | €66,89 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 26 | 26 | 30,77% | 0,47 | -0,39R | €-101,67 |
| SHADOW_ETH_EMA_1H | 0 | 42 | 42 | 35,71% | 0,48 | -0,36R | €-150,20 |
| SHADOW_ETH_EMA_4H | 0 | 7 | 7 | 42,86% | 0,49 | -0,31R | €-21,53 |
| SHADOW_GLOBAL_PURE | 1 | 18 | 18 | 44,44% | 0,85 | -0,09R | €-16,16 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 12 | 390 | 390 | 34,87% | 1,09 | 0,06R | €224,63 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 746 | 746 | 66,22% | 1,30 | 0,10R | €712,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 10 | 324 | 324 | 34,26% | 1,07 | 0,05R | €149,80 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 12 | 358 | 358 | 34,36% | 1,11 | 0,07R | €240,97 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 230 | 230 | 32,17% | 0,97 | -0,02R | €-42,07 |
| SHADOW_MASTER_ADAPTIVE_V1 | 12 | 374 | 374 | 34,76% | 1,09 | 0,05R | €202,90 |
| Forza relativa 1H V1 | 31 | 900 | 900 | 33,78% | 0,90 | -0,05R | €-486,20 |
| Forza relativa 1H V2 | 19 | 382 | 355 | 38,48% | 1,11 | 0,06R | €217,45 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 18 | 283 | 283 | 28,98% | 0,55 | -0,26R | €-723,82 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 18 | 283 | 283 | 28,98% | 0,55 | -0,26R | €-723,82 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 18 | 283 | 283 | 28,98% | 0,55 | -0,26R | €-723,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 14 | 310 | 310 | 30,00% | 0,65 | -0,19R | €-600,44 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 14 | 343 | 343 | 53,06% | 0,75 | -0,11R | €-385,20 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 13 | 309 | 309 | 52,43% | 0,68 | -0,14R | €-437,53 |
| SHADOW_SCANNER_TOP10_LONG | 11 | 588 | 588 | 40,14% | 0,99 | -0,01R | €-32,03 |
| SHADOW_SCANNER_TOP15_LONG | 11 | 590 | 590 | 40,17% | 0,99 | -0,00R | €-28,51 |
| SHADOW_SCANNER_TOP20_LONG | 11 | 590 | 590 | 40,17% | 0,99 | -0,00R | €-28,51 |
| SHADOW_SCANNER_TOP5_BTC | 11 | 559 | 559 | 38,64% | 1,06 | 0,03R | €164,31 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 5 | 203 | 203 | 31,03% | 0,70 | -0,18R | €-370,91 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 10 | 414 | 414 | 34,78% | 0,85 | -0,08R | €-348,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 9 | 440 | 440 | 42,95% | 1,04 | 0,02R | €75,80 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 9 | 369 | 369 | 36,31% | 0,91 | -0,05R | €-181,41 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 10 | 570 | 570 | 44,21% | 1,12 | 0,05R | €291,59 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 10 | 468 | 468 | 39,53% | 1,05 | 0,03R | €133,44 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 11 | 635 | 635 | 42,99% | 1,04 | 0,02R | €105,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 11 | 506 | 506 | 37,94% | 1,01 | 0,00R | €17,16 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 11 | 479 | 479 | 37,58% | 1,03 | 0,01R | €63,53 |
| SHADOW_SCANNER_TOP5_LONG | 11 | 612 | 612 | 40,03% | 1,07 | 0,04R | €222,32 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 39 | 39 | 38,46% | 0,79 | -0,14R | €-55,78 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 11 | 11 | 54,55% | 1,54 | 0,26R | €28,27 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 28 | 28 | 50,00% | 0,79 | -0,12R | €-32,74 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 6 | 6 | 66,67% | 2,48 | 0,51R | €30,82 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 31 | 31 | 45,16% | 0,98 | -0,01R | €-3,19 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 9 | 9 | 33,33% | 0,84 | -0,11R | €-9,79 |
| SHADOW_SOL_EMA_1H | 1 | 38 | 38 | 36,84% | 0,83 | -0,12R | €-45,58 |
| SHADOW_SOL_EMA_4H | 0 | 12 | 12 | 33,33% | 0,64 | -0,25R | €-30,53 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 7 | 98 | 98 | 30,61% | 0,65 | -0,20R | €-194,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 3 | 210 | 210 | 43,81% | 1,03 | 0,02R | €34,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 4 | 177 | 177 | 38,98% | 0,92 | -0,04R | €-70,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,23R | €-49,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 7 | 7 | 71,43% | 2,09 | 0,32R | €22,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 68 | 68 | 36,76% | 1,38 | 0,16R | €105,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 68 | 68 | 20,59% | 0,43 | -0,31R | €-208,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 10 | 89 | 89 | 28,09% | 0,47 | -0,33R | €-292,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 3 | 191 | 191 | 42,41% | 1,02 | 0,01R | €16,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 4 | 170 | 170 | 38,82% | 0,86 | -0,07R | €-119,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,57 | -0,25R | €-50,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 5,17 | 0,70R | €42,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 67 | 67 | 37,31% | 1,37 | 0,15R | €99,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 64 | 64 | 23,44% | 0,45 | -0,30R | €-189,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 12 | 12 | 41,67% | 0,62 | -0,24R | €-28,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 115 | 115 | 47,83% | 0,96 | -0,02R | €-24,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 100 | 100 | 45,00% | 0,81 | -0,11R | €-108,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 42 | 42 | 64,29% | 2,20 | 0,39R | €163,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 52 | 52 | 42,31% | 0,69 | -0,16R | €-85,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,66 | -0,20R | €-21,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 118 | 118 | 38,98% | 0,87 | -0,07R | €-83,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 1 | 104 | 104 | 41,35% | 0,88 | -0,06R | €-64,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 42 | 42 | 38,10% | 1,86 | 0,26R | €109,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 52 | 52 | 26,92% | 0,64 | -0,17R | €-87,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 31,82% | 0,77 | -0,10R | €-42,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 3 | 249 | 249 | 38,96% | 0,84 | -0,08R | €-203,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 1 | 132 | 132 | 40,91% | 1,00 | 0,00R | €1,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 72 | 72 | 30,56% | 0,72 | -0,14R | €-101,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 43 | 43 | 32,56% | 0,76 | -0,10R | €-43,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 3 | 228 | 228 | 38,16% | 0,85 | -0,08R | €-184,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 1 | 119 | 119 | 42,86% | 1,01 | 0,01R | €6,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 57 | 57 | 42,11% | 1,81 | 0,26R | €145,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 66 | 66 | 31,82% | 0,62 | -0,19R | €-124,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 3 | 209 | 209 | 37,80% | 0,93 | -0,04R | €-75,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 12 | 35 | 35 | 34,29% | 0,69 | -0,20R | €-70,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 2 | 139 | 139 | 35,97% | 0,77 | -0,13R | €-179,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 3 | 184 | 184 | 38,59% | 0,98 | -0,01R | €-17,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 50 | 50 | 36,00% | 1,35 | 0,14R | €69,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 12 | 59 | 59 | 32,20% | 0,73 | -0,15R | €-89,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 2 | 150 | 150 | 36,67% | 0,80 | -0,11R | €-166,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 4 | 221 | 221 | 38,01% | 0,93 | -0,04R | €-78,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 68 | 68 | 33,82% | 1,20 | 0,08R | €53,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 89 | 89 | 25,84% | 0,61 | -0,20R | €-180,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 12 | 54 | 54 | 27,78% | 0,54 | -0,29R | €-154,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 2 | 134 | 134 | 34,33% | 0,73 | -0,16R | €-211,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 4 | 208 | 208 | 37,50% | 0,87 | -0,06R | €-124,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 67 | 67 | 34,33% | 1,14 | 0,05R | €36,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 83 | 83 | 26,51% | 0,52 | -0,25R | €-209,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 31,82% | 0,77 | -0,10R | €-42,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 3 | 250 | 250 | 39,20% | 0,86 | -0,07R | €-183,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 1 | 132 | 132 | 42,42% | 1,09 | 0,05R | €60,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 72 | 72 | 30,56% | 0,72 | -0,14R | €-101,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 12 | 148 | 148 | 38,51% | 0,70 | -0,15R | €-220,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 3 | 299 | 299 | 40,80% | 0,92 | -0,04R | €-112,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 4 | 248 | 248 | 41,53% | 1,01 | 0,00R | €9,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 32 | 32 | 34,38% | 0,58 | -0,23R | €-73,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 8 | 8 | 50,00% | 0,84 | -0,08R | €-6,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 88 | 88 | 47,73% | 1,61 | 0,18R | €161,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 102 | 102 | 38,24% | 0,71 | -0,14R | €-147,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 9 | 37 | 37 | 37,84% | 0,82 | -0,12R | €-43,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 65 | 65 | 33,85% | 0,64 | -0,23R | €-150,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 1 | 93 | 93 | 43,01% | 0,84 | -0,08R | €-77,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 15 | 15 | 60,00% | 1,97 | 0,42R | €63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 33 | 33 | 21,21% | 0,31 | -0,50R | €-164,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 12 | 123 | 123 | 28,46% | 0,61 | -0,21R | €-259,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 4 | 262 | 262 | 38,93% | 0,87 | -0,07R | €-175,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 4 | 217 | 217 | 37,79% | 0,92 | -0,04R | €-84,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 88 | 88 | 25,00% | 0,57 | -0,23R | €-200,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 12 | 123 | 123 | 28,46% | 0,61 | -0,21R | €-259,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 4 | 264 | 264 | 39,02% | 0,88 | -0,06R | €-165,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 4 | 218 | 218 | 37,61% | 0,91 | -0,04R | €-94,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,59 | -0,22R | €-71,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 88 | 88 | 25,00% | 0,57 | -0,23R | €-200,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 12 | 114 | 114 | 27,19% | 0,52 | -0,27R | €-313,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 4 | 239 | 239 | 38,08% | 0,86 | -0,08R | €-183,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 4 | 206 | 206 | 36,89% | 0,82 | -0,09R | €-175,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 28 | 28 | 25,00% | 0,63 | -0,20R | €-56,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,45 | 0,17R | €133,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 82 | 82 | 25,61% | 0,47 | -0,29R | €-234,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 4 | 37 | 37 | 29,73% | 0,82 | -0,10R | €-36,29 |
| MAIN | ALT_ROTATION_UP | 4 | 111 | 111 | 31,53% | 0,66 | -0,22R | €-239,59 |
| MAIN | RANGE | 6 | 95 | 95 | 29,47% | 0,81 | -0,11R | €-101,52 |
| MAIN | RANGE_HIGH_VOL | 1 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 3 | 42 | 42 | 30,95% | 0,85 | -0,08R | €-34,43 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 2 | 48 | 48 | 29,17% | 0,93 | -0,04R | €-19,03 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 19 | 19 | 36,84% | 0,17 | -0,51R | €-97,72 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 25 | 25 | 44,00% | 0,92 | -0,04R | €-9,44 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 13 | 121 | 121 | 27,27% | 0,54 | -0,31R | €-369,21 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 6 | 274 | 274 | 42,34% | 0,99 | -0,00R | €-8,57 |
| Bilanciata 1H V1 | RANGE | 7 | 250 | 250 | 42,00% | 1,03 | 0,02R | €41,03 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 27,66% | 0,51 | -0,32R | €-151,94 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-2,77 |
| Bilanciata 1H V1 | TRANSITION | 0 | 117 | 117 | 37,61% | 1,08 | 0,04R | €48,40 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 128 | 128 | 32,03% | 0,91 | -0,05R | €-59,38 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,30 | 0,15R | €60,95 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 4 | 155 | 131 | 47,10% | 1,31 | 0,15R | €229,00 |
| Bilanciata 1H V2 | RANGE | 6 | 179 | 160 | 38,55% | 0,91 | -0,05R | €-91,24 |
| Bilanciata 1H V2 | TRANSITION | 0 | 97 | 84 | 39,18% | 1,21 | 0,11R | €102,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 8 | 87 | 87 | 27,59% | 0,48 | -0,34R | €-299,39 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 3 | 173 | 173 | 42,77% | 1,06 | 0,03R | €59,86 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 170 | 170 | 43,53% | 1,10 | 0,05R | €80,17 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,52 | -0,32R | €-61,13 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 64 | 64 | 37,50% | 1,15 | 0,07R | €44,08 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 75 | 75 | 34,67% | 1,13 | 0,06R | €47,35 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 8 | 76 | 76 | 25,00% | 0,35 | -0,44R | €-332,76 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 171 | 171 | 43,27% | 1,09 | 0,05R | €80,86 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 6 | 148 | 148 | 42,57% | 0,95 | -0,02R | €-35,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,62 | -0,24R | €-40,30 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 56 | 56 | 37,50% | 1,16 | 0,07R | €38,40 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 31,48% | 0,95 | -0,02R | €-13,49 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 22,58% | 0,49 | -0,26R | €-80,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 120 | 120 | 39,17% | 0,79 | -0,11R | €-130,66 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 79 | 79 | 41,77% | 0,98 | -0,01R | €-7,65 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -1,10R | €-76,85 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 45,95% | 1,50 | 0,20R | €74,56 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 63 | 63 | 33,33% | 0,87 | -0,06R | €-35,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 8 | 58 | 58 | 39,66% | 1,11 | 0,05R | €29,42 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 2 | 166 | 166 | 41,57% | 0,92 | -0,04R | €-70,07 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 4 | 228 | 228 | 38,60% | 0,91 | -0,05R | €-104,58 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 78 | 78 | 39,74% | 1,13 | 0,05R | €41,79 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 97 | 97 | 29,90% | 0,75 | -0,12R | €-114,38 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 8 | 76 | 76 | 35,53% | 0,87 | -0,07R | €-52,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 2 | 167 | 167 | 41,92% | 0,94 | -0,03R | €-56,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 4 | 258 | 258 | 41,09% | 1,03 | 0,02R | €40,61 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 80 | 80 | 41,25% | 1,23 | 0,09R | €71,48 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 113 | 113 | 29,20% | 0,68 | -0,17R | €-186,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 12 | 161 | 161 | 31,06% | 0,66 | -0,19R | €-313,67 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 5 | 324 | 324 | 39,81% | 0,84 | -0,09R | €-281,30 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 4 | 301 | 301 | 39,87% | 0,96 | -0,02R | €-58,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 40 | 40 | 37,50% | 0,86 | -0,07R | €-29,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 54,55% | 1,45 | 0,17R | €18,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 107 | 107 | 42,99% | 1,40 | 0,15R | €162,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 128 | 128 | 28,91% | 0,70 | -0,16R | €-204,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 50 | 50 | 46,00% | 1,46 | 0,17R | €87,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 6 | 93 | 93 | 31,18% | 0,57 | -0,27R | €-251,28 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 2 | 191 | 191 | 42,41% | 0,98 | -0,01R | €-22,10 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 165 | 165 | 44,85% | 1,22 | 0,10R | €166,61 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 38,89% | 0,78 | -0,12R | €-21,79 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 100,00% | ∞ | 0,89R | €62,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 61 | 61 | 42,62% | 1,60 | 0,20R | €120,86 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 75 | 75 | 28,00% | 0,62 | -0,21R | €-159,54 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 13 | 155 | 155 | 28,39% | 0,61 | -0,22R | €-343,57 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 5 | 320 | 320 | 40,00% | 0,90 | -0,05R | €-162,69 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 4 | 280 | 280 | 37,86% | 0,95 | -0,03R | €-77,12 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 39 | 39 | 28,21% | 0,64 | -0,20R | €-78,08 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 50,00% | 1,49 | 0,20R | €20,16 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 103 | 103 | 39,81% | 1,39 | 0,15R | €157,26 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 118 | 118 | 22,88% | 0,51 | -0,27R | €-318,56 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 37 | 33 | 45,95% | 0,89 | -0,06R | €-23,16 |
| Rapida 1H V2 | RANGE | 0 | 67 | 56 | 40,30% | 0,90 | -0,05R | €-34,75 |
| Rapida 1H V2 | TRANSITION | 0 | 11 | 11 | 63,64% | 1,79 | 0,25R | €27,27 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 12 | 153 | 153 | 30,72% | 0,60 | -0,23R | €-347,85 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 4 | 292 | 292 | 41,44% | 0,93 | -0,04R | €-102,43 |
| Rapida 1H V3 Filtered | RANGE | 4 | 269 | 269 | 39,78% | 0,97 | -0,02R | €-45,80 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 34 | 34 | 38,24% | 0,87 | -0,07R | €-23,20 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 93 | 93 | 40,86% | 1,31 | 0,12R | €114,75 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 126 | 126 | 36,51% | 0,94 | -0,03R | €-37,80 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 61 | 61 | 36,07% | 0,87 | -0,07R | €-42,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 7 | 121 | 121 | 32,23% | 0,59 | -0,24R | €-294,26 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 229 | 229 | 44,98% | 1,05 | 0,02R | €57,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 208 | 208 | 40,87% | 1,02 | 0,01R | €15,76 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 24 | 24 | 37,50% | 0,79 | -0,11R | €-26,88 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 87,50% | 6,12 | 0,65R | €51,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,26 | 0,11R | €75,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 86 | 86 | 29,07% | 0,64 | -0,20R | €-171,36 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,24 | -0,58R | €-110,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 126 | 126 | 49,21% | 0,97 | -0,02R | €-20,77 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 116 | 116 | 46,55% | 1,02 | 0,01R | €10,92 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 43 | 43 | 65,12% | 2,22 | 0,36R | €154,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 63 | 63 | 47,62% | 0,91 | -0,05R | €-28,47 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 16,67% | 0,23 | -0,58R | €-104,29 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 128 | 128 | 39,84% | 0,90 | -0,06R | €-71,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 1 | 119 | 119 | 44,54% | 1,11 | 0,05R | €63,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 43 | 43 | 44,19% | 1,85 | 0,26R | €109,67 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 65 | 65 | 32,31% | 0,78 | -0,11R | €-69,36 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 54 | 54 | 25,93% | 0,43 | -0,30R | €-161,83 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 279 | 279 | 40,86% | 0,90 | -0,05R | €-140,81 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 1 | 156 | 156 | 44,23% | 1,12 | 0,06R | €90,97 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 61 | 61 | 47,54% | 1,82 | 0,27R | €163,90 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 85 | 85 | 34,12% | 0,83 | -0,09R | €-72,37 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 43,59% | 1,23 | 0,10R | €40,01 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 12 | 83 | 83 | 33,73% | 0,69 | -0,18R | €-148,17 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 2 | 166 | 166 | 38,55% | 0,83 | -0,09R | €-155,18 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 4 | 271 | 271 | 40,59% | 1,00 | 0,00R | €2,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 74 | 74 | 39,19% | 1,32 | 0,12R | €87,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 112 | 112 | 32,14% | 0,76 | -0,13R | €-142,98 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 12 | 152 | 152 | 30,92% | 0,61 | -0,22R | €-336,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 4 | 291 | 291 | 40,89% | 0,91 | -0,05R | €-143,55 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 267 | 267 | 39,70% | 0,95 | -0,02R | €-60,54 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,92 | -0,04R | €-13,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 88 | 88 | 40,91% | 1,35 | 0,13R | €117,52 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 109 | 109 | 31,19% | 0,73 | -0,15R | €-160,54 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 41 | 41 | 41,46% | 1,16 | 0,07R | €29,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 5 | 32 | 32 | 25,00% | 1,09 | 0,05R | €15,87 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 9 | 91 | 91 | 34,07% | 0,90 | -0,07R | €-59,19 |
| SHADOW_4H_WIDE | RANGE | 7 | 87 | 87 | 18,39% | 0,71 | -0,19R | €-167,25 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 1 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 43 | 43 | 20,93% | 0,61 | -0,26R | €-110,90 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 46 | 46 | 28,26% | 1,22 | 0,13R | €57,78 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 3 | 19 | 19 | 21,05% | 0,75 | -0,17R | €-31,47 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 6 | 39 | 39 | 51,28% | 1,10 | 0,04R | €16,60 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 126 | 126 | 50,79% | 1,20 | 0,08R | €100,95 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 92 | 92 | 46,74% | 0,94 | -0,03R | €-27,81 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 60,00% | 2,25 | 0,41R | €41,08 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 18 | 18 | 50,00% | 1,35 | 0,17R | €29,83 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 45 | 45 | 42,22% | 0,85 | -0,07R | €-33,39 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 45,00% | 1,00 | 0,00R | €0,09 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 40,00% | 0,83 | -0,08R | €-4,03 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,39 | -0,39R | €-26,97 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,32 | 0,69R | €13,75 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 1 | 3 | 3 | 66,67% | 1,54 | 0,20R | €6,15 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 2,22 | 0,45R | €13,43 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,65R | €6,51 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 6 | 6 | 33,33% | 0,43 | -0,43R | €-25,78 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 25,00% | 0,26 | -0,53R | €-42,27 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 1,28 | 0,20R | €5,87 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,38 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,28 | -0,68R | €-47,66 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,15 | -0,70R | €-28,17 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 8 | 8 | 50,00% | 0,87 | -0,07R | €-5,73 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 14 | 105 | 105 | 29,52% | 0,64 | -0,22R | €-233,39 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 5 | 226 | 226 | 42,48% | 1,03 | 0,01R | €31,86 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 202 | 202 | 45,05% | 1,00 | 0,00R | €1,47 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 33 | 33 | 39,39% | 0,91 | -0,04R | €-14,24 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,95 | -0,03R | €-3,06 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 92 | 92 | 42,39% | 1,23 | 0,11R | €98,46 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 75 | 75 | 34,67% | 0,89 | -0,05R | €-37,29 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 106 | 106 | 37,74% | 1,09 | 0,04R | €41,55 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 30,00% | 0,75 | -0,14R | €-56,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 5 | 218 | 218 | 42,20% | 1,00 | -0,00R | €-0,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 4 | 108 | 108 | 50,00% | 1,18 | 0,08R | €88,39 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 53 | 53 | 47,17% | 1,65 | 0,22R | €114,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 65 | 65 | 32,31% | 0,68 | -0,15R | €-98,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 13 | 123 | 123 | 35,77% | 0,74 | -0,13R | €-163,99 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 5 | 265 | 265 | 38,49% | 0,92 | -0,04R | €-96,10 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 213 | 213 | 42,72% | 1,16 | 0,07R | €144,98 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 40 | 40 | 40,00% | 0,75 | -0,11R | €-43,81 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,51 | -0,30R | €-35,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 84 | 84 | 45,24% | 1,22 | 0,09R | €71,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 98 | 98 | 36,73% | 0,88 | -0,05R | €-46,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 109 | 109 | 50,46% | 1,27 | 0,11R | €121,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 14 | 105 | 105 | 29,52% | 0,65 | -0,22R | €-225,87 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 5 | 224 | 224 | 42,86% | 0,98 | -0,01R | €-22,57 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 190 | 190 | 47,89% | 1,07 | 0,03R | €64,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 31 | 31 | 45,16% | 1,09 | 0,04R | €12,23 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,75 | -0,16R | €-15,75 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 75 | 75 | 46,67% | 1,21 | 0,09R | €70,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 75 | 75 | 38,67% | 0,90 | -0,05R | €-33,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 85 | 85 | 38,82% | 0,78 | -0,10R | €-87,22 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,97 | -0,01R | €-6,60 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 38 | 38 | 52,63% | 1,53 | 0,20R | €77,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 57,89% | 2,69 | 0,47R | €88,74 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,88 | -0,06R | €-26,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 38 | 38 | 42,11% | 1,37 | 0,14R | €54,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 3,13 | 0,59R | €112,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 7 | 27 | 27 | 29,63% | 0,57 | -0,24R | €-64,29 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 4 | 102 | 102 | 41,18% | 0,87 | -0,07R | €-72,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 3 | 65 | 65 | 38,46% | 0,88 | -0,07R | €-44,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 39 | 39 | 41,03% | 0,90 | -0,05R | €-19,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 26 | 26 | 38,46% | 1,17 | 0,06R | €15,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 108 | 108 | 41,67% | 1,04 | 0,02R | €21,28 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 125 | 125 | 36,80% | 0,78 | -0,11R | €-133,30 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 29 | 29 | 34,48% | 0,58 | -0,21R | €-59,96 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 17 | 17 | 41,18% | 0,89 | -0,07R | €-11,45 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 44 | 44 | 43,18% | 0,91 | -0,05R | €-21,27 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 8 | 8 | 62,50% | 2,67 | 0,46R | €36,75 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 17 | 17 | 58,82% | 1,72 | 0,23R | €38,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 43 | 43 | 23,26% | 0,38 | -0,43R | €-186,53 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 5 | 179 | 179 | 41,34% | 1,07 | 0,04R | €70,77 |
| SHADOW_COMBO_SCANNER | RANGE | 4 | 121 | 121 | 47,11% | 1,28 | 0,13R | €162,78 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 14 | 14 | 35,71% | 0,54 | -0,25R | €-35,18 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 71 | 71 | 43,66% | 1,54 | 0,24R | €170,50 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 72 | 72 | 31,94% | 1,09 | 0,04R | €31,62 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 12 | 80 | 80 | 28,75% | 0,51 | -0,32R | €-258,31 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 4 | 201 | 201 | 42,29% | 1,05 | 0,03R | €61,01 |
| SHADOW_COMBO_TREND | RANGE | 7 | 173 | 173 | 39,88% | 1,10 | 0,05R | €87,67 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 24 | 24 | 37,50% | 1,18 | 0,08R | €19,31 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 76 | 76 | 36,84% | 1,15 | 0,08R | €60,00 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 67 | 67 | 29,85% | 0,70 | -0,16R | €-107,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 82 | 82 | 31,71% | 1,04 | 0,02R | €15,16 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 0,93 | -0,03R | €-1,47 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 6 | 6 | 66,67% | 3,84 | 0,56R | €33,45 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 8 | 8 | 62,50% | 1,13 | 0,05R | €4,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 6 | 6 | 33,33% | 0,49 | -0,38R | €-22,68 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,14 | -0,73R | €-36,57 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,75 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 1 | 10 | 10 | 10,00% | 0,09 | -0,71R | €-70,70 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 18,18% | 0,41 | -0,51R | €-56,27 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 12 | 12 | 50,00% | 1,47 | 0,22R | €26,39 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,55R | €5,45 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 10 | 51 | 51 | 21,57% | 0,45 | -0,43R | €-217,14 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 110 | 110 | 33,64% | 0,68 | -0,22R | €-247,11 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 95 | 95 | 37,89% | 1,02 | 0,01R | €10,70 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 33 | 33 | 39,39% | 1,29 | 0,15R | €48,35 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 43 | 43 | 30,23% | 1,15 | 0,07R | €32,24 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 54,17% | 1,90 | 0,44R | €104,71 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 10 | 41 | 41 | 19,51% | 0,32 | -0,55R | €-225,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 102 | 102 | 35,29% | 0,72 | -0,19R | €-196,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 3 | 75 | 75 | 40,00% | 0,99 | -0,01R | €-4,37 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 26 | 26 | 46,15% | 1,68 | 0,30R | €77,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 29 | 29 | 27,59% | 1,04 | 0,02R | €5,27 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 61,11% | 2,36 | 0,56R | €99,93 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 11 | 87 | 87 | 27,59% | 0,45 | -0,37R | €-325,16 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 4 | 205 | 205 | 41,95% | 1,03 | 0,02R | €34,27 |
| SHADOW_EMA_TREND_1H | RANGE | 8 | 165 | 165 | 38,18% | 1,05 | 0,02R | €39,29 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 72 | 72 | 34,72% | 1,04 | 0,02R | €17,55 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 89 | 89 | 29,21% | 0,86 | -0,08R | €-68,04 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,55 | -0,34R | €-34,23 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,53 | -0,33R | €-26,19 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 66,67% | 3,39 | 0,57R | €51,50 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 66,67% | 1,30 | 0,11R | €3,44 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,21 | -0,60R | €-18,01 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,35 | -0,53R | €-42,57 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 25,00% | 0,44 | -0,40R | €-32,16 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 16 | 16 | 43,75% | 0,69 | -0,17R | €-27,15 |
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
| SHADOW_GLOBAL_PURE | RANGE | 1 | 8 | 8 | 37,50% | 0,75 | -0,17R | €-13,63 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 37,50% | 1,22 | 0,14R | €32,47 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 5 | 74 | 74 | 35,14% | 1,04 | 0,03R | €21,97 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 5 | 118 | 118 | 32,20% | 0,99 | -0,01R | €-9,19 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 46 | 46 | 47,83% | 1,97 | 0,46R | €212,56 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 1 | 71 | 71 | 29,58% | 0,85 | -0,11R | €-74,81 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 38 | 38 | 57,89% | 1,08 | 0,03R | €12,15 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 3 | 166 | 166 | 67,47% | 1,35 | 0,11R | €180,57 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 218 | 218 | 66,97% | 1,34 | 0,11R | €234,46 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 100 | 100 | 73,00% | 1,75 | 0,18R | €181,85 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 132 | 132 | 60,61% | 0,99 | -0,00R | €-5,71 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 36,36% | 1,27 | 0,15R | €33,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 7 | 121 | 121 | 33,06% | 1,02 | 0,02R | €18,99 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 46 | 46 | 45,65% | 1,79 | 0,40R | €182,06 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 1 | 82 | 82 | 25,61% | 0,69 | -0,23R | €-188,38 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 47,37% | 2,00 | 0,49R | €93,92 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 5 | 78 | 78 | 32,05% | 0,91 | -0,06R | €-50,41 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 5 | 104 | 104 | 33,65% | 1,17 | 0,11R | €110,37 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 41 | 41 | 43,90% | 1,70 | 0,36R | €145,68 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 67 | 67 | 25,37% | 0,71 | -0,21R | €-142,89 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 18,75% | 0,48 | -0,40R | €-64,65 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 5 | 80 | 80 | 35,00% | 1,06 | 0,04R | €33,42 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 36 | 36 | 47,22% | 2,12 | 0,49R | €176,16 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,75 | -0,18R | €-106,89 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 36,36% | 1,18 | 0,11R | €23,42 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 5 | 76 | 76 | 35,53% | 1,06 | 0,04R | €29,44 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 5 | 110 | 110 | 34,55% | 1,11 | 0,07R | €75,88 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 45 | 45 | 44,44% | 1,71 | 0,36R | €162,62 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 1 | 70 | 70 | 25,71% | 0,70 | -0,22R | €-153,22 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 12 | 101 | 101 | 29,70% | 0,62 | -0,23R | €-234,71 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 6 | 227 | 227 | 39,65% | 0,99 | -0,01R | €-12,05 |
| Forza relativa 1H V1 | RANGE | 9 | 223 | 223 | 33,63% | 0,83 | -0,09R | €-199,96 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 29 | 29 | 27,59% | 0,49 | -0,28R | €-81,70 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 11 | 11 | 27,27% | 0,72 | -0,18R | €-19,83 |
| Forza relativa 1H V1 | TRANSITION | 1 | 90 | 90 | 40,00% | 1,41 | 0,20R | €178,39 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 75 | 75 | 28,00% | 0,87 | -0,07R | €-51,18 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 108 | 108 | 27,78% | 0,92 | -0,04R | €-43,00 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 34 | 34 | 26,47% | 0,77 | -0,15R | €-50,36 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 8 | 46 | 44 | 36,96% | 0,68 | -0,18R | €-83,11 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 4 | 91 | 84 | 42,86% | 1,25 | 0,14R | €126,94 |
| Forza relativa 1H V2 | RANGE | 6 | 99 | 94 | 35,35% | 0,89 | -0,06R | €-61,02 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 8 | 7 | 25,00% | 0,66 | -0,18R | €-14,36 |
| Forza relativa 1H V2 | TRANSITION | 0 | 49 | 44 | 40,82% | 1,54 | 0,25R | €122,15 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 35 | 34 | 28,57% | 0,95 | -0,02R | €-7,36 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 42 | 38 | 47,62% | 1,81 | 0,36R | €152,91 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 12 | 66 | 66 | 18,18% | 0,27 | -0,55R | €-362,48 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 1,18 | 0,09R | €13,09 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 3 | 90 | 90 | 33,33% | 0,59 | -0,20R | €-179,19 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 12 | 66 | 66 | 18,18% | 0,27 | -0,55R | €-362,48 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 1,18 | 0,09R | €13,09 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 3 | 90 | 90 | 33,33% | 0,59 | -0,20R | €-179,19 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 12 | 66 | 66 | 18,18% | 0,27 | -0,55R | €-362,48 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 1,18 | 0,09R | €13,09 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 3 | 90 | 90 | 33,33% | 0,59 | -0,20R | €-179,19 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,29 | 0,12R | €20,92 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 8 | 55 | 55 | 21,82% | 0,38 | -0,44R | €-239,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 16 | 16 | 43,75% | 1,44 | 0,21R | €32,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 104 | 104 | 33,65% | 0,74 | -0,13R | €-136,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 19 | 19 | 47,37% | 1,39 | 0,15R | €28,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 42 | 42 | 38,10% | 1,01 | 0,01R | €2,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 9 | 69 | 69 | 42,03% | 0,43 | -0,33R | €-225,43 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 0,92 | -0,04R | €-4,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 2 | 113 | 113 | 61,06% | 0,89 | -0,04R | €-45,92 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 23 | 23 | 65,22% | 1,43 | 0,16R | €35,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 33 | 33 | 57,58% | 1,30 | 0,13R | €44,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 8 | 55 | 55 | 36,36% | 0,25 | -0,46R | €-255,47 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,28 | 0,12R | €17,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 2 | 105 | 105 | 62,86% | 0,77 | -0,08R | €-84,45 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 21 | 21 | 61,90% | 1,24 | 0,10R | €20,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 32 | 32 | 59,38% | 1,50 | 0,21R | €67,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 37 | 37 | 35,14% | 0,83 | -0,09R | €-34,25 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 5 | 232 | 232 | 40,52% | 0,92 | -0,05R | €-110,47 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 4 | 102 | 102 | 50,00% | 1,18 | 0,08R | €81,10 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 56 | 56 | 41,07% | 1,43 | 0,16R | €88,53 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 37 | 37 | 35,14% | 0,83 | -0,09R | €-34,19 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 5 | 236 | 236 | 41,10% | 0,92 | -0,04R | €-99,77 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 4 | 102 | 102 | 50,00% | 1,18 | 0,08R | €81,10 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 56 | 56 | 41,07% | 1,43 | 0,16R | €88,53 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 37 | 37 | 35,14% | 0,83 | -0,09R | €-34,19 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 5 | 236 | 236 | 41,10% | 0,92 | -0,04R | €-99,77 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 4 | 102 | 102 | 50,00% | 1,18 | 0,08R | €81,10 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 56 | 56 | 41,07% | 1,43 | 0,16R | €88,53 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 64 | 64 | 31,25% | 0,69 | -0,16R | €-100,31 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 40 | 40 | 25,00% | 0,43 | -0,38R | €-153,60 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 5 | 178 | 178 | 41,57% | 1,08 | 0,05R | €82,47 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 4 | 112 | 112 | 47,32% | 1,32 | 0,15R | €164,56 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 66 | 66 | 42,42% | 1,53 | 0,24R | €155,81 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 71 | 71 | 30,99% | 1,03 | 0,02R | €10,91 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,18 | -0,67R | €-119,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 3 | 75 | 75 | 30,67% | 0,60 | -0,27R | €-204,79 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 1 | 8 | 8 | 37,50% | 0,21 | -0,54R | €-42,98 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 30 | 30 | 53,33% | 2,17 | 0,40R | €120,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 58 | 58 | 29,31% | 0,86 | -0,07R | €-42,83 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 34 | 34 | 23,53% | 0,39 | -0,41R | €-139,80 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 3 | 91 | 91 | 31,87% | 0,65 | -0,22R | €-203,82 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 5 | 108 | 108 | 46,30% | 1,19 | 0,09R | €98,82 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,56 | -0,24R | €-28,85 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 50 | 50 | 48,00% | 2,23 | 0,41R | €204,25 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 52 | 52 | 23,08% | 0,59 | -0,24R | €-122,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 28 | 28 | 32,14% | 0,69 | -0,14R | €-38,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 2 | 91 | 91 | 36,26% | 0,77 | -0,11R | €-102,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 5 | 129 | 129 | 44,96% | 1,26 | 0,11R | €139,38 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,63 | -0,15R | €-29,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 50 | 50 | 48,00% | 1,35 | 0,13R | €65,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 53 | 53 | 50,94% | 1,34 | 0,14R | €72,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 57,14% | 1,17 | 0,07R | €5,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 25 | 25 | 28,00% | 0,37 | -0,39R | €-96,37 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 73 | 73 | 32,88% | 0,73 | -0,17R | €-121,05 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 5 | 112 | 112 | 47,32% | 1,22 | 0,11R | €118,51 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,47 | -0,31R | €-45,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 45 | 45 | 40,00% | 1,61 | 0,24R | €107,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 26,83% | 0,78 | -0,12R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,42 | -0,37R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 36 | 36 | 38,89% | 0,86 | -0,06R | €-22,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 4 | 184 | 184 | 41,85% | 1,05 | 0,02R | €39,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 130 | 130 | 45,38% | 1,28 | 0,12R | €152,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,63 | -0,15R | €-29,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 56 | 56 | 44,64% | 1,31 | 0,11R | €61,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 60 | 60 | 50,00% | 1,33 | 0,13R | €78,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 31 | 31 | 29,03% | 0,48 | -0,32R | €-100,48 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 4 | 150 | 150 | 44,00% | 1,22 | 0,12R | €175,19 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 4 | 111 | 111 | 47,75% | 1,25 | 0,12R | €131,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,47 | -0,31R | €-45,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 50 | 50 | 40,00% | 1,41 | 0,17R | €84,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 46 | 46 | 26,09% | 0,80 | -0,10R | €-48,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 46 | 46 | 36,96% | 0,73 | -0,12R | €-55,07 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 5 | 211 | 211 | 40,28% | 0,91 | -0,04R | €-86,47 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 121 | 121 | 46,28% | 1,31 | 0,13R | €154,56 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,53 | -0,21R | €-37,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 64 | 64 | 45,31% | 1,33 | 0,12R | €77,54 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 73 | 73 | 49,32% | 1,28 | 0,11R | €78,63 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 33 | 33 | 30,30% | 0,53 | -0,31R | €-101,24 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 5 | 179 | 179 | 41,34% | 1,09 | 0,05R | €92,51 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 103 | 103 | 45,63% | 1,23 | 0,11R | €116,08 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 54 | 54 | 40,74% | 1,48 | 0,20R | €109,62 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 54 | 54 | 24,07% | 0,68 | -0,17R | €-91,68 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 32 | 32 | 28,12% | 0,54 | -0,31R | €-98,65 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 5 | 169 | 169 | 40,24% | 1,06 | 0,03R | €56,75 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 97 | 97 | 45,36% | 1,30 | 0,15R | €143,63 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 48 | 48 | 39,58% | 1,67 | 0,26R | €126,77 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 53 | 53 | 26,42% | 0,73 | -0,13R | €-70,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 46 | 46 | 30,43% | 0,63 | -0,22R | €-102,58 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 5 | 185 | 185 | 40,54% | 0,97 | -0,01R | €-26,28 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 117 | 117 | 48,72% | 1,25 | 0,12R | €135,15 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 69 | 69 | 42,03% | 1,48 | 0,20R | €134,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 92 | 92 | 38,04% | 1,14 | 0,07R | €59,88 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 7 | 7 | 0,00% | 0,00 | -1,10R | €-76,72 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 58,33% | 1,98 | 0,44R | €53,24 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 10 | 10 | 50,00% | 0,90 | -0,05R | €-5,33 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,86 | -0,10R | €-3,05 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 3,31 | 0,60R | €23,94 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 80,00% | 2,30 | 0,28R | €13,97 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,42 | -0,40R | €-44,47 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,53 | -0,33R | €-26,28 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 0,97 | -0,01R | €-0,27 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 20,00% | 0,16 | -0,75R | €-37,55 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 9 | 9 | 44,44% | 1,33 | 0,16R | €14,69 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 66,67% | 2,08 | 0,41R | €36,51 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,72R | €27,23 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,60 | -0,28R | €-8,29 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,64 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 58,33% | 1,98 | 0,44R | €53,30 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 10 | 10 | 40,00% | 0,91 | -0,06R | €-6,03 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,29 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,91 | -0,05R | €-1,98 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-10T13:11:33+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **433**
- Scenari virtuali ancora attivi: **3842**
- Gruppi in attesa dell'uscita originale: **400**
- Gruppi con originale chiuso ma Shadow ancora attive: **33**
- Confronti completati: **582027**

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

Generato: 2026-09-10T13:14:01+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **582027**
- Valutazioni prodotte: **28475**
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

🏆 CHALLENGER CANDIDATE
Aggiornamento aggregazione UTC: 2026-09-10T13:20:02+00:00
Mother canonica simulata: stessi ingressi, osservazioni ed execution del challenger.
PnL al netto delle fee modellate, funding escluso da entrambi; FX congelato all'ingresso.
Osservazioni MARK discrete: nessuna certificazione del percorso intrabar tra quotazioni.
Ranking promozionale: INSUFFICIENT_CERTIFIED_DATA

Rapida 1H V1 — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Rapida 1H V1 — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 90 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Master Adaptive Consensus — breakeven dopo +0,2R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 38 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 154 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 0 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-09T19:19:01.976607+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

AUTO_PROMOTION=DISABLED · nessun ordine · revisione umana obbligatoria.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-10T13:08:25+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **5**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **576.00 R**
- Profitto virtuale mancato: **1740.39 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 244 | 0 | 13543.92 |
| DOWN_20 | 244 | 0 | 27087.85 |
| DOWN_30 | 244 | 3 | 40684.83 |
| DOWN_40 | 244 | 58 | 51908.33 |
| UP_10 | 178 | 0 | 14585.71 |
| UP_20 | 178 | 0 | 29171.41 |
| UP_30 | 178 | 0 | 43757.12 |
| UP_40 | 178 | 99 | 51439.98 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-10T13:05:20+00:00

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

Generato: 2026-09-10T13:20:08+00:00

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

Generato: 2026-09-10T13:20:09+00:00

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

Generato: 2026-09-10T13:20:09+00:00

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

Generato: 2026-09-10T13:20:09+00:00

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
| 1 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 24.1 | E | 53 | 2.13 | 0.453 | 4.71 |
| 2 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 23.0 | E | 155 | 1.43 | 0.214 | 23.36 |
| 3 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | BASELINE | 21.0 | E | 148 | 1.16 | 0.080 | 10.66 |
| 4 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 20.9 | E | 152 | 1.26 | 0.124 | 14.92 |
| 5 | SHADOW_COMBO_ADAPTIVE | BASELINE | 20.6 | E | 211 | 1.26 | 0.127 | 23.82 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 20.5 | E | 202 | 1.22 | 0.107 | 24.60 |
| 7 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 19.8 | E | 219 | 1.15 | 0.076 | 30.08 |
| 8 | SHADOW_DONCHIAN_1H | BASELINE | 19.5 | E | 145 | 1.22 | 0.132 | 19.74 |
| 9 | SHADOW_1H_FAST_V3 | BASELINE | 18.9 | E | 263 | 1.13 | 0.066 | 29.54 |
| 10 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 18.6 | E | 276 | 1.11 | 0.053 | 32.84 |

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

Generato: 2026-09-10T13:20:09+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BEAR_TREND**
- Righe di performance: **1110**
- Strategie preferite nel regime corrente: **1**
- Strategie da evitare nel regime corrente: **20**
- Memorie contestuali: **530**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 84.4 | 23 | 3.02 | 0.515 | 3.16 |
| 2 | MAIN | main | OBSERVING | 81.2 | 11 | 3.01 | 0.450 | 1.07 |
| 3 | SHADOW_RSI_SHORT_15X_10_RSI75 | shadow-rsi-short-15x-10-rsi75 | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.742 | 0.00 |
| 4 | SHADOW_RSI_SHORT_15X_50_RSI75 | shadow-rsi-short-15x-50-rsi75 | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.742 | 0.00 |
| 5 | SHADOW_RSI_SHORT_15X_10_RSI80 | shadow-rsi-short-15x-10-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.583 | 0.00 |
| 6 | SHADOW_RSI_SHORT_15X_50_RSI80 | shadow-rsi-short-15x-50-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.583 | 0.00 |
| 7 | SHADOW_RSI_SHORT_5X_RSI80 | shadow-rsi-short-5x-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.498 | 0.00 |
| 8 | SHADOW_ETH_EMA_4H | shadow-eth-ema-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.574 | 0.00 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | shadow-1h-fast-v3-no-esports-stress-guard-v1 | OBSERVING | 78.2 | 24 | 2.22 | 0.403 | 4.27 |
| 10 | SHADOW_RSI_LONG_5X_RSI20 | shadow-rsi-long-5x-rsi20 | INSUFFICIENT | 75.9 | 3 | 2.90 | 0.480 | 0.76 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-10T13:20:10+00:00

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

Generato: 2026-09-10T13:08:25+00:00

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
