# Paper trading automatico KuCoin

Generato: 2026-07-16T11:23:11+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-16T11:19:17+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-16T11:19:17+00:00 | 2026-07-16T11:19:17+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-16T11:00:00+00:00 | 2026-07-16T11:00:00+00:00 | 4,3 min | 25,0 min | OK |
| 60m | 12 | 2026-07-16T10:00:00+00:00 | 2026-07-16T10:00:00+00:00 | 19,3 min | 45,0 min | OK |
| 240m | 12 | 2026-07-16T04:00:00+00:00 | 2026-07-16T04:00:00+00:00 | 3,32 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,91 | 6,00 | 0,00 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -5,95 | 6,00 | 0,05 | STALE_CANDLE | 3,32 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -5,08 | 6,00 | 0,92 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -4,80 | 6,00 | 1,20 | STALE_CANDLE | 3,32 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | 0G | 240m | SHORT | -3,96 | 6,00 | 2,04 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,08 | 6,00 | 2,92 | STALE_CANDLE | 3,32 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 0,97 | 6,00 | 5,03 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,66 | 6,00 | 5,34 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 0,58 | 6,00 | 5,42 | STALE_CANDLE | 3,32 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 199.3 minuti; tolleranza 60 minuti. |
| Rapida 1H | SOL | 60m | SHORT | -7,27 | 4,50 | 0,00 | STRATEGY_FILTER | 19,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.79%. |
| Forza relativa 1H | SOL | 60m | SHORT | -7,27 | 4,00 | 0,00 | STRATEGY_FILTER | 19,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-1.33%. |
| Bilanciata 1H | SOL | 60m | SHORT | -7,27 | 5,00 | 0,00 | RISK_GATE | 19,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Scanner Bottom 5 Short 1H | SOL | 60m | SHORT | -7,27 | 5,00 | 0,00 | RISK_GATE | 19,3 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Bilanciata 1H | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | RISK_GATE | 19,3 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Rapida 1H | LAB | 60m | SHORT | -7,00 | 4,50 | 0,00 | RISK_GATE | 19,3 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Forza relativa 1H | LAB | 60m | SHORT | -7,00 | 4,00 | 0,00 | RISK_GATE | 19,3 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Bilanciata 1H | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | RISK_GATE | 19,3 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.892,75 | -1,07% | €-107,25 | €3.000,00 | -3,58% | 2 | 9 | 33,33% | 0,86 | 3,17% |

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
| TEST | Scanner Top 5 Long 1H | 2 | €10.350,58 | €1.190,90 | €2.381,80 | €49,99 | €44,61 |
| TEST | Scanner Top 5 + forza BTC 1H | 2 | €10.285,51 | €1.188,95 | €2.377,89 | €101,30 | €23,53 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.196,91 | €1.516,14 | €3.032,28 | €51,00 | €75,13 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.081,73 | €210,07 | €420,14 | €50,42 | €-1,41 |
| TEST | Combo Mean Reversion | 0 | €10.076,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.057,73 | €1.964,02 | €3.928,04 | €150,30 | €11,34 |
| TEST | Rapida 1H | 4 | €10.049,86 | €2.598,20 | €7.794,61 | €200,52 | €32,38 |
| TEST | Ampia 4H | 4 | €10.048,98 | €2.257,17 | €4.514,33 | €200,61 | €-35,09 |
| TEST | Combo Adaptive | 1 | €10.048,69 | €209,60 | €419,20 | €0,00 | €43,34 |
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
| TEST | Global Confluence puro 1H | 1 | €9.953,56 | €1.562,50 | €3.125,00 | €50,00 | €-43,32 |
| TEST | Combo Trend | 1 | €9.936,15 | €207,30 | €414,61 | €49,75 | €42,87 |
| TEST | Combo Scanner | 1 | €9.935,87 | €207,31 | €414,63 | €49,76 | €42,87 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.911,62 | €2.720,15 | €5.440,31 | €149,22 | €-32,99 |

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
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.350,58 | €307,40 | 6 | 6 | 83,33% | 6,48 | €51,23 | 0,44% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.285,51 | €263,41 | 5 | 5 | 80,00% | 5,90 | €52,68 | 0,76% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.196,91 | €123,26 | 3 | 3 | 66,67% | 3,27 | €41,09 | 1,02% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.081,73 | €83,39 | 4 | 4 | 50,00% | 2,38 | €20,85 | 0,60% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.076,46 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,02% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.057,73 | €48,53 | 2 | 2 | 50,00% | 1,96 | €24,27 | 0,51% |
| TEST | Rapida 1H | Momentum / breakout | €10.049,86 | €22,15 | 22 | 22 | 40,91% | 1,05 | €1,01 | 2,34% |
| TEST | Ampia 4H | Confluenza trend | €10.048,98 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,59% |
| TEST | Combo Adaptive | Combo Adaptive | €10.048,69 | €5,60 | 5 | 5 | 40,00% | 1,05 | €1,12 | 0,75% |
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
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.953,56 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Combo Trend | Combo Trend | €9.936,15 | €-106,47 | 3 | 3 | 0,00% | 0,00 | €-35,49 | 1,48% |
| TEST | Combo Scanner | Combo Scanner | €9.935,87 | €-106,75 | 2 | 2 | 0,00% | 0,00 | €-53,37 | 1,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.911,62 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,89% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64112,28000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €-24,07 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-44,16 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,21674 | 0,21299 | 0,24275 | 0,28790 | 0,17772 | €139,85 | €419,55 | €50,35 | €7,25 |
| Rapida 1H | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00086 | 0,00090 | 0,00075 | 0,00058 | 0,00101 | €139,26 | €417,77 | €50,13 | €22,99 |
| Rapida 1H | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,07307 | 0,07303 | 0,07388 | 0,09706 | 0,07184 | €1.474,91 | €4.424,73 | €49,56 | €2,14 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07303 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-11,91 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 546,13000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €30,26 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64112,28000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €-18,68 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-34,77 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,21299 | 0,25585 | 0,39091 | 0,18303 | €211,57 | €423,15 | €0,00 | €78,47 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,16194 | 0,16215 | 0,16511 | 0,24210 | 0,15403 | €1.304,57 | €2.609,14 | €51,00 | €-3,34 |
| Benchmark Bollinger mean reversion 1H | AKE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00090 | 0,00090 | 0,00101 | 0,00135 | 0,00074 | €210,07 | €420,14 | €50,42 | €-1,41 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64112,28000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €-32,99 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00082 | 0,00090 | 0,00082 | 0,00041 | 0,00102 | €215,75 | €431,50 | €0,00 | €44,61 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,21299 | 0,24741 | 0,33025 | 0,16789 | €209,34 | €418,67 | €50,24 | €15,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16194 | 0,16215 | 0,16479 | 0,24210 | 0,15624 | €1.429,76 | €2.859,53 | €50,31 | €-3,66 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00086 | 0,00090 | 0,00075 | 0,00043 | 0,00108 | €213,80 | €427,59 | €51,31 | €23,53 |
| Global Confluence puro 1H | BTC | LONG | Global Confluence puro | 60m | 2,0x | 65013,44009 | 64112,28000 | 63973,22505 | 32831,78724 | 67613,97769 | €1.562,50 | €3.125,00 | €50,00 | €-43,32 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00082 | 0,00090 | 0,00072 | 0,00041 | 0,00103 | €207,30 | €414,61 | €49,75 | €42,87 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00082 | 0,00090 | 0,00072 | 0,00041 | 0,00103 | €207,31 | €414,63 | €49,76 | €42,87 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00082 | 0,00090 | 0,00082 | 0,00041 | 0,00102 | €209,60 | €419,20 | €0,00 | €43,34 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1892,02053 | €-56,09 | -1,09 | STOP |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 557,65511 | €-53,72 | -1,06 | STOP |
| Combo Trend | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 549,27606 | €-52,70 | -1,05 | STOP |
| Combo Scanner | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 550,85746 | €-53,00 | -1,06 | STOP |
| Combo Adaptive | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1893,00242 | €-55,15 | -1,10 | STOP |
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
