# Paper trading automatico KuCoin

Generato: 2026-08-18T06:08:50+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-18T06:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-18T06:05:28+00:00 | 2026-08-18T06:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-18T05:45:00+00:00 | 2026-08-18T05:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-18T05:00:00+00:00 | 2026-08-18T05:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-18T00:00:00+00:00 | 2026-08-18T00:00:00+00:00 | 2,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SNDK | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,98 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | GPS | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,39 | 6,00 | 0,00 | STALE_CANDLE | 2,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,63 | 6,00 | 0,37 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,61 | 6,00 | 1,39 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,25 | 6,00 | 4,75 | STALE_CANDLE | 2,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 1,15 | 6,00 | 4,85 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -0,24 | 6,00 | 5,76 | STALE_CANDLE | 2,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,07 | 6,00 | 5,93 | STALE_CANDLE | 2,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 125.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V3 Filtered | BEAT | 60m | SHORT | -7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — score 6–7,5 | BEAT | 60m | SHORT | -7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida score 6–7,5 — senza Trend Up | BEAT | 60m | SHORT | -7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V3 — score <7,5 | BEAT | 60m | SHORT | -7,00 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | BEAT | 60m | SHORT | -7,00 | 4,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata V3 · LONG only | BEAT | 60m | SHORT | -7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | BEAT | 60m | SHORT | -7,00 | 5,50 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BEAT | 60m | SHORT | -7,00 | 5,00 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.656,20 | -3,44% | €-92,15 | €3.000,00 | -3,07% | 5 | 42 | 33,33% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 42 | 1559 | PRIME INDICAZIONI | 50 (mancano 8) |

- Trade del Principale 4H chiusi: **42**; win rate **33,33%**; profit factor **0,72**.
- Expectancy: **€-9,04** per trade; P&L netto: **€-379,65**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.656,20 | €1.270,03 | €3.810,09 | €192,07 | €34,69 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.629,63 | €4.573,29 | €9.146,58 | €104,61 | €-23,58 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.611,75 | €1.769,88 | €5.309,64 | €106,16 | €9,96 |
| TEST | MAIN — Side × Regime Guard | 6 | €10.392,34 | €1.442,14 | €4.326,41 | €208,48 | €-10,63 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.388,86 | €3.442,13 | €10.326,38 | €207,57 | €23,77 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.379,37 | €4.465,62 | €8.931,24 | €102,14 | €-23,03 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.348,78 | €386,22 | €1.158,67 | €51,78 | €0,00 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.332,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 1 | €10.266,86 | €189,64 | €568,93 | €49,82 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 2 | €10.214,82 | €196,80 | €590,40 | €2,05 | €30,44 |
| TEST | Rapida V3 NoHigh — Regime Guard | 1 | €10.199,20 | €1.508,82 | €4.526,45 | €50,70 | €-22,08 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 4 | €10.157,91 | €3.391,14 | €6.782,27 | €152,57 | €27,53 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.139,86 | €2.162,07 | €4.324,14 | €148,75 | €29,51 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 2 | €10.124,16 | €2.326,70 | €6.980,10 | €100,51 | €19,24 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €10.112,64 | €3.350,61 | €10.051,82 | €202,05 | €23,14 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €10.039,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 5 | €10.035,87 | €3.355,77 | €10.067,30 | €200,64 | €23,10 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 1 | €10.011,37 | €184,93 | €554,78 | €48,58 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.004,97 | €1.155,63 | €3.466,88 | €49,92 | €18,58 |
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
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €9.979,54 | €1.662,17 | €3.324,34 | €199,40 | €25,45 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.973,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.931,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.930,36 | €1.413,45 | €2.826,90 | €49,75 | €-21,47 |
| TEST | Sol Adaptive 4H | 0 | €9.928,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.902,43 | €3.389,27 | €10.167,82 | €198,48 | €-29,42 |
| TEST | Combo Adaptive — Side × Regime Guard | 4 | €9.897,76 | €4.838,90 | €9.677,80 | €99,33 | €8,98 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.875,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.872,36 | €1.406,00 | €2.812,00 | €49,49 | €-27,40 |
| TEST | Btc Ema 1H | 0 | €9.848,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.838,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 3 | €9.824,97 | €1.660,65 | €3.321,30 | €101,25 | €-9,61 |
| TEST | Scanner Bottom10 Short | 3 | €9.818,94 | €1.923,37 | €3.846,75 | €98,53 | €17,54 |
| TEST | Scanner Bottom15 Short | 3 | €9.818,94 | €1.923,37 | €3.846,75 | €98,53 | €17,54 |
| TEST | Scanner Bottom20 Short | 3 | €9.818,94 | €1.923,37 | €3.846,75 | €98,53 | €17,54 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €9.811,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.805,38 | €1.690,92 | €3.381,84 | €49,43 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.792,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.762,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.760,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.750,43 | €1.892,84 | €3.785,69 | €97,35 | €17,64 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.735,60 | €1.889,96 | €3.779,93 | €97,20 | €17,62 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 3 | €9.720,12 | €436,17 | €872,34 | €50,02 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.720,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 4 | €9.707,04 | €369,55 | €1.108,64 | €43,76 | €28,93 |
| TEST | Global Confluence puro 1H | 1 | €9.695,12 | €1.512,09 | €3.024,18 | €48,39 | €16,21 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 2 | €9.682,78 | €279,72 | €839,17 | €3,88 | €26,71 |
| TEST | Rapida V3 — no volatilità HIGH | 1 | €9.668,04 | €215,12 | €645,36 | €48,02 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.660,68 | €1.875,42 | €3.750,84 | €96,45 | €17,48 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €9.643,60 | €367,13 | €1.101,40 | €43,47 | €28,74 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 1 | €9.630,78 | €196,64 | €589,91 | €45,15 | €0,00 |
| TEST | Forza relativa 1H V2 | 2 | €9.622,28 | €1.930,62 | €3.861,24 | €96,38 | €16,85 |
| TEST | Sol Adaptive 1H | 0 | €9.621,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 3 | €9.597,86 | €430,68 | €861,36 | €49,39 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €9.587,77 | €1.189,62 | €3.568,85 | €97,21 | €-23,07 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 1 | €9.572,84 | €174,37 | €523,12 | €0,00 | €28,36 |
| TEST | Combo Adaptive — Long Only | 4 | €9.566,72 | €3.405,47 | €6.810,95 | €146,43 | €17,82 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.564,42 | €202,90 | €405,81 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.522,40 | €1.105,17 | €3.315,52 | €47,74 | €-24,23 |
| TEST | Combo Adaptive — Quality7 | 0 | €9.515,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 4 | €9.502,54 | €2.591,80 | €7.775,40 | €141,13 | €8,92 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.501,03 | €2.959,04 | €5.918,08 | €94,61 | €33,47 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 3 | €9.490,93 | €2.955,89 | €5.911,79 | €94,51 | €33,43 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.476,46 | €1.938,06 | €3.876,12 | €139,84 | €29,42 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.470,20 | €4.571,18 | €9.142,35 | €141,05 | €35,47 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €9.457,25 | €1.687,33 | €3.374,66 | €97,16 | €21,61 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.454,25 | €2.726,64 | €5.453,28 | €94,96 | €1,08 |
| TEST | Master Adaptive V1 | 3 | €9.454,22 | €2.944,46 | €5.888,92 | €94,15 | €33,30 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.434,38 | €1.594,63 | €3.189,26 | €97,22 | €-9,23 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €9.428,27 | €201,44 | €604,33 | €2,94 | €28,08 |
| TEST | Bilanciata 1H V1 | 5 | €9.417,07 | €1.443,61 | €4.330,82 | €96,37 | €30,17 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.401,29 | €3.311,30 | €6.622,61 | €133,15 | €40,79 |
| TEST | Bilanciata V3 · LONG only | 6 | €9.366,12 | €3.205,71 | €9.617,13 | €187,73 | €-27,82 |
| TEST | Top 5 + BTC — Guard | 3 | €9.361,45 | €1.914,54 | €3.829,08 | €138,14 | €29,06 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.337,99 | €475,06 | €1.425,18 | €139,18 | €10,76 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.328,60 | €2.905,34 | €5.810,68 | €92,90 | €32,86 |
| TEST | Scanner Top10 Long | 4 | €9.316,04 | €2.020,88 | €4.041,76 | €137,91 | €4,59 |
| TEST | Scanner Top15 Long | 4 | €9.316,04 | €2.020,88 | €4.041,76 | €137,91 | €4,59 |
| TEST | Scanner Top20 Long | 4 | €9.316,04 | €2.020,88 | €4.041,76 | €137,91 | €4,59 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.313,87 | €1.904,81 | €3.809,61 | €137,44 | €28,92 |
| TEST | Combo Trend | 6 | €9.261,73 | €1.769,19 | €3.538,39 | €96,87 | €29,12 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 4 | €9.234,38 | €1.462,29 | €2.924,57 | €52,74 | €18,53 |
| TEST | Benchmark trend following EMA 1H | 9 | €9.145,81 | €2.873,93 | €5.747,85 | €136,93 | €-1,72 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.143,74 | €1.870,01 | €3.740,03 | €134,93 | €28,39 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 2 | €9.143,13 | €3.642,04 | €7.284,08 | €78,67 | €20,24 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €9.127,94 | €3.195,37 | €6.390,74 | €138,94 | €8,35 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €9.122,59 | €3.193,50 | €6.387,00 | €138,86 | €8,34 |
| TEST | Rapida V3 — Long Only | 1 | €9.114,39 | €166,02 | €498,07 | €0,00 | €27,00 |
| TEST | Master Adaptive Strict3 V1 | 2 | €9.091,26 | €1.605,81 | €3.211,63 | €85,72 | €7,09 |
| TEST | Forza relativa 1H V1 | 5 | €9.087,27 | €5.037,46 | €10.074,93 | €180,32 | €2,35 |
| TEST | Combo Scanner | 3 | €9.080,89 | €1.831,17 | €3.662,33 | €92,80 | €27,28 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.061,87 | €1.434,97 | €2.869,94 | €51,75 | €18,18 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €9.037,35 | €1.612,41 | €3.224,82 | €92,84 | €20,65 |
| TEST | Top 5 + BTC — solo MFE | 3 | €8.864,80 | €1.581,63 | €3.163,25 | €91,07 | €20,25 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €8.746,92 | €1.479,67 | €2.959,34 | €90,13 | €-9,13 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.656,20 | €-379,65 | 42 | 42 | 33,33% | 0,72 | €-9,04 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.629,63 | €657,21 | 63 | 63 | 47,62% | 1,44 | €10,43 | 3,63% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.611,75 | €604,98 | 72 | 72 | 50,00% | 1,40 | €8,40 | 3,35% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.392,34 | €402,00 | 23 | 23 | 47,83% | 1,80 | €17,48 | 2,40% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.388,86 | €303,70 | 125 | 124 | 44,00% | 1,11 | €2,43 | 4,89% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.379,37 | €406,30 | 31 | 31 | 45,16% | 1,64 | €13,11 | 3,63% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.348,78 | €349,47 | 33 | 33 | 51,52% | 1,41 | €10,59 | 2,31% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.332,02 | €332,02 | 34 | 34 | 47,06% | 1,47 | €9,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.266,86 | €267,44 | 114 | 114 | 43,86% | 1,11 | €2,35 | 6,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.214,82 | €184,72 | 128 | 128 | 43,75% | 1,08 | €1,44 | 3,64% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.199,20 | €224,39 | 56 | 56 | 44,64% | 1,19 | €4,01 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.157,91 | €127,70 | 48 | 48 | 50,00% | 1,14 | €2,66 | 2,94% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.139,86 | €113,14 | 78 | 78 | 42,31% | 1,06 | €1,45 | 8,85% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.124,16 | €104,33 | 11 | 11 | 36,36% | 1,53 | €9,48 | 1,80% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.112,64 | €29,75 | 83 | 82 | 46,99% | 1,01 | €0,36 | 5,23% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.039,30 | €39,30 | 6 | 6 | 50,00% | 1,24 | €6,55 | 1,89% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.035,87 | €18,81 | 118 | 118 | 40,68% | 1,01 | €0,16 | 6,72% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.011,37 | €11,94 | 78 | 78 | 42,31% | 1,01 | €0,15 | 6,52% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Doge Ema 1H | Trend following EMA | €10.004,97 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,10% |
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
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Ampia 4H | Confluenza trend | €9.979,54 | €-46,73 | 37 | 37 | 24,32% | 0,95 | €-1,26 | 4,45% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.973,77 | €-26,23 | 7 | 7 | 57,14% | 0,84 | €-3,75 | 1,49% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.931,19 | €-68,81 | 3 | 3 | 33,33% | 0,35 | €-22,94 | 0,87% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Btc Ema 4H | Trend following EMA | €9.930,36 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,28% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.928,55 | €-71,45 | 3 | 3 | 33,33% | 0,32 | €-23,82 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.902,43 | €-61,85 | 100 | 100 | 38,00% | 0,97 | €-0,62 | 7,32% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €9.897,76 | €-112,57 | 58 | 58 | 41,38% | 0,91 | €-1,94 | 7,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.875,62 | €-124,38 | 8 | 8 | 37,50% | 0,49 | €-15,55 | 2,74% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.872,36 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,86% |
| TEST | Btc Ema 1H | Trend following EMA | €9.848,58 | €-151,42 | 9 | 9 | 33,33% | 0,53 | €-16,82 | 1,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.838,66 | €-161,34 | 31 | 28 | 38,71% | 0,80 | €-5,20 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €9.824,97 | €-163,51 | 83 | 83 | 38,55% | 0,90 | €-1,97 | 5,40% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.818,94 | €-196,29 | 61 | 61 | 34,43% | 0,86 | €-3,22 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.818,94 | €-196,29 | 61 | 61 | 34,43% | 0,86 | €-3,22 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.818,94 | €-196,29 | 61 | 61 | 34,43% | 0,86 | €-3,22 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €9.811,70 | €-188,30 | 38 | 38 | 44,74% | 0,80 | €-4,96 | 4,50% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.805,38 | €-192,61 | 32 | 32 | 40,62% | 0,75 | €-6,02 | 3,91% |
| TEST | Sol Ema 4H | Trend following EMA | €9.792,72 | €-207,28 | 4 | 4 | 0,00% | 0,00 | €-51,82 | 2,10% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.762,69 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Sol Ema 1H | Trend following EMA | €9.760,52 | €-239,48 | 9 | 9 | 22,22% | 0,37 | €-26,61 | 3,16% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.750,43 | €-264,94 | 53 | 53 | 33,96% | 0,78 | €-5,00 | 5,27% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.735,60 | €-279,75 | 54 | 54 | 33,33% | 0,75 | €-5,18 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.720,12 | €-282,28 | 22 | 22 | 36,36% | 0,63 | €-12,83 | 4,21% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.720,09 | €-279,91 | 34 | 34 | 41,18% | 0,74 | €-8,23 | 5,09% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.707,04 | €-326,79 | 106 | 105 | 44,34% | 0,84 | €-3,08 | 7,17% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.695,12 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,53% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.682,78 | €-399,79 | 142 | 141 | 35,21% | 0,87 | €-2,82 | 4,95% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.668,04 | €-331,57 | 104 | 104 | 42,31% | 0,87 | €-3,19 | 6,10% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.660,68 | €-354,55 | 81 | 81 | 33,33% | 0,79 | €-4,38 | 6,41% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.643,60 | €-390,00 | 150 | 149 | 37,33% | 0,87 | €-2,60 | 7,14% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.630,78 | €-368,87 | 72 | 72 | 40,28% | 0,81 | €-5,12 | 5,23% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.622,28 | €-392,25 | 78 | 75 | 39,74% | 0,85 | €-5,03 | 8,11% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.621,05 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,47% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.597,86 | €-404,51 | 22 | 22 | 27,27% | 0,48 | €-18,39 | 5,41% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.587,77 | €-386,92 | 70 | 64 | 41,43% | 0,77 | €-5,53 | 7,27% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.572,84 | €-455,22 | 70 | 70 | 34,29% | 0,74 | €-6,50 | 8,59% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.566,72 | €-446,93 | 49 | 49 | 36,73% | 0,66 | €-9,12 | 5,16% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.564,42 | €-435,33 | 73 | 73 | 42,47% | 0,78 | €-5,96 | 6,55% |
| TEST | Eth Ema 1H | Trend following EMA | €9.522,40 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,80% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.515,13 | €-484,87 | 46 | 46 | 30,43% | 0,64 | €-10,54 | 7,10% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.502,54 | €-564,16 | 75 | 75 | 44,00% | 0,75 | €-7,52 | 6,85% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.501,03 | €-528,84 | 46 | 46 | 26,09% | 0,62 | €-11,50 | 8,39% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.490,93 | €-538,91 | 41 | 41 | 31,71% | 0,60 | €-13,14 | 7,98% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.476,46 | €-550,50 | 50 | 50 | 36,00% | 0,66 | €-11,01 | 7,74% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.470,20 | €-559,67 | 47 | 47 | 31,91% | 0,67 | €-11,91 | 6,80% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.457,25 | €-562,34 | 69 | 69 | 36,23% | 0,70 | €-8,15 | 11,27% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.454,25 | €-543,27 | 50 | 50 | 34,00% | 0,68 | €-10,87 | 6,90% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.454,22 | €-575,51 | 43 | 43 | 30,23% | 0,62 | €-13,38 | 7,80% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.434,38 | €-554,55 | 84 | 84 | 36,90% | 0,68 | €-6,60 | 6,20% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.428,27 | €-654,02 | 124 | 123 | 37,10% | 0,76 | €-5,27 | 7,03% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.417,07 | €-610,53 | 114 | 114 | 38,60% | 0,75 | €-5,36 | 11,66% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.401,29 | €-638,09 | 42 | 42 | 26,19% | 0,59 | €-15,19 | 8,18% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.366,12 | €-600,10 | 56 | 56 | 33,93% | 0,52 | €-10,72 | 7,05% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.361,45 | €-665,17 | 55 | 55 | 32,73% | 0,62 | €-12,09 | 7,34% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.337,99 | €-674,38 | 49 | 49 | 32,65% | 0,58 | €-13,76 | 9,05% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.328,60 | €-700,73 | 78 | 78 | 48,72% | 0,59 | €-8,98 | 9,02% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.316,04 | €-685,94 | 50 | 50 | 34,00% | 0,53 | €-13,72 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.316,04 | €-685,94 | 50 | 50 | 34,00% | 0,53 | €-13,72 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.316,04 | €-685,94 | 50 | 50 | 34,00% | 0,53 | €-13,72 | 10,31% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.313,87 | €-712,63 | 65 | 65 | 36,92% | 0,63 | €-10,96 | 7,02% |
| TEST | Combo Trend | Combo Trend | €9.261,73 | €-765,22 | 110 | 110 | 33,64% | 0,75 | €-6,96 | 9,82% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.234,38 | €-782,06 | 87 | 87 | 33,33% | 0,60 | €-8,99 | 10,14% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.145,81 | €-848,62 | 76 | 76 | 28,95% | 0,54 | €-11,17 | 9,53% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.143,74 | €-882,27 | 72 | 72 | 36,11% | 0,58 | €-12,25 | 8,78% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.143,13 | €-872,67 | 33 | 33 | 18,18% | 0,37 | €-26,44 | 11,09% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.127,94 | €-876,59 | 54 | 54 | 31,48% | 0,49 | €-16,23 | 11,61% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.122,59 | €-881,93 | 58 | 58 | 32,76% | 0,49 | €-15,21 | 11,90% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.114,39 | €-912,33 | 90 | 90 | 28,89% | 0,62 | €-10,14 | 10,56% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.091,26 | €-913,48 | 47 | 47 | 27,66% | 0,57 | €-19,44 | 11,51% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.087,27 | €-909,05 | 94 | 94 | 29,79% | 0,61 | €-9,67 | 11,15% |
| TEST | Combo Scanner | Combo Scanner | €9.080,89 | €-948,24 | 74 | 74 | 35,14% | 0,58 | €-12,81 | 11,38% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.061,87 | €-954,26 | 68 | 68 | 32,35% | 0,43 | €-14,03 | 10,14% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.037,35 | €-981,37 | 50 | 50 | 32,00% | 0,39 | €-19,63 | 11,72% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €8.864,80 | €-1.153,56 | 62 | 62 | 32,26% | 0,32 | €-18,61 | 12,28% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €8.746,92 | €-1.242,21 | 94 | 94 | 31,91% | 0,44 | €-13,21 | 12,57% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99401 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €34,78 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,06976 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,09 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1889,17209 | 1893,51000 | 1916,37617 | 2509,45026 | 1834,76393 | €43,74 | €131,21 | €1,89 | €-0,30 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,93 | €104,79 | €1,51 | €-0,00 |
| Bilanciata 1H V1 | GPS | LONG | Confluenza trend | 60m | 3,0x | 0,01630 | 0,01712 | 0,01445 | 0,01095 | 0,02000 | €133,98 | €401,93 | €45,63 | €20,23 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06998 | 0,06976 | 0,07099 | 0,09295 | 0,06796 | €1.095,91 | €3.287,73 | €47,34 | €10,24 |
| Bilanciata 1H — LONG senza Range High Vol | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | LONG | Confluenza trend | 60m | 3,0x | 512,07239 | 507,82000 | 503,16526 | 343,94196 | 529,88667 | €65,27 | €195,80 | €3,41 | €-1,63 |
| Bilanciata 1H — LONG senza Range High Vol | GPS | LONG | Confluenza trend | 60m | 3,0x | 0,01658 | 0,01712 | 0,01459 | 0,01114 | 0,02056 | €127,57 | €382,70 | €45,92 | €12,39 |
| Bilanciata 1H — SHORT Trend Down stretto | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,06976 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €18,59 |
| Bilanciata 1H — SHORT Trend Down stretto | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 0,99401 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €0,65 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 512,07239 | 507,82000 | 503,16526 | 343,94196 | 529,88667 | €925,85 | €2.777,56 | €48,31 | €-23,07 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06976 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,08 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99401 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €0,74 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.164,76 | €3.494,29 | €50,32 | €-0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 514,86295 | 507,82000 | 506,12617 | 345,81628 | 532,33652 | €992,76 | €2.978,27 | €50,54 | €-40,74 |
| Bilanciata 1H V3 Filtered | GPS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01431 | 0,01091 | 0,02011 | €141,49 | €424,46 | €50,53 | €23,01 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 59,29886 | 59,06100 | 58,44495 | 39,82907 | 61,00666 | €1.026,23 | €3.078,69 | €44,33 | €-12,35 |
| Rapida V1 — score 6–7,5 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €144,97 | €434,90 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.575,03 | €4.725,08 | €52,92 | €-0,00 |
| Rapida V1 — score 6–7,5 | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01666 | 0,01712 | 0,01524 | 0,01119 | 0,01879 | €201,11 | €603,33 | €51,36 | €16,66 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99401 | 1,00671 | 1,32244 | 0,97884 | €1.521,02 | €4.563,07 | €51,11 | €7,11 |
| Rapida score 6–7,5 — senza Trend Up | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €141,11 | €423,34 | €50,80 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.533,15 | €4.599,45 | €51,51 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01666 | 0,01712 | 0,01524 | 0,01119 | 0,01879 | €195,76 | €587,29 | €49,99 | €16,22 |
| Rapida score 6–7,5 — senza Trend Up | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99401 | 1,00671 | 1,32244 | 0,97884 | €1.480,58 | €4.441,75 | €49,75 | €6,92 |
| Rapida score 6–7,5 — Range Only | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99401 | 1,00671 | 1,32244 | 0,97884 | €1.578,12 | €4.734,36 | €53,02 | €7,38 |
| Rapida score 6–7,5 — Cost Aware | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01704 | 0,01712 | 0,01547 | 0,01145 | 0,01940 | €191,76 | €575,28 | €53,13 | €2,59 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| Rapida V1 — senza PEPE | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01850 | €187,17 | €561,52 | €0,00 | €30,44 |
| Rapida V1 — target pieno 2R | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €115,44 | €346,32 | €3,88 | €-0,00 |
| Rapida V1 — target pieno 2R | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01925 | €164,28 | €492,85 | €0,00 | €26,71 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered — madre | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,35 | €73,04 | €0,82 | €-0,00 |
| Rapida 1H V3 Filtered — madre | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01850 | €176,73 | €530,19 | €0,00 | €28,74 |
| Rapida 1H V3 Filtered — madre | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €154,24 | €462,73 | €40,02 | €0,00 |
| Rapida V3 — score <7,5 | APR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €136,16 | €408,49 | €49,02 | €-0,00 |
| Rapida V3 — score <7,5 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.494,66 | €4.483,99 | €50,22 | €-0,00 |
| Rapida V3 — score <7,5 | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01666 | 0,01712 | 0,01524 | 0,01119 | 0,01879 | €195,87 | €587,61 | €50,02 | €16,22 |
| Rapida V3 — score <7,5 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99556 | 0,99401 | 1,00671 | 1,32244 | 0,97884 | €1.491,98 | €4.475,94 | €50,13 | €6,97 |
| Rapida V3 — score <7,5 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06970 | 0,06976 | 0,07048 | 0,09258 | 0,06853 | €37,09 | €111,27 | €1,25 | €-0,10 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| Rapida V3 — Long Only | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01850 | €166,02 | €498,07 | €0,00 | €27,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| Rapida V3 — senza ESPORTS | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,35 | €55,04 | €0,62 | €-0,00 |
| Rapida V3 — senza ESPORTS | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01850 | €172,70 | €518,09 | €0,00 | €28,08 |
| Rapida V3 senza ESPORTS — Long Only | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01850 | €174,37 | €523,12 | €0,00 | €28,36 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,51 | €73,52 | €0,82 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01624 | 0,01091 | 0,01850 | €177,89 | €533,68 | €0,00 | €28,93 |
| Rapida V3 senza ESPORTS — MFE Lock | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €155,26 | €465,77 | €40,28 | €0,00 |
| Rapida V3 — qualità completa + profit lock | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 9,38563 | 9,38563 | 9,22869 | 6,30401 | 9,62103 | €949,50 | €2.848,50 | €47,63 | €0,00 |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1893,51000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €8,67 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 59,06100 | 58,25395 | 39,57042 | 59,90353 | €33,51 | €100,52 | €1,13 | €0,25 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 0,99401 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €27,09 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 64163,30000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €-1,43 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,06976 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,20 |
| Ampia 4H | BTW | LONG | Confluenza trend | 240m | 2,0x | 0,32695 | 0,32695 | 0,28771 | 0,16511 | 0,43680 | €207,21 | €414,42 | €49,73 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,49 | €-0,00 |
| Forza relativa 1H V1 | GPS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,01630 | 0,01712 | 0,01445 | 0,00823 | 0,02037 | €177,71 | €355,43 | €40,35 | €17,89 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 59,44389 | 59,06100 | 58,58789 | 30,01916 | 61,32707 | €1.587,77 | €3.175,54 | €45,73 | €-20,45 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,99556 | 0,99401 | 1,00990 | 1,48836 | 0,96402 | €1.577,31 | €3.154,62 | €45,43 | €4,91 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | GPS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01652 | 0,01712 | 0,01483 | 0,00834 | 0,02024 | €231,94 | €463,89 | €47,46 | €16,85 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €0,00 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06976 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-11,61 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 59,28285 | 59,06100 | 58,33433 | 29,93784 | 61,65417 | €1.599,80 | €3.199,61 | €51,19 | €-11,97 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €0,00 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06976 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-11,33 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 59,28285 | 59,06100 | 58,33433 | 29,93784 | 61,65417 | €1.562,14 | €3.124,27 | €49,99 | €-11,69 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,06976 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,25 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 0,99401 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €0,32 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 74,94501 | 75,65600 | 76,14413 | 112,04279 | 72,30694 | €1.248,89 | €2.497,78 | €39,96 | €-23,70 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 59,17783 | 59,06100 | 58,23099 | 29,88481 | 61,26089 | €74,07 | €148,13 | €2,37 | €-0,29 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 1911,30218 | 1893,51000 | 1880,72135 | 965,20760 | 1978,58002 | €44,44 | €88,89 | €1,42 | €-0,83 |
| Benchmark trend following EMA 1H | GPS | LONG | Trend following EMA | 60m | 2,0x | 0,01697 | 0,01712 | 0,01505 | 0,00857 | 0,02119 | €203,01 | €406,01 | €45,92 | €3,58 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,20797 | €186,11 | €372,23 | €44,67 | €18,94 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.703,71 | €3.407,43 | €49,07 | €1,28 |
| Scanner Top 5 Long 1H | GPS | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01622 | 0,01712 | 0,01460 | 0,00819 | 0,01945 | €254,32 | €508,64 | €50,72 | €28,23 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,21475 | €200,95 | €401,89 | €48,23 | €20,45 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,06976 | 0,07070 | 0,10420 | 0,06769 | €1.674,47 | €3.348,95 | €48,22 | €-2,97 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €1,18 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 1911,30218 | 1893,51000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,63 |
| Scanner Top10 Long | GPS | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01697 | 0,01712 | 0,01524 | 0,00857 | 0,02043 | €228,91 | €457,83 | €46,60 | €4,04 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,16396 | 75,65600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,23 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,21475 | €204,24 | €408,48 | €49,02 | €20,79 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06970 | 0,06976 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-3,02 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €1,18 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 1911,30218 | 1893,51000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,63 |
| Scanner Top15 Long | GPS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01697 | 0,01712 | 0,01524 | 0,00857 | 0,02043 | €228,91 | €457,83 | €46,60 | €4,04 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,16396 | 75,65600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,23 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,21475 | €204,24 | €408,48 | €49,02 | €20,79 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06970 | 0,06976 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-3,02 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €1,18 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 1911,30218 | 1893,51000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,63 |
| Scanner Top20 Long | GPS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01697 | 0,01712 | 0,01524 | 0,00857 | 0,02043 | €228,91 | €457,83 | €46,60 | €4,04 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,16396 | 75,65600 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,23 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,21475 | €204,24 | €408,48 | €49,02 | €20,79 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06970 | 0,06976 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-3,02 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €201,00 | €402,01 | €47,85 | €21,79 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,41588 | 59,06100 | 58,56029 | 30,00502 | 61,29818 | €15,47 | €30,93 | €0,45 | €-0,18 |
| Top 5 + BTC — solo MFE | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Top 5 + BTC — solo MFE | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €188,41 | €376,82 | €44,86 | €20,43 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,41588 | 59,06100 | 58,56029 | 30,00502 | 61,29818 | €14,50 | €29,00 | €0,42 | €-0,17 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Top 5 + BTC — Guard | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,06100 | 58,06542 | 29,75146 | 60,78017 | €1.519,74 | €3.039,48 | €43,77 | €7,60 |
| Top 5 + BTC — Guard | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €198,03 | €396,06 | €47,14 | €21,47 |
| Top 5 + BTC — BTC≤3 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Top 5 + BTC — BTC≤3 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €192,08 | €384,16 | €45,73 | €20,82 |
| Top 5 + BTC — BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,41588 | 59,06100 | 58,56029 | 30,00502 | 61,29818 | €14,78 | €29,56 | €0,43 | €-0,18 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,06100 | 58,06542 | 29,75146 | 60,78017 | €1.484,39 | €2.968,79 | €42,75 | €7,42 |
| Top 5 + BTC — Guard + MFE | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €193,42 | €386,84 | €46,05 | €20,97 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,06100 | 58,06542 | 29,75146 | 60,78017 | €1.538,41 | €3.076,82 | €44,31 | €7,69 |
| Top 5 + BTC — Guard + BTC≤3 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €200,46 | €400,92 | €47,72 | €21,73 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,06100 | 58,06542 | 29,75146 | 60,78017 | €1.512,01 | €3.024,03 | €43,55 | €7,56 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €197,02 | €394,04 | €46,91 | €21,36 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02204 | €194,18 | €388,37 | €46,23 | €21,05 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,29886 | 59,06100 | 58,44495 | 29,94592 | 61,86057 | €1.584,08 | €3.168,15 | €45,62 | €-12,71 |
| Top 5 + BTC — target pieno 3R | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Top 5 + BTC — target pieno 3R | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02204 | €194,30 | €388,60 | €46,26 | €21,06 |
| Top 5 + BTC — target pieno 3R | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,29886 | 59,06100 | 58,44495 | 29,94592 | 61,86057 | €1.585,00 | €3.170,01 | €45,65 | €-12,72 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,06976 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €16,21 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,06976 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,31 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 58,85077 | 59,06100 | 57,90916 | 29,71964 | 60,92231 | €1.350,47 | €2.700,94 | €43,22 | €9,65 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 510,90216 | 507,82000 | 501,16840 | 258,00559 | 532,31642 | €21,03 | €42,06 | €0,80 | €-0,25 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €118,87 | €237,73 | €3,80 | €-0,00 |
| Combo Trend | GPS | LONG | Combo Trend | 60m | 2,0x | 0,01630 | 0,01712 | 0,01434 | 0,00823 | 0,02060 | €192,92 | €385,84 | €46,30 | €19,42 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,06976 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €6,77 |
| Combo Scanner | GPS | LONG | Combo Scanner | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02049 | €191,44 | €382,89 | €45,58 | €20,75 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 59,41588 | 59,06100 | 58,56029 | 30,00502 | 61,29818 | €20,21 | €40,41 | €0,58 | €-0,24 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06976 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,33 |
| Combo Adaptive — madre | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02011 | €210,12 | €420,24 | €50,02 | €22,78 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 531,95932 | €1.419,29 | €2.838,59 | €50,33 | €-32,72 |
| Combo Adaptive — MFE Trail esistente | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,06976 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,06 |
| Combo Adaptive — MFE Trail esistente | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02011 | €186,88 | €373,75 | €44,49 | €20,26 |
| Combo Adaptive — MFE Trail esistente | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 531,95932 | €1.263,05 | €2.526,11 | €44,79 | €-29,12 |
| Combo Adaptive — MFE Trail esistente | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,41588 | 59,06100 | 58,56029 | 30,00502 | 61,12706 | €17,03 | €34,06 | €0,49 | €-0,20 |
| Combo Adaptive — Trend/Transition | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive — Trend/Transition | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive — Quality7 + Regime | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive — Quality7 + Regime | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive — Quality7 + Regime | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive — Long Only | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.675,98 | €3.351,96 | €48,27 | €1,26 |
| Combo Adaptive — Long Only | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01652 | 0,01712 | 0,01483 | 0,00834 | 0,01990 | €237,17 | €474,34 | €48,53 | €17,23 |
| Combo Adaptive — Long Only | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 531,95932 | €29,05 | €58,10 | €1,03 | €-0,67 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06976 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,32 |
| Combo Adaptive — parziale 1R | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02011 | €201,77 | €403,54 | €48,04 | €21,87 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 531,95932 | €1.362,87 | €2.725,74 | €48,33 | €-31,42 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €0,00 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06976 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,33 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02204 | €197,23 | €394,46 | €46,96 | €21,38 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 541,06761 | €138,01 | €276,03 | €4,89 | €-3,18 |
| Combo Adaptive — target pieno 3R | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €0,00 | €-0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06976 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,33 |
| Combo Adaptive — target pieno 3R | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01712 | 0,01431 | 0,00820 | 0,02204 | €193,55 | €387,09 | €46,08 | €20,98 |
| Combo Adaptive — target pieno 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 541,06761 | €135,44 | €270,87 | €4,80 | €-3,12 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 64163,30000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €-21,47 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 64163,30000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €-27,40 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1907,45141 | 1893,51000 | 1879,98411 | 1281,17153 | 1962,38601 | €1.105,17 | €3.315,52 | €47,74 | €-24,23 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,06976 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €18,58 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1893,51000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €-0,46 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €33,77 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1893,51000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,08 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.637,93 | €3.275,87 | €47,17 | €1,23 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €34,16 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,06100 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €7,09 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1893,51000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €-0,15 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 59,06100 | 58,18865 | 29,81460 | 60,73912 | €1.636,69 | €3.273,37 | €47,14 | €1,23 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1893,51000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €-0,46 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €33,32 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,06100 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €7,38 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €33,41 |
| Combo Adaptive — Side × Regime Guard | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,06976 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €6,93 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 0,99401 | 0,99748 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €0,00 | €35,10 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 507,82000 | 504,63443 | 259,44008 | 531,95932 | €1.398,25 | €2.796,51 | €49,58 | €-32,24 |
| Combo Adaptive — Side × Regime Guard | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,41588 | 59,06100 | 58,56029 | 30,00502 | 61,12706 | €68,07 | €136,14 | €1,96 | €-0,81 |
| Master Adaptive GB20 — Breakeven 0,5R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1893,51000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €-0,46 |
| Master Adaptive GB20 — Breakeven 0,5R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €33,93 |
| Master Adaptive GB20 — 50% a 0,75R | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1893,51000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €-0,46 |
| Master Adaptive GB20 — 50% a 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €33,90 |
| Master Adaptive GB20 — Loss Cap 0,75R | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1893,51000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €-17,77 |
| Master Adaptive GB20 — Loss Cap 0,75R | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64163,30000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €38,01 |
| Rapida V3 NoHigh — Regime Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1902,79048 | 1893,51000 | 1881,47923 | 1278,04094 | 1934,75736 | €1.508,82 | €4.526,45 | €50,70 | €-22,08 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99401 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €36,50 |
| MAIN — Side × Regime Guard | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| MAIN — Side × Regime Guard | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| MAIN — Side × Regime Guard | HYPE | LONG | Confluenza trend | 240m | 3,0x | 59,42488 | 59,06100 | 57,77054 | 39,91371 | 62,73356 | €20,16 | €60,47 | €1,68 | €-0,37 |
| MAIN — Side × Regime Guard | SNDK | LONG | Confluenza trend | 240m | 3,0x | 1787,69747 | 1712,48000 | 1707,14791 | 1200,73680 | 1948,79656 | €370,44 | €1.111,33 | €50,07 | €-46,76 |
| Combo Trend — Side × Regime Guard | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,06976 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-4,24 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 0,99401 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €32,53 |
| Combo Trend — Side × Regime Guard | ZEC | LONG | Combo Trend | 60m | 2,0x | 512,07239 | 507,82000 | 502,17558 | 258,59656 | 533,84539 | €45,72 | €91,45 | €1,77 | €-0,76 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €0,00 |
| Bilanciata V3 · LONG only | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06976 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,07 |
| Bilanciata V3 · LONG only | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99401 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €0,70 |
| Bilanciata V3 · LONG only | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.101,68 | €3.305,04 | €47,59 | €-0,00 |
| Bilanciata V3 · LONG only | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 514,86295 | 507,82000 | 506,12617 | 345,81628 | 532,33652 | €938,99 | €2.816,96 | €47,80 | €-38,53 |
| Bilanciata V3 · LONG only | GPS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,01624 | 0,01712 | 0,01431 | 0,01091 | 0,02011 | €133,83 | €401,48 | €47,79 | €21,76 |
| Bilanciata V3 · LONG only | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 59,29886 | 59,06100 | 58,44495 | 39,82907 | 61,00666 | €970,65 | €2.911,95 | €41,93 | €-11,68 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,21475 | €202,51 | €405,01 | €48,60 | €20,61 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,06976 | 0,07070 | 0,10420 | 0,06769 | €1.687,46 | €3.374,92 | €48,60 | €-2,99 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,26819 | 0,31648 | 0,42244 | 0,21475 | €202,81 | €405,63 | €48,68 | €20,64 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,06976 | 0,07070 | 0,10420 | 0,06769 | €1.690,03 | €3.380,06 | €48,67 | €-3,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top20 Long | XOM | LONG | 2026-08-18T06:05:44+00:00 | 160,14994 | €-5,06 | -0,11 | TIME_EXIT_NO_CANDLES |
| Scanner Top15 Long | XOM | LONG | 2026-08-18T06:05:44+00:00 | 160,14994 | €-5,06 | -0,11 | TIME_EXIT_NO_CANDLES |
| Scanner Top10 Long | XOM | LONG | 2026-08-18T06:05:44+00:00 | 160,14994 | €-5,06 | -0,11 | TIME_EXIT_NO_CANDLES |
| Scanner Top 5 Long 1H | XOM | LONG | 2026-08-18T06:05:44+00:00 | 160,14994 | €-5,50 | -0,11 | TIME_EXIT_NO_CANDLES |
| Bilanciata 1H — LONG senza Range High Vol | XOM | LONG | 2026-08-18T06:05:44+00:00 | 160,14994 | €-5,14 | -0,11 | TIME_EXIT_NO_CANDLES |
| Rapida V3 — senza ESPORTS | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €1,12 | 0,02 | TIME_EXIT_NO_CANDLES |
| Rapida V3 senza ESPORTS — MFE Lock | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €0,11 | 0,02 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V3 Filtered — madre | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €0,11 | 0,02 | TIME_EXIT_NO_CANDLES |
| Rapida V1 — target pieno 2R | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €1,15 | 0,02 | TIME_EXIT_NO_CANDLES |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-4,72 | -1,38 | STOP_GAP_STRESS |
| Top 5 + BTC — target pieno 3R | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-63,39 | -1,38 | STOP_GAP_STRESS |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-63,35 | -1,38 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 382/30 | 33/30 | 0,69 | 2,04 | -0,16R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 350/30 | 20/30 | 0,60 | 1,90 | -0,21R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 215/30 | 22/30 | 0,78 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 217/30 | 22/30 | 0,75 | 1,57 | -0,13R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 295/30 | 31/30 | 0,78 | 0,62 | -0,11R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 265/30 | 11/30 | 0,68 | 0,00 | -0,16R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 121/30 | 8/30 | 0,67 | 1,02 | -0,17R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 276/30 | 17/30 | 0,59 | 4,50 | -0,23R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 422/30 | 24/30 | 0,68 | 0,64 | -0,17R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 386/30 | 7/30 | 0,59 | 0,02 | -0,21R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 295/30 | 30/30 | 0,82 | 1,02 | -0,09R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 536/30 | 55/30 | 0,82 | 1,12 | -0,09R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 121/30 | 15/30 | 0,42 | 0,99 | -0,39R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 480/30 | 44/30 | 0,69 | 1,20 | -0,16R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 484/30 | 37/30 | 0,69 | 0,76 | -0,16R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 444/30 | 23/30 | 0,60 | 1,12 | -0,21R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 275/30 | 42/30 | 0,72 | 0,72 | -0,17R | €-9,04 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 23/30 | 0,00 | 1,80 | 0,00R | €17,48 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 25/30 | 15/30 | 0,53 | 0,83 | -0,26R | €-0,83 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 39/30 | 24/30 | 0,62 | 0,47 | -0,21R | €-2,87 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 654/30 | 114/30 | 0,87 | 0,75 | -0,07R | €-5,36 | 11,66% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 49/30 | 0,00 | 0,58 | 0,00R | €-13,76 | 9,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 11/30 | 0,00 | 1,53 | 0,00R | €9,48 | 1,80% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 228/30 | 64/30 | 1,03 | 0,77 | 0,02R | €-5,53 | 7,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 410/30 | 100/30 | 0,90 | 0,97 | -0,05R | €-0,62 | 7,32% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 331/30 | 56/30 | 0,80 | 0,52 | -0,11R | €-10,72 | 7,05% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 172/30 | 29/30 | 0,95 | 1,05 | -0,02R | €1,12 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 437/30 | 78/30 | 0,80 | 1,01 | -0,10R | €0,15 | 6,52% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 504/30 | 114/30 | 0,84 | 1,11 | -0,08R | €2,35 | 6,52% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 668/30 | 128/30 | 0,76 | 1,08 | -0,13R | €1,44 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 72/30 | 0,00 | 1,40 | 0,00R | €8,40 | 3,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 82/30 | 0,00 | 1,01 | 0,00R | €0,36 | 5,23% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 33/30 | 0,00 | 1,41 | 0,00R | €10,59 | 2,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 394/30 | 124/30 | 0,82 | 1,11 | -0,09R | €2,43 | 4,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 632/30 | 141/30 | 0,73 | 0,87 | -0,15R | €-2,82 | 4,95% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 49/30 | 28/30 | 0,59 | 0,80 | -0,24R | €-5,20 | 3,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 641/30 | 149/30 | 0,79 | 0,87 | -0,11R | €-2,60 | 7,14% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 467/30 | 118/30 | 0,79 | 1,01 | -0,11R | €0,16 | 6,72% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 256/30 | 75/30 | 0,92 | 0,75 | -0,04R | €-7,52 | 6,85% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 259/30 | 72/30 | 0,88 | 0,81 | -0,06R | €-5,12 | 5,23% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 356/30 | 90/30 | 0,86 | 0,62 | -0,07R | €-10,14 | 10,56% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 34/30 | 0,00 | 1,47 | 0,00R | €9,77 | 3,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 56/30 | 0,00 | 1,19 | 0,00R | €4,01 | 5,24% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 531/30 | 104/30 | 0,76 | 0,87 | -0,13R | €-3,19 | 6,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 70/30 | 0,00 | 0,74 | 0,00R | €-6,50 | 8,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 105/30 | 0,00 | 0,84 | 0,00R | €-3,08 | 7,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 38/30 | 0,00 | 0,80 | 0,00R | €-4,96 | 4,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 594/30 | 123/30 | 0,75 | 0,76 | -0,13R | €-5,27 | 7,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 259/30 | 37/30 | 0,70 | 0,95 | -0,20R | €-1,26 | 4,45% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 182/30 | 73/30 | 1,14 | 0,78 | 0,06R | €-5,96 | 6,55% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 11/30 | 5/30 | 0,57 | 0,89 | -0,22R | €-2,34 | 1,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 8/30 | 5/30 | 2,79 | 3,42 | 0,51R | €27,68 | 0,85% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 14/30 | 7/30 | 0,22 | 0,84 | -0,63R | €-3,75 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 4/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,86% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 15/30 | 9/30 | 0,78 | 0,53 | -0,13R | €-16,82 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 1,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 527/30 | 83/30 | 0,97 | 0,90 | -0,02R | €-1,97 | 5,40% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 290/30 | 49/30 | 0,97 | 0,66 | -0,02R | €-9,12 | 5,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 564/30 | 94/30 | 0,96 | 0,44 | -0,02R | €-13,21 | 12,57% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 468/30 | 84/30 | 0,92 | 0,68 | -0,04R | €-6,60 | 6,20% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 62/30 | 22/30 | 1,22 | 0,63 | 0,10R | €-12,83 | 4,21% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 62/30 | 22/30 | 1,15 | 0,48 | 0,07R | €-18,39 | 5,41% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 152/30 | 46/30 | 0,88 | 0,64 | -0,06R | €-10,54 | 7,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 189/30 | 32/30 | 0,86 | 0,75 | -0,07R | €-6,02 | 3,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 87/30 | 0,74 | 0,60 | -0,20R | €-8,99 | 10,14% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 58/30 | 0,00 | 0,91 | 0,00R | €-1,94 | 7,02% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 68/30 | 0,74 | 0,43 | -0,20R | €-14,03 | 10,14% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 88/30 | 34/30 | 1,23 | 0,74 | 0,10R | €-8,23 | 5,09% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_SCANNER | Combo Scanner | 329/30 | 74/30 | 1,08 | 0,58 | 0,04R | €-12,81 | 11,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 437/30 | 110/30 | 0,90 | 0,75 | -0,06R | €-6,96 | 9,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 48/30 | 0,00 | 1,14 | 0,00R | €2,66 | 2,94% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 8/30 | 6/30 | 1,44 | 0,85 | 0,18R | €-4,12 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 12/30 | 10/30 | 0,51 | 0,62 | -0,36R | €-10,55 | 2,13% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 18/30 | 12/30 | 0,40 | 0,94 | -0,41R | €-1,28 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 208/30 | 63/30 | 0,83 | 1,44 | -0,11R | €10,43 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 138/30 | 31/30 | 0,80 | 1,64 | -0,12R | €13,11 | 3,63% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 440/30 | 76/30 | 0,87 | 0,54 | -0,07R | €-11,17 | 9,53% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 14/30 | 8/30 | 0,30 | 0,05 | -0,56R | €-38,45 | 3,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 13/30 | 7/30 | 0,28 | 0,28 | -0,63R | €-33,90 | 2,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 20/30 | 11/30 | 0,29 | 0,11 | -0,55R | €-41,03 | 4,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-52,67 | 1,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 12/30 | 15/30 | 0,89 | 0,35 | -0,07R | €-21,51 | 3,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 262/30 | 50/30 | 1,01 | 0,68 | 0,01R | €-10,87 | 6,90% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 46/30 | 0,00 | 0,62 | 0,00R | €-11,50 | 8,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 33/30 | 0,00 | 0,37 | 0,00R | €-26,44 | 11,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 41/30 | 0,00 | 0,60 | 0,00R | €-13,14 | 7,98% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 487/30 | 78/30 | 1,40 | 0,59 | 0,13R | €-8,98 | 9,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 230/30 | 47/30 | 1,03 | 0,67 | 0,02R | €-11,91 | 6,80% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 239/30 | 42/30 | 0,99 | 0,59 | -0,01R | €-15,19 | 8,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 166/30 | 47/30 | 1,02 | 0,57 | 0,01R | €-19,44 | 11,51% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 252/30 | 43/30 | 0,98 | 0,62 | -0,01R | €-13,38 | 7,80% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 552/30 | 94/30 | 0,86 | 0,61 | -0,08R | €-9,67 | 11,15% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 220/30 | 75/30 | 1,14 | 0,85 | 0,07R | €-5,03 | 8,11% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 195/30 | 61/30 | 0,49 | 0,86 | -0,29R | €-3,22 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 195/30 | 61/30 | 0,49 | 0,86 | -0,29R | €-3,22 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 195/30 | 61/30 | 0,49 | 0,86 | -0,29R | €-3,22 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 228/30 | 81/30 | 0,68 | 0,79 | -0,18R | €-4,38 | 6,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 230/30 | 53/30 | 0,74 | 0,78 | -0,12R | €-5,00 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 208/30 | 54/30 | 0,65 | 0,75 | -0,16R | €-5,18 | 5,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 269/30 | 50/30 | 0,98 | 0,53 | -0,01R | €-13,72 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 270/30 | 50/30 | 0,98 | 0,53 | -0,01R | €-13,72 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 270/30 | 50/30 | 0,98 | 0,53 | -0,01R | €-13,72 | 10,31% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 317/30 | 69/30 | 1,10 | 0,70 | 0,05R | €-8,15 | 11,27% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 125/30 | 10/30 | 0,87 | 0,87 | -0,07R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 270/30 | 50/30 | 0,94 | 0,39 | -0,03R | €-19,63 | 11,72% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 284/30 | 65/30 | 1,16 | 0,63 | 0,07R | €-10,96 | 7,02% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 238/30 | 50/30 | 1,03 | 0,66 | 0,01R | €-11,01 | 7,74% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 295/30 | 72/30 | 1,17 | 0,58 | 0,07R | €-12,25 | 8,78% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 246/30 | 55/30 | 1,03 | 0,62 | 0,02R | €-12,09 | 7,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 335/30 | 62/30 | 1,07 | 0,32 | 0,03R | €-18,61 | 12,28% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 266/30 | 58/30 | 0,99 | 0,49 | -0,01R | €-15,21 | 11,90% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 253/30 | 54/30 | 0,98 | 0,49 | -0,01R | €-16,23 | 11,61% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 347/30 | 78/30 | 1,10 | 1,06 | 0,05R | €1,45 | 8,85% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 21/30 | 10/30 | 0,36 | 0,15 | -0,54R | €-37,89 | 4,47% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 3/30 | 3/30 | 0,58 | 0,32 | -0,30R | €-23,82 | 0,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 12/30 | 6/30 | 0,81 | 1,24 | -0,11R | €6,55 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 15/30 | 8/30 | 0,55 | 0,49 | -0,34R | €-15,55 | 2,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 3/30 | 3/30 | 0,63 | 0,35 | -0,26R | €-22,94 | 0,87% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 19/30 | 9/30 | 0,51 | 0,37 | -0,40R | €-26,61 | 3,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 4/30 | 4/30 | 0,00 | 0,00 | -1,06R | €-51,82 | 2,10% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06976**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.8 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64163.3 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.06987**; close **0.06977**; wick alta **0.0%**; volume **x0.08**

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
- Confidenza: **73,50%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sottoperformando BTC: mediana relativa -1.35%, 55% sotto -1%.
- BTC trend score: **0,00**; ADX: **23,05**; breadth sopra EMA50: **50,00%**
- Mediana alt vs BTC: **-1,35%**; dispersione: **8,28%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **2**
- Posizioni research aperte: **534**
- Trade research chiusi: **25649**
- Eventi di mercato indipendenti chiusi: **3549**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **66192**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 10 | 382 | 382 | 29,84% | 0,69 | -0,16R | €-613,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 10 | 350 | 350 | 28,86% | 0,60 | -0,21R | €-728,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 2 | 215 | 215 | 45,58% | 0,78 | -0,12R | €-253,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 2 | 217 | 217 | 31,80% | 0,75 | -0,13R | €-278,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 4 | 295 | 295 | 31,86% | 0,78 | -0,11R | €-327,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 4 | 265 | 265 | 31,70% | 0,68 | -0,16R | €-414,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 0 | 121 | 121 | 33,88% | 0,67 | -0,17R | €-207,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 1 | 276 | 276 | 26,81% | 0,59 | -0,23R | €-642,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 4 | 422 | 422 | 29,15% | 0,68 | -0,17R | €-702,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 4 | 386 | 386 | 27,98% | 0,59 | -0,21R | €-827,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 4 | 295 | 295 | 32,54% | 0,82 | -0,09R | €-268,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 10 | 536 | 536 | 39,74% | 0,82 | -0,09R | €-456,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 121 | 121 | 28,10% | 0,42 | -0,39R | €-469,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 10 | 480 | 480 | 29,17% | 0,69 | -0,16R | €-767,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 10 | 484 | 484 | 29,13% | 0,69 | -0,16R | €-767,80 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 10 | 444 | 444 | 27,93% | 0,60 | -0,21R | €-924,83 |
| MAIN | 16 | 275 | 275 | 25,82% | 0,72 | -0,17R | €-468,64 |
| RSI_EXTREME_LONG_15M | 0 | 25 | 25 | 44,00% | 0,53 | -0,26R | €-64,41 |
| RSI_EXTREME_SHORT_15M | 0 | 39 | 39 | 38,46% | 0,62 | -0,21R | €-80,70 |
| Bilanciata 1H V1 | 14 | 654 | 654 | 33,03% | 0,87 | -0,07R | €-449,68 |
| Bilanciata 1H V2 | 5 | 261 | 228 | 36,78% | 1,03 | 0,02R | €45,89 |
| Bilanciata 1H V3 Filtered | 12 | 410 | 410 | 33,90% | 0,90 | -0,05R | €-218,77 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 12 | 331 | 331 | 32,63% | 0,80 | -0,11R | €-364,11 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 172 | 172 | 37,79% | 0,95 | -0,02R | €-41,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 4 | 437 | 437 | 34,32% | 0,80 | -0,10R | €-447,99 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 4 | 504 | 504 | 35,52% | 0,84 | -0,08R | €-413,65 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 9 | 668 | 668 | 33,53% | 0,76 | -0,13R | €-836,56 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 8 | 394 | 394 | 35,03% | 0,82 | -0,09R | €-367,35 |
| SHADOW_1H_FAST_TP2_V1 | 10 | 632 | 632 | 30,38% | 0,73 | -0,15R | €-927,68 |
| Rapida 1H V2 | 0 | 57 | 49 | 36,84% | 0,59 | -0,24R | €-135,15 |
| Rapida 1H V3 Filtered | 10 | 641 | 641 | 34,32% | 0,79 | -0,11R | €-701,00 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 10 | 467 | 467 | 34,48% | 0,79 | -0,11R | €-517,14 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 256 | 256 | 47,27% | 0,92 | -0,04R | €-112,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 259 | 259 | 36,68% | 0,88 | -0,06R | €-153,66 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 4 | 356 | 356 | 36,52% | 0,86 | -0,07R | €-260,02 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 4 | 531 | 531 | 33,33% | 0,76 | -0,13R | €-678,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 10 | 594 | 594 | 33,33% | 0,75 | -0,13R | €-782,96 |
| SHADOW_4H_WIDE | 26 | 259 | 259 | 20,08% | 0,70 | -0,20R | €-522,27 |
| SHADOW_BOLLINGER_MR_1H | 1 | 182 | 182 | 48,90% | 1,14 | 0,06R | €112,62 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 11 | 11 | 54,55% | 0,57 | -0,22R | €-23,77 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 8 | 8 | 75,00% | 2,79 | 0,51R | €40,58 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 14 | 14 | 28,57% | 0,22 | -0,63R | €-88,00 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,93 |
| SHADOW_BTC_EMA_1H | 0 | 15 | 15 | 46,67% | 0,78 | -0,13R | €-19,79 |
| SHADOW_BTC_EMA_4H | 1 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 11 | 527 | 527 | 36,43% | 0,97 | -0,02R | €-94,12 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 290 | 290 | 35,86% | 0,97 | -0,02R | €-48,56 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 10 | 564 | 564 | 40,60% | 0,96 | -0,02R | €-91,03 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 11 | 468 | 468 | 39,10% | 0,92 | -0,04R | €-185,34 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 62 | 62 | 45,16% | 1,22 | 0,10R | €61,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 62 | 62 | 37,10% | 1,15 | 0,07R | €43,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 2 | 152 | 152 | 31,58% | 0,88 | -0,06R | €-93,53 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 189 | 189 | 34,92% | 0,86 | -0,07R | €-129,79 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 88 | 88 | 50,00% | 1,23 | 0,10R | €89,89 |
| SHADOW_COMBO_SCANNER | 8 | 329 | 329 | 35,26% | 1,08 | 0,04R | €138,69 |
| SHADOW_COMBO_TREND | 13 | 437 | 437 | 31,12% | 0,90 | -0,06R | €-241,52 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 8 | 8 | 62,50% | 1,44 | 0,18R | €14,73 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 12 | 12 | 33,33% | 0,51 | -0,36R | €-43,62 |
| SHADOW_DOGE_EMA_1H | 0 | 18 | 18 | 27,78% | 0,40 | -0,41R | €-73,66 |
| SHADOW_DONCHIAN_1H | 3 | 208 | 208 | 29,33% | 0,83 | -0,11R | €-227,86 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 3 | 138 | 138 | 31,16% | 0,80 | -0,12R | €-162,78 |
| SHADOW_EMA_TREND_1H | 14 | 440 | 440 | 30,68% | 0,87 | -0,07R | €-312,27 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 14 | 14 | 28,57% | 0,30 | -0,56R | €-77,90 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 13 | 13 | 23,08% | 0,28 | -0,63R | €-81,36 |
| SHADOW_ETH_EMA_1H | 1 | 20 | 20 | 30,00% | 0,29 | -0,55R | €-110,17 |
| SHADOW_ETH_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-31,95 |
| SHADOW_GLOBAL_PURE | 1 | 12 | 12 | 41,67% | 0,89 | -0,07R | €-8,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 8 | 262 | 262 | 32,82% | 1,01 | 0,01R | €19,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 3 | 487 | 487 | 66,53% | 1,40 | 0,13R | €622,32 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 8 | 230 | 230 | 33,04% | 1,03 | 0,02R | €42,05 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 7 | 239 | 239 | 30,96% | 0,99 | -0,01R | €-19,70 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 166 | 166 | 33,13% | 1,02 | 0,01R | €23,24 |
| SHADOW_MASTER_ADAPTIVE_V1 | 8 | 252 | 252 | 32,14% | 0,98 | -0,01R | €-35,45 |
| Forza relativa 1H V1 | 15 | 552 | 552 | 29,17% | 0,86 | -0,08R | €-446,93 |
| Forza relativa 1H V2 | 7 | 235 | 220 | 35,32% | 1,14 | 0,07R | €170,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 7 | 195 | 195 | 26,15% | 0,49 | -0,29R | €-564,94 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 7 | 195 | 195 | 26,15% | 0,49 | -0,29R | €-564,94 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 7 | 195 | 195 | 26,15% | 0,49 | -0,29R | €-564,94 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 228 | 228 | 28,95% | 0,68 | -0,18R | €-402,44 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 7 | 230 | 230 | 51,74% | 0,74 | -0,12R | €-269,47 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 7 | 208 | 208 | 50,96% | 0,65 | -0,16R | €-333,48 |
| SHADOW_SCANNER_TOP10_LONG | 7 | 269 | 269 | 34,57% | 0,98 | -0,01R | €-21,26 |
| SHADOW_SCANNER_TOP15_LONG | 7 | 270 | 270 | 34,44% | 0,98 | -0,01R | €-32,37 |
| SHADOW_SCANNER_TOP20_LONG | 7 | 270 | 270 | 34,44% | 0,98 | -0,01R | €-32,37 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 317 | 317 | 34,70% | 1,10 | 0,05R | €159,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 0 | 125 | 125 | 31,20% | 0,87 | -0,07R | €-91,35 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 7 | 270 | 270 | 32,96% | 0,94 | -0,03R | €-82,82 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 6 | 284 | 284 | 45,42% | 1,16 | 0,07R | €195,07 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 6 | 238 | 238 | 34,45% | 1,03 | 0,01R | €31,31 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 6 | 295 | 295 | 45,08% | 1,17 | 0,07R | €206,37 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 6 | 246 | 246 | 34,15% | 1,03 | 0,02R | €42,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 335 | 335 | 43,58% | 1,07 | 0,03R | €97,21 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 266 | 266 | 32,33% | 0,99 | -0,01R | €-16,24 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 253 | 253 | 31,62% | 0,98 | -0,01R | €-20,53 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 347 | 347 | 36,02% | 1,10 | 0,05R | €168,18 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 21 | 21 | 23,81% | 0,36 | -0,54R | €-113,90 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 3 | 3 | 33,33% | 0,58 | -0,30R | €-8,87 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 12 | 12 | 50,00% | 0,81 | -0,11R | €-12,76 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 15 | 15 | 33,33% | 0,55 | -0,34R | €-50,34 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 3 | 3 | 33,33% | 0,63 | -0,26R | €-7,86 |
| SHADOW_SOL_EMA_1H | 0 | 19 | 19 | 26,32% | 0,51 | -0,40R | €-76,60 |
| SHADOW_SOL_EMA_4H | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,50 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 2 | 36 | 36 | 22,22% | 0,48 | -0,32R | €-116,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 54 | 54 | 40,74% | 1,26 | 0,12R | €66,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 110 | 110 | 33,64% | 0,63 | -0,19R | €-212,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 4 | 12 | 12 | 33,33% | 0,47 | -0,28R | €-33,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 2 | 53 | 53 | 32,08% | 0,97 | -0,01R | €-6,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 1 | 58 | 58 | 27,59% | 0,56 | -0,26R | €-152,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 52 | 52 | 17,31% | 0,47 | -0,26R | €-137,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 2 | 35 | 35 | 20,00% | 0,30 | -0,49R | €-170,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 41 | 41 | 41,46% | 1,39 | 0,17R | €69,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 1 | 103 | 103 | 33,01% | 0,52 | -0,25R | €-259,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 4 | 11 | 11 | 27,27% | 0,29 | -0,41R | €-45,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 2 | 52 | 52 | 32,69% | 1,07 | 0,03R | €15,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 1 | 54 | 54 | 25,93% | 0,52 | -0,28R | €-150,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 49 | 49 | 16,33% | 0,31 | -0,36R | €-177,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,78 | -0,12R | €-7,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 45 | 45 | 53,33% | 1,22 | 0,10R | €46,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 64 | 64 | 39,06% | 0,48 | -0,33R | €-208,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 2 | 31 | 31 | 54,84% | 1,03 | 0,01R | €4,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 38 | 38 | 42,11% | 0,84 | -0,08R | €-29,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 1,08 | 0,04R | €1,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 47 | 47 | 40,43% | 1,17 | 0,08R | €39,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-207,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 2 | 31 | 31 | 29,03% | 0,88 | -0,05R | €-15,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 37 | 37 | 24,32% | 0,82 | -0,07R | €-27,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 0,99 | -0,00R | €-1,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 79 | 79 | 34,18% | 0,62 | -0,21R | €-166,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 2 | 11 | 11 | 18,18% | 0,24 | -0,53R | €-58,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 2 | 42 | 42 | 33,33% | 1,17 | 0,07R | €29,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,18 | -0,48R | €-43,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 44 | 44 | 36,36% | 1,02 | 0,01R | €4,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 0 | 69 | 69 | 36,23% | 0,56 | -0,23R | €-160,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 2 | 10 | 10 | 20,00% | 0,14 | -0,57R | €-57,27 |
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
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,14 | -0,67R | €-161,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 62 | 62 | 35,48% | 1,02 | 0,01R | €5,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 1 | 135 | 135 | 33,33% | 0,65 | -0,19R | €-256,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 2 | 50 | 50 | 26,00% | 0,80 | -0,09R | €-43,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 1 | 77 | 77 | 28,57% | 0,62 | -0,20R | €-155,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 71 | 71 | 23,94% | 0,65 | -0,17R | €-119,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,09 | -0,71R | €-171,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,05 | 0,02R | €12,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 1 | 126 | 126 | 32,54% | 0,57 | -0,22R | €-281,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 2 | 49 | 49 | 26,53% | 0,78 | -0,09R | €-45,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 1 | 71 | 71 | 26,76% | 0,57 | -0,23R | €-163,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 66 | 66 | 22,73% | 0,47 | -0,27R | €-176,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 53 | 53 | 37,74% | 1,07 | 0,03R | €18,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 79 | 79 | 36,71% | 0,75 | -0,14R | €-107,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 2 | 11 | 11 | 18,18% | 0,24 | -0,53R | €-58,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 2 | 42 | 42 | 33,33% | 1,17 | 0,07R | €29,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 40 | 40 | 32,50% | 0,79 | -0,12R | €-46,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 55 | 55 | 29,09% | 0,80 | -0,09R | €-50,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 53 | 53 | 32,08% | 0,42 | -0,35R | €-184,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 67 | 67 | 46,27% | 1,03 | 0,01R | €9,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 149 | 149 | 37,58% | 0,79 | -0,10R | €-145,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 4 | 24 | 24 | 37,50% | 0,52 | -0,28R | €-66,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 2 | 66 | 66 | 46,97% | 1,41 | 0,13R | €85,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 1 | 89 | 89 | 38,20% | 0,76 | -0,11R | €-94,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 81 | 81 | 40,74% | 0,84 | -0,07R | €-56,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 16 | 16 | 25,00% | 0,62 | -0,29R | €-47,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 48 | 48 | 37,50% | 0,47 | -0,32R | €-151,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 1 | 4 | 4 | 50,00% | 0,92 | -0,05R | €-1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 13 | 13 | 30,77% | 0,47 | -0,28R | €-35,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 2 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 0 | 61 | 61 | 34,43% | 0,98 | -0,01R | €-5,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 1 | 131 | 131 | 32,82% | 0,63 | -0,20R | €-261,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 4 | 24 | 24 | 29,17% | 0,45 | -0,32R | €-76,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 2 | 60 | 60 | 33,33% | 1,24 | 0,10R | €57,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 1 | 77 | 77 | 28,57% | 0,62 | -0,20R | €-155,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 2 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 0 | 63 | 63 | 34,92% | 1,01 | 0,01R | €4,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 1 | 132 | 132 | 32,58% | 0,62 | -0,21R | €-271,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 4 | 24 | 24 | 29,17% | 0,45 | -0,32R | €-76,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 2 | 60 | 60 | 33,33% | 1,24 | 0,10R | €57,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 1 | 77 | 77 | 28,57% | 0,62 | -0,20R | €-155,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 70 | 70 | 22,86% | 0,60 | -0,20R | €-139,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 48 | 48 | 16,67% | 0,26 | -0,48R | €-230,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 51 | 51 | 35,29% | 1,04 | 0,02R | €11,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 1 | 124 | 124 | 31,45% | 0,50 | -0,27R | €-332,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 4 | 20 | 20 | 25,00% | 0,40 | -0,35R | €-70,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 2 | 59 | 59 | 33,90% | 1,31 | 0,12R | €72,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 1 | 71 | 71 | 26,76% | 0,57 | -0,23R | €-163,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 65 | 65 | 21,54% | 0,39 | -0,31R | €-201,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,89 | -0,05R | €-10,79 |
| MAIN | ALT_ROTATION_UP | 3 | 39 | 39 | 17,95% | 0,31 | -0,51R | €-196,95 |
| MAIN | RANGE | 1 | 73 | 73 | 21,92% | 0,64 | -0,23R | €-165,36 |
| MAIN | RANGE_HIGH_VOL | 4 | 15 | 15 | 20,00% | 0,61 | -0,19R | €-28,06 |
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
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 57 | 57 | 21,05% | 0,43 | -0,41R | €-231,30 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 2 | 84 | 84 | 34,52% | 0,92 | -0,05R | €-39,28 |
| Bilanciata 1H V1 | RANGE | 1 | 169 | 169 | 39,05% | 1,07 | 0,03R | €56,92 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 4 | 35 | 35 | 22,86% | 0,41 | -0,39R | €-138,15 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 3 | 93 | 93 | 38,71% | 1,25 | 0,12R | €113,98 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 85 | 85 | 30,59% | 0,70 | -0,16R | €-135,86 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 0 | 109 | 109 | 30,28% | 0,92 | -0,04R | €-40,50 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 61 | 52 | 36,07% | 1,04 | 0,02R | €13,48 |
| Bilanciata 1H V2 | RANGE | 1 | 122 | 110 | 35,25% | 0,84 | -0,09R | €-113,72 |
| Bilanciata 1H V2 | TRANSITION | 3 | 78 | 66 | 39,74% | 1,38 | 0,19R | €146,14 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 42 | 42 | 26,19% | 0,54 | -0,30R | €-128,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 1 | 46 | 46 | 30,43% | 1,04 | 0,02R | €10,61 |
| Bilanciata 1H V3 Filtered | RANGE | 1 | 116 | 116 | 40,52% | 1,08 | 0,04R | €43,95 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 14 | 14 | 21,43% | 0,48 | -0,35R | €-49,56 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 3 | 51 | 51 | 35,29% | 1,10 | 0,05R | €24,61 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 2 | 59 | 59 | 35,59% | 0,66 | -0,19R | €-114,01 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 62 | 62 | 30,65% | 1,06 | 0,03R | €18,24 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 3 | 31 | 31 | 19,35% | 0,26 | -0,52R | €-161,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 44 | 44 | 31,82% | 1,13 | 0,07R | €31,60 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 1 | 94 | 94 | 38,30% | 0,85 | -0,08R | €-72,21 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 12 | 12 | 25,00% | 0,61 | -0,24R | €-28,73 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 3 | 43 | 43 | 34,88% | 1,10 | 0,04R | €18,93 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 2 | 60 | 60 | 35,00% | 0,64 | -0,21R | €-125,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 41 | 41 | 24,39% | 0,78 | -0,10R | €-42,60 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,25 | -0,50R | €-54,74 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 48,84% | 1,27 | 0,11R | €46,79 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 42 | 42 | 38,10% | 0,93 | -0,04R | €-16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 30,61% | 0,80 | -0,08R | €-38,10 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 15,79% | 0,25 | -0,52R | €-99,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 64 | 64 | 45,31% | 1,11 | 0,05R | €33,16 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 143 | 143 | 34,97% | 0,78 | -0,12R | €-166,44 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 2 | 56 | 56 | 39,29% | 1,07 | 0,03R | €14,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 79 | 79 | 29,11% | 0,60 | -0,24R | €-189,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 73 | 73 | 27,40% | 0,74 | -0,12R | €-84,75 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 18,92% | 0,33 | -0,49R | €-181,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 65 | 65 | 46,15% | 1,16 | 0,07R | €47,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 1 | 173 | 173 | 39,31% | 0,98 | -0,01R | €-21,26 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 2 | 58 | 58 | 41,38% | 1,20 | 0,08R | €44,55 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 79 | 79 | 29,11% | 0,60 | -0,24R | €-189,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 89 | 89 | 26,97% | 0,65 | -0,18R | €-156,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 77 | 77 | 20,78% | 0,38 | -0,43R | €-330,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 37,84% | 0,85 | -0,08R | €-62,01 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 195 | 195 | 36,92% | 0,82 | -0,09R | €-184,68 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 3 | 28 | 28 | 42,86% | 0,96 | -0,02R | €-4,89 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 2 | 81 | 81 | 40,74% | 1,24 | 0,10R | €77,75 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 100 | 100 | 29,00% | 0,59 | -0,23R | €-229,73 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 104 | 104 | 27,88% | 0,70 | -0,15R | €-160,49 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 2 | 44 | 44 | 22,73% | 0,37 | -0,46R | €-202,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 52 | 52 | 36,54% | 0,89 | -0,06R | €-29,98 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 113 | 113 | 42,48% | 1,11 | 0,05R | €59,96 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 3 | 11 | 11 | 54,55% | 1,16 | 0,08R | €8,28 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 52 | 52 | 40,38% | 1,25 | 0,10R | €50,06 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 1 | 58 | 58 | 27,59% | 0,55 | -0,25R | €-145,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 59 | 59 | 27,12% | 0,60 | -0,22R | €-127,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 2 | 75 | 75 | 20,00% | 0,42 | -0,40R | €-298,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 76 | 76 | 39,47% | 1,03 | 0,02R | €13,46 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 1 | 179 | 179 | 34,64% | 0,77 | -0,12R | €-219,83 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 4 | 27 | 27 | 29,63% | 0,54 | -0,25R | €-68,44 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 76 | 76 | 38,16% | 1,39 | 0,15R | €117,72 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 93 | 93 | 27,96% | 0,59 | -0,24R | €-222,70 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 95 | 95 | 21,05% | 0,53 | -0,25R | €-237,49 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 10 | 9 | 20,00% | 0,18 | -0,73R | €-72,55 |
| Rapida 1H V2 | RANGE | 0 | 40 | 33 | 37,50% | 0,73 | -0,14R | €-57,99 |
| Rapida 1H V2 | TRANSITION | 0 | 7 | 7 | 57,14% | 0,81 | -0,07R | €-4,61 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 74 | 74 | 20,27% | 0,37 | -0,43R | €-315,89 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 70 | 70 | 38,57% | 0,94 | -0,03R | €-23,47 |
| Rapida 1H V3 Filtered | RANGE | 1 | 174 | 174 | 37,36% | 0,82 | -0,09R | €-164,09 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 4 | 25 | 25 | 44,00% | 0,95 | -0,03R | €-6,63 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 2 | 74 | 74 | 37,84% | 1,08 | 0,04R | €26,23 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 88 | 88 | 28,41% | 0,60 | -0,22R | €-190,39 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 108 | 108 | 37,04% | 1,00 | 0,00R | €0,97 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-232,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 61 | 61 | 40,98% | 1,03 | 0,01R | €8,26 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 141 | 141 | 38,30% | 0,90 | -0,05R | €-68,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 4 | 14 | 14 | 50,00% | 1,16 | 0,07R | €9,96 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 2 | 56 | 56 | 37,50% | 0,98 | -0,01R | €-5,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 64 | 64 | 28,12% | 0,61 | -0,22R | €-143,04 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 69 | 69 | 28,99% | 0,67 | -0,17R | €-116,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 23,08% | 0,19 | -0,65R | €-84,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 50 | 50 | 54,00% | 1,10 | 0,04R | €22,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 79 | 79 | 43,04% | 0,86 | -0,08R | €-63,69 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 2 | 32 | 32 | 56,25% | 1,29 | 0,11R | €36,12 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 48 | 48 | 50,00% | 0,97 | -0,02R | €-7,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 16,67% | 0,19 | -0,63R | €-75,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 0,98 | -0,01R | €-4,85 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 81 | 81 | 39,51% | 0,94 | -0,03R | €-27,15 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 2 | 32 | 32 | 37,50% | 1,09 | 0,03R | €10,98 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 49 | 49 | 32,65% | 0,88 | -0,05R | €-25,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 5,56% | 0,10 | -0,73R | €-131,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 61 | 61 | 37,70% | 0,87 | -0,07R | €-40,41 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 98 | 98 | 40,82% | 0,93 | -0,04R | €-34,70 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 11 | 11 | 36,36% | 0,65 | -0,21R | €-23,15 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 2 | 47 | 47 | 40,43% | 1,17 | 0,07R | €32,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 47 | 47 | 34,04% | 0,76 | -0,14R | €-63,60 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 68 | 68 | 33,82% | 0,87 | -0,06R | €-44,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 17,39% | 0,32 | -0,51R | €-234,33 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 66 | 66 | 37,88% | 0,89 | -0,06R | €-40,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 1 | 176 | 176 | 38,64% | 0,87 | -0,07R | €-116,04 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 2 | 58 | 58 | 32,76% | 0,91 | -0,04R | €-22,74 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 1 | 88 | 88 | 28,41% | 0,60 | -0,22R | €-190,39 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 94 | 94 | 31,91% | 0,79 | -0,11R | €-104,22 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 73 | 73 | 20,55% | 0,38 | -0,42R | €-304,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 69 | 69 | 36,23% | 0,83 | -0,09R | €-64,59 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 172 | 172 | 37,21% | 0,80 | -0,10R | €-178,82 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 4 | 24 | 24 | 45,83% | 1,03 | 0,01R | €3,50 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 2 | 69 | 69 | 37,68% | 1,10 | 0,04R | €28,99 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 88 | 88 | 28,41% | 0,60 | -0,22R | €-190,39 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 91 | 91 | 30,77% | 0,75 | -0,13R | €-121,78 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 1,25 | 0,12R | €18,44 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 4 | 34 | 34 | 23,53% | 0,48 | -0,41R | €-138,96 |
| SHADOW_4H_WIDE | RANGE | 6 | 65 | 65 | 15,38% | 0,60 | -0,28R | €-183,37 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 3 | 13 | 13 | 15,38% | 0,68 | -0,20R | €-26,05 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 36 | 36 | 13,89% | 0,39 | -0,45R | €-163,12 |
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
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 6 | 6 | 50,00% | 0,52 | -0,26R | €-15,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
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
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 5 | 5 | 60,00% | 1,54 | 0,24R | €11,96 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,73R | €7,31 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 2 | 47 | 47 | 25,53% | 0,60 | -0,25R | €-119,80 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 61 | 61 | 34,43% | 0,92 | -0,05R | €-28,90 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 140 | 140 | 41,43% | 0,97 | -0,01R | €-20,28 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 2 | 24 | 24 | 33,33% | 0,83 | -0,08R | €-19,86 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 71 | 71 | 42,25% | 1,47 | 0,21R | €151,63 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 4 | 71 | 71 | 35,21% | 0,91 | -0,05R | €-32,20 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 94 | 94 | 36,17% | 1,12 | 0,05R | €48,17 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 14 | 14 | 14,29% | 0,43 | -0,38R | €-52,64 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 55 | 55 | 34,55% | 0,93 | -0,04R | €-21,89 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 68 | 68 | 47,06% | 1,21 | 0,10R | €70,10 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,52 | -0,26R | €-20,89 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 2 | 38 | 38 | 47,37% | 2,09 | 0,35R | €134,72 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 2 | 42 | 42 | 35,71% | 1,10 | 0,05R | €19,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,60 | -0,19R | €-101,81 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 1 | 57 | 57 | 29,82% | 0,56 | -0,26R | €-145,38 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 69 | 69 | 37,68% | 0,88 | -0,06R | €-41,75 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 0 | 138 | 138 | 41,30% | 1,11 | 0,05R | €67,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 4 | 27 | 27 | 44,44% | 0,76 | -0,09R | €-25,24 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 2 | 61 | 61 | 47,54% | 1,25 | 0,11R | €65,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 3 | 95 | 95 | 37,89% | 0,91 | -0,04R | €-34,85 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 96 | 96 | 50,00% | 1,33 | 0,13R | €127,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 2 | 47 | 47 | 25,53% | 0,62 | -0,24R | €-112,45 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 1 | 59 | 59 | 35,59% | 0,94 | -0,03R | €-18,76 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 0 | 128 | 128 | 44,53% | 1,04 | 0,02R | €26,19 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 2 | 22 | 22 | 40,91% | 1,08 | 0,04R | €7,96 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 54 | 54 | 46,30% | 1,36 | 0,16R | €87,25 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 4 | 71 | 71 | 39,44% | 0,91 | -0,04R | €-31,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 73 | 73 | 36,99% | 0,73 | -0,12R | €-87,95 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 2 | 32 | 32 | 34,38% | 0,86 | -0,08R | €-25,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 2 | 32 | 32 | 34,38% | 0,88 | -0,07R | €-23,11 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 18 | 18 | 27,78% | 0,63 | -0,21R | €-38,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 38 | 38 | 39,47% | 1,17 | 0,09R | €34,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 25,00% | 0,64 | -0,19R | €-14,85 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 2 | 26 | 26 | 34,62% | 0,99 | -0,01R | €-1,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 5 | 77 | 77 | 38,96% | 1,08 | 0,04R | €32,25 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 99 | 99 | 34,34% | 0,80 | -0,09R | €-93,73 |
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
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,84R | €-33,76 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 5 | 5 | 80,00% | 4,65 | 0,83R | €41,31 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 2 | 16 | 16 | 6,25% | 0,19 | -0,58R | €-92,77 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 1 | 53 | 53 | 35,85% | 1,05 | 0,03R | €15,18 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 77 | 77 | 44,16% | 1,40 | 0,19R | €150,15 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 9 | 9 | 33,33% | 0,34 | -0,32R | €-28,51 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 3 | 54 | 54 | 44,44% | 1,75 | 0,35R | €187,26 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 43 | 43 | 30,23% | 0,73 | -0,15R | €-65,86 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 63 | 63 | 30,16% | 1,02 | 0,01R | €5,81 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 2 | 36 | 36 | 25,00% | 0,62 | -0,23R | €-83,86 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 55 | 55 | 29,09% | 0,71 | -0,20R | €-107,45 |
| SHADOW_COMBO_TREND | RANGE | 3 | 117 | 117 | 34,19% | 0,98 | -0,01R | €-12,21 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 17 | 17 | 29,41% | 0,79 | -0,09R | €-15,94 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 60 | 60 | 36,67% | 1,36 | 0,19R | €114,33 |
| SHADOW_COMBO_TREND | TREND_DOWN | 5 | 62 | 62 | 30,65% | 0,73 | -0,14R | €-89,10 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 72 | 72 | 29,17% | 1,03 | 0,01R | €9,60 |
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
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 27 | 27 | 22,22% | 0,51 | -0,37R | €-98,95 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 22 | 22 | 18,18% | 0,23 | -0,63R | €-139,43 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 57 | 57 | 31,58% | 0,94 | -0,04R | €-20,96 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 10 | 10 | 40,00% | 1,28 | 0,14R | €14,45 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 0 | 24 | 24 | 41,67% | 1,71 | 0,34R | €82,19 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 2 | 20 | 20 | 25,00% | 0,29 | -0,51R | €-102,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 40 | 40 | 27,50% | 1,09 | 0,05R | €18,29 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,23 | -0,63R | €-107,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 21,43% | 0,16 | -0,64R | €-89,01 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 1 | 37 | 37 | 32,43% | 0,84 | -0,10R | €-36,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 50,00% | 2,11 | 0,43R | €34,72 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 0 | 17 | 17 | 52,94% | 2,80 | 0,66R | €111,46 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 2 | 18 | 18 | 27,78% | 0,32 | -0,51R | €-92,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 26 | 26 | 23,08% | 0,92 | -0,03R | €-8,69 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 2 | 38 | 38 | 23,68% | 0,55 | -0,29R | €-110,59 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 51 | 51 | 27,45% | 0,68 | -0,22R | €-112,36 |
| SHADOW_EMA_TREND_1H | RANGE | 3 | 116 | 116 | 34,48% | 1,04 | 0,02R | €22,87 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 2 | 19 | 19 | 36,84% | 1,16 | 0,06R | €11,74 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 58 | 58 | 36,21% | 1,25 | 0,14R | €78,65 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 4 | 65 | 65 | 30,77% | 0,70 | -0,17R | €-107,60 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 75 | 75 | 28,00% | 0,95 | -0,03R | €-21,00 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,69 | -0,22R | €-35,19 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 32,35% | 0,94 | -0,04R | €-13,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 2 | 76 | 76 | 31,58% | 1,00 | 0,00R | €1,84 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 4 | 30 | 30 | 46,67% | 1,78 | 0,40R | €120,27 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 2 | 46 | 46 | 34,78% | 1,09 | 0,06R | €25,70 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 44,44% | 0,85 | -0,08R | €-14,12 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 74 | 74 | 74,32% | 2,04 | 0,26R | €195,11 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 139 | 139 | 65,47% | 1,38 | 0,12R | €169,39 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 72 | 72 | 75,00% | 1,91 | 0,22R | €160,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 2 | 75 | 75 | 65,33% | 1,35 | 0,12R | €90,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 108 | 108 | 62,04% | 1,08 | 0,03R | €31,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,63 | -0,24R | €-34,08 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 2 | 77 | 77 | 33,77% | 1,11 | 0,07R | €50,58 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 4 | 29 | 29 | 37,93% | 1,23 | 0,14R | €40,36 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 2 | 42 | 42 | 38,10% | 1,23 | 0,14R | €58,57 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 1,36 | 0,21R | €18,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 27,03% | 0,74 | -0,20R | €-72,56 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 69 | 69 | 30,43% | 1,10 | 0,06R | €44,62 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 3 | 27 | 27 | 40,74% | 1,41 | 0,24R | €64,16 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 2 | 39 | 39 | 38,46% | 1,25 | 0,16R | €60,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -0,90R | €-71,98 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 58 | 58 | 36,21% | 1,14 | 0,09R | €51,45 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 4 | 22 | 22 | 50,00% | 2,31 | 0,56R | €122,58 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 31 | 31 | 25,81% | 0,70 | -0,22R | €-66,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,57 | -0,31R | €-43,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 0,98 | -0,02R | €-6,05 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 2 | 72 | 72 | 33,33% | 1,11 | 0,06R | €45,30 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 4 | 29 | 29 | 41,38% | 1,42 | 0,24R | €70,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 2 | 40 | 40 | 37,50% | 1,20 | 0,12R | €48,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 2 | 47 | 47 | 19,15% | 0,43 | -0,38R | €-179,11 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 68 | 68 | 32,35% | 0,85 | -0,09R | €-63,94 |
| Forza relativa 1H V1 | RANGE | 5 | 159 | 159 | 30,82% | 0,85 | -0,08R | €-134,84 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 22 | 22 | 22,73% | 0,30 | -0,37R | €-81,65 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 2 | 71 | 71 | 38,03% | 1,46 | 0,23R | €161,78 |
| Forza relativa 1H V1 | TREND_DOWN | 3 | 72 | 72 | 29,17% | 0,87 | -0,07R | €-50,78 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 0 | 95 | 95 | 25,26% | 0,91 | -0,05R | €-45,58 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 25,00% | 0,64 | -0,21R | €-41,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 29 | 26 | 34,48% | 1,17 | 0,09R | €26,73 |
| Forza relativa 1H V2 | RANGE | 3 | 68 | 66 | 36,76% | 0,98 | -0,01R | €-7,82 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 2 | 39 | 34 | 41,03% | 1,80 | 0,36R | €140,16 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 34 | 33 | 29,41% | 0,95 | -0,02R | €-7,23 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 0 | 36 | 33 | 44,44% | 1,70 | 0,32R | €116,09 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 2 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 2 | 14 | 14 | 35,71% | 1,12 | 0,05R | €7,34 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 2 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 2 | 14 | 14 | 35,71% | 1,12 | 0,05R | €7,34 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 2 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,75 | -0,13R | €-15,53 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 1 | 58 | 58 | 24,14% | 0,35 | -0,37R | €-215,50 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 2 | 14 | 14 | 35,71% | 1,12 | 0,05R | €7,34 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 1 | 19 | 19 | 47,37% | 1,38 | 0,19R | €36,43 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 44 | 44 | 27,27% | 0,37 | -0,38R | €-166,63 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 16 | 16 | 6,25% | 0,29 | -0,29R | €-46,02 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 1,07 | 0,03R | €4,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 71 | 71 | 29,58% | 0,65 | -0,19R | €-135,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 2 | 15 | 15 | 40,00% | 1,24 | 0,10R | €14,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 1 | 35 | 35 | 40,00% | 1,09 | 0,05R | €17,72 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 40 | 40 | 27,50% | 0,38 | -0,36R | €-144,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 23 | 23 | 4,35% | 0,16 | -0,42R | €-97,06 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 27 | 27 | 29,63% | 0,29 | -0,48R | €-128,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 33,33% | 0,57 | -0,25R | €-22,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 1 | 63 | 63 | 55,56% | 0,69 | -0,13R | €-84,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 3 | 18 | 18 | 66,67% | 1,53 | 0,18R | €32,49 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 27 | 27 | 59,26% | 1,51 | 0,22R | €58,91 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 64 | 64 | 54,69% | 0,65 | -0,15R | €-95,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 19 | 19 | 42,11% | 0,65 | -0,16R | €-29,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 24 | 24 | 29,17% | 0,22 | -0,52R | €-124,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 11 | 11 | 36,36% | 0,79 | -0,10R | €-11,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 1 | 56 | 56 | 55,36% | 0,42 | -0,25R | €-138,62 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 3 | 16 | 16 | 62,50% | 1,35 | 0,13R | €20,99 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 26 | 26 | 61,54% | 1,57 | 0,23R | €59,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 54 | 54 | 53,70% | 0,65 | -0,15R | €-81,86 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 18 | 18 | 38,89% | 0,34 | -0,31R | €-55,83 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 10 | 10 | 20,00% | 0,64 | -0,22R | €-22,09 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 2 | 52 | 52 | 30,77% | 0,80 | -0,11R | €-58,98 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,50 | -0,27R | €-21,44 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 10 | 10 | 20,00% | 0,64 | -0,22R | €-22,09 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 2 | 53 | 53 | 30,19% | 0,77 | -0,13R | €-70,09 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,50 | -0,27R | €-21,44 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 10 | 10 | 20,00% | 0,64 | -0,22R | €-22,09 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 2 | 53 | 53 | 30,19% | 0,77 | -0,13R | €-70,09 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 60 | 60 | 50,00% | 1,54 | 0,23R | €135,14 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,50 | -0,27R | €-21,44 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 2 | 42 | 42 | 40,48% | 1,62 | 0,23R | €96,64 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 44 | 44 | 29,55% | 0,95 | -0,03R | €-12,83 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 48 | 48 | 27,08% | 0,58 | -0,20R | €-95,25 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 15 | 15 | 6,67% | 0,21 | -0,55R | €-81,76 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 53 | 53 | 35,85% | 1,05 | 0,03R | €15,77 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 72 | 72 | 44,44% | 1,55 | 0,25R | €183,13 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 9 | 9 | 33,33% | 0,34 | -0,32R | €-28,51 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 3 | 50 | 50 | 44,00% | 1,81 | 0,37R | €184,83 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 62 | 62 | 29,03% | 0,95 | -0,02R | €-14,90 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,64R | €-31,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 47 | 47 | 27,66% | 0,81 | -0,10R | €-47,19 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 0,00% | 0,00 | -0,79R | €-102,94 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 50 | 50 | 36,00% | 0,98 | -0,01R | €-5,10 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 67 | 67 | 43,28% | 1,40 | 0,19R | €129,90 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 37,50% | 0,45 | -0,22R | €-17,82 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 3 | 38 | 38 | 47,37% | 2,26 | 0,48R | €180,65 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 42 | 42 | 28,57% | 0,73 | -0,16R | €-66,28 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 19,51% | 0,46 | -0,31R | €-126,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,03 | -0,54R | €-70,10 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 3 | 9 | 9 | 44,44% | 0,85 | -0,04R | €-3,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 2 | 40 | 40 | 50,00% | 1,40 | 0,16R | €62,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 12 | 12 | 0,00% | 0,00 | -0,77R | €-92,81 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 71 | 71 | 46,48% | 1,52 | 0,23R | €166,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 37,50% | 0,45 | -0,22R | €-17,82 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 3 | 35 | 35 | 40,00% | 1,71 | 0,29R | €102,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 23,53% | 0,48 | -0,28R | €-48,31 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 41 | 41 | 46,34% | 1,28 | 0,12R | €50,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 81 | 81 | 45,68% | 1,44 | 0,17R | €138,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 3 | 9 | 9 | 44,44% | 0,85 | -0,04R | €-3,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 2 | 42 | 42 | 47,62% | 1,32 | 0,13R | €52,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 1 | 50 | 50 | 48,00% | 0,98 | -0,01R | €-5,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 50 | 50 | 48,00% | 1,25 | 0,11R | €52,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 14 | 14 | 7,14% | 0,23 | -0,51R | €-71,62 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 38,24% | 1,31 | 0,16R | €55,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 71 | 71 | 46,48% | 1,52 | 0,23R | €166,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 1 | 8 | 8 | 37,50% | 0,45 | -0,22R | €-17,82 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 3 | 36 | 36 | 38,89% | 1,59 | 0,26R | €91,94 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 1 | 39 | 39 | 30,77% | 0,76 | -0,15R | €-57,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 39 | 39 | 20,51% | 0,59 | -0,22R | €-84,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,43 | -0,32R | €-58,44 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 1 | 56 | 56 | 42,86% | 0,95 | -0,02R | €-12,78 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 74 | 74 | 45,95% | 1,40 | 0,16R | €119,34 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 2 | 10 | 10 | 40,00% | 0,81 | -0,05R | €-4,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 3 | 46 | 46 | 50,00% | 1,36 | 0,15R | €67,24 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 56 | 56 | 44,64% | 0,92 | -0,03R | €-18,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 61 | 61 | 47,54% | 1,26 | 0,10R | €61,08 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 8 | 8 | 12,50% | 0,41 | -0,38R | €-30,33 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 54 | 54 | 33,33% | 1,01 | 0,01R | €3,43 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 63 | 63 | 41,27% | 1,42 | 0,21R | €129,63 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 8 | 8 | 37,50% | 0,45 | -0,22R | €-17,82 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 3 | 38 | 38 | 44,74% | 1,99 | 0,40R | €153,15 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 41 | 41 | 29,27% | 0,77 | -0,13R | €-54,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 46 | 46 | 19,57% | 0,51 | -0,27R | €-125,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 8 | 8 | 0,00% | 0,00 | -0,65R | €-51,83 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 2 | 54 | 54 | 35,19% | 0,96 | -0,02R | €-11,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 59 | 59 | 40,68% | 1,44 | 0,22R | €131,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 33,33% | 0,33 | -0,32R | €-28,93 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 3 | 32 | 32 | 43,75% | 2,50 | 0,53R | €170,30 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 38 | 38 | 28,95% | 0,79 | -0,11R | €-43,01 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 45 | 45 | 20,00% | 0,54 | -0,25R | €-113,17 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 17 | 17 | 11,76% | 0,32 | -0,50R | €-85,00 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 2 | 54 | 54 | 33,33% | 0,90 | -0,06R | €-30,19 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 75 | 75 | 49,33% | 1,64 | 0,27R | €205,66 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 10 | 10 | 20,00% | 0,34 | -0,42R | €-42,27 |
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
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 7 | 7 | 28,57% | 0,68 | -0,25R | €-17,78 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-18T06:05:55+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **629**
- Scenari virtuali ancora attivi: **10060**
- Gruppi in attesa dell'uscita originale: **247**
- Gruppi con originale chiuso ma Shadow ancora attive: **382**
- Confronti completati: **244311**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 5748 | 5821 | +€0,07 | 47,7% | 1285 | 711 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 5742 | 5811 | +€8,12 | 51,8% | 1626 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5742 | 5811 | +€7,26 | 51,2% | 1609 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5742 | 5811 | +€5,97 | 49,6% | 1624 | 128 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5742 | 5811 | +€4,88 | 49,2% | 1783 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5742 | 5811 | +€4,60 | 49,7% | 1545 | 193 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5740 | 5813 | +€0,03 | 43,0% | 814 | 1046 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5725 | 5794 | +€7,27 | 45,0% | 1315 | 111 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5725 | 5794 | +€6,08 | 45,0% | 1250 | 177 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5725 | 5794 | +€5,41 | 43,1% | 1437 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5722 | 5791 | +€5,05 | 44,3% | 1134 | 305 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5721 | 5790 | +€2,18 | 38,4% | 740 | 930 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5721 | 5790 | +€1,40 | 36,0% | 600 | 1195 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5717 | 5786 | +€3,21 | 42,7% | 1015 | 529 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5710 | 5783 | €-4,26 | 35,0% | 507 | 1466 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5657 | 5726 | €-2,52 | 33,3% | 502 | 1376 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5644 | 5713 | +€4,77 | 34,9% | 876 | 507 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5621 | 5687 | +€4,87 | 38,8% | 472 | 795 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5613 | 5682 | €-3,25 | 36,4% | 1023 | 1048 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5497 | 5566 | €-7,00 | 28,3% | 466 | 1555 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-18T06:06:06+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **244311**
- Valutazioni prodotte: **19361**
- Candidature al Blocco 5: **47**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_TOP5BTC_GB20_R140 | 290 | 0,446 | 0,309 | 0,342 | 63,1% | 91,6 | VALIDATING |
| GB20_R040 | 4329 | 0,213 | 0,149 | 0,181 | 55,2% | 88,1 | ELIGIBLE_FOR_MUTATION |
| GB30_R040 | 4329 | 0,199 | 0,140 | 0,168 | 55,0% | 88,0 | ELIGIBLE_FOR_MUTATION |
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

Generato: 2026-08-18T06:08:42+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 70 | 100,00% | 0,92 | €-71,99 | €-1,03 | 2,46% | NOT_READY_FOR_PROMOTION |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 70 | 100,00% | 0,92 | €-67,27 | €-0,96 | 2,70% | NOT_READY_FOR_PROMOTION |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 36 | 97,30% | 0,88 | €-111,72 | €-3,10 | 2,95% | EARLY_NOT_CONFIRMED |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 27 | 90,00% | 0,00 | €-286,84 | €-10,62 | 2,87% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 71 | 100,00% | 1,05 | +€64,64 | +€0,91 | 2,13% | NOT_READY_FOR_PROMOTION |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-18T06:05:44+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **68**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **620.33 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 166 | 0 | 21211.89 |
| DOWN_20 | 166 | 0 | 42423.78 |
| DOWN_30 | 166 | 1 | 63672.71 |
| DOWN_40 | 166 | 49 | 81518.63 |
| UP_10 | 87 | 0 | 14343.49 |
| UP_20 | 87 | 0 | 28686.98 |
| UP_30 | 87 | 0 | 43030.47 |
| UP_40 | 87 | 34 | 53322.58 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-18T06:05:15+00:00

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

Generato: 2026-08-18T06:08:45+00:00

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

Generato: 2026-08-18T06:08:45+00:00

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

Generato: 2026-08-18T06:08:45+00:00

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

Generato: 2026-08-18T06:08:45+00:00

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
| 1 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 18.9 | E | 128 | 1.13 | 0.060 | 8.02 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 16.3 | E | 72 | 1.28 | 0.125 | 5.98 |
| 3 | SHADOW_1H_FAST_V3 | BASELINE | 15.0 | E | 150 | 0.87 | -0.064 | 20.48 |
| 4 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.6 | E | 125 | 0.98 | -0.008 | 16.32 |
| 5 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 14.2 | E | 48 | 1.28 | 0.136 | 5.48 |
| 6 | SHADOW_DONCHIAN_1H | BASELINE | 13.6 | E | 63 | 1.19 | 0.112 | 8.55 |
| 7 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 13.0 | E | 114 | 0.94 | -0.032 | 23.13 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 12.8 | E | 104 | 0.97 | -0.014 | 12.98 |
| 9 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 11.4 | E | 118 | 0.82 | -0.105 | 22.00 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 11.4 | E | 124 | 0.79 | -0.110 | 20.45 |

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

Generato: 2026-08-18T06:08:45+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **UNKNOWN**
- Righe di performance: **640**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **302**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | MAIN | main | INSUFFICIENT | 81.6 | 4 | 99.00 | 0.750 | 0.00 |
| 2 | EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | momentum_breakout_v3_filtered | INSUFFICIENT | 81.2 | 3 | 99.00 | 0.775 | 0.00 |
| 3 | SHADOW_MASTER_ADAPTIVE_GB20_V1 | shadow-master-adaptive-gb20-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.550 | 0.00 |
| 4 | SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | shadow-master-adaptive-gb20-be-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.986 | 0.00 |
| 5 | SHADOW_SOL_BOLLINGER_1H | shadow-sol-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.395 | 0.00 |
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

Generato: 2026-08-18T06:08:45+00:00

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

Generato: 2026-08-18T06:05:44+00:00

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
