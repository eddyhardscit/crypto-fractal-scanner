# Paper trading automatico KuCoin

Generato: 2026-07-18T21:23:35+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-18T21:23:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-18T21:23:25+00:00 | 2026-07-18T21:23:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-18T21:00:00+00:00 | 2026-07-18T21:00:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-18T20:00:00+00:00 | 2026-07-18T20:00:00+00:00 | 23,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-18T16:00:00+00:00 | 2026-07-18T16:00:00+00:00 | 1,39 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -7,81 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ESPORTS | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,50 | 6,00 | 1,50 | STALE_CANDLE | 1,39 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -3,93 | 6,00 | 2,07 | STALE_CANDLE | 1,39 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 3,72 | 6,00 | 2,28 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,56 | 6,00 | 2,44 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BNB | 240m | SHORT | -3,47 | 6,00 | 2,53 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,16 | 6,00 | 3,84 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -2,07 | 6,00 | 3,93 | STALE_CANDLE | 1,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 83.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | AKE | 60m | LONG | 6,75 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | AKE | 60m | LONG | 6,75 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | ZEC | 60m | LONG | 5,84 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | ZEC | 60m | LONG | 5,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.11%. |
| Rapida 1H V2 | ZEC | 60m | LONG | 5,84 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | ZEC | 60m | LONG | 5,84 | 4,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+0.46%. |
| Bilanciata 1H V2 | ESPORTS | 60m | LONG | 5,50 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | ESPORTS | 60m | LONG | 5,50 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.952,76 | -0,47% | €-47,24 | €3.000,00 | -1,57% | 4 | 15 | 33,33% | 0,89 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 15 | 125 | CAMPIONE INSUFFICIENTE | 30 (mancano 15) |

- Trade del Principale 4H chiusi: **15**; win rate **33,33%**; profit factor **0,89**.
- Expectancy: **€-3,37** per trade; P&L netto: **€-50,49**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.952,76 | €1.317,93 | €3.953,78 | €197,45 | €4,29 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.361,25 | €2.760,17 | €5.520,34 | €153,56 | €10,17 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.332,45 | €2.809,27 | €5.618,54 | €152,93 | €10,14 |
| TEST | Combo Adaptive | 3 | €10.280,51 | €2.703,68 | €5.407,37 | €153,33 | €-23,18 |
| TEST | Ampia 4H | 4 | €10.258,37 | €1.562,36 | €3.124,72 | €150,11 | €101,37 |
| TEST | Rapida 1H V1 | 4 | €10.256,08 | €2.495,24 | €7.485,71 | €204,90 | €12,64 |
| TEST | Combo Mean Reversion | 1 | €10.147,05 | €281,61 | €563,22 | €50,37 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 0 | €10.146,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €10.132,85 | €3.048,77 | €6.097,54 | €151,18 | €-35,24 |
| TEST | Forza relativa 1H V1 | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €10.074,12 | €1.305,56 | €2.611,12 | €100,67 | €64,70 |
| TEST | Bilanciata 1H V1 | 4 | €10.069,34 | €1.461,18 | €4.383,54 | €201,39 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €10.049,48 | €848,96 | €2.546,87 | €99,11 | €63,89 |
| TEST | Combo Scanner | 3 | €10.047,39 | €3.487,82 | €6.975,64 | €150,65 | €-3,98 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €10.019,03 | €2.089,95 | €4.179,90 | €149,62 | €-8,90 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.014,69 | €2.275,49 | €4.550,97 | €99,89 | €-12,71 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.999,77 | €277,38 | €554,76 | €49,61 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.997,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.995,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.993,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.990,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.989,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.981,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 2 | €9.978,97 | €1.112,68 | €3.338,03 | €49,79 | €32,37 |
| TEST | Doge Ema 1H | 1 | €9.971,00 | €1.155,81 | €3.467,44 | €49,93 | €-13,13 |
| TEST | Btc Ema 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.945,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.945,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.944,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.915,07 | €1.551,38 | €3.102,75 | €49,64 | €-12,18 |
| TEST | Combo Adaptive MFE Trail | 1 | €9.891,06 | €206,72 | €413,44 | €49,61 | €-7,49 |
| TEST | Bilanciata 1H V3 Filtered | 3 | €9.865,04 | €2.448,48 | €7.345,43 | €99,92 | €23,15 |

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
| TEST | Combo Adaptive MFE Trail | Combo Adaptive | Portafoglio sperimentale separato. |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.952,76 | €-50,49 | 15 | 15 | 33,33% | 0,89 | €-3,37 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.361,25 | €354,46 | 14 | 14 | 57,14% | 2,31 | €25,32 | 1,65% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.332,45 | €325,68 | 12 | 12 | 50,00% | 2,51 | €27,14 | 1,62% |
| TEST | Combo Adaptive | Combo Adaptive | €10.280,51 | €306,61 | 12 | 12 | 50,00% | 2,85 | €25,55 | 0,75% |
| TEST | Ampia 4H | Confluenza trend | €10.258,37 | €157,76 | 9 | 9 | 33,33% | 1,60 | €17,53 | 2,08% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.256,08 | €247,83 | 33 | 33 | 45,45% | 1,35 | €7,51 | 2,34% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.147,05 | €147,74 | 2 | 2 | 100,00% | ∞ | €73,87 | 0,59% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.146,99 | €146,99 | 8 | 8 | 50,00% | 1,92 | €18,37 | 1,37% |
| TEST | Combo Trend | Combo Trend | €10.132,85 | €170,64 | 8 | 8 | 50,00% | 2,07 | €21,33 | 1,48% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.074,12 | €10,82 | 7 | 7 | 28,57% | 1,05 | €1,55 | 2,32% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.069,34 | €71,78 | 10 | 10 | 50,00% | 1,44 | €7,18 | 1,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.049,48 | €-13,06 | 11 | 9 | 45,45% | 0,95 | €-1,19 | 2,10% |
| TEST | Combo Scanner | Combo Scanner | €10.047,39 | €55,26 | 10 | 10 | 40,00% | 1,21 | €5,53 | 1,69% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.019,03 | €30,25 | 4 | 4 | 50,00% | 1,28 | €7,56 | 1,10% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.014,69 | €29,58 | 5 | 5 | 60,00% | 1,28 | €5,92 | 1,78% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.999,77 | €0,44 | 9 | 9 | 44,44% | 1,00 | €0,05 | 2,06% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.997,88 | €-2,12 | 3 | 3 | 33,33% | 0,30 | €-0,71 | 0,04% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.995,51 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,43% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.993,84 | €-6,16 | 3 | 3 | 33,33% | 0,55 | €-2,05 | 0,16% |
| TEST | Sol Ema 1H | Trend following EMA | €9.990,84 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,87% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.989,40 | €-10,60 | 3 | 3 | 33,33% | 0,30 | €-3,53 | 0,18% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.981,55 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,89% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.978,97 | €-51,40 | 5 | 5 | 40,00% | 0,66 | €-10,28 | 1,46% |
| TEST | Doge Ema 1H | Trend following EMA | €9.971,00 | €-13,78 | 2 | 2 | 50,00% | 0,75 | €-6,89 | 1,05% |
| TEST | Btc Ema 1H | Trend following EMA | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Eth Ema 1H | Trend following EMA | €9.945,10 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,55% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.945,10 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,55% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,88 | €-55,12 | 1 | 1 | 0,00% | 0,00 | €-55,12 | 0,67% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.915,07 | €-71,19 | 3 | 3 | 33,33% | 0,35 | €-23,73 | 1,18% |
| TEST | Combo Adaptive MFE Trail | Combo Adaptive | €9.891,06 | €-101,20 | 3 | 3 | 0,00% | 0,00 | €-33,73 | 1,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.865,04 | €-154,34 | 3 | 3 | 0,00% | 0,00 | €-51,45 | 1,98% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07243 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €11,47 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 60,07600 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €-11,33 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 558,69000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €4,15 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00172 | 0,00198 | 0,00172 | 0,00116 | 0,00213 | €139,07 | €417,21 | €0,00 | €63,89 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,07217 | 0,07243 | 0,07321 | 0,09586 | 0,07009 | €1.157,41 | €3.472,22 | €50,00 | €-12,67 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 74,89902 | 75,47000 | 75,97756 | 99,49086 | 72,74193 | €1.155,58 | €3.466,74 | €49,92 | €-26,43 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00172 | 0,00198 | 0,00172 | 0,00116 | 0,00213 | €135,49 | €406,47 | €0,00 | €62,25 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,18833 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €-0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37292 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €0,00 |
| Rapida 1H V1 | GRAM | SHORT | Momentum / breakout | 60m | 3,0x | 1,49240 | 1,49240 | 1,52648 | 1,98241 | 1,44129 | €757,31 | €2.271,94 | €51,87 | €-0,00 |
| Rapida 1H V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 556,25123 | 558,69000 | 546,59458 | 373,61541 | 570,73620 | €961,25 | €2.883,75 | €50,06 | €12,64 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 555,61110 | 558,69000 | 546,14143 | 373,18546 | 569,81561 | €973,80 | €2.921,40 | €49,79 | €16,19 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00191 | 0,00198 | 0,00191 | 0,00128 | 0,00225 | €138,88 | €416,63 | €0,00 | €16,18 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07243 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-1,14 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 558,69000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €46,25 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 60,07600 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-8,87 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00172 | 0,00198 | 0,00172 | 0,00087 | 0,00230 | €212,64 | €425,29 | €0,00 | €65,13 |
| Forza relativa 1H V1 | AAVE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H V1 | T | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00172 | 0,00198 | 0,00172 | 0,00087 | 0,00217 | €211,25 | €422,49 | €0,00 | €64,70 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 59,78804 | 60,07600 | 61,40996 | 89,38312 | 56,21982 | €924,22 | €1.848,44 | €50,14 | €-8,90 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 556,25123 | 558,69000 | 543,83554 | 280,90687 | 581,08261 | €1.159,54 | €2.319,07 | €51,76 | €10,17 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22091 | 0,20335 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07217 | 0,07243 | 0,07321 | 0,10789 | 0,07009 | €1.741,23 | €3.482,46 | €50,15 | €-12,71 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 556,25123 | 558,69000 | 543,83554 | 280,90687 | 583,56574 | €1.156,31 | €2.312,63 | €51,62 | €10,14 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07215 | 0,07243 | 0,07330 | 0,10786 | 0,06926 | €1.551,38 | €3.102,75 | €49,64 | €-12,18 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,08689 | 1,09599 | 1,10428 | 1,62490 | 1,04863 | €1.565,99 | €3.131,98 | €50,11 | €-26,22 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 59,78804 | 60,07600 | 61,40996 | 89,38312 | 56,21982 | €936,92 | €1.873,85 | €50,83 | €-9,03 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07215 | 0,07243 | 0,07319 | 0,10786 | 0,06986 | €1.763,29 | €3.526,57 | €50,78 | €-13,85 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 556,25123 | 558,69000 | 543,83554 | 280,90687 | 583,56574 | €1.125,40 | €2.250,79 | €50,24 | €9,87 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 59,36013 | 60,07600 | 60,93558 | 88,74339 | 56,20922 | €960,91 | €1.921,82 | €51,01 | €-23,18 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive MFE Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00202 | 0,00198 | 0,00178 | 0,00102 | 0,00251 | €206,72 | €413,44 | €49,61 | €-7,49 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07216 | 0,07243 | 0,07320 | 0,09585 | 0,07008 | €1.155,81 | €3.467,44 | €49,93 | €-13,13 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive MFE Trail | ESPORTS | LONG | 2026-07-18T21:23:31+00:00 | 0,02745 | €-50,43 | -1,01 | STOP |
| Scalp RSI Short 75 · prudente · 5x | ZEC | SHORT | 2026-07-18T21:23:31+00:00 | 558,80174 | €-2,96 | -0,30 | TIME_EXIT |
| Forza relativa 1H V2 | ESPORTS | LONG | 2026-07-18T21:23:31+00:00 | 0,02750 | €-51,37 | -1,01 | STOP |
| Rapida 1H V3 Filtered | ESPORTS | LONG | 2026-07-18T21:23:31+00:00 | 0,02750 | €-50,83 | -1,01 | STOP |
| Combo Adaptive MFE Trail | AKE | LONG | 2026-07-18T20:23:30+00:00 | 0,00191 | €-0,08 | -0,00 | STOP |
| Forza relativa 1H V2 | ESPORTS | LONG | 2026-07-18T20:08:30+00:00 | 0,03002 | €-51,31 | -1,01 | STOP |
| Rapida 1H V3 Filtered | ESPORTS | LONG | 2026-07-18T20:08:30+00:00 | 0,03024 | €-50,65 | -1,01 | STOP |
| Scalp RSI Short 75 · €50 · 15x | ZEC | SHORT | 2026-07-18T19:38:30+00:00 | 556,65131 | €-0,65 | -0,05 | TIME_EXIT |
| Scalp RSI Short 75 · €10 · 15x | ZEC | SHORT | 2026-07-18T19:38:30+00:00 | 556,65131 | €-0,13 | -0,05 | TIME_EXIT |
| Combo Adaptive MFE Trail | ESPORTS | LONG | 2026-07-18T19:38:30+00:00 | 0,03062 | €-50,69 | -1,01 | STOP |
| Rapida 1H V3 Filtered | AKE | LONG | 2026-07-18T19:38:30+00:00 | 0,00203 | €73,98 | 1,49 | TARGET |
| Bilanciata 1H V3 Filtered | ESPORTS | LONG | 2026-07-18T19:38:30+00:00 | 0,03090 | €-50,24 | -1,01 | STOP |

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
| MAIN | Principale 4H | 20/30 | 15/30 | 0,82 | 0,89 | -0,13R | €-3,37 | 4,26% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 3/30 | 3/30 | 0,86 | 0,55 | -0,07R | €-2,05 | 0,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 71/30 | 10/30 | 0,87 | 1,44 | -0,09R | €7,18 | 1,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 8/30 | 9/30 | 1,88 | 0,95 | 0,46R | €-1,19 | 2,10% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 4/30 | 3/30 | 0,64 | 0,00 | -0,28R | €-51,45 | 1,98% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 | 80/30 | 33/30 | 0,87 | 1,35 | -0,08R | €7,51 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 1/30 | 1/30 | 1,19 | 11,45 | 0,11R | €31,39 | 0,93% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered | 4/30 | 5/30 | 1,47 | 0,66 | 0,24R | €-10,28 | 1,46% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 18/30 | 9/30 | 1,04 | 1,60 | 0,03R | €17,53 | 2,08% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 15/30 | 9/30 | 0,88 | 1,00 | -0,08R | €0,05 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-55,12 | 0,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 29/30 | 12/30 | 1,49 | 2,85 | 0,29R | €25,55 | 0,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive MFE Trail | 1/30 | 3/30 | 0,00 | 0,00 | -1,01R | €-33,73 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 5/30 | 2/30 | 5,95 | ∞ | 1,01R | €73,87 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 18/30 | 10/30 | 1,03 | 1,21 | 0,02R | €5,53 | 1,69% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 24/30 | 8/30 | 1,03 | 2,07 | 0,02R | €21,33 | 1,48% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €26,22 | 0,36% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 2/30 | 0,00 | 0,75 | 0,00R | €-6,89 | 1,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 12/30 | 8/30 | 0,77 | 1,92 | -0,18R | €18,37 | 1,37% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 30/30 | 4/30 | 0,88 | 1,28 | -0,09R | €7,56 | 1,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 3/30 | 0,00 | 0,35 | -1,10R | €-23,73 | 1,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 45/30 | 7/30 | 0,94 | 1,56 | -0,04R | €12,63 | 1,36% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 8/30 | 7/30 | 1,28 | 1,05 | 0,18R | €1,55 | 2,32% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 11/30 | 5/30 | 1,03 | 1,28 | 0,02R | €5,92 | 1,78% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 20/30 | 12/30 | 1,11 | 2,51 | 0,08R | €27,14 | 1,62% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 25/30 | 14/30 | 1,04 | 2,31 | 0,03R | €25,32 | 1,65% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,49 | 0,43% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 2/30 | 2/30 | 1,70 | 0,83 | 0,39R | €-4,58 | 0,87% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07243**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.6 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64734.81 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07247**; close **0.07247**; wick alta **0.0%**; volume **x0.69**

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

- Regime: **TREND_UP**
- Famiglia: **TREND_UP**
- Confidenza: **74,60%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +3.0, 83% sopra EMA50, ADX 19.8.
- BTC trend score: **3,00**; ADX: **19,84**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **-0,22%**; dispersione: **6,39%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **146**
- Trade research chiusi: **465**
- Eventi di mercato indipendenti chiusi: **194**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **1313**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 9 | 20 | 20 | 30,00% | 0,82 | -0,13R | €-25,53 |
| RSI_EXTREME_SHORT_15M | 1 | 3 | 3 | 33,33% | 0,86 | -0,07R | €-2,17 |
| Bilanciata 1H V1 | 15 | 71 | 71 | 32,39% | 0,87 | -0,09R | €-64,85 |
| Bilanciata 1H V2 | 7 | 8 | 8 | 50,00% | 1,88 | 0,46R | €37,19 |
| Bilanciata 1H V3 Filtered | 3 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,22 |
| Rapida 1H V1 | 10 | 80 | 80 | 38,75% | 0,87 | -0,08R | €-66,52 |
| Rapida 1H V2 | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | 4 | 4 | 4 | 50,00% | 1,47 | 0,24R | €9,47 |
| SHADOW_4H_WIDE | 15 | 18 | 18 | 27,78% | 1,04 | 0,03R | €6,00 |
| SHADOW_BOLLINGER_MR_1H | 0 | 15 | 15 | 40,00% | 0,88 | -0,08R | €-11,81 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | 10 | 29 | 29 | 44,83% | 1,49 | 0,29R | €83,31 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 3 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 5 | 5 | 80,00% | 5,95 | 1,01R | €50,43 |
| SHADOW_COMBO_SCANNER | 5 | 18 | 18 | 33,33% | 1,03 | 0,02R | €3,89 |
| SHADOW_COMBO_TREND | 8 | 24 | 24 | 33,33% | 1,03 | 0,02R | €5,18 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 5 | 12 | 12 | 25,00% | 0,77 | -0,18R | €-21,93 |
| SHADOW_EMA_TREND_1H | 11 | 30 | 30 | 30,00% | 0,88 | -0,09R | €-26,73 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| Forza relativa 1H V1 | 11 | 45 | 45 | 31,11% | 0,94 | -0,04R | €-19,47 |
| Forza relativa 1H V2 | 5 | 8 | 8 | 37,50% | 1,28 | 0,18R | €14,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 11 | 11 | 36,36% | 1,03 | 0,02R | €1,96 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 20 | 20 | 35,00% | 1,11 | 0,08R | €15,07 |
| SHADOW_SCANNER_TOP5_LONG | 6 | 25 | 25 | 36,00% | 1,04 | 0,03R | €7,47 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 1 | 13 | 13 | 30,77% | 0,86 | -0,10R | €-13,29 |
| MAIN | TRANSITION | 5 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,54 |
| MAIN | TREND_UP | 3 | 4 | 4 | 25,00% | 0,63 | -0,29R | €-11,70 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,86 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 2,27 | 0,60R | €54,20 |
| Bilanciata 1H V1 | RANGE | 5 | 23 | 23 | 34,78% | 0,98 | -0,02R | €-3,57 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| Bilanciata 1H V1 | TRANSITION | 7 | 16 | 16 | 43,75% | 1,42 | 0,25R | €40,29 |
| Bilanciata 1H V1 | TREND_UP | 3 | 14 | 14 | 21,43% | 0,50 | -0,42R | €-58,52 |
| Bilanciata 1H V2 | RANGE | 3 | 3 | 3 | 66,67% | 3,58 | 0,95R | €28,62 |
| Bilanciata 1H V2 | TRANSITION | 4 | 5 | 5 | 40,00% | 1,27 | 0,17R | €8,56 |
| Bilanciata 1H V3 Filtered | TRANSITION | 3 | 3 | 3 | 33,33% | 0,95 | -0,04R | €-1,08 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| Rapida 1H V1 | RANGE | 3 | 32 | 32 | 43,75% | 1,11 | 0,06R | €20,16 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| Rapida 1H V1 | TRANSITION | 3 | 16 | 16 | 62,50% | 2,29 | 0,51R | €81,94 |
| Rapida 1H V1 | TREND_UP | 4 | 16 | 16 | 25,00% | 0,46 | -0,44R | €-70,98 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 3 | 3 | 66,67% | 2,93 | 0,65R | €19,60 |
| Rapida 1H V3 Filtered | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | RANGE | 6 | 11 | 11 | 27,27% | 1,02 | 0,01R | €1,48 |
| SHADOW_4H_WIDE | TRANSITION | 6 | 4 | 4 | 25,00% | 0,92 | -0,06R | €-2,53 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 3 | 3 | 33,33% | 1,34 | 0,24R | €7,06 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,85 | -0,10R | €-4,84 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 5 | 7 | 7 | 42,86% | 1,34 | 0,21R | €14,90 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 4 | 12 | 12 | 50,00% | 1,87 | 0,45R | €54,36 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 10 | 10 | 40,00% | 1,22 | 0,14R | €14,04 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | TRANSITION | 3 | 9 | 9 | 33,33% | 1,05 | 0,04R | €3,16 |
| SHADOW_COMBO_SCANNER | TREND_UP | 1 | 8 | 8 | 25,00% | 0,67 | -0,26R | €-21,14 |
| SHADOW_COMBO_TREND | RANGE | 3 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,81 |
| SHADOW_COMBO_TREND | TRANSITION | 4 | 11 | 11 | 45,45% | 1,74 | 0,42R | €45,85 |
| SHADOW_COMBO_TREND | TREND_UP | 1 | 8 | 8 | 25,00% | 0,69 | -0,25R | €-19,86 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | RANGE | 4 | 4 | 4 | 25,00% | 0,76 | -0,19R | €-7,56 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 4 | 4 | 25,00% | 0,78 | -0,17R | €-6,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 4 | 4 | 25,00% | 0,77 | -0,19R | €-7,43 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 6 | 6 | 16,67% | 0,41 | -0,52R | €-30,95 |
| SHADOW_EMA_TREND_1H | TRANSITION | 4 | 11 | 11 | 45,45% | 1,74 | 0,42R | €45,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 13 | 13 | 23,08% | 0,61 | -0,32R | €-41,63 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,68 | -0,26R | €-20,48 |
| Forza relativa 1H V1 | RANGE | 4 | 16 | 16 | 25,00% | 0,69 | -0,24R | €-38,67 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 11 | 11 | 54,55% | 2,55 | 0,72R | €78,82 |
| Forza relativa 1H V1 | TREND_UP | 6 | 8 | 8 | 25,00% | 0,70 | -0,24R | €-18,82 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 3 | 5 | 5 | 40,00% | 1,40 | 0,25R | €12,56 |
| Forza relativa 1H V2 | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-54,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 5 | 4 | 4 | 75,00% | 5,24 | 1,16R | €46,30 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 2,14R | €64,28 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 2 | 9 | 9 | 33,33% | 1,05 | 0,04R | €3,16 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 1 | 7 | 7 | 14,29% | 0,34 | -0,60R | €-41,85 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 4 | 4 | 100,00% | ∞ | 1,95R | €78,15 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 2 | 9 | 9 | 33,33% | 0,95 | -0,03R | €-2,84 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 11 | 11 | 18,18% | 0,41 | -0,52R | €-56,73 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
