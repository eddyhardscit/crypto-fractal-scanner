# Paper trading automatico KuCoin

Generato: 2026-07-15T00:07:52+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-15T00:07:46+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-15T00:07:46+00:00 | 2026-07-15T00:07:46+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-14T23:45:00+00:00 | 2026-07-14T23:45:00+00:00 | 22,8 min | 40,0 min | OK |
| 60m | 12 | 2026-07-14T23:00:00+00:00 | 2026-07-14T23:00:00+00:00 | 1,13 h | 1,42 h | OK |
| 240m | 12 | 2026-07-14T20:00:00+00:00 | 2026-07-14T20:00:00+00:00 | 4,13 h | 4,42 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | 240m | LONG | 9,08 | 6,00 | 0,00 | RISK_GATE | 4,13 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ZEC | 240m | LONG | 8,25 | 6,00 | 0,00 | RISK_GATE | 4,13 h | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ETH | 240m | LONG | 7,16 | 6,00 | 0,00 | RISK_GATE | 4,13 h | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | RISK_GATE | 4,13 h | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | PEPE | 240m | LONG | 5,57 | 6,00 | 0,43 | BELOW_SCORE | 4,13 h | D: n/a | W: n/a | peso 0 | Punteggio +5.57; soglia ±6.00; mancano 0.43 punti. |
| Principale 4H | SUI | 240m | LONG | 5,10 | 6,00 | 0,90 | BELOW_SCORE | 4,13 h | D: n/a | W: n/a | peso 0 | Punteggio +5.10; soglia ±6.00; mancano 0.90 punti. |
| Principale 4H | EVAA | 240m | SHORT | -4,75 | 6,00 | 1,25 | BELOW_SCORE | 4,13 h | D: n/a | W: n/a | peso 0 | Punteggio -4.75; soglia ±6.00; mancano 1.25 punti. |
| Benchmark Donchian breakout 1H | LAB | 60m | SHORT | -9,25 | 5,00 | 0,00 | OPENED | 1,13 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Long 25 · €10 · 15x | LAB | 15m | LONG | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 22,8 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥30.0 in recupero. RSI 23.7→25.5; volume x2.03; shock 2.06 ATR. |
| Scalp RSI Long 25 · €50 · 15x | LAB | 15m | LONG | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 22,8 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥30.0 in recupero. RSI 23.7→25.5; volume x2.03; shock 2.06 ATR. |
| Scalp RSI Long 25 · prudente · 5x | LAB | 15m | LONG | 9,00 | 8,00 | 0,00 | STRATEGY_FILTER | 22,8 min | D: n/a | W: n/a | peso 0 | Filtro scalp RSI estremo: servono RSI estremo, shock, volume e conferma della candela successiva; manca: RSI ≥30.0 in recupero. RSI 23.7→25.5; volume x2.03; shock 2.06 ATR. |
| Rapida 1H | SUI | 60m | LONG | 6,11 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.82%. |
| Forza relativa 1H | SUI | 60m | LONG | 6,11 | 4,00 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+1.79%. |
| Rapida 1H | BTC | 60m | LONG | 5,58 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.64%. |
| Forza relativa 1H | BTC | 60m | LONG | 5,58 | 4,00 | 0,00 | STRATEGY_FILTER | 1,13 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+0.00%. |
| Rapida 1H | PEPE | 60m | LONG | 5,01 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.30%. |
| Forza relativa 1H | PEPE | 60m | LONG | 5,01 | 4,00 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+0.03%. |
| Rapida 1H | ETH | 60m | LONG | 4,81 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.09%. |
| Forza relativa 1H | XRP | 60m | LONG | 4,20 | 4,00 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.27%. |
| Bilanciata 1H | LAB | 60m | SHORT | -9,25 | 5,00 | 0,00 | RISK_GATE | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.982,39 | -0,18% | €-17,61 | €3.000,00 | -0,59% | 4 | 6 | 33,33% | 0,96 | 2,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 6 | 28 | CAMPIONE INSUFFICIENTE | 30 (mancano 24) |

- Trade del Principale 4H chiusi: **6**; win rate **33,33%**; profit factor **0,96**.
- Expectancy: **€-1,23** per trade; P&L netto: **€-7,37**; max drawdown: **2,86%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.982,39 | €1.796,43 | €5.389,28 | €199,43 | €-6,82 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.164,34 | €2.491,80 | €4.983,60 | €99,99 | €38,96 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.155,25 | €1.576,56 | €3.153,12 | €100,78 | €34,98 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.142,01 | €3.381,98 | €6.763,96 | €99,99 | €115,58 |
| TEST | Ampia 4H | 4 | €10.092,44 | €2.257,17 | €4.514,33 | €200,61 | €7,82 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Rapida 1H | 4 | €10.073,05 | €2.910,00 | €8.730,00 | €150,61 | €33,81 |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.997,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.995,92 | €1.562,50 | €3.125,00 | €50,00 | €-2,21 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.989,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.987,14 | €1.357,41 | €2.714,83 | €0,00 | €43,46 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.985,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.977,62 | €532,19 | €1.064,38 | €49,75 | €28,88 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.953,90 | €2.720,15 | €5.440,31 | €149,22 | €8,04 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.982,39 | €-7,37 | 6 | 6 | 33,33% | 0,96 | €-1,23 | 2,86% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.164,34 | €128,52 | 2 | 2 | 100,00% | ∞ | €64,26 | 0,25% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.155,25 | €122,29 | 1 | 1 | 100,00% | ∞ | €122,29 | 0,17% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.142,01 | €30,64 | 1 | 1 | 100,00% | ∞ | €30,64 | 0,25% |
| TEST | Ampia 4H | Confluenza trend | €10.092,44 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,51% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Rapida 1H | Momentum / breakout | €10.073,05 | €44,48 | 15 | 15 | 46,67% | 1,14 | €2,97 | 1,82% |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.997,11 | €-2,89 | 1 | 1 | 0,00% | 0,00 | €-2,89 | 0,03% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.995,92 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,04% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.989,21 | €-10,79 | 1 | 1 | 0,00% | 0,00 | €-10,79 | 0,11% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.987,14 | €-54,96 | 1 | 1 | 0,00% | 0,00 | €-54,96 | 0,48% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.985,56 | €-14,44 | 1 | 1 | 0,00% | 0,00 | €-14,44 | 0,14% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.977,62 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,51% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.953,90 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,68% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 63,85923 | 65,62100 | 66,45178 | 84,82634 | 58,67412 | €415,02 | €1.245,07 | €50,55 | €-34,35 |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64967,52000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €5,86 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 539,89796 | 561,87000 | 509,03713 | 362,63146 | 601,61962 | €290,77 | €872,31 | €49,86 | €35,50 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-13,83 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,28111 | 0,26153 | 0,28111 | 0,37341 | 0,23051 | €139,46 | €418,39 | €0,00 | €29,15 |
| Rapida 1H | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.004,95 | €3.014,86 | €50,14 | €4,66 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07438 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-36,14 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 561,87000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €50,30 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64967,52000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €4,55 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-10,89 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1865,88310 | 1889,85000 | 1831,70908 | 942,27097 | 1951,31818 | €1.364,99 | €2.729,97 | €50,00 | €35,07 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,26153 | 0,29286 | 0,39091 | 0,18303 | €211,57 | €423,15 | €50,78 | €-0,08 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.357,41 | €2.714,83 | €0,00 | €43,46 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64967,52000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €8,04 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1865,88310 | 1889,85000 | 1835,12648 | 942,27097 | 1927,39636 | €1.516,65 | €3.033,30 | €50,00 | €38,96 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28111 | 0,26153 | 0,28111 | 0,42027 | 0,21365 | €207,27 | €414,54 | €0,00 | €28,88 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1865,88310 | 1889,85000 | 1835,12648 | 942,27097 | 1933,54767 | €1.516,65 | €3.033,30 | €50,00 | €38,96 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 538,68772 | 561,87000 | 549,54167 | 272,03730 | 572,12052 | €890,18 | €1.780,35 | €0,00 | €76,62 |
| Global Confluence puro 1H | BTC | LONG | Global Confluence puro | 60m | 2,0x | 65013,44009 | 64967,52000 | 63973,22505 | 32831,78724 | 67613,97769 | €1.562,50 | €3.125,00 | €50,00 | €-2,21 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | ZEC | LONG | 2026-07-15T00:07:50+00:00 | 568,96736 | €97,88 | 1,95 | TARGET |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | 2026-07-15T00:07:50+00:00 | 1891,13532 | €-54,96 | -1,10 | STOP |
| Benchmark Donchian breakout 1H | ZEC | LONG | 2026-07-15T00:07:50+00:00 | 566,85249 | €122,29 | 2,45 | TARGET |
| Scalp RSI Short 75 · prudente · 5x | ZEC | SHORT | 2026-07-15T00:07:50+00:00 | 565,26797 | €-10,79 | -1,08 | STOP |
| Scalp RSI Short 75 · €50 · 15x | ZEC | SHORT | 2026-07-15T00:07:50+00:00 | 565,26797 | €-14,44 | -1,08 | STOP |
| Scalp RSI Short 75 · €10 · 15x | ZEC | SHORT | 2026-07-15T00:07:50+00:00 | 565,26797 | €-2,89 | -1,08 | STOP |
| Scanner Top 5 Long 1H | ZEC | LONG | 2026-07-14T19:58:20+00:00 | 537,68865 | €30,64 | 0,61 | STOP |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-07-14T19:58:20+00:00 | 537,68865 | €30,64 | 0,61 | STOP |
| Rapida 1H | PEPE | LONG | 2026-07-14T17:23:05+00:00 | 0,00000 | €-54,54 | -1,08 | STOP |
| Principale 4H | DOGE | SHORT | 2026-07-14T16:00:54+00:00 | 0,07452 | €-51,90 | -1,04 | STOP |
| Forza relativa 1H | HYPE | SHORT | 2026-07-14T14:14:01+00:00 | 64,52242 | €-54,29 | -1,07 | STOP |
| Rapida 1H | ETH | LONG | 2026-07-14T14:14:01+00:00 | 1825,87785 | €69,23 | 1,37 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07438**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 22.9 min | OK |
| Global DOGE | -1.0 | NO |
| Classic raw | 2.0 | NO |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64967.52 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation**
- High **0.07462**; close **0.07441**; wick alta **80.8%**; volume **x1.19**

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
- Confidenza: **84,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 92% sopra EMA50, ADX 25.7.
- BTC trend score: **4,00**; ADX: **25,65**; breadth sopra EMA50: **91,67%**
- Mediana alt vs BTC: **-0,12%**; dispersione: **7,14%**

- Aperti in questo ciclo: **5**
- Chiusi in questo ciclo: **2**
- Posizioni research aperte: **68**
- Trade research chiusi: **102**
- Eventi di mercato indipendenti chiusi: **53**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **234**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 7 | 9 | 9 | 22,22% | 0,55 | -0,36R | €-32,23 |
| RSI_EXTREME_SHORT_15M | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_1H_BALANCED | 9 | 29 | 29 | 27,59% | 0,69 | -0,24R | €-68,35 |
| SHADOW_1H_FAST | 8 | 31 | 31 | 25,81% | 0,47 | -0,41R | €-128,33 |
| SHADOW_4H_WIDE | 9 | 6 | 6 | 16,67% | 0,54 | -0,39R | €-23,42 |
| SHADOW_BOLLINGER_MR_1H | 2 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,87 |
| SHADOW_DONCHIAN_1H | 3 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_EMA_TREND_1H | 8 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_GLOBAL_PURE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 8 | 19 | 19 | 15,79% | 0,39 | -0,53R | €-101,09 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 1 | 1 | 100,00% | ∞ | 2,14R | €21,39 |
| SHADOW_SCANNER_TOP5_LONG | 6 | 1 | 1 | 100,00% | ∞ | 1,94R | €19,39 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 1 | 9 | 9 | 22,22% | 0,55 | -0,36R | €-32,23 |
| MAIN | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 2 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 2 | 14 | 14 | 35,71% | 1,03 | 0,02R | €2,86 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 1 | 8 | 8 | 0,00% | 0,00 | -1,08R | €-86,29 |
| SHADOW_1H_BALANCED | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 3 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 2 | 18 | 18 | 38,89% | 0,89 | -0,07R | €-12,99 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 1 | 9 | 9 | 0,00% | 0,00 | -1,09R | €-98,53 |
| SHADOW_1H_FAST | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_4H_WIDE | RANGE | 4 | 6 | 6 | 16,67% | 0,54 | -0,39R | €-23,42 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,16 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,70 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TREND_UP | 7 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 3 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 3 | 12 | 12 | 16,67% | 0,42 | -0,50R | €-59,95 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 1 | 1 | 100,00% | ∞ | 2,14R | €21,39 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 1 | 1 | 100,00% | ∞ | 1,94R | €19,39 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
