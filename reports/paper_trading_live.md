# Paper trading automatico KuCoin

Generato: 2026-07-28T05:15:11+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-28T05:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-28T05:08:25+00:00 | 2026-07-28T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-28T04:45:00+00:00 | 2026-07-28T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-28T04:00:00+00:00 | 2026-07-28T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-28T00:00:00+00:00 | 2026-07-28T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Mfe Trail | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | BEAT | 60m | SHORT | -4,75 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | SUI | 240m | SHORT | -7,49 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -7,39 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -6,72 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -6,69 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,50 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -5,90 | 6,00 | 0,10 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -5,72 | 6,00 | 0,28 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -1,43 | 6,00 | 4,57 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,82 | 6,00 | 5,18 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,03 | 6,00 | 5,97 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | AKE | 60m | LONG | 7,75 | 4,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.607,10 | -3,93% | €-392,90 | €3.000,00 | -13,10% | 6 | 25 | 28,00% | 0,58 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 25 | 867 | CAMPIONE INSUFFICIENTE | 30 (mancano 5) |

- Trade del Principale 4H chiusi: **25**; win rate **28,00%**; profit factor **0,58**.
- Expectancy: **€-17,67** per trade; P&L netto: **€-441,81**; max drawdown: **6,36%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.607,10 | €956,55 | €2.869,65 | €97,18 | €49,86 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.564,66 | €1.610,58 | €4.831,74 | €157,52 | €-20,88 |
| TEST | 1H Fast Score 6 75 V1 | 6 | €10.555,92 | €3.844,61 | €11.533,83 | €53,79 | €96,95 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €10.515,98 | €3.841,03 | €11.523,10 | €53,42 | €96,50 |
| TEST | Benchmark Donchian breakout 1H | 7 | €10.505,24 | €4.754,01 | €9.508,03 | €101,35 | €191,20 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.497,24 | €289,14 | €578,29 | €55,00 | €12,81 |
| TEST | 1H Fast V3 Cap75 V1 | 6 | €10.438,71 | €3.029,24 | €9.087,73 | €102,58 | €63,09 |
| TEST | 1H Fast Nohigh Cap75 V1 | 1 | €10.415,57 | €225,73 | €677,19 | €51,70 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 1 | €10.395,73 | €172,19 | €516,57 | €51,51 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 6 | €10.389,49 | €3.471,87 | €10.415,61 | €154,43 | €10,01 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.364,59 | €469,39 | €938,78 | €105,09 | €12,65 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 7 | €10.328,24 | €3.399,82 | €10.199,45 | €156,26 | €-6,63 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €10.327,26 | €2.397,44 | €7.192,33 | €51,15 | €58,07 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 6 | €10.323,87 | €2.975,89 | €8.927,68 | €52,77 | €62,76 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €10.299,20 | €4.213,47 | €8.426,95 | €153,60 | €-7,39 |
| TEST | Bilanciata 1H V1 | 7 | €10.297,10 | €3.167,53 | €9.502,58 | €104,00 | €40,30 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 2 | €10.296,85 | €313,60 | €940,79 | €102,49 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 8 | €10.266,65 | €4.918,20 | €14.754,61 | €153,30 | €15,00 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.264,58 | €142,13 | €426,38 | €0,00 | €31,69 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.237,04 | €3.980,81 | €7.961,62 | €56,76 | €193,93 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.235,71 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.218,59 | €143,01 | €429,04 | €51,48 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 6 | €10.200,35 | €5.014,59 | €15.043,76 | €52,28 | €114,51 |
| TEST | Combo Adaptive | 6 | €10.195,96 | €1.603,92 | €3.207,84 | €203,73 | €12,52 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 7 | €10.185,10 | €4.877,60 | €14.632,81 | €152,97 | €14,29 |
| TEST | Bilanciata 1H V2 | 3 | €10.181,14 | €1.358,78 | €4.076,33 | €101,14 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 7 | €10.177,60 | €3.768,54 | €11.305,62 | €102,66 | €46,28 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.175,99 | €141,59 | €424,78 | €50,97 | €-18,52 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 2 | €10.159,32 | €1.034,94 | €3.104,81 | €98,69 | €0,00 |
| TEST | Btc Bollinger 1H | 1 | €10.144,18 | €1.412,24 | €4.236,72 | €50,84 | €-21,40 |
| TEST | Combo Adaptive Runner25 V1 | 7 | €10.134,76 | €2.324,06 | €4.648,11 | €201,56 | €13,42 |
| TEST | Main Side Regime Guard V1 | 4 | €10.127,11 | €1.253,51 | €3.760,52 | €101,62 | €57,26 |
| TEST | Sol Donchian 1H | 1 | €10.123,46 | €1.254,69 | €3.764,07 | €0,00 | €33,59 |
| TEST | Combo Trend Side Regime Guard V1 | 7 | €10.112,64 | €3.527,57 | €7.055,14 | €202,63 | €3,85 |
| TEST | Doge Ema 1H | 1 | €10.102,84 | €1.101,76 | €3.305,29 | €50,46 | €12,96 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 1 | €10.090,48 | €141,78 | €425,35 | €51,04 | €-18,54 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €10.074,08 | €1.220,11 | €3.660,32 | €50,47 | €-17,53 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.071,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 1 | €10.048,63 | €1.486,90 | €4.460,70 | €49,96 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 7 | €10.045,64 | €4.960,33 | €14.880,99 | €101,09 | €65,52 |
| TEST | Ampia 4H | 6 | €10.036,04 | €1.767,28 | €3.534,57 | €201,08 | €60,97 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €10.034,70 | €1.337,04 | €2.674,08 | €150,30 | €-18,26 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.034,69 | €4.199,61 | €12.598,83 | €149,89 | €14,63 |
| TEST | Btc Adaptive 1H | 1 | €10.020,48 | €1.158,94 | €3.476,83 | €50,07 | €9,29 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €10.018,01 | €2.386,15 | €7.158,46 | €148,70 | €-19,82 |
| TEST | Forza relativa 1H V2 | 4 | €10.015,98 | €2.768,37 | €5.536,73 | €155,16 | €-21,63 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.013,11 | €502,10 | €1.004,20 | €103,17 | €-18,22 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.008,47 | €2.704,17 | €5.408,34 | €199,93 | €12,19 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.007,22 | €487,53 | €975,06 | €102,62 | €-18,21 |
| TEST | Sol Donchian 4H | 1 | €10.005,46 | €830,21 | €1.660,43 | €0,00 | €57,99 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.000,84 | €761,04 | €1.522,08 | €0,00 | €53,15 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.996,42 | €1.299,56 | €3.898,68 | €49,90 | €18,14 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.990,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.979,60 | €1.494,54 | €4.483,63 | €50,22 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 7 | €9.977,73 | €4.778,27 | €14.334,80 | €149,83 | €14,01 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €9.969,22 | €207,87 | €415,74 | €49,89 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 5 | €9.966,45 | €2.739,02 | €5.478,05 | €198,53 | €-36,07 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.953,65 | €1.091,78 | €3.275,34 | €49,89 | €-21,48 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.951,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 7 | €9.948,75 | €2.599,68 | €5.199,37 | €100,20 | €31,39 |
| TEST | Btc Donchian 4H | 1 | €9.944,25 | €1.196,13 | €2.392,26 | €49,75 | €-4,99 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.938,65 | €452,98 | €905,96 | €101,06 | €-18,09 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.922,91 | €1.300,18 | €3.900,53 | €49,51 | €24,01 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.918,99 | €1.147,21 | €3.441,62 | €49,56 | €9,20 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 2 | €9.915,06 | €412,83 | €825,66 | €99,08 | €-18,05 |
| TEST | Combo Scanner | 3 | €9.914,45 | €438,70 | €877,39 | €100,43 | €-18,07 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.903,77 | €206,52 | €413,04 | €49,56 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.892,80 | €780,22 | €1.560,44 | €49,48 | €-2,57 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 7 | €9.892,65 | €2.817,91 | €8.453,74 | €98,64 | €14,94 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.886,03 | €137,56 | €412,68 | €49,52 | €-17,99 |
| TEST | 1H Fast V3 Nohigh V1 | 2 | €9.874,22 | €2.309,61 | €6.928,83 | €100,01 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.863,73 | €1.988,26 | €3.976,53 | €47,72 | €-20,08 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.848,43 | €1.267,95 | €3.803,86 | €49,17 | €16,68 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.842,81 | €2.117,13 | €4.234,26 | €150,04 | €98,96 |
| TEST | Global Confluence puro 1H | 1 | €9.833,51 | €1.428,07 | €2.856,13 | €49,20 | €-4,24 |
| TEST | Scanner Bottom10 Short | 7 | €9.820,87 | €3.359,18 | €6.718,36 | €100,19 | €30,67 |
| TEST | Scanner Bottom15 Short | 7 | €9.820,87 | €3.359,18 | €6.718,36 | €100,19 | €30,67 |
| TEST | Scanner Bottom20 Short | 7 | €9.820,87 | €3.359,18 | €6.718,36 | €100,19 | €30,67 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 1 | €9.813,54 | €194,51 | €583,53 | €49,25 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.812,08 | €1.076,25 | €3.228,75 | €49,18 | €-21,17 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.806,54 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.796,05 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 2 | €9.792,95 | €1.052,18 | €3.156,55 | €99,37 | €12,05 |
| TEST | Scanner Bottom 5 Short 1H | 7 | €9.775,26 | €2.995,81 | €5.991,63 | €50,19 | €30,92 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 2 | €9.770,94 | €2.043,62 | €4.087,25 | €100,09 | €36,90 |
| TEST | Scanner Top5 Btc Guard V1 | 2 | €9.761,07 | €405,59 | €811,17 | €97,34 | €11,91 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.757,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 4 | €9.754,29 | €6.802,28 | €13.604,57 | €169,04 | €-26,15 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.739,73 | €135,52 | €406,57 | €48,79 | €-17,73 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.738,67 | €440,31 | €880,62 | €98,85 | €36,05 |
| TEST | Scanner Top5 Btc Mfe V1 | 2 | €9.737,45 | €1.566,58 | €3.133,17 | €97,82 | €-0,08 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.730,44 | €202,72 | €405,45 | €48,65 | €-0,08 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €9.729,81 | €2.381,10 | €4.762,20 | €194,74 | €3,16 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.726,39 | €427,39 | €854,79 | €98,33 | €36,01 |
| TEST | Scanner Top10 Long | 3 | €9.705,45 | €1.598,07 | €3.196,14 | €101,35 | €-17,66 |
| TEST | Scanner Top15 Long | 3 | €9.705,45 | €1.598,07 | €3.196,14 | €101,35 | €-17,66 |
| TEST | Scanner Top20 Long | 3 | €9.705,45 | €1.598,07 | €3.196,14 | €101,35 | €-17,66 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.698,71 | €427,48 | €854,96 | €98,21 | €35,90 |
| TEST | Master Adaptive V1 | 3 | €9.694,71 | €427,40 | €854,79 | €98,19 | €35,89 |
| TEST | Combo Trend | 7 | €9.682,06 | €3.374,06 | €6.748,11 | €146,39 | €90,23 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.628,98 | €1.549,90 | €3.099,79 | €97,01 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €9.607,23 | €135,03 | €405,10 | €48,61 | €-17,66 |
| TEST | Forza relativa 1H V1 | 7 | €9.556,70 | €3.372,93 | €6.745,86 | €106,19 | €57,39 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 1 | €9.552,70 | €199,02 | €398,04 | €47,77 | €-0,08 |
| TEST | Combo Adaptive Mfe Trail | 5 | €9.551,78 | €2.468,48 | €4.936,95 | €143,18 | €15,99 |
| TEST | Master Adaptive Strict3 V1 | 2 | €9.410,39 | €2.217,67 | €4.435,35 | €97,56 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.607,10 | €-441,81 | 25 | 25 | 28,00% | 0,58 | €-17,67 | 6,36% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.564,66 | €588,53 | 54 | 54 | 42,59% | 1,52 | €10,90 | 2,20% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.555,92 | €465,66 | 59 | 59 | 44,07% | 1,45 | €7,89 | 2,49% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.515,98 | €426,16 | 22 | 22 | 54,55% | 2,38 | €19,37 | 1,96% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.505,24 | €319,85 | 32 | 32 | 53,12% | 1,37 | €10,00 | 3,09% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.497,24 | €484,78 | 46 | 46 | 47,83% | 1,47 | €10,54 | 3,91% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.438,71 | €380,90 | 53 | 53 | 47,17% | 1,40 | €7,19 | 2,49% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.415,57 | €415,97 | 60 | 60 | 46,67% | 1,35 | €6,93 | 2,83% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.395,73 | €396,49 | 18 | 18 | 66,67% | 3,42 | €22,03 | 1,39% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.389,49 | €385,73 | 38 | 38 | 63,16% | 1,81 | €10,15 | 2,51% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.364,59 | €352,90 | 36 | 36 | 44,44% | 1,46 | €9,80 | 3,23% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.328,24 | €341,43 | 41 | 41 | 60,98% | 1,69 | €8,33 | 2,05% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.327,26 | €273,27 | 18 | 18 | 66,67% | 1,79 | €15,18 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.323,87 | €266,30 | 20 | 20 | 50,00% | 2,64 | €13,32 | 2,01% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.299,20 | €311,88 | 19 | 19 | 68,42% | 2,34 | €16,41 | 1,41% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.297,10 | €265,54 | 58 | 58 | 50,00% | 1,24 | €4,58 | 3,56% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.296,85 | €297,96 | 10 | 10 | 70,00% | 2,84 | €29,80 | 1,78% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.266,65 | €260,35 | 54 | 54 | 46,30% | 1,26 | €4,82 | 2,15% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.264,58 | €233,14 | 8 | 8 | 50,00% | 2,39 | €29,14 | 1,50% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.237,04 | €47,40 | 1 | 1 | 100,00% | ∞ | €47,40 | 1,09% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.235,71 | €236,97 | 14 | 14 | 57,14% | 4,59 | €16,93 | 1,01% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.218,59 | €218,95 | 12 | 12 | 58,33% | 1,75 | €18,25 | 2,28% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.200,35 | €94,65 | 6 | 6 | 33,33% | 2,13 | €15,77 | 1,14% |
| TEST | Combo Adaptive | Combo Adaptive | €10.195,96 | €186,48 | 28 | 28 | 46,43% | 1,44 | €6,66 | 1,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.185,10 | €179,43 | 87 | 87 | 39,08% | 1,11 | €2,06 | 2,89% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.181,14 | €183,58 | 38 | 36 | 52,63% | 1,24 | €4,83 | 2,75% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.177,60 | €137,88 | 29 | 29 | 44,83% | 1,28 | €4,75 | 2,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.175,99 | €194,76 | 25 | 25 | 44,00% | 1,52 | €7,79 | 3,34% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.159,32 | €161,18 | 23 | 23 | 47,83% | 1,49 | €7,01 | 1,76% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.144,18 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,63% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.134,76 | €125,00 | 28 | 28 | 46,43% | 1,24 | €4,46 | 2,12% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.127,11 | €72,40 | 11 | 11 | 36,36% | 1,22 | €6,58 | 2,40% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.123,46 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.112,64 | €113,03 | 21 | 21 | 52,38% | 1,33 | €5,38 | 1,73% |
| TEST | Doge Ema 1H | Trend following EMA | €10.102,84 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.090,48 | €109,28 | 31 | 31 | 45,16% | 1,19 | €3,53 | 2,82% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.074,08 | €93,80 | 5 | 5 | 80,00% | 2,64 | €18,76 | 1,08% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.071,28 | €71,28 | 19 | 19 | 42,11% | 1,16 | €3,75 | 2,17% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.048,63 | €51,31 | 77 | 77 | 35,06% | 1,03 | €0,67 | 6,76% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.045,64 | €-11,16 | 9 | 9 | 33,33% | 0,94 | €-1,24 | 1,99% |
| TEST | Ampia 4H | Confluenza trend | €10.036,04 | €-23,31 | 21 | 21 | 23,81% | 0,96 | €-1,11 | 3,68% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.034,70 | €55,43 | 21 | 21 | 38,10% | 1,19 | €2,64 | 1,64% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.034,69 | €27,46 | 60 | 60 | 36,67% | 1,02 | €0,46 | 2,58% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.020,48 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €10.018,01 | €42,78 | 13 | 13 | 38,46% | 1,16 | €3,29 | 1,46% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.015,98 | €40,94 | 45 | 44 | 40,00% | 1,03 | €0,91 | 5,10% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.013,11 | €32,32 | 20 | 20 | 40,00% | 1,06 | €1,62 | 3,22% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,36 | €10,36 | 10 | 10 | 30,00% | 1,22 | €1,04 | 0,25% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.008,47 | €-0,10 | 14 | 14 | 35,71% | 1,00 | €-0,01 | 2,34% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.007,22 | €26,39 | 24 | 24 | 41,67% | 1,04 | €1,10 | 3,44% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.005,46 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,79% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,07 | €2,07 | 10 | 10 | 30,00% | 1,22 | €0,21 | 0,05% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,84 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,77% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,42 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.990,65 | €-9,35 | 14 | 14 | 42,86% | 0,97 | €-0,67 | 2,46% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.979,60 | €-17,71 | 16 | 14 | 43,75% | 0,95 | €-1,11 | 1,69% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.977,73 | €-27,83 | 61 | 61 | 39,34% | 0,98 | €-0,46 | 2,49% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.969,22 | €-30,15 | 9 | 9 | 33,33% | 0,87 | €-3,35 | 2,84% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.966,45 | €5,91 | 10 | 10 | 70,00% | 1,04 | €0,59 | 1,38% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Sol Ema 1H | Trend following EMA | €9.953,65 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.951,70 | €-48,30 | 10 | 10 | 30,00% | 0,27 | €-4,83 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.948,75 | €-78,99 | 7 | 7 | 57,14% | 0,50 | €-11,28 | 1,53% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.944,25 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,02% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.938,65 | €-42,34 | 16 | 16 | 43,75% | 0,91 | €-2,65 | 3,23% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.922,91 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Btc Ema 1H | Trend following EMA | €9.918,99 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.915,06 | €-66,02 | 15 | 15 | 40,00% | 0,87 | €-4,40 | 3,38% |
| TEST | Combo Scanner | Combo Scanner | €9.914,45 | €-66,57 | 43 | 43 | 41,86% | 0,94 | €-1,55 | 3,25% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,77 | €-95,76 | 21 | 21 | 47,62% | 0,79 | €-4,56 | 2,18% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Sol Ema 4H | Trend following EMA | €9.892,80 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,10% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.892,65 | €-117,37 | 24 | 24 | 45,83% | 0,77 | €-4,89 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.886,03 | €-95,73 | 26 | 26 | 38,46% | 0,83 | €-3,68 | 3,33% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.874,22 | €-121,63 | 59 | 59 | 38,98% | 0,91 | €-2,06 | 2,96% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.863,73 | €-113,80 | 19 | 19 | 36,84% | 0,82 | €-5,99 | 3,60% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.848,43 | €-165,97 | 3 | 3 | 0,00% | 0,00 | €-55,32 | 1,82% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.842,81 | €-252,96 | 32 | 32 | 34,38% | 0,69 | €-7,91 | 3,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.833,51 | €-160,53 | 11 | 11 | 36,36% | 0,52 | €-14,59 | 2,92% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.820,87 | €-205,24 | 8 | 8 | 37,50% | 0,26 | €-25,65 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.820,87 | €-205,24 | 8 | 8 | 37,50% | 0,26 | €-25,65 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.820,87 | €-205,24 | 8 | 8 | 37,50% | 0,26 | €-25,65 | 2,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.813,54 | €-186,11 | 22 | 22 | 40,91% | 0,63 | €-8,46 | 2,93% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.812,08 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,61% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.806,54 | €-191,77 | 21 | 21 | 19,05% | 0,67 | €-9,13 | 3,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.796,05 | €-202,30 | 16 | 16 | 31,25% | 0,62 | €-12,64 | 2,89% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.792,95 | €-217,20 | 15 | 15 | 33,33% | 0,59 | €-14,48 | 2,95% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.775,26 | €-248,55 | 31 | 31 | 35,48% | 0,67 | €-8,02 | 5,48% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.770,94 | €-263,40 | 17 | 17 | 23,53% | 0,60 | €-15,49 | 3,74% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.761,07 | €-249,98 | 21 | 21 | 28,57% | 0,64 | €-11,90 | 3,65% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.757,70 | €-242,30 | 6 | 6 | 0,00% | 0,00 | €-40,38 | 2,42% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.754,29 | €-211,40 | 46 | 46 | 39,13% | 0,83 | €-4,60 | 5,30% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.739,73 | €-242,30 | 6 | 6 | 0,00% | 0,00 | €-40,38 | 2,69% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.738,67 | €-296,38 | 19 | 19 | 31,58% | 0,62 | €-15,60 | 3,64% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.737,45 | €-260,59 | 29 | 29 | 37,93% | 0,57 | €-8,99 | 3,95% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.730,44 | €-269,23 | 31 | 31 | 38,71% | 0,68 | €-8,68 | 3,93% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.729,81 | €-269,71 | 26 | 26 | 46,15% | 0,56 | €-10,37 | 3,32% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.726,39 | €-308,63 | 18 | 18 | 27,78% | 0,57 | €-17,15 | 3,98% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.705,45 | €-274,96 | 16 | 16 | 37,50% | 0,47 | €-17,18 | 4,75% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.705,45 | €-274,96 | 16 | 16 | 37,50% | 0,47 | €-17,18 | 4,75% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.705,45 | €-274,96 | 16 | 16 | 37,50% | 0,47 | €-17,18 | 4,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.698,71 | €-336,21 | 16 | 16 | 25,00% | 0,53 | €-21,01 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.694,71 | €-340,19 | 16 | 16 | 25,00% | 0,53 | €-21,26 | 4,07% |
| TEST | Combo Trend | Combo Trend | €9.682,06 | €-403,86 | 47 | 47 | 34,04% | 0,75 | €-8,59 | 7,02% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.628,98 | €-369,16 | 52 | 52 | 57,69% | 0,60 | €-7,10 | 4,27% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.607,23 | €-374,86 | 51 | 51 | 31,37% | 0,71 | €-7,35 | 4,91% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.556,70 | €-496,80 | 36 | 36 | 25,00% | 0,54 | €-13,80 | 7,55% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.552,70 | €-446,98 | 38 | 38 | 36,84% | 0,57 | €-11,76 | 5,08% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.551,78 | €-461,15 | 37 | 37 | 32,43% | 0,48 | €-12,46 | 5,33% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.410,39 | €-586,95 | 25 | 25 | 24,00% | 0,49 | €-23,48 | 6,09% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 56,30800 | 59,33830 | 76,08234 | 53,15302 | €419,05 | €1.257,15 | €45,25 | €21,26 |
| Principale 4H | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00412 | 0,00442 | 0,00412 | 0,00276 | 0,00510 | €128,49 | €385,48 | €0,00 | €28,65 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 73,31100 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €-0,05 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 483,74323 | 478,27000 | 481,86559 | 642,57226 | 461,39195 | €17,56 | €52,68 | €0,00 | €0,60 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 57,07858 | 56,30800 | 56,70908 | 75,81938 | 54,73013 | €786,25 | €2.358,74 | €0,00 | €31,84 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63620,87328 | 63450,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.153,42 | €3.460,26 | €49,83 | €9,25 |
| Bilanciata 1H V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 72,83343 | 73,31100 | 73,94273 | 96,74707 | 70,61483 | €70,54 | €211,63 | €3,22 | €-1,39 |
| 1H Balanced Long No Rhv V1 | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00430 | 0,00442 | 0,00378 | 0,00289 | 0,00533 | €136,92 | €410,76 | €49,29 | €12,05 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 488,51228 | 478,27000 | 481,68165 | 648,90714 | 465,56407 | €24,50 | €73,51 | €0,00 | €1,54 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,95646 | 98,25841 | 71,73999 | €39,75 | €119,24 | €0,00 | €1,06 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63953,88094 | 83746,12761 | 61230,29295 | €1.219,33 | €3.657,98 | €52,67 | €-23,49 |
| Rapida 1H V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| 1H Fast Score 6 75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €972,21 | €2.916,64 | €0,00 | €33,00 |
| 1H Fast Score 6 75 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.094,57 | €3.283,72 | €0,00 | €23,49 |
| 1H Fast Score 6 75 V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €1.496,78 | €4.490,35 | €0,00 | €40,08 |
| 1H Fast Score 6 75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63747,34798 | 63450,80000 | 63562,15308 | 84677,72723 | 62676,39253 | €30,97 | €92,90 | €0,00 | €0,43 |
| 1H Fast Score 6 75 V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,68319 | 0,68350 | 0,69289 | 0,90750 | 0,66864 | €37,40 | €112,21 | €1,59 | €-0,05 |
| 1H Fast Score 6 75 No Trend Up V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €961,25 | €2.883,74 | €0,00 | €32,63 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.083,98 | €3.251,95 | €0,00 | €23,26 |
| 1H Fast Score 6 75 No Trend Up V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €103,21 | €309,64 | €0,00 | €2,76 |
| 1H Fast Score 6 75 No Trend Up V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61986,84517 | €30,09 | €90,27 | €1,01 | €-0,58 |
| 1H Fast Score 6 75 Range Only V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €968,54 | €2.905,63 | €0,00 | €32,88 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.090,44 | €3.271,33 | €0,00 | €23,40 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €1.491,13 | €4.473,40 | €0,00 | €39,93 |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63747,34798 | 63450,80000 | 63562,15308 | 84677,72723 | 62676,39253 | €35,76 | €107,29 | €0,00 | €0,50 |
| 1H Fast Score 6 75 Cost Aware V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06998 | 0,07008 | 0,07082 | 0,09295 | 0,06871 | €43,95 | €131,85 | €1,59 | €-0,20 |
| 1H Fast Nohigh Cap75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| 1H Fast No Pepe V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| 1H Fast No Pepe V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €28,82 | €86,46 | €0,00 | €0,98 |
| 1H Fast No Pepe V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.064,33 | €3.192,99 | €0,00 | €22,84 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63620,87328 | 63450,80000 | 64333,42706 | 84509,72667 | 62552,04261 | €19,21 | €57,62 | €0,65 | €0,15 |
| 1H Fast No Pepe V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €8,54 | €25,63 | €0,32 | €-0,04 |
| 1H Fast No Pepe V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03914 | €9,88 | €29,65 | €0,33 | €-0,06 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06871 | €1.435,95 | €4.307,84 | €50,18 | €-8,87 |
| 1H Fast Tp2 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| 1H Fast Tp2 V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| 1H Fast Tp2 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| 1H Fast Tp2 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €27,61 | €82,84 | €0,00 | €0,94 |
| 1H Fast Tp2 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.039,45 | €3.118,34 | €0,00 | €22,30 |
| 1H Fast Tp2 V1 | NEAR | SHORT | Momentum / breakout | 60m | 3,0x | 1,67599 | 1,67599 | 1,70517 | 2,22628 | 1,61763 | €25,97 | €77,91 | €1,36 | €-0,00 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06831 | €1.394,41 | €4.183,24 | €48,73 | €-8,61 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €27,86 | €83,58 | €0,00 | €0,95 |
| Rapida 1H V3 Filtered | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.037,92 | €3.113,75 | €0,00 | €22,27 |
| Rapida 1H V3 Filtered | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €8,54 | €25,62 | €0,32 | €-0,04 |
| Rapida 1H V3 Filtered | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03914 | €9,49 | €28,48 | €0,32 | €-0,06 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06871 | €1.429,19 | €4.287,56 | €49,95 | €-8,83 |
| 1H Fast V3 Cap75 V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €30,24 | €90,72 | €0,00 | €1,03 |
| 1H Fast V3 Cap75 V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.087,88 | €3.263,64 | €0,00 | €23,34 |
| 1H Fast V3 Cap75 V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €1.494,31 | €4.482,92 | €0,00 | €40,01 |
| 1H Fast V3 Cap75 V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61986,84517 | €54,22 | €162,67 | €1,82 | €-1,04 |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,91758 | 2,91933 | 3,26769 | 3,87552 | 2,39241 | €135,27 | €405,82 | €48,70 | €-0,24 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| 1H Fast V3 Nohigh V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00546 | €135,03 | €405,10 | €48,61 | €-17,66 |
| 1H Fast V3 No Esports V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| 1H Fast V3 No Esports V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| 1H Fast V3 No Esports V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €27,30 | €81,91 | €0,00 | €0,93 |
| 1H Fast V3 No Esports V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.017,33 | €3.051,98 | €0,00 | €21,83 |
| 1H Fast V3 No Esports V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €8,36 | €25,09 | €0,31 | €-0,04 |
| 1H Fast V3 No Esports V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03914 | €9,31 | €27,93 | €0,31 | €-0,06 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06871 | €1.400,09 | €4.200,28 | €48,93 | €-8,65 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00546 | €141,78 | €425,35 | €51,04 | €-18,54 |
| 1H Fast V3 No Esports Mfe Lock V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63620,87328 | 63450,80000 | 63620,87328 | 84509,72667 | 62552,04261 | €1.511,01 | €4.533,03 | €0,00 | €12,12 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00546 | €143,94 | €431,82 | €51,82 | €-18,83 |
| 1H Fast V3 No Esports Mfe Lock V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €13,72 | €41,16 | €0,51 | €-0,07 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,07018 | 0,07008 | 0,07099 | 0,09322 | 0,06895 | €37,48 | €112,45 | €1,31 | €0,15 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 56,30800 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €29,92 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00412 | 0,00442 | 0,00362 | 0,00208 | 0,00550 | €208,53 | €417,05 | €50,05 | €31,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,05906 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €0,13 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63318,66373 | 63450,80000 | 64874,97444 | 94661,40228 | 58960,99415 | €18,28 | €36,56 | €0,90 | €-0,08 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 483,74323 | 478,27000 | 482,47314 | 723,19613 | 459,15682 | €1.028,52 | €2.057,03 | €0,00 | €23,27 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 57,27654 | 56,30800 | 56,68219 | 85,62843 | 54,89695 | €1.014,19 | €2.028,38 | €0,00 | €34,30 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,05518 | 1,05906 | 1,07037 | 1,57749 | 1,02175 | €24,53 | €49,07 | €0,71 | €-0,18 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 477,51448 | 478,27000 | 488,76646 | 713,88414 | 452,76011 | €1.065,11 | €2.130,22 | €50,20 | €-3,37 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €209,44 | €418,88 | €50,27 | €-18,26 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 56,30800 | 56,67469 | 87,09174 | 55,41491 | €1.364,10 | €2.728,20 | €0,00 | €91,20 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,05906 | 1,06529 | 1,62864 | 1,04582 | €1.662,45 | €3.324,89 | €0,00 | €92,58 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 478,27000 | 496,16061 | 723,19613 | 452,69979 | €19,59 | €39,18 | €1,01 | €0,44 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63620,87328 | 63450,80000 | 64638,80725 | 95113,20555 | 61076,03835 | €1.401,20 | €2.802,39 | €44,84 | €7,49 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 72,83343 | 73,31100 | 74,06598 | 108,88598 | 69,75205 | €39,01 | €78,03 | €1,32 | €-0,51 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 56,30800 | 56,67469 | 87,09174 | 55,41491 | €1.281,83 | €2.563,66 | €0,00 | €85,70 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,05906 | 1,06529 | 1,62864 | 1,04582 | €1.562,18 | €3.124,36 | €0,00 | €86,99 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 478,27000 | 496,16061 | 723,19613 | 452,69979 | €978,17 | €1.956,34 | €50,22 | €22,13 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63046,01827 | 63450,80000 | 64054,75457 | 94253,79732 | 60524,17754 | €69,70 | €139,41 | €2,23 | €-0,90 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 63772,85202 | 63450,80000 | 63007,57780 | 32205,29027 | 64920,76336 | €1.981,46 | €3.962,93 | €47,56 | €-20,01 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,06582 | 1,05906 | 1,05303 | 0,53824 | 1,08501 | €1.980,83 | €3.961,66 | €47,54 | €-25,14 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06977 | 0,07008 | 0,06887 | 0,03524 | 0,07113 | €1.881,64 | €3.763,27 | €48,65 | €16,51 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,21564 | 73,31100 | 72,24942 | 36,97390 | 74,66497 | €958,36 | €1.916,71 | €25,29 | €2,50 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,09230 | 1,05906 | 1,06496 | 1,63299 | 1,05385 | €1.438,76 | €2.877,52 | €0,00 | €87,57 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €202,78 | €405,56 | €48,67 | €11,89 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,67450 | 0,68350 | 0,68819 | 1,00837 | 0,64436 | €18,93 | €37,85 | €0,77 | €-0,51 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €218,43 | €436,86 | €52,42 | €12,81 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,93 | €37,87 | €0,00 | €0,43 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.150,85 | €2.301,70 | €0,00 | €31,07 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,90 | €43,79 | €0,80 | €-0,58 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €202,57 | €405,14 | €48,62 | €-17,66 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,00 | €0,42 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €0,00 | €30,82 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,58 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €202,57 | €405,14 | €48,62 | €-17,66 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,00 | €0,42 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €0,00 | €30,82 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,58 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €202,57 | €405,14 | €48,62 | €-17,66 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,00 | €0,42 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €0,00 | €30,82 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,58 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €215,67 | €431,34 | €51,76 | €12,65 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00559 | €202,87 | €405,74 | €48,69 | €-0,08 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €203,11 | €406,23 | €48,75 | €11,91 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €207,48 | €414,96 | €49,80 | €-18,09 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00559 | €199,02 | €398,04 | €47,77 | €-0,08 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €206,99 | €413,98 | €49,68 | €-18,05 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00559 | €202,72 | €405,45 | €48,65 | €-0,08 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00629 | €208,87 | €417,74 | €50,13 | €-18,21 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00629 | €208,99 | €417,98 | €50,16 | €-18,22 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06998 | 0,07008 | 0,07118 | 0,10461 | 0,06696 | €1.428,07 | €2.856,13 | €49,20 | €-4,24 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,09094 | 1,05906 | 1,06516 | 1,63096 | 1,05254 | €1.454,27 | €2.908,55 | €0,00 | €85,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €183,87 | €367,73 | €44,13 | €10,78 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,68350 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,71 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63046,01827 | 63450,80000 | 64054,75457 | 94253,79732 | 60826,79843 | €59,43 | €118,86 | €1,90 | €-0,76 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06998 | 0,07008 | 0,07118 | 0,10461 | 0,06732 | €1.373,53 | €2.747,07 | €47,32 | €-4,08 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63772,85202 | 63450,80000 | 63007,57780 | 32205,29027 | 64997,29078 | €1.988,26 | €3.976,53 | €47,72 | €-20,08 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €207,27 | €414,53 | €49,74 | €-18,07 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 56,91461 | 56,30800 | 56,70720 | 85,08735 | 54,57291 | €13,99 | €27,97 | €0,00 | €0,30 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €208,31 | €416,62 | €49,99 | €12,22 |
| Combo Adaptive | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive Mfe Trail | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive Mfe Trail | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 56,71366 | 56,30800 | 56,71366 | 84,78691 | 54,39073 | €1.168,54 | €2.337,08 | €0,00 | €16,72 |
| Combo Adaptive Mfe Trail | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €24,23 | €48,47 | €0,89 | €-0,65 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00548 | €190,23 | €380,45 | €45,65 | €-0,08 |
| Combo Adaptive Quality7 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive Quality7 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €209,44 | €418,88 | €50,27 | €-18,26 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive Long Only V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive Long Only V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €207,92 | €415,84 | €49,90 | €12,19 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Partial 1R V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €71,80 | €143,60 | €17,23 | €4,21 |
| Combo Adaptive Partial 1R V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €12,97 | €25,95 | €0,47 | €-0,35 |
| Combo Adaptive Partial 1R V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,05724 | 1,05906 | 1,07246 | 1,58057 | 1,02679 | €204,10 | €408,19 | €5,88 | €-0,70 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive Runner25 V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 488,51228 | 478,27000 | 481,06439 | 730,32586 | 454,08996 | €32,69 | €65,39 | €0,00 | €1,37 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00584 | €205,49 | €410,98 | €49,32 | €12,05 |
| Combo Adaptive Runner25 V1 | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive Tp3 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive Tp3 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 63620,87328 | 63450,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.147,21 | €3.441,62 | €49,56 | €9,20 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63747,34798 | 63450,80000 | 64563,31403 | 84677,72723 | 62115,41587 | €1.299,56 | €3.898,68 | €49,90 | €18,14 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63318,66373 | 63450,80000 | 64635,54187 | 94661,40228 | 59631,40456 | €1.196,13 | €2.392,26 | €49,75 | €-4,99 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 63772,85202 | 63450,80000 | 63007,57780 | 42834,09894 | 64920,76336 | €1.412,24 | €4.236,72 | €50,84 | €-21,40 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63620,87328 | 63450,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.158,94 | €3.476,83 | €50,07 | €9,29 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 72,83343 | 73,31100 | 73,94273 | 96,74707 | 70,61483 | €1.091,78 | €3.275,34 | €49,89 | €-21,48 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 73,31100 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-2,57 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 73,97120 | 73,31100 | 73,83397 | 98,25841 | 71,98791 | €1.254,69 | €3.764,07 | €0,00 | €33,59 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 73,31100 | 74,54202 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €0,00 | €57,99 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 72,86257 | 73,31100 | 71,93778 | 48,93936 | 74,24975 | €1.300,18 | €3.900,53 | €49,51 | €24,01 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 72,83343 | 73,31100 | 73,94273 | 96,74707 | 70,61483 | €1.076,25 | €3.228,75 | €49,18 | €-21,17 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 73,31100 | 74,59202 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €0,00 | €53,15 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07036 | 0,07008 | 0,07143 | 0,09346 | 0,06821 | €1.101,76 | €3.305,29 | €50,46 | €12,96 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06975 | 0,07008 | 0,07071 | 0,09265 | 0,06782 | €1.220,11 | €3.660,32 | €50,47 | €-17,53 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06977 | 0,07008 | 0,06887 | 0,04686 | 0,07113 | €1.267,95 | €3.803,86 | €49,17 | €16,68 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00504 | €202,05 | €404,11 | €48,49 | €35,89 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00504 | €202,14 | €404,28 | €48,51 | €35,90 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00504 | €202,97 | €405,94 | €48,71 | €36,05 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00552 | €202,72 | €405,45 | €48,65 | €36,01 |
| Combo Adaptive Side Regime Guard V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 483,74323 | 478,27000 | 481,25805 | 723,19613 | 461,39195 | €34,68 | €69,35 | €0,00 | €0,78 |
| Combo Adaptive Side Regime Guard V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 57,22855 | 56,30800 | 56,60840 | 85,55669 | 54,94411 | €29,04 | €58,08 | €0,00 | €0,93 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07038 | 0,07008 | 0,07031 | 0,10521 | 0,06823 | €1.664,07 | €3.328,14 | €0,00 | €13,99 |
| Combo Adaptive Side Regime Guard V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63046,01827 | 63450,80000 | 63953,88094 | 94253,79732 | 61230,29295 | €1.798,90 | €3.597,79 | €51,81 | €-23,10 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €36,90 |
| 1H Fast V3 Nohigh Range Only V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 56,30800 | 59,33830 | 76,08234 | 53,15302 | €471,26 | €1.413,79 | €50,89 | €23,91 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00412 | 0,00442 | 0,00412 | 0,00276 | 0,00510 | €140,35 | €421,05 | €0,00 | €31,30 |
| Main Side Regime Guard V1 | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,07008 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €2,06 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00412 | 0,00442 | 0,00412 | 0,00276 | 0,00510 | €142,13 | €426,38 | €0,00 | €31,69 |
| Combo Trend Side Regime Guard V1 | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ZEC | SHORT | Combo Trend | 60m | 2,0x | 477,71444 | 478,27000 | 490,38685 | 714,18308 | 449,83512 | €19,75 | €39,50 | €1,05 | €-0,05 |
| Combo Trend Side Regime Guard V1 | BTC | SHORT | Combo Trend | 60m | 2,0x | 63620,87328 | 63450,80000 | 64638,80725 | 95113,20555 | 61381,41854 | €1.578,90 | €3.157,81 | €50,52 | €8,44 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,06427 | 1,05906 | 1,08130 | 1,59108 | 1,02680 | €32,70 | €65,39 | €1,05 | €0,32 |
| Combo Trend Side Regime Guard V1 | SOL | SHORT | Combo Trend | 60m | 2,0x | 72,83343 | 73,31100 | 74,06598 | 108,88598 | 70,12181 | €45,02 | €90,04 | €1,52 | €-0,59 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06998 | 0,07008 | 0,07118 | 0,10461 | 0,06732 | €1.439,06 | €2.878,12 | €49,58 | €-4,28 |
| 1H Fast Nohigh Cap75 Short Only V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| 1H Balanced V3 Long Only V1 | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| 1H Balanced V3 Long Only V1 | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 488,51228 | 478,27000 | 481,68165 | 648,90714 | 465,56407 | €14,72 | €44,15 | €0,00 | €0,93 |
| 1H Balanced V3 Long Only V1 | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,95646 | 98,25841 | 71,73999 | €36,55 | €109,64 | €0,00 | €0,98 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63953,88094 | 83746,12761 | 61230,29295 | €1.127,91 | €3.383,73 | €48,73 | €-21,72 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,50810 | 723,19613 | 461,39195 | €19,22 | €38,45 | €0,00 | €0,44 |
| Scanner Bottom5 Short Profit Lock V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.168,54 | €2.337,08 | €0,00 | €31,55 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €22,23 | €44,47 | €0,81 | €-0,59 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €15,45 | €30,90 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €1.350,73 | €2.701,46 | €49,38 | €-36,07 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 462,01282 | €927,74 | €2.783,21 | €0,00 | €31,49 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07858 | 56,30800 | 56,56934 | 75,81938 | 54,79537 | €1.027,90 | €3.083,70 | €0,00 | €41,63 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 71,80197 | €1.442,22 | €4.326,65 | €0,00 | €38,62 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63747,34798 | 63450,80000 | 63562,15308 | 84677,72723 | 61962,42224 | €84,44 | €253,33 | €0,00 | €1,18 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05948 | 1,05906 | 1,07134 | 1,40734 | 1,02981 | €1.444,58 | €4.333,74 | €48,54 | €1,71 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,68319 | 0,68350 | 0,69289 | 0,90750 | 0,65893 | €87,71 | €263,14 | €3,74 | €-0,12 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €43,20 | €129,60 | €0,00 | €1,47 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.034,08 | €3.102,24 | €0,00 | €22,19 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,38347 | €8,38 | €25,15 | €0,31 | €-0,04 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03322 | €9,61 | €28,84 | €0,32 | €-0,06 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06831 | €1.395,23 | €4.185,70 | €48,76 | €-8,62 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €939,82 | €2.819,46 | €0,00 | €31,90 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.054,69 | €3.164,08 | €0,00 | €22,63 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,23582 | €21,56 | €64,67 | €0,00 | €0,58 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,06424 | 1,05906 | 1,07616 | 1,41366 | 1,04040 | €82,60 | €247,81 | €2,78 | €1,21 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61633,78746 | €68,64 | €205,91 | €2,31 | €-1,32 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06831 | €1.410,51 | €4.231,54 | €49,29 | €-8,71 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 462,01282 | €919,87 | €2.759,61 | €0,00 | €31,22 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07858 | 56,30800 | 56,56934 | 75,81938 | 54,79537 | €1.012,65 | €3.037,94 | €0,00 | €41,01 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 71,80197 | €78,41 | €235,23 | €0,00 | €2,10 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61280,72976 | €90,53 | €271,58 | €3,04 | €-1,74 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05948 | 1,05906 | 1,07134 | 1,40734 | 1,02981 | €1.431,80 | €4.295,40 | €48,11 | €1,69 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,68319 | 0,68350 | 0,69289 | 0,90750 | 0,65893 | €8,84 | €26,52 | €0,38 | €-0,01 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06790 | €1.418,23 | €4.254,70 | €49,56 | €-8,76 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,06424 | 1,05906 | 1,06424 | 1,41366 | 1,04040 | €1.539,70 | €4.619,09 | €0,00 | €22,47 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63620,87328 | 63450,80000 | 63620,87328 | 84509,72667 | 62195,76572 | €58,03 | €174,10 | €0,00 | €0,47 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | NEAR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,66900 | 1,66900 | 1,69806 | 2,21699 | 1,61088 | €52,00 | €156,00 | €2,72 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00573 | €144,80 | €434,39 | €52,13 | €-18,94 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,07018 | 0,07008 | 0,07099 | 0,09322 | 0,06854 | €1.466,24 | €4.398,72 | €51,24 | €6,02 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00573 | €137,56 | €412,68 | €49,52 | €-17,99 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00573 | €141,59 | €424,78 | €50,97 | €-18,52 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €46,24 | €138,72 | €0,00 | €1,57 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.073,18 | €3.219,54 | €0,00 | €23,03 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,23582 | €1.460,75 | €4.382,26 | €0,00 | €39,11 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61633,78746 | €49,42 | €148,27 | €1,66 | €-0,95 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00601 | €135,52 | €406,57 | €48,79 | €-17,73 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,57 | -0,01 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,56 | -0,01 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,57 | -0,01 | STOP |
| Master Adaptive Gb20 Partial V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-77,67 | -1,55 | STOP_GAP_STRESS |
| Master Adaptive Gb20 Loss Cap V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-103,62 | -2,07 | STOP_GAP_STRESS |
| Master Adaptive Gb20 Be V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-77,75 | -1,55 | STOP_GAP_STRESS |
| Combo Adaptive Mfe Trail | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,54 | -0,01 | STOP |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-99,59 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Long Only V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-97,66 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Long Nohigh Cap75 V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-98,73 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-98,14 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-103,59 | -1,99 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
