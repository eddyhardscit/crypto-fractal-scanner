# Paper trading automatico KuCoin

Generato: 2026-07-14T09:42:09+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-14T09:41:58+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-14T09:41:58+00:00 | 2026-07-14T09:41:58+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-14T09:15:00+00:00 | 2026-07-14T09:15:00+00:00 | 27,0 min | 40,0 min | OK |
| 60m | 12 | 2026-07-14T08:00:00+00:00 | 2026-07-14T08:00:00+00:00 | 1,70 h | 1,42 h | STALE_CANDLE |
| 240m | 12 | 2026-07-14T04:00:00+00:00 | 2026-07-14T04:00:00+00:00 | 5,70 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -7,72 | 6,00 | 0,00 | STALE_CANDLE | 5,70 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish invalidata [INVALIDATA] | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | XRP | 240m | SHORT | -6,11 | 6,00 | 0,00 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | SKHYNIX | 240m | SHORT | -5,75 | 6,00 | 0,25 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 5,04 | 6,00 | 0,96 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | HYPE | 240m | SHORT | -4,35 | 6,00 | 1,65 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | ALLO | 240m | LONG | 4,00 | 6,00 | 2,00 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -3,99 | 6,00 | 2,01 | STALE_CANDLE | 5,70 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 2,28 | 6,00 | 3,72 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 2,26 | 6,00 | 3,74 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Principale 4H | BTC | 240m | SHORT | -1,25 | 6,00 | 4,75 | STALE_CANDLE | 5,70 h | D: Hidden bearish [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Ampia 4H | DOGE | 240m | SHORT | -7,72 | 5,00 | 0,00 | STALE_CANDLE | 5,70 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish invalidata [INVALIDATA] | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Ampia 4H | LAB | 240m | SHORT | -6,75 | 5,00 | 0,00 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Ampia 4H | EVAA | 240m | SHORT | -6,25 | 5,00 | 0,00 | STALE_CANDLE | 5,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 342.0 minuti; limite 265. |
| Bilanciata 1H | LAB | 60m | SHORT | -6,25 | 5,00 | 0,00 | STALE_CANDLE | 1,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 102.0 minuti; limite 85. |
| Rapida 1H | LAB | 60m | SHORT | -6,25 | 4,50 | 0,00 | STALE_CANDLE | 1,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 102.0 minuti; limite 85. |
| Forza relativa 1H | LAB | 60m | SHORT | -6,25 | 4,00 | 0,00 | STALE_CANDLE | 1,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 102.0 minuti; limite 85. |
| Benchmark Donchian breakout 1H | LAB | 60m | SHORT | -6,25 | 5,00 | 0,00 | STALE_CANDLE | 1,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 102.0 minuti; limite 85. |
| Benchmark Bollinger mean reversion 1H | LAB | 60m | SHORT | -6,25 | 5,00 | 0,00 | STALE_CANDLE | 1,70 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 102.0 minuti; limite 85. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.119,26 | +1,19% | €119,26 | €3.000,00 | 3,98% | 3 | 4 | 50,00% | 1,94 | 0,96% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 4 | 16 | CAMPIONE INSUFFICIENTE | 30 (mancano 26) |

- Trade del Principale 4H chiusi: **4**; win rate **50,00%**; profit factor **1,94**.
- Expectancy: **€24,05** per trade; P&L netto: **€96,20**; max drawdown: **0,96%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €10.119,26 | €1.119,04 | €3.357,11 | €151,35 | €24,49 |
| TEST | Forza relativa 1H | 4 | €10.129,99 | €2.940,20 | €5.880,40 | €150,62 | €-10,87 |
| TEST | Ampia 4H | 3 | €10.116,65 | €1.190,22 | €2.380,44 | €99,99 | €29,90 |
| TEST | Rapida 1H | 2 | €10.113,55 | €2.395,35 | €7.186,05 | €100,65 | €-19,84 |
| TEST | Bilanciata 1H | 4 | €10.107,47 | €2.183,15 | €6.549,44 | €150,55 | €-15,42 |
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
| TEST | Benchmark Donchian breakout 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €10.119,26 | €96,20 | 4 | 4 | 50,00% | 1,94 | €24,05 | 0,96% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.129,99 | €142,33 | 5 | 5 | 60,00% | 2,37 | €28,47 | 0,98% |
| TEST | Ampia 4H | Confluenza trend | €10.116,65 | €88,07 | 2 | 2 | 50,00% | 2,71 | €44,04 | 0,90% |
| TEST | Rapida 1H | Momentum / breakout | €10.113,55 | €137,88 | 11 | 11 | 54,55% | 1,88 | €12,53 | 1,32% |
| TEST | Bilanciata 1H | Confluenza trend | €10.107,47 | €125,00 | 6 | 6 | 50,00% | 2,20 | €20,83 | 0,86% |
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
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07237 | 0,07213 | 0,07451 | 0,09613 | 0,06808 | €562,89 | €1.688,66 | €50,00 | €5,52 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 63,85923 | 63,58800 | 66,45178 | 84,82634 | 58,67412 | €415,02 | €1.245,07 | €50,55 | €5,29 |
| Principale 4H | EVAA | SHORT | Confluenza trend | 240m | 3,0x | 0,84263 | 0,81540 | 0,94375 | 1,11930 | 0,64040 | €141,12 | €423,37 | €50,80 | €13,68 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | VELVET | LONG | Confluenza trend | 60m | 3,0x | 0,59035 | 0,59035 | 0,59702 | 0,39652 | 0,70445 | €174,63 | €523,89 | €0,00 | €0,00 |
| Bilanciata 1H | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,63707 | 74,97200 | 75,73639 | 99,14291 | 72,43843 | €1.145,69 | €3.437,06 | €50,62 | €-15,42 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 74,63707 | 74,97200 | 75,49210 | 99,14291 | 73,35453 | €1.473,95 | €4.421,85 | €50,66 | €-19,84 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07213 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €4,25 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 503,79000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-23,65 |
| Ampia 4H | EVAA | SHORT | Confluenza trend | 240m | 2,0x | 0,92491 | 0,81540 | 0,92491 | 1,38275 | 0,61414 | €208,21 | €416,41 | €0,00 | €49,31 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | VELVET | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,59490 | 0,59490 | 0,59646 | 0,30042 | 0,71431 | €277,68 | €555,36 | €0,00 | €0,00 |
| Forza relativa 1H | HYPE | SHORT | Forza relativa vs BTC | 60m | 2,0x | 63,33633 | 63,58800 | 64,50951 | 94,68781 | 60,75532 | €1.368,27 | €2.736,55 | €50,69 | €-10,87 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida 1H | VELVET | LONG | 2026-07-14T05:35:47+00:00 | 0,60448 | €15,27 | 0,30 | STOP |
| Rapida 1H | HYPE | SHORT | 2026-07-14T05:35:47+00:00 | 63,51717 | €14,59 | 0,29 | STOP |
| Ampia 4H | ALLO | LONG | 2026-07-14T03:20:27+00:00 | 0,41592 | €-51,45 | -1,01 | STOP |
| Principale 4H | ALLO | LONG | 2026-07-14T03:20:27+00:00 | 0,41592 | €-51,51 | -1,01 | STOP |
| Principale 4H | ZEC | LONG | 2026-07-13T21:06:38+00:00 | 492,06139 | €-51,21 | -1,02 | STOP |
| Forza relativa 1H | EVAA | SHORT | 2026-07-13T18:11:31+00:00 | 0,78053 | €-51,47 | -1,01 | STOP |
| Ampia 4H | LAB | SHORT | 2026-07-13T18:11:31+00:00 | 0,23085 | €139,52 | 2,79 | TARGET |
| Rapida 1H | EVAA | SHORT | 2026-07-13T18:11:31+00:00 | 0,77627 | €-50,73 | -1,01 | STOP |
| Rapida 1H | LAB | SHORT | 2026-07-13T18:11:31+00:00 | 0,28509 | €74,59 | 1,49 | TARGET |
| Bilanciata 1H | EVAA | SHORT | 2026-07-13T18:11:31+00:00 | 0,77627 | €-50,98 | -1,01 | STOP |
| Bilanciata 1H | LAB | SHORT | 2026-07-13T18:11:31+00:00 | 0,26423 | €99,79 | 1,99 | TARGET |
| Principale 4H | LAB | SHORT | 2026-07-13T18:11:31+00:00 | 0,26423 | €99,49 | 1,99 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07213**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 27.1 min | OK |
| Global DOGE | -5.0 | OK |
| Classic raw | -8.0 | OK |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 62579.88 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.07223**; close **0.07216**; wick alta **57.1%**; volume **x0.08**

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

- Regime: **RANGE**
- Famiglia: **RANGE**
- Confidenza: **80,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 0%, ADX 25.7.
- BTC trend score: **1,00**; ADX: **25,71**; breadth sopra EMA50: **0,00%**
- Mediana alt vs BTC: **-0,22%**; dispersione: **8,60%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **24**
- Trade research chiusi: **64**
- Eventi di mercato indipendenti chiusi: **34**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **121**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 4 | 6 | 6 | 33,33% | 0,98 | -0,02R | €-0,94 |
| SHADOW_1H_BALANCED | 6 | 20 | 20 | 30,00% | 0,78 | -0,16R | €-32,47 |
| SHADOW_1H_FAST | 3 | 23 | 23 | 26,09% | 0,49 | -0,40R | €-93,00 |
| SHADOW_4H_WIDE | 7 | 3 | 3 | 33,33% | 1,38 | 0,25R | €7,60 |
| SHADOW_RELATIVE_STRENGTH | 4 | 12 | 12 | 16,67% | 0,42 | -0,50R | €-60,29 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 4 | 6 | 6 | 33,33% | 0,98 | -0,02R | €-0,94 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 3 | 7 | 7 | 42,86% | 1,41 | 0,24R | €16,83 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 3 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,38 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 2 | 11 | 11 | 45,45% | 1,19 | 0,11R | €11,65 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 1 | 9 | 9 | 0,00% | 0,00 | -1,09R | €-98,53 |
| SHADOW_4H_WIDE | RANGE | 7 | 3 | 3 | 33,33% | 1,38 | 0,25R | €7,60 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 4 | 5 | 5 | 20,00% | 0,53 | -0,38R | €-19,14 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
