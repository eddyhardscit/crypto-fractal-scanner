# Paper trading automatico KuCoin

Generato: 2026-07-15T10:23:27+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-15T10:23:17+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-15T10:23:17+00:00 | 2026-07-15T10:23:17+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-15T10:00:00+00:00 | 2026-07-15T10:00:00+00:00 | 23,3 min | 40,0 min | OK |
| 60m | 12 | 2026-07-15T09:00:00+00:00 | 2026-07-15T09:00:00+00:00 | 1,39 h | 1,42 h | OK |
| 240m | 12 | 2026-07-15T04:00:00+00:00 | 2026-07-15T04:00:00+00:00 | 6,39 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive | HYPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | HYPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | HYPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | BTC | 240m | LONG | 7,42 | 6,00 | 0,00 | STALE_CANDLE | 6,39 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 6,49 | 6,00 | 0,00 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | SUI | 240m | LONG | 4,86 | 6,00 | 1,14 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 3,97 | 6,00 | 2,03 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | HYPE | 240m | LONG | 2,64 | 6,00 | 3,36 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | SOL | 240m | LONG | 2,61 | 6,00 | 3,39 | STALE_CANDLE | 6,39 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -1,58 | 6,00 | 4,42 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -1,48 | 6,00 | 4,52 | STALE_CANDLE | 6,39 h | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Principale 4H | XRP | 240m | LONG | 0,32 | 6,00 | 5,68 | STALE_CANDLE | 6,39 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 383.3 minuti; limite 265. |
| Rapida 1H | LAB | 60m | SHORT | -7,75 | 4,50 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | LAB | 60m | SHORT | -7,75 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | LAB | 60m | SHORT | -7,75 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | ZEC | 60m | LONG | 7,10 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | ZEC | 60m | LONG | 7,10 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | ZEC | 60m | LONG | 7,10 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H | HYPE | 60m | LONG | 6,77 | 4,50 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | HYPE | 60m | LONG | 6,77 | 5,00 | 0,00 | OPENED | 1,39 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.951,46 | -0,49% | €-48,54 | €3.000,00 | -1,62% | 3 | 7 | 28,57% | 0,77 | 2,88% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 7 | 32 | CAMPIONE INSUFFICIENTE | 30 (mancano 23) |

- Trade del Principale 4H chiusi: **7**; win rate **28,57%**; profit factor **0,77**.
- Expectancy: **€-8,49** per trade; P&L netto: **€-59,45**; max drawdown: **2,88%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €9.951,46 | €1.381,40 | €4.144,21 | €148,88 | €14,04 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.179,75 | €3.398,14 | €6.796,28 | €150,75 | €55,77 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.171,21 | €2.774,28 | €5.548,56 | €151,64 | €52,61 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.138,58 | €3.381,98 | €6.763,96 | €99,99 | €112,63 |
| TEST | Ampia 4H | 4 | €10.091,53 | €2.257,17 | €4.514,33 | €200,61 | €6,99 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Rapida 1H | 4 | €10.058,74 | €3.033,49 | €9.100,48 | €201,09 | €-0,76 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €10.016,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €10.005,28 | €532,19 | €1.064,38 | €49,75 | €56,53 |
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
| TEST | Combo Mean Reversion | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.997,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €9.996,35 | €2.278,77 | €4.557,55 | €149,98 | €-0,91 |
| TEST | Combo Scanner | 2 | €9.996,32 | €2.300,55 | €4.601,09 | €99,99 | €-0,92 |
| TEST | Combo Adaptive | 3 | €9.995,99 | €2.508,80 | €5.017,61 | €149,98 | €-1,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.989,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.985,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.983,82 | €1.562,50 | €3.125,00 | €50,00 | €-13,99 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.941,82 | €2.720,15 | €5.440,31 | €149,22 | €-3,73 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.951,46 | €-59,45 | 7 | 7 | 28,57% | 0,77 | €-8,49 | 2,88% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.179,75 | €128,52 | 2 | 2 | 100,00% | ∞ | €64,26 | 0,35% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.171,21 | €122,29 | 1 | 1 | 100,00% | ∞ | €122,29 | 0,32% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.138,58 | €30,64 | 1 | 1 | 100,00% | ∞ | €30,64 | 0,54% |
| TEST | Ampia 4H | Confluenza trend | €10.091,53 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,51% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Rapida 1H | Momentum / breakout | €10.058,74 | €64,96 | 17 | 17 | 47,06% | 1,17 | €3,82 | 1,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.016,56 | €16,56 | 2 | 2 | 50,00% | 1,30 | €8,28 | 0,48% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.005,28 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,51% |
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
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.997,11 | €-2,89 | 1 | 1 | 0,00% | 0,00 | €-2,89 | 0,03% |
| TEST | Combo Trend | Combo Trend | €9.996,35 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,04% |
| TEST | Combo Scanner | Combo Scanner | €9.996,32 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,04% |
| TEST | Combo Adaptive | Combo Adaptive | €9.995,99 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,04% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.989,21 | €-10,79 | 1 | 1 | 0,00% | 0,00 | €-10,79 | 0,11% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.985,56 | €-14,44 | 1 | 1 | 0,00% | 0,00 | €-14,44 | 0,14% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.983,82 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,21% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.941,82 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,68% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64722,30000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €-2,72 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 539,89796 | 565,09000 | 509,03713 | 362,63146 | 601,61962 | €290,77 | €872,31 | €49,86 | €40,70 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-23,94 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,24273 | 0,24278 | 0,27186 | 0,32243 | 0,19904 | €139,75 | €419,24 | €50,31 | €-0,08 |
| Rapida 1H | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 67,96459 | 67,95100 | 66,95436 | 45,64955 | 69,47994 | €1.128,16 | €3.384,49 | €50,31 | €-0,68 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07384 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-26,45 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 565,09000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €54,40 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64722,30000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €-2,11 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-18,85 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1865,88310 | 1881,49000 | 1831,70908 | 942,27097 | 1951,31818 | €1.364,99 | €2.729,97 | €50,00 | €22,83 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,24278 | 0,29286 | 0,39091 | 0,18303 | €211,57 | €423,15 | €50,78 | €30,26 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 67,96459 | 67,95100 | 66,52140 | 34,32212 | 71,57256 | €1.197,72 | €2.395,44 | €50,87 | €-0,48 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64722,30000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €-3,73 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1865,88310 | 1881,49000 | 1835,12648 | 942,27097 | 1927,39636 | €1.516,65 | €3.033,30 | €50,00 | €25,37 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 555,77113 | 565,09000 | 540,20737 | 280,66442 | 586,89867 | €906,34 | €1.812,67 | €50,76 | €30,39 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28111 | 0,24278 | 0,26803 | 0,42027 | 0,21365 | €207,27 | €414,54 | €0,00 | €56,53 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1865,88310 | 1881,49000 | 1835,12648 | 942,27097 | 1933,54767 | €1.516,65 | €3.033,30 | €50,00 | €25,37 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 538,68772 | 565,09000 | 552,69101 | 272,03730 | 572,12052 | €890,18 | €1.780,35 | €0,00 | €87,26 |
| Global Confluence puro 1H | BTC | LONG | Global Confluence puro | 60m | 2,0x | 65013,44009 | 64722,30000 | 63973,22505 | 32831,78724 | 67613,97769 | €1.562,50 | €3.125,00 | €50,00 | €-13,99 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 565,20302 | 565,09000 | 549,38594 | 285,42752 | 600,00058 | €893,34 | €1.786,69 | €50,00 | €-0,36 |
| Combo Trend | LAB | SHORT | Combo Trend | 60m | 2,0x | 0,24273 | 0,24278 | 0,27186 | 0,36288 | 0,17865 | €208,30 | €416,61 | €49,99 | €-0,08 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 67,96459 | 67,95100 | 66,52140 | 34,32212 | 71,13960 | €1.177,13 | €2.354,26 | €49,99 | €-0,47 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 565,20302 | 565,09000 | 550,96765 | 285,42752 | 596,52083 | €992,60 | €1.985,21 | €50,00 | €-0,40 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 67,96459 | 67,95100 | 66,66572 | 34,32212 | 70,82210 | €1.307,94 | €2.615,89 | €49,99 | €-0,52 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 565,20302 | 565,09000 | 550,96765 | 285,42752 | 593,67375 | €992,60 | €1.985,21 | €50,00 | €-0,40 |
| Combo Adaptive | LAB | SHORT | Combo Adaptive | 60m | 2,0x | 0,24273 | 0,24278 | 0,27186 | 0,36288 | 0,18448 | €208,30 | €416,60 | €49,99 | €-0,08 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 67,96459 | 67,95100 | 66,66572 | 34,32212 | 70,56233 | €1.307,90 | €2.615,80 | €49,99 | €-0,52 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | 2026-07-15T08:29:20+00:00 | 0,00000 | €71,51 | 1,43 | TARGET |
| Rapida 1H | PEPE | LONG | 2026-07-15T08:29:20+00:00 | 0,00000 | €-54,31 | -1,08 | STOP |
| Rapida 1H | LAB | SHORT | 2026-07-15T06:01:30+00:00 | 0,23056 | €74,79 | 1,49 | TARGET |
| Principale 4H | HYPE | SHORT | 2026-07-15T03:39:33+00:00 | 66,46507 | €-52,08 | -1,03 | STOP |
| Scanner Top 5 Long 1H | ZEC | LONG | 2026-07-15T00:07:50+00:00 | 568,96736 | €97,88 | 1,95 | TARGET |
| Scalp RSI Short 75 · prudente · 5x | ZEC | SHORT | 2026-07-15T00:07:50+00:00 | 565,26797 | €-10,79 | -1,08 | STOP |
| Scalp RSI Short 75 · €50 · 15x | ZEC | SHORT | 2026-07-15T00:07:50+00:00 | 565,26797 | €-14,44 | -1,08 | STOP |
| Scalp RSI Short 75 · €10 · 15x | ZEC | SHORT | 2026-07-15T00:07:50+00:00 | 565,26797 | €-2,89 | -1,08 | STOP |
| Benchmark Donchian breakout 1H | ZEC | LONG | 2026-07-15T00:07:50+00:00 | 566,85249 | €122,29 | 2,45 | TARGET |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | 2026-07-15T00:07:50+00:00 | 1891,13532 | €-54,96 | -1,10 | STOP |
| Scanner Top 5 Long 1H | ZEC | LONG | 2026-07-14T19:58:20+00:00 | 537,68865 | €30,64 | 0,61 | STOP |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-07-14T19:58:20+00:00 | 537,68865 | €30,64 | 0,61 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07384**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.4 min | OK |
| Global DOGE | -5.0 | OK |
| Classic raw | -1.0 | NO |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64722.3 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation, volume_valid**
- High **0.07386**; close **0.07378**; wick alta **42.1%**; volume **x2.23**

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
- Confidenza: **82,20%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 83% sopra EMA50, ADX 26.2.
- BTC trend score: **4,00**; ADX: **26,15**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **0,32%**; dispersione: **13,51%**

- Aperti in questo ciclo: **20**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **77**
- Trade research chiusi: **114**
- Eventi di mercato indipendenti chiusi: **62**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **265**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| RSI_EXTREME_SHORT_15M | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_1H_BALANCED | 9 | 30 | 30 | 26,67% | 0,66 | -0,26R | €-79,31 |
| SHADOW_1H_FAST | 6 | 35 | 35 | 25,71% | 0,47 | -0,42R | €-146,79 |
| SHADOW_4H_WIDE | 8 | 7 | 7 | 14,29% | 0,45 | -0,48R | €-33,73 |
| SHADOW_BOLLINGER_MR_1H | 1 | 3 | 3 | 33,33% | 0,65 | -0,26R | €-7,73 |
| SHADOW_COMBO_ADAPTIVE | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 4 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_EMA_TREND_1H | 8 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_GLOBAL_PURE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 8 | 20 | 20 | 15,00% | 0,37 | -0,56R | €-112,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 2 | 2 | 50,00% | 2,00 | 0,53R | €10,70 |
| SHADOW_SCANNER_TOP5_LONG | 6 | 2 | 2 | 50,00% | 1,81 | 0,43R | €8,70 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 0 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| MAIN | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 2 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 2 | 14 | 14 | 35,71% | 1,03 | 0,02R | €2,86 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| SHADOW_1H_BALANCED | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 0,93 | -0,04R | €-2,22 |
| SHADOW_1H_FAST | RANGE | 2 | 18 | 18 | 38,89% | 0,89 | -0,07R | €-12,99 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| SHADOW_1H_FAST | TREND_UP | 3 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,82 |
| SHADOW_4H_WIDE | RANGE | 3 | 7 | 7 | 14,29% | 0,45 | -0,48R | €-33,73 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €2,97 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,70 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TREND_UP | 7 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 3 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 2 | 13 | 13 | 15,38% | 0,38 | -0,55R | €-70,96 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 1 | 1 | 100,00% | ∞ | 2,14R | €21,39 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 1 | 1 | 100,00% | ∞ | 1,94R | €19,39 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
