# Paper trading automatico KuCoin

Generato: 2026-07-15T17:23:19+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-15T17:23:11+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-15T17:23:11+00:00 | 2026-07-15T17:23:11+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-15T17:00:00+00:00 | 2026-07-15T17:00:00+00:00 | 23,2 min | 40,0 min | OK |
| 60m | 12 | 2026-07-15T16:00:00+00:00 | 2026-07-15T16:00:00+00:00 | 1,39 h | 1,42 h | OK |
| 240m | 12 | 2026-07-15T12:00:00+00:00 | 2026-07-15T12:00:00+00:00 | 5,39 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive | AKE | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | AKE | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | AKE | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BTC | 240m | LONG | 9,42 | 6,00 | 0,00 | STALE_CANDLE | 5,39 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 7,26 | 6,00 | 0,00 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 6,04 | 6,00 | 0,00 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | AKE | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | XRP | 240m | LONG | 3,80 | 6,00 | 2,20 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | SOL | 240m | LONG | 3,45 | 6,00 | 2,55 | STALE_CANDLE | 5,39 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -3,09 | 6,00 | 2,91 | STALE_CANDLE | 5,39 h | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | HYPE | 240m | LONG | 2,78 | 6,00 | 3,22 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -2,50 | 6,00 | 3,50 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -0,18 | 6,00 | 5,82 | STALE_CANDLE | 5,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.2 minuti; limite 265. |
| Scanner Top 5 Long 1H | BTC | 60m | LONG | 7,92 | 5,00 | 0,00 | READY | 1,39 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | BTC | 60m | LONG | 7,92 | 5,00 | 0,00 | READY | 1,39 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom 5 Short 1H | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H | ETH | 60m | LONG | 6,76 | 4,50 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | ETH | 60m | LONG | 6,76 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | ETH | 60m | LONG | 6,76 | 5,00 | 0,00 | READY | 1,39 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | ETH | 60m | LONG | 6,76 | 5,00 | 0,00 | READY | 1,39 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H | AKE | 60m | LONG | 6,75 | 4,50 | 0,00 | READY | 1,39 h | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.978,18 | -0,22% | €-21,82 | €3.000,00 | -0,73% | 3 | 8 | 25,00% | 0,77 | 2,88% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 8 | 39 | CAMPIONE INSUFFICIENTE | 30 (mancano 22) |

- Trade del Principale 4H chiusi: **8**; win rate **25,00%**; profit factor **0,77**.
- Expectancy: **€-7,50** per trade; P&L netto: **€-60,04**; max drawdown: **2,88%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €9.978,18 | €1.381,40 | €4.144,21 | €99,02 | €41,76 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.257,50 | €2.799,01 | €5.598,01 | €152,59 | €-0,73 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.237,66 | €1.409,29 | €2.818,59 | €50,87 | €61,69 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.208,18 | €2.152,20 | €4.304,40 | €151,83 | €5,22 |
| TEST | Ampia 4H | 4 | €10.111,44 | €2.257,17 | €4.514,33 | €200,61 | €27,08 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Rapida 1H | 4 | €10.085,04 | €3.469,07 | €10.407,22 | €151,24 | €31,30 |
| TEST | Combo Mean Reversion | 0 | €10.076,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Combo Trend | 3 | €10.059,99 | €2.278,77 | €4.557,55 | €99,99 | €62,72 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €10.047,81 | €534,26 | €1.068,51 | €99,99 | €-0,08 |
| TEST | Combo Adaptive | 3 | €10.046,10 | €1.725,50 | €3.451,00 | €100,22 | €33,04 |
| TEST | Combo Scanner | 2 | €10.025,39 | €2.300,55 | €4.601,09 | €99,99 | €28,15 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.008,99 | €3.091,06 | €6.182,12 | €50,08 | €-3,86 |
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
| TEST | Global Confluence puro 1H | 1 | €9.998,72 | €1.562,50 | €3.125,00 | €50,00 | €1,22 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.998,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.996,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.956,70 | €2.720,15 | €5.440,31 | €149,22 | €11,46 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.978,18 | €-60,04 | 8 | 8 | 25,00% | 0,77 | €-7,50 | 2,88% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.257,50 | €261,58 | 4 | 4 | 100,00% | ∞ | €65,40 | 0,44% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.237,66 | €177,56 | 2 | 2 | 100,00% | ∞ | €88,78 | 0,61% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.208,18 | €205,54 | 3 | 3 | 100,00% | ∞ | €68,51 | 0,61% |
| TEST | Ampia 4H | Confluenza trend | €10.111,44 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,51% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Rapida 1H | Momentum / breakout | €10.085,04 | €59,99 | 18 | 18 | 44,44% | 1,16 | €3,33 | 1,82% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.076,46 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,02% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Combo Trend | Combo Trend | €10.059,99 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,23% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.047,81 | €48,53 | 2 | 2 | 50,00% | 1,96 | €24,27 | 0,51% |
| TEST | Combo Adaptive | Combo Adaptive | €10.046,10 | €15,12 | 1 | 1 | 100,00% | ∞ | €15,12 | 0,25% |
| TEST | Combo Scanner | Combo Scanner | €10.025,39 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,69% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.008,99 | €16,56 | 2 | 2 | 50,00% | 1,30 | €8,28 | 0,60% |
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
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.998,72 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,23% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.998,01 | €-1,99 | 2 | 2 | 50,00% | 0,31 | €-1,00 | 0,04% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.996,80 | €-3,20 | 2 | 2 | 50,00% | 0,70 | €-1,60 | 0,16% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.956,70 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,68% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 65038,83000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €8,36 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 539,89796 | 574,43000 | 555,96789 | 362,63146 | 601,61962 | €290,77 | €872,31 | €0,00 | €55,79 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-22,39 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,24273 | 0,22095 | 0,24273 | 0,32243 | 0,19904 | €139,75 | €419,24 | €0,00 | €37,62 |
| Rapida 1H | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 67,96459 | 67,85400 | 66,95436 | 45,64955 | 69,47994 | €1.128,16 | €3.384,49 | €50,31 | €-5,51 |
| Rapida 1H | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,03453 | 1922,65000 | 1899,20690 | 1291,63819 | 1958,77597 | €1.356,98 | €4.070,94 | €50,44 | €-0,81 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07393 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-28,06 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 574,43000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €66,29 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 65038,83000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €6,49 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-17,63 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,22095 | 0,26148 | 0,39091 | 0,18303 | €211,57 | €423,15 | €0,00 | €65,59 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 67,96459 | 67,85400 | 66,52140 | 34,32212 | 71,57256 | €1.197,72 | €2.395,44 | €50,87 | €-3,90 |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | Bollinger mean reversion | 60m | 2,0x | 570,96578 | 574,43000 | 583,49757 | 853,59385 | 552,16811 | €1.140,92 | €2.281,84 | €50,08 | €-13,84 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1927,58441 | 1922,65000 | 1927,58441 | 2881,73869 | 1890,60858 | €1.950,14 | €3.900,28 | €0,00 | €9,98 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 65038,83000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €11,46 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00065 | 0,00065 | 0,00057 | 0,00033 | 0,00081 | €213,76 | €427,52 | €51,30 | €-0,09 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1923,03453 | 1922,65000 | 1892,39901 | 971,13244 | 1984,30556 | €1.610,10 | €3.220,20 | €51,30 | €-0,64 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22095 | 0,24741 | 0,33025 | 0,16789 | €209,34 | €418,67 | €50,24 | €-0,08 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 572,85455 | 574,43000 | 557,76666 | 289,29155 | 606,04791 | €964,37 | €1.928,74 | €50,80 | €5,30 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00065 | 0,00065 | 0,00057 | 0,00033 | 0,00082 | €212,68 | €425,35 | €51,04 | €-0,09 |
| Global Confluence puro 1H | BTC | LONG | Global Confluence puro | 60m | 2,0x | 65013,44009 | 65038,83000 | 63973,22505 | 32831,78724 | 67613,97769 | €1.562,50 | €3.125,00 | €50,00 | €1,22 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 565,20302 | 574,43000 | 549,38594 | 285,42752 | 600,00058 | €893,34 | €1.786,69 | €50,00 | €29,17 |
| Combo Trend | LAB | SHORT | Combo Trend | 60m | 2,0x | 0,24273 | 0,22095 | 0,24273 | 0,36288 | 0,17865 | €208,30 | €416,61 | €0,00 | €37,38 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 67,96459 | 67,85400 | 66,52140 | 34,32212 | 71,13960 | €1.177,13 | €2.354,26 | €49,99 | €-3,83 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 565,20302 | 574,43000 | 550,96765 | 285,42752 | 596,52083 | €992,60 | €1.985,21 | €50,00 | €32,41 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 67,96459 | 67,85400 | 66,66572 | 34,32212 | 70,82210 | €1.307,94 | €2.615,89 | €49,99 | €-4,26 |
| Combo Adaptive | LAB | SHORT | Combo Adaptive | 60m | 2,0x | 0,24273 | 0,22095 | 0,24273 | 0,36288 | 0,18448 | €208,30 | €416,60 | €0,00 | €37,38 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 67,96459 | 67,85400 | 66,66572 | 34,32212 | 70,56233 | €1.307,90 | €2.615,80 | €49,99 | €-4,26 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00065 | 0,00065 | 0,00057 | 0,00033 | 0,00081 | €209,30 | €418,60 | €50,23 | €-0,08 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
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
| Principale 4H | LAB | SHORT | 2026-07-15T15:40:23+00:00 | 0,23998 | €-0,58 | -0,01 | STOP |
| Scanner Top 5 Long 1H | ETH | LONG | 2026-07-15T14:02:37+00:00 | 1927,01088 | €95,22 | 1,90 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07393**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.3 min | OK |
| Global DOGE | -5.0 | OK |
| Classic raw | -1.0 | NO |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65038.83 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation**
- High **0.07408**; close **0.07397**; wick alta **61.1%**; volume **x0.42**

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
- Confidenza: **82,70%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 83% sopra EMA50, ADX 27.6.
- BTC trend score: **4,00**; ADX: **27,60**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **-0,18%**; dispersione: **75,47%**

- Aperti in questo ciclo: **17**
- Chiusi in questo ciclo: **9**
- Posizioni research aperte: **91**
- Trade research chiusi: **143**
- Eventi di mercato indipendenti chiusi: **76**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **392**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| RSI_EXTREME_SHORT_15M | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,96 |
| SHADOW_1H_BALANCED | 10 | 36 | 36 | 33,33% | 0,91 | -0,07R | €-23,49 |
| SHADOW_1H_FAST | 7 | 41 | 41 | 29,27% | 0,56 | -0,34R | €-137,50 |
| SHADOW_4H_WIDE | 7 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_BOLLINGER_MR_1H | 1 | 6 | 6 | 33,33% | 0,64 | -0,26R | €-15,62 |
| SHADOW_COMBO_ADAPTIVE | 6 | 2 | 2 | 100,00% | ∞ | 1,91R | €38,20 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | 5 | 1 | 1 | 100,00% | ∞ | 2,09R | €20,89 |
| SHADOW_COMBO_TREND | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 5 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_EMA_TREND_1H | 11 | 3 | 3 | 33,33% | 1,03 | 0,02R | €0,71 |
| SHADOW_GLOBAL_PURE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 10 | 22 | 22 | 22,73% | 0,61 | -0,31R | €-69,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 2 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 3 | 3 | 66,67% | 3,97 | 1,06R | €31,73 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 5 | 5 | 60,00% | 2,71 | 0,73R | €36,50 |

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
| SHADOW_1H_BALANCED | TREND_UP | 9 | 3 | 3 | 33,33% | 0,89 | -0,08R | €-2,33 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| SHADOW_1H_FAST | RANGE | 1 | 19 | 19 | 42,11% | 1,01 | 0,00R | €0,76 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| SHADOW_1H_FAST | TREND_UP | 6 | 6 | 6 | 16,67% | 0,27 | -0,68R | €-40,61 |
| SHADOW_4H_WIDE | RANGE | 2 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €2,97 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 4 | 4 | 25,00% | 0,43 | -0,46R | €-18,59 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 6 | 2 | 2 | 100,00% | ∞ | 1,91R | €38,20 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 5 | 1 | 1 | 100,00% | ∞ | 2,09R | €20,89 |
| SHADOW_COMBO_TREND | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TREND_UP | 10 | 2 | 2 | 50,00% | 2,02 | 0,54R | €10,84 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 1,02 | 0,02R | €1,05 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 1 | 14 | 14 | 21,43% | 0,56 | -0,36R | €-49,93 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 7 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 2,12R | €42,42 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 4 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 1,92R | €38,42 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 6 | 3 | 3 | 33,33% | 0,91 | -0,06R | €-1,91 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
