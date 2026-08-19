# Paper trading automatico KuCoin

Generato: 2026-08-19T05:33:31+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-19T05:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-19T05:05:28+00:00 | 2026-08-19T05:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-19T04:45:00+00:00 | 2026-08-19T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-19T04:00:00+00:00 | 2026-08-19T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-19T00:00:00+00:00 | 2026-08-19T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ACE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOXL | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,99 | 6,00 | 1,01 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,95 | 6,00 | 1,05 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,92 | 6,00 | 1,08 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | SHORT | -4,90 | 6,00 | 1,10 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,21 | 6,00 | 2,79 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | GPS | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 1,29 | 6,00 | 4,71 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 0,40 | 6,00 | 5,60 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V3 Filtered | ACE | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced V3 Long Only V1 | ACE | 60m | LONG | 6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | SOXL | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced V3 Long Only V1 | SOXL | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | SKHYNIX | 60m | SHORT | -4,75 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | GPS | 60m | SHORT | -4,25 | 4,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Expanded V1 | SOL | 60m | LONG | 3,40 | 0,00 | 0,00 | READY | 5,6 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ACE | 60m | LONG | 6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.642,22 | -3,58% | €-106,12 | €3.000,00 | -3,54% | 6 | 42 | 33,33% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 42 | 1603 | PRIME INDICAZIONI | 100 (mancano 58) |

- Trade del Principale 4H chiusi: **42**; win rate **33,33%**; profit factor **0,72**.
- Expectancy: **€-9,04** per trade; P&L netto: **€-379,65**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.642,22 | €1.281,99 | €3.845,96 | €192,75 | €20,66 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.667,00 | €3.807,11 | €7.614,22 | €55,33 | €68,01 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.415,85 | €3.717,48 | €7.434,96 | €54,03 | €66,41 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.406,71 | €1.752,90 | €5.258,70 | €103,53 | €60,25 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 2 | €10.374,11 | €3.144,71 | €9.434,12 | €105,66 | €-55,58 |
| TEST | Main Side Regime Guard V1 | 6 | €10.344,52 | €1.934,28 | €5.802,85 | €207,05 | €10,49 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.332,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.258,15 | €4.336,32 | €13.008,97 | €205,10 | €-0,28 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 1 | €10.241,11 | €1.508,82 | €4.526,45 | €50,70 | €19,86 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.240,07 | €142,09 | €426,26 | €51,15 | €10,02 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 6 | €10.217,13 | €1.641,80 | €4.925,41 | €204,02 | €21,47 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.138,32 | €2.871,87 | €8.615,60 | €202,91 | €-26,02 |
| TEST | Combo Trend Side Regime Guard V1 | 2 | €10.124,89 | €3.135,06 | €6.270,11 | €100,32 | €-4,15 |
| TEST | Btc Bollinger 4H | 1 | €10.105,73 | €1.575,64 | €3.151,29 | €50,42 | €23,47 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.098,33 | €2.265,49 | €4.530,99 | €153,17 | €-36,28 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 1 | €10.087,56 | €1.170,75 | €3.512,25 | €50,58 | €-22,35 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.991,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €9.985,41 | €4.221,03 | €12.663,09 | €199,65 | €-0,28 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €9.966,86 | €1.633,87 | €3.267,74 | €199,26 | €15,88 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 6 | €9.962,88 | €1.600,95 | €4.802,84 | €198,95 | €20,93 |
| TEST | Btc Adaptive 1H | 1 | €9.962,61 | €1.156,05 | €3.468,16 | €49,94 | €-23,61 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.944,89 | €1.298,67 | €3.896,00 | €49,87 | €-26,52 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.927,72 | €1.295,52 | €2.591,05 | €49,75 | €-20,32 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.919,66 | €1.200,73 | €2.401,46 | €49,66 | €-9,90 |
| TEST | Sol Adaptive 4H | 1 | €9.917,99 | €1.100,38 | €2.200,75 | €49,64 | €-9,07 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €9.906,76 | €4.213,05 | €12.639,15 | €198,08 | €-1,46 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.886,68 | €4.158,00 | €8.316,00 | €148,97 | €-6,92 |
| TEST | Scanner Bottom15 Short | 5 | €9.886,68 | €4.158,00 | €8.316,00 | €148,97 | €-6,92 |
| TEST | Scanner Bottom20 Short | 5 | €9.886,68 | €4.158,00 | €8.316,00 | €148,97 | €-6,92 |
| TEST | Btc Ema 4H | 1 | €9.876,01 | €1.406,22 | €2.812,44 | €49,50 | €-22,06 |
| TEST | Sol Donchian 1H | 0 | €9.875,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €9.848,96 | €1.651,13 | €4.953,38 | €99,18 | €-18,92 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.838,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.823,24 | €1.139,88 | €3.419,65 | €49,24 | €-23,28 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 5 | €9.818,18 | €4.129,16 | €8.258,32 | €147,94 | €-6,87 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 0 | €9.815,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.813,27 | €3.594,66 | €7.189,31 | €147,40 | €9,44 |
| TEST | Btc Donchian 4H | 1 | €9.808,64 | €1.396,63 | €2.793,26 | €49,16 | €-21,91 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 5 | €9.803,24 | €4.122,88 | €8.245,76 | €147,72 | €-6,86 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.796,85 | €2.975,26 | €8.925,78 | €146,27 | €-14,66 |
| TEST | Sol Ema 4H | 1 | €9.781,35 | €1.183,99 | €2.367,98 | €48,96 | €-9,76 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 1 | €9.779,24 | €1.460,07 | €4.380,22 | €49,06 | €-29,82 |
| TEST | Eth Donchian 1H | 0 | €9.762,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €9.755,58 | €209,35 | €418,71 | €49,71 | €-12,97 |
| TEST | Sol Ema 1H | 1 | €9.751,75 | €1.129,69 | €3.389,07 | €48,80 | €-6,39 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 4 | €9.729,98 | €638,67 | €1.277,34 | €98,62 | €9,36 |
| TEST | Scanner Bottom 5 Short 1H | 5 | €9.727,80 | €4.091,15 | €8.182,31 | €146,58 | €-6,81 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 4 | €9.689,74 | €1.669,55 | €3.339,10 | €145,28 | €-12,00 |
| TEST | Global Confluence puro 1H | 1 | €9.684,38 | €1.512,09 | €3.024,18 | €48,39 | €4,57 |
| TEST | Combo Mean Reversion | 1 | €9.647,37 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.621,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 5 | €9.615,52 | €2.484,74 | €7.454,23 | €192,60 | €-54,89 |
| TEST | Combo Adaptive Quality7 Regime V1 | 4 | €9.607,59 | €630,64 | €1.261,28 | €97,38 | €9,24 |
| TEST | Forza relativa 1H V2 | 6 | €9.606,73 | €1.800,65 | €3.601,29 | €96,04 | €84,03 |
| TEST | Bilanciata 1H V2 | 5 | €9.591,00 | €867,39 | €2.602,16 | €145,64 | €31,16 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €9.590,34 | €1.242,77 | €3.728,32 | €189,39 | €-7,21 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.578,86 | €1.082,19 | €3.246,57 | €144,26 | €9,10 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.564,42 | €202,90 | €405,81 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.553,02 | €1.105,17 | €3.315,52 | €47,74 | €6,41 |
| TEST | Rapida 1H V3 Filtered | 6 | €9.527,67 | €1.234,65 | €3.703,96 | €188,15 | €-7,17 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.520,66 | €713,02 | €1.426,04 | €95,14 | €5,64 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.478,72 | €2.055,65 | €4.111,31 | €143,26 | €-17,46 |
| TEST | Combo Adaptive Long Only V1 | 3 | €9.475,58 | €1.682,60 | €3.365,20 | €96,98 | €-11,48 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 2 | €9.465,81 | €1.628,58 | €4.885,73 | €93,27 | €-29,24 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €9.458,37 | €3.280,71 | €6.561,42 | €142,78 | €-17,23 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 1 | €9.445,95 | €173,57 | €520,72 | €48,08 | €-16,13 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 3 | €9.376,88 | €3.028,31 | €9.084,94 | €140,07 | €19,23 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.363,68 | €2.030,71 | €4.061,41 | €141,53 | €-17,24 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €9.347,99 | €1.063,87 | €3.191,61 | €145,45 | €-6,78 |
| TEST | Combo Trend | 8 | €9.336,97 | €1.717,94 | €3.435,88 | €95,95 | €53,71 |
| TEST | Master Adaptive Gb20 Be V1 | 4 | €9.333,50 | €3.486,57 | €6.973,15 | €141,63 | €49,72 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.329,68 | €5.050,54 | €10.101,09 | €186,34 | €2,48 |
| TEST | Master Adaptive Gb20 Partial V1 | 4 | €9.323,58 | €3.482,87 | €6.965,73 | €141,48 | €49,67 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.316,09 | €2.020,38 | €4.040,77 | €140,81 | €-17,16 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €9.304,52 | €1.603,18 | €3.206,36 | €139,51 | €-11,52 |
| TEST | Bilanciata 1H V1 | 5 | €9.299,37 | €1.758,39 | €5.275,16 | €138,02 | €-23,54 |
| TEST | Master Adaptive V1 | 4 | €9.287,51 | €3.469,39 | €6.938,79 | €140,94 | €49,48 |
| TEST | Scanner Top10 Long | 5 | €9.284,83 | €2.093,81 | €4.187,61 | €141,25 | €-33,27 |
| TEST | Scanner Top15 Long | 5 | €9.284,83 | €2.093,81 | €4.187,61 | €141,25 | €-33,27 |
| TEST | Scanner Top20 Long | 5 | €9.284,83 | €2.093,81 | €4.187,61 | €141,25 | €-33,27 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.267,73 | €3.631,57 | €7.263,13 | €185,74 | €-78,23 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.266,25 | €2.814,12 | €8.442,36 | €138,35 | €-13,86 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.252,32 | €3.507,78 | €7.015,55 | €185,45 | €-6,31 |
| TEST | 1H Balanced Long No Rhv V1 | 4 | €9.164,41 | €495,86 | €1.487,59 | €138,93 | €-14,32 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.164,11 | €3.423,30 | €6.846,60 | €139,06 | €48,82 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.145,92 | €1.983,48 | €3.966,96 | €138,23 | €-16,84 |
| TEST | Combo Adaptive Runner25 V1 | 4 | €9.133,99 | €1.578,01 | €3.156,02 | €137,15 | €-11,28 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €9.119,25 | €3.197,62 | €6.395,23 | €93,03 | €60,01 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €9.113,92 | €3.195,74 | €6.391,49 | €92,97 | €59,97 |
| TEST | Benchmark trend following EMA 1H | 10 | €9.101,52 | €1.989,35 | €3.978,69 | €88,35 | €-14,29 |
| TEST | Combo Scanner | 2 | €9.069,79 | €1.743,97 | €3.487,94 | €90,40 | €-16,58 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.038,42 | €3.135,05 | €6.270,09 | €136,44 | €-16,47 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 5 | €8.999,90 | €5.713,47 | €11.426,93 | €176,81 | €56,40 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €8.993,57 | €165,26 | €495,78 | €45,78 | €-15,36 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €8.963,36 | €1.548,53 | €3.097,06 | €134,58 | €-11,07 |
| TEST | Forza relativa 1H V1 | 6 | €8.943,39 | €3.814,51 | €7.629,02 | €177,65 | €-36,04 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.943,17 | €3.207,55 | €6.415,10 | €136,45 | €-40,93 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €8.865,85 | €3.075,19 | €6.150,38 | €133,84 | €-16,15 |
| TEST | Combo Adaptive Mfe Trail | 4 | €8.626,82 | €1.479,89 | €2.959,77 | €129,39 | €-10,85 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.642,22 | €-379,65 | 42 | 42 | 33,33% | 0,72 | €-9,04 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.667,00 | €601,37 | 64 | 64 | 46,88% | 1,39 | €9,40 | 3,63% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.415,85 | €351,77 | 32 | 32 | 43,75% | 1,51 | €10,99 | 3,63% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.406,71 | €349,47 | 33 | 33 | 51,52% | 1,41 | €10,59 | 2,31% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.374,11 | €435,24 | 74 | 74 | 48,65% | 1,26 | €5,88 | 3,67% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.344,52 | €334,47 | 24 | 24 | 45,83% | 1,59 | €13,94 | 2,40% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.332,02 | €332,02 | 34 | 34 | 47,06% | 1,47 | €9,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.258,15 | €198,40 | 127 | 126 | 43,31% | 1,07 | €1,56 | 4,89% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.241,11 | €224,39 | 56 | 56 | 44,64% | 1,19 | €4,01 | 5,24% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.240,07 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.217,13 | €198,71 | 116 | 116 | 43,97% | 1,08 | €1,71 | 6,52% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.138,32 | €169,37 | 131 | 131 | 44,27% | 1,07 | €1,29 | 3,64% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.124,89 | €125,02 | 50 | 50 | 48,00% | 1,13 | €2,50 | 2,94% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.105,73 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.098,33 | €137,46 | 81 | 81 | 41,98% | 1,07 | €1,70 | 8,85% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.087,56 | €111,00 | 12 | 12 | 41,67% | 1,57 | €9,25 | 1,80% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
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
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,28 | €-8,72 | 13 | 13 | 61,54% | 0,97 | €-0,67 | 2,10% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.985,41 | €-72,76 | 85 | 84 | 45,88% | 0,97 | €-0,86 | 5,23% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Ampia 4H | Confluenza trend | €9.966,86 | €-49,84 | 38 | 38 | 23,68% | 0,95 | €-1,31 | 4,45% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.962,88 | €-55,08 | 80 | 80 | 42,50% | 0,97 | €-0,69 | 6,52% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.962,61 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,89 | €-26,23 | 7 | 7 | 57,14% | 0,84 | €-3,75 | 1,49% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.927,72 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,93% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.919,66 | €-68,81 | 3 | 3 | 33,33% | 0,35 | €-22,94 | 1,05% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.917,99 | €-71,45 | 3 | 3 | 33,33% | 0,32 | €-23,82 | 1,00% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.906,76 | €-84,48 | 121 | 121 | 39,67% | 0,97 | €-0,70 | 6,72% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.886,68 | €-102,53 | 63 | 63 | 34,92% | 0,93 | €-1,63 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.886,68 | €-102,53 | 63 | 63 | 34,92% | 0,93 | €-1,63 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.886,68 | €-102,53 | 63 | 63 | 34,92% | 0,93 | €-1,63 | 5,27% |
| TEST | Btc Ema 4H | Trend following EMA | €9.876,01 | €-100,21 | 2 | 2 | 0,00% | 0,00 | €-50,11 | 1,72% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.875,62 | €-124,38 | 8 | 8 | 37,50% | 0,49 | €-15,55 | 2,74% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.848,96 | €-129,14 | 30 | 30 | 36,67% | 0,84 | €-4,30 | 3,56% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.838,66 | €-161,34 | 31 | 28 | 38,71% | 0,80 | €-5,20 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Btc Ema 1H | Trend following EMA | €9.823,24 | €-151,42 | 9 | 9 | 33,33% | 0,53 | €-16,82 | 1,90% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.818,18 | €-171,11 | 54 | 54 | 35,19% | 0,86 | €-3,17 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.815,48 | €-184,52 | 62 | 62 | 40,32% | 0,86 | €-2,98 | 7,99% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.813,27 | €-192,61 | 32 | 32 | 40,62% | 0,75 | €-6,02 | 3,91% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,64 | €-167,74 | 3 | 3 | 0,00% | 0,00 | €-55,91 | 2,39% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.803,24 | €-186,06 | 55 | 55 | 34,55% | 0,84 | €-3,38 | 5,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.796,85 | €-183,24 | 103 | 103 | 36,89% | 0,92 | €-1,78 | 8,39% |
| TEST | Sol Ema 4H | Trend following EMA | €9.781,35 | €-207,28 | 4 | 4 | 0,00% | 0,00 | €-51,82 | 2,27% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.779,24 | €-188,30 | 38 | 38 | 44,74% | 0,80 | €-4,96 | 4,50% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.762,69 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.755,58 | €-231,87 | 12 | 12 | 25,00% | 0,47 | €-19,32 | 4,00% |
| TEST | Sol Ema 1H | Trend following EMA | €9.751,75 | €-239,48 | 9 | 9 | 22,22% | 0,37 | €-26,61 | 3,33% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.729,98 | €-282,28 | 22 | 22 | 36,36% | 0,63 | €-12,83 | 4,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.727,80 | €-261,58 | 82 | 82 | 34,15% | 0,85 | €-3,19 | 6,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Combo Adaptive | Combo Adaptive | €9.689,74 | €-296,35 | 85 | 85 | 37,65% | 0,83 | €-3,49 | 6,28% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.684,38 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,56% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.647,37 | €-352,36 | 35 | 35 | 40,00% | 0,70 | €-10,07 | 5,48% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.621,05 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,47% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.615,52 | €-381,45 | 144 | 143 | 35,42% | 0,88 | €-2,65 | 5,68% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.607,59 | €-404,51 | 22 | 22 | 27,27% | 0,48 | €-18,39 | 5,41% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.606,73 | €-475,43 | 80 | 76 | 38,75% | 0,82 | €-5,94 | 8,11% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.591,00 | €-439,36 | 71 | 64 | 40,85% | 0,75 | €-6,19 | 7,55% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.590,34 | €-406,60 | 109 | 108 | 44,95% | 0,81 | €-3,73 | 7,87% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.578,86 | €-428,29 | 107 | 107 | 42,06% | 0,84 | €-4,00 | 6,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.564,42 | €-435,33 | 73 | 73 | 42,47% | 0,78 | €-5,96 | 6,55% |
| TEST | Eth Ema 1H | Trend following EMA | €9.553,02 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,80% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.527,67 | €-469,29 | 153 | 152 | 37,91% | 0,86 | €-3,07 | 7,84% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.520,66 | €-484,87 | 46 | 46 | 30,43% | 0,64 | €-10,54 | 7,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.478,72 | €-500,92 | 53 | 53 | 37,74% | 0,71 | €-9,45 | 7,74% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.475,58 | €-510,92 | 54 | 54 | 37,04% | 0,65 | €-9,46 | 6,08% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.465,81 | €-502,00 | 73 | 73 | 39,73% | 0,76 | €-6,88 | 6,37% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.458,37 | €-520,14 | 72 | 72 | 36,11% | 0,73 | €-7,22 | 11,27% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.445,95 | €-538,45 | 72 | 72 | 34,72% | 0,72 | €-7,48 | 9,13% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.376,88 | €-699,70 | 78 | 77 | 43,59% | 0,71 | €-8,97 | 7,61% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.363,68 | €-616,20 | 58 | 58 | 34,48% | 0,66 | €-10,62 | 7,34% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.347,99 | €-698,69 | 127 | 126 | 37,80% | 0,76 | €-5,50 | 7,67% |
| TEST | Combo Trend | Combo Trend | €9.336,97 | €-714,56 | 115 | 115 | 33,91% | 0,77 | €-6,21 | 9,82% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.333,50 | €-713,06 | 49 | 49 | 24,49% | 0,54 | €-14,55 | 8,39% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.329,68 | €-666,82 | 49 | 49 | 30,61% | 0,63 | €-13,61 | 7,12% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.323,58 | €-722,93 | 44 | 44 | 29,55% | 0,52 | €-16,43 | 7,98% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.316,09 | €-663,90 | 68 | 68 | 38,24% | 0,66 | €-9,76 | 7,02% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.304,52 | €-682,11 | 86 | 86 | 36,05% | 0,63 | €-7,93 | 7,07% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.299,37 | €-674,90 | 116 | 116 | 37,93% | 0,73 | €-5,82 | 12,69% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.287,51 | €-758,82 | 46 | 46 | 28,26% | 0,55 | €-16,50 | 7,80% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.284,83 | €-679,26 | 53 | 53 | 33,96% | 0,56 | €-12,82 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.284,83 | €-679,26 | 53 | 53 | 33,96% | 0,56 | €-12,82 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.284,83 | €-679,26 | 53 | 53 | 33,96% | 0,56 | €-12,82 | 10,31% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.267,73 | €-649,45 | 53 | 53 | 32,08% | 0,64 | €-12,25 | 7,75% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.266,25 | €-714,91 | 59 | 59 | 32,20% | 0,48 | €-12,12 | 8,12% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.252,32 | €-739,76 | 44 | 44 | 25,00% | 0,55 | €-16,81 | 8,18% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.164,41 | €-823,44 | 52 | 52 | 30,77% | 0,53 | €-15,84 | 9,26% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.164,11 | €-881,60 | 81 | 81 | 46,91% | 0,53 | €-10,88 | 9,02% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.145,92 | €-834,43 | 75 | 75 | 37,33% | 0,61 | €-11,13 | 8,78% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.133,99 | €-852,92 | 90 | 90 | 32,22% | 0,58 | €-9,48 | 11,05% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.119,25 | €-937,64 | 56 | 56 | 30,36% | 0,48 | €-16,74 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.113,92 | €-942,94 | 60 | 60 | 31,67% | 0,47 | €-15,72 | 12,06% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.101,52 | €-881,51 | 81 | 81 | 29,63% | 0,55 | €-10,88 | 9,84% |
| TEST | Combo Scanner | Combo Scanner | €9.069,79 | €-911,23 | 78 | 78 | 34,62% | 0,61 | €-11,68 | 11,38% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.038,42 | €-941,04 | 53 | 53 | 32,08% | 0,43 | €-17,76 | 11,72% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €8.999,90 | €-1.049,90 | 35 | 35 | 17,14% | 0,33 | €-30,00 | 11,40% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €8.993,57 | €-991,57 | 92 | 92 | 29,35% | 0,61 | €-10,78 | 11,09% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.963,36 | €-1.023,80 | 71 | 71 | 30,99% | 0,42 | €-14,42 | 11,05% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.943,39 | €-1.016,19 | 98 | 98 | 29,59% | 0,58 | €-10,37 | 12,58% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.943,17 | €-1.011,64 | 48 | 48 | 27,08% | 0,54 | €-21,08 | 11,51% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €8.865,85 | €-1.114,00 | 65 | 65 | 32,31% | 0,37 | €-17,14 | 12,28% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.626,82 | €-1.360,58 | 97 | 97 | 30,93% | 0,42 | €-14,03 | 13,79% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00052 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €21,02 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,07003 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,22 |
| Principale 4H | SOL | LONG | Confluenza trend | 240m | 3,0x | 77,23844 | 76,92000 | 75,78654 | 51,87849 | 80,14224 | €11,96 | €35,87 | €0,67 | €-0,15 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,93 | €104,79 | €1,51 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06998 | 0,07003 | 0,07099 | 0,09295 | 0,06796 | €1.095,91 | €3.287,73 | €47,34 | €-2,44 |
| Bilanciata 1H V1 | ACE | LONG | Confluenza trend | 60m | 3,0x | 0,23434 | 0,22010 | 0,20982 | 0,15740 | 0,28337 | €142,14 | €426,43 | €44,61 | €-25,91 |
| Bilanciata 1H V1 | SOXL | SHORT | Confluenza trend | 60m | 3,0x | 127,38352 | 126,80000 | 132,78383 | 169,20778 | 116,58291 | €350,35 | €1.051,05 | €44,56 | €4,81 |
| 1H Balanced Long No Rhv V1 | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| 1H Balanced Long No Rhv V1 | BTC | LONG | Confluenza trend | 60m | 3,0x | 64764,77036 | 64323,89000 | 63832,15767 | 43500,33743 | 66629,99575 | €87,47 | €262,41 | €3,78 | €-1,79 |
| 1H Balanced Long No Rhv V1 | ACE | LONG | Confluenza trend | 60m | 3,0x | 0,22764 | 0,22010 | 0,20039 | 0,15290 | 0,28213 | €126,17 | €378,51 | €45,31 | €-12,53 |
| 1H Balanced Short Trend Down Strict V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 1,00052 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €-22,35 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ACE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,21513 | 0,22010 | 0,18931 | 0,14449 | 0,26676 | €132,78 | €398,34 | €47,80 | €9,20 |
| Bilanciata 1H V2 | SNDK | SHORT | Confluenza trend V2 | 60m | 3,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2137,41315 | 1493,65499 | €444,17 | €1.332,50 | €47,80 | €21,96 |
| Bilanciata 1H V2 | SUI | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,65261 | 0,65261 | 0,66201 | 0,86688 | 0,63381 | €26,68 | €80,03 | €1,15 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,25 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 1,00052 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €-0,23 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.164,76 | €3.494,29 | €50,32 | €-0,00 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 64764,77036 | 64323,89000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.042,91 | €3.128,72 | €45,05 | €-21,30 |
| Bilanciata 1H V3 Filtered | SKHYNIX | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1120,69460 | 1447,61199 | 1027,99798 | €565,93 | €1.697,79 | €48,14 | €7,11 |
| 1H Fast Score 6 75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.575,03 | €4.725,08 | €52,92 | €-0,00 |
| 1H Fast Score 6 75 V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 1,00052 | 1,00671 | 1,32244 | 0,97884 | €1.521,02 | €4.563,07 | €51,11 | €-22,73 |
| 1H Fast Score 6 75 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €489,70 | €1.469,11 | €51,42 | €13,01 |
| 1H Fast Score 6 75 V1 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €750,57 | €2.251,70 | €49,66 | €9,43 |
| 1H Fast Score 6 75 No Trend Up V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.533,15 | €4.599,45 | €51,51 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 1,00052 | 1,00671 | 1,32244 | 0,97884 | €1.480,58 | €4.441,75 | €49,75 | €-22,13 |
| 1H Fast Score 6 75 No Trend Up V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €476,68 | €1.430,05 | €50,05 | €12,67 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €730,61 | €2.191,84 | €48,33 | €9,18 |
| 1H Fast Score 6 75 Range Only V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €492,83 | €1.478,49 | €51,74 | €13,10 |
| 1H Fast Score 6 75 Range Only V1 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1105,10654 | 1085,23000 | 1099,51029 | 1467,94985 | 1072,37322 | €873,85 | €2.621,54 | €0,00 | €47,15 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 1,00052 | 1,00671 | 1,32244 | 0,97884 | €1.578,12 | €4.734,36 | €53,02 | €-23,58 |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.566,58 | €4.699,75 | €52,64 | €-31,99 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €63,61 | €190,84 | €2,14 | €-1,30 |
| 1H Fast Nohigh Cap75 V1 | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1609,09396 | 1582,58000 | 1653,98690 | 2137,41315 | 1541,75456 | €12,94 | €38,82 | €1,08 | €0,64 |
| 1H Fast Nohigh Cap75 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €485,34 | €1.456,02 | €50,96 | €12,90 |
| 1H Fast Nohigh Cap75 V1 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €734,40 | €2.203,21 | €48,59 | €9,23 |
| 1H Fast Long Btc 1 3 Cap75 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.488,39 | €4.465,16 | €50,01 | €-30,40 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ACE | LONG | Momentum / breakout | 60m | 3,0x | 0,21504 | 0,22010 | 0,19338 | 0,14444 | 0,24753 | €162,74 | €488,22 | €49,17 | €11,48 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| 1H Fast No Pepe V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| 1H Fast No Pepe V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.477,62 | €4.432,85 | €49,65 | €-30,18 |
| 1H Fast No Pepe V1 | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1609,09396 | 1582,58000 | 1653,98690 | 2137,41315 | 1541,75456 | €15,88 | €47,64 | €1,33 | €0,78 |
| 1H Fast No Pepe V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €483,03 | €1.449,09 | €50,71 | €12,84 |
| 1H Fast No Pepe V1 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1080,56127 | 1085,23000 | 1104,16618 | 1435,34556 | 1045,15392 | €730,26 | €2.190,78 | €47,86 | €-9,47 |
| 1H Fast Tp2 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €115,44 | €346,32 | €3,88 | €-0,00 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| 1H Fast Tp2 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 66215,50122 | €1.432,32 | €4.296,97 | €48,13 | €-29,25 |
| 1H Fast Tp2 V1 | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1591,30464 | 1582,58000 | 1632,05331 | 2113,78300 | 1509,80731 | €632,00 | €1.896,01 | €48,55 | €10,40 |
| 1H Fast Tp2 V1 | ACE | LONG | Momentum / breakout | 60m | 3,0x | 0,23824 | 0,22010 | 0,21637 | 0,16002 | 0,28199 | €157,73 | €473,20 | €43,44 | €-36,04 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,35 | €73,04 | €0,82 | €-0,00 |
| Rapida 1H V3 Filtered | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €154,24 | €462,73 | €40,02 | €0,00 |
| Rapida 1H V3 Filtered | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,22010 | 0,20616 | 0,15256 | 0,25859 | €174,86 | €524,57 | €48,44 | €-16,25 |
| Rapida 1H V3 Filtered | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €722,64 | €2.167,91 | €47,81 | €9,08 |
| 1H Fast V3 Cap75 V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.494,66 | €4.483,99 | €50,22 | €-0,00 |
| 1H Fast V3 Cap75 V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99556 | 1,00052 | 1,00671 | 1,32244 | 0,97884 | €1.491,98 | €4.475,94 | €50,13 | €-22,30 |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06970 | 0,07003 | 0,07048 | 0,09258 | 0,06853 | €37,09 | €111,27 | €1,25 | €-0,53 |
| 1H Fast V3 Cap75 V1 | SOXL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €458,42 | €1.375,27 | €48,13 | €12,18 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €730,89 | €2.192,68 | €48,35 | €9,19 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| 1H Fast V3 Nohigh V1 | SNDK | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1591,30464 | 1582,58000 | 1632,05331 | 2113,78300 | 1530,18165 | €13,22 | €39,65 | €1,02 | €0,22 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €707,08 | €2.121,25 | €46,78 | €8,89 |
| 1H Fast V3 Long Only V1 | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,22010 | 0,20616 | 0,15256 | 0,25859 | €165,26 | €495,78 | €45,78 | €-15,36 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.431,94 | €4.295,82 | €48,11 | €-29,24 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,35 | €55,04 | €0,62 | €-0,00 |
| 1H Fast V3 No Esports V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| 1H Fast V3 No Esports V1 | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,22010 | 0,20616 | 0,15256 | 0,25859 | €170,95 | €512,85 | €47,35 | €-15,89 |
| 1H Fast V3 No Esports V1 | SNDK | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1591,30464 | 1582,58000 | 1632,05331 | 2113,78300 | 1530,18165 | €11,72 | €35,16 | €0,90 | €0,19 |
| 1H Fast V3 No Esports V1 | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €708,97 | €2.126,90 | €46,90 | €8,91 |
| 1H Fast V3 No Esports Long Only V1 | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,22010 | 0,20616 | 0,15256 | 0,25859 | €173,57 | €520,72 | €48,08 | €-16,13 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,51 | €73,52 | €0,82 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €155,26 | €465,77 | €40,28 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ACE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22714 | 0,22010 | 0,20616 | 0,15256 | 0,25859 | €176,01 | €528,02 | €48,75 | €-16,36 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €727,39 | €2.182,17 | €48,12 | €9,14 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.460,07 | €4.380,22 | €49,06 | €-29,82 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1911,14000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €48,22 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €1.419,52 | €4.258,55 | €47,70 | €-28,99 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00052 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €16,37 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,07003 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,49 |
| Ampia 4H | BTW | LONG | Confluenza trend | 240m | 2,0x | 0,32695 | 0,32695 | 0,28771 | 0,16511 | 0,43680 | €207,21 | €414,42 | €49,73 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,65521 | 0,65521 | 0,67955 | 0,97953 | 0,58704 | €31,61 | €63,21 | €2,35 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,49 | €-0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,99556 | 1,00052 | 1,00990 | 1,48836 | 0,96402 | €1.577,31 | €3.154,62 | €45,43 | €-15,71 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,65491 | 0,65491 | 0,66473 | 0,97909 | 0,63329 | €1.513,47 | €3.026,93 | €45,42 | €-0,00 |
| Forza relativa 1H V1 | SNDK | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1625,29424 | 1582,58000 | 1683,24365 | 2429,81489 | 1497,80552 | €31,35 | €62,71 | €2,24 | €1,65 |
| Forza relativa 1H V1 | ACE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,23434 | 0,22010 | 0,20982 | 0,11834 | 0,28828 | €215,46 | €430,92 | €45,08 | €-26,19 |
| Forza relativa 1H V1 | SOXL | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 127,38352 | 126,80000 | 132,78383 | 190,43837 | 115,50285 | €460,04 | €920,07 | €39,01 | €4,21 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SKHYNIX | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1149,28002 | 1085,23000 | 1102,62450 | 1718,17363 | 1074,31996 | €816,29 | €1.632,59 | €0,00 | €90,98 |
| Forza relativa 1H V2 | ACE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,22714 | 0,22010 | 0,20017 | 0,11470 | 0,28646 | €202,95 | €405,90 | €48,19 | €-12,57 |
| Forza relativa 1H V2 | SNDK | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1482,11107 | €20,14 | €40,27 | €1,44 | €0,66 |
| Forza relativa 1H V2 | SUI | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,65001 | 0,65001 | 0,65937 | 0,97176 | 0,62942 | €20,45 | €40,91 | €0,59 | €-0,00 |
| Forza relativa 1H V2 | SOXL | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 127,38352 | 126,80000 | 132,78383 | 190,43837 | 115,50285 | €540,44 | €1.080,88 | €45,82 | €4,95 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €0,00 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07003 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-24,57 |
| Benchmark Donchian breakout 1H | SKHYNIX | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1154,93662 | 1085,23000 | 1105,66779 | 1726,63025 | 1055,56120 | €773,75 | €1.547,50 | €0,00 | €93,40 |
| Benchmark Donchian breakout 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 64764,77036 | 64323,89000 | 63728,53404 | 32706,20903 | 67355,36118 | €59,87 | €119,74 | €1,92 | €-0,82 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €0,00 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,07003 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-24,00 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1154,93662 | 1085,23000 | 1105,66779 | 1726,63025 | 1055,56120 | €755,53 | €1.511,07 | €0,00 | €91,20 |
| Donchian 1H Gb20 120R V1 | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 64764,77036 | 64323,89000 | 63728,53404 | 32706,20903 | 67355,36118 | €58,46 | €116,93 | €1,87 | €-0,80 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,07003 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,07 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 1,00052 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €-0,07 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 1911,30218 | 1911,14000 | 1880,72135 | 965,20760 | 1978,58002 | €44,44 | €88,89 | €1,42 | €-0,01 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SKHYNIX | SHORT | Trend following EMA | 60m | 2,0x | 1149,28002 | 1085,23000 | 1102,62450 | 1718,17363 | 1065,99106 | €59,36 | €118,73 | €0,00 | €6,62 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €21,92 | €43,84 | €0,72 | €-0,00 |
| Benchmark trend following EMA 1H | SNDK | SHORT | Trend following EMA | 60m | 2,0x | 1609,09396 | 1582,58000 | 1673,22674 | 2405,59548 | 1468,00188 | €13,00 | €26,01 | €1,04 | €0,43 |
| Benchmark trend following EMA 1H | SOXL | SHORT | Trend following EMA | 60m | 2,0x | 127,93319 | 126,80000 | 134,32945 | 191,26013 | 113,86143 | €389,91 | €779,82 | €38,99 | €6,91 |
| Benchmark trend following EMA 1H | ACE | LONG | Trend following EMA | 60m | 2,0x | 0,23824 | 0,22010 | 0,20965 | 0,12031 | 0,30114 | €185,38 | €370,75 | €44,49 | €-28,23 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | BTC | LONG | Scanner Top 5 Long | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.762,47 | €3.524,93 | €50,76 | €-24,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1914,76288 | 1911,14000 | 1887,19029 | 966,95525 | 1969,90805 | €57,06 | €114,13 | €1,64 | €-0,22 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,28489 | €28,12 | €56,23 | €0,81 | €-0,11 |
| Scanner Top 5 Long 1H | ACE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28044 | €213,82 | €427,63 | €50,99 | €-11,97 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,07003 | 0,07070 | 0,10420 | 0,06769 | €1.674,47 | €3.348,95 | €48,22 | €-15,94 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.627,25 | €3.254,49 | €48,28 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,39 | €58,78 | €2,11 | €0,97 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €559,10 | €1.118,20 | €47,97 | €8,17 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 1911,30218 | 1911,14000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,01 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €-22,05 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,28489 | €55,73 | €111,47 | €1,61 | €-0,21 |
| Scanner Top10 Long | ACE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-11,01 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06970 | 0,07003 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-16,21 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,76 | €59,51 | €2,13 | €0,98 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €568,25 | €1.136,50 | €48,76 | €8,30 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 1911,30218 | 1911,14000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,01 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €-22,05 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,28489 | €55,73 | €111,47 | €1,61 | €-0,21 |
| Scanner Top15 Long | ACE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-11,01 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06970 | 0,07003 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-16,21 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,76 | €59,51 | €2,13 | €0,98 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €568,25 | €1.136,50 | €48,76 | €8,30 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 1911,30218 | 1911,14000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,01 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.619,28 | €3.238,57 | €46,64 | €-22,05 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,28489 | €55,73 | €111,47 | €1,61 | €-0,21 |
| Scanner Top20 Long | ACE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28044 | €196,75 | €393,50 | €46,92 | €-11,01 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06970 | 0,07003 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-16,21 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.653,82 | €3.307,64 | €49,06 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,76 | €59,51 | €2,13 | €0,98 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €568,25 | €1.136,50 | €48,76 | €8,30 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.610,50 | €3.221,00 | €46,38 | €-6,08 |
| Scanner Top 5 + forza BTC 1H | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €199,35 | €398,70 | €47,54 | €-11,16 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.509,61 | €3.019,22 | €43,48 | €-5,70 |
| Scanner Top5 Btc Mfe V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €186,86 | €373,72 | €44,57 | €-10,46 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.636,11 | €3.272,21 | €47,12 | €-6,17 |
| Scanner Top5 Btc Guard V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €197,83 | €395,66 | €47,18 | €-11,07 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.538,99 | €3.077,99 | €44,32 | €-5,81 |
| Scanner Top5 Btc Btc Le3 V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €190,50 | €381,00 | €45,43 | €-10,66 |
| Scanner Top5 Btc Btc 2 3 V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22714 | 0,22010 | 0,20017 | 0,11470 | 0,28646 | €209,35 | €418,71 | €49,71 | €-12,97 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.598,05 | €3.196,11 | €46,02 | €-6,03 |
| Scanner Top5 Btc Guard Mfe V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €193,23 | €386,45 | €46,08 | €-10,81 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.656,20 | €3.312,41 | €47,70 | €-6,25 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €200,26 | €400,52 | €47,76 | €-11,21 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.627,79 | €3.255,58 | €46,88 | €-6,14 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €196,82 | €393,65 | €46,94 | €-11,01 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18671 | 0,22010 | 0,21397 | 0,09429 | 0,25393 | €184,53 | €369,05 | €0,00 | €65,99 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 80,39464 | €1.595,98 | €3.191,96 | €45,96 | €-6,02 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ACE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18671 | 0,22010 | 0,21397 | 0,09429 | 0,25393 | €184,63 | €369,27 | €0,00 | €66,03 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 80,39464 | €1.596,91 | €3.193,82 | €45,99 | €-6,03 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,07003 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €4,57 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,07003 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,09 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €118,87 | €237,73 | €3,80 | €-0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | SKHYNIX | SHORT | Combo Trend | 60m | 2,0x | 1149,28002 | 1085,23000 | 1102,62450 | 1718,17363 | 1065,99106 | €678,02 | €1.356,03 | €0,00 | €75,57 |
| Combo Trend | BTC | LONG | Combo Trend | 60m | 2,0x | 64764,77036 | 64323,89000 | 63728,53404 | 32706,20903 | 67044,49028 | €47,89 | €95,77 | €1,53 | €-0,65 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,65521 | 0,65521 | 0,66601 | 0,97953 | 0,63145 | €29,12 | €58,23 | €0,96 | €-0,00 |
| Combo Trend | SOXL | SHORT | Combo Trend | 60m | 2,0x | 127,93319 | 126,80000 | 134,32945 | 191,26013 | 113,86143 | €431,24 | €862,49 | €43,12 | €7,64 |
| Combo Trend | ACE | LONG | Combo Trend | 60m | 2,0x | 0,23824 | 0,22010 | 0,20965 | 0,12031 | 0,30114 | €190,01 | €380,02 | €45,60 | €-28,94 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 77,06541 | 76,92000 | 75,95567 | 38,91803 | 79,50684 | €1.552,40 | €3.104,81 | €44,71 | €-5,86 |
| Combo Scanner | ACE | LONG | Combo Scanner | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28584 | €191,56 | €383,13 | €45,69 | €-10,72 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07003 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,09 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €569,18 | €1.138,35 | €48,84 | €8,32 |
| Combo Adaptive | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,22010 | 0,20982 | 0,11834 | 0,28337 | €233,37 | €466,74 | €48,83 | €-28,36 |
| Combo Adaptive | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1085,23000 | 1120,89130 | 1630,17096 | 1029,46346 | €835,77 | €1.671,55 | €46,72 | €7,95 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,07003 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,16 |
| Combo Adaptive Mfe Trail | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €506,73 | €1.013,47 | €43,48 | €7,41 |
| Combo Adaptive Mfe Trail | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,22010 | 0,20982 | 0,11834 | 0,28337 | €207,77 | €415,53 | €43,47 | €-25,25 |
| Combo Adaptive Mfe Trail | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1085,23000 | 1120,89130 | 1630,17096 | 1029,46346 | €752,68 | €1.505,36 | €42,07 | €7,16 |
| Combo Adaptive Quality7 V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,22714 | 0,22010 | 0,20017 | 0,11470 | 0,28107 | €200,38 | €400,75 | €47,58 | €-12,41 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 129,07251 | 126,80000 | 135,06094 | 192,96340 | 117,09566 | €512,64 | €1.025,28 | €47,57 | €18,05 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Regime V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €204,28 | €408,56 | €49,03 | €9,44 |
| Combo Adaptive Regime V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,65421 | 0,65421 | 0,66363 | 0,97804 | 0,63537 | €1.699,46 | €3.398,92 | €48,94 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €199,96 | €399,91 | €47,99 | €9,24 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €18,79 | €37,57 | €0,54 | €-0,26 |
| Combo Adaptive Long Only V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28044 | €200,54 | €401,09 | €47,83 | €-11,22 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07003 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,09 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €546,55 | €1.093,10 | €46,90 | €7,99 |
| Combo Adaptive Partial 1R V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,22010 | 0,20982 | 0,11834 | 0,28337 | €224,09 | €448,18 | €46,89 | €-27,24 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1085,23000 | 1120,89130 | 1630,17096 | 1029,46346 | €802,55 | €1.605,09 | €44,86 | €7,63 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €202,50 | €405,01 | €48,60 | €9,36 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07003 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,09 |
| Combo Adaptive Runner25 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 111,29360 | €536,52 | €1.073,03 | €46,03 | €7,84 |
| Combo Adaptive Runner25 V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,22010 | 0,20982 | 0,11834 | 0,30789 | €219,98 | €439,95 | €46,03 | €-26,74 |
| Combo Adaptive Runner25 V1 | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1085,23000 | 1120,89130 | 1630,17096 | 998,98752 | €790,61 | €1.581,23 | €44,19 | €7,52 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,07003 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,09 |
| Combo Adaptive Tp3 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 111,29360 | €526,49 | €1.052,99 | €45,17 | €7,69 |
| Combo Adaptive Tp3 V1 | ACE | LONG | Combo Adaptive | 60m | 2,0x | 0,23434 | 0,22010 | 0,20982 | 0,11834 | 0,30789 | €215,87 | €431,74 | €45,17 | €-26,24 |
| Combo Adaptive Tp3 V1 | SKHYNIX | SHORT | Combo Adaptive | 60m | 2,0x | 1090,41536 | 1085,23000 | 1120,89130 | 1630,17096 | 998,98752 | €775,84 | €1.551,69 | €43,37 | €7,38 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64764,77036 | 64323,89000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.139,88 | €3.419,65 | €49,24 | €-23,28 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 64832,38388 | 64323,89000 | 63691,33393 | 32740,35386 | 67685,00877 | €1.406,22 | €2.812,44 | €49,50 | €-22,06 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 64764,77036 | 64323,89000 | 63935,78130 | 43500,33743 | 66422,74849 | €1.298,67 | €3.896,00 | €49,87 | €-26,52 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 64832,38388 | 64323,89000 | 63691,33393 | 32740,35386 | 68027,32376 | €1.396,63 | €2.793,26 | €49,16 | €-21,91 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 64806,45612 | 64323,89000 | 65843,35941 | 96885,65189 | 62940,03018 | €1.575,64 | €3.151,29 | €50,42 | €23,47 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 64764,77036 | 64323,89000 | 63832,15767 | 43500,33743 | 66629,99575 | €1.156,05 | €3.468,16 | €49,94 | €-23,61 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 64832,38388 | 64323,89000 | 63587,60211 | 32740,35386 | 67944,33831 | €1.295,52 | €2.591,05 | €49,75 | €-20,32 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,06541 | 76,92000 | 75,95567 | 51,76227 | 79,28489 | €1.129,69 | €3.389,07 | €48,80 | €-6,39 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 77,23844 | 76,92000 | 75,64136 | 39,00541 | 81,23117 | €1.183,99 | €2.367,98 | €48,96 | €-9,76 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 77,23844 | 76,92000 | 75,64136 | 39,00541 | 81,71030 | €1.200,73 | €2.401,46 | €49,66 | €-9,90 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 77,23844 | 76,92000 | 75,49616 | 39,00541 | 81,59414 | €1.100,38 | €2.200,75 | €49,64 | €-9,07 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1907,45141 | 1911,14000 | 1879,98411 | 1281,17153 | 1962,38601 | €1.105,17 | €3.315,52 | €47,74 | €6,41 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1911,14000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €0,42 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €41,94 |
| Master Adaptive V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €194,21 | €388,43 | €46,61 | €8,98 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,92000 | 75,85610 | 38,86702 | 79,18096 | €1.611,05 | €3.222,10 | €46,40 | €-1,86 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1911,14000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,42 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 58,53900 | 58,18865 | 29,81460 | 60,73912 | €1.637,93 | €3.275,87 | €47,17 | €-27,73 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €42,43 |
| Master Adaptive No Alt V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22644 | 0,22010 | 0,19943 | 0,11435 | 0,28044 | €194,09 | €388,18 | €46,29 | €-10,86 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,92000 | 75,85610 | 38,86702 | 79,18096 | €1.548,55 | €3.097,10 | €44,60 | €-1,79 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 58,53900 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €-18,05 |
| Master Adaptive Strict3 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.579,70 | €3.159,40 | €45,50 | €-21,51 |
| Master Adaptive Strict3 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22714 | 0,22010 | 0,20017 | 0,11470 | 0,28107 | €22,04 | €44,08 | €5,23 | €-1,37 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1911,14000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €0,13 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 58,53900 | 58,18865 | 29,81460 | 60,73912 | €1.636,69 | €3.273,37 | €47,14 | €-27,71 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 64764,77036 | 64323,89000 | 63832,15767 | 32706,20903 | 66629,99575 | €1.591,99 | €3.183,97 | €45,85 | €-21,67 |
| Master Adaptive Expanded V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23824 | 0,22010 | 0,21012 | 0,12031 | 0,29449 | €190,24 | €380,49 | €44,91 | €-28,98 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1911,14000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €0,41 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €41,39 |
| Master Adaptive Gb20 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €191,63 | €383,27 | €45,99 | €8,86 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,92000 | 75,85610 | 38,86702 | 79,18096 | €1.589,64 | €3.179,29 | €45,78 | €-1,83 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 58,53900 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €-18,79 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €41,51 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23824 | 0,22010 | 0,21012 | 0,12031 | 0,32261 | €190,60 | €381,19 | €45,00 | €-29,03 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1911,14000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €0,42 |
| Master Adaptive Gb20 Be V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €42,15 |
| Master Adaptive Gb20 Be V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €195,18 | €390,35 | €46,84 | €9,02 |
| Master Adaptive Gb20 Be V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,92000 | 75,85610 | 38,86702 | 79,18096 | €1.619,03 | €3.238,05 | €46,63 | €-1,87 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1911,14000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €0,42 |
| Master Adaptive Gb20 Partial V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €42,11 |
| Master Adaptive Gb20 Partial V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21513 | 0,22010 | 0,18931 | 0,10864 | 0,26676 | €194,97 | €389,94 | €46,79 | €9,01 |
| Master Adaptive Gb20 Partial V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,92000 | 75,85610 | 38,86702 | 79,18096 | €1.617,31 | €3.234,61 | €46,58 | €-1,87 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1911,14000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €15,99 |
| Master Adaptive Gb20 Loss Cap V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64323,89000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €47,22 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ACE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22714 | 0,22010 | 0,20691 | 0,11470 | 0,28107 | €76,44 | €152,88 | €13,61 | €-4,74 |
| Master Adaptive Gb20 Loss Cap V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 76,96439 | 76,92000 | 76,13317 | 38,86702 | 79,18096 | €1.799,28 | €3.598,56 | €38,86 | €-2,08 |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1902,79048 | 1911,14000 | 1881,47923 | 1278,04094 | 1934,75736 | €1.508,82 | €4.526,45 | €50,70 | €19,86 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00052 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €22,06 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 59,42488 | 58,53900 | 57,77054 | 39,91371 | 62,73356 | €20,16 | €60,47 | €1,68 | €-0,90 |
| Main Side Regime Guard V1 | SOL | LONG | Confluenza trend | 240m | 3,0x | 77,23844 | 76,92000 | 75,78654 | 51,87849 | 80,14224 | €862,59 | €2.587,77 | €48,64 | €-10,67 |
| Main Dynamic Asset Selector V1 | ACE | LONG | Confluenza trend | 240m | 3,0x | 0,21504 | 0,22010 | 0,18924 | 0,14444 | 0,26665 | €142,09 | €426,26 | €51,15 | €10,02 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,07003 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-16,42 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00052 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €12,26 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 64764,77036 | 64323,89000 | 64039,40494 | 43500,33743 | 65852,81851 | €62,03 | €186,09 | €2,08 | €-1,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | SHORT | Momentum / breakout | 60m | 3,0x | 1609,09396 | 1582,58000 | 1653,98690 | 2137,41315 | 1541,75456 | €12,62 | €37,86 | €1,06 | €0,62 |
| 1H Fast Nohigh Cap75 Short Only V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 127,93319 | 126,80000 | 132,41057 | 169,93793 | 121,21713 | €473,26 | €1.419,79 | €49,69 | €12,58 |
| 1H Fast Nohigh Cap75 Short Only V1 | SKHYNIX | SHORT | Momentum / breakout | 60m | 3,0x | 1089,79573 | 1085,23000 | 1113,82819 | 1447,61199 | 1053,74704 | €716,13 | €2.148,39 | €47,38 | €9,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,23 |
| 1H Balanced V3 Long Only V1 | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 1,00052 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €-0,21 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.101,68 | €3.305,04 | €47,59 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BTC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 64764,77036 | 64323,89000 | 63832,15767 | 43500,33743 | 66629,99575 | €986,42 | €2.959,27 | €42,61 | €-20,14 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 1089,79573 | 1085,23000 | 1120,69460 | 1447,61199 | 1027,99798 | €535,28 | €1.605,84 | €45,53 | €6,73 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,07003 | 0,07070 | 0,10420 | 0,06769 | €1.687,46 | €3.374,92 | €48,60 | €-16,07 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.639,87 | €3.279,73 | €48,65 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,62 | €59,23 | €2,12 | €0,98 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €563,44 | €1.126,87 | €48,34 | €8,23 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,07003 | 0,07070 | 0,10420 | 0,06769 | €1.690,03 | €3.380,06 | €48,67 | €-16,09 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,65521 | 0,65521 | 0,66493 | 0,97953 | 0,63577 | €1.642,36 | €3.284,73 | €48,72 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1609,09396 | 1582,58000 | 1666,81345 | 2405,59548 | 1493,65499 | €29,66 | €59,32 | €2,13 | €0,98 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 127,73331 | 126,80000 | 133,21322 | 190,96130 | 116,77350 | €564,29 | €1.128,59 | €48,42 | €8,25 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Forza relativa 1H V1 | SKHYNIX | SHORT | 2026-08-19T05:05:45+00:00 | 1076,87703 | €4,15 | 2,13 | TARGET |
| 1H Fast V3 Nohigh V1 | ACE | LONG | 2026-08-19T05:05:45+00:00 | 0,21622 | €-0,43 | -0,01 | STOP_GAP_STRESS |
| Scanner Top 5 Long 1H | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-76,60 | -1,51 | STOP_GAP_STRESS |
| Scanner Top5 Btc Tp3 V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,88 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Runner25 V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,85 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Mfe V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-57,10 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-60,01 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Mfe V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,61 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Btc Le3 V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-60,75 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-59,71 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Btc Le3 V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-58,21 | -1,27 | STOP_GAP_STRESS |
| Scanner Top5 Btc Btc 2 3 V1 | GPS | LONG | 2026-08-19T03:06:26+00:00 | 0,01379 | €-123,11 | -2,48 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
