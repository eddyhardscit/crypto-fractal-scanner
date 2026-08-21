# Paper trading automatico KuCoin

Generato: 2026-08-21T11:10:07+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-21T11:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-21T11:05:28+00:00 | 2026-08-21T11:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-21T10:45:00+00:00 | 2026-08-21T10:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-21T10:00:00+00:00 | 2026-08-21T10:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-21T04:00:00+00:00 | 2026-08-21T04:00:00+00:00 | 3,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend — Side × Regime Guard | ADA | 60m | LONG | 6,52 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — parziale 1R | SUI | 60m | LONG | 5,20 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | XRP | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | XRP | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | ETH | 60m | LONG | 6,15 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | 60m | LONG | 6,52 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Long Only | PEPE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | PEPE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | ADA | 60m | LONG | 6,52 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | PEPE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | PEPE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | ADA | 60m | LONG | 6,52 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — target pieno 2R | BOME | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — Cost Aware | ETH | 60m | LONG | 6,15 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida score 6–7,5 — Cost Aware | ENA | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BOME | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 7,42 | 6,00 | 0,00 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,94 | 6,00 | 0,06 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,27 | 6,00 | 0,73 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,69 | 6,00 | 1,31 | STALE_CANDLE | 3,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 3,26 | 6,00 | 2,74 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 3,15 | 6,00 | 2,85 | STALE_CANDLE | 3,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 2,15 | 6,00 | 3,85 | STALE_CANDLE | 3,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.7 minuti; tolleranza 60 minuti. |
| Bilanciata 1H — LONG senza Range High Vol | XRP | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | XRP | 60m | LONG | 8,25 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | XRP | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | XRP | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Long Only | XRP | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | XRP | 60m | LONG | 8,25 | 5,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | XRP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top15 Long | XRP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.760,03 | -2,40% | €11,68 | €3.000,00 | 0,39% | 4 | 47 | 36,17% | 0,83 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 47 | 1878 | PRIME INDICAZIONI | 50 (mancano 3) |

- Trade del Principale 4H chiusi: **47**; win rate **36,17%**; profit factor **0,83**.
- Expectancy: **€-5,09** per trade; P&L netto: **€-239,21**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.760,03 | €563,88 | €1.691,63 | €144,97 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 7 | €11.331,32 | €2.949,85 | €5.899,71 | €221,64 | €94,75 |
| TEST | Rapida score 6–7,5 — Cost Aware | 7 | €11.190,12 | €2.553,43 | €7.660,29 | €223,80 | €50,46 |
| TEST | Combo Trend — Side × Regime Guard | 6 | €11.122,99 | €2.350,01 | €4.700,01 | €167,19 | €69,41 |
| TEST | Donchian 1H Gb20 120R V1 | 7 | €11.064,54 | €2.880,40 | €5.760,81 | €216,43 | €92,52 |
| TEST | Rapida V1 — senza PEPE | 7 | €10.800,70 | €1.796,94 | €5.390,82 | €216,04 | €53,74 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.791,21 | €2.509,74 | €5.019,49 | €107,78 | €106,30 |
| TEST | MAIN — Side × Regime Guard | 3 | €10.618,11 | €576,16 | €1.728,47 | €156,14 | €37,60 |
| TEST | Combo Adaptive — madre | 7 | €10.460,08 | €3.102,85 | €6.205,70 | €155,36 | €59,91 |
| TEST | Combo Adaptive — Side × Regime Guard | 6 | €10.456,11 | €3.439,02 | €6.878,04 | €104,02 | €102,95 |
| TEST | Combo Adaptive — Long Only | 6 | €10.429,96 | €3.314,42 | €6.628,84 | €158,39 | €44,65 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.296,95 | €2.487,15 | €4.974,30 | €154,15 | €82,01 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 7 | €10.265,42 | €2.289,89 | €4.579,78 | €101,69 | €106,16 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 7 | €10.259,41 | €2.288,55 | €4.577,10 | €101,63 | €106,10 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 7 | €10.210,02 | €1.159,78 | €3.479,33 | €154,61 | €58,11 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €10.209,46 | €1.462,77 | €4.388,32 | €49,87 | €105,43 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.166,80 | €727,07 | €1.454,13 | €0,00 | €101,92 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.141,04 | €665,34 | €1.330,67 | €0,00 | €93,27 |
| TEST | Rapida V3 NoHigh — Regime Guard | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 5 | €10.131,59 | €1.605,58 | €3.211,17 | €98,91 | €62,88 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 7 | €10.119,58 | €1.792,97 | €5.378,91 | €202,39 | €56,83 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 8 | €10.081,46 | €2.764,41 | €5.528,83 | €101,22 | €90,14 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.059,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 7 | €10.054,56 | €1.781,51 | €5.344,54 | €201,09 | €56,46 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 2 | €10.041,61 | €962,01 | €2.886,04 | €99,43 | €18,90 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.032,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 1 | €10.029,22 | €155,86 | €467,58 | €51,44 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.003,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.000,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €9.995,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.979,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €9.976,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.942,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.942,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.940,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.934,66 | €826,55 | €2.479,66 | €49,75 | €-13,42 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 7 | €9.931,32 | €1.994,96 | €5.984,89 | €198,63 | €44,69 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.928,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.920,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.911,34 | €577,20 | €1.154,41 | €0,00 | €70,49 |
| TEST | Top 5 + BTC — Guard | 5 | €9.904,51 | €2.167,27 | €4.334,55 | €51,15 | €136,03 |
| TEST | Rapida V3 — senza ESPORTS | 7 | €9.901,30 | €1.759,14 | €5.277,43 | €198,03 | €55,94 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.898,25 | €863,71 | €1.727,42 | €48,65 | €28,48 |
| TEST | Sol Bollinger 1H | 0 | €9.892,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.879,06 | €2.386,21 | €4.772,43 | €147,89 | €78,69 |
| TEST | Eth Adaptive 1H | 1 | €9.865,76 | €729,50 | €2.188,49 | €49,39 | €-11,85 |
| TEST | Scanner Top15 Long | 7 | €9.864,68 | €2.431,12 | €4.862,25 | €100,52 | €90,95 |
| TEST | Scanner Top20 Long | 7 | €9.864,68 | €2.431,12 | €4.862,25 | €100,52 | €90,95 |
| TEST | Scanner Top10 Long | 6 | €9.858,65 | €2.401,31 | €4.802,62 | €100,51 | €84,89 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.825,02 | €651,23 | €1.953,70 | €49,13 | €0,07 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.816,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.801,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 1 | €9.779,65 | €151,98 | €455,94 | €50,16 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.773,75 | €852,85 | €1.705,70 | €48,04 | €28,13 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 7 | €9.768,35 | €1.316,02 | €3.948,05 | €141,18 | €74,23 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.752,51 | €883,06 | €1.766,12 | €49,99 | €29,27 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.702,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €9.697,87 | €2.066,52 | €4.133,04 | €96,66 | €74,17 |
| TEST | Top 5 + BTC — Guard + MFE | 5 | €9.674,17 | €2.116,87 | €4.233,74 | €49,96 | €132,86 |
| TEST | Bilanciata V3 · LONG only | 7 | €9.656,51 | €1.383,55 | €4.150,65 | €47,17 | €99,72 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.652,88 | €2.331,58 | €4.663,16 | €144,50 | €76,88 |
| TEST | Eth Bollinger 1H | 0 | €9.634,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 5 | €9.608,35 | €2.168,24 | €4.336,48 | €189,89 | €35,15 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 6 | €9.556,87 | €1.181,94 | €3.545,82 | €97,28 | €25,45 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 6 | €9.456,78 | €1.823,54 | €3.647,08 | €95,85 | €122,12 |
| TEST | Rapida V3 — Long Only | 7 | €9.455,77 | €1.904,00 | €5.712,01 | €189,12 | €42,63 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.447,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.444,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 1 | €9.435,91 | €146,77 | €440,31 | €48,44 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.320,02 | €1.082,57 | €2.165,15 | €96,67 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.305,85 | €1.080,93 | €2.161,86 | €96,53 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.234,23 | €1.072,61 | €2.145,22 | €95,79 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 8 | €9.208,65 | €1.614,39 | €3.228,78 | €49,44 | €147,44 |
| TEST | Combo Adaptive — MFE Trail esistente | 5 | €9.205,13 | €2.682,00 | €5.364,00 | €137,98 | €94,23 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 1 | €9.151,18 | €135,05 | €405,16 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.114,86 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.760,03 | €-239,21 | 47 | 47 | 36,17% | 0,83 | €-5,09 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.331,32 | €1.239,45 | 80 | 80 | 50,00% | 1,71 | €15,49 | 3,63% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.190,12 | €1.144,25 | 102 | 102 | 55,88% | 1,56 | €11,22 | 4,41% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.122,99 | €1.056,40 | 77 | 77 | 55,84% | 1,77 | €13,72 | 4,33% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.064,54 | €974,83 | 48 | 48 | 50,00% | 2,12 | €20,31 | 3,63% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.800,70 | €750,20 | 158 | 158 | 50,00% | 1,26 | €4,75 | 4,46% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.791,21 | €688,36 | 106 | 106 | 49,06% | 1,31 | €6,49 | 8,85% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.618,11 | €581,80 | 30 | 30 | 50,00% | 1,93 | €19,39 | 2,40% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.460,08 | €403,90 | 114 | 114 | 43,86% | 1,20 | €3,54 | 7,91% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.456,11 | €357,28 | 85 | 85 | 47,06% | 1,22 | €4,20 | 8,68% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.429,96 | €389,29 | 82 | 82 | 47,56% | 1,23 | €4,75 | 6,25% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.296,95 | €218,13 | 95 | 95 | 43,16% | 1,10 | €2,30 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.265,42 | €162,03 | 77 | 77 | 40,26% | 1,08 | €2,10 | 11,78% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.259,41 | €156,09 | 81 | 81 | 40,74% | 1,08 | €1,93 | 12,06% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.210,02 | €97,66 | 175 | 174 | 39,43% | 1,03 | €0,56 | 6,56% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.209,46 | €106,66 | 126 | 126 | 42,06% | 1,04 | €0,85 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.166,80 | €66,34 | 4 | 4 | 50,00% | 1,63 | €16,58 | 1,05% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.141,04 | €49,10 | 4 | 4 | 50,00% | 1,47 | €12,27 | 1,01% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Ampia 4H | Confluenza trend | €10.131,59 | €71,05 | 46 | 46 | 28,26% | 1,06 | €1,54 | 4,45% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.119,58 | €60,43 | 139 | 138 | 50,36% | 1,02 | €0,43 | 9,50% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.081,46 | €-5,36 | 113 | 113 | 42,48% | 1,00 | €-0,05 | 8,69% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.059,56 | €59,56 | 11 | 11 | 45,45% | 1,24 | €5,41 | 2,77% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.054,56 | €-4,21 | 183 | 182 | 43,17% | 1,00 | €-0,02 | 9,48% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,94 | €46,94 | 7 | 7 | 57,14% | 1,28 | €6,71 | 1,89% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.041,61 | €24,44 | 36 | 32 | 44,44% | 1,03 | €0,68 | 3,89% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Sol Ema 4H | Trend following EMA | €10.032,52 | €32,52 | 6 | 6 | 33,33% | 1,16 | €5,42 | 2,27% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.029,22 | €29,50 | 121 | 121 | 43,80% | 1,01 | €0,24 | 7,10% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.003,36 | €3,36 | 27 | 27 | 44,44% | 1,03 | €0,12 | 0,33% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,67 | €0,67 | 27 | 27 | 44,44% | 1,03 | €0,02 | 0,07% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €9.995,25 | €-4,75 | 4 | 4 | 50,00% | 0,09 | €-1,19 | 0,06% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,76 | €-5,24 | 14 | 14 | 35,71% | 0,47 | €-0,37 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.979,71 | €-20,29 | 4 | 4 | 50,00% | 0,08 | €-5,07 | 0,30% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €9.976,25 | €-23,75 | 4 | 4 | 50,00% | 0,09 | €-5,94 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,79 | €-26,21 | 14 | 14 | 35,71% | 0,47 | €-1,87 | 0,53% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Sol Ema 1H | Trend following EMA | €9.942,98 | €-57,02 | 12 | 12 | 33,33% | 0,85 | €-4,75 | 3,33% |
| TEST | Btc Ema 1H | Trend following EMA | €9.942,20 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,80 | €-59,20 | 14 | 14 | 35,71% | 0,32 | €-4,23 | 0,89% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.934,66 | €-50,43 | 9 | 9 | 33,33% | 0,85 | €-5,60 | 2,63% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.931,32 | €-109,78 | 98 | 98 | 43,88% | 0,95 | €-1,12 | 10,60% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.928,01 | €-71,99 | 27 | 27 | 44,44% | 0,52 | €-2,67 | 0,84% |
| TEST | Doge Ema 1H | Trend following EMA | €9.920,90 | €-79,10 | 14 | 14 | 57,14% | 0,77 | €-5,65 | 2,61% |
| TEST | Eth Ema 4H | Trend following EMA | €9.911,34 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,83% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.904,51 | €-228,66 | 77 | 77 | 38,96% | 0,88 | €-2,97 | 7,34% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.901,30 | €-206,03 | 155 | 154 | 43,87% | 0,93 | €-1,33 | 9,00% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.898,25 | €-129,01 | 30 | 30 | 46,67% | 0,84 | €-4,30 | 4,21% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.892,99 | €-107,01 | 8 | 8 | 37,50% | 0,66 | €-13,38 | 1,89% |
| TEST | Combo Scanner | Combo Scanner | €9.879,06 | €-196,56 | 99 | 99 | 42,42% | 0,92 | €-1,99 | 11,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.865,76 | €-121,08 | 10 | 10 | 40,00% | 0,63 | €-12,11 | 3,14% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.864,68 | €-222,95 | 83 | 83 | 45,78% | 0,87 | €-2,69 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.864,68 | €-222,95 | 83 | 83 | 45,78% | 0,87 | €-2,69 | 10,31% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.858,65 | €-222,95 | 83 | 83 | 45,78% | 0,87 | €-2,69 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Eth Ema 1H | Trend following EMA | €9.825,02 | €-173,88 | 14 | 14 | 35,71% | 0,66 | €-12,42 | 4,80% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.816,06 | €-183,94 | 11 | 11 | 45,45% | 0,49 | €-16,72 | 2,90% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.801,57 | €-198,43 | 13 | 13 | 30,77% | 0,56 | €-15,26 | 4,59% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €9.779,65 | €-220,08 | 85 | 85 | 42,35% | 0,88 | €-2,59 | 7,10% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.773,75 | €-253,17 | 30 | 30 | 40,00% | 0,69 | €-8,44 | 5,41% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.768,35 | €-303,44 | 73 | 73 | 43,84% | 0,83 | €-4,16 | 9,26% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.752,51 | €-275,50 | 43 | 43 | 46,51% | 0,78 | €-6,41 | 5,38% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.702,33 | €-365,26 | 131 | 130 | 41,98% | 0,90 | €-2,79 | 9,66% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.697,87 | €-373,75 | 91 | 87 | 39,56% | 0,87 | €-4,11 | 10,88% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.674,17 | €-455,91 | 94 | 94 | 40,43% | 0,80 | €-4,85 | 8,78% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.656,51 | €-440,71 | 82 | 82 | 41,46% | 0,75 | €-5,37 | 8,85% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.652,88 | €-421,01 | 87 | 87 | 41,38% | 0,78 | €-4,84 | 12,28% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.634,33 | €-365,67 | 6 | 6 | 16,67% | 0,04 | €-60,94 | 4,14% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.608,35 | €-423,98 | 58 | 58 | 36,21% | 0,74 | €-7,31 | 8,88% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.556,87 | €-466,29 | 83 | 76 | 40,96% | 0,76 | €-5,62 | 8,84% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Combo Trend | Combo Trend | €9.456,78 | €-662,95 | 133 | 133 | 36,09% | 0,80 | €-4,98 | 10,85% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.455,77 | €-583,43 | 118 | 118 | 38,14% | 0,80 | €-4,94 | 12,52% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.447,55 | €-615,90 | 84 | 83 | 44,05% | 0,76 | €-7,33 | 7,69% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.444,37 | €-621,42 | 89 | 88 | 43,82% | 0,78 | €-6,98 | 9,98% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.435,91 | €-563,83 | 111 | 111 | 40,54% | 0,80 | €-5,08 | 6,91% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.320,02 | €-678,72 | 58 | 58 | 32,76% | 0,60 | €-11,70 | 8,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,85 | €-692,90 | 59 | 59 | 32,20% | 0,58 | €-11,74 | 8,30% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.234,23 | €-764,52 | 86 | 86 | 32,56% | 0,66 | €-8,89 | 9,40% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.208,65 | €-936,69 | 99 | 99 | 32,32% | 0,58 | €-9,46 | 12,31% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.205,13 | €-885,88 | 121 | 121 | 38,02% | 0,65 | €-7,32 | 15,45% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.151,18 | €-848,58 | 120 | 120 | 36,67% | 0,69 | €-7,07 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,86 | €-884,87 | 37 | 37 | 37,84% | 0,48 | €-23,92 | 10,64% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
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
| Principale 4H | LINK | LONG | Confluenza trend | 240m | 3,0x | 10,58112 | 10,58112 | 10,13407 | 7,10698 | 11,47522 | €16,96 | €50,87 | €2,15 | €0,00 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | HYPE | LONG | Confluenza trend | 60m | 3,0x | 72,76855 | 75,13000 | 72,76855 | 48,87621 | 77,95329 | €16,05 | €48,15 | €0,00 | €1,56 |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | LONG | Confluenza trend | 60m | 3,0x | 634,78693 | 659,06000 | 637,55678 | 426,36522 | 688,04444 | €384,93 | €1.154,80 | €0,00 | €44,16 |
| Bilanciata 1H — LONG senza Range High Vol | ENA | LONG | Confluenza trend | 60m | 3,0x | 0,13642 | 0,14011 | 0,12894 | 0,09163 | 0,15136 | €294,71 | €884,14 | €48,43 | €23,93 |
| Bilanciata 1H — LONG senza Range High Vol | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,06 | €102,18 | €0,00 | €4,58 |
| Bilanciata 1H — LONG senza Range High Vol | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,38951 | 1,38923 | 1,32451 | 0,93329 | 1,51951 | €11,81 | €35,44 | €1,66 | €-0,01 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | LINK | LONG | Confluenza trend V2 | 60m | 3,0x | 10,70214 | 10,70214 | 10,45333 | 7,18827 | 11,19976 | €19,07 | €57,20 | €1,33 | €0,00 |
| Bilanciata 1H V2 | ADA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,21053 | 0,21432 | 0,21053 | 0,14141 | 0,22486 | €464,96 | €1.394,88 | €0,00 | €25,10 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 74,38487 | 75,13000 | 71,84452 | 49,96184 | 79,46558 | €11,76 | €35,29 | €1,21 | €0,35 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 72,76855 | 75,13000 | 72,76855 | 48,87621 | 77,95329 | €13,01 | €39,02 | €0,00 | €1,27 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20930 | 0,21432 | 0,20930 | 0,14058 | 0,22355 | €11,15 | €33,45 | €0,00 | €0,80 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 634,78693 | 659,06000 | 637,55678 | 426,36522 | 688,04444 | €401,20 | €1.203,60 | €0,00 | €46,02 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €426,44 | €1.279,33 | €0,00 | €57,34 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2395,91909 | 2396,00000 | 2335,66764 | 1609,25899 | 2516,42198 | €12,92 | €38,76 | €0,97 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €624,93 | €1.874,80 | €51,62 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 74,38487 | 75,13000 | 72,40904 | 49,96184 | 77,34862 | €694,04 | €2.082,11 | €55,31 | €20,86 |
| Rapida score 6–7,5 — Cost Aware | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,79186 | 0,80160 | 0,77403 | 0,53186 | 0,81860 | €811,85 | €2.435,55 | €54,84 | €29,96 |
| Rapida score 6–7,5 — Cost Aware | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,21499 | 0,21432 | 0,20838 | 0,14440 | 0,22492 | €12,90 | €38,69 | €1,19 | €-0,12 |
| Rapida score 6–7,5 — Cost Aware | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,14014 | 0,14011 | 0,13308 | 0,09413 | 0,15073 | €370,14 | €1.110,43 | €55,96 | €-0,22 |
| Rapida score 6–7,5 — Cost Aware | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2396,47920 | 2396,00000 | 2350,64232 | 1609,63520 | 2465,23455 | €30,67 | €92,00 | €1,76 | €-0,02 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| Rapida V1 — senza PEPE | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| Rapida V1 — senza PEPE | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1213,43264 | 1213,43264 | 1179,70743 | 815,02226 | 1264,02045 | €33,31 | €99,94 | €2,78 | €0,00 |
| Rapida V1 — senza PEPE | LINK | LONG | Momentum / breakout | 60m | 3,0x | 10,64413 | 10,64413 | 10,46121 | 7,14931 | 10,91851 | €17,86 | €53,58 | €0,92 | €0,00 |
| Rapida V1 — senza PEPE | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,13642 | 0,14011 | 0,13061 | 0,09163 | 0,14514 | €417,58 | €1.252,75 | €53,37 | €33,91 |
| Rapida V1 — senza PEPE | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 74,38487 | 75,13000 | 72,40904 | 49,96184 | 77,34862 | €669,72 | €2.009,17 | €53,37 | €20,13 |
| Rapida V1 — senza PEPE | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2395,91909 | 2396,00000 | 2349,05685 | 1609,25899 | 2466,21245 | €12,15 | €36,44 | €0,71 | €0,00 |
| Rapida V1 — senza PEPE | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,38951 | 1,38923 | 1,33895 | 0,93329 | 1,46534 | €490,86 | €1.472,58 | €53,58 | €-0,29 |
| Rapida V1 — target pieno 2R | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| Rapida V1 — target pieno 2R | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| Rapida V1 — target pieno 2R | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1204,83092 | 1204,83092 | 1170,97389 | 809,24477 | 1272,54496 | €18,91 | €56,74 | €1,59 | €0,00 |
| Rapida V1 — target pieno 2R | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| Rapida V1 — target pieno 2R | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 634,78693 | 659,06000 | 640,62867 | 426,36522 | 676,20944 | €506,64 | €1.519,92 | €0,00 | €58,12 |
| Rapida V1 — target pieno 2R | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2395,91909 | 2396,00000 | 2349,05685 | 1609,25899 | 2489,64356 | €9,76 | €29,29 | €0,57 | €0,00 |
| Rapida V1 — target pieno 2R | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €-0,01 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 74,38487 | 75,13000 | 72,40904 | 49,96184 | 77,34862 | €628,95 | €1.886,86 | €50,12 | €18,90 |
| Rapida 1H V3 Filtered — madre | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered — madre | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,81 | €65,43 | €1,80 | €0,00 |
| Rapida 1H V3 Filtered — madre | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13642 | 0,14011 | 0,13061 | 0,09163 | 0,14514 | €387,90 | €1.163,70 | €49,58 | €31,50 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,79186 | 0,80160 | 0,77403 | 0,53186 | 0,81860 | €708,92 | €2.126,75 | €47,89 | €26,16 |
| Rapida 1H V3 Filtered — madre | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41139 | 1,38923 | 1,36370 | 0,94799 | 1,48293 | €19,14 | €57,42 | €1,94 | €-0,90 |
| Rapida 1H V3 Filtered — madre | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €484,23 | €1.452,70 | €50,28 | €-0,29 |
| Rapida 1H V3 Filtered — madre | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21436 | 0,21432 | 0,20782 | 0,14398 | 0,22417 | €12,75 | €38,25 | €1,17 | €-0,01 |
| Rapida V3 — no volatilità HIGH | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| Rapida V3 — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| Rapida V3 — Long Only | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,38487 | 75,13000 | 72,40904 | 49,96184 | 77,34862 | €585,79 | €1.757,36 | €46,68 | €17,60 |
| Rapida V3 — Long Only | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,79186 | 0,80160 | 0,77403 | 0,53186 | 0,81860 | €690,94 | €2.072,82 | €46,67 | €25,50 |
| Rapida V3 — Long Only | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 77900,71703 | 77781,36000 | 76616,30481 | 52323,31494 | 79827,33497 | €45,70 | €137,11 | €2,26 | €-0,21 |
| Rapida V3 — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2395,91909 | 2396,00000 | 2349,05685 | 1609,25899 | 2466,21245 | €12,53 | €37,59 | €0,74 | €0,00 |
| Rapida V3 — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,38951 | 1,38923 | 1,33895 | 0,93329 | 1,46534 | €433,20 | €1.299,61 | €47,28 | €-0,26 |
| Rapida V3 — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,27 | €27,80 | €0,96 | €-0,01 |
| Rapida V3 — senza ESPORTS | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| Rapida V3 — senza ESPORTS | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €18,11 | €54,34 | €1,50 | €0,00 |
| Rapida V3 — senza ESPORTS | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13642 | 0,14011 | 0,13061 | 0,09163 | 0,14514 | €381,97 | €1.145,92 | €48,82 | €31,02 |
| Rapida V3 — senza ESPORTS | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,79186 | 0,80160 | 0,77403 | 0,53186 | 0,81860 | €707,28 | €2.121,84 | €47,78 | €26,10 |
| Rapida V3 — senza ESPORTS | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41139 | 1,38923 | 1,36370 | 0,94799 | 1,48293 | €18,90 | €56,69 | €1,92 | €-0,89 |
| Rapida V3 — senza ESPORTS | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €476,85 | €1.430,56 | €49,51 | €-0,29 |
| Rapida V3 — senza ESPORTS | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21436 | 0,21432 | 0,20782 | 0,14398 | 0,22417 | €12,54 | €37,63 | €1,15 | €-0,01 |
| Rapida V3 senza ESPORTS — Long Only | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,38487 | 75,13000 | 72,40904 | 49,96184 | 77,34862 | €615,25 | €1.845,76 | €49,03 | €18,49 |
| Rapida V3 senza ESPORTS — Long Only | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,79186 | 0,80160 | 0,77403 | 0,53186 | 0,81860 | €725,70 | €2.177,09 | €49,02 | €26,78 |
| Rapida V3 senza ESPORTS — Long Only | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 77900,71703 | 77781,36000 | 76616,30481 | 52323,31494 | 79827,33497 | €48,00 | €144,01 | €2,37 | €-0,22 |
| Rapida V3 senza ESPORTS — Long Only | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21499 | 0,21432 | 0,20838 | 0,14440 | 0,22492 | €8,36 | €25,09 | €0,77 | €-0,08 |
| Rapida V3 senza ESPORTS — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,38951 | 1,38923 | 1,33895 | 0,93329 | 1,46534 | €454,99 | €1.364,97 | €49,66 | €-0,27 |
| Rapida V3 senza ESPORTS — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,72 | €29,17 | €1,01 | €-0,01 |
| Rapida V3 senza ESPORTS — MFE Lock | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,95 | €65,86 | €1,81 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13642 | 0,14011 | 0,13061 | 0,09163 | 0,14514 | €390,41 | €1.171,22 | €49,90 | €31,70 |
| Rapida V3 senza ESPORTS — MFE Lock | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,79186 | 0,80160 | 0,77403 | 0,53186 | 0,81860 | €713,42 | €2.140,26 | €48,19 | €26,33 |
| Rapida V3 senza ESPORTS — MFE Lock | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,41139 | 1,38923 | 1,36370 | 0,94799 | 1,48293 | €19,27 | €57,80 | €1,95 | €-0,91 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €487,37 | €1.462,10 | €50,60 | €-0,29 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21436 | 0,21432 | 0,20782 | 0,14398 | 0,22417 | €12,83 | €38,50 | €1,17 | €-0,01 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 9,97398 | 9,97398 | 10,38253 | 5,03686 | 11,21104 | €560,46 | €1.120,91 | €0,00 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2396,00000 | 2324,55588 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €0,00 | €61,42 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 71,99640 | 75,13000 | 66,32059 | 36,35818 | 87,88866 | €16,69 | €33,38 | €2,63 | €1,45 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 72,36547 | 75,13000 | 72,36547 | 36,54456 | 78,22831 | €640,11 | €1.280,23 | €0,00 | €48,91 |
| Forza relativa 1H V2 | ADA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,21053 | 0,21432 | 0,20337 | 0,10632 | 0,22629 | €707,70 | €1.415,40 | €48,17 | €25,47 |
| Forza relativa 1H V2 | XRP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,38951 | 1,38923 | 1,32451 | 0,70170 | 1,53251 | €518,33 | €1.036,66 | €48,49 | €-0,21 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,51209 | €910,44 | €1.820,87 | €54,32 | €0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 73,54771 | 75,13000 | 70,54476 | 37,14159 | 81,05509 | €82,39 | €164,78 | €6,73 | €3,55 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20285 | 0,21432 | 0,20869 | 0,10244 | 0,22131 | €16,05 | €32,11 | €0,00 | €1,82 |
| Benchmark Donchian breakout 1H | ENA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,12853 | 0,14011 | 0,13436 | 0,06491 | 0,14501 | €19,91 | €39,82 | €0,00 | €3,59 |
| Benchmark Donchian breakout 1H | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,35808 | 1,38923 | 1,30030 | 0,68583 | 1,50254 | €660,67 | €1.321,33 | €56,22 | €30,31 |
| Benchmark Donchian breakout 1H | PEPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €619,14 | €1.238,29 | €54,27 | €55,50 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,51209 | €889,00 | €1.778,00 | €53,04 | €0,00 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 73,54771 | 75,13000 | 70,54476 | 37,14159 | 81,05509 | €80,45 | €160,90 | €6,57 | €3,46 |
| Donchian 1H Gb20 120R V1 | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20285 | 0,21432 | 0,20869 | 0,10244 | 0,22131 | €15,68 | €31,35 | €0,00 | €1,77 |
| Donchian 1H Gb20 120R V1 | ENA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,12853 | 0,14011 | 0,13436 | 0,06491 | 0,14501 | €19,44 | €38,89 | €0,00 | €3,50 |
| Donchian 1H Gb20 120R V1 | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,35808 | 1,38923 | 1,30030 | 0,68583 | 1,50254 | €645,11 | €1.290,22 | €54,90 | €29,59 |
| Donchian 1H Gb20 120R V1 | PEPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €604,57 | €1.209,13 | €52,99 | €54,19 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 69,29086 | 75,13000 | 72,45784 | 34,99188 | 76,51998 | €468,29 | €936,58 | €0,00 | €78,93 |
| Benchmark trend following EMA 1H | LINK | LONG | Trend following EMA | 60m | 2,0x | 10,64413 | 10,64413 | 10,38282 | 5,37528 | 11,21901 | €12,99 | €25,97 | €0,64 | €0,00 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,20930 | 0,21432 | 0,20138 | 0,10570 | 0,22672 | €13,66 | €27,31 | €1,03 | €0,65 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 634,78693 | 659,06000 | 605,19942 | 320,56740 | 699,87944 | €18,06 | €36,12 | €1,68 | €1,38 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €520,88 | €1.041,76 | €0,00 | €46,69 |
| Benchmark trend following EMA 1H | ENA | LONG | Trend following EMA | 60m | 2,0x | 0,13642 | 0,14011 | 0,12811 | 0,06889 | 0,15468 | €365,66 | €731,32 | €44,51 | €19,80 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2396,47920 | 2396,00000 | 2330,99792 | 1210,22200 | 2540,53801 | €28,74 | €57,48 | €1,57 | €-0,01 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | LINK | LONG | Scanner Top 5 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €897,38 | €1.794,76 | €50,51 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 688,04444 | €636,15 | €1.272,31 | €0,00 | €48,65 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €676,64 | €1.353,27 | €0,00 | €60,65 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €95,54 | €191,08 | €8,30 | €-3,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top10 Long | ADA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,20930 | 0,21432 | 0,20930 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €0,00 | €30,86 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 688,04444 | €23,40 | €46,80 | €0,00 | €1,79 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €620,54 | €1.241,09 | €0,00 | €55,62 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €107,93 | €215,87 | €9,38 | €-3,39 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | LINK | LONG | Scanner Top15 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top15 Long | ADA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,20930 | 0,21432 | 0,20930 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €0,00 | €30,86 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 688,04444 | €23,40 | €46,80 | €0,00 | €1,79 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €620,54 | €1.241,09 | €0,00 | €55,62 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 74,38487 | 75,13000 | 71,84452 | 37,56436 | 79,46558 | €122,93 | €245,86 | €8,40 | €2,46 |
| Scanner Top15 Long | SUI | LONG | Scanner Top15 Long | 60m | 2,0x | 0,79596 | 0,80160 | 0,76935 | 0,40196 | 0,84917 | €14,82 | €29,63 | €0,99 | €0,21 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | LINK | LONG | Scanner Top20 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top20 Long | ADA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,20930 | 0,21432 | 0,20930 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €0,00 | €30,86 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 688,04444 | €23,40 | €46,80 | €0,00 | €1,79 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €620,54 | €1.241,09 | €0,00 | €55,62 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 74,38487 | 75,13000 | 71,84452 | 37,56436 | 79,46558 | €122,93 | €245,86 | €8,40 | €2,46 |
| Scanner Top20 Long | SUI | LONG | Scanner Top20 Long | 60m | 2,0x | 0,79596 | 0,80160 | 0,76935 | 0,40196 | 0,84917 | €14,82 | €29,63 | €0,99 | €0,21 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 79,49355 | €663,04 | €1.326,08 | €48,73 | €28,53 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 693,37019 | €604,08 | €1.208,16 | €0,00 | €46,20 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,54629 | €589,43 | €1.178,86 | €51,22 | €-18,51 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €607,11 | €1.214,21 | €51,21 | €24,78 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13715 | 0,14011 | 0,12843 | 0,06926 | 0,15634 | €23,50 | €46,99 | €2,99 | €1,02 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 79,49355 | €621,57 | €1.243,14 | €45,68 | €26,74 |
| Top 5 + BTC — solo MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 693,37019 | €566,29 | €1.132,59 | €0,00 | €43,31 |
| Top 5 + BTC — solo MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,54629 | €552,56 | €1.105,12 | €48,01 | €-17,35 |
| Top 5 + BTC — solo MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €569,13 | €1.138,27 | €48,01 | €23,23 |
| Top 5 + BTC — solo MFE | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13715 | 0,14011 | 0,12843 | 0,06926 | 0,15634 | €22,03 | €44,06 | €2,80 | €0,95 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Top 5 + BTC — Guard | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20843 | 0,21432 | 0,20937 | 0,10526 | 0,22375 | €722,36 | €1.444,72 | €0,00 | €40,81 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 693,37019 | €582,95 | €1.165,89 | €0,00 | €44,58 |
| Top 5 + BTC — Guard | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €619,99 | €1.239,98 | €0,00 | €52,05 |
| Top 5 + BTC — Guard | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,54629 | €45,20 | €90,41 | €3,93 | €-1,42 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20843 | 0,21432 | 0,20937 | 0,10526 | 0,22375 | €705,56 | €1.411,12 | €0,00 | €39,87 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 693,37019 | €569,39 | €1.138,78 | €0,00 | €43,54 |
| Top 5 + BTC — Guard + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €605,57 | €1.211,14 | €0,00 | €50,84 |
| Top 5 + BTC — Guard + MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,54629 | €44,15 | €88,31 | €3,84 | €-1,39 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,55211 | 10,55211 | 10,31704 | 5,32882 | 11,25731 | €17,19 | €34,38 | €0,77 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 81,65567 | €64,00 | €127,99 | €4,70 | €2,75 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,21432 | 0,20947 | 0,10244 | 0,22278 | €32,84 | €65,68 | €0,00 | €3,71 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 714,67320 | €589,21 | €1.178,42 | €0,00 | €45,06 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €643,33 | €1.286,66 | €0,00 | €57,66 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,59535 | €586,88 | €1.173,77 | €51,00 | €-18,43 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13715 | 0,14011 | 0,12843 | 0,06926 | 0,16331 | €355,10 | €710,19 | €45,16 | €15,34 |
| Top 5 + BTC — target pieno 3R | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,55211 | 10,55211 | 10,31704 | 5,32882 | 11,25731 | €17,20 | €34,40 | €0,77 | €0,00 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 81,65567 | €64,03 | €128,07 | €4,71 | €2,76 |
| Top 5 + BTC — target pieno 3R | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,21432 | 0,20947 | 0,10244 | 0,22278 | €32,86 | €65,72 | €0,00 | €3,72 |
| Top 5 + BTC — target pieno 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 714,67320 | €589,56 | €1.179,11 | €0,00 | €45,09 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €643,71 | €1.287,41 | €0,00 | €57,70 |
| Top 5 + BTC — target pieno 3R | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,59535 | €587,23 | €1.174,45 | €51,02 | €-18,44 |
| Top 5 + BTC — target pieno 3R | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13715 | 0,14011 | 0,12843 | 0,06926 | 0,16331 | €355,30 | €710,61 | €45,19 | €15,35 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 69,29086 | 75,13000 | 72,45784 | 34,99188 | 76,51998 | €482,28 | €964,56 | €0,00 | €81,28 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,95 | €25,90 | €0,00 | €1,94 |
| Combo Trend | ENA | LONG | Combo Trend | 60m | 2,0x | 0,13642 | 0,14011 | 0,12811 | 0,06889 | 0,15468 | €386,42 | €772,83 | €47,04 | €20,92 |
| Combo Trend | SUI | LONG | Combo Trend | 60m | 2,0x | 0,79186 | 0,80160 | 0,76639 | 0,39989 | 0,84789 | €731,11 | €1.462,22 | €47,03 | €17,99 |
| Combo Trend | XRP | LONG | Combo Trend | 60m | 2,0x | 1,38951 | 1,38923 | 1,31729 | 0,70170 | 1,54840 | €17,08 | €34,15 | €1,78 | €-0,01 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 79,49355 | €636,13 | €1.272,26 | €46,75 | €27,37 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 634,78693 | 659,06000 | 637,55678 | 320,56740 | 693,37019 | €579,56 | €1.159,12 | €0,00 | €44,32 |
| Combo Scanner | XRP | LONG | Combo Scanner | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,54629 | €565,51 | €1.131,02 | €49,14 | €-17,76 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €582,47 | €1.164,94 | €49,13 | €23,78 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,13715 | 0,14011 | 0,12843 | 0,06926 | 0,15634 | €22,54 | €45,09 | €2,87 | €0,97 |
| Combo Adaptive — madre | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive — madre | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,02180 | 75,13000 | 71,44110 | 37,38101 | 79,18321 | €17,24 | €34,48 | €1,20 | €0,52 |
| Combo Adaptive — madre | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20506 | 0,21432 | 0,20957 | 0,10356 | 0,21928 | €32,01 | €64,01 | €0,00 | €2,89 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 634,78693 | 659,06000 | 639,09273 | 320,56740 | 688,04444 | €615,29 | €1.230,58 | €0,00 | €47,06 |
| Combo Adaptive — madre | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2409,04171 | 2396,00000 | 2354,66913 | 1216,56606 | 2517,78687 | €1.151,19 | €2.302,39 | €51,97 | €-12,46 |
| Combo Adaptive — madre | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,79186 | 0,80160 | 0,76893 | 0,39989 | 0,83771 | €890,96 | €1.781,92 | €51,59 | €21,92 |
| Combo Adaptive — madre | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,38951 | 1,38923 | 1,32451 | 0,70170 | 1,51951 | €28,85 | €57,71 | €2,70 | €-0,01 |
| Combo Adaptive — MFE Trail esistente | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €577,45 | €1.154,90 | €0,00 | €48,48 |
| Combo Adaptive — MFE Trail esistente | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,21195 | 0,21432 | 0,20443 | 0,10704 | 0,22700 | €641,59 | €1.283,17 | €45,54 | €14,33 |
| Combo Adaptive — MFE Trail esistente | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,38487 | 75,13000 | 71,84452 | 37,56436 | 79,46558 | €666,73 | €1.333,46 | €45,54 | €13,36 |
| Combo Adaptive — MFE Trail esistente | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,79186 | 0,80160 | 0,76893 | 0,39989 | 0,83771 | €768,89 | €1.537,77 | €44,52 | €18,92 |
| Combo Adaptive — MFE Trail esistente | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €27,35 | €54,69 | €2,38 | €-0,86 |
| Combo Adaptive — Quality7 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive — Quality7 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 78,95302 | €638,10 | €1.276,19 | €46,90 | €27,46 |
| Combo Adaptive — Quality7 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2339,94790 | 2396,00000 | 2364,59527 | 1181,67369 | 2458,22812 | €39,02 | €78,04 | €0,00 | €1,87 |
| Combo Adaptive — Quality7 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €552,07 | €1.104,13 | €47,97 | €-17,34 |
| Combo Adaptive — Quality7 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €567,37 | €1.134,75 | €47,86 | €23,16 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive — Trend/Transition | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 78,95302 | €680,15 | €1.360,29 | €49,99 | €29,27 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 78,95302 | €653,66 | €1.307,32 | €48,04 | €28,13 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,71874 | 75,13000 | 71,23745 | 37,22796 | 78,68131 | €18,24 | €36,48 | €1,23 | €0,70 |
| Combo Adaptive — Long Only | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €634,42 | €1.268,83 | €0,00 | €53,26 |
| Combo Adaptive — Long Only | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2409,04171 | 2396,00000 | 2354,66913 | 1216,56606 | 2517,78687 | €1.149,88 | €2.299,77 | €51,91 | €-12,45 |
| Combo Adaptive — Long Only | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,79186 | 0,80160 | 0,76893 | 0,39989 | 0,83771 | €896,33 | €1.792,67 | €51,90 | €22,05 |
| Combo Adaptive — Long Only | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €598,96 | €1.197,93 | €52,04 | €-18,81 |
| Combo Adaptive — Long Only | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,21499 | 0,21432 | 0,20648 | 0,10857 | 0,23201 | €16,58 | €33,17 | €1,31 | €-0,10 |
| Combo Adaptive — parziale 1R | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,02180 | 75,13000 | 71,44110 | 37,38101 | 79,18321 | €16,14 | €32,28 | €1,13 | €0,48 |
| Combo Adaptive — parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20843 | 0,21432 | 0,20976 | 0,10526 | 0,22236 | €13,54 | €27,09 | €0,00 | €0,77 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 634,78693 | 659,06000 | 639,09273 | 320,56740 | 688,04444 | €591,05 | €1.182,09 | €0,00 | €45,20 |
| Combo Adaptive — parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €632,84 | €1.265,67 | €0,00 | €56,72 |
| Combo Adaptive — parziale 1R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2409,04171 | 2396,00000 | 2354,66913 | 1216,56606 | 2517,78687 | €1.105,80 | €2.211,59 | €49,92 | €-11,97 |
| Combo Adaptive — parziale 1R | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €33,48 | €66,97 | €2,91 | €-1,05 |
| Combo Adaptive — parziale 1R | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,80176 | 0,80160 | 0,77495 | 0,40489 | 0,85539 | €18,86 | €37,72 | €1,26 | €-0,01 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 75,13000 | 70,84505 | 37,14159 | 78,95302 | €661,99 | €1.323,97 | €48,65 | €28,48 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 85,47309 | 91,46400 | 89,30548 | 43,16391 | 93,75681 | €727,07 | €1.454,13 | €0,00 | €101,92 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 85,47309 | 91,46400 | 89,30548 | 43,16391 | 93,54165 | €665,34 | €1.330,67 | €0,00 | €93,27 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2395,91909 | 2396,00000 | 2335,66764 | 1609,25899 | 2516,42198 | €651,23 | €1.953,70 | €49,13 | €0,07 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2258,11153 | 2396,00000 | 2338,55656 | 1140,34632 | 2498,75762 | €577,20 | €1.154,41 | €0,00 | €70,49 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2409,04171 | 2396,00000 | 2360,71053 | 1618,07302 | 2505,70408 | €826,55 | €2.479,66 | €49,75 | €-13,42 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2409,04171 | 2396,00000 | 2354,66913 | 1618,07302 | 2517,78687 | €729,50 | €2.188,49 | €49,39 | €-11,85 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive — Side × Regime Guard | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 72,76855 | 75,13000 | 72,76855 | 36,74812 | 77,95329 | €23,38 | €46,77 | €0,00 | €1,52 |
| Combo Adaptive — Side × Regime Guard | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20930 | 0,21432 | 0,20948 | 0,10570 | 0,22405 | €721,85 | €1.443,70 | €0,00 | €34,61 |
| Combo Adaptive — Side × Regime Guard | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €657,55 | €1.315,11 | €0,00 | €58,94 |
| Combo Adaptive — Side × Regime Guard | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2409,04171 | 2396,00000 | 2354,66913 | 1216,56606 | 2517,78687 | €1.148,99 | €2.297,97 | €51,87 | €-12,44 |
| Combo Adaptive — Side × Regime Guard | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,79186 | 0,80160 | 0,76893 | 0,39989 | 0,83771 | €860,36 | €1.720,72 | €49,81 | €21,17 |
| Combo Adaptive — Side × Regime Guard | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,41139 | 1,38923 | 1,35007 | 0,71275 | 1,53403 | €26,89 | €53,77 | €2,34 | €-0,84 |
| Master Adaptive GB20 — Loss Cap 0,75R | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 71,99640 | 75,13000 | 67,63039 | 48,35758 | 80,72841 | €287,94 | €863,83 | €52,38 | €37,60 |
| Combo Trend — Side × Regime Guard | LINK | LONG | Combo Trend | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,41622 | €12,55 | €25,10 | €0,75 | €0,00 |
| Combo Trend — Side × Regime Guard | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €630,61 | €1.261,22 | €0,00 | €56,52 |
| Combo Trend — Side × Regime Guard | HYPE | LONG | Combo Trend | 60m | 2,0x | 74,38487 | 75,13000 | 71,56226 | 37,56436 | 80,59463 | €728,24 | €1.456,48 | €55,27 | €14,59 |
| Combo Trend — Side × Regime Guard | XRP | LONG | Combo Trend | 60m | 2,0x | 1,41139 | 1,38923 | 1,34326 | 0,71275 | 1,56128 | €574,17 | €1.148,35 | €55,43 | €-18,03 |
| Combo Trend — Side × Regime Guard | ENA | LONG | Combo Trend | 60m | 2,0x | 0,13715 | 0,14011 | 0,12746 | 0,06926 | 0,15847 | €378,29 | €756,58 | €53,46 | €16,34 |
| Combo Trend — Side × Regime Guard | ADA | LONG | Combo Trend | 60m | 2,0x | 0,21436 | 0,21432 | 0,20502 | 0,10825 | 0,23491 | €26,14 | €52,28 | €2,28 | €-0,01 |
| FAST NoHigh <7,5 · SHORT only | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| Bilanciata V3 · LONG only | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 72,76855 | 75,13000 | 72,76855 | 48,87621 | 77,95329 | €12,30 | €36,91 | €0,00 | €1,20 |
| Bilanciata V3 · LONG only | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20930 | 0,21432 | 0,20930 | 0,14058 | 0,22355 | €10,55 | €31,64 | €0,00 | €0,76 |
| Bilanciata V3 · LONG only | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 634,78693 | 659,06000 | 637,55678 | 426,36522 | 688,04444 | €379,47 | €1.138,42 | €0,00 | €43,53 |
| Bilanciata V3 · LONG only | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €403,35 | €1.210,04 | €0,00 | €54,23 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2395,91909 | 2396,00000 | 2335,66764 | 1609,25899 | 2516,42198 | €12,22 | €36,66 | €0,92 | €0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend — Side × Regime Guard | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 660,04219 | €3,33 | 2,16 | TARGET |
| Combo Adaptive — madre | PEPE | LONG | 2026-08-21T11:06:19+00:00 | 0,00000 | €2,59 | 1,96 | TARGET |
| Ampia 4H | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 659,82159 | €10,33 | 2,77 | TARGET |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 665,72064 | €72,42 | 1,46 | TARGET |
| Rapida V3 senza ESPORTS — Long Only | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 665,72064 | €71,14 | 1,46 | TARGET |
| Rapida V3 — senza ESPORTS | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 665,72064 | €70,85 | 1,46 | TARGET |
| Rapida V3 — Long Only | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 665,72064 | €67,73 | 1,46 | TARGET |
| Rapida 1H V3 Filtered — madre | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 665,72064 | €71,96 | 1,46 | TARGET |
| Rapida V1 — target pieno 2R | XRP | LONG | 2026-08-21T11:06:19+00:00 | 1,36744 | €0,52 | 0,19 | STOP_GAP_STRESS |
| Rapida V1 — target pieno 2R | PEPE | LONG | 2026-08-21T11:06:19+00:00 | 0,00000 | €3,88 | 1,95 | TARGET |
| Rapida V1 — senza PEPE | ZEC | LONG | 2026-08-21T11:06:19+00:00 | 659,78649 | €75,22 | 1,46 | TARGET |
| Rapida score 6–7,5 — Cost Aware | PEPE | LONG | 2026-08-21T11:06:19+00:00 | 0,00000 | €80,36 | 1,45 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 471/30 | 33/30 | 0,83 | 2,04 | -0,09R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 433/30 | 20/30 | 0,76 | 1,90 | -0,12R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 223/30 | 22/30 | 0,81 | 1,74 | -0,10R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 226/30 | 22/30 | 0,78 | 1,57 | -0,11R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 385/30 | 31/30 | 0,94 | 0,62 | -0,03R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 350/30 | 11/30 | 0,90 | 0,00 | -0,05R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 130/30 | 8/30 | 0,75 | 1,02 | -0,13R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 285/30 | 17/30 | 0,62 | 4,50 | -0,21R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 450/30 | 24/30 | 0,70 | 0,64 | -0,16R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 412/30 | 7/30 | 0,60 | 0,02 | -0,21R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 385/30 | 30/30 | 0,97 | 1,02 | -0,02R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 656/30 | 55/30 | 0,89 | 1,12 | -0,05R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 125/30 | 15/30 | 0,49 | 0,99 | -0,33R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 589/30 | 44/30 | 0,79 | 1,20 | -0,10R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 593/30 | 37/30 | 0,79 | 0,76 | -0,10R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 547/30 | 23/30 | 0,71 | 1,12 | -0,14R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 306/30 | 47/30 | 0,74 | 0,83 | -0,15R | €-5,09 | 6,39% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 12/30 | 0,00 | 1,74 | 0,00R | €17,78 | 1,54% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 30/30 | 0,00 | 1,93 | 0,00R | €19,39 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 46/30 | 27/30 | 0,59 | 0,52 | -0,22R | €-2,67 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 742/30 | 120/30 | 0,92 | 0,69 | -0,04R | €-7,07 | 13,99% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 73/30 | 0,00 | 0,83 | 0,00R | €-4,16 | 9,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 13/30 | 0,00 | 1,13 | 0,00R | €2,73 | 1,80% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 248/30 | 76/30 | 1,15 | 0,76 | 0,08R | €-5,62 | 8,84% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 465/30 | 126/30 | 1,01 | 1,04 | 0,00R | €0,85 | 9,12% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 386/30 | 82/30 | 0,94 | 0,75 | -0,03R | €-5,37 | 8,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 189/30 | 40/30 | 0,92 | 1,13 | -0,04R | €3,16 | 3,73% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 463/30 | 85/30 | 0,82 | 0,88 | -0,09R | €-2,59 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 530/30 | 121/30 | 0,86 | 1,01 | -0,07R | €0,24 | 7,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 804/30 | 158/30 | 0,83 | 1,26 | -0,09R | €4,75 | 4,46% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 102/30 | 0,00 | 1,56 | 0,00R | €11,22 | 4,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 88/30 | 0,00 | 0,78 | 0,00R | €-6,98 | 9,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 38/30 | 0,00 | 1,14 | 0,00R | €3,94 | 3,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 461/30 | 130/30 | 0,86 | 0,90 | -0,07R | €-2,79 | 9,66% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 766/30 | 174/30 | 0,81 | 1,03 | -0,10R | €0,56 | 6,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 54/30 | 32/30 | 0,69 | 1,03 | -0,17R | €0,68 | 3,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 758/30 | 182/30 | 0,84 | 1,00 | -0,08R | €-0,02 | 9,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 560/30 | 126/30 | 0,85 | 0,80 | -0,07R | €-5,12 | 11,75% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 264/30 | 83/30 | 0,93 | 0,76 | -0,04R | €-7,33 | 7,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 268/30 | 78/30 | 0,90 | 0,78 | -0,05R | €-6,19 | 6,59% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 454/30 | 118/30 | 0,95 | 0,80 | -0,02R | €-4,94 | 12,52% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 41/30 | 0,00 | 1,25 | 0,00R | €6,05 | 3,97% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 63/30 | 0,00 | 1,10 | 0,00R | €2,24 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 560/30 | 111/30 | 0,77 | 0,80 | -0,12R | €-5,08 | 6,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 98/30 | 0,00 | 0,95 | 0,00R | €-1,12 | 10,60% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 138/30 | 0,00 | 1,02 | 0,00R | €0,43 | 9,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 41/30 | 0,00 | 1,01 | 0,00R | €0,34 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 711/30 | 154/30 | 0,81 | 0,93 | -0,10R | €-1,33 | 9,00% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 292/30 | 46/30 | 0,79 | 1,06 | -0,14R | €1,54 | 4,45% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 239/30 | 81/30 | 1,07 | 0,55 | 0,03R | €-15,55 | 14,60% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 12/30 | 6/30 | 0,91 | 1,77 | -0,04R | €13,88 | 1,13% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 2/30 | 2/30 | 2,26 | 2,39 | 0,67R | €35,09 | 0,96% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 2/30 | 2/30 | 1,56 | 1,54 | 0,31R | €14,72 | 0,82% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 15/30 | 8/30 | 0,38 | 1,41 | -0,46R | €8,50 | 1,49% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 6/30 | 4/30 | 0,50 | 0,80 | -0,45R | €-8,55 | 2,43% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 16/30 | 10/30 | 0,99 | 0,82 | -0,01R | €-5,78 | 1,94% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 4/30 | 3/30 | 0,75 | 1,19 | -0,20R | €6,47 | 1,76% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 609/30 | 114/30 | 1,02 | 1,20 | 0,01R | €3,54 | 7,91% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 358/30 | 82/30 | 1,09 | 1,23 | 0,04R | €4,75 | 6,25% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 661/30 | 121/30 | 1,05 | 0,65 | 0,02R | €-7,32 | 15,45% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 550/30 | 113/30 | 0,97 | 1,00 | -0,01R | €-0,05 | 8,69% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 75/30 | 30/30 | 1,44 | 0,84 | 0,19R | €-4,30 | 4,21% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 75/30 | 30/30 | 1,45 | 0,69 | 0,19R | €-8,44 | 5,41% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 183/30 | 58/30 | 1,03 | 0,74 | 0,02R | €-7,31 | 8,88% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 221/30 | 43/30 | 0,97 | 0,78 | -0,01R | €-6,41 | 5,38% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 94/30 | 0,74 | 0,53 | -0,20R | €-11,02 | 12,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 85/30 | 0,00 | 1,22 | 0,00R | €4,20 | 8,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 75/30 | 0,74 | 0,38 | -0,20R | €-16,04 | 12,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 92/30 | 37/30 | 1,24 | 0,48 | 0,11R | €-23,92 | 10,64% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 381/30 | 99/30 | 1,14 | 0,92 | 0,07R | €-1,99 | 11,38% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 508/30 | 133/30 | 0,97 | 0,80 | -0,02R | €-4,98 | 10,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 77/30 | 0,00 | 1,77 | 0,00R | €13,72 | 4,33% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 9/30 | 7/30 | 1,86 | 1,28 | 0,32R | €6,71 | 1,89% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 13/30 | 11/30 | 0,46 | 0,49 | -0,42R | €-16,72 | 2,90% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 19/30 | 14/30 | 0,37 | 0,77 | -0,44R | €-5,65 | 2,61% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 253/30 | 80/30 | 0,93 | 1,71 | -0,05R | €15,49 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 183/30 | 48/30 | 0,95 | 2,12 | -0,03R | €20,31 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 511/30 | 99/30 | 0,97 | 0,58 | -0,01R | €-9,46 | 12,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 18/30 | 10/30 | 0,54 | 0,63 | -0,34R | €-12,11 | 3,14% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 12/30 | 6/30 | 1,35 | 0,04 | 0,16R | €-60,94 | 4,14% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 17/30 | 9/30 | 0,52 | 0,85 | -0,38R | €-5,60 | 2,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 25/30 | 14/30 | 0,44 | 0,66 | -0,42R | €-12,42 | 4,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 4/30 | 3/30 | 0,00 | 0,00 | -1,06R | €-52,67 | 1,83% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 13/30 | 16/30 | 0,78 | 0,32 | -0,15R | €-23,25 | 3,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 276/30 | 61/30 | 1,04 | 0,66 | 0,02R | €-11,15 | 7,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 55/30 | 0,00 | 0,62 | 0,00R | €-11,41 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 42/30 | 0,00 | 0,53 | 0,00R | €-17,80 | 11,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 50/30 | 0,00 | 0,60 | 0,00R | €-12,75 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 506/30 | 87/30 | 1,43 | 0,60 | 0,14R | €-9,17 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 244/30 | 58/30 | 1,06 | 0,67 | 0,03R | €-11,13 | 7,26% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 253/30 | 51/30 | 1,02 | 0,66 | 0,01R | €-12,19 | 8,18% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 175/30 | 53/30 | 1,02 | 0,59 | 0,01R | €-17,80 | 11,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 266/30 | 52/30 | 1,00 | 0,62 | 0,00R | €-12,96 | 7,80% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 624/30 | 105/30 | 0,89 | 0,47 | -0,06R | €-14,80 | 17,39% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 239/30 | 87/30 | 1,21 | 0,87 | 0,10R | €-4,11 | 10,88% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 211/30 | 67/30 | 0,49 | 0,67 | -0,29R | €-9,16 | 8,28% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 211/30 | 67/30 | 0,49 | 0,67 | -0,29R | €-9,16 | 8,28% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 211/30 | 67/30 | 0,49 | 0,67 | -0,29R | €-9,16 | 8,28% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 244/30 | 86/30 | 0,66 | 0,66 | -0,19R | €-8,89 | 9,40% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 248/30 | 58/30 | 0,75 | 0,60 | -0,12R | €-11,70 | 8,30% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 225/30 | 59/30 | 0,66 | 0,58 | -0,16R | €-11,74 | 8,30% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 340/30 | 83/30 | 1,10 | 0,87 | 0,05R | €-2,69 | 10,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 341/30 | 83/30 | 1,09 | 0,87 | 0,04R | €-2,69 | 10,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 341/30 | 83/30 | 1,09 | 0,87 | 0,04R | €-2,69 | 10,31% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 368/30 | 95/30 | 1,16 | 1,10 | 0,08R | €2,30 | 11,27% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 128/30 | 13/30 | 0,83 | 0,41 | -0,10R | €-22,20 | 4,35% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 288/30 | 59/30 | 0,94 | 0,57 | -0,03R | €-12,93 | 11,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 304/30 | 73/30 | 1,18 | 0,73 | 0,07R | €-7,80 | 7,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 254/30 | 58/30 | 1,05 | 0,78 | 0,02R | €-6,97 | 7,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 356/30 | 94/30 | 1,25 | 0,80 | 0,10R | €-4,85 | 8,78% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 295/30 | 77/30 | 1,15 | 0,88 | 0,07R | €-2,97 | 7,34% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 399/30 | 87/30 | 1,15 | 0,78 | 0,06R | €-4,84 | 12,28% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 317/30 | 81/30 | 1,08 | 1,08 | 0,04R | €1,93 | 12,06% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 300/30 | 77/30 | 1,10 | 1,08 | 0,05R | €2,10 | 11,78% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 404/30 | 106/30 | 1,16 | 1,31 | 0,08R | €6,49 | 8,85% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 26/30 | 13/30 | 0,48 | 0,56 | -0,42R | €-15,26 | 4,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 6/30 | 4/30 | 1,69 | 1,47 | 0,36R | €12,27 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 16/30 | 8/30 | 1,08 | 0,66 | 0,04R | €-13,38 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 4/30 | 3/30 | 3,94 | 0,83 | 0,77R | €-6,09 | 1,22% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 20/30 | 11/30 | 0,69 | 1,24 | -0,23R | €5,41 | 2,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 6/30 | 4/30 | 0,96 | 1,63 | -0,03R | €16,58 | 1,05% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 24/30 | 12/30 | 0,62 | 0,85 | -0,30R | €-4,75 | 3,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 7/30 | 6/30 | 0,38 | 1,16 | -0,56R | €5,42 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.08451**
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
| BTC sotto filtro | 77781.36 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, bearish_confirmation, stop_within_limit**
- High **0.08469**; close **0.08455**; wick alta **18.9%**; volume **x0.53**

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
- Confidenza: **83,40%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +2.10%, 64% oltre +1%.
- BTC trend score: **4,00**; ADX: **57,12**; breadth sopra EMA50: **100,00%**
- Mediana alt vs BTC: **2,10%**; dispersione: **9,75%**

- Aperti in questo ciclo: **48**
- Chiusi in questo ciclo: **60**
- Posizioni research aperte: **514**
- Trade research chiusi: **29548**
- Eventi di mercato indipendenti chiusi: **3993**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **73201**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 8 | 471 | 471 | 32,70% | 0,83 | -0,09R | €-403,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 9 | 433 | 433 | 31,64% | 0,76 | -0,12R | €-524,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 0 | 223 | 223 | 45,74% | 0,81 | -0,10R | €-226,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 0 | 226 | 226 | 32,74% | 0,78 | -0,11R | €-253,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 11 | 385 | 385 | 35,06% | 0,94 | -0,03R | €-119,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 10 | 350 | 350 | 35,14% | 0,90 | -0,05R | €-169,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 130 | 130 | 35,38% | 0,75 | -0,13R | €-164,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 0 | 285 | 285 | 27,72% | 0,62 | -0,21R | €-607,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 0 | 450 | 450 | 29,56% | 0,70 | -0,16R | €-711,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 0 | 412 | 412 | 28,40% | 0,60 | -0,21R | €-855,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 11 | 385 | 385 | 35,58% | 0,97 | -0,02R | €-59,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 10 | 656 | 656 | 40,55% | 0,89 | -0,05R | €-313,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 0 | 125 | 125 | 30,40% | 0,49 | -0,33R | €-417,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 12 | 589 | 589 | 31,41% | 0,79 | -0,10R | €-616,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 12 | 593 | 593 | 31,37% | 0,79 | -0,10R | €-616,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 11 | 547 | 547 | 30,35% | 0,71 | -0,14R | €-785,74 |
| MAIN | 12 | 306 | 306 | 26,80% | 0,74 | -0,15R | €-468,40 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 46 | 46 | 36,96% | 0,59 | -0,22R | €-102,23 |
| Bilanciata 1H V1 | 17 | 742 | 742 | 34,77% | 0,92 | -0,04R | €-309,05 |
| Bilanciata 1H V2 | 8 | 285 | 248 | 38,95% | 1,15 | 0,08R | €221,85 |
| Bilanciata 1H V3 Filtered | 12 | 465 | 465 | 36,77% | 1,01 | 0,00R | €17,50 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 12 | 386 | 386 | 36,27% | 0,94 | -0,03R | €-127,85 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 189 | 189 | 38,10% | 0,92 | -0,04R | €-70,27 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 0 | 463 | 463 | 34,77% | 0,82 | -0,09R | €-419,30 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 0 | 530 | 530 | 35,85% | 0,86 | -0,07R | €-384,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 14 | 804 | 804 | 35,45% | 0,83 | -0,09R | €-706,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 461 | 461 | 36,44% | 0,86 | -0,07R | €-332,83 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 766 | 766 | 32,51% | 0,81 | -0,10R | €-760,94 |
| Rapida 1H V2 | 1 | 63 | 54 | 39,68% | 0,69 | -0,17R | €-109,44 |
| Rapida 1H V3 Filtered | 12 | 758 | 758 | 35,75% | 0,84 | -0,08R | €-600,19 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 7 | 560 | 560 | 36,43% | 0,85 | -0,07R | €-410,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 0 | 264 | 264 | 47,35% | 0,93 | -0,04R | €-100,28 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 0 | 268 | 268 | 37,31% | 0,90 | -0,05R | €-135,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 10 | 454 | 454 | 38,77% | 0,95 | -0,02R | €-101,72 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 0 | 560 | 560 | 33,57% | 0,77 | -0,12R | €-684,48 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 12 | 711 | 711 | 35,02% | 0,81 | -0,10R | €-682,14 |
| SHADOW_4H_WIDE | 23 | 292 | 292 | 21,58% | 0,79 | -0,14R | €-408,27 |
| SHADOW_BOLLINGER_MR_1H | 4 | 239 | 239 | 46,03% | 1,07 | 0,03R | €78,84 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 12 | 12 | 58,33% | 0,91 | -0,04R | €-4,88 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 2 | 2 | 50,00% | 2,26 | 0,67R | €13,50 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 2 | 2 | 50,00% | 1,56 | 0,31R | €6,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 15 | 15 | 33,33% | 0,38 | -0,46R | €-69,25 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 6 | 6 | 16,67% | 0,50 | -0,45R | €-26,75 |
| SHADOW_BTC_EMA_1H | 0 | 16 | 16 | 50,00% | 0,99 | -0,01R | €-0,90 |
| SHADOW_BTC_EMA_4H | 0 | 4 | 4 | 25,00% | 0,75 | -0,20R | €-8,17 |
| SHADOW_COMBO_ADAPTIVE | 13 | 609 | 609 | 38,26% | 1,02 | 0,01R | €63,40 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 10 | 358 | 358 | 39,39% | 1,09 | 0,04R | €153,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 10 | 661 | 661 | 41,75% | 1,05 | 0,02R | €134,42 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 13 | 550 | 550 | 40,73% | 0,97 | -0,01R | €-71,01 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 75 | 75 | 48,00% | 1,44 | 0,19R | €138,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 75 | 75 | 41,33% | 1,45 | 0,19R | €141,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 5 | 183 | 183 | 35,52% | 1,03 | 0,02R | €29,04 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 1 | 221 | 221 | 37,56% | 0,97 | -0,01R | €-29,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 92 | 92 | 50,00% | 1,24 | 0,11R | €98,52 |
| SHADOW_COMBO_SCANNER | 7 | 381 | 381 | 37,27% | 1,14 | 0,07R | €273,31 |
| SHADOW_COMBO_TREND | 15 | 508 | 508 | 33,66% | 0,97 | -0,02R | €-81,81 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 9 | 9 | 66,67% | 1,86 | 0,32R | €28,99 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 13 | 13 | 30,77% | 0,46 | -0,42R | €-54,31 |
| SHADOW_DOGE_EMA_1H | 0 | 19 | 19 | 26,32% | 0,37 | -0,44R | €-84,28 |
| SHADOW_DONCHIAN_1H | 10 | 253 | 253 | 32,02% | 0,93 | -0,05R | €-116,76 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 10 | 183 | 183 | 34,43% | 0,95 | -0,03R | €-51,67 |
| SHADOW_EMA_TREND_1H | 16 | 511 | 511 | 33,66% | 0,97 | -0,01R | €-72,62 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 18 | 18 | 33,33% | 0,54 | -0,34R | €-61,09 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 12 | 12 | 58,33% | 1,35 | 0,16R | €19,48 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 17 | 17 | 29,41% | 0,52 | -0,38R | €-64,95 |
| SHADOW_ETH_EMA_1H | 1 | 25 | 25 | 32,00% | 0,44 | -0,42R | €-104,47 |
| SHADOW_ETH_EMA_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,33 |
| SHADOW_GLOBAL_PURE | 0 | 13 | 13 | 38,46% | 0,78 | -0,15R | €-19,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 1 | 276 | 276 | 32,97% | 1,04 | 0,02R | €60,60 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 1 | 506 | 506 | 66,60% | 1,43 | 0,14R | €691,48 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 1 | 244 | 244 | 33,20% | 1,06 | 0,03R | €83,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 1 | 253 | 253 | 31,23% | 1,02 | 0,01R | €31,35 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 0 | 175 | 175 | 32,57% | 1,02 | 0,01R | €19,45 |
| SHADOW_MASTER_ADAPTIVE_V1 | 1 | 266 | 266 | 32,33% | 1,00 | 0,00R | €6,06 |
| Forza relativa 1H V1 | 17 | 624 | 624 | 30,61% | 0,89 | -0,06R | €-363,72 |
| Forza relativa 1H V2 | 8 | 256 | 239 | 37,11% | 1,21 | 0,10R | €266,42 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 4 | 211 | 211 | 26,07% | 0,49 | -0,29R | €-621,68 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 4 | 211 | 211 | 26,07% | 0,49 | -0,29R | €-621,68 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 4 | 211 | 211 | 26,07% | 0,49 | -0,29R | €-621,68 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 4 | 244 | 244 | 28,69% | 0,66 | -0,19R | €-459,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 4 | 248 | 248 | 51,61% | 0,75 | -0,12R | €-286,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 4 | 225 | 225 | 50,67% | 0,66 | -0,16R | €-352,72 |
| SHADOW_SCANNER_TOP10_LONG | 11 | 340 | 340 | 38,24% | 1,10 | 0,05R | €157,11 |
| SHADOW_SCANNER_TOP15_LONG | 12 | 341 | 341 | 38,12% | 1,09 | 0,04R | €146,03 |
| SHADOW_SCANNER_TOP20_LONG | 12 | 341 | 341 | 38,12% | 1,09 | 0,04R | €146,03 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 368 | 368 | 36,96% | 1,16 | 0,08R | €305,46 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 128 | 128 | 30,47% | 0,83 | -0,10R | €-122,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 1 | 288 | 288 | 33,33% | 0,94 | -0,03R | €-86,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 1 | 304 | 304 | 44,74% | 1,18 | 0,07R | €222,09 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 1 | 254 | 254 | 35,43% | 1,05 | 0,02R | €59,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 6 | 356 | 356 | 46,07% | 1,25 | 0,10R | €363,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 6 | 295 | 295 | 37,63% | 1,15 | 0,07R | €219,37 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 6 | 399 | 399 | 44,61% | 1,15 | 0,06R | €247,59 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 317 | 317 | 35,33% | 1,08 | 0,04R | €132,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 300 | 300 | 34,33% | 1,10 | 0,05R | €148,75 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 404 | 404 | 38,12% | 1,16 | 0,08R | €321,35 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 26 | 26 | 26,92% | 0,48 | -0,42R | €-108,57 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 6 | 6 | 50,00% | 1,69 | 0,36R | €21,88 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 16 | 16 | 56,25% | 1,08 | 0,04R | €6,28 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 4 | 4 | 75,00% | 3,94 | 0,77R | €30,86 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 20 | 20 | 35,00% | 0,69 | -0,23R | €-45,59 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 6 | 6 | 33,33% | 0,96 | -0,03R | €-1,68 |
| SHADOW_SOL_EMA_1H | 0 | 24 | 24 | 29,17% | 0,62 | -0,30R | €-71,27 |
| SHADOW_SOL_EMA_4H | 0 | 7 | 7 | 14,29% | 0,38 | -0,56R | €-39,32 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 23,91% | 0,53 | -0,29R | €-131,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 8 | 89 | 89 | 43,82% | 1,41 | 0,18R | €159,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 0 | 118 | 118 | 33,90% | 0,63 | -0,19R | €-227,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 0 | 19 | 19 | 31,58% | 0,71 | -0,15R | €-28,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 55 | 55 | 32,73% | 1,01 | 0,01R | €3,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,56 | -0,26R | €-152,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 53 | 53 | 16,98% | 0,45 | -0,28R | €-147,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 50,00% | 2,30 | 0,44R | €131,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 22,73% | 0,37 | -0,43R | €-189,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 9 | 73 | 73 | 42,47% | 1,39 | 0,17R | €121,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 0 | 111 | 111 | 33,33% | 0,54 | -0,24R | €-269,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,69 | -0,17R | €-30,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 54 | 54 | 33,33% | 1,11 | 0,05R | €26,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,52 | -0,27R | €-150,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 50 | 50 | 16,00% | 0,30 | -0,38R | €-188,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 51,85% | 2,75 | 0,58R | €157,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 8 | 8 | 50,00% | 1,03 | 0,02R | €1,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 68 | 68 | 39,71% | 0,51 | -0,31R | €-208,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 33 | 33 | 54,55% | 1,17 | 0,07R | €22,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 42,86% | 1,32 | 0,14R | €10,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 71 | 71 | 33,80% | 0,50 | -0,28R | €-201,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 33 | 33 | 30,30% | 0,96 | -0,02R | €-5,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,63 | -0,18R | €-28,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 11 | 94 | 94 | 40,43% | 1,11 | 0,05R | €48,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 88 | 88 | 35,23% | 0,68 | -0,17R | €-151,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 44 | 44 | 34,09% | 1,23 | 0,09R | €39,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 44,83% | 1,73 | 0,31R | €89,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,56 | -0,22R | €-32,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 10 | 83 | 83 | 40,96% | 1,21 | 0,10R | €79,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 77 | 77 | 36,36% | 0,59 | -0,21R | €-159,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,75 | -0,13R | €-19,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 43 | 43 | 34,88% | 1,33 | 0,12R | €51,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 37 | 37 | 29,73% | 0,58 | -0,24R | €-87,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 50 | 50 | 28,00% | 0,56 | -0,20R | €-102,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 44,83% | 1,82 | 0,35R | €100,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 0 | 128 | 128 | 35,16% | 0,73 | -0,14R | €-174,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 52 | 52 | 30,77% | 0,73 | -0,16R | €-83,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 112 | 112 | 33,93% | 0,71 | -0,15R | €-168,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 33 | 33 | 24,24% | 0,76 | -0,11R | €-37,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 55 | 55 | 25,45% | 0,60 | -0,22R | €-122,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 35 | 35 | 20,00% | 0,33 | -0,44R | €-154,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 148 | 148 | 33,11% | 0,66 | -0,18R | €-272,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 52 | 52 | 26,92% | 0,85 | -0,06R | €-33,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 72 | 72 | 23,61% | 0,63 | -0,18R | €-129,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 34 | 34 | 20,59% | 0,26 | -0,50R | €-169,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 0 | 138 | 138 | 31,88% | 0,57 | -0,23R | €-312,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 51 | 51 | 27,45% | 0,83 | -0,07R | €-35,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 67 | 67 | 22,39% | 0,45 | -0,28R | €-187,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,63 | -0,18R | €-28,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 11 | 95 | 95 | 41,05% | 1,16 | 0,07R | €68,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 88 | 88 | 37,50% | 0,80 | -0,10R | €-91,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 16 | 16 | 25,00% | 0,66 | -0,19R | €-30,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 44 | 44 | 34,09% | 1,23 | 0,09R | €39,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 44,83% | 1,73 | 0,31R | €89,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 1 | 68 | 68 | 36,76% | 0,55 | -0,25R | €-168,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 8 | 118 | 118 | 46,61% | 1,23 | 0,10R | €113,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 164 | 164 | 37,80% | 0,83 | -0,08R | €-124,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 31 | 31 | 35,48% | 0,58 | -0,24R | €-73,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 68 | 68 | 47,06% | 1,43 | 0,13R | €91,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 90 | 90 | 37,78% | 0,76 | -0,11R | €-95,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 82 | 82 | 40,24% | 0,82 | -0,08R | €-67,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 42,42% | 1,14 | 0,06R | €20,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,17 | -0,75R | €-119,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 50 | 50 | 40,00% | 0,55 | -0,26R | €-128,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 5 | 5 | 60,00% | 1,39 | 0,17R | €8,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 63 | 63 | 20,63% | 0,39 | -0,36R | €-224,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 11 | 105 | 105 | 40,00% | 1,18 | 0,08R | €85,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 144 | 144 | 32,64% | 0,64 | -0,19R | €-277,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 31 | 31 | 29,03% | 0,59 | -0,23R | €-70,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 62 | 62 | 33,87% | 1,28 | 0,11R | €68,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 71 | 71 | 22,54% | 0,58 | -0,21R | €-149,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 41,94% | 1,60 | 0,26R | €79,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 63 | 63 | 20,63% | 0,39 | -0,36R | €-224,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 11 | 107 | 107 | 40,19% | 1,20 | 0,09R | €94,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 145 | 145 | 32,41% | 0,63 | -0,20R | €-287,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 31 | 31 | 29,03% | 0,59 | -0,23R | €-70,95 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 62 | 62 | 33,87% | 1,28 | 0,11R | €68,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 78 | 78 | 28,21% | 0,62 | -0,20R | €-155,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 71 | 71 | 22,54% | 0,58 | -0,21R | €-149,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 40,62% | 1,59 | 0,25R | €79,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 61 | 61 | 21,31% | 0,33 | -0,41R | €-251,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 10 | 92 | 92 | 40,22% | 1,21 | 0,10R | €87,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 0 | 136 | 136 | 30,88% | 0,50 | -0,27R | €-363,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 27 | 27 | 25,93% | 0,63 | -0,21R | €-55,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 61 | 61 | 34,43% | 1,36 | 0,14R | €83,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 72 | 72 | 26,39% | 0,57 | -0,23R | €-163,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 66 | 66 | 21,21% | 0,38 | -0,32R | €-211,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 31 | 31 | 41,94% | 1,68 | 0,29R | €90,04 |
| MAIN | ALT_ROTATION_DOWN | 1 | 25 | 25 | 28,00% | 0,76 | -0,13R | €-32,69 |
| MAIN | ALT_ROTATION_UP | 5 | 51 | 51 | 23,53% | 0,46 | -0,36R | €-182,03 |
| MAIN | RANGE | 1 | 76 | 76 | 21,05% | 0,61 | -0,24R | €-185,76 |
| MAIN | RANGE_HIGH_VOL | 0 | 19 | 19 | 26,32% | 0,90 | -0,05R | €-9,26 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 2 | 37 | 37 | 27,03% | 0,70 | -0,19R | €-70,98 |
| MAIN | TREND_DOWN | 1 | 46 | 46 | 28,26% | 0,79 | -0,12R | €-57,38 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 1 | 38 | 38 | 31,58% | 1,05 | 0,03R | €11,82 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 11 | 11 | 45,45% | 1,54 | 0,26R | €28,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 13 | 13 | 30,77% | 0,16 | -0,61R | €-79,61 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 0,91 | -0,04R | €-6,71 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 1 | 64 | 64 | 23,44% | 0,49 | -0,35R | €-223,48 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 12 | 121 | 121 | 40,50% | 1,11 | 0,06R | €69,93 |
| Bilanciata 1H V1 | RANGE | 1 | 179 | 179 | 39,66% | 1,05 | 0,03R | €49,71 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 46 | 46 | 26,09% | 0,50 | -0,34R | €-156,31 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 1 | 96 | 96 | 37,50% | 1,19 | 0,10R | €92,29 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 87 | 87 | 29,89% | 0,70 | -0,16R | €-136,13 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 110 | 110 | 30,00% | 0,91 | -0,05R | €-50,84 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 1 | 35 | 35 | 40,00% | 1,22 | 0,11R | €40,11 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 6 | 74 | 61 | 44,59% | 1,58 | 0,26R | €191,02 |
| Bilanciata 1H V2 | RANGE | 1 | 129 | 117 | 34,88% | 0,83 | -0,10R | €-127,84 |
| Bilanciata 1H V2 | TRANSITION | 1 | 82 | 70 | 40,24% | 1,41 | 0,19R | €158,67 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 49 | 49 | 30,61% | 0,58 | -0,27R | €-132,34 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 8 | 64 | 64 | 40,62% | 1,45 | 0,23R | €145,50 |
| Bilanciata 1H V3 Filtered | RANGE | 1 | 123 | 123 | 40,65% | 1,07 | 0,03R | €41,05 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 18 | 18 | 27,78% | 0,56 | -0,28R | €-50,80 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 53 | 53 | 33,96% | 1,05 | 0,03R | €13,37 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €7,90 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 1 | 31 | 31 | 48,39% | 1,60 | 0,29R | €90,48 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 38 | 38 | 26,32% | 0,34 | -0,44R | €-165,71 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 8 | 62 | 62 | 41,94% | 1,56 | 0,27R | €166,50 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 101 | 101 | 38,61% | 0,86 | -0,07R | €-75,11 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 16 | 16 | 31,25% | 0,69 | -0,19R | €-29,97 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 45 | 45 | 33,33% | 1,04 | 0,02R | €7,69 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 42 | 42 | 23,81% | 0,74 | -0,13R | €-52,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 1 | 17 | 17 | 70,59% | 3,47 | 0,77R | €130,47 |
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
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 25,93% | 0,50 | -0,28R | €-76,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 64 | 64 | 45,31% | 1,11 | 0,05R | €33,16 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 0 | 155 | 155 | 35,48% | 0,78 | -0,11R | €-177,52 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 59 | 59 | 38,98% | 1,12 | 0,05R | €27,90 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 75 | 75 | 28,00% | 0,76 | -0,11R | €-80,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 45 | 45 | 24,44% | 0,46 | -0,35R | €-158,71 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 0 | 185 | 185 | 39,46% | 0,96 | -0,02R | €-32,33 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 61 | 61 | 40,98% | 1,26 | 0,09R | €57,59 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,60 | -0,24R | €-189,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 91 | 91 | 27,47% | 0,67 | -0,17R | €-153,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 90 | 90 | 25,56% | 0,48 | -0,33R | €-299,93 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 11 | 127 | 127 | 41,73% | 0,97 | -0,02R | €-22,01 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 0 | 213 | 213 | 37,09% | 0,83 | -0,09R | €-188,26 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 39 | 39 | 38,46% | 0,86 | -0,07R | €-29,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 85 | 85 | 41,18% | 1,33 | 0,12R | €105,09 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 101 | 101 | 28,71% | 0,59 | -0,23R | €-229,86 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 105 | 105 | 27,62% | 0,69 | -0,16R | €-170,93 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 1 | 40 | 40 | 50,00% | 1,64 | 0,25R | €99,67 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 52 | 52 | 26,92% | 0,46 | -0,37R | €-191,88 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 6 | 80 | 80 | 42,50% | 1,07 | 0,03R | €25,79 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 0 | 119 | 119 | 42,02% | 1,06 | 0,03R | €37,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 41,18% | 0,87 | -0,07R | €-11,36 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 53 | 53 | 39,62% | 1,25 | 0,09R | €49,85 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 60 | 60 | 26,67% | 0,58 | -0,23R | €-137,91 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 44,44% | 1,15 | 0,06R | €11,25 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 90 | 90 | 24,44% | 0,48 | -0,32R | €-287,54 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 12 | 129 | 129 | 42,64% | 1,13 | 0,06R | €79,48 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 0 | 195 | 195 | 34,87% | 0,80 | -0,11R | €-206,82 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 38 | 38 | 28,95% | 0,64 | -0,20R | €-77,77 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,43 | 0,16R | €127,75 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 94 | 94 | 27,66% | 0,59 | -0,24R | €-222,83 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 96 | 96 | 20,83% | 0,52 | -0,26R | €-247,93 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 39,02% | 1,37 | 0,16R | €65,70 |
| Rapida 1H V2 | ALT_ROTATION_UP | 1 | 12 | 11 | 25,00% | 0,31 | -0,57R | €-68,70 |
| Rapida 1H V2 | RANGE | 0 | 44 | 36 | 40,91% | 0,84 | -0,08R | €-36,12 |
| Rapida 1H V2 | TRANSITION | 0 | 7 | 7 | 57,14% | 0,81 | -0,07R | €-4,61 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 89 | 89 | 23,60% | 0,44 | -0,36R | €-321,05 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 10 | 118 | 118 | 44,07% | 1,18 | 0,08R | €95,44 |
| Rapida 1H V3 Filtered | RANGE | 0 | 188 | 188 | 37,23% | 0,82 | -0,09R | €-176,31 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 33 | 33 | 39,39% | 0,87 | -0,07R | €-22,89 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 76 | 76 | 38,16% | 1,12 | 0,05R | €39,59 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 109 | 109 | 36,70% | 0,98 | -0,01R | €-9,47 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 52 | 52 | 36,54% | 0,85 | -0,08R | €-44,06 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 66 | 66 | 25,76% | 0,46 | -0,37R | €-242,19 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 7 | 98 | 98 | 44,90% | 1,21 | 0,09R | €87,93 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 0 | 149 | 149 | 38,26% | 0,88 | -0,06R | €-88,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 22 | 22 | 40,91% | 0,94 | -0,03R | €-6,30 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 58 | 58 | 37,93% | 1,03 | 0,01R | €8,02 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 65 | 65 | 27,69% | 0,61 | -0,22R | €-143,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 70 | 70 | 28,57% | 0,65 | -0,18R | €-127,20 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 51,72% | 1,70 | 0,25R | €71,27 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,29 | -0,54R | €-81,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 83 | 83 | 43,37% | 0,86 | -0,08R | €-68,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 34 | 34 | 55,88% | 1,39 | 0,15R | €49,48 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,31 | -0,52R | €-72,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 86 | 86 | 40,70% | 0,94 | -0,03R | €-25,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 34 | 34 | 38,24% | 1,19 | 0,07R | €24,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 25 | 25 | 16,00% | 0,26 | -0,50R | €-123,89 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 10 | 107 | 107 | 42,99% | 1,10 | 0,05R | €48,76 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 108 | 108 | 41,67% | 0,97 | -0,01R | €-15,59 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,82 | -0,10R | €-16,55 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 49 | 49 | 40,82% | 1,24 | 0,09R | €45,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 46,67% | 1,29 | 0,13R | €38,52 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 57 | 57 | 22,81% | 0,41 | -0,40R | €-230,68 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 0 | 190 | 190 | 38,42% | 0,87 | -0,07R | €-128,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 60 | 60 | 33,33% | 0,96 | -0,02R | €-9,37 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 95 | 95 | 31,58% | 0,77 | -0,12R | €-114,65 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 88 | 88 | 23,86% | 0,44 | -0,35R | €-309,63 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 10 | 117 | 117 | 42,74% | 1,10 | 0,05R | €54,32 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 0 | 186 | 186 | 37,10% | 0,80 | -0,10R | €-191,04 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 32 | 32 | 40,62% | 0,92 | -0,04R | €-12,76 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 71 | 71 | 38,03% | 1,15 | 0,06R | €42,36 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 89 | 89 | 28,09% | 0,60 | -0,21R | €-190,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 92 | 92 | 30,43% | 0,73 | -0,14R | €-132,21 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 32 | 32 | 43,75% | 1,20 | 0,09R | €28,25 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 22 | 22 | 31,82% | 1,67 | 0,32R | €69,57 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 9 | 40 | 40 | 30,00% | 0,78 | -0,15R | €-61,90 |
| SHADOW_4H_WIDE | RANGE | 3 | 72 | 72 | 15,28% | 0,62 | -0,26R | €-187,33 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,91 | -0,05R | €-8,55 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 38 | 38 | 15,79% | 0,47 | -0,38R | €-145,68 |
| SHADOW_4H_WIDE | TREND_DOWN | 2 | 45 | 45 | 26,67% | 0,96 | -0,03R | €-11,28 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 39 | 39 | 23,08% | 0,99 | -0,01R | €-2,00 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 2 | 16 | 16 | 12,50% | 0,45 | -0,43R | €-68,57 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 4 | 54 | 54 | 42,59% | 0,95 | -0,02R | €-11,45 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 69 | 69 | 44,93% | 0,98 | -0,01R | €-6,11 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 60,00% | 2,25 | 0,41R | €41,08 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 13 | 13 | 53,85% | 1,74 | 0,31R | €39,93 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,80 | -0,10R | €-17,83 |
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
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 1 | 55 | 55 | 27,27% | 0,66 | -0,20R | €-112,38 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 10 | 95 | 95 | 42,11% | 1,13 | 0,07R | €65,78 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 149 | 149 | 42,28% | 1,00 | -0,00R | €-2,37 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 32 | 32 | 37,50% | 0,88 | -0,06R | €-19,15 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 74 | 74 | 40,54% | 1,42 | 0,19R | €140,09 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 1 | 74 | 74 | 35,14% | 0,90 | -0,05R | €-37,15 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 95 | 95 | 35,79% | 1,09 | 0,04R | €37,83 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 33 | 33 | 36,36% | 0,97 | -0,02R | €-6,52 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,77 | -0,12R | €-23,58 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 10 | 87 | 87 | 41,38% | 1,07 | 0,04R | €33,06 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 75 | 75 | 49,33% | 1,31 | 0,14R | €108,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,61 | -0,23R | €-29,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 40 | 40 | 45,00% | 2,07 | 0,33R | €133,62 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 44 | 44 | 36,36% | 1,13 | 0,06R | €26,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 41,67% | 1,14 | 0,07R | €17,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 69 | 69 | 34,78% | 0,72 | -0,14R | €-96,86 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 8 | 107 | 107 | 42,99% | 1,15 | 0,07R | €73,10 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 148 | 148 | 41,89% | 1,16 | 0,07R | €105,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 38 | 38 | 42,11% | 0,80 | -0,09R | €-32,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 64 | 64 | 45,31% | 1,24 | 0,10R | €64,04 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 1 | 97 | 97 | 37,11% | 0,88 | -0,05R | €-46,09 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 97 | 97 | 49,48% | 1,29 | 0,12R | €117,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 35,90% | 0,78 | -0,12R | €-48,33 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 1 | 55 | 55 | 27,27% | 0,68 | -0,20R | €-107,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 10 | 93 | 93 | 43,01% | 1,11 | 0,06R | €53,63 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 137 | 137 | 45,26% | 1,05 | 0,02R | €33,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 30 | 30 | 43,33% | 1,03 | 0,01R | €3,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 57 | 57 | 43,86% | 1,30 | 0,13R | €75,71 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 1 | 74 | 74 | 39,19% | 0,91 | -0,05R | €-33,66 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 74 | 74 | 36,49% | 0,71 | -0,13R | €-98,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 28 | 28 | 42,86% | 1,01 | 0,01R | €1,52 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 35 | 35 | 37,14% | 0,96 | -0,02R | €-7,14 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 66,67% | 3,50 | 0,66R | €79,43 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 35 | 35 | 37,14% | 0,95 | -0,03R | €-9,78 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 58,33% | 4,29 | 0,87R | €104,99 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 13,33% | 0,06 | -0,53R | €-79,99 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 4 | 32 | 32 | 43,75% | 1,26 | 0,12R | €37,45 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 42 | 42 | 38,10% | 1,02 | 0,01R | €4,16 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 28 | 28 | 35,71% | 1,05 | 0,02R | €6,92 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 60,00% | 5,47 | 0,96R | €95,90 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 85 | 85 | 38,82% | 1,04 | 0,02R | €16,49 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 100 | 100 | 34,00% | 0,78 | -0,10R | €-104,07 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 44,44% | 1,30 | 0,16R | €57,70 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 1 | 5 | 5 | 60,00% | 2,02 | 0,45R | €22,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 32 | 32 | 50,00% | 1,38 | 0,18R | €57,26 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,45 | -0,37R | €-18,67 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 1 | 5 | 5 | 80,00% | 4,65 | 0,83R | €41,31 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,69 | -0,22R | €-6,71 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 21 | 21 | 14,29% | 0,20 | -0,52R | €-109,48 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 6 | 78 | 78 | 41,03% | 1,20 | 0,11R | €83,94 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 84 | 84 | 46,43% | 1,45 | 0,21R | €179,30 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 56 | 56 | 42,86% | 1,74 | 0,33R | €186,16 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,73 | -0,15R | €-65,99 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 38,10% | 1,40 | 0,21R | €43,25 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 1 | 42 | 42 | 28,57% | 0,65 | -0,22R | €-90,45 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 10 | 86 | 86 | 37,21% | 0,99 | -0,01R | €-5,85 |
| SHADOW_COMBO_TREND | RANGE | 0 | 128 | 128 | 35,16% | 1,04 | 0,02R | €24,85 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 23 | 23 | 34,78% | 1,15 | 0,07R | €15,88 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 61 | 61 | 36,07% | 1,32 | 0,17R | €103,93 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 65 | 65 | 30,77% | 0,70 | -0,17R | €-107,46 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 73 | 73 | 28,77% | 1,00 | -0,00R | €-0,70 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 28 | 28 | 35,71% | 0,90 | -0,06R | €-17,56 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,43R | €14,26 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 66,67% | 1,54 | 0,20R | €12,21 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,70 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,61 | -0,25R | €-17,63 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -0,75R | €-45,24 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,62 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,97 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 29 | 29 | 24,14% | 0,60 | -0,30R | €-85,94 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 8 | 38 | 38 | 23,68% | 0,50 | -0,39R | €-146,92 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 65 | 65 | 32,31% | 1,02 | 0,01R | €8,90 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 13 | 13 | 46,15% | 1,65 | 0,31R | €40,69 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 25 | 25 | 40,00% | 1,57 | 0,29R | €71,79 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 21 | 21 | 23,81% | 0,27 | -0,54R | €-113,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 57,14% | 2,04 | 0,48R | €100,52 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 21,05% | 0,37 | -0,50R | €-94,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 8 | 30 | 30 | 26,67% | 0,56 | -0,32R | €-96,50 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 0 | 45 | 45 | 33,33% | 0,98 | -0,01R | €-6,16 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 54,55% | 2,45 | 0,55R | €60,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 18 | 18 | 50,00% | 2,40 | 0,56R | €101,05 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 19 | 19 | 26,32% | 0,29 | -0,55R | €-103,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 66,67% | 2,82 | 0,64R | €95,74 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 1 | 45 | 45 | 26,67% | 0,55 | -0,28R | €-128,10 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 11 | 82 | 82 | 37,80% | 1,08 | 0,04R | €35,75 |
| SHADOW_EMA_TREND_1H | RANGE | 0 | 125 | 125 | 35,20% | 1,08 | 0,04R | €49,33 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 26 | 26 | 42,31% | 1,60 | 0,25R | €64,24 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 60 | 60 | 35,00% | 1,17 | 0,10R | €57,24 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 67 | 67 | 31,34% | 0,68 | -0,17R | €-114,96 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 76 | 76 | 27,63% | 0,92 | -0,04R | €-31,30 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 28 | 28 | 39,29% | 1,10 | 0,06R | €16,17 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 6 | 6 | 33,33% | 0,52 | -0,35R | €-21,16 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,74 | -0,17R | €-8,58 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,50R | €5,03 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,30 | 0,16R | €6,43 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,23 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 4 | 4 | 25,00% | 0,58 | -0,35R | €-13,87 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,56 | -0,33R | €-19,66 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,66 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 6 | 6 | 33,33% | 0,50 | -0,36R | €-21,85 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,23 | -0,57R | €-34,18 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,04 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 34 | 34 | 44,12% | 1,77 | 0,38R | €127,78 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 1,15 | 0,09R | €44,82 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 60 | 60 | 30,00% | 0,87 | -0,08R | €-50,78 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 25 | 25 | 52,00% | 1,10 | 0,04R | €11,03 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 149 | 149 | 66,44% | 1,46 | 0,14R | €213,68 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 72 | 72 | 75,00% | 1,91 | 0,22R | €160,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 77 | 77 | 63,64% | 1,35 | 0,12R | €90,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 23,53% | 0,69 | -0,21R | €-35,48 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 0 | 82 | 82 | 34,15% | 1,14 | 0,08R | €66,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 33 | 33 | 36,36% | 1,26 | 0,15R | €47,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 44 | 44 | 38,64% | 1,30 | 0,18R | €77,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 30,77% | 1,10 | 0,07R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 0 | 74 | 74 | 31,08% | 1,15 | 0,09R | €65,91 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 30 | 30 | 40,00% | 1,55 | 0,28R | €85,28 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 41 | 41 | 39,02% | 1,33 | 0,19R | €79,11 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,20 | -0,67R | €-73,38 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 59 | 59 | 35,59% | 1,11 | 0,07R | €41,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 26 | 26 | 46,15% | 2,24 | 0,50R | €130,45 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 17 | 17 | 23,53% | 0,63 | -0,27R | €-45,34 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 0 | 77 | 77 | 33,77% | 1,14 | 0,08R | €61,59 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 33 | 33 | 39,39% | 1,44 | 0,24R | €77,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 42 | 42 | 38,10% | 1,27 | 0,16R | €67,95 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 2 | 54 | 54 | 20,37% | 0,38 | -0,42R | €-227,12 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 7 | 103 | 103 | 37,86% | 1,08 | 0,05R | €48,25 |
| Forza relativa 1H V1 | RANGE | 1 | 169 | 169 | 30,18% | 0,81 | -0,10R | €-171,44 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 28 | 28 | 28,57% | 0,53 | -0,25R | €-70,96 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 2 | 71 | 71 | 38,03% | 1,46 | 0,23R | €161,78 |
| Forza relativa 1H V1 | TREND_DOWN | 3 | 72 | 72 | 29,17% | 0,87 | -0,07R | €-50,78 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 96 | 96 | 25,00% | 0,89 | -0,06R | €-55,92 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 28 | 28 | 28,57% | 0,91 | -0,06R | €-15,62 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 25 | 25 | 32,00% | 0,73 | -0,14R | €-36,12 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 3 | 36 | 32 | 47,22% | 1,82 | 0,35R | €127,61 |
| Forza relativa 1H V2 | RANGE | 1 | 74 | 71 | 33,78% | 0,88 | -0,07R | €-50,90 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 1 | 41 | 36 | 41,46% | 1,81 | 0,37R | €150,95 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 34 | 33 | 29,41% | 0,95 | -0,02R | €-7,23 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 7 | 6 | 14,29% | 0,42 | -0,43R | €-30,05 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 1 | 32 | 32 | 12,50% | 0,14 | -0,67R | €-213,59 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 60 | 60 | 23,33% | 0,33 | -0,39R | €-236,12 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 1 | 32 | 32 | 12,50% | 0,14 | -0,67R | €-213,59 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 60 | 60 | 23,33% | 0,33 | -0,39R | €-236,12 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 1 | 32 | 32 | 12,50% | 0,14 | -0,67R | €-213,59 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 1,38 | 0,17R | €24,20 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 60 | 60 | 23,33% | 0,33 | -0,39R | €-236,12 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 17 | 17 | 41,18% | 1,23 | 0,10R | €16,55 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 21 | 21 | 42,86% | 1,13 | 0,07R | €14,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 28 | 28 | 21,43% | 0,54 | -0,32R | €-88,93 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 15 | 15 | 46,67% | 1,70 | 0,29R | €44,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 73 | 73 | 28,77% | 0,61 | -0,21R | €-156,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 18 | 18 | 44,44% | 1,33 | 0,13R | €23,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 37 | 37 | 37,84% | 0,98 | -0,01R | €-3,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 31 | 31 | 38,71% | 0,36 | -0,37R | €-116,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 45,45% | 1,12 | 0,06R | €6,29 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 65 | 65 | 53,85% | 0,64 | -0,16R | €-104,63 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 22 | 22 | 63,64% | 1,42 | 0,16R | €34,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 28 | 28 | 60,71% | 1,52 | 0,22R | €60,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 66 | 66 | 53,03% | 0,63 | -0,16R | €-106,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 37,04% | 0,25 | -0,45R | €-120,55 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,55 | 0,22R | €28,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 58 | 58 | 53,45% | 0,38 | -0,27R | €-159,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 20 | 20 | 60,00% | 1,23 | 0,10R | €19,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 27 | 27 | 62,96% | 1,58 | 0,23R | €61,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 56 | 56 | 51,79% | 0,62 | -0,17R | €-93,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 15 | 15 | 33,33% | 1,10 | 0,05R | €7,38 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 10 | 87 | 87 | 39,08% | 1,02 | 0,01R | €10,47 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 1 | 43 | 43 | 39,53% | 1,62 | 0,22R | €96,51 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 1,91 | 0,36R | €69,22 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 15 | 15 | 33,33% | 1,10 | 0,05R | €7,38 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 11 | 88 | 88 | 38,64% | 1,00 | -0,00R | €-0,61 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 1 | 43 | 43 | 39,53% | 1,62 | 0,22R | €96,51 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 1,91 | 0,36R | €69,22 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 15 | 15 | 33,33% | 1,10 | 0,05R | €7,38 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 11 | 88 | 88 | 38,64% | 1,00 | -0,00R | €-0,61 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 67 | 67 | 50,75% | 1,46 | 0,19R | €129,59 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 15 | 15 | 26,67% | 0,62 | -0,25R | €-37,70 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 1 | 43 | 43 | 39,53% | 1,62 | 0,22R | €96,51 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 52,63% | 1,91 | 0,36R | €69,22 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 19 | 19 | 15,79% | 0,24 | -0,46R | €-87,36 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 6 | 78 | 78 | 41,03% | 1,20 | 0,11R | €84,53 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 79 | 79 | 46,84% | 1,60 | 0,27R | €212,29 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,48 | -0,30R | €-39,55 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 52 | 52 | 42,31% | 1,80 | 0,35R | €183,73 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 62 | 62 | 29,03% | 0,95 | -0,02R | €-14,90 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 38,10% | 1,40 | 0,21R | €43,25 |
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
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 40 | 40 | 45,00% | 2,24 | 0,45R | €179,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 43 | 43 | 27,91% | 0,73 | -0,15R | €-66,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,13 | -0,45R | €-71,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 41 | 41 | 48,78% | 1,40 | 0,15R | €62,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,02 | -0,72R | €-101,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 37 | 37 | 40,54% | 1,85 | 0,33R | €123,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 31,82% | 0,56 | -0,21R | €-45,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 5 | 67 | 67 | 47,76% | 1,37 | 0,16R | €106,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 88 | 88 | 46,59% | 1,56 | 0,21R | €181,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 35,29% | 0,73 | -0,11R | €-17,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 43 | 43 | 46,51% | 1,32 | 0,12R | €52,52 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 58,82% | 1,92 | 0,28R | €48,37 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,26 | -0,45R | €-76,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 5 | 58 | 58 | 44,83% | 1,48 | 0,23R | €135,25 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 77 | 77 | 48,05% | 1,55 | 0,25R | €189,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 38,46% | 0,62 | -0,19R | €-24,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 38 | 38 | 39,47% | 1,73 | 0,30R | €113,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 41,67% | 1,67 | 0,29R | €35,15 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 33,33% | 0,52 | -0,23R | €-54,57 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 5 | 84 | 84 | 45,24% | 1,12 | 0,05R | €44,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 81 | 81 | 46,91% | 1,52 | 0,20R | €162,96 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 17 | 17 | 29,41% | 0,61 | -0,16R | €-26,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 48 | 48 | 47,92% | 1,35 | 0,14R | €66,14 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 57 | 57 | 43,86% | 0,92 | -0,03R | €-19,05 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 26 | 26 | 46,15% | 1,20 | 0,09R | €23,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 25,00% | 0,43 | -0,30R | €-35,93 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 6 | 79 | 79 | 39,24% | 1,17 | 0,09R | €73,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 0 | 70 | 70 | 44,29% | 1,49 | 0,23R | €162,79 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 33,33% | 0,55 | -0,24R | €-29,35 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 40 | 40 | 42,50% | 1,98 | 0,38R | €152,06 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 28,57% | 0,77 | -0,13R | €-54,77 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 1,00 | -0,00R | €-0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,09 | -0,51R | €-56,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 6 | 77 | 77 | 38,96% | 1,23 | 0,12R | €94,12 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 65 | 65 | 43,08% | 1,53 | 0,26R | €169,81 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 13 | 13 | 30,77% | 0,41 | -0,35R | €-44,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 34 | 34 | 41,18% | 2,47 | 0,50R | €169,20 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 39 | 39 | 28,21% | 0,79 | -0,11R | €-43,14 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 33,33% | 0,81 | -0,11R | €-16,62 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,59 | -0,25R | €-55,53 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 7 | 79 | 79 | 37,97% | 1,00 | 0,00R | €1,85 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 81 | 81 | 49,38% | 1,55 | 0,24R | €194,78 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,51 | -0,34R | €-58,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 56 | 56 | 41,07% | 1,62 | 0,25R | €142,55 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 45 | 45 | 28,89% | 0,95 | -0,03R | €-12,97 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 78 | 78 | 34,62% | 1,08 | 0,04R | €29,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 48,00% | 1,83 | 0,36R | €90,13 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,29 | -0,58R | €-23,37 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,75 | -0,18R | €-14,00 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,43R | €24,29 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,70R | €16,99 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 0,74 | -0,15R | €-5,96 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 6 | 6 | 33,33% | 0,60 | -0,30R | €-18,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,51 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,10 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 66,67% | 2,69 | 0,63R | €38,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 2,72R | €27,23 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,46 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,43 | -0,41R | €-12,26 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 8 | 8 | 37,50% | 1,02 | 0,01R | €1,11 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 1,15 | 0,11R | €3,17 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,46 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-21T11:06:33+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **1085**
- Scenari virtuali ancora attivi: **17560**
- Gruppi in attesa dell'uscita originale: **276**
- Gruppi con originale chiuso ma Shadow ancora attive: **809**
- Confronti completati: **304418**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 7035 | 7108 | +€8,29 | 50,9% | 2224 | 15 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 7035 | 7108 | +€7,66 | 50,7% | 2179 | 68 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 7035 | 7108 | +€4,20 | 48,0% | 2440 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 7029 | 7102 | +€5,28 | 42,5% | 2079 | 106 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 7027 | 7100 | +€8,61 | 45,7% | 1833 | 121 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 7027 | 7100 | +€8,08 | 46,6% | 1692 | 202 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 7023 | 7096 | +€5,66 | 35,6% | 1348 | 568 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 7014 | 7087 | +€5,49 | 43,0% | 979 | 1010 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 7008 | 7081 | +€6,27 | 49,6% | 2153 | 151 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 6983 | 7056 | +€2,18 | 48,7% | 1695 | 795 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 6981 | 7054 | +€6,29 | 40,3% | 659 | 894 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 6924 | 6997 | +€4,48 | 46,4% | 1070 | 1137 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 6922 | 6995 | +€5,66 | 40,6% | 767 | 1325 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 6921 | 6994 | +€6,60 | 46,1% | 1500 | 346 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 6920 | 6993 | +€5,07 | 49,5% | 2026 | 232 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 6809 | 6882 | +€4,60 | 44,4% | 1300 | 613 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 6782 | 6855 | +€4,39 | 39,8% | 597 | 1617 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 6762 | 6835 | +€2,11 | 37,3% | 604 | 1558 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 6622 | 6695 | €-2,50 | 37,4% | 1295 | 1202 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 6425 | 6498 | €-6,32 | 30,3% | 565 | 1799 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-21T11:06:47+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **304418**
- Valutazioni prodotte: **19801**
- Candidature al Blocco 5: **23**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 468 | 0,353 | 0,191 | 0,249 | 58,5% | 87,5 | VALIDATING |
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

Generato: 2026-08-21T11:09:56+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 81 | 100,00% | 1,11 | +€95,26 | +€1,18 | 2,32% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 81 | 100,00% | 1,09 | +€75,72 | +€0,93 | 2,59% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 63 | 100,00% | 1,80 | +€879,36 | +€13,96 | 2,95% | PROMOTION_REVIEW_READY |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 36 | 92,31% | 0,00 | €-352,37 | €-9,79 | 3,52% | EARLY_NOT_CONFIRMED |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 102 | 99,03% | 1,52 | +€724,43 | +€7,10 | 2,13% | PROMOTION_REVIEW_READY |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-21T11:06:19+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **49**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **712.86 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 227 | 0 | 19169.04 |
| DOWN_20 | 227 | 0 | 38338.08 |
| DOWN_30 | 227 | 0 | 57507.12 |
| DOWN_40 | 227 | 80 | 72079.90 |
| UP_10 | 41 | 0 | 2468.82 |
| UP_20 | 41 | 0 | 4937.64 |
| UP_30 | 41 | 0 | 7406.46 |
| UP_40 | 41 | 14 | 9400.35 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-21T11:05:15+00:00

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

Generato: 2026-08-21T11:10:01+00:00

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

Generato: 2026-08-21T11:10:01+00:00

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

Generato: 2026-08-21T11:10:01+00:00

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

Generato: 2026-08-21T11:10:01+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 24.8 | E | 158 | 1.41 | 0.182 | 8.23 |
| 2 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 24.8 | E | 77 | 1.99 | 0.434 | 7.65 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 23.0 | E | 102 | 1.64 | 0.267 | 8.50 |
| 4 | SHADOW_DONCHIAN_1H | BASELINE | 19.5 | E | 80 | 1.53 | 0.284 | 8.55 |
| 5 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | BASELINE | 19.1 | E | 48 | 1.77 | 0.387 | 8.16 |
| 6 | SHADOW_COMBO_ADAPTIVE | BASELINE | 18.8 | E | 114 | 1.44 | 0.194 | 14.19 |
| 7 | SHADOW_1H_FAST_V3 | BASELINE | 17.8 | E | 183 | 1.06 | 0.027 | 29.51 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 17.7 | E | 139 | 1.07 | 0.032 | 30.06 |
| 9 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 17.2 | E | 155 | 0.99 | -0.003 | 30.93 |
| 10 | MAIN_SIDE_REGIME_GUARD_V1 | BASELINE | 17.2 | E | 30 | 1.65 | 0.336 | 4.71 |

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

Generato: 2026-08-21T11:10:01+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **UNKNOWN**
- Righe di performance: **674**
- Strategie preferite nel regime corrente: **7**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **319**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | MAIN | main | INSUFFICIENT | 82.0 | 5 | 99.00 | 0.990 | 0.00 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | COMPATIBLE | 82.0 | 37 | 1.97 | 0.343 | 3.32 |
| 3 | EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | momentum_breakout_v3_filtered | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.775 | 0.00 |
| 4 | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | shadow-1h-fast-v3-long-nohigh-cap75-lock-v1 | INSUFFICIENT | 80.5 | 5 | 3.14 | 0.433 | 1.01 |
| 5 | SHADOW_MASTER_ADAPTIVE_GB20_V1 | shadow-master-adaptive-gb20-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.550 | 0.00 |
| 6 | SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | shadow-master-adaptive-gb20-be-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.986 | 0.00 |
| 7 | SHADOW_ETH_ADAPTIVE_1H | shadow-eth-adaptive-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.930 | 0.00 |
| 8 | SHADOW_ETH_DONCHIAN_1H | shadow-eth-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.921 | 0.00 |
| 9 | SHADOW_ETH_EMA_1H | shadow-eth-ema-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.938 | 0.00 |
| 10 | SHADOW_DONCHIAN_1H | shadow-donchian-1h | OBSERVING | 79.7 | 18 | 3.80 | 0.702 | 2.81 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-21T11:10:01+00:00

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

Generato: 2026-08-21T11:06:19+00:00

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
