# Paper trading automatico KuCoin

Generato: 2026-07-15T19:38:46+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-15T19:38:39+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-15T19:38:39+00:00 | 2026-07-15T19:38:39+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-15T19:15:00+00:00 | 2026-07-15T19:15:00+00:00 | 23,7 min | 40,0 min | OK |
| 60m | 12 | 2026-07-15T18:00:00+00:00 | 2026-07-15T18:00:00+00:00 | 1,64 h | 1,42 h | STALE_CANDLE |
| 240m | 12 | 2026-07-15T12:00:00+00:00 | 2026-07-15T12:00:00+00:00 | 7,64 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | 240m | LONG | 9,42 | 6,00 | 0,00 | STALE_CANDLE | 7,64 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 7,26 | 6,00 | 0,00 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 6,04 | 6,00 | 0,00 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | AKE | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | XRP | 240m | LONG | 3,80 | 6,00 | 2,20 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | SOL | 240m | LONG | 3,45 | 6,00 | 2,55 | STALE_CANDLE | 7,64 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -3,09 | 6,00 | 2,91 | STALE_CANDLE | 7,64 h | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | HYPE | 240m | LONG | 2,78 | 6,00 | 3,22 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -0,18 | 6,00 | 5,82 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Principale 4H | 0G | 240m | LONG | 0,15 | 6,00 | 5,85 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Ampia 4H | BTC | 240m | LONG | 9,42 | 5,00 | 0,00 | STALE_CANDLE | 7,64 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Ampia 4H | ZEC | 240m | LONG | 8,25 | 5,00 | 0,00 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Ampia 4H | ETH | 240m | LONG | 7,26 | 5,00 | 0,00 | STALE_CANDLE | 7,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 458.7 minuti; limite 265. |
| Bilanciata 1H | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | STALE_CANDLE | 1,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 98.7 minuti; limite 85. |
| Rapida 1H | LAB | 60m | SHORT | -7,00 | 4,50 | 0,00 | STALE_CANDLE | 1,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 98.7 minuti; limite 85. |
| Forza relativa 1H | LAB | 60m | SHORT | -7,00 | 4,00 | 0,00 | STALE_CANDLE | 1,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 98.7 minuti; limite 85. |
| Benchmark Donchian breakout 1H | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | STALE_CANDLE | 1,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 98.7 minuti; limite 85. |
| Benchmark Bollinger mean reversion 1H | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | STALE_CANDLE | 1,64 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 98.7 minuti; limite 85. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.963,73 | -0,36% | €-36,27 | €3.000,00 | -1,21% | 3 | 8 | 25,00% | 0,77 | 2,88% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 8 | 41 | CAMPIONE INSUFFICIENTE | 30 (mancano 22) |

- Trade del Principale 4H chiusi: **8**; win rate **25,00%**; profit factor **0,77**.
- Expectancy: **€-7,50** per trade; P&L netto: **€-60,04**; max drawdown: **2,88%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €9.963,73 | €1.381,40 | €4.144,21 | €99,02 | €27,31 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.262,83 | €2.799,01 | €5.598,01 | €152,59 | €4,60 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.199,16 | €1.409,29 | €2.818,59 | €50,87 | €23,31 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.183,26 | €2.152,20 | €4.304,40 | €151,83 | €-19,63 |
| TEST | Ampia 4H | 4 | €10.101,18 | €2.257,17 | €4.514,33 | €200,61 | €16,82 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.076,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €10.039,22 | €534,26 | €1.068,51 | €99,99 | €-8,67 |
| TEST | Rapida 1H | 3 | €10.032,62 | €2.340,91 | €7.022,73 | €100,93 | €31,84 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.029,09 | €1.140,92 | €2.281,84 | €50,08 | €19,29 |
| TEST | Combo Adaptive | 3 | €10.007,47 | €1.725,50 | €3.451,00 | €100,22 | €-5,63 |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.998,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.996,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €9.995,49 | €2.278,77 | €4.557,55 | €99,99 | €-1,78 |
| TEST | Global Confluence puro 1H | 1 | €9.992,53 | €1.562,50 | €3.125,00 | €50,00 | €-4,97 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 2 | €9.962,17 | €2.300,55 | €4.601,09 | €99,99 | €-34,87 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.950,52 | €2.720,15 | €5.440,31 | €149,22 | €5,28 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H | Confluenza trend | Test bilanciato a 1 ora basato sulla confluenza di trend. |
| TEST | Rapida 1H | Momentum / breakout | Test rapido a 1 ora che cerca momentum e breakout. |
| TEST | Ampia 4H | Confluenza trend | Test a 4 ore con stop più ampio, leva inferiore e durata maggiore. |
| TEST | Forza relativa 1H | Forza relativa vs BTC | Test a 1 ora che seleziona forza o debolezza rispetto a Bitcoin. |
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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.963,73 | €-60,04 | 8 | 8 | 25,00% | 0,77 | €-7,50 | 2,88% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.262,83 | €261,58 | 4 | 4 | 100,00% | ∞ | €65,40 | 0,44% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.199,16 | €177,56 | 2 | 2 | 100,00% | ∞ | €88,78 | 0,86% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.183,26 | €205,54 | 3 | 3 | 100,00% | ∞ | €68,51 | 0,76% |
| TEST | Ampia 4H | Confluenza trend | €10.101,18 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,51% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.076,46 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,02% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.039,22 | €48,53 | 2 | 2 | 50,00% | 1,96 | €24,27 | 0,51% |
| TEST | Rapida 1H | Momentum / breakout | €10.032,62 | €4,81 | 19 | 19 | 42,11% | 1,01 | €0,25 | 1,88% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.029,09 | €11,10 | 3 | 3 | 33,33% | 1,18 | €3,70 | 0,60% |
| TEST | Combo Adaptive | Combo Adaptive | €10.007,47 | €15,12 | 1 | 1 | 100,00% | ∞ | €15,12 | 0,50% |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.998,01 | €-1,99 | 2 | 2 | 50,00% | 0,31 | €-1,00 | 0,04% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.996,80 | €-3,20 | 2 | 2 | 50,00% | 0,70 | €-1,60 | 0,16% |
| TEST | Combo Trend | Combo Trend | €9.995,49 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,65% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.992,53 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,28% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Combo Scanner | Combo Scanner | €9.962,17 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 1,06% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.950,52 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,68% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64909,96000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €3,85 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 539,89796 | 566,14000 | 555,96789 | 362,63146 | 601,61962 | €290,77 | €872,31 | €0,00 | €42,40 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-18,94 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,24273 | 0,22548 | 0,24273 | 0,32243 | 0,19904 | €139,75 | €419,24 | €0,00 | €29,80 |
| Rapida 1H | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,03453 | 1924,00000 | 1899,20690 | 1291,63819 | 1958,77597 | €1.356,98 | €4.070,94 | €50,44 | €2,04 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07387 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-26,99 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 566,14000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €55,73 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64909,96000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €2,99 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-14,91 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,22548 | 0,26148 | 0,39091 | 0,18303 | €211,57 | €423,15 | €0,00 | €58,26 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 67,96459 | 66,97300 | 66,52140 | 34,32212 | 71,57256 | €1.197,72 | €2.395,44 | €50,87 | €-34,95 |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | Bollinger mean reversion | 60m | 2,0x | 570,96578 | 566,14000 | 583,49757 | 853,59385 | 552,16811 | €1.140,92 | €2.281,84 | €50,08 | €19,29 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64909,96000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €5,28 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00065 | 0,00066 | 0,00057 | 0,00033 | 0,00081 | €213,76 | €427,52 | €51,30 | €2,99 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1923,03453 | 1924,00000 | 1892,39901 | 971,13244 | 1984,30556 | €1.610,10 | €3.220,20 | €51,30 | €1,62 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22548 | 0,24741 | 0,33025 | 0,16789 | €209,34 | €418,67 | €50,24 | €-8,67 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 572,85455 | 566,14000 | 557,76666 | 289,29155 | 606,04791 | €964,37 | €1.928,74 | €50,80 | €-22,61 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00065 | 0,00066 | 0,00057 | 0,00033 | 0,00082 | €212,68 | €425,35 | €51,04 | €2,97 |
| Global Confluence puro 1H | BTC | LONG | Global Confluence puro | 60m | 2,0x | 65013,44009 | 64909,96000 | 63973,22505 | 32831,78724 | 67613,97769 | €1.562,50 | €3.125,00 | €50,00 | €-4,97 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 565,20302 | 566,14000 | 549,38594 | 285,42752 | 600,00058 | €893,34 | €1.786,69 | €50,00 | €2,96 |
| Combo Trend | LAB | SHORT | Combo Trend | 60m | 2,0x | 0,24273 | 0,22548 | 0,24273 | 0,36288 | 0,17865 | €208,30 | €416,61 | €0,00 | €29,61 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 67,96459 | 66,97300 | 66,52140 | 34,32212 | 71,13960 | €1.177,13 | €2.354,26 | €49,99 | €-34,35 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 565,20302 | 566,14000 | 550,96765 | 285,42752 | 596,52083 | €992,60 | €1.985,21 | €50,00 | €3,29 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 67,96459 | 66,97300 | 66,66572 | 34,32212 | 70,82210 | €1.307,94 | €2.615,89 | €49,99 | €-38,17 |
| Combo Adaptive | LAB | SHORT | Combo Adaptive | 60m | 2,0x | 0,24273 | 0,22548 | 0,24273 | 0,36288 | 0,18448 | €208,30 | €416,60 | €0,00 | €29,61 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 67,96459 | 66,97300 | 66,66572 | 34,32212 | 70,56233 | €1.307,90 | €2.615,80 | €49,99 | €-38,16 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00065 | 0,00066 | 0,00057 | 0,00033 | 0,00081 | €209,30 | €418,60 | €50,23 | €2,93 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida 1H | HYPE | LONG | 2026-07-15T19:38:43+00:00 | 66,94097 | €-55,17 | -1,10 | STOP |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | 2026-07-15T18:14:36+00:00 | 1927,96992 | €-5,46 | -0,11 | STOP |
| Scanner Top 5 Long 1H | ZEC | LONG | 2026-07-15T16:57:25+00:00 | 568,10453 | €37,85 | 0,75 | STOP |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | 2026-07-15T16:57:25+00:00 | 1909,92846 | €67,16 | 1,34 | STOP |
| Scalp RSI Short 75 · prudente · 5x | XRP | SHORT | 2026-07-15T16:57:25+00:00 | 1,11559 | €7,59 | 0,76 | STOP |
| Scalp RSI Short 75 · €50 · 15x | XRP | SHORT | 2026-07-15T16:57:25+00:00 | 1,11525 | €4,49 | 0,80 | STOP_SAME_CANDLE_CONSERVATIVE |
| Scalp RSI Short 75 · €10 · 15x | XRP | SHORT | 2026-07-15T16:57:25+00:00 | 1,11525 | €0,90 | 0,80 | STOP_SAME_CANDLE_CONSERVATIVE |
| Benchmark Donchian breakout 1H | ETH | LONG | 2026-07-15T16:57:25+00:00 | 1906,38496 | €55,27 | 1,11 | STOP |
| Combo Mean Reversion | PEPE | SHORT | 2026-07-15T16:57:25+00:00 | 0,00000 | €76,46 | 1,53 | TARGET |
| Scanner Bottom 5 Short 1H | LAB | SHORT | 2026-07-15T15:40:23+00:00 | 0,21369 | €99,16 | 1,99 | TARGET |
| Combo Adaptive | ZEC | LONG | 2026-07-15T15:40:23+00:00 | 570,18986 | €15,12 | 0,30 | STOP |
| Rapida 1H | AAVE | LONG | 2026-07-15T15:40:23+00:00 | 98,81996 | €-4,97 | -0,10 | TIME_EXIT_NO_CANDLES |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07387**
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
| Global DOGE | -5.0 | OK |
| Classic raw | -1.0 | NO |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64909.96 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07399**; close **0.07383**; wick alta **0.0%**; volume **x0.85**

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
- Confidenza: **85,10%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 92% sopra EMA50, ADX 27.6.
- BTC trend score: **4,00**; ADX: **27,60**; breadth sopra EMA50: **91,67%**
- Mediana alt vs BTC: **-0,11%**; dispersione: **65,30%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **8**
- Posizioni research aperte: **84**
- Trade research chiusi: **152**
- Eventi di mercato indipendenti chiusi: **77**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **429**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| RSI_EXTREME_SHORT_15M | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,96 |
| SHADOW_1H_BALANCED | 9 | 37 | 37 | 32,43% | 0,87 | -0,09R | €-33,63 |
| SHADOW_1H_FAST | 6 | 42 | 42 | 28,57% | 0,54 | -0,35R | €-147,63 |
| SHADOW_4H_WIDE | 7 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_BOLLINGER_MR_1H | 1 | 6 | 6 | 33,33% | 0,64 | -0,26R | €-15,62 |
| SHADOW_COMBO_ADAPTIVE | 5 | 3 | 3 | 66,67% | 3,77 | 0,94R | €28,07 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | 4 | 2 | 2 | 50,00% | 2,06 | 0,54R | €10,76 |
| SHADOW_COMBO_TREND | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | 5 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_EMA_TREND_1H | 10 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,43 |
| SHADOW_GLOBAL_PURE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 11 | 23 | 23 | 21,74% | 0,58 | -0,34R | €-79,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 2 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 4 | 4 | 50,00% | 2,04 | 0,54R | €21,59 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 6 | 6 | 50,00% | 1,84 | 0,44R | €26,37 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 0 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| MAIN | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,86 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 2,27 | 0,60R | €54,20 |
| SHADOW_1H_BALANCED | RANGE | 1 | 15 | 15 | 40,00% | 1,23 | 0,15R | €21,89 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| SHADOW_1H_BALANCED | TREND_UP | 8 | 4 | 4 | 25,00% | 0,61 | -0,31R | €-12,46 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| SHADOW_1H_FAST | RANGE | 1 | 19 | 19 | 42,11% | 1,01 | 0,00R | €0,76 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| SHADOW_1H_FAST | TREND_UP | 5 | 7 | 7 | 14,29% | 0,23 | -0,72R | €-50,74 |
| SHADOW_4H_WIDE | RANGE | 2 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €2,97 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 4 | 4 | 25,00% | 0,43 | -0,46R | €-18,59 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 5 | 3 | 3 | 66,67% | 3,77 | 0,94R | €28,07 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 4 | 2 | 2 | 50,00% | 2,06 | 0,54R | €10,76 |
| SHADOW_COMBO_TREND | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TREND_UP | 9 | 3 | 3 | 33,33% | 1,03 | 0,02R | €0,71 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 1,02 | 0,02R | €1,05 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 1 | 14 | 14 | 21,43% | 0,56 | -0,36R | €-49,93 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 8 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 2,12R | €42,42 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 3 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,82 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 1,92R | €38,42 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 5 | 4 | 4 | 25,00% | 0,62 | -0,30R | €-12,05 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
