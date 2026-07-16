# Paper trading automatico KuCoin

Generato: 2026-07-16T09:22:59+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-16T09:22:48+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-16T09:22:48+00:00 | 2026-07-16T09:22:48+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-16T09:00:00+00:00 | 2026-07-16T09:00:00+00:00 | 22,9 min | 40,0 min | OK |
| 60m | 12 | 2026-07-16T08:00:00+00:00 | 2026-07-16T08:00:00+00:00 | 1,38 h | 1,42 h | OK |
| 240m | 12 | 2026-07-16T04:00:00+00:00 | 2026-07-16T04:00:00+00:00 | 5,38 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom 5 Short 1H | ADA | 60m | SHORT | -5,03 | 5,00 | 0,00 | OPENED | 1,38 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 6,91 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -5,62 | 6,00 | 0,38 | STALE_CANDLE | 5,38 h | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -5,08 | 6,00 | 0,92 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | BTC | 240m | LONG | 4,42 | 6,00 | 1,58 | STALE_CANDLE | 5,38 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | 0G | 240m | SHORT | -3,96 | 6,00 | 2,04 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -2,13 | 6,00 | 3,87 | STALE_CANDLE | 5,38 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | XRP | 240m | LONG | 0,97 | 6,00 | 5,03 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | HYPE | 240m | LONG | 0,66 | 6,00 | 5,34 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 0,58 | 6,00 | 5,42 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 322.9 minuti; limite 265. |
| Rapida 1H | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 1,38 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 1,38 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H | DOGE | 60m | SHORT | -5,27 | 4,50 | 0,00 | OPENED | 1,38 h | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H | 0G | 60m | SHORT | -5,13 | 4,50 | 0,00 | READY | 1,38 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | 0G | 60m | SHORT | -5,13 | 5,00 | 0,00 | READY | 1,38 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom 5 Short 1H | 0G | 60m | SHORT | -5,13 | 5,00 | 0,00 | READY | 1,38 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H | ADA | 60m | SHORT | -5,03 | 4,50 | 0,00 | READY | 1,38 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | ADA | 60m | SHORT | -5,03 | 5,00 | 0,00 | OPENED | 1,38 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.892,75 | -1,07% | €-107,25 | €3.000,00 | -3,57% | 2 | 9 | 33,33% | 0,86 | 3,17% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 9 | 49 | CAMPIONE INSUFFICIENTE | 30 (mancano 21) |

- Trade del Principale 4H chiusi: **9**; win rate **33,33%**; profit factor **0,86**.
- Expectancy: **€-3,97** per trade; P&L netto: **€-35,75**; max drawdown: **3,17%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 2 | €9.892,75 | €1.090,63 | €3.271,90 | €99,02 | €-68,23 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.325,66 | €1.190,90 | €2.381,80 | €101,77 | €19,69 |
| TEST | Scanner Top 5 + forza BTC 1H | 2 | €10.261,90 | €1.188,95 | €2.377,89 | €101,30 | €-0,09 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.197,70 | €1.516,14 | €3.032,28 | €51,00 | €75,91 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €10.083,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.076,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.058,37 | €1.964,02 | €3.928,04 | €150,30 | €12,13 |
| TEST | Ampia 4H | 4 | €10.046,24 | €2.257,17 | €4.514,33 | €200,61 | €-37,84 |
| TEST | Combo Adaptive | 1 | €10.024,48 | €209,60 | €419,20 | €50,30 | €19,13 |
| TEST | Rapida 1H | 4 | €10.022,58 | €2.598,20 | €7.794,61 | €200,52 | €5,10 |
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
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.952,79 | €1.562,50 | €3.125,00 | €50,00 | €-44,08 |
| TEST | Combo Trend | 1 | €9.912,21 | €207,30 | €414,61 | €49,75 | €18,92 |
| TEST | Combo Scanner | 1 | €9.911,93 | €207,31 | €414,63 | €49,76 | €18,92 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.910,86 | €2.720,15 | €5.440,31 | €149,22 | €-33,76 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.892,75 | €-35,75 | 9 | 9 | 33,33% | 0,86 | €-3,97 | 3,17% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.325,66 | €307,40 | 6 | 6 | 83,33% | 6,48 | €51,23 | 0,44% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.261,90 | €263,41 | 5 | 5 | 80,00% | 5,90 | €52,68 | 0,76% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.197,70 | €123,26 | 3 | 3 | 66,67% | 3,27 | €41,09 | 1,02% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.083,39 | €83,39 | 4 | 4 | 50,00% | 2,38 | €20,85 | 0,60% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.076,46 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,02% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.058,37 | €48,53 | 2 | 2 | 50,00% | 1,96 | €24,27 | 0,51% |
| TEST | Ampia 4H | Confluenza trend | €10.046,24 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,59% |
| TEST | Combo Adaptive | Combo Adaptive | €10.024,48 | €5,60 | 5 | 5 | 40,00% | 1,05 | €1,12 | 0,75% |
| TEST | Rapida 1H | Momentum / breakout | €10.022,58 | €22,15 | 22 | 22 | 40,91% | 1,05 | €1,01 | 2,34% |
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
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.952,79 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Combo Trend | Combo Trend | €9.912,21 | €-106,47 | 3 | 3 | 0,00% | 0,00 | €-35,49 | 1,48% |
| TEST | Combo Scanner | Combo Scanner | €9.911,93 | €-106,75 | 2 | 2 | 0,00% | 0,00 | €-53,37 | 1,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.910,86 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,89% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64096,30000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €-24,63 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-43,60 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,21674 | 0,21360 | 0,24275 | 0,28790 | 0,17772 | €139,85 | €419,55 | €50,35 | €6,07 |
| Rapida 1H | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00086 | 0,00086 | 0,00075 | 0,00058 | 0,00101 | €139,26 | €417,77 | €50,13 | €-0,08 |
| Rapida 1H | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,07307 | 0,07308 | 0,07388 | 0,09706 | 0,07184 | €1.474,91 | €4.424,73 | €49,56 | €-0,89 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07308 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-12,81 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 544,67000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €28,40 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64096,30000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €-19,11 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-34,32 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,21360 | 0,25846 | 0,39091 | 0,18303 | €211,57 | €423,15 | €0,00 | €77,48 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,16194 | 0,16204 | 0,16511 | 0,24210 | 0,15403 | €1.304,57 | €2.609,14 | €51,00 | €-1,57 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64096,30000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €-33,76 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00082 | 0,00086 | 0,00072 | 0,00041 | 0,00102 | €215,75 | €431,50 | €51,78 | €19,69 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,21360 | 0,24741 | 0,33025 | 0,16789 | €209,34 | €418,67 | €50,24 | €13,85 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16194 | 0,16204 | 0,16479 | 0,24210 | 0,15624 | €1.429,76 | €2.859,53 | €50,31 | €-1,72 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00086 | 0,00086 | 0,00075 | 0,00043 | 0,00108 | €213,80 | €427,59 | €51,31 | €-0,09 |
| Global Confluence puro 1H | BTC | LONG | Global Confluence puro | 60m | 2,0x | 65013,44009 | 64096,30000 | 63973,22505 | 32831,78724 | 67613,97769 | €1.562,50 | €3.125,00 | €50,00 | €-44,08 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00082 | 0,00086 | 0,00072 | 0,00041 | 0,00103 | €207,30 | €414,61 | €49,75 | €18,92 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00082 | 0,00086 | 0,00072 | 0,00041 | 0,00103 | €207,31 | €414,63 | €49,76 | €18,92 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00082 | 0,00086 | 0,00072 | 0,00041 | 0,00102 | €209,60 | €419,20 | €50,30 | €19,13 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1893,00242 | €-55,15 | -1,10 | STOP |
| Combo Scanner | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 550,85746 | €-53,00 | -1,06 | STOP |
| Combo Trend | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 549,27606 | €-52,70 | -1,05 | STOP |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 557,65511 | €-53,72 | -1,06 | STOP |
| Scanner Top 5 Long 1H | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1892,02053 | €-56,09 | -1,09 | STOP |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | 2026-07-16T09:22:55+00:00 | 552,27854 | €72,29 | 1,44 | TARGET |
| Rapida 1H | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1898,82706 | €-56,51 | -1,12 | STOP |
| Principale 4H | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 555,85670 | €24,29 | 0,49 | STOP |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | 2026-07-16T07:03:56+00:00 | 0,00082 | €111,59 | 2,19 | TARGET |
| Rapida 1H | AKE | LONG | 2026-07-16T07:03:56+00:00 | 0,00084 | €74,25 | 1,49 | TARGET |
| Scanner Top 5 Long 1H | AKE | LONG | 2026-07-16T04:25:04+00:00 | 0,00081 | €101,90 | 1,99 | TARGET |
| Combo Adaptive | AKE | LONG | 2026-07-16T04:25:04+00:00 | 0,00081 | €99,78 | 1,99 | TARGET |

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
| MAIN | Principale 4H | 10/30 | 9/30 | 0,48 | 0,86 | -0,43R | €-3,97 | 3,17% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 2/30 | 2/30 | 1,18 | 0,70 | 0,10R | €-1,60 | 0,16% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H | 42/30 | 8/30 | 0,82 | 1,47 | -0,13R | €9,31 | 1,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H | 48/30 | 22/30 | 0,50 | 1,05 | -0,39R | €1,01 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 8/30 | 3/30 | 0,39 | 2,66 | -0,55R | €29,02 | 1,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 7/30 | 4/30 | 0,96 | 2,38 | -0,03R | €20,85 | 0,60% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 7/30 | 5/30 | 1,36 | 1,05 | 0,22R | €1,12 | 0,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 1/30 | 1/30 | ∞ | ∞ | 1,52R | €76,46 | 0,02% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 7/30 | 2/30 | 0,80 | 0,00 | -0,16R | €-53,37 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 4/30 | 3/30 | 0,70 | 0,00 | -0,24R | €-35,49 | 1,48% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 3/30 | 3/30 | 1,15 | 3,27 | 0,11R | €41,09 | 1,02% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 8/30 | 1/30 | 0,69 | 0,00 | -0,25R | €-50,62 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 0/30 | 0,00 | 0,00 | -1,10R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H | 28/30 | 7/30 | 0,57 | 1,56 | -0,36R | €12,63 | 1,36% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 3/30 | 2/30 | 0,98 | 1,96 | -0,01R | €24,27 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 7/30 | 5/30 | 1,51 | 5,90 | 0,31R | €52,68 | 0,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 10/30 | 6/30 | 1,22 | 6,48 | 0,14R | €51,23 | 0,44% | COERENTE + | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07308**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.0 min | OK |
| Global DOGE | -5.0 | OK |
| Classic raw | -1.0 | NO |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64096.3 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation**
- High **0.07321**; close **0.07313**; wick alta **66.7%**; volume **x0.40**

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

- Regime: **TRANSITION**
- Famiglia: **TRANSITION**
- Confidenza: **78,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Segnali contrastanti tra trend BTC, breadth e forza delle altcoin.
- BTC trend score: **3,00**; ADX: **28,64**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-0,48%**; dispersione: **8,25%**

- Aperti in questo ciclo: **18**
- Chiusi in questo ciclo: **24**
- Posizioni research aperte: **72**
- Trade research chiusi: **196**
- Eventi di mercato indipendenti chiusi: **91**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **453**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| RSI_EXTREME_SHORT_15M | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,96 |
| SHADOW_1H_BALANCED | 10 | 42 | 42 | 30,95% | 0,82 | -0,13R | €-56,32 |
| SHADOW_1H_FAST | 7 | 48 | 48 | 27,08% | 0,50 | -0,39R | €-187,47 |
| SHADOW_4H_WIDE | 7 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_BOLLINGER_MR_1H | 0 | 7 | 7 | 42,86% | 0,96 | -0,03R | €-1,87 |
| SHADOW_COMBO_ADAPTIVE | 3 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,42 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | 1 | 7 | 7 | 28,57% | 0,80 | -0,16R | €-11,00 |
| SHADOW_COMBO_TREND | 4 | 4 | 4 | 25,00% | 0,70 | -0,24R | €-9,59 |
| SHADOW_DONCHIAN_1H | 5 | 3 | 3 | 33,33% | 1,15 | 0,11R | €3,16 |
| SHADOW_EMA_TREND_1H | 8 | 8 | 8 | 25,00% | 0,69 | -0,25R | €-19,85 |
| SHADOW_GLOBAL_PURE | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_RELATIVE_STRENGTH | 8 | 28 | 28 | 21,43% | 0,57 | -0,36R | €-99,77 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 4 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_TOP5_BTC | 4 | 7 | 7 | 42,86% | 1,51 | 0,31R | €21,58 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 10 | 10 | 40,00% | 1,22 | 0,14R | €13,81 |

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
| SHADOW_1H_BALANCED | TRANSITION | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED | TREND_UP | 5 | 9 | 9 | 22,22% | 0,53 | -0,39R | €-35,16 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| SHADOW_1H_FAST | RANGE | 1 | 19 | 19 | 42,11% | 1,01 | 0,00R | €0,76 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| SHADOW_1H_FAST | TRANSITION | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | TREND_UP | 2 | 13 | 13 | 15,38% | 0,25 | -0,70R | €-90,58 |
| SHADOW_4H_WIDE | RANGE | 2 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €2,97 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,85 | -0,10R | €-4,84 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,42 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 7 | 7 | 28,57% | 0,80 | -0,16R | €-11,00 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TREND_UP | 3 | 4 | 4 | 25,00% | 0,70 | -0,24R | €-9,59 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TRANSITION | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,29 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TREND_UP | 6 | 7 | 7 | 28,57% | 0,82 | -0,14R | €-9,71 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 1,02 | 0,02R | €1,05 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 1 | 14 | 14 | 21,43% | 0,56 | -0,36R | €-49,93 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 5 | 6 | 6 | 16,67% | 0,42 | -0,51R | €-30,56 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 2,12R | €42,42 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 1 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,84 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 1,92R | €38,42 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 8 | 8 | 25,00% | 0,62 | -0,31R | €-24,61 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
