# Paper trading automatico KuCoin

Generato: 2026-07-23T07:38:17+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-23T07:34:49+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-23T07:34:49+00:00 | 2026-07-23T07:34:49+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-23T07:15:00+00:00 | 2026-07-23T07:15:00+00:00 | 4,9 min | 25,0 min | OK |
| 60m | 12 | 2026-07-23T06:00:00+00:00 | 2026-07-23T06:00:00+00:00 | 34,9 min | 45,0 min | OK |
| 240m | 12 | 2026-07-23T00:00:00+00:00 | 2026-07-23T00:00:00+00:00 | 3,58 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | 240m | SHORT | -8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,29 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,29 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,05 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -3,90 | 6,00 | 2,10 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 3,03 | 6,00 | 2,97 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,67 | 6,00 | 4,33 | STALE_CANDLE | 3,58 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,04 | 6,00 | 4,96 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,25 | 6,00 | 5,75 | STALE_CANDLE | 3,58 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | DOGE | 60m | SHORT | -5,51 | 5,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| 1H Fast Nohigh Cap75 V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| 1H Fast No Pepe V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| 1H Fast Tp2 V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| Rapida 1H V2 | DOGE | 60m | SHORT | -5,51 | 5,00 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | DOGE | 60m | SHORT | -5,51 | 4,00 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.06%. |
| Rapida 1H V1 | BANK | 60m | LONG | 5,50 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.33%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.922,84 | -0,77% | €-77,16 | €3.000,00 | -2,57% | 4 | 17 | 29,41% | 0,73 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 17 | 365 | CAMPIONE INSUFFICIENTE | 30 (mancano 13) |

- Trade del Principale 4H chiusi: **17**; win rate **29,41%**; profit factor **0,73**.
- Expectancy: **€-8,97** per trade; P&L netto: **€-152,45**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.922,84 | €1.512,92 | €4.538,75 | €147,66 | €74,39 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.495,82 | €1.266,43 | €2.532,86 | €157,89 | €-16,69 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.376,32 | €2.729,95 | €5.459,91 | €156,45 | €-37,34 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.283,86 | €2.235,58 | €6.706,75 | €154,42 | €7,79 |
| TEST | Combo Adaptive | 3 | €10.218,64 | €2.169,96 | €4.339,92 | €153,94 | €-18,85 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.167,63 | €3.555,00 | €7.109,99 | €152,79 | €13,39 |
| TEST | Bilanciata 1H V1 | 4 | €10.129,42 | €3.258,29 | €9.774,87 | €203,95 | €-75,43 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.114,88 | €1.299,75 | €2.599,50 | €50,41 | €0,54 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.085,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.062,38 | €1.816,61 | €3.633,23 | €148,54 | €7,12 |
| TEST | Ampia 4H | 4 | €10.053,65 | €2.235,83 | €4.471,66 | €201,27 | €-33,05 |
| TEST | Btc Bollinger 4H | 1 | €10.043,49 | €1.313,84 | €2.627,69 | €50,00 | €46,82 |
| TEST | Sol Bollinger 4H | 1 | €10.032,03 | €968,56 | €1.937,11 | €50,00 | €33,51 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.014,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.009,38 | €1.825,85 | €5.477,55 | €149,54 | €8,13 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.005,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.002,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.001,68 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| TEST | Btc Donchian 4H | 1 | €10.001,68 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.997,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 3 | €9.989,20 | €2.120,81 | €6.362,43 | €148,99 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.981,09 | €883,93 | €1.767,86 | €50,00 | €-17,47 |
| TEST | Btc Adaptive 4H | 1 | €9.976,47 | €1.047,40 | €2.094,81 | €50,00 | €-24,37 |
| TEST | Sol Ema 1H | 1 | €9.971,52 | €1.001,44 | €3.004,32 | €49,95 | €-17,91 |
| TEST | Sol Adaptive 4H | 1 | €9.970,74 | €807,13 | €1.614,26 | €50,00 | €-28,56 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.968,08 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| TEST | Sol Donchian 4H | 1 | €9.968,08 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €9.965,64 | €1.277,26 | €2.554,51 | €149,85 | €-15,84 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €9.965,64 | €1.277,26 | €2.554,51 | €149,85 | €-15,84 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.962,24 | €1.000,51 | €3.001,52 | €49,91 | €-17,90 |
| TEST | 1H Fast No Pepe V1 | 4 | €9.960,83 | €2.745,37 | €8.236,12 | €199,36 | €-9,35 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.959,10 | €2.827,84 | €5.655,68 | €150,04 | €-42,32 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €9.959,10 | €2.827,84 | €5.655,68 | €150,04 | €-42,32 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.945,89 | €2.339,93 | €4.679,86 | €149,52 | €-16,14 |
| TEST | Rapida 1H V2 | 0 | €9.944,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.937,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.934,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €9.930,22 | €2.556,00 | €5.111,99 | €149,56 | €18,45 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.929,69 | €2.181,37 | €4.362,74 | €149,06 | €-15,61 |
| TEST | Combo Trend | 3 | €9.927,44 | €1.698,61 | €3.397,22 | €100,04 | €-21,21 |
| TEST | Eth Adaptive 1H | 1 | €9.918,67 | €1.153,05 | €3.459,15 | €49,81 | €-41,66 |
| TEST | Forza relativa 1H V1 | 4 | €9.909,58 | €2.404,07 | €4.808,14 | €148,58 | €-15,15 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.901,53 | €2.075,49 | €4.150,97 | €148,31 | €-12,61 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.899,64 | €1.968,07 | €3.936,13 | €99,06 | €3,30 |
| TEST | 1H Fast V3 Cap75 V1 | 1 | €9.898,20 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.898,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 0 | €9.897,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 3 | €9.891,20 | €2.783,21 | €5.566,43 | €149,21 | €-13,69 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.883,55 | €3.243,15 | €6.486,31 | €149,32 | €-24,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €9.870,01 | €954,90 | €2.864,70 | €99,67 | €-12,31 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.864,02 | €1.282,24 | €2.564,48 | €148,09 | €-15,68 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.854,44 | €1.099,22 | €2.198,44 | €98,72 | €-11,51 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.850,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.850,17 | €1.144,65 | €3.433,94 | €49,45 | €-37,29 |
| TEST | 1H Fast V3 No Esports V1 | 1 | €9.845,03 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.841,37 | €1.973,66 | €3.947,32 | €99,07 | €3,30 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €9.841,37 | €1.973,66 | €3.947,32 | €99,07 | €3,30 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.835,08 | €1.280,52 | €2.561,03 | €147,68 | €14,08 |
| TEST | 1H Fast Tp2 V1 | 2 | €9.830,72 | €849,53 | €2.548,60 | €98,95 | €22,70 |
| TEST | 1H Fast Nohigh Cap75 V1 | 2 | €9.823,11 | €840,90 | €2.522,69 | €98,32 | €22,69 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.818,47 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.802,24 | €2.227,72 | €4.455,45 | €147,21 | €-20,25 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.802,01 | €2.141,01 | €4.282,03 | €147,68 | €-7,58 |
| TEST | Global Confluence puro 1H | 1 | €9.776,79 | €1.527,19 | €3.054,37 | €48,87 | €4,03 |
| TEST | Master Adaptive V1 | 3 | €9.756,37 | €2.731,68 | €5.463,37 | €146,91 | €-23,00 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.756,37 | €2.731,68 | €5.463,37 | €146,91 | €-23,00 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.756,37 | €2.731,68 | €5.463,37 | €146,91 | €-23,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.749,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 3 | €9.730,21 | €2.121,86 | €6.365,57 | €146,23 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.723,42 | €1.161,43 | €2.322,87 | €146,28 | €13,92 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.721,27 | €2.430,51 | €4.861,03 | €97,11 | €10,24 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.706,39 | €2.826,24 | €5.652,48 | €147,55 | €-13,03 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.702,66 | €1.161,08 | €2.322,16 | €146,20 | €-15,43 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.672,31 | €1.258,76 | €2.517,53 | €146,00 | €-19,87 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.665,67 | €1.149,02 | €2.298,05 | €96,76 | €-15,54 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.922,84 | €-152,45 | 17 | 17 | 29,41% | 0,73 | €-8,97 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.495,82 | €513,90 | 28 | 28 | 50,00% | 1,96 | €18,35 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.376,32 | €416,52 | 20 | 20 | 50,00% | 2,23 | €20,83 | 1,74% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.283,86 | €279,12 | 29 | 29 | 44,83% | 1,37 | €9,62 | 2,20% |
| TEST | Combo Adaptive | Combo Adaptive | €10.218,64 | €239,35 | 20 | 20 | 45,00% | 1,71 | €11,97 | 1,31% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.167,63 | €157,56 | 17 | 17 | 47,06% | 1,40 | €9,27 | 2,05% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.129,42 | €209,55 | 31 | 31 | 48,39% | 1,34 | €6,76 | 2,08% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.114,88 | €116,68 | 20 | 20 | 45,00% | 1,34 | €5,83 | 2,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.085,92 | €85,92 | 9 | 9 | 44,44% | 1,40 | €9,55 | 1,12% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.062,38 | €57,01 | 24 | 23 | 33,33% | 1,08 | €2,38 | 3,69% |
| TEST | Ampia 4H | Confluenza trend | €10.053,65 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,37% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.043,49 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,27% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.032,03 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.014,00 | €14,00 | 2 | 2 | 100,00% | ∞ | €7,00 | 0,04% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.009,38 | €4,32 | 20 | 18 | 50,00% | 1,01 | €0,22 | 2,75% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.005,24 | €5,24 | 2 | 2 | 50,00% | 10,75 | €2,62 | 0,09% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.002,80 | €2,80 | 2 | 2 | 100,00% | ∞ | €1,40 | 0,01% |
| TEST | Btc Ema 4H | Trend following EMA | €10.001,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,45% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.001,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,45% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.997,37 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,55% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.989,20 | €-7,38 | 47 | 47 | 34,04% | 0,99 | €-0,16 | 2,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,26 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Eth Ema 4H | Trend following EMA | €9.981,09 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.976,47 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,42% |
| TEST | Sol Ema 1H | Trend following EMA | €9.971,52 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 1,10% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.970,74 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Sol Ema 4H | Trend following EMA | €9.968,08 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.968,08 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.965,64 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,33% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.965,64 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,33% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.962,24 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 1,12% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €9.960,83 | €-25,94 | 17 | 17 | 29,41% | 0,93 | €-1,53 | 2,10% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.959,10 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.959,10 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.945,89 | €-35,63 | 8 | 8 | 50,00% | 0,83 | €-4,45 | 1,41% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.944,87 | €-55,13 | 5 | 4 | 20,00% | 0,56 | €-11,03 | 1,30% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.937,58 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Btc Ema 1H | Trend following EMA | €9.934,39 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.930,22 | €-85,47 | 6 | 6 | 16,67% | 0,31 | €-14,25 | 2,06% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.929,69 | €-52,14 | 15 | 15 | 33,33% | 0,88 | €-3,48 | 2,25% |
| TEST | Combo Trend | Combo Trend | €9.927,44 | €-49,58 | 17 | 17 | 29,41% | 0,90 | €-2,92 | 3,02% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.918,67 | €-37,64 | 3 | 3 | 66,67% | 0,31 | €-12,55 | 1,02% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.909,58 | €-72,58 | 22 | 22 | 27,27% | 0,83 | €-3,30 | 3,25% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.901,53 | €-83,93 | 8 | 8 | 37,50% | 0,70 | €-10,49 | 2,18% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.899,64 | €-101,74 | 3 | 3 | 33,33% | 0,05 | €-33,91 | 1,51% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.898,20 | €-100,92 | 18 | 18 | 27,78% | 0,77 | €-5,61 | 2,49% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.898,20 | €-101,80 | 19 | 19 | 26,32% | 0,77 | €-5,36 | 2,49% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.897,06 | €-102,94 | 10 | 10 | 20,00% | 0,57 | €-10,29 | 2,11% |
| TEST | Combo Scanner | Combo Scanner | €9.891,20 | €-91,73 | 21 | 21 | 38,10% | 0,85 | €-4,37 | 2,66% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.883,55 | €-89,34 | 8 | 8 | 37,50% | 0,67 | €-11,17 | 1,65% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.870,01 | €-115,93 | 4 | 4 | 0,00% | 0,00 | €-28,98 | 1,53% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.864,02 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,64% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.854,44 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.850,91 | €-149,09 | 9 | 9 | 22,22% | 0,48 | €-16,57 | 2,00% |
| TEST | Eth Ema 1H | Trend following EMA | €9.850,17 | €-110,26 | 5 | 5 | 40,00% | 0,33 | €-22,05 | 1,59% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.845,03 | €-154,08 | 19 | 19 | 26,32% | 0,69 | €-8,11 | 2,49% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.841,37 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.841,37 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.835,08 | €-177,42 | 4 | 4 | 0,00% | 0,00 | €-44,36 | 2,30% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.830,72 | €-190,85 | 17 | 17 | 23,53% | 0,60 | €-11,23 | 2,47% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.823,11 | €-198,46 | 23 | 23 | 30,43% | 0,71 | €-8,63 | 2,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.818,47 | €-180,65 | 20 | 20 | 30,00% | 0,70 | €-9,03 | 2,96% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.802,24 | €-174,68 | 6 | 6 | 16,67% | 0,34 | €-29,11 | 2,79% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.802,01 | €-187,92 | 10 | 10 | 30,00% | 0,51 | €-18,79 | 2,24% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.776,79 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,92% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.756,37 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.756,37 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.756,37 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.749,89 | €-250,11 | 9 | 9 | 33,33% | 0,25 | €-27,79 | 2,84% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.730,21 | €-266,37 | 55 | 55 | 30,91% | 0,80 | €-4,84 | 6,66% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.723,42 | €-289,21 | 7 | 7 | 0,00% | 0,00 | €-41,32 | 3,47% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.721,27 | €-286,05 | 19 | 19 | 26,32% | 0,46 | €-15,06 | 4,93% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.706,39 | €-276,43 | 5 | 5 | 0,00% | 0,00 | €-55,29 | 3,29% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.702,66 | €-280,49 | 5 | 5 | 0,00% | 0,00 | €-56,10 | 3,31% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.672,31 | €-306,25 | 10 | 10 | 20,00% | 0,10 | €-30,62 | 3,84% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.665,67 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07228 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €15,02 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,15250 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €59,37 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 514,40710 | 514,72000 | 526,37866 | 683,30410 | 490,46397 | €731,22 | €2.193,66 | €51,05 | €-1,33 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1937,36740 | 1914,53000 | 1909,46931 | 1301,26510 | 1993,16358 | €1.184,41 | €3.553,24 | €51,17 | €-41,89 |
| Bilanciata 1H V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,17542 | 0,17294 | 0,17150 | 0,11782 | 0,18325 | €760,90 | €2.282,69 | €50,95 | €-32,21 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00180 | 0,00184 | 0,00159 | 0,00121 | 0,00222 | €143,70 | €431,11 | €50,27 | €9,81 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 512,43749 | 514,72000 | 523,41700 | 680,68780 | 490,47847 | €780,12 | €2.340,36 | €50,14 | €-10,42 |
| Bilanciata 1H V2 | HYPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 58,72425 | 58,50000 | 59,98403 | 78,00538 | 56,20471 | €763,34 | €2.290,02 | €49,13 | €8,74 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 514,40710 | 514,72000 | 526,37866 | 683,30410 | 490,46397 | €738,63 | €2.215,89 | €51,57 | €-1,35 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 58,72425 | 58,50000 | 59,98403 | 78,00538 | 56,20471 | €797,86 | €2.393,58 | €51,35 | €9,14 |
| Rapida 1H V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23652 | 0,24962 | 0,20814 | 0,15886 | 0,27909 | €136,51 | €409,52 | €49,14 | €22,69 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | LAB | LONG | Momentum / breakout | 60m | 3,0x | 0,15623 | 0,15250 | 0,14118 | 0,10494 | 0,17881 | €171,84 | €515,51 | €49,67 | €-12,31 |
| 1H Fast No Pepe V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| 1H Fast No Pepe V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 515,14695 | 514,72000 | 524,33753 | 684,28687 | 501,36109 | €935,01 | €2.805,03 | €50,04 | €2,32 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17481 | 0,17294 | 0,17178 | 0,11742 | 0,17937 | €954,58 | €2.863,74 | €49,72 | €-30,71 |
| 1H Fast No Pepe V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23895 | 0,24962 | 0,21105 | 0,16049 | 0,28080 | €142,10 | €426,29 | €49,78 | €19,04 |
| 1H Fast Tp2 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| 1H Fast Tp2 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23652 | 0,24962 | 0,20814 | 0,15886 | 0,29328 | €136,61 | €409,83 | €49,18 | €22,70 |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| 1H Fast V3 Cap75 V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| 1H Fast V3 Nohigh V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| 1H Fast V3 No Esports V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07228 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €1,55 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 514,72000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-9,73 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-9,92 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1914,53000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €-14,95 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 510,91780 | 514,72000 | 523,17072 | 763,82211 | 483,96137 | €1.018,21 | €2.036,41 | €48,84 | €-15,15 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 512,43749 | 514,72000 | 523,41700 | 766,09405 | 488,28257 | €1.188,35 | €2.376,70 | €50,92 | €-10,59 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00234 | €214,82 | €429,64 | €50,07 | €-4,25 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,23652 | 0,24962 | 0,20814 | 0,11944 | 0,29896 | €198,11 | €396,21 | €47,55 | €21,95 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,85923 | 58,50000 | 60,10965 | 87,99454 | 55,73317 | €1.195,13 | €2.390,27 | €50,78 | €14,59 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 514,72000 | 527,70883 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €50,83 | €-1,20 |
| Benchmark Bollinger mean reversion 1H | ZEC | LONG | Bollinger mean reversion | 60m | 2,0x | 514,61290 | 514,72000 | 504,63261 | 259,87952 | 529,58334 | €1.299,75 | €2.599,50 | €50,41 | €0,54 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €-11,60 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 511,44769 | 514,72000 | 525,07617 | 764,61430 | 481,46504 | €934,35 | €1.868,69 | €49,79 | €-11,96 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 58,72425 | 58,50000 | 60,12400 | 87,79276 | 55,64481 | €1.039,97 | €2.079,94 | €49,58 | €7,94 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €-12,27 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00231 | €218,50 | €437,00 | €52,44 | €-4,42 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 515,09696 | 514,72000 | 526,55393 | 770,06996 | 492,18303 | €1.091,80 | €2.183,60 | €48,57 | €1,60 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 58,72425 | 58,50000 | 59,98403 | 87,79276 | 56,20471 | €1.131,31 | €2.262,62 | €48,54 | €8,64 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 77,10200 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €-25,21 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €-12,13 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,23895 | 0,24962 | 0,21027 | 0,12067 | 0,30203 | €206,50 | €413,00 | €49,56 | €18,45 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €-11,34 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €201,99 | €403,97 | €48,48 | €-4,08 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,10200 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €-30,68 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-11,64 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,10200 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €-30,68 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-11,64 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €203,02 | €406,03 | €48,72 | €-4,10 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,23895 | 0,24962 | 0,21027 | 0,12067 | 0,30203 | €201,80 | €403,60 | €48,43 | €18,03 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €-11,53 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-4,15 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-4,15 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,23895 | 0,24962 | 0,21027 | 0,12067 | 0,30203 | €204,12 | €408,23 | €48,99 | €18,23 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-11,65 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-4,19 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-11,65 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-4,19 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07238 | 0,07228 | 0,07353 | 0,10820 | 0,06948 | €1.527,19 | €3.054,37 | €48,87 | €4,03 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,39131 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €0,00 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 508,99818 | 514,72000 | 522,42162 | 760,95228 | 479,46661 | €943,19 | €1.886,37 | €49,75 | €-21,21 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €-11,62 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07224 | 0,07228 | 0,07328 | 0,10799 | 0,06995 | €1.717,79 | €3.435,58 | €49,47 | €-2,06 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,17714 | 514,72000 | 525,63928 | 768,69483 | 491,25287 | €1.147,58 | €2.295,16 | €51,16 | €-2,42 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €-16,43 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €-15,54 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive Quality7 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.108,92 | €2.217,83 | €49,44 | €3,30 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive Regime V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.111,03 | €2.222,05 | €49,53 | €3,31 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €-15,92 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €3,30 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €-11,51 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €-11,49 |
| Combo Adaptive Partial 1R V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,68684 | 514,72000 | 527,82154 | 770,95183 | 491,41745 | €1.042,77 | €2.085,55 | €49,08 | €3,91 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €3,30 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 514,72000 | 525,11837 | 769,45713 | 483,39306 | €1.229,27 | €2.458,54 | €49,83 | €-0,16 |
| Combo Adaptive Runner25 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17481 | 0,17294 | 0,17091 | 0,08828 | 0,18652 | €1.111,70 | €2.223,40 | €49,63 | €-23,85 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 514,72000 | 525,11837 | 769,45713 | 483,39306 | €1.230,32 | €2.460,64 | €49,87 | €-0,16 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €-15,99 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65402,10000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65402,10000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 65402,10000 | 67855,55360 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €50,00 | €46,82 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 65402,10000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-24,37 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 77,10200 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €-17,91 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 77,10200 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 77,10200 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 77,10200 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €33,51 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 77,10200 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €-17,90 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 77,10200 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-28,56 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1935,54703 | 1914,53000 | 1907,67515 | 1300,04242 | 1991,29079 | €1.144,65 | €3.433,94 | €49,45 | €-37,29 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1914,53000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €-17,47 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1937,86750 | 1914,53000 | 1909,96220 | 1301,60100 | 1993,67808 | €1.153,05 | €3.459,15 | €49,81 | €-41,66 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13392 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €-11,58 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive No Alt V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13392 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €-11,58 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1914,53000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-35,41 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23652 | 0,24962 | 0,20814 | 0,11944 | 0,29328 | €202,06 | €404,12 | €48,49 | €22,39 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17358 | 0,17294 | 0,17000 | 0,08766 | 0,18074 | €1.190,93 | €2.381,85 | €49,11 | €-8,84 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00229 | €208,66 | €417,31 | €48,63 | €-4,12 |
| Master Adaptive Gb20 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15870 | 0,15250 | 0,13966 | 0,08014 | 0,19679 | €201,47 | €402,94 | €48,35 | €-15,75 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive Runner25 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13392 | 1,12142 | 0,57459 | 1,18696 | €1.694,88 | €3.389,77 | €48,81 | €-11,58 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Tp2 V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17227 | €-53,96 | -1,09 | STOP |
| 1H Fast Nohigh Cap75 V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17227 | €-54,07 | -1,09 | STOP |
| 1H Fast Long Btc 1 3 Cap75 V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17274 | €-54,52 | -1,10 | STOP |
| Rapida 1H V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17227 | €-53,53 | -1,09 | STOP |
| Forza relativa 1H V2 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21843 | €-59,36 | -1,21 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Strict3 V1 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21843 | €-59,23 | -1,21 | STOP_STRESS_SLIPPAGE |
| 1H Fast Tp2 V1 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21849 | €-0,17 | -0,00 | STOP_STRESS_SLIPPAGE |
| 1H Fast Nohigh Cap75 V1 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21795 | €-11,35 | -0,23 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Mfe V1 | LAB | LONG | 2026-07-23T01:23:33+00:00 | 0,14541 | €-50,41 | -1,01 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | LAB | LONG | 2026-07-23T01:23:33+00:00 | 0,14541 | €-49,39 | -1,01 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LAB | LONG | 2026-07-23T01:23:33+00:00 | 0,14541 | €-49,96 | -1,01 | STOP |
| 1H Fast No Pepe V1 | BANK | LONG | 2026-07-23T01:23:33+00:00 | 0,25757 | €72,59 | 1,49 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
