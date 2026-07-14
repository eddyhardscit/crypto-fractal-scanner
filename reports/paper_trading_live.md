# Paper trading automatico KuCoin

Generato: 2026-07-14T17:23:08+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-14T17:22:58+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-14T17:22:58+00:00 | 2026-07-14T17:22:58+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-14T17:00:00+00:00 | 2026-07-14T17:00:00+00:00 | 23,0 min | 40,0 min | OK |
| 60m | 12 | 2026-07-14T16:00:00+00:00 | 2026-07-14T16:00:00+00:00 | 1,38 h | 1,42 h | OK |
| 240m | 12 | 2026-07-14T12:00:00+00:00 | 2026-07-14T12:00:00+00:00 | 5,38 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | 240m | LONG | 8,75 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: Hidden bearish [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 8,12 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 7,85 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | SUI | 240m | LONG | 7,08 | 6,00 | 0,00 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -4,25 | 6,00 | 1,75 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | HYPE | 240m | SHORT | -4,10 | 6,00 | 1,90 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | SOL | 240m | LONG | 1,49 | 6,00 | 4,51 | STALE_CANDLE | 5,38 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | ALLO | 240m | LONG | 1,06 | 6,00 | 4,94 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | XRP | 240m | LONG | 0,83 | 6,00 | 5,17 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | EVAA | 240m | LONG | 0,75 | 6,00 | 5,25 | STALE_CANDLE | 5,38 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -0,72 | 6,00 | 5,28 | STALE_CANDLE | 5,38 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 323.0 minuti; limite 265. |
| Scalp RSI Short 80 · €10 · 15x | ZEC | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤75.0 in rientro. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 75 · €10 · 15x | ZEC | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤70.0 in rientro. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 80 · €50 · 15x | ZEC | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤75.0 in rientro. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 75 · €50 · 15x | ZEC | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤70.0 in rientro. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 80 · prudente · 5x | ZEC | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤75.0 in rientro. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 75 · prudente · 5x | ZEC | 15m | SHORT | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≤70.0 in rientro. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 85 · €10 · 15x | ZEC | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥85.0. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |
| Scalp RSI Short 85 · €50 · 15x | ZEC | 15m | SHORT | 8,00 | 8,00 | 0,00 | STRATEGY_FILTER | 23,0 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥85.0. RSI 83.7→79.9; volume x3.85; shock 2.25 ATR. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.967,68 | -0,32% | €-32,32 | €3.000,00 | -1,08% | 4 | 6 | 33,33% | 0,96 | 2,44% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 6 | 24 | CAMPIONE INSUFFICIENTE | 30 (mancano 24) |

- Trade del Principale 4H chiusi: **6**; win rate **33,33%**; profit factor **0,96**.
- Expectancy: **€-1,23** per trade; P&L netto: **€-7,37**; max drawdown: **2,44%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.967,68 | €1.796,43 | €5.389,28 | €199,43 | €-21,91 |
| TEST | Forza relativa 1H | 4 | €10.090,88 | €2.607,73 | €5.215,46 | €200,81 | €3,62 |
| TEST | Bilanciata 1H | 4 | €10.076,93 | €1.737,28 | €5.211,83 | €200,67 | €3,61 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.068,84 | €3.447,49 | €6.894,98 | €99,99 | €72,98 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.068,84 | €3.447,49 | €6.894,98 | €99,99 | €72,98 |
| TEST | Ampia 4H | 4 | €10.068,25 | €2.257,17 | €4.514,33 | €200,61 | €-16,53 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.063,02 | €2.225,33 | €4.450,66 | €50,00 | €65,69 |
| TEST | Rapida 1H | 2 | €10.041,30 | €1.765,58 | €5.296,75 | €100,48 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.025,01 | €3.177,40 | €6.354,79 | €50,00 | €28,82 |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 1 | €9.952,56 | €324,92 | €649,84 | €49,75 | €3,57 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.932,01 | €2.720,15 | €5.440,31 | €149,22 | €-14,10 |

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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.967,68 | €-7,37 | 6 | 6 | 33,33% | 0,96 | €-1,23 | 2,44% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.090,88 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Bilanciata 1H | Confluenza trend | €10.076,93 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.068,84 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,06% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.068,84 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,06% |
| TEST | Ampia 4H | Confluenza trend | €10.068,25 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,46% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.063,02 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,04% |
| TEST | Rapida 1H | Momentum / breakout | €10.041,30 | €44,48 | 15 | 15 | 46,67% | 1,14 | €2,97 | 1,79% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.025,01 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.952,56 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,51% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.932,01 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,68% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 63,85923 | 64,64400 | 66,45178 | 84,82634 | 58,67412 | €415,02 | €1.245,07 | €50,55 | €-15,30 |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64439,19000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €-12,63 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 539,89796 | 548,96000 | 509,03713 | 362,63146 | 601,61962 | €290,77 | €872,31 | €49,86 | €14,64 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-8,62 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37375 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €3,61 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07425 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-33,81 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 548,96000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €33,86 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64439,19000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €-9,80 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-6,79 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37375 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €3,62 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1865,88310 | 1865,43000 | 1831,70908 | 942,27097 | 1951,31818 | €1.364,99 | €2.729,97 | €50,00 | €-0,66 |
| Benchmark Donchian breakout 1H | ZEC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 528,57569 | 548,96000 | 536,20138 | 266,93073 | 566,96589 | €860,34 | €1.720,69 | €0,00 | €66,36 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1865,13690 | 1865,43000 | 1890,75716 | 2788,37966 | 1826,70650 | €1.819,98 | €3.639,96 | €50,00 | €-0,57 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.357,41 | €2.714,83 | €0,00 | €29,39 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64439,19000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €-17,31 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37375 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €3,21 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1865,88310 | 1865,43000 | 1835,12648 | 942,27097 | 1927,39636 | €1.516,65 | €3.033,30 | €50,00 | €-0,74 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 528,57569 | 548,96000 | 537,79621 | 266,93073 | 556,21663 | €955,69 | €1.911,38 | €0,00 | €73,71 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37375 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €3,57 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1865,88310 | 1865,43000 | 1835,12648 | 942,27097 | 1933,54767 | €1.516,65 | €3.033,30 | €50,00 | €-0,74 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 528,57569 | 548,96000 | 537,79621 | 266,93073 | 558,98073 | €955,69 | €1.911,38 | €0,00 | €73,71 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida 1H | PEPE | LONG | 2026-07-14T17:23:05+00:00 | 0,00000 | €-54,54 | -1,08 | STOP |
| Principale 4H | DOGE | SHORT | 2026-07-14T16:00:54+00:00 | 0,07452 | €-51,90 | -1,04 | STOP |
| Forza relativa 1H | HYPE | SHORT | 2026-07-14T14:14:01+00:00 | 64,52242 | €-54,29 | -1,07 | STOP |
| Rapida 1H | ETH | LONG | 2026-07-14T14:14:01+00:00 | 1825,87785 | €69,23 | 1,37 | TARGET |
| Bilanciata 1H | SOL | SHORT | 2026-07-14T14:14:01+00:00 | 75,75154 | €-55,49 | -1,10 | STOP |
| Scanner Bottom 5 Short 1H | LAB | SHORT | 2026-07-14T12:33:59+00:00 | 0,30162 | €-50,62 | -1,01 | STOP |
| Benchmark trend following EMA 1H | LAB | SHORT | 2026-07-14T12:33:59+00:00 | 0,30162 | €-50,62 | -1,01 | STOP |
| Rapida 1H | LAB | SHORT | 2026-07-14T12:33:59+00:00 | 0,30162 | €-51,02 | -1,01 | STOP |
| Forza relativa 1H | VELVET | LONG | 2026-07-14T11:10:12+00:00 | 0,59610 | €0,36 | 0,01 | STOP |
| Ampia 4H | EVAA | SHORT | 2026-07-14T11:10:12+00:00 | 0,92547 | €-1,00 | -0,02 | STOP |
| Rapida 1H | SOL | SHORT | 2026-07-14T11:10:12+00:00 | 75,50720 | €-57,06 | -1,13 | STOP |
| Bilanciata 1H | VELVET | LONG | 2026-07-14T11:10:12+00:00 | 0,59666 | €4,94 | 0,10 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07425**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.1 min | OK |
| Global DOGE | -5.0 | OK |
| Classic raw | -7.0 | OK |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64439.19 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07454**; close **0.07432**; wick alta **0.0%**; volume **x1.46**

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
- Confidenza: **79,60%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 75% sopra EMA50, ADX 25.6.
- BTC trend score: **4,00**; ADX: **25,65**; breadth sopra EMA50: **75,00%**
- Mediana alt vs BTC: **0,38%**; dispersione: **15,65%**

- Aperti in questo ciclo: **4**
- Chiusi in questo ciclo: **3**
- Posizioni research aperte: **65**
- Trade research chiusi: **87**
- Eventi di mercato indipendenti chiusi: **45**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **159**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 9 | 9 | 22,22% | 0,55 | -0,36R | €-32,23 |
| SHADOW_1H_BALANCED | 8 | 28 | 28 | 28,57% | 0,73 | -0,21R | €-57,63 |
| SHADOW_1H_FAST | 8 | 28 | 28 | 28,57% | 0,55 | -0,34R | €-96,58 |
| SHADOW_4H_WIDE | 10 | 4 | 4 | 25,00% | 0,92 | -0,06R | €-2,53 |
| SHADOW_BOLLINGER_MR_1H | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | 7 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_RELATIVE_STRENGTH | 8 | 15 | 15 | 13,33% | 0,33 | -0,60R | €-90,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 1 | 1 | 100,00% | ∞ | 1,94R | €19,39 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 1 | 9 | 9 | 22,22% | 0,55 | -0,36R | €-32,23 |
| MAIN | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 3 | 13 | 13 | 38,46% | 1,16 | 0,10R | €13,58 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 1 | 8 | 8 | 0,00% | 0,00 | -1,08R | €-86,29 |
| SHADOW_1H_BALANCED | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 4 | 16 | 16 | 43,75% | 1,09 | 0,05R | €8,07 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 1 | 9 | 9 | 0,00% | 0,00 | -1,09R | €-98,53 |
| SHADOW_1H_FAST | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | RANGE | 6 | 4 | 4 | 25,00% | 0,92 | -0,06R | €-2,53 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 7 | 8 | 8 | 12,50% | 0,31 | -0,62R | €-49,56 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 1 | 1 | 100,00% | ∞ | 1,94R | €19,39 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
